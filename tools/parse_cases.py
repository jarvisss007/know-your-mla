"""Parse 'Cases where Pending' and 'Cases where Convicted' tables from myneta 2023 pages into data/cases.csv."""
import csv, html, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build' / 'raw'
mlas = {r['myneta_candidate_id']: r for r in csv.DictReader(open(ROOT / 'data' / 'mlas.csv')) if r['myneta_candidate_id']}
def cells(tr): return [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', c))).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)]
def table_after(s, title):
    i = s.find(f'<h3>{title}</h3>')
    if i < 0: return []
    j = s.find('</table>', i); return re.findall(r'<tr[^>]*>(.*?)</tr>', s[i:j], re.S)
rows = []
for cid, m in mlas.items():
    p = RAW / f'{cid}.html'
    if not p.exists(): continue
    s = p.read_text(errors='replace')
    for kind in ('Pending', 'Convicted'):
        for tr in table_after(s, f'Cases where {kind}'):
            c = cells(tr)
            if len(c) < 6 or not c[0].strip().isdigit(): continue
            c += [''] * (10 - len(c))
            rows.append({'mla': m['name'], 'constituency': m['constituency'], 'party': m['party'], 'myneta_id': cid, 'kind': kind,
                         'fir_no': c[1], 'case_no': c[2], 'court': c[3], 'ipc': c[4], 'other_acts': c[5],
                         'charges_framed': c[6], 'charges_date': c[7], 'appeal_filed': c[8], 'appeal_status': c[9]})
out = ROOT / 'data' / 'cases.csv'
with open(out, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), 'case rows from', len({r['myneta_id'] for r in rows}), 'MLAs ->', out)
