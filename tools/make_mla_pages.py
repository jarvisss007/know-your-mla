"""Build one static report-card page per MLA: mla/<slug>.html, plus mla/index.html.

    py tools/make_mla_pages.py

Single source of truth: the D (MLAs) and DIST (constituency -> district) arrays inside index.html,
plus research/farmer_schemes/district/district_data.csv for district context (official sources only).
Static pages exist so each MLA has a link that search engines index and WhatsApp previews properly.
Re-run after index.html's data changes.
"""
import csv, html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "mla"
SITE = "https://jarvisss007.github.io/know-your-mla/"
GFORM = "https://docs.google.com/forms/d/e/1FAIpQLSdGCs8oRCLplhyq3VxHH_olo9GzMJk9I7kv5q54yxgUFp2C3A/viewform"
SAT = {"Kanakapura": "kanakapura", "Holenarasipur": "holenarasipur", "Mahadevapura": "mahadevapura"}
DIST_ALIAS = {"Chikkaballapura": "Chikkaballapur", "Davanagere": "Davangere"}  # site name -> research CSV name
PARTY_KN = {"Congress": "ಕಾಂಗ್ರೆಸ್", "BJP": "ಬಿಜೆಪಿ", "JD(S)": "ಜೆಡಿ(ಎಸ್)", "Independent": "ಪಕ್ಷೇತರ"}
E = html.escape
from urllib.parse import quote

src = (ROOT / "index.html").read_text(encoding="utf-8")
k = src.index("const D = [")
D = json.loads(src[k + 10: src.index("];", k) + 1])
k = src.index("const DIST = ")
DIST = json.loads(src[k + 13: src.index("};", k) + 1])


def section_text(sid):
    m = re.search(rf'<section class="block page" id="{sid}">(.*?)</section>', src, re.S)
    return re.sub(r"<[^>]+>", " ", m.group(1)).lower() if m else ""


def norm(s):
    return re.sub(r"[^a-z]+", " ", s.lower()).strip()


ALSO = {sid: norm(section_text(sid)) for sid in ("record", "tested", "cabinet", "latest")}
# Seats whose MLA appears in a section under a shorter name than the affidavit name in D
ALSO_EXTRA = {"Athani": ("cabinet",), "Byatarayanapura": ("cabinet",), "Sedam": ("cabinet",), "Mangalore": ("cabinet",),
              "Kanakagiri (SC)": ("cabinet",), "Haveri (SC)": ("cabinet",), "Hungund": ("cabinet",)}
ALSO_LABEL = {"record": "On the record", "tested": "Five MLAs tested", "cabinet": "Twenty-three ministers tested", "latest": "Latest"}

LIAB = {}  # constituency -> {"loans", "dues", "disputed"} (crore) from the affidavit, via tools/fetch_liabilities.py
_lp = ROOT / "data/liabilities_myneta.csv"
if _lp.exists():
    for r in csv.DictReader(open(_lp, encoding="utf-8")):
        if r.get("affidavit_total_cr", "") != "" and r.get("govt_dues_cr", "") != "":
            LIAB[r["constituency"]] = {"loans": float(r["affidavit_total_cr"]), "dues": float(r["govt_dues_cr"]),
                                       "disputed": float(r["disputed_cr"] or 0)}


ITEMISED = {}  # constituency -> (stated total, itemised sum, note): affidavits whose own rows do not add up to their stated total
_ip = ROOT / "data/liab_itemised_check.csv"
if _ip.exists():
    for r in csv.DictReader(open(_ip, encoding="utf-8")):
        ITEMISED[r["constituency"]] = (float(r["stated_total_cr"]), float(r["itemised_sum_cr"]), r["note"])


def itemised_note(c):
    if c not in ITEMISED:
        return ""
    st, it, note = ITEMISED[c]
    extra = f" ({note})" if note else ""
    if it == 0:
        return f". The affidavit states a total of {money(st)} but itemises no debts{'' if not note else ''}; we show its stated total"
    return (f". The affidavit's itemised debts add up to {money(it)}{extra}, but its stated total is {money(st)}; "
            f"we show the stated total")


