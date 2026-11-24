"""Step 1: match every current MLA (data/mlas.csv) to their 2023, 2018 and 2013 myneta affidavits.

Reads the cached myneta candidate listings (fetch_myneta.py ... listings 2023 2018 2013) and writes
CACHE/matches.json. Confidence:
  exact     same normalised name (case, dots, spacing, word order, titles ignored) and same seat
  probable  name variant (initials expanded/contracted, spelling variant, extra/missing word) in the same seat
  uncertain anything else worth a look (weak name similarity, same name in a different seat,
            or two same-seat candidates that fit equally well); never used in the rankings
Usage: py match_affidavits.py CACHE_DIR
"""
import csv, difflib, html, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import myneta_parse
ROOT = pathlib.Path(__file__).resolve().parents[2]
CACHE = pathlib.Path(sys.argv[1])
MAJOR = {'INC', 'BJP', 'JD(S)', 'JDS', 'Indian National Congress', 'Bharatiya Janata Party', 'Janata Dal (Secular)'}

def rs(cell):
    m = re.search(r'Rs&nbsp;([\d,]+)', cell)
    return int(m.group(1).replace(',', '')) if m else (0 if 'Nil' in cell else None)

def listing(year):
    rows, seen = [], set()
    for p in sorted((CACHE / f'list{year}').glob('p*.html'), key=lambda x: int(x.stem[1:])):
        s = myneta_parse.decoded(p.read_bytes().decode('utf-8', 'replace')).replace("\'", "'")
        for cid, name, seat, party, a, l in re.findall(
                r'<tr><td>\d+</td><td><a href=candidate\.php\?candidate_id=(\d+)>(.*?)</a>.*?</td><td>(.*?)</td>\s*<td>(.*?)</td>.*?<td align=right>(.*?)</td><td align=right>(.*?)</td>', s, re.S):
            if cid in seen: continue
            seen.add(cid)
            rows.append({'id': cid, 'name': html.unescape(name).strip(), 'seat': html.unescape(seat).strip(),
                         'party': html.unescape(party).strip(), 'assets': rs(a), 'liab': rs(l)})
    return rows

COMMON = {'kumar', 'gowda', 'gouda', 'patil', 'reddy', 'naik', 'nayak', 'shetty', 'singh', 'rao', 'swamy', 'appa',
          'manjunatha', 'manjunath', 'basavaraj', 'srinivas', 'srinivasa', 'ramesh', 'suresh', 'prakash', 'krishna', 'shivakumar',
          'nayaka', 'raju', 'murthy', 'babu', 'khan', 'ahmed', 'mohammed', 'lamani', 'devi', 'bai', 'gowdru', 'hegde', 'sharma', 'jain'}
TITLES = {'dr', 'adv', 'shri', 'sri', 'smt', 'prof', 'mr', 'mrs', 'ms', 'kum', 'alias', 'urf', 'urpha', 'er', 'capt', 'col'}

def toks(name):
    n = name.lower()
    n = re.sub(r'\(([^)]*)\)', r' \1 ', n)
    n = re.sub(r'[^a-z ]', ' ', n)
    t = [x for x in n.split() if x not in TITLES]
    return t

def compact(t):
    """Collapse runs of initials: ['d','k','shivakumar'] and ['dk','shivakumar'] both -> {'dk','shivakumar'}."""
    out, run = [], ''
    for x in t:
        if len(x) <= 2: run += x
        else:
            if run: out.append(run); run = ''
            out.append(x)
    if run: out.append(run)
    return out

