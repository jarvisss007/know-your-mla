"""Step 4: growth, composition, income test, add-up checks and party medians.
Reads CACHE/built.json (build_wealth.py); writes affidavits_2013_2018_2023.csv, MATCH_REVIEW.csv
and CACHE/summary.json (all numbers quoted in FINDINGS_DRAFT.md).
Usage: py analyze.py CACHE_DIR
"""
import csv, json, pathlib, statistics, sys
HERE = pathlib.Path(__file__).resolve().parent
CACHE = pathlib.Path(sys.argv[1])
B = json.load(open(CACHE / 'built.json'))
rows, review = B['rows'], B['review']
USE = ('exact', 'probable')
PCT_FLOOR = 1.0  # crore: percentage rankings only for a starting total of at least Rs 1 crore

def ok(r, y):
    if r[f'assets_cr_{y}'] is None: return False
    return r[f'match_{y}'] in USE

def num(x): return x if isinstance(x, (int, float)) else None

def comp(dm, di):
    if dm is None or di is None: return 'no breakdown'
    tot = dm + di
    if tot == 0: return 'no change'
    if tot > 0:
        if di >= 0.6 * tot: return 'mostly immovable'
        if dm >= 0.6 * tot: return 'mostly movable'
        return 'mixed'
    if di <= 0.6 * tot: return 'mostly immovable (fall)'
    if dm <= 0.6 * tot: return 'mostly movable (fall)'
    return 'mixed (fall)'

for r in rows:
    for a, b in (('2013', '2018'), ('2018', '2023'), ('2013', '2023')):
        k = f'{a}_{b}'
        if ok(r, a) and ok(r, b):
            A, Bv = r[f'assets_cr_{a}'], r[f'assets_cr_{b}']
            r[f'growth_cr_{k}'] = round(Bv - A, 2)
            r[f'growth_pct_{k}'] = round(100 * (Bv - A) / A, 1) if A > 0 else None
            ma, mb, ia, ib = (r.get(f'movable_cr_{a}'), r.get(f'movable_cr_{b}'), r.get(f'immovable_cr_{a}'), r.get(f'immovable_cr_{b}'))
            dm = round(mb - ma, 2) if ma is not None and mb is not None else None
            di = round(ib - ia, 2) if ia is not None and ib is not None else None
            r[f'movable_change_cr_{k}'] = dm; r[f'immovable_change_cr_{k}'] = di
            r[f'composition_{k}'] = comp(dm, di)
            la, lb = r[f'liabilities_cr_{a}'], r[f'liabilities_cr_{b}']
            r[f'liabilities_change_cr_{k}'] = round(lb - la, 2) if la is not None and lb is not None else None
            r[f'networth_change_cr_{k}'] = round((Bv - (lb or 0)) - (A - (la or 0)), 2) if la is not None and lb is not None else None
        else:
            for f in ('growth_cr', 'growth_pct', 'movable_change_cr', 'immovable_change_cr', 'composition', 'liabilities_change_cr', 'networth_change_cr'):
                r[f'{f}_{k}'] = None
    # income test, 2018 -> 2023 only: the 2023 affidavit lists five years of ITR income (FY2018-19..2022-23)
    inc = num(r.get('itr_family_5yr_lakh_2023'))
    r['family_itr_income_cr_2023_affidavit'] = round(inc / 100, 2) if inc is not None else None
    r['income_test_2018_2023'] = ''
    nw, dm, dl = r['networth_change_cr_2018_2023'], r['movable_change_cr_2018_2023'], r['liabilities_change_cr_2018_2023']
    if nw is not None and r['family_itr_income_cr_2023_affidavit'] is not None:
        I = r['family_itr_income_cr_2023_affidavit']
        if nw >= 2 * I and nw - I >= 5.0 and len((r.get('itr_years_2023') or '').split(',')) >= 4:
            t = (f'growth larger than declared income would suggest: net worth up {nw} cr against {I} cr of family income in the five ITRs; '
                 'affidavits value land differently across years')
            if dm is not None and dl is not None and dm - max(dl, 0) > I:
                t += '; the rise in movable assets alone, net of new borrowing, also exceeds that income'
            r['income_test_2018_2023'] = t
        elif len((r.get('itr_years_2023') or '').split(',')) < 4:
            r['income_test_2018_2023'] = 'not tested: the 2023 affidavit lists fewer than four years of ITR income'
        else:
            r['income_test_2018_2023'] = 'within declared income' if nw <= I else 'above declared income, but not clearly (margin small)'
    r['addup_any'] = ' | '.join(x for x in (r['addup_2013'], r['addup_2018'], r['addup_2023']) if x)