def debts_note(c, l):
    """What the debts figure contains, for one MLA."""
    x = LIAB.get(c)
    if l is None or not x:
        return "Loans and dues to government declared in the affidavit"
    if x["loans"] and x["dues"]:
        parts = f"Loans {money(x['loans'])} and dues to government {money(x['dues'])}, as declared in the affidavit"
    elif x["dues"]:
        parts = "Dues to government declared in the affidavit; no loans"
    elif x["loans"]:
        parts = "Loans declared in the affidavit; no dues to government"
    else:
        parts = "No loans or dues to government declared in the affidavit"
    if x["disputed"]:
        parts += f". Not included: {money(x['disputed'])} the MLA lists as disputed"
    return parts + itemised_note(c)
dd = {}
for r in csv.DictReader(open(ROOT / "research/farmer_schemes/district/district_data.csv", encoding="utf-8-sig")):
    if r["value"] and r["confidence"] == "HIGH":
        dd.setdefault(r["district"], {})[(r["metric"], r["season"])] = r


def slug(c):
    return re.sub(r"[^a-z0-9]+", "-", c.lower()).strip("-")


def money(v):
    if v is None:
        return None
    if v < 1:
        return f"₹{v * 100:,.0f} lakh"
    return f"₹{v:,.2f} crore".replace(".00 crore", " crore")


ranked = sorted([d for d in D if d["a"] is not None], key=lambda d: -d["a"])
RANK = {d["c"]: i + 1 for i, d in enumerate(ranked)}
by_dist = {}
for d in ranked:
    by_dist.setdefault(DIST.get(d["c"], ""), []).append(d["c"])

CSS = """
:root { --bg: #f5f6f8; --surface: #fff; --fg: #161a22; --muted: #5b6474; --line: #dde1e8; --red: #c21f30; --yellow: #f2b705; --accent: #c21f30;
  --inc: #1f6feb; --bjp: #e8730c; --jds: #1a8f4c; --oth: #6b7280;
  --display: "Space Grotesk", "Segoe UI", system-ui, sans-serif; --body: Inter, "Segoe UI", system-ui, sans-serif; --kn: "Noto Sans Kannada", "Nirmala UI", sans-serif }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d; --red: #ef5261; --yellow: #f5c93a; --accent: #ef5261;
  --inc: #6aa5ff; --bjp: #ff9a45; --jds: #4fcf86; --oth: #a3aab8; color-scheme: dark } }
* { box-sizing: border-box }
body { margin: 0; background: var(--bg); color: var(--fg); font: 16px/1.55 var(--body) }
.top { position: sticky; top: 0; z-index: 5; background: #11141a; color: #eceef2; border-bottom: 3px solid #f2b705; padding: 10px max(16px, env(safe-area-inset-left, 0px)); display: flex; gap: 8px 16px; flex-wrap: wrap; align-items: center; font: 600 14px/1.4 var(--body) }
.top a { color: #f5c93a; text-decoration: none }
.wrap { max-width: 860px; margin: 0 auto; padding-block: 28px 56px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); display: grid; gap: 26px }
h1, h2 { font-family: var(--display); margin: 0; line-height: 1.15; text-wrap: balance }
h1 { font-size: clamp(30px, 6vw, 44px) } h2 { font-size: 21px }
.kn { font-family: var(--kn) } .sub { color: var(--muted); display: flex; flex-wrap: wrap; gap: 4px 12px; align-items: center; margin-top: 8px }
.party { display: inline-flex; align-items: center; gap: 6px; color: var(--fg); font-weight: 600 }
.party::before { content: ""; width: 10px; height: 10px; border-radius: 50%; background: var(--oth) }
.party.Congress::before { background: var(--inc) } .party.BJP::before { background: var(--bjp) } .party.JDS::before { background: var(--jds) }
.tiles { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(190px, 100%), 1fr)); gap: 10px }
.tile { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; display: grid; gap: 2px; align-content: start }
.tile .k { font-size: 12px; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); font-weight: 600 }
.tile .k .kn { text-transform: none; letter-spacing: 0; display: block; font-weight: 400 }
.tile .v { font-family: var(--display); font-size: clamp(21px, 2.6vw, 25px); line-height: 1.2; font-weight: 700; font-variant-numeric: tabular-nums }
.tile .s { font-size: 13px; color: var(--muted) }
.box { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 18px 20px; display: grid; gap: 10px }
.box ul { margin: 0; padding-left: 20px; display: grid; gap: 6px } .box p { margin: 0 }
.ask { border-left: 4px solid var(--red) }
.btns { display: flex; flex-wrap: wrap; gap: 8px }
.btn { font: 600 15px/1 var(--body); border-radius: 999px; padding: 12px 18px; text-decoration: none; display: inline-flex; gap: 6px; align-items: center; border: 1px solid var(--fg); background: var(--fg); color: var(--bg) }
.btn.wa { background: #25d366; border-color: #25d366; color: #0b1f12 } .btn.ghost { background: transparent; color: var(--fg); border-color: var(--line) }
.fine { font-size: 13px; color: var(--muted) } .fine a, .box a { color: var(--accent) }
.box a.btn { color: var(--bg) } .box a.btn.wa { color: #0b1f12 }
.list { columns: 2 220px; gap: 24px; padding: 0; list-style: none; margin: 0 } .list li { break-inside: avoid; padding: 4px 0; border-bottom: 1px solid var(--line) }
.list a { color: var(--fg); text-decoration: none } .list a:hover { color: var(--accent) } .list small { color: var(--muted) }
"""

HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{site}brand/gandaberunda-banner.png"><link rel="canonical" href="{canon}">
<link rel="icon" type="image/svg+xml" href="../brand/mark.svg">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Space+Grotesk:wght@500;700&family=Noto+Sans+Kannada:wght@400;600&display=swap">
<style>{css}</style></head><body>
<div class="top"><a href="../index.html#find">← Gandaberunda · all 224 MLAs</a><span style="color:#9aa3b2;font-weight:400">Know Your MLA · <span class="kn">ನಿಮ್ಮ ಶಾಸಕರನ್ನು ತಿಳಿಯಿರಿ</span></span></div>
<div class="wrap">
"""


def tile(k_en, k_kn, v, s=""):
    return f'<div class="tile"><span class="k">{k_en}<span class="kn">{k_kn}</span></span><span class="v">{v}</span><span class="s">{s}</span></div>'


def form(kind, district, ac, text):
    return (GFORM + "?usp=pp_url&entry.503187352=" + quote(kind) + "&entry.1517758372=" + quote(district)
            + "&entry.604747719=" + quote(ac) + "&entry.878251699=" + quote(text))


KN_NAMES = {}  # constituency_en -> row of data/names_kn.csv (Karnataka Legislative Assembly member list)
_kp = ROOT / "data" / "names_kn.csv"
if _kp.exists():
    for _r in csv.DictReader(open(_kp, encoding="utf-8")):
        KN_NAMES[_r["constituency_en"]] = _r


def page(d):
    c, n, p = d["c"], d["n"], d["p"]
    dist = DIST.get(c, "")
    pcls = "JDS" if p == "JD(S)" else p
    g = round(100 * (d["a23"] - d["a18"]) / d["a18"]) if d.get("a18") and d.get("a23") else None
    rank = RANK.get(c)
    drank = by_dist.get(dist, [])
    aff = d.get("url") or (f"https://www.myneta.info/Karnataka2023/candidate.php?candidate_id={d['id']}" if d.get("id") else "")
    tiles = [
        tile("Declared assets", "ಘೋಷಿತ ಆಸ್ತಿ", money(d["a"]) or "Not in archive",
             (f"{rank} of {len(ranked)} MLAs by declared assets" + (f" · {drank.index(c) + 1} of {len(drank)} in {E(dist)}" if c in drank else "")) if rank else ""),
        tile("Since 2018", "2018ರಿಂದ", (("+" if g >= 0 else "") + f"{g}%") if g is not None else "—",
             f"{money(d['a18'])} in 2018" if g is not None else "Only for re-elected MLAs matched across both elections"),
        tile("Declared debts", "ಘೋಷಿತ ಸಾಲ", (money(d["l"]) if d["l"] else "0") if d["l"] is not None else "Not in archive",
             debts_note(c, d["l"])),
        tile("Declared criminal cases", "ಘೋಷಿತ ಕ್ರಿಮಿನಲ್ ಪ್ರಕರಣಗಳು", str(d["k"]) if d["k"] is not None else "Not in archive",
             "A declared case is not a conviction"),
    ]
    # district context: only HIGH-confidence official figures
    ctx = []
    rd = dd.get(DIST_ALIAS.get(dist, dist), {})
    sev = rd.get(("taluks_declared_severe", "Kharif 2023 (monsoon 2023)"))
    mod = rd.get(("taluks_declared_moderate", "Kharif 2023 (monsoon 2023)"))
    if sev and mod:
        ctx.append(f'<li><b>Drought, 2023:</b> in the first state declaration (13 Sep 2023), {int(float(sev["value"]))} taluks of {E(dist)} were declared severely drought-hit and {int(float(mod["value"]))} moderately. More taluks were added later that year, so this may undercount. <a href="{E(sev["source_url"])}" target="_blank" rel="noopener">Government order</a></li>')
    rep = rd.get(("claims_reported_cr", "2020-21 to 2024-25 (cumulative)"))
    paid = rd.get(("claims_paid_cr", "2020-21 to 2024-25 (cumulative)"))
    if rep and paid:
        ctx.append(f'<li><b>Crop insurance, 2020-21 to 2024-25:</b> claims of ₹{float(rep["value"]):,.2f} crore were reported for farmers in {E(dist)} and ₹{float(paid["value"]):,.2f} crore paid, by 31 Dec 2025. <a href="{E(paid["source_url"])}" target="_blank" rel="noopener">Lok Sabha answer, 3 Feb 2026</a></li>')
    sat = SAT.get(re.sub(r"\s*\((SC|ST)\)$", "", c))
    sat_html = (f'<p><b>From space:</b> {E(c)} has been compared in satellite pictures from 2019 and 2026. <a href="../reports/satellite/{sat}/">See {E(c)} from space →</a></p>' if sat else
                f'<p><b>From space:</b> {E(c)} has not been checked in satellite pictures yet. <a href="{E(form("Check my constituency from space", dist, c, "Please compare " + c + " from space next."))}" target="_blank" rel="noopener">Ask for {E(c)} →</a> <span class="fine">(short form, no account needed)</span></p>')
    nn = norm(n)
    also = [f'<a href="../index.html#{sid}">{ALSO_LABEL[sid]}</a>' for sid, txt in ALSO.items() if (len(nn) > 6 and nn in txt) or sid in ALSO_EXTRA.get(c, ())]
    by = f' · elected in a by-election, {E(d["by"])}' if d.get("by") else ""
    url = SITE + "mla/" + slug(c) + ".html"
    kr = KN_NAMES.get(c, {})
    n_kn, c_kn = kr.get("name_kn", ""), kr.get("constituency_kn", "")
    card = ROOT / "cards" / "mla" / f"{slug(c)}-en.png"
    og_img = f"{SITE}cards/mla/{slug(c)}-en.png" if card.exists() else f"{SITE}brand/gandaberunda-banner.png"
    wa_kn = (f"{n_kn or n} ({c_kn or c}) ವರದಿ ಕಾರ್ಡ್: ಘೋಷಿತ ಆಸ್ತಿ " + (money(d['a']).replace('crore', 'ಕೋಟಿ').replace('lakh', 'ಲಕ್ಷ') if d['a'] is not None else "ಲಭ್ಯವಿಲ್ಲ")
             + (f", 2018ರಿಂದ {'+' if g >= 0 else ''}{g}%" if g is not None else "")
             + f", ಘೋಷಿತ ಕ್ರಿಮಿನಲ್ ಪ್ರಕರಣಗಳು {d['k'] if d['k'] is not None else '?'}. ಕೆಲಸ ತೋರಿಸಿ, ಆಮೇಲೆ ಮತ. {url}")
    wa = (f"{n} ({c}) report card: declared assets {money(d['a']) or 'not in archive'}"
          + (f", {'+' if g >= 0 else ''}{g}% since 2018" if g is not None else "") + f", {d['k'] if d['k'] is not None else '?'} declared criminal cases. Show me the work, then my vote. {url}")
    title = (f"{n} ({n_kn}), {c} ({c_kn}) MLA: declared assets and cases · Gandaberunda" if n_kn and c_kn
             else f"{n}, {c} MLA: declared assets and cases · Gandaberunda")
    desc = (f"{n} ({p}), MLA for {c}, {dist} district. Declared assets {money(d['a']) or 'not in archive'}"
            + (f", {'+' if g >= 0 else ''}{g}% since 2018" if g is not None else "") + f"; {d['k'] if d['k'] is not None else 'no'} declared criminal cases. From sworn affidavits.")
    body = f"""<div><h1>{E(n)}</h1>{f'<p class="kn" lang="kn" style="font-size:22px;font-weight:600;margin:4px 0 0">{E(n_kn)} · {E(c_kn)}</p>' if n_kn else ''}