def name_score(a, b):
    ta, tb = toks(a), toks(b)
    if not ta or not tb: return 'none', 0.0
    if sorted(ta) == sorted(tb) or sorted(compact(ta)) == sorted(compact(tb)) or ''.join(ta) == ''.join(tb):
        return 'exact', 1.0
    la = [x for x in ta if len(x) > 2]; lb = [x for x in tb if len(x) > 2]
    # pair each long token with its best counterpart
    def sim(x, y):
        r = difflib.SequenceMatcher(None, x, y).ratio()
        if min(len(x), len(y)) >= 4 and (x.startswith(y) or y.startswith(x)): r = max(r, 0.9)
        return r
    def best(x, pool): return max((sim(x, y) for y in pool), default=0)
    if la and lb:
        short, long_ = (la, lb) if len(la) <= len(lb) else (lb, la)
        cover = sum(best(x, long_) for x in short) / len(short)
        cover_min = min(best(x, long_) for x in short)
        # a word of the MLA's name that the affidavit name lacks (often the given name, so a
        # father or son with the family name would otherwise pass): never 'probable' on names alone
        mla_dropped = any(best(x, lb) < 0.85 for x in la)
    else:
        cover = cover_min = 0; mla_dropped = True
    whole = difflib.SequenceMatcher(None, ''.join(sorted(la)), ''.join(sorted(lb))).ratio()
    xa = ''.join(x for x in ta if len(x) <= 2); xb = ''.join(x for x in tb if len(x) <= 2)
    fa = ''.join(x[0] for x in ta); fb = ''.join(x[0] for x in tb)
    def within(xs, starts):
        st = list(starts)
        for ch in xs:
            if ch in st: st.remove(ch)
            else: return False
        return True
    if xa and xb:
        init_ok = sorted(xa) == sorted(xb) or within(xa, fb) and within(xb, fa)
        init_ok = init_ok and (set(xa) <= set(xb) or set(xb) <= set(xa))
    else:
        # one side spells the name out: its word starts must cover the other side's initials
        # (M B Patil = Mallanagoud Basanagoud Patil; H T Manju != Manjula)
        init_ok = within(xa, fb) and within(xb, fa)
    s = max(cover, whole)
    if init_ok and not mla_dropped and cover_min >= 0.85 and max(len(x) for x in short) >= 4: return 'probable', s
    if init_ok and not mla_dropped and whole >= 0.9: return 'probable', s
    distinctive = [x for x in short if x not in COMMON and best(x, long_) >= 0.85] if la and lb else []
    if s >= 0.72 or distinctive: return 'weak', s
    return 'none', s

def seat_key(s):
    s = re.sub(r'\((sc|st)\)', '', s.lower())
    return re.sub(r'[^a-z]', '', s)

# Seat spellings that differ between data/mlas.csv and myneta, or between myneta years.
SEAT_ALIAS = {
    'bijapurcity': ['vijayapuracity', 'bijapurcity', 'vijaypurcity'], 'gulbargauttar': ['gulbarganorth', 'kalaburagiuttar', 'gulbargauttar'],
    'gulbargadakshin': ['gulbargasouth', 'kalaburagidakshin'], 'gulbargarural': ['kalaburagirural'],
    'padmanabanagar': ['padmanabhanagar'], 'cvramannnagar': ['cvramannagar', 'cvramannanagar', 'sarvagnanagar_no'],
    'hublidharwadcentral': ['hublidharwadcentral', 'hubballidharwadcentral'], 'hublidharwadeast': ['hubballidharwadeast'],
    'kapu': ['kaup'], 'baindur': ['byndoor'], 'shrirangapattana': ['srirangapatna', 'srirangapattana'],
    'hublidharwadwest': ['hubballidharwadwest'], 'yemkanamardi': ['yamakanamardi', 'yemakanmardi', 'yamkanmardi'],
}

def seat_match(mla_seat, seats):
    """Best myneta seat (exact key, alias, else fuzzy >= 0.8) for a mlas.csv seat. Returns (seat, ratio)."""
    k = seat_key(mla_seat)
    keys = {seat_key(s): s for s in seats}
    for cand in [k] + SEAT_ALIAS.get(k, []):
        if cand in keys: return keys[cand], 1.0
    best = max(keys, key=lambda x: difflib.SequenceMatcher(None, k, x).ratio())
    r = difflib.SequenceMatcher(None, k, best).ratio()
    return (keys[best], r) if r >= 0.8 else (None, r)

