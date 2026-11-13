import re, sys, subprocess, json
# For each query, print myneta candidate links whose row mentions a by-election, then read those pages' totals.
def get(url):
    return subprocess.run(['curl', '-s', '-m', '30', '-A', 'Mozilla/5.0', url], capture_output=True).stdout.decode('utf-8', 'ignore')

def text(h): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h))

hits = {}
for q in sys.argv[1:]:
    s = get('https://www.myneta.info/search_myneta.php?q=' + q)
    parts = re.split(r'(<a[^>]*href="[^"]*candidate\.php\?candidate_id=\d+"[^>]*>)', s)
    for i in range(1, len(parts), 2):
        href = re.search(r'href="([^"]+)"', parts[i]).group(1)
        t = text(parts[i + 1][:1200])
        if 'BYE ELECTION' in t.upper():
            url = href if href.startswith('http') else 'https://www.myneta.info/' + href.lstrip('/')
            hits[url] = t[:150]
for url, t in hits.items():
    p = get(url)
    tt = text(p)
    def grab(lbl):
        m = re.search(lbl + r'[^:]*:\s*Rs\s*([\d,]+)', tt)
        return m.group(1) if m else None
    title = re.search(r'<title>([^<]+)', p)
    cases = re.search(r'Number of Criminal Cases:\s*(\d+)', tt)
    print(json.dumps({'url': url, 'row': t, 'title': title.group(1).strip() if title else None,
                      'assets': grab('Assets'), 'liab': grab('Liabilities'), 'cases': cases.group(1) if cases else None}, ensure_ascii=False))
