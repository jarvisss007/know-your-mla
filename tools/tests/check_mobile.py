"""Phone-width check: sideways overflow and broken images, page by page, in headless Chrome.

    py tools/tests/check_mobile.py                 # main pages, every report, a sample of report cards and member pages
    py tools/tests/check_mobile.py index.html ...   # just these pages
Test copies go to the system temp folder with a <base> tag pointing back at the repo, so nothing is written into the
repo. Headless Chrome's narrowest window is 500 px.
"""
import html, json, pathlib, re, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROBE = """<script>setTimeout(()=>{const bad=[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.currentSrc||i.src).slice(0,3);
const wide=[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.right>innerWidth+2&&getComputedStyle(e).position!=='fixed'&&!e.closest('.tw,.tablewrap,.tbl,.chart,[style*="overflow"],table,pre,svg,.nav,.topnav')}).slice(0,2).map(e=>e.tagName+'.'+e.className);
document.body.setAttribute('data-gbm',JSON.stringify({sw:document.documentElement.scrollWidth,iw:innerWidth,bad,wide}))},2500)</script></body>"""


def pages():
    if sys.argv[1:]:
        return sys.argv[1:]
    fixed = ["index.html", "money.html", "members.html", "farmers.html", "rti.html", "mla/index.html",
             "mla/kanakapura.html", "mla/byatarayanapura.html", "mla/shirahatti-sc.html", "members/ajay-maken.html"]
    return fixed + sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "reports").rglob("*.html"))


def check(rel):
    p = ROOT / rel
    src = p.read_text(encoding="utf-8", errors="ignore")
    base = f'<base href="{p.parent.as_uri()}/">'
    src = src.replace("<head>", "<head>" + base, 1) if "<head>" in src else base + src
    tmp = pathlib.Path(tempfile.gettempdir()) / "gb_mobile_probe.html"
    tmp.write_text(src.replace("</body>", PROBE, 1), encoding="utf-8")
    dom = subprocess.run([CHROME, "--headless=new", "--dump-dom", "--window-size=500,1200", "--virtual-time-budget=6000",
                          "--allow-file-access-from-files", tmp.as_uri()], capture_output=True, text=True, encoding="utf-8", timeout=120).stdout
    tmp.unlink(missing_ok=True)
    m = re.search(r'data-gbm="([^"]*)"', dom)
    return json.loads(html.unescape(m.group(1))) if m else {"err": "no result"}


problems = []
ps = pages()
for rel in ps:
    r = check(rel)
    if "err" in r or r.get("sw", 0) > r.get("iw", 0) + 2 or r.get("bad") or r.get("wide"):
        problems.append((rel, r))
print(f"{len(ps)} pages tested at 500 px, {len(problems)} with problems")
for rel, r in problems:
    print(" ", rel, r)