def pick(mla, rows, seat, expect_assets=None):
    """Return (row, confidence, note, alternatives)."""
    insame = [r for r in rows if seat and r['seat'] == seat]
    scored = [(name_score(mla['name'], r['name']), r) for r in insame]
    ex = [r for (k, _), r in scored if k == 'exact']
    pr = sorted([(s, r) for (k, s), r in scored if k == 'probable'], key=lambda x: -x[0])
    wk = sorted([(s, r) for (k, s), r in scored if k == 'weak'], key=lambda x: -x[0])
    def corroborate(r):
        if expect_assets and r['assets'] and abs(r['assets'] / 1e7 - expect_assets) <= 0.011: return ' 2018 total equals the site\'s existing 2018 figure.'
        return ''
    if len(ex) == 1:
        return ex[0], 'exact', 'same name, same seat.' + corroborate(ex[0]), []
    if len(ex) > 1:
        maj = [r for r in ex if r['party'] in MAJOR]
        if len(maj) == 1:
            return maj[0], 'probable', f'{len(ex)} same-name candidates in the seat (namesakes); took the {maj[0]["party"]} one.' + corroborate(maj[0]), [r for r in ex if r is not maj[0]]
        return ex[0], 'uncertain', f'{len(ex)} same-name candidates in the seat; cannot tell which.', ex[1:]
    if pr:
        top = pr[0][1]
        rest = [r for s, r in pr[1:]]
        if rest and pr[1][0] >= pr[0][0] - 0.03:
            return top, 'uncertain', 'two name variants in the seat fit about equally.', rest
        return top, 'probable', f'name variant ("{top["name"]}"), same seat.' + corroborate(top), rest
    # statewide: same name elsewhere (seat change)
    far = [r for r in rows if r['seat'] != seat and name_score(mla['name'], r['name'])[0] == 'exact']
    if far:
        far.sort(key=lambda r: (r['party'] not in MAJOR, -(r['assets'] or 0)))
        return far[0], 'uncertain', f'same name but different seat ({far[0]["seat"]}); may have changed seat, may be a namesake.', far[1:4]
    if wk:
        return wk[0][1], 'uncertain', f'only a weak name resemblance in the seat ("{wk[0][1]["name"]}").', [r for s, r in wk[1:3]]
    return None, 'none', 'no candidate with this or a similar name in the seat or statewide.', []

def main():
    mlas = list(csv.DictReader(open(ROOT / 'data' / 'mlas.csv', encoding='utf-8')))
    L = {y: listing(y) for y in ('2023', '2018', '2013')}
    byid23 = {r['id']: r for r in L['2023']}
    seats = {y: sorted({r['seat'] for r in L[y]}) for y in L}
    out, seatlog = [], []
    for m in mlas:
        rec = {'name': m['name'], 'constituency': m['constituency'], 'party': m['party'], 'election': m['election'],
               'mlas_id': m['myneta_candidate_id'], 'assets_crore_2018_site': m['assets_crore_2018']}
        # 2023 (or the by-election that elected the sitting MLA)
        s23, r23 = seat_match(m['constituency'], seats['2023'])
        if m['myneta_candidate_id']:
            row = byid23.get(m['myneta_candidate_id'])
            rec['y2023'] = {'id': m['myneta_candidate_id'], 'confidence': 'exact', 'note': 'id already in data/mlas.csv.',
                            **({'name': row['name'], 'seat': row['seat'], 'party': row['party']} if row else {})}
            if row: s23 = row['seat']
        else:
            r, c, note, alt = pick(m, L['2023'], s23)
            rec['y2023'] = {'id': r['id'] if r else '', 'confidence': c, 'note': note, 'name': r['name'] if r else '',
                            'seat': r['seat'] if r else '', 'party': r['party'] if r else '',
                            'alternatives': [{'id': a['id'], 'name': a['name'], 'seat': a['seat'], 'party': a['party']} for a in alt]}
        for y in ('2018', '2013'):
            sy, ry = seat_match(s23 or m['constituency'], seats[y])
            if not sy: sy, ry = seat_match(m['constituency'], seats[y])
            seatlog.append((m['constituency'], s23, y, sy, round(ry, 2)))
            exp = float(m['assets_crore_2018']) if y == '2018' and m['assets_crore_2018'] else None
            r, c, note, alt = pick(m, L[y], sy, exp)
            rec['y' + y] = {'id': r['id'] if r else '', 'confidence': c, 'note': note, 'name': r['name'] if r else '',
                            'seat': r['seat'] if r else '', 'party': r['party'] if r else '', 'seat_used': sy or '',
                            'alternatives': [{'id': a['id'], 'name': a['name'], 'seat': a['seat'], 'party': a['party']} for a in alt]}
        out.append(rec)
    json.dump({'matches': out, 'listing_counts': {y: len(L[y]) for y in L}}, open(CACHE / 'matches.json', 'w'), indent=1)
    with open(CACHE / 'seatlog.csv', 'w', newline='') as f:
        csv.writer(f).writerows([('mla_seat', 'seat2023', 'year', 'seat_used', 'ratio')] + seatlog)
    from collections import Counter
    for y in ('2023', '2018', '2013'):
        print(y, 'listing', len(L[y]), Counter(r['y' + y]['confidence'] for r in out))

if __name__ == '__main__':
    main()