<div class="sub"><span>MLA for <b>{E(c)}</b></span><span class="party {E(pcls)}">{E(p)}</span><span>{E(dist)} district{by}</span>
<span class="kn">{E(PARTY_KN.get(p, p))} · {E(dist)} ಜಿಲ್ಲೆ</span></div></div>
<div class="tiles">{''.join(tiles)}</div>
<div class="box"><h2>What the record shows in {E(dist)} district <span class="kn" style="font-size:15px;color:var(--muted);font-weight:400">ಜಿಲ್ಲೆಯ ದಾಖಲೆ</span></h2>
{'<ul>' + ''.join(ctx) + '</ul>' if ctx else '<p class="fine">No district figure has passed our checks yet.</p>'}
{sat_html}
{('<p>Also on this site: ' + ' · '.join(also) + '</p>') if also else ''}</div>
<div class="box ask"><h2>Questions to ask <span class="kn" style="font-size:15px;color:var(--muted);font-weight:400">ಕೇಳಬೇಕಾದ ಪ್ರಶ್ನೆಗಳು</span></h2>
<ul><li>What work have you done in this constituency since 2023? Show me. <span class="kn">2023ರಿಂದ ಈ ಕ್ಷೇತ್ರದಲ್ಲಿ ನೀವು ಮಾಡಿದ ಕೆಲಸ ಏನು? ತೋರಿಸಿ.</span></li>
<li>Did you file this year's asset statement with the Lokayukta? <span class="kn">ಈ ವರ್ಷದ ಆಸ್ತಿ ಘೋಷಣೆಯನ್ನು ಲೋಕಾಯುಕ್ತಕ್ಕೆ ಸಲ್ಲಿಸಿದ್ದೀರಾ?</span></li>
<li>When will the pending project in our district be finished, in writing? <span class="kn">ನಮ್ಮ ಜಿಲ್ಲೆಯ ಬಾಕಿ ಯೋಜನೆ ಯಾವಾಗ ಮುಗಿಯುತ್ತದೆ? ಬರೆದು ಕೊಡಿ.</span></li></ul></div>
<div class="box"><h2>Know something about {E(c)}? <span class="kn" style="font-size:15px;color:var(--muted);font-weight:400">ನಿಮ್ಮ ಅಭಿಪ್ರಾಯ ತಿಳಿಸಿ</span></h2>
<p>A project paid for but not built, a scheme not reaching people, something we should check. It goes to the Gandaberunda team only; no account or name needed. Send records, not rumours.</p>
<div class="btns"><a class="btn" href="{E(form("A suggestion: what to dig into next", dist, c, ""))}" target="_blank" rel="noopener">Tell us about {E(c)}</a>
<a class="btn wa" href="https://wa.me/?text={quote(wa)}" target="_blank" rel="noopener">Share on WhatsApp</a>
<a class="btn wa kn" lang="kn" href="https://wa.me/?text={quote(wa_kn)}" target="_blank" rel="noopener">ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಹಂಚಿ</a></div></div>
<p style="margin:0"><a href="../index.html#join"><b>Have your say</b>: tell us what to check next in {E(c)} →</a> <span class="kn" lang="kn">ನಿಮ್ಮ ಅಭಿಪ್ರಾಯ ತಿಳಿಸಿ</span></p>
<p class="fine">Figures are what the MLA declared in a sworn affidavit to the Election Commission{', archived by ADR at <a href="' + E(aff) + '" target="_blank" rel="noopener">myneta.info</a>' if aff and 'myneta' in aff else (', <a href="' + E(aff) + '" target="_blank" rel="noopener">affidavit</a>' if aff else '')}. Nobody audits them. Declared wealth is not evidence of wrongdoing: growth often reflects land being revalued. A declared case is not a conviction. District figures are about the district, not about the MLA. Errors: <a href="../index.html#join">tell us</a>. Gandaberunda is independent and takes no money from any party.</p>
"""
    return HEAD.format(title=E(title), desc=E(desc), site=SITE, canon=url, css=CSS).replace(f"{SITE}brand/gandaberunda-banner.png", og_img, 1) + body + '</div><script data-goatcounter="https://gandaberunda.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>\n</body></html>\n'


def _codes(s):
    """Search Console / GoatCounter slot (tools/site_codes.py; empty until a code is set)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("site_codes", ROOT / "tools" / "site_codes.py")
    sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
    return s.replace("</head>", sc.head_block() + "</head>", 1)


