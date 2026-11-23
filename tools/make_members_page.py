"""Build members.html: Karnataka's MLCs, Lok Sabha MPs and Rajya Sabha MPs, with what each declared in their own
sworn election affidavit (as transcribed by ADR on myneta.info). Declared figures only: no grades, gaps or analysis.

    py tools/make_members_page.py --from <private sweep members.json>   # refresh data/mlc_mp.json, then build
    py tools/make_members_page.py                                        # build from data/mlc_mp.json

data/mlc_mp.json is the public subset: name, house, seat, party, term, and per affidavit the year, type, myneta link,
assets, liabilities and declared criminal cases. Nothing else from the private sweep is copied.
"""
import html, io, json, pathlib, re, sys
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "mlc_mp.json"
OUT = ROOT / "members.html"
SITE = "https://jarvisss007.github.io/know-your-mla/"
PARTY = {"INC": "Congress", "IND": "Independent"}
HOUSES = [("Lok Sabha", "ಲೋಕಸಭೆ", "Members of Parliament elected from Karnataka in 2024."),
          ("Rajya Sabha", "ರಾಜ್ಯಸಭೆ", "Members of Parliament elected by Karnataka's MLAs."),
          ("Legislative Council", "ವಿಧಾನ ಪರಿಷತ್", "Members of Karnataka's upper house (MLCs): elected by MLAs, by local-body members, by graduates and teachers, or nominated.")]
E = html.escape


def label(t):
    """Public label for an affidavit: drop working notes (inferences, myneta ids) from the sweep's label."""
    import re
    if "myneta record" in t:
        return "Rajya Sabha (earlier term)"
    t = re.sub(r";[^)]*(inferred|myneta)[^)]*", "", t)
    t = re.sub(r",\s*(inferred[^)]*)", "", t)
    return t


def refresh(src):
    ms = json.load(io.open(src, encoding="utf-8"))["members"]
    out = []
    for m in ms:
        r = {k: m[k] for k in ("name", "house", "seat", "elected_by", "term")}
        r["party"] = PARTY.get(m["party"], m["party"])
        r["affs"] = []
        # An affidavit whose identity match is uncertain is never published.
        if m.get("affidavit_found") and "identity probable" in m["latest_affidavit"]["type"]:
            m = dict(m, affidavit_found=False)
        if m.get("affidavit_found"):
            la = dict(m["latest_affidavit"]); la["type"] = label(la["type"])
            r["current"] = bool(m.get("current_office_affidavit_on_myneta"))
            r["latest"] = {"year": la["year"], "type": la["type"], "url": la["url"],
                           "a": round(la["total_assets_rs"] / 1e7, 2) if la.get("total_assets_rs") is not None else None,
                           "l": round(la["total_liabilities_rs"] / 1e7, 2) if la.get("total_liabilities_rs") is not None else None,
                           "k": la.get("declared_criminal_cases")}
            r["affs"] = [{"year": a["year"], "type": label(a["type"]), "url": a["url"], "a": a.get("assets_cr"), "l": a.get("liabilities_cr")}
                         for a in m.get("affidavits", []) if "identity probable" not in a["type"]]
        out.append(r)
    DATA.parent.mkdir(exist_ok=True)
    io.open(DATA, "w", encoding="utf-8", newline="\n").write(json.dumps(out, ensure_ascii=False, indent=1))
    print("data rows:", len(out))


def money(v):
    if v is None:
        return "not given"
    if v < 1:
        return f"Rs {round(v * 100)} lakh"
    s = f"{v:,.0f}" if v >= 100 else (f"{v:.1f}" if v >= 10 else f"{v:.2f}")
    return f"Rs {s} crore"


