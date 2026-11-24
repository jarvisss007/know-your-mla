"""Parse a myneta candidate page: totals, immovable total, movable total (decoded from the
page's obfuscated script), liabilities, ITR income. Pure parsing; no network."""
import re, html, urllib.parse

def _base(d, e, f):
    g = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
    h = g[:e]; i = g[:f]
    j = sum(h.index(b) * e ** c for c, b in enumerate(reversed(d)) if b in h)
    k = ''
    while j > 0:
        k = i[j % f] + k; j //= f
    return k or '0'

def _unpack(hh, n, t, e):
    out = []; i = 0
    while i < len(hh):
        s = ''
        while hh[i] != n[e]:
            s += hh[i]; i += 1
        for j, ch in enumerate(n): s = s.replace(ch, str(j))
        out.append(chr(int(_base(s, e, 10)) - t)); i += 1
    r = ''.join(out)
    try: return r.encode('latin-1').decode('utf-8')
    except Exception: return r

PACK = re.compile(r'eval\(function\(h,u,n,t,e,r\).*?\}\("([^"]+)",(\d+),"([^"]+)",(\d+),(\d+),(\d+)\)\)', re.S)

def decoded(s):
    """Return page html with obfuscated script blocks replaced by their decoded output."""
    def rep(m):
        try:
            js = _unpack(m.group(1), m.group(3), int(m.group(4)), int(m.group(5)))
        except Exception:
            return m.group(0)
        # decoded script is usually document.write('...html...') possibly with escapes
        return js
    return PACK.sub(rep, s)

def text(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s)))

def rs(x):
    x = x.replace(',', '').strip()
    return int(x) if x.isdigit() else None

def last_rs(segment):
    """Final 'Rs N' in a totals row = the row's grand total column."""
    v = re.findall(r'Rs\s*([\d,]+)', segment)
    return rs(v[-1]) if v else None

def parse(raw):
    s = decoded(raw)
    t = text(s)
    d = {}
    m = re.search(r'Assets:\s*Rs\s*([\d,]+)', t); d['assets'] = rs(m.group(1)) if m else None
    m = re.search(r'Liabilities:\s*Rs\s*([\d,]+)', t); d['liabilities'] = rs(m.group(1)) if m else None
    if d['assets'] is None and re.search(r'Assets:\s*Nil', t): d['assets'] = 0
    if d['liabilities'] is None and re.search(r'Liabilities:\s*Nil', t): d['liabilities'] = 0
    # Movable section: between 'Details of Movable Assets' and 'Details of Immovable Assets'
    i = t.find('Details of Movable Assets'); j = t.find('Details of Immovable Assets')
    mov = t[i:j] if 0 <= i < j else ''
    imm = t[j:t.find('Details of Liabilities', j)] if j >= 0 else ''
    def tot(sec, label):
        k = sec.find(label)
        if k < 0: return None
        seg = sec[k:k + 400]
        seg = re.split(r'Totals Calculated|Totals \(Calculated|Disclaimer|Gross Total|Total Current|Data Readability', seg[len(label):])[0]
        return last_rs(seg) if 'Rs' in seg else (0 if re.fullmatch(r'[\sNil()a-zA-Z]*', seg) else None)
    d['movable_affidavit'] = tot(mov, 'Gross Total Value (as per Affidavit)') if mov else None
    d['movable_calc'] = tot(mov, 'Totals (Calculated as Sum of Values)') if mov else None
    d['immovable_affidavit'] = tot(imm, 'Total Current Market Value of (i) to (v) (as per Affidavit)')
    d['immovable_calc'] = tot(imm, 'Totals Calculated')
    k = t.find('Details of Liabilities'); lia = t[k:k + 20000] if k >= 0 else ''
    d['liab_affidavit'] = tot(lia, 'Total of Liabilities (as per affidavit)') if lia else None
    d['liab_calc'] = tot(lia, 'Totals (Calculated as Sum of Values)') if lia else None
    # ITR: latest year for self (first FY after 'self'), plus spouse
    k = t.find('Total Income Shown in ITR')
    itr = t[k:t.find('Data Readability Report of PAN', k)] if k >= 0 else ''
    d['itr_self_fy'] = d['itr_self'] = d['itr_spouse'] = None; d['itr_self_all'] = ''
    for who in ('self', 'spouse'):
        m = re.search(r'\b' + who + r'\b\s+[YN]\s+(.*?)(?=\b(?:self|spouse|huf|dependent\d)\b\s+[YN]\b|$)', itr)
        if not m: continue
        rows = re.findall(r'(\d{4}\s*-\s*\d{4})\s*\*\*\s*Rs\s*([\d,]+)', m.group(1))
        if not rows:
            rows = [(fy, v) for fy, v in re.findall(r'(\d{4}\s*-\s*\d{4})[^R]{0,40}Rs\s*([\d,]+)', m.group(1))]
        if rows:
            fy, v = rows[0]
            if who == 'self':
                d['itr_self_fy'] = fy.replace(' ', ''); d['itr_self'] = rs(v)
                d['itr_self_all'] = '; '.join(f"{a.replace(' ', '')}:{rs(b)}" for a, b in rows)
            else:
                d['itr_spouse'] = rs(v)
    fam, years = 0, set()
    for who in ('self', 'spouse', 'huf', 'dependent1', 'dependent2', 'dependent3'):
        m = re.search(r'\b' + who + r'\b\s+[YN]\s+(.*?)(?=\b(?:self|spouse|huf|dependent\d)\b\s+[YN]\b|$)', itr)
        if not m: continue
        for fy, v in re.findall(r'(\d{4}\s*-\s*\d{4})\s*\*\*\s*Rs\s*([\d,]+)', m.group(1)):
            fam += rs(v) or 0; years.add(fy.replace(' ', ''))
    d['itr_family_total'] = fam if years else None
    d['itr_years'] = ','.join(sorted(years))
    m = re.search(r'<title>([^<]+)', raw); d['title'] = m.group(1).strip() if m else ''
    return d
