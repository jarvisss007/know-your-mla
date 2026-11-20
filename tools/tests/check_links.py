"""Check every link on the published site.

    py tools/tests/check_links.py            internal links and #anchors only (fast, offline)
    py tools/tests/check_links.py --web      also fetch every external link (a few minutes)

Prints broken internal links, then (with --web) external links that return 404/410.
403s and timeouts are listed separately: Karnataka government sites often refuse visitors from outside India,
so those need a check from India, not a fix.
"""
import collections, concurrent.futures as cf, html, pathlib, re, sys, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKIP_DIRS = {"research", "video", ".git", "content", "cards"}
pages = [p for p in ROOT.rglob("*.html") if not (SKIP_DIRS & set(p.relative_to(ROOT).parts))]
ids = {p: set(re.findall(r'\sid="([^"]+)"', p.read_text(encoding="utf-8", errors="ignore"))) for p in pages}

bad, ext = [], collections.defaultdict(set)
for p in pages:
    t = p.read_text(encoding="utf-8", errors="ignore")
    for h in re.findall(r'\shref="([^"]+)"', t):
        h = html.unescape(h)
        if "${" in h or re.match(r"(mailto:|tel:|javascript:|data:)", h):
            continue
        if h.startswith("http"):
            if not any(s in h for s in ("docs.google.com/forms", "wa.me", "openstreetmap.org/?", "google.com/maps", "fonts.g")):
                ext[h].add(str(p.relative_to(ROOT)))
            continue
        path, _, frag = h.partition("#")
        tgt = (p.parent / path).resolve() if path else p
        if path and tgt.is_dir():
            tgt = tgt / "index.html"
        if not tgt.exists():
            bad.append((p.relative_to(ROOT), h, "missing file"))
        elif frag and tgt.suffix == ".html" and not frag.startswith("mla=") and frag not in ids.get(tgt, set()):
            bad.append((p.relative_to(ROOT), h, "missing anchor"))

print(f"{len(pages)} pages, {len(bad)} broken internal links")
for p, h, why in bad:
    print(f"  {why}: {h}  (in {p})")

if "--web" in sys.argv:
    def check(u):
        for method in ("HEAD", "GET"):
            try:
                r = urllib.request.urlopen(urllib.request.Request(u, method=method, headers={"User-Agent": "Mozilla/5.0"}), timeout=20)
                return u, r.status
            except urllib.error.HTTPError as e:
                if method == "HEAD" and e.code in (400, 403, 405, 501):
                    continue
                return u, e.code
            except Exception as e:
                return u, type(e).__name__
        return u, "?"
    with cf.ThreadPoolExecutor(10) as ex:
        res = list(ex.map(check, sorted(ext)))
    dead = [(u, s) for u, s in res if s in (404, 410)]
    other = [(u, s) for u, s in res if not (isinstance(s, int) and s < 400) and s not in (404, 410)]
    print(f"{len(res)} external links: {len(dead)} dead, {len(other)} blocked or timed out")
    for u, s in dead:
        print(f"  DEAD {s}: {u}  (in {', '.join(sorted(ext[u]))})")
    for u, s in other:
        print(f"  check from India ({s}): {u}")
