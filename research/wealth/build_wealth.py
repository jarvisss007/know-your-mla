"""Step 3: reconcile matches with myneta\'s grouping, fetch matched 2018/2013 affidavits, parse, compute,
write affidavits_2013_2018_2023.csv, MATCH_REVIEW.csv and CACHE/summary.json (numbers for the findings).
Usage: py build_wealth.py CACHE_DIR [--no-fetch]
"""
import csv, json, pathlib, statistics, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import fetch_myneta, myneta_parse

CACHE = pathlib.Path(sys.argv[1]); FETCH = '--no-fetch' not in sys.argv
M = json.load(open(CACHE / 'matches.json'))['matches']
G = json.load(open(CACHE / 'groups.json'))
L = {}
import match_affidavits as MA  # reuses listing() (module reads sys.argv[1] = CACHE)
for y in ('2023', '2018', '2013'):
    L[y] = {r['id']: r for r in MA.listing(y)}
SITE = {(r['name'], r['constituency']): r for r in csv.DictReader(open(ROOT / 'data' / 'mlas.csv', encoding='utf-8'))}
URL = {'2023': 'https://www.myneta.info/Karnataka2023/candidate.php?candidate_id={}',
       '2018': 'https://www.myneta.info/Karnataka2018/candidate.php?candidate_id={}',
       '2013': 'https://www.myneta.info/Karnataka2013/candidate.php?candidate_id={}'}
USE = ('exact', 'probable')

# ---- reconcile name+seat matches with myneta\'s own cross-election grouping
def alt_of(c): return {k: c.get(k) for k in ('id', 'name', 'seat', 'party')}

for m in M:
    g = G.get(m['y2023'].get('id') or '', {})
    for y in ('2018', '2013'):
        r = m['y' + y]
        linked = [l['id'] for l in g.get('links', []) if l['folder'] == 'karnataka' + y]
        gen = [L[y][i] for i in linked if i in L[y]]          # general-election affidavits
        bye = [i for i in linked if i not in L[y]]             # by-elections filed in the same myneta folder
        r['myneta_links'] = linked
        bye_note = (f' myneta also links by-election affidavit(s) {", ".join(bye)} in its {y} folder (filed between general elections; not used).' if bye else '')
        r['note'] += bye_note
        if not g.get('group'):
            r['myneta_grouping'] = 'no grouping page'
        elif r['id'] and r['id'] in [c['id'] for c in gen]:
            r['myneta_grouping'] = 'agrees'
            if r['confidence'] == 'uncertain' and r.get('seat') == r.get('seat_used'):
                r['confidence'] = 'probable'
                r['note'] = f'name variant ("{r["name"]}"), same seat; myneta\'s own grouping links the same affidavit.' + bye_note
            elif r['confidence'] == 'uncertain':
                r['note'] += ' myneta\'s own grouping links this affidavit too.'
        elif gen:
            same = [c for c in gen if c['seat'] == r.get('seat_used')]
            c = (same or gen)[0]
            k = MA.name_score(m['name'], c['name'])[0]
            if r['confidence'] in ('exact', 'probable'):
                r['myneta_grouping'] = 'links a different affidavit'
                r['alternatives'] = [alt_of(c)] + r.get('alternatives', [])
                r['note'] += f' But myneta groups this MLA with a different {y} affidavit ("{c["name"]}", {c["seat"]}, id {c["id"]}).'
                r['confidence'] = 'uncertain'
            else:
                if r.get('id'): r['alternatives'] = [alt_of(r)] + r.get('alternatives', [])
                same_seat = c['seat'] == r.get('seat_used')
                conf = 'probable' if same_seat and k in ('exact', 'probable', 'weak') else 'uncertain'
                r['myneta_grouping'] = 'only myneta links one'
                why = ('name variant, same seat; found through myneta\'s own grouping' if conf == 'probable' else
                       f'found only through myneta\'s grouping; ' + ('different seat' if not same_seat else 'names barely alike'))
                r.update(id=c['id'], name=c['name'], seat=c['seat'], party=c['party'], confidence=conf,
                         note=f'{why} ("{c["name"]}", {c["seat"]}).' + bye_note)
        else:
            r['myneta_grouping'] = 'no link' if r.get('id') else 'no link, no match'

# ---- fetch and parse detail pages
need = {y: sorted({m['y' + y]['id'] for m in M if m['y' + y].get('id') and m['y' + y]['confidence'] in USE + ('uncertain',)}) for y in ('2023', '2018', '2013')}
P = {}
for y in ('2023', '2018', '2013'):
    if FETCH:
        fetch_myneta.details(CACHE, y, need[y])
    for cid in need[y]:
        p = CACHE / f'cand{y}' / f'{cid}.html'
        P[(y, cid)] = myneta_parse.parse(p.read_bytes().decode('utf-8', 'replace')) if p.exists() else None

def cr(x): return None if x is None else round(x / 1e7, 4)

def pick_val(d, a, c):
    """Affidavit-stated total, else the calculated sum."""
    if not d: return None
    return d[a] if d[a] is not None else d[c]

