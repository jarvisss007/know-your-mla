# Map each of the 224 MLAs to a district using the Wikipedia constituency table (district = ECI/CEO list).
import io, json, re, sys, difflib
wiki, data, out = sys.argv[1:4]
lines = io.open(wiki, encoding='utf-8').read().split('\n')
acs = []           # (num, name, district)
cur = None; dist = None; left = 0
for i, ln in enumerate(lines):
    m = re.match(r'^!\s*(\d{1,3})\s*$', ln)
    if m:
        num = int(m.group(1))
        nm = re.match(r'^\|\s*\[\[[^|\]]*\|([^\]]+)\]\]', lines[i + 1])
        if not nm: continue
        name = nm.group(1).strip()
        nxt = lines[i + 2]
        dm = re.match(r'^\|\s*rowspan="(\d+)"\s*\|\s*\[\[[^|\]]*\|([^\]]+)\]\]', nxt)
        if dm and 'district' in nxt.lower():
            dist = dm.group(2).strip(); left = int(dm.group(1))
        elif left <= 0:
            d1 = re.match(r'^\|\s*\[\[([^|\]]*district)[^|\]]*\|([^\]]+)\]\]', nxt)
            if d1: dist = d1.group(2).strip(); left = 1
        acs.append((num, name, dist)); left -= 1
acs = [a for a in acs if a[0] <= 224]
seen = {}
for a in acs: seen[a[0]] = a
acs = [seen[k] for k in sorted(seen)]
print('constituencies parsed', len(acs), 'districts', len(set(a[2] for a in acs)))

def norm(s):
    s = s.lower().replace('(sc)', '').replace('(st)', '')
    s = s.replace('belgaum', 'belagavi').replace('gulbarga', 'kalaburagi').replace('bijapur', 'vijayapura').replace('shimoga', 'shivamogga').replace('mangalore', 'mangaluru').replace('tumkur', 'tumakuru').replace('mysore', 'mysuru').replace('hubli', 'hubballi').replace('chikmagalur', 'chikkamagaluru').replace('hospet', 'hosapete')
    return re.sub(r'[^a-z]', '', s)
key = {norm(a[1]): a for a in acs}
bynum = {a[0]: a for a in acs}
ALIAS = {'Vijayanagar': 167, 'Bellary (ST)': 93, 'Baindur': 118, 'K.R. Pura': 151, 'Hadagali (SC)': 88,
         'Vijayanagara': 90, 'Sandur (ST)': 95, 'Bellary City': 94}
mlas = json.load(io.open(data, encoding='utf-8'))
miss = []
for m in mlas:
    k = norm(m['c'])
    a = bynum[ALIAS[m['c']]] if m['c'] in ALIAS else key.get(k)
    if not a:
        c = difflib.get_close_matches(k, list(key), n=1, cutoff=0.75)
        a = key[c[0]] if c else None
        if a: print('fuzzy:', m['c'], '->', a[1])
    if a: m['ac'] = a[0]; m['dist'] = a[2]
    else: miss.append(m['c'])
print('unmatched', miss)
used = [m.get('ac') for m in mlas if m.get('ac')]
dups = [x for x in set(used) if used.count(x) > 1]
print('duplicate AC numbers', dups)
json.dump(mlas, io.open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
