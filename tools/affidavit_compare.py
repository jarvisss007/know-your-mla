"""Compare immovable-property declarations between two myneta affidavit pages of the same MLA.

Usage: python affidavit_compare.py PAIRS.csv RAW_2018_DIR RAW_2023_DIR OUT_DIR
PAIRS.csv needs columns: name, constituency, party, id18, id23.

Writes OUT_DIR/properties.csv (every parsed row) and OUT_DIR/flags.csv (matched plots whose
fixed facts changed between affidavits). A flag is a lead for a human to check against the
scanned originals, never a finding by itself: myneta is a transcription.
"""
import csv, html, pathlib, re, sys

OWNERS = ['self', 'spouse', 'dependent1', 'dependent2', 'dependent3']
ENTRY = re.compile(
    r'<span class=desc>(?P<loc>.*?)</span>\s*<br>\s*'
    r'<span class=desc>Total Area</span>\s*<span class=immov>(?P<area>.*?)</span>.*?'
    r'Whether Inherited\s*</span>\s*<span class=immov>(?P<inh>.*?)</span>.*?'
    r'Purchase Date\s*</span>\s*<span class=immov>(?P<date>.*?)</span>.*?'
    r'Purchase Cost\s*</span>\s*<span class=immov>(?P<cost>.*?)</span>.*?'
    r'Development Cost</span>\s*<span class=immov>(?P<dev>.*?)</span>\s*<br>\s*(?P<value>[\d,]+|Nil|0\*)?', re.S)

def clean(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()

def parse(path):
    s = pathlib.Path(path).read_text(errors='replace')
    i = s.find('id=immovable_assets')
    if i < 0: return []
    tbl = s[i:s.find('</table>', i)]
    rows = []
    for tr in re.findall(r'<tr valign=top>(.*?)</tr>', tbl, re.S):
        tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)
        if len(tds) < 3: continue
        cat = clean(tds[1])
        for owner, td in zip(OWNERS, tds[2:7]):
            for m in ENTRY.finditer(td):
                d = {k: clean(v or '') for k, v in m.groupdict().items()}
                d.update(category=cat, owner=owner)
                rows.append(d)
    return rows

def acres_options(a):
    """All plausible readings of an area string, in acres. '1.19 Acres' may mean 1 acre 19 guntas."""
    a = a.lower().replace(',', '')
    if not a or a in ('-', 'nil', '0'): return []
    out = []
    def f(x):
        try: return float(x)
        except ValueError: return None
    ac = re.search(r'([\d.]+)\s*(acre|ac\b|a\b)', a); gu = re.search(r'([\d.]+)\s*(gunta|g\b)', a)
    if ac or gu:
        A = f(ac.group(1)) if ac else 0.0; G = f(gu.group(1)) if gu else 0.0
        if A is None or G is None: return []
        out.append(A + G / 40)
        if ac and not gu and '.' in ac.group(1):
            whole, frac = ac.group(1).split('.', 1)
            if frac.isdigit() and int(frac) < 40: out.append(int(whole or 0) + int(frac) / 40)
        return out
    sqft = re.search(r'([\d.]+)\s*(sq\.?\s*ft|sft|square feet)', a); sqm = re.search(r'([\d.]+)\s*(sq\.?\s*m|square met)', a)
    ha = re.search(r'([\d.]+)\s*(hect|ha\b)', a)
    for m, k in ((sqft, 1 / 43560), (sqm, 1 / 4046.86), (ha, 2.47105)):
        if m and f(m.group(1)) is not None: out.append(f(m.group(1)) * k)
    return out

def survey_keys(loc):
    """Survey / RS / CTS / plot numbers in a location string, normalised: '290/1', '309/2b', '71'."""
    l = loc.lower().replace(' ', '')
    nums = re.findall(r'(?:sy|rs|survey|sno|s\.no|cts|no)\.?(?:no)?\.?([0-9]+(?:/[0-9a-z]+)*)', l)
    if not nums: nums = re.findall(r'\b([0-9]{1,4}(?:/[0-9a-z]+)+)\b', loc.lower())
    return frozenset(nums)

def money(s):
    s = s.replace(',', '')
    try: return float(s)
    except ValueError: return None

def diff(a, b):
    """Facts about a holding that should not change between affidavits."""
    why = []
    if a['inh'][:1] and b['inh'][:1] and a['inh'][:1] != b['inh'][:1]: why.append(f"inherited {a['inh']} -> {b['inh']}")
    da, db = a['date'], b['date']
    if da[:4].isdigit() and db[:4].isdigit() and da != db and not da.startswith('0000') and not db.startswith('0000'): why.append(f"purchase date {da} -> {db}")
    ca, cb = money(a['cost']), money(b['cost'])
    if ca is not None and cb is not None and max(ca, cb) > 0 and abs(ca - cb) > 0.01 * max(ca, cb): why.append(f"purchase cost {a['cost']} -> {b['cost']}")
    xa, xb = acres_options(a['area']), acres_options(b['area'])
    if xa and xb and not any(abs(u - v) <= 0.05 * max(u, v) for u in xa for v in xb): why.append(f"area {a['area']} -> {b['area']}")
    return why

def main(pairs, raw18, raw23, out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    props, flags = [], []
    for p in csv.DictReader(open(pairs)):
        r18 = parse(pathlib.Path(raw18) / f"{p['id18']}.html"); r23 = parse(pathlib.Path(raw23) / f"{p['id23']}.html")
        for yr, rows in (('2018', r18), ('2023', r23)):
            for r in rows: props.append({'mla': p['name'], 'year': yr, **r})
        # Candidate pairs share owner and the exact set of survey numbers. When a survey number
        # repeats (one survey split into several holdings), pair greedily by fewest differences,
        # and mark the pair ambiguous so a reviewer knows the pairing itself is a guess.
        cand = []
        for i, a in enumerate(r18):
            ka = survey_keys(a['loc'])
            if not ka: continue
            for j, b in enumerate(r23):
                if b['owner'] == a['owner'] and survey_keys(b['loc']) == ka:
                    cand.append((len(diff(a, b)), i, j))
        n18, n23 = {}, {}
        for _, i, j in cand: n18[i] = n18.get(i, 0) + 1; n23[j] = n23.get(j, 0) + 1
        used18, used23 = set(), set()
        for _, i, j in sorted(cand):
            if i in used18 or j in used23: continue
            used18.add(i); used23.add(j); a, b = r18[i], r23[j]
            why = diff(a, b)
            if why:
                flags.append({'mla': p['name'], 'party': p['party'], 'constituency': p['constituency'], 'owner': a['owner'],
                              'ambiguous_pairing': 'yes' if n18[i] > 1 or n23[j] > 1 else 'no',
                              'category': a['category'], 'loc_2018': a['loc'], 'loc_2023': b['loc'], 'changes': '; '.join(why),
                              'value_2018': a['value'], 'value_2023': b['value'],
                              'url_2018': f"https://www.myneta.info/karnataka2018/candidate.php?candidate_id={p['id18']}",
                              'url_2023': f"https://www.myneta.info/Karnataka2023/candidate.php?candidate_id={p['id23']}"})
    for name, rows in (('properties.csv', props), ('flags.csv', flags)):
        with open(out / name, 'w', newline='') as f:
            if rows:
                w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(f"{len(props)} property rows parsed; {len(flags)} matched plots flagged")

if __name__ == '__main__':
    main(*sys.argv[1:5])