def rank(key, n=20, reverse=True, floor_key=None):
    c = [r for r in rows if r[key] is not None and (floor_key is None or r[floor_key] >= PCT_FLOOR)]
    c.sort(key=lambda r: r[key], reverse=reverse)
    return c[:n]

R = {
    'abs_2018_2023': rank('growth_cr_2018_2023'),
    'pct_2018_2023': rank('growth_pct_2018_2023', floor_key='assets_cr_2018'),
    'abs_2013_2023': rank('growth_cr_2013_2023'),
    'pct_2013_2023': rank('growth_pct_2013_2023', floor_key='assets_cr_2013'),
    'fall_2018_2023': [r for r in rank('growth_cr_2018_2023', 20, reverse=False) if r['growth_cr_2018_2023'] < 0],
    'fall_2013_2023': [r for r in rank('growth_cr_2013_2023', 20, reverse=False) if r['growth_cr_2013_2023'] < 0],
}
for k, lst in R.items():
    for i, r in enumerate(lst, 1): r[f'rank_{k}'] = i

def med(v):
    v = [x for x in v if x is not None]
    return round(statistics.median(v), 2) if v else None

parties = {}
for p in sorted({r['party_now'] for r in rows}) + ['ALL']:
    rs = [r for r in rows if p == 'ALL' or r['party_now'] == p]
    both = [r for r in rs if r['growth_cr_2018_2023'] is not None]
    both13 = [r for r in rs if r['growth_cr_2013_2023'] is not None]
    parties[p] = {
        'mlas': len(rs),
        'median_assets_2023_cr': med([r['assets_cr_2023'] for r in rs if r['assets_cr_2023'] is not None]),
        'n_2018_2023': len(both),
        'median_assets_2018_cr': med([r['assets_cr_2018'] for r in both]),
        'median_assets_2023_cr_same_mlas': med([r['assets_cr_2023'] for r in both]),
        'median_growth_cr_2018_2023': med([r['growth_cr_2018_2023'] for r in both]),
        'median_growth_pct_2018_2023': med([r['growth_pct_2018_2023'] for r in both]),
        'median_movable_change_cr_2018_2023': med([r['movable_change_cr_2018_2023'] for r in both]),
        'median_immovable_change_cr_2018_2023': med([r['immovable_change_cr_2018_2023'] for r in both]),
        'n_fell_2018_2023': sum(1 for r in both if r['growth_cr_2018_2023'] < 0),
        'n_income_flag': sum(1 for r in both if r['income_test_2018_2023'].startswith('growth larger')),
        'n_2013_2023': len(both13),
        'median_growth_cr_2013_2023': med([r['growth_cr_2013_2023'] for r in both13]),
        'median_growth_pct_2013_2023': med([r['growth_pct_2013_2023'] for r in both13]),
        'composition_2018_2023': {c: sum(1 for r in both if r['composition_2018_2023'] == c) for c in
                                  ('mostly immovable', 'mostly movable', 'mixed', 'mostly immovable (fall)', 'mostly movable (fall)', 'mixed (fall)', 'no breakdown', 'no change')},
    }