def split(d):
    """Movable and immovable totals. Prefer the affidavit's stated totals; where a stated total is
    missing or nil but the rows add up to something, use the row sum. Among the choices, take the
    pair that reproduces myneta\'s headline total (which is movable + immovable)."""
    if not d: return None, None
    mo = [v for v in (d['movable_affidavit'], d['movable_calc']) if v is not None]
    im = [v for v in (d['immovable_affidavit'], d['immovable_calc']) if v is not None]
    if not mo and not im: return None, None
    mo = mo or [0]; im = im or [0]
    a = d['assets']
    if a is None: return mo[0], im[0]
    best = min(((abs(a - x - y), i + j, x, y) for i, x in enumerate(mo) for j, y in enumerate(im)))
    return best[2], best[3]

rows, review, adds = [], [], []
for m in M:
    out = {'name': m['name'], 'constituency': m['constituency'], 'party_now': m['party'], 'elected_in': m['election']}
    for y in ('2023', '2018', '2013'):
        r = m['y' + y]; d = P.get((y, r.get('id'))) if r.get('id') else None
        out[f'match_{y}'] = r['confidence'] if r.get('id') or r['confidence'] != 'none' else 'none'
        if y == '2023' and m['mlas_id']: out['match_2023'] = 'exact'
        out[f'myneta_id_{y}'] = r.get('id', '')
        out[f'name_on_affidavit_{y}'] = r.get('name', '')
        out[f'seat_{y}'] = r.get('seat', '')
        out[f'party_{y}'] = r.get('party', '')
        if y != '2023': out[f'myneta_grouping_{y}'] = r.get('myneta_grouping', '')
        out[f'match_note_{y}'] = r.get('note', '')
        a = d['assets'] if d else None; l = d['liabilities'] if d else None
        mov, imm = split(d)
        if y == '2023' and not d and SITE[(m['name'], m['constituency'])]['assets_crore']:
            # e.g. K. J. George: not analysed on myneta; site figure from opencity, no breakdown
            a = float(SITE[(m['name'], m['constituency'])]['assets_crore']) * 1e7
            l = float(SITE[(m['name'], m['constituency'])]['liabilities_crore']) * 1e7 if SITE[(m['name'], m['constituency'])]['liabilities_crore'] else None
            out['match_note_2023'] += ' Totals from data/mlas.csv (' + (SITE[(m['name'], m['constituency'])]['source_url'] or 'site') + '); no myneta page, no breakdown.'
        out[f'assets_cr_{y}'] = cr(a); out[f'liabilities_cr_{y}'] = cr(l)
        out[f'movable_cr_{y}'] = cr(mov); out[f'immovable_cr_{y}'] = cr(imm)
        out[f'itr_self_latest_fy_{y}'] = d['itr_self_fy'] if d else ''
        out[f'itr_self_latest_lakh_{y}'] = round(d['itr_self'] / 1e5, 2) if d and d['itr_self'] is not None else ''
        out[f'itr_spouse_latest_lakh_{y}'] = round(d['itr_spouse'] / 1e5, 2) if d and d['itr_spouse'] is not None else ''
        out[f'itr_family_5yr_lakh_{y}'] = round(d['itr_family_total'] / 1e5, 2) if d and d.get('itr_family_total') else ''
        out[f'itr_years_{y}'] = d.get('itr_years', '') if d else ''
        # add-up checks
        chk = []
        if d:
            if a and mov is not None and imm is not None and abs(a - (mov + imm)) > max(0.01 * a, 1e5):
                chk.append(f'{y}: total assets {cr(a)} cr != movable {cr(mov)} + immovable {cr(imm)}')
            for lab, x, c in (('movable', d['movable_affidavit'], d['movable_calc']), ('immovable', d['immovable_affidavit'], d['immovable_calc']),
                              ('liabilities', d['liab_affidavit'], d['liab_calc'])):
                if x is not None and c is not None and abs(x - c) > max(0.10 * max(x, c), 1e7):
                    chk.append(f'{y}: {lab} stated {cr(x)} cr vs rows add to {cr(c)} cr')
        out[f'addup_{y}'] = '; '.join(chk)
        out[f'url_{y}'] = URL[y].format(r['id']) if r.get('id') and d else ''
        if r['confidence'] in ('uncertain',) or (y != '2023' and r['confidence'] == 'none' and r.get('myneta_links')):
            review.append({'mla': m['name'], 'constituency': m['constituency'], 'party_now': m['party'], 'year': y,
                           'candidate_found': r.get('name', ''), 'seat_found': r.get('seat', ''), 'party_then': r.get('party', ''),
                           'myneta_id': r.get('id', ''), 'assets_cr': cr(a), 'why_uncertain': r.get('note', ''),
                           'myneta_grouping': r.get('myneta_grouping', ''),
                           'other_candidates': '; '.join(f"{x['name']} ({x['seat']}, {x['party']}, id {x['id']})" for x in r.get('alternatives', [])),
                           'url': URL[y].format(r['id']) if r.get('id') else '',
                           'reviewer_decision (same person? yes/no)': ''})
    rows.append(out)

json.dump({'rows': rows, 'review': review}, open(CACHE / 'built.json', 'w'), indent=1)
print('rows', len(rows), 'review', len(review))
