"""Google Search Console verification (and an optional second visitor counter), in one place.

NOTE: GoatCounter is ALREADY live at https://gandaberunda.goatcounter.com (commit 10ae93b, hard-coded in the page
generators and pages). Leave GOATCOUNTER_CODE empty, or visits are counted twice. Only Search Console needs a code.

Both are switched OFF until a code is set. Every page this session owns carries a marked slot
<!--gb-site-codes-->...<!--/gb-site-codes--> in its <head>; generators call head_block() to fill it.

Owner steps (one each):
  Search Console: https://search.google.com/search-console -> Add property -> "URL prefix" ->
                  https://jarvisss007.github.io/know-your-mla/ -> choose "HTML tag" -> copy only the content="..." value.
  Visitor numbers: already counting at https://gandaberunda.goatcounter.com (sign in there to see them).

Then:
  py tools/site_codes.py --search-console <content value>
fills every slot, rebuilds the report cards and member pages, and prints the next step (submit the sitemap).
  py tools/site_codes.py --off       switches both off again.
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SEARCH_CONSOLE_CODE = ""   # the content="..." value of Google's verification meta tag
GOATCOUNTER_CODE = ""      # e.g. "gandaberunda" for https://gandaberunda.goatcounter.com

START, END = "<!--gb-site-codes-->", "<!--/gb-site-codes-->"
# Pages this session owns and edits by hand; generated pages get the block from their generator.
STATIC = ["index.html", "money.html", "members.html", "farmers.html"]
GENERATORS = ["tools/make_mla_pages.py", "tools/make_members_page.py"]


def head_block(home=False):
    """The slot's contents. The Search Console tag only needs to be on the home page."""
    parts = []
    if SEARCH_CONSOLE_CODE and home:
        parts.append(f'<meta name="google-site-verification" content="{SEARCH_CONSOLE_CODE}">')
    if GOATCOUNTER_CODE:
        parts.append(f'<script data-goatcounter="https://{GOATCOUNTER_CODE}.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>')
    return START + "".join(parts) + END


def fill(path, home=False):
    p = ROOT / path
    t = p.read_text(encoding="utf-8")
    block = head_block(home)
    if START in t:
        t2 = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, t, count=1, flags=re.S)
    else:
        t2 = t.replace("</head>", block + "\n</head>", 1)
    if t2 != t:
        p.write_text(t2, encoding="utf-8", newline="\n")
    return t2 != t


def set_codes(sc, gc):
    me = pathlib.Path(__file__)
    s = me.read_text(encoding="utf-8")
    s = re.sub(r'^SEARCH_CONSOLE_CODE = ".*?"', f'SEARCH_CONSOLE_CODE = "{sc}"', s, count=1, flags=re.M)
    s = re.sub(r'^GOATCOUNTER_CODE = ".*?"', f'GOATCOUNTER_CODE = "{gc}"', s, count=1, flags=re.M)
    me.write_text(s, encoding="utf-8", newline="\n")


def main(argv):
    global SEARCH_CONSOLE_CODE, GOATCOUNTER_CODE
    if "--off" in argv:
        SEARCH_CONSOLE_CODE = GOATCOUNTER_CODE = ""
    if "--search-console" in argv:
        SEARCH_CONSOLE_CODE = argv[argv.index("--search-console") + 1].strip().strip('"')
    if "--goatcounter" in argv:
        GOATCOUNTER_CODE = argv[argv.index("--goatcounter") + 1].strip().replace(".goatcounter.com", "")
    for code in (SEARCH_CONSOLE_CODE, GOATCOUNTER_CODE):
        assert re.fullmatch(r"[A-Za-z0-9_\-]*", code), f"unexpected characters in code: {code!r}"
    set_codes(SEARCH_CONSOLE_CODE, GOATCOUNTER_CODE)
    changed = [p for p in STATIC if (ROOT / p).exists() and fill(p, home=(p == "index.html"))]
    for g in GENERATORS:
        subprocess.run([sys.executable, str(ROOT / g)], check=True, cwd=ROOT)
    print("Search Console:", "ON" if SEARCH_CONSOLE_CODE else "off", "| GoatCounter:", "ON" if GOATCOUNTER_CODE else "off")
    print("static pages updated:", changed or "none")
    if SEARCH_CONSOLE_CODE:
        print("Next: push, wait a minute, press Verify in Search Console, then Sitemaps -> add sitemap.xml -> Submit.")


if __name__ == "__main__":
    main(sys.argv[1:])