from collections import Counter
summary = {
    'match_counts': {y: dict(Counter(r[f'match_{y}'] for r in rows)) for y in ('2023', '2018', '2013')},
    'grouping_counts': {y: dict(Counter(r[f'myneta_grouping_{y}'] for r in rows if r[f'match_{y}'] in USE)) for y in ('2018', '2013')},
    'n_review': len(review),
    'rankings': {k: [{f: r.get(f) for f in ('name', 'constituency', 'party_now', 'party_2018', 'party_2013', 'assets_cr_2013', 'assets_cr_2018', 'assets_cr_2023',
                                              'growth_cr_2018_2023', 'growth_pct_2018_2023', 'growth_cr_2013_2023', 'growth_pct_2013_2023',
                                              'movable_change_cr_2018_2023', 'immovable_change_cr_2018_2023', 'composition_2018_2023',
                                              'movable_change_cr_2013_2023', 'immovable_change_cr_2013_2023', 'composition_2013_2023',
                                              'liabilities_change_cr_2018_2023', 'networth_change_cr_2018_2023',
                                              'family_itr_income_cr_2023_affidavit', 'itr_years_2023', 'income_test_2018_2023',
                                              'itr_self_latest_lakh_2023', 'itr_self_latest_fy_2023', 'match_2018', 'match_2013', 'addup_any')}
                     for r in lst] for k, lst in R.items()},
    'parties': parties,
    'addup': [{'name': r['name'], 'constituency': r['constituency'], 'party_now': r['party_now'], 'issues': r['addup_any'],
               'used_years': [y for y in ('2013', '2018', '2023') if r[f'addup_{y}'] and (y == '2023' or r[f'match_{y}'] in USE)]}
              for r in rows if r['addup_any']],
    'income_flags': [{'name': r['name'], 'constituency': r['constituency'], 'party_now': r['party_now'], 'nw': r['networth_change_cr_2018_2023'],
                      'income': r['family_itr_income_cr_2023_affidavit'], 'growth': r['growth_cr_2018_2023'], 'composition': r['composition_2018_2023'],
                      'text': r['income_test_2018_2023']} for r in rows if r['income_test_2018_2023'].startswith('growth larger')],
    'party_switch_2018_2023': sum(1 for r in rows if r['match_2018'] in USE and r['party_2018'] and
                                  {'INC': 'Congress', 'BJP': 'BJP', 'JD(S)': 'JD(S)'}.get(r['party_2018'], r['party_2018']) != r['party_now']),
}
json.dump(summary, open(CACHE / 'summary.json', 'w'), indent=1)

# ---- CSVs
cols = ['name', 'constituency', 'party_now', 'elected_in']
for y in ('2023', '2018', '2013'):
    cols += [f'match_{y}', f'myneta_id_{y}', f'name_on_affidavit_{y}', f'seat_{y}', f'party_{y}'] + ([f'myneta_grouping_{y}'] if y != '2023' else []) + [
        f'match_note_{y}', f'assets_cr_{y}', f'liabilities_cr_{y}', f'movable_cr_{y}', f'immovable_cr_{y}',
        f'itr_self_latest_fy_{y}', f'itr_self_latest_lakh_{y}', f'itr_spouse_latest_lakh_{y}', f'itr_family_5yr_lakh_{y}', f'itr_years_{y}',
        f'addup_{y}', f'url_{y}']
for k in ('2013_2018', '2018_2023', '2013_2023'):
    cols += [f'growth_cr_{k}', f'growth_pct_{k}', f'movable_change_cr_{k}', f'immovable_change_cr_{k}', f'composition_{k}',
             f'liabilities_change_cr_{k}', f'networth_change_cr_{k}']
cols += ['family_itr_income_cr_2023_affidavit', 'income_test_2018_2023'] + [f'rank_{k}' for k in R]
with open(HERE / 'affidavits_2013_2018_2023.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore'); w.writeheader()
    for r in sorted(rows, key=lambda r: r['name']):
        w.writerow({k: ('' if r.get(k) is None else r.get(k)) for k in cols})
with open(HERE / 'MATCH_REVIEW.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(review[0])); w.writeheader()
    w.writerows(sorted(review, key=lambda r: (r['year'], r['mla'])))
print(json.dumps(summary['match_counts']), 'review', len(review), 'income flags', len(summary['income_flags']), 'addup', len(summary['addup']))
