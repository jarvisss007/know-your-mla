"""Polite cached fetcher for myneta pages (1 request/second). Used by build_wealth.py.
Usage: py fetch_myneta.py CACHE_DIR listings|details IDS_FILE(optional)
"""
import pathlib, sys, time, urllib.request, re
UA = {'User-Agent': 'Mozilla/5.0 (civic research; non-partisan citizen site)'}
BASE = {'2013': 'https://www.myneta.info/Karnataka2013/', '2018': 'https://www.myneta.info/Karnataka2018/',
        '2023': 'https://www.myneta.info/Karnataka2023/'}
_last = [0.0]

def get(url, out, minsize=2000):
    out = pathlib.Path(out)
    if out.exists() and out.stat().st_size > minsize:
        return out.read_bytes().decode('utf-8', 'replace')
    for attempt in range(4):
        wait = 1.0 - (time.time() - _last[0])
        if wait > 0: time.sleep(wait)
        _last[0] = time.time()
        try:
            b = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
            out.parent.mkdir(parents=True, exist_ok=True); out.write_bytes(b)
            return b.decode('utf-8', 'replace')
        except Exception as e:
            print('retry', url, e, flush=True); time.sleep(5 * (attempt + 1))
    return ''

def listings(cache, year):
    url = BASE[year] + 'index.php?action=summary&subAction=candidates_analyzed&sort=candidate&page={}'
    first = get(url.format(1), cache / f'list{year}' / 'p1.html')
    n = int(re.search(r'of\s+(\d+)\s+pages', re.sub(r'<[^>]+>', ' ', first)).group(1))
    for p in range(2, n + 1):
        get(url.format(p), cache / f'list{year}' / f'p{p}.html')
    print(year, 'listing pages', n, flush=True)

def details(cache, year, ids):
    for cid in ids:
        get(BASE[year] + f'candidate.php?candidate_id={cid}', cache / f'cand{year}' / f'{cid}.html', minsize=20000)
    print(year, 'detail pages', len(ids), flush=True)

if __name__ == '__main__':
    cache = pathlib.Path(sys.argv[1]); mode = sys.argv[2]
    if mode == 'listings':
        for y in sys.argv[3:]: listings(cache, y)
    else:
        year = sys.argv[3]; ids = [l.strip() for l in open(sys.argv[4]) if l.strip()]
        details(cache, year, ids)
