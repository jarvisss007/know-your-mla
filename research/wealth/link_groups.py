"""Step 2: read myneta's own cross-election grouping ('Other Elections' -> compare_profile.php) for each
sitting MLA's current affidavit, and record which 2018 / 2013 Karnataka affidavit ids myneta links.
This is ADR's linkage, used only to corroborate or contradict the name+seat match, never alone.
Usage: py link_groups.py CACHE_DIR   (reads CACHE/matches.json, writes CACHE/groups.json)
"""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fetch_myneta, myneta_parse

CACHE = pathlib.Path(sys.argv[1])
M = json.load(open(CACHE / 'matches.json'))['matches']
groups = {}
for m in M:
    cid = m['y2023'].get('id')
    if not cid or m['y2023']['confidence'] not in ('exact', 'probable'): continue
    p = CACHE / 'cand2023' / f'{cid}.html'
    if not p.exists(): continue
    s = p.read_bytes().decode('utf-8', 'replace')
    g = re.search(r'compare_profile\.php\?group_id=([A-Za-z0-9]+)', s)
    if not g:
        groups[cid] = {'group': None, 'links': []}; continue
    html_ = fetch_myneta.get('https://www.myneta.info/compare_profile.php?group_id=' + g.group(1),
                             CACHE / 'groups' / f'{g.group(1)}.html', minsize=3000)
    d = myneta_parse.decoded(html_)
    links = []
    for folder, lid in re.findall(r'href=[\'"]?/([A-Za-z0-9]+)/candidate\.php\?candidate_id=(\d+)', d):
        links.append({'folder': folder.lower(), 'id': lid})
    # rows of the comparison table: "<name> in <election> <seat> <age> <party> ..."
    t = myneta_parse.text(d)
    rows = re.findall(r'([A-Za-z][A-Za-z .()\-]{1,60}?) in (Karnataka 20\d\d|Bye-Election Karnataka|Lok Sabha 20\d\d|Karnataka Bye[^ ]*) (.+?) (\d{2}) ', t)
    groups[cid] = {'group': g.group(1), 'links': links, 'rows': rows}
json.dump(groups, open(CACHE / 'groups.json', 'w'), indent=1)
n18 = sum(1 for v in groups.values() if any(l['folder'] == 'karnataka2018' for l in v['links']))
n13 = sum(1 for v in groups.values() if any(l['folder'] == 'karnataka2013' for l in v['links']))
print('groups', len(groups), 'with 2018 link', n18, 'with 2013 link', n13)