def card(m):
    party = E(m["party"])
    nm = f'<a class="nm" href="members/{mslug(m)}.html">{E(m["name"])}</a>' if m.get("latest") else E(m["name"])
    head = f'<h3>{nm}</h3><div class="meta"><span class="pty">{party}</span> · {E(m["seat"])} · {E(m["term"])}</div>'
    if not m.get("latest"):
        return (f'<article class="mc none" data-p="{party}" data-q="{E((m["name"] + " " + m["seat"]).lower())}">{head}'
                f'<p class="miss" data-kn="ಈ ಸ್ಥಾನಕ್ಕೆ ಪ್ರಮಾಣಪತ್ರ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಸಿಗಲಿಲ್ಲ.">No affidavit for this member could be found online.</p></article>')
    la = m["latest"]
    old = "" if m.get("current") else (f'<p class="old" data-kn="ಇದು ಹಿಂದಿನ ಚುನಾವಣೆಯ ಪ್ರಮಾಣಪತ್ರ; ಈಗಿನ ಸ್ಥಾನದ ಪ್ರಮಾಣಪತ್ರ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಇಲ್ಲ.">'
                                       f'This is from an earlier election; the affidavit for the current seat is not online.</p>')
    k = la.get("k") or 0
    hist = ""
    if len(m["affs"]) > 1:
        rows = "".join(f'<li><a href="{E(a["url"])}" rel="noopener">{E(a["type"])}</a>: assets {money(a["a"])}, debts {money(a["l"])}</li>' for a in m["affs"])
        hist = f'<details><summary data-kn="ಹಿಂದಿನ ಪ್ರಮಾಣಪತ್ರಗಳು">Every affidavit found ({len(m["affs"])})</summary><ul>{rows}</ul></details>'
    return (f'<article class="mc" data-p="{party}" data-q="{E((m["name"] + " " + m["seat"]).lower())}">{head}'
            f'<div class="big">{money(la["a"])}</div><div class="lbl" data-kn="ಘೋಷಿತ ಆಸ್ತಿ">assets declared</div>'
            f'<ul class="facts"><li><span data-kn="ಘೋಷಿತ ಸಾಲ">Debts declared</span>: {money(la["l"])}</li>'
            f'<li><span data-kn="ಘೋಷಿತ ಕ್ರಿಮಿನಲ್ ಪ್ರಕರಣಗಳು">Declared criminal cases</span>: {k}'
            + (' <span class="hint" data-kn="(ಪ್ರಕರಣ ಎಂದರೆ ಶಿಕ್ಷೆ ಅಲ್ಲ)">(a case is not a conviction)</span>' if k else "") + '</li>'
            f'<li class="src"><span data-kn="ಮೂಲ">Source</span>: <a href="{E(la["url"])}" rel="noopener">{E(la["type"])}</a></li></ul>'
            f'{old}{hist}</article>')


def nk(name):
    """Name key for exact matching: letters only, single spaces, lower case."""
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z]+', ' ', name.lower())).strip()


def mslug(m):
    return re.sub(r'[^a-z0-9]+', '-', m["name"].lower()).strip('-')


def loans_names():
    """Names that appear in the public 'Money between politicians' table, to link from member pages."""
    src = io.open(ROOT / "index.html", encoding="utf-8").read()
    mm = re.search(r'<section class="block page" id="loans">(.*?)</section>', src, re.S)
    return {nk(x) for x in re.findall(r'<b>([^<]+)</b>', mm.group(1))} if mm else set()


def member_page(m, style, loans_txt):
    la = m["latest"]
    k = la.get("k") or 0
    rows = "".join(
        f'<tr><td><a href="{E(a["url"])}" target="_blank" rel="noopener">{E(a["type"])}</a></td><td>{money(a["a"])}</td>'
        f'<td>{money(a["l"])}</td><td>{money(round(a["a"] - a["l"], 2)) if a["a"] is not None and a["l"] is not None else "not given"}</td></tr>'
        for a in m["affs"])
    first, last = m["affs"][0], m["affs"][-1]
    growth = ""
    if len(m["affs"]) > 1 and first["a"] and last["a"] is not None:
        g = round(100 * (last["a"] - first["a"]) / first["a"])
        growth = (f'<p>Declared assets went from {money(first["a"])} ({E(first["type"])}) to {money(last["a"])} '
                  f'({E(last["type"])}), {"+" if g >= 0 else ""}{g}%. Values are mostly what the member paid, not market value, '
                  f'and they include the family&#x27;s holdings.</p>')
    old = "" if m.get("current") else '<p class="old">The latest affidavit online is from an earlier election; the one for the current seat is not online.</p>'
    loans = ('<p>This member appears in <a href="../index.html#loans">Money between politicians</a>: loans declared on both sides.</p>'
             if nk(m["name"]) in loans_txt else "")
    sl = mslug(m)
    url = SITE + "members/" + sl + ".html"
    desc = (f'{m["name"]} ({m["party"]}), {m["house"]}, {m["seat"]}: declared assets {money(la["a"])}, debts {money(la["l"])}, '
            f'{k} declared criminal cases. From sworn election affidavits.')
    wa = f'{m["name"]} ({m["house"]}) declared assets of {money(la["a"])}. Every affidavit, side by side: {url}'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(m["name"])}: declared assets · Gandaberunda</title>