def main():
    OUT.mkdir(exist_ok=True)
    slugs = {}
    for d in D:
        s = slug(d["c"]); assert s not in slugs, (s, d["c"]); slugs[s] = d
        (OUT / f"{s}.html").write_text(_codes(page(d)), encoding="utf-8", newline="\n")
    rows = "".join(f'<li><a href="{slug(d["c"])}.html">{E(d["c"])}</a> <small>· {E(d["n"])} · {E(d["p"])}</small></li>'
                   for d in sorted(D, key=lambda d: d["c"]))
    idx = HEAD.format(title="All 224 MLAs: report cards · Gandaberunda", desc="One page per Karnataka MLA: declared assets, debts, criminal cases, growth since 2018, and district records.",
                      site=SITE, canon=SITE + "mla/", css=CSS)
    idx += f'<h1>Report cards: all 224 MLAs</h1><p class="fine">One page per constituency, from sworn affidavits and official district records. <span class="kn">ಎಲ್ಲ 224 ಶಾಸಕರ ವರದಿ ಕಾರ್ಡ್‌ಗಳು</span></p><ul class="list">{rows}</ul></div><script data-goatcounter="https://gandaberunda.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>\n</body></html>\n'
    (OUT / "index.html").write_text(_codes(idx), encoding="utf-8", newline="\n")
    # sitemap helps search engines find every page
    urls = [SITE] + [SITE + "mla/" + s + ".html" for s in slugs] + [SITE + "farmers.html", SITE + "members.html"] + [SITE + "members/" + q.name for q in sorted((ROOT / "members").glob("*.html"))]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    print("ok", len(slugs), "pages")


if __name__ == "__main__":
    main()