<meta name="description" content="{E(desc)}">
<meta property="og:type" content="article">
<meta property="og:title" content="{E(m["name"])}: declared assets · Gandaberunda">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}brand/gandaberunda-banner.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+Kannada:wght@400;600;800&family=Space+Grotesk:wght@500;700&display=swap">
<style>{style}
table {{ border-collapse: collapse; width: 100%; font-size: 15px; background: var(--surface); border: 1px solid var(--line); border-radius: 12px; overflow: hidden; margin-top: 10px }}
th {{ text-align: left; font-size: 11px; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); padding: 10px 12px; border-bottom: 1px solid var(--line) }}
td {{ padding: 10px 12px; border-bottom: 1px solid var(--line); vertical-align: top; overflow-wrap: anywhere }}
tr:last-child td {{ border-bottom: 0 }}
.tw {{ overflow-x: auto }}
.share {{ display: inline-block; margin-top: 14px; padding: 10px 16px; border-radius: 10px; background: var(--fg); color: var(--bg); text-decoration: none; font-weight: 600 }}
</style>
</head>
<body>
<div class="wrap">
<header class="top"><a class="home" href="../members.html">← MLCs and MPs</a><a class="home" href="../">Gandaberunda</a></header>
<h1>{E(m["name"])}</h1>
<p class="lede">{E(m["party"])} · {E(m["house"])} · {E(m["seat"])} · {E(m["term"])}</p>
<div class="big">{money(la["a"])}</div><div class="lbl">assets declared in the latest affidavit found ({E(la["type"])})</div>
<ul class="facts"><li>Debts declared: {money(la["l"])}</li><li>Declared criminal cases: {k}{' <span class="hint">(a case is not a conviction)</span>' if k else ''}</li></ul>
{old}
<h2>Every affidavit we found</h2>
<div class="tw"><table><thead><tr><th>Affidavit</th><th>Assets</th><th>Debts</th><th>Net</th></tr></thead><tbody>{rows}</tbody></table></div>
{growth}
{loans}
<a class="share" href="https://wa.me/?text={quote(wa)}" target="_blank" rel="noopener">Share on WhatsApp</a>
<div class="box">Declared figures only, as transcribed from the member&#x27;s sworn affidavits by the Association for Democratic Reforms on myneta.info. No allegation, grade or analysis. Seen a mistake? <a href="https://github.com/jarvisss007/know-your-mla/issues/new" target="_blank" rel="noopener">Tell us</a> and we will correct it.</div>
<footer><p><a href="../members.html">← All MLCs and MPs</a> · <a href="../">Gandaberunda</a></p></footer>
</div>
<script data-goatcounter="https://gandaberunda.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
"""


def build_member_pages(ms):
    style = re.search(r'<style>(.*?)</style>', PAGE, re.S).group(1)
    out = ROOT / "members"
    out.mkdir(exist_ok=True)
    lt = loans_names()
    slugs = [mslug(m) for m in ms if m.get("latest")]
    assert len(slugs) == len(set(slugs)), "duplicate member slugs"
    for m in ms:
        if m.get("latest"):
            io.open(out / f"{mslug(m)}.html", "w", encoding="utf-8", newline="\n").write(member_page(m, style, lt))
    print("member pages:", len(slugs))


def build():
    ms = json.load(io.open(DATA, encoding="utf-8"))
    found = sum(1 for m in ms if m.get("latest"))
    secs = []
    for h, kn, blurb in HOUSES:
        grp = sorted([m for m in ms if m["house"] == h], key=lambda m: (0, -m["latest"]["a"]) if m.get("latest") and m["latest"]["a"] is not None else (1, 0))
        n_f = sum(1 for m in grp if m.get("latest"))
        secs.append(f'<section class="house" id="{h.split()[0].lower()}"><h2><span data-kn="{kn}">{h}</span> <small>({len(grp)})</small></h2>'
                    f'<p class="note">{E(blurb)} Affidavit found for {n_f} of {len(grp)}. Sorted by declared assets.</p>'
                    f'<div class="grid">{"".join(card(m) for m in grp)}</div></section>')
    parties = sorted({m["party"] for m in ms})
    desc = "What Karnataka's MLCs and MPs declared in their own sworn election affidavits: assets, debts and criminal cases, with the source for each."
    page = PAGE.replace("{{DESC}}", E(desc)).replace("{{N}}", str(len(ms))).replace("{{F}}", str(found)).replace(
        "{{OPTS}}", "".join(f'<option>{E(p)}</option>' for p in parties)).replace("{{SECS}}", "\n".join(secs))
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(page)
    build_member_pages(ms)
    print("wrote", OUT.name, len(ms), "members,", found, "with affidavits")


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{{DESC}}">
<meta property="og:type" content="article">
<meta property="og:title" content="MLCs and MPs · Gandaberunda">
<meta property="og:description" content="{{DESC}}">
<meta property="og:url" content="https://jarvisss007.github.io/know-your-mla/members.html">
<meta property="og:image" content="https://jarvisss007.github.io/know-your-mla/brand/gandaberunda-banner.png">
<meta name="twitter:card" content="summary_large_image">
<title>MLCs and MPs · Gandaberunda</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+Kannada:wght@400;600;800&family=Space+Grotesk:wght@500;700&display=swap">
<style>
:root {
  --bg: #f5f6f8; --surface: #ffffff; --fg: #161a22; --muted: #5b6474; --line: #dde1e8;
  --red: #c21f30; --redbg: #fbe9eb; --yellow: #f2b705; --chip: #eef0f4;
  --display: "Space Grotesk", "Noto Sans Kannada", system-ui, sans-serif;
  --body: "Noto Sans Kannada", system-ui, "Segoe UI", sans-serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d;
  --red: #ef5261; --redbg: #3a1d22; --yellow: #f5c93a; --chip: #232835; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d;
  --red: #ef5261; --redbg: #3a1d22; --yellow: #f5c93a; --chip: #232835; color-scheme: dark }
* { box-sizing: border-box }
html, body { overflow-x: clip }
body { margin: 0; background: var(--bg); color: var(--fg); font-family: var(--body); font-size: 16px; line-height: 1.6 }
.wrap { max-width: 1040px; margin: 0 auto; padding: 20px 16px 60px }
header.top { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 28px }
header.top a.home { color: var(--fg); text-decoration: none; font-family: var(--display); font-weight: 700 }
#lang { font: inherit; font-size: .9rem; padding: 6px 14px; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); color: var(--fg); cursor: pointer }
h1, h2, h3 { font-family: var(--display); line-height: 1.25; margin: 0; text-wrap: balance }
h1 { font-size: clamp(30px, 6vw, 44px) }
h2 { font-size: 24px; margin: 40px 0 6px } h2 small { color: var(--muted); font-size: 16px; font-weight: 500 }
.lede { color: var(--muted); max-width: 66ch; margin: 12px 0 0 }
.note { color: var(--muted); font-size: 14px; max-width: 72ch; margin: 0 0 14px }
.tools { display: flex; flex-wrap: wrap; gap: 10px; margin: 24px 0 0; position: sticky; top: 0; background: var(--bg); padding: 10px 0; z-index: 2 }
.tools input, .tools select { font: inherit; padding: 8px 12px; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); color: var(--fg) }
.tools input { flex: 1 1 220px }
.jump { display: flex; gap: 8px; flex-wrap: wrap } .jump a { font-size: 14px; padding: 8px 12px; border-radius: 999px; background: var(--chip); color: var(--fg); text-decoration: none }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(290px, 100%), 1fr)); gap: 12px }
.tools select { min-width: 0; max-width: 100% }
@media (max-width: 520px) { .tools input, .tools select { flex: 1 1 100% } }
.mc { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 14px 16px; display: flex; flex-direction: column; gap: 4px; min-width: 0 }
.mc h3 { font-size: 18px } .mc h3 a.nm { color: var(--fg); text-decoration: none } .mc h3 a.nm:hover { text-decoration: underline }
.meta { color: var(--muted); font-size: 13.5px } .pty { font-weight: 600; color: var(--fg) }
.big { font-family: var(--display); font-weight: 700; font-size: 28px; margin-top: 8px; color: var(--fg) }
.lbl { color: var(--muted); font-size: 13px; margin-top: -4px }
.facts { list-style: none; padding: 0; margin: 8px 0 0; font-size: 14.5px; display: grid; gap: 2px }
.facts .src { font-size: 13px; color: var(--muted); overflow-wrap: anywhere }
.hint { color: var(--muted); font-size: 12.5px }
.old { font-size: 13px; background: var(--chip); border-radius: 8px; padding: 6px 10px; margin: 8px 0 0 }
.miss { color: var(--muted); font-size: 14px; margin: 8px 0 0 }
.mc.none { border-style: dashed }
details { font-size: 13.5px; margin-top: 8px } summary { cursor: pointer; color: var(--muted) }
details ul { padding-left: 18px; margin: 6px 0 0 } details li { overflow-wrap: anywhere }
a { color: var(--red) }
.box { background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--yellow); border-radius: 12px; padding: 14px 16px; margin-top: 20px; font-size: 14.5px; color: var(--muted) }
footer { margin-top: 48px; color: var(--muted); font-size: 14px }
[hidden] { display: none !important }
</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="home" href="./">← Gandaberunda</a>
  <button type="button" id="lang">ಕನ್ನಡ</button>
</header>

<h1 data-kn="ವಿಧಾನ ಪರಿಷತ್ ಸದಸ್ಯರು ಮತ್ತು ಸಂಸದರು">MLCs and MPs</h1>
<p class="lede" data-kn="ಕರ್ನಾಟಕದ ವಿಧಾನ ಪರಿಷತ್ ಸದಸ್ಯರು ಮತ್ತು ಸಂಸದರು ತಮ್ಮ ಸ್ವಂತ ಚುನಾವಣಾ ಪ್ರಮಾಣಪತ್ರಗಳಲ್ಲಿ ಘೋಷಿಸಿದ ಆಸ್ತಿ, ಸಾಲ ಮತ್ತು ಪ್ರಕರಣಗಳು. ಪ್ರತಿ ಅಂಕಿಗೂ ಮೂಲದ ಕೊಂಡಿ ಇದೆ.">What Karnataka's {{N}} MLCs and MPs declared under oath when they stood for election: assets, debts and criminal cases. Every figure links to its source. We found an affidavit online for {{F}} of them.</p>

<div class="box" data-kn="ಇವು ಘೋಷಿತ ಅಂಕಿಗಳು ಮಾತ್ರ. ಇಲ್ಲಿ ಯಾವುದೇ ಆರೋಪ ಅಥವಾ ಶ್ರೇಣಿ ಇಲ್ಲ. ಅಂಕಿಗಳು ADR (myneta.info) ಮಾಡಿದ ಪ್ರತಿಲೇಖನದಿಂದ ಬಂದಿವೆ; ತಪ್ಪು ಕಂಡರೆ ತಿಳಿಸಿ.">These are declared figures only: no allegation, grade or analysis. Figures are as transcribed from the affidavits by the Association for Democratic Reforms on myneta.info. Assets and debts are what the member declared for themselves and their family on the date of filing; values are often book cost, not market value. If you see a mistake, tell us and we will correct it.</div>

<div class="tools">
  <input type="search" id="q" placeholder="Search a name or seat" aria-label="Search a name or seat">
  <select id="p" aria-label="Party"><option value="">All parties</option>{{OPTS}}</select>
  <div class="jump"><a href="#lok">Lok Sabha</a><a href="#rajya">Rajya Sabha</a><a href="#legislative">Council</a></div>
</div>

{{SECS}}

<footer>
<p>Members list: public lists of Karnataka's Legislative Council and Rajya Sabha members as of 17-19 November 2026, checked against reports of the 2026 elections (the Council's own website did not load); Lok Sabha: the 2024 results. Five nominated Council seats are vacant. Affidavits: myneta.info (ADR), read 20 November 2026. MLAs are on the <a href="./">main page</a>.</p>
<p><a href="./">← Back to Gandaberunda</a></p>
</footer>
</div>
<script>
(function () {
  const q = document.getElementById('q'), p = document.getElementById('p');
  function filt() {
    const t = q.value.trim().toLowerCase(), pv = p.value;
    document.querySelectorAll('.mc').forEach(c => { c.hidden = !((!t || c.dataset.q.includes(t)) && (!pv || c.dataset.p === pv)); });
    document.querySelectorAll('.house').forEach(s => { s.hidden = !s.querySelector('.mc:not([hidden])'); });
  }
  q.addEventListener('input', filt); p.addEventListener('change', filt);
  const lb = document.getElementById('lang');
  document.querySelectorAll('[data-kn]').forEach(e => { e.dataset.en = e.innerHTML; });
  lb.addEventListener('click', () => {
    const kn = document.documentElement.lang !== 'kn';
    document.documentElement.lang = kn ? 'kn' : 'en';
    document.querySelectorAll('[data-kn]').forEach(e => { e.innerHTML = kn ? e.dataset.kn : e.dataset.en; });
    lb.textContent = kn ? 'English' : 'ಕನ್ನಡ';
  });
})();
</script>
<script data-goatcounter="https://gandaberunda.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
"""

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--from":
        refresh(sys.argv[2])
    build()
