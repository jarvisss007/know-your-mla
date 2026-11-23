"""Build DRAFT_officials_tracker.html and its Kannada twin
DRAFT_officials_tracker_kn.html from tracker.csv.

Run from the repo root:  py research/officials_tracker/build.py
The page is a DRAFT for the owner's review. It carries designations only, no names.
"""
import csv
import html
import pathlib
from collections import Counter
from urllib.parse import urlparse

HERE = pathlib.Path(__file__).parent
rows = list(csv.DictReader(open(HERE / "tracker.csv", encoding="utf-8")))
rows.sort(key=lambda r: (r["id"][:10], int(r["id"][11:])))

LADDER = ["Action taken", "Suspended or beyond", "Chargesheet filed", "Sanction to prosecute", "Trial under way", "Verdict"]
STAGE_RANK = {"Raided": 0, "Searched": 0, "Arrested": 0, "Trap laid": 0, "Suspended": 1, "Chargesheet filed": 2,
              "Sanction to prosecute": 3, "Trial under way": 4, "Verdict": 5}


def group(r):
    p, d = r["post"].lower(), r["department"].lower()
    if "engineer" in p:
        return "Engineers"
    if "excise" in d:
        return "Excise"
    if "forest" in p or "forest" in d or "conservator" in p:
        return "Forest"
    if "police" in d:
        return "Police"
    if any(k in d for k in ("revenue", "registration", "land records")):
        return "Revenue and registration"
    if any(k in d for k in ("panchayat", "local bodies", "town planning", "housing")) or "town planning" in p:
        return "Local bodies and planning"
    return "Other departments"


def num(v):
    try:
        return float(v)
    except ValueError:
        return None


def e(s):
    return html.escape(s, quote=True)


n = len(rows)
days = len({r["action_date"] for r in rows})
def claimed(r):
    """Total assets where reported, otherwise the disproportionate-assets (DA) figure."""
    a = num(r["assets_claimed_crore"])
    return (a, "") if a is not None else (num(r["da_claimed_crore"]), " (DA)")


valued = [claimed(r)[0] for r in rows if claimed(r)[0] is not None]
total = sum(valued)
moved = [r for r in rows if r["followup_url"]]
unchecked = sum(1 for r in rows if r["followup"].startswith("Follow-up not yet checked"))
unchecked_note = f" {unchecked} officials added late have not been checked yet." if unchecked else " Every official in the table has been checked at least once."
reached = [sum(1 for r in rows if STAGE_RANK[r["stage"]] >= i) for i in range(len(LADDER))]
groups = Counter(group(r) for r in rows).most_common()
gmax = groups[0][1]
first, last = rows[0]["action_date"], rows[-1]["action_date"]
checked = max(max(r["checked_on"] for r in rows), max(r["followup_checked"] for r in rows))
# Reports used for figures or details in the notes, beyond each row's own source.
OTHER_SOURCES = {
    "https://www.countryandpolitics.in/2026/04/08/lokayukta-officials-raids-several-officials-across-state-against-8-govt-officials-unearthed-disproportionate-assets-worth-rs-36-9-crores",
    "https://medicaldialogues.in/amp/news/industry/pharma/lokayukta-raids-assistant-drug-controller-unearths-rs-337-crore-disproportionate-assets-168317",
    "https://newsable.asianetnews.com/india/karnataka-lokayukta-raids-gescom-aee-retired-hostel-superintendent-articleshow-0dlex4i",
}
sources = sorted({r["source_url"] for r in rows} | {r["followup_url"] for r in rows if r["followup_url"]} | OTHER_SOURCES)

MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def d(iso):
    y, m, dd = iso.split("-")
    return f"{int(dd)} {MONTHS[int(m) - 1]} {y}"


# Where the money was found: asset types the agency reported, per official (assets.csv).
assets = list(csv.DictReader(open(HERE / "assets.csv", encoding="utf-8")))
na = len(assets)


def present(col):
    return [a for a in assets if a[col].strip()]


def colsum(col):
    return sum(num(a[col]) or 0 for a in assets if num(a[col]) is not None)


def lakh(v):
    return f"Rs {v / 100:.2f} crore" if v >= 100 else f"Rs {v:.0f} lakh"


def lakh_kn(v):
    return f"₹{v / 100:.2f} ಕೋಟಿ" if v >= 100 else f"₹{v:.0f} ಲಕ್ಷ"


money_rows = [
    ("Farmland", len(present("farmland_acres")), f"at least {colsum('farmland_acres'):.0f} acres where the area was given"),
    ("Houses or flats", len(present("houses")), f"at least {colsum('houses'):.0f} where counted"),
    ("House sites and plots", len(present("sites")), f"at least {colsum('sites'):.0f} where counted"),
    ("Gold, silver or jewellery", len(present("gold_silver_lakh")), f"at least {lakh(colsum('gold_silver_lakh'))} where valued"),
    ("Cash found in the searches", len(present("cash_lakh")), f"at least {lakh(colsum('cash_lakh'))} where valued"),
    ("Bank deposits and investments", len(present("deposits_lakh")), f"at least {lakh(colsum('deposits_lakh'))} where valued"),
    ("A business or commercial property", len(present("business")), "; ".join(sorted({a['business'] for a in present('business')}))),
    ("Assets reported in relatives' or associates' hands", len(present("others_names")), "as stated in the report; never attributed to a named person here"),
]
# Kannada version of the same rows. The business list is CSV data and stays in English.
money_rows_kn = [
    ("ಕೃಷಿ ಭೂಮಿ", money_rows[0][1], f"ವಿಸ್ತೀರ್ಣ ನೀಡಿರುವಲ್ಲಿ ಕನಿಷ್ಠ {colsum('farmland_acres'):.0f} ಎಕರೆ"),
    ("ಮನೆಗಳು ಅಥವಾ ಫ್ಲ್ಯಾಟ್‌ಗಳು", money_rows[1][1], f"ಎಣಿಕೆ ನೀಡಿರುವಲ್ಲಿ ಕನಿಷ್ಠ {colsum('houses'):.0f}"),
    ("ನಿವೇಶನಗಳು ಮತ್ತು ಪ್ಲಾಟ್‌ಗಳು", money_rows[2][1], f"ಎಣಿಕೆ ನೀಡಿರುವಲ್ಲಿ ಕನಿಷ್ಠ {colsum('sites'):.0f}"),
    ("ಚಿನ್ನ, ಬೆಳ್ಳಿ ಅಥವಾ ಆಭರಣ", money_rows[3][1], f"ಮೌಲ್ಯ ನೀಡಿರುವಲ್ಲಿ ಕನಿಷ್ಠ {lakh_kn(colsum('gold_silver_lakh'))}"),
    ("ಶೋಧದಲ್ಲಿ ಸಿಕ್ಕ ನಗದು", money_rows[4][1], f"ಮೌಲ್ಯ ನೀಡಿರುವಲ್ಲಿ ಕನಿಷ್ಠ {lakh_kn(colsum('cash_lakh'))}"),
    ("ಬ್ಯಾಂಕ್ ಠೇವಣಿಗಳು ಮತ್ತು ಹೂಡಿಕೆಗಳು", money_rows[5][1], f"ಮೌಲ್ಯ ನೀಡಿರುವಲ್ಲಿ ಕನಿಷ್ಠ {lakh_kn(colsum('deposits_lakh'))}"),
    ("ವ್ಯಾಪಾರ ಅಥವಾ ವಾಣಿಜ್ಯ ಆಸ್ತಿ", money_rows[6][1], money_rows[6][2]),
    ("ಸಂಬಂಧಿಕರು ಅಥವಾ ಸಹವರ್ತಿಗಳ ಕೈಯಲ್ಲಿ ಇರುವುದಾಗಿ ವರದಿಯಾದ ಆಸ್ತಿ", money_rows[7][1], "ವರದಿಯಲ್ಲಿ ಹೇಳಿದಂತೆ; ಇಲ್ಲಿ ಯಾವುದೇ ಹೆಸರಿಸಿದ ವ್ಯಕ್ತಿಗೆ ಆರೋಪಿಸಿಲ್ಲ"),
]

# Kannada labels for the fixed vocabularies the page computes or the CSV draws from a short list.
# Anything not in these maps falls back to the English text.
MONTHS_KN = ["ಜನವರಿ", "ಫೆಬ್ರವರಿ", "ಮಾರ್ಚ್", "ಏಪ್ರಿಲ್", "ಮೇ", "ಜೂನ್",
             "ಜುಲೈ", "ಆಗಸ್ಟ್", "ಸೆಪ್ಟೆಂಬರ್", "ಅಕ್ಟೋಬರ್", "ನವೆಂಬರ್", "ಡಿಸೆಂಬರ್"]
LADDER_KN = ["ಕ್ರಮ ಕೈಗೊಳ್ಳಲಾಗಿದೆ", "ಅಮಾನತು ಅಥವಾ ಅದರಾಚೆ", "ದೋಷಾರೋಪಣ ಪಟ್ಟಿ ಸಲ್ಲಿಕೆ",
             "ಅಭಿಯೋಜನಾ ಮಂಜೂರಾತಿ", "ವಿಚಾರಣೆ ನಡೆಯುತ್ತಿದೆ", "ತೀರ್ಪು"]
GROUP_KN = {"Engineers": "ಎಂಜಿನಿಯರ್‌ಗಳು", "Excise": "ಅಬಕಾರಿ", "Forest": "ಅರಣ್ಯ", "Police": "ಪೊಲೀಸ್",
            "Revenue and registration": "ಕಂದಾಯ ಮತ್ತು ನೋಂದಣಿ",
            "Local bodies and planning": "ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು ಮತ್ತು ನಗರ ಯೋಜನೆ",
            "Other departments": "ಇತರ ಇಲಾಖೆಗಳು"}
STAGE_KN = {"Raided": "ದಾಳಿ", "Trap laid": "ಟ್ರ್ಯಾಪ್", "Searched": "ಶೋಧ", "Arrested": "ಬಂಧನ", "Suspended": "ಅಮಾನತು",
            "Chargesheet filed": "ದೋಷಾರೋಪಣ ಪಟ್ಟಿ ಸಲ್ಲಿಕೆ", "Sanction to prosecute": "ಅಭಿಯೋಜನಾ ಮಂಜೂರಾತಿ",
            "Trial under way": "ವಿಚಾರಣೆ ನಡೆಯುತ್ತಿದೆ", "Verdict": "ತೀರ್ಪು"}
ACTION_KN = {"DA raid": "ಆದಾಯ ಮೀರಿದ ಆಸ್ತಿ ದಾಳಿ", "Trap (bribe)": "ಟ್ರ್ಯಾಪ್ (ಲಂಚ)",
             "Departmental (posting audio)": "ಇಲಾಖಾ ಕ್ರಮ (ವರ್ಗಾವಣೆ ಕುರಿತ ಆಡಿಯೊ)",
             "ED search (money laundering)": "ಇಡಿ ಶೋಧ (ಅಕ್ರಮ ಹಣ ವರ್ಗಾವಣೆ)",
             "Arrest (CID)": "ಬಂಧನ (ಸಿಐಡಿ)", "Arrest (ED)": "ಬಂಧನ (ಇಡಿ)",
             "Named in ED prosecution complaint": "ಇಡಿ ಅಭಿಯೋಜನಾ ದೂರಿನಲ್ಲಿ ಹೆಸರಿದೆ"}
AGENCY_KN = {"Lokayukta": "ಲೋಕಾಯುಕ್ತ", "ED": "ಇಡಿ", "Police (internal)": "ಪೊಲೀಸ್ (ಆಂತರಿಕ)", "CID; ED": "ಸಿಐಡಿ; ಇಡಿ"}


def d_kn(iso):
    y, m, dd = iso.split("-")
    return f"{int(dd)} {MONTHS_KN[int(m) - 1]} {y}"


def fragments(kn):
    """The data-driven parts of the page, in English or Kannada. CSV text stays as it is."""
    dt = d_kn if kn else d
    money_html = "".join(
        f"<tr><td>{e(k)}</td><td class=\"n\">{f'{na}ರಲ್ಲಿ {c}' if kn else f'{c} of {na}'}</td><td>{e(dd)}</td></tr>"
        for k, c, dd in (money_rows_kn if kn else money_rows))
    ladder_html = "".join(
        f'<li class="{"zero" if c == 0 else ""}"><b>{c}</b><span>{e(name)}</span></li>'
        for name, c in zip(LADDER_KN if kn else LADDER, reached))
    bars_html = "".join(
        f'<div class="brow"><span>{e(GROUP_KN[g] if kn else g)}</span><div class="bar"><i style="width:{c / gmax * 100:.0f}%"></i></div><b>{c}</b></div>'
        for g, c in groups)
    since, src_word, not_stated = ("ಅಂದಿನಿಂದ:", "ಮೂಲ", "ಹೇಳಿಲ್ಲ") if kn else ("Since then:", "source", "not stated")
    tr = (lambda m, k: m.get(k, k)) if kn else (lambda m, k: k)
    body = []
    for r in rows:
        a, tag = claimed(r)
        fu = e(r["followup"])
        if r["followup_url"]:
            fu = f'{fu} <a href="{e(r["followup_url"])}">{src_word}</a> · {dt(r["followup_date"])}'
        host = urlparse(r["source_url"]).netloc.replace("www.", "")
        note = f'<div class="nt">{e(r["notes"])}</div>' if r["notes"] else ""
        body.append(
            f'<tr><td class="dt">{dt(r["action_date"])}</td>'
            f'<td><strong>{e(r["post"])}</strong><div class="sub">{e(r["department"])} · {e(r["district"])}</div>{note}<div class="fu"><b>{since}</b> {fu}</div></td>'
            f'<td>{e(tr(ACTION_KN, r["action"]))}<div class="sub">{e(tr(AGENCY_KN, r["agency"]))}</div></td>'
            f'<td class="n">{f"{a:.2f}{tag}" if a is not None else not_stated}</td>'
            f'<td><span class="st s{STAGE_RANK[r["stage"]]}">{e(tr(STAGE_KN, r["stage"]))}</span><div class="sub">{dt(r["stage_date"])}</div></td>'
            f'<td><a href="{e(r["source_url"])}">{e(host)}</a><div class="sub">{dt(r["source_published"])}</div></td></tr>')
    return money_html, ladder_html, bars_html, "".join(body)


src_html = "".join(f'<li><a href="{e(u)}">{e(u)}</a></li>' for u in sources)

FONTS_EN = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap"
FONTS_KN = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Noto+Sans+Kannada:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap"
STYLE = """<style>
/* One reading column. The ladder is the page: how far each case has got since the raid. */
:root {
  --bg: #f5f6f8; --surface: #ffffff; --fg: #161a22; --muted: #5b6474; --line: #dde1e8;
  --red: #c21f30; --yellow: #f2b705; --track: #e3e6ec; --ok: #1a8f4c; --warn: #b45309;
  --display: "Space Grotesk", "Segoe UI", system-ui, sans-serif;
  --body: Inter, "Segoe UI", system-ui, sans-serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d;
  --red: #ef5261; --yellow: #f5c93a; --track: #2b313d; --ok: #4fcf86; --warn: #f0a04b; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d;
  --red: #ef5261; --yellow: #f5c93a; --track: #2b313d; --ok: #4fcf86; --warn: #f0a04b; color-scheme: dark }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--fg); font: 16px/1.55 var(--body); padding: 28px 16px 64px; }
.wrap { max-width: 920px; margin: 0 auto; display: flex; flex-direction: column; gap: 40px; }
a { color: inherit; text-underline-offset: 3px; }
a:focus-visible { outline: 2px solid var(--red); outline-offset: 2px; }
h1, h2 { font-family: var(--display); text-wrap: balance; margin: 0; }
h1 { font-size: clamp(2.2rem, 7vw, 3.6rem); line-height: 1; letter-spacing: -0.02em; }
h1 span { color: var(--red); }
h2 { font-size: 1.5rem; }
p { margin: 0; max-width: 66ch; }
.eyebrow { font-size: .75rem; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); font-weight: 600; }
.draft { display: inline-block; background: var(--yellow); color: #161a22; font-weight: 600; font-size: .8rem; padding: 3px 10px; border-radius: 3px; letter-spacing: .04em; }
header, section { display: flex; flex-direction: column; gap: 14px; }
.lede { font-size: 1.1rem; }
.muted { color: var(--muted); font-size: .9rem; }
.ladder { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); border-block: 2px solid var(--fg); }
.ladder li { padding: 16px 12px 16px 0; display: flex; flex-direction: column; gap: 4px; min-width: 0; }
.ladder b { font: 700 2.6rem/1 var(--display); font-variant-numeric: tabular-nums; }
.ladder li.zero b { color: var(--red); }
.ladder span { font-size: .88rem; }
.brow { display: grid; grid-template-columns: minmax(0, 190px) minmax(0, 1fr) 2.5ch; gap: 12px; align-items: center; font-size: .92rem; }
.brow b { font-variant-numeric: tabular-nums; text-align: right; }
.bar { height: 12px; background: var(--track); border-radius: 2px; overflow: hidden; }
.bar i { display: block; height: 100%; background: var(--red); }
.tbl { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: .9rem; min-width: 760px; }
th, td { text-align: left; padding: 10px 14px 10px 0; border-top: 1px solid var(--line); vertical-align: top; }
th { font-size: .75rem; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); border-top: 2px solid var(--fg); }
td.n, th.n { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
td.dt { white-space: nowrap; font-variant-numeric: tabular-nums; }
.fu { font-size: .82rem; margin-top: 6px; }
.nt { overflow-wrap: anywhere; }
.sub, .nt { color: var(--muted); font-size: .8rem; }
.st { font-weight: 600; white-space: nowrap; }
.st.s1 { color: var(--warn); }
.st.s2, .st.s3, .st.s4, .st.s5 { color: var(--ok); }
ul { margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 8px; max-width: 74ch; }
.src { font-size: .82rem; word-break: break-all; }
footer { border-top: 2px solid var(--fg); padding-top: 14px; }
</style>"""
# The Kannada page puts Noto Sans Kannada (then the Windows Kannada fonts) behind the Latin faces.
STYLE_KN = (STYLE
            .replace('--display: "Space Grotesk", "Segoe UI"', '--display: "Space Grotesk", "Noto Sans Kannada", "Nirmala UI", "Tunga", "Segoe UI"')
            .replace('--body: Inter, "Segoe UI"', '--body: Inter, "Noto Sans Kannada", "Nirmala UI", "Tunga", "Segoe UI"'))
assert STYLE_KN != STYLE

# ---------------------------------------------------------------- English page
money_html, ladder_html, bars_html, body_html = fragments(kn=False)
page = f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>After the Raid</title>
<link rel="stylesheet" href="{FONTS_EN}">
{STYLE}

<div class="wrap">
<header>
  <div><span class="draft">DRAFT · NOT PUBLISHED</span></div>
  <div class="eyebrow">Gandaberunda · Karnataka officials · reports read up to {d(checked)}</div>
  <h1>After the <span>raid</span></h1>
  <p class="lede">{n} Karnataka officials were raided, trapped, searched, arrested, suspended or charged on {days} days between {d(first)} and {d(last)}, in the reports read so far. This page follows each one from that first day towards a verdict.</p>
  <p class="muted">A raid or an arrest is an allegation, not a finding of guilt. Asset figures are the agency's first-day estimates. The page gives the post, not the person: names are in the linked reports and are added here only after the FIR and the person's reply are checked.</p>
</header>

<section>
  <h2>The government's own count</h2>
  <ol class="ladder">
    <li><b>1,248</b><span>Lokayukta cases against officials, 10 Sep 2022 to 13 Aug 2026</span></li>
    <li><b>364</b><span>Chargesheet filed</span></li>
    <li><b>648</b><span>Still under investigation</span></li>
    <li><b>218</b><span>Stayed by courts</span></li>
    <li class="zero"><b>0</b><span>Government servants held guilty so far</span></li>
  </ol>
  <p class="muted">From the Chief Minister's written reply to Legislative Council unstarred question 452 (628), 20 Aug 2026, read in the original: 939 bribery-trap cases and 309 disproportionate-assets cases, 1,451 officers and employees in all; 18 more cases were closed. <a href="https://kla.kar.nic.in/council/Replies/unstarred/20082026/usq628(20082026).pdf">The reply (PDF, Kannada)</a>. Press reports of this reply mislabelled the 939 trap cases as assets cases.</p>
</section>

<section>
  <h2>How far the 2026 cases have got</h2>
  <ol class="ladder">{ladder_html}</ol>
  <p class="muted">Each number counts officials whose case reached that step or a later one, as far as the reports read show. A zero means no report of that step was found. It does not mean the step has not happened: the follow-up check on {d(checked)} was a web search by name in English and Kannada. It could not reach Prajavani, Deccan Herald or the Lokayukta's own website, and did not cover court case-status sites.{unchecked_note} {len(moved)} rows carry a later development of another kind (a court order, further searches, a posting, a separate case); each is shown in the table with its source.</p>
</section>

<section>
  <h2>How such cases usually end</h2>
  <p class="muted">The state's own figures for corruption cases, all agencies, as reported to the National Crime Records Bureau for 2023 (the latest year published). They show what the cases above are up against.</p>
  <ol class="ladder">
    <li><b>362</b><span>new corruption cases registered in Karnataka in 2023 (245 bribery traps, 84 assets cases)</span></li>
    <li><b>195</b><span>cases charge-sheeted in 2023; 1,448 were still under investigation at the year's end</span></li>
    <li><b>120</b><span>trials finished in 2023, out of 1,690 cases waiting for trial</span></li>
    <li class="zero"><b>35</b><span>ended in conviction: 29.2%, against 46.2% for India. 74 ended in acquittal</span></li>
  </ol>
  <p class="muted">At the end of 2023, 1,529 Karnataka corruption cases were pending trial, 90.5% of all cases due for trial that year. At the 2023 pace of 120 finished trials a year, that is about 13 years of work (our arithmetic). That year courts also quashed 28 cases and stayed 70. Of the people involved, 43 were convicted and 4 were dismissed or removed from service. Source: <a href="https://www.ncrb.mha.gov.in/uploads/files/2CrimeinIndia2023PartII.pdf">NCRB, Crime in India 2023, Vol. II, Tables 8C.2 to 8C.5 (pp. 779-784)</a>; Karnataka rows checked against the page images on 18 Nov 2026. These are all corruption cases in the state, not only the officials on this page.</p>
</section>

<section>
  <h2>Where the money was found</h2>
  <p class="muted">For {na} of the {n} officials, a report listed what kind of assets the agency found. This is what those lists contain. It shows where wealth is kept, not that any of it is illegal: each figure is a first-day claim that the case still has to prove.</p>
  <div class="tbl"><table>
    <thead><tr><th>Kind of asset</th><th class="n">Officials</th><th>Amount reported</th></tr></thead>
    <tbody>{money_html}</tbody>
  </table></div>
  <p class="muted">Counts are minimums: many reports list an asset without a number or a value. Per-official detail and sources are in assets.csv beside this page.</p>
</section>

<section>
  <h2>Which posts turn up</h2>
  {bars_html}
  <p class="muted">First estimates add up to Rs {total:.2f} crore across the {len(valued)} officials for whom a figure was reported (total assets where given, otherwise the disproportionate-assets figure, marked DA); the other {n - len(valued)} had no figure in the report.</p>
</section>

<section>
  <h2>Every official, by date</h2>
  <div class="tbl"><table>
    <thead><tr><th>Date</th><th>Post</th><th>Action</th><th class="n">Assets claimed (Rs crore)</th><th>Last step reported</th><th>Source</th></tr></thead>
    <tbody>{body_html}</tbody>
  </table></div>
</section>

<section>
  <h2>What is missing</h2>
  <ul>
    <li>This is not every case of 2026. No assets raid was found for May 2026. A Mysuru raid reported on 5 Feb 2026 is a lead only. Bribery-trap cases are not tracked systematically: there were many more in 2026 than the few shown here.</li>
    <li>The follow-up check was a press search. Chargesheets, sanction requests, court stays and verdicts are rarely reported and must come from Lokayukta replies, RTI answers and court records. The outcome of the High Court hearing of 22 Jul 2026 in the excise matter was not found.</li>
    <li>Follow-up entries marked UNVERIFIED rest on a single outlet. The arrest in a separate case is matched by name and former post.</li>
    <li>Several asset figures come from one small outlet, and reports of the same raid often differ on the post, the department or the amount; the notes say where.</li>
  </ul>
</section>

<footer>
  <p class="muted">Sources</p>
  <ul class="src">{src_html}</ul>
</footer>
</div>
</html>
"""
out = HERE / "DRAFT_officials_tracker.html"
out.write_text(page, encoding="utf-8")

# ---------------------------------------------------------------- Kannada page
# Same figures and sources. Table data from the CSV (posts, departments, places, notes,
# follow-up text) stays in English; the page says so. The badge text is fixed: the publisher swaps it.
unchecked_note_kn = (f" ತಡವಾಗಿ ಸೇರಿಸಿದ {unchecked} ಅಧಿಕಾರಿಗಳನ್ನು ಇನ್ನೂ ಪರಿಶೀಲಿಸಿಲ್ಲ." if unchecked
                     else " ಕೋಷ್ಟಕದಲ್ಲಿರುವ ಪ್ರತಿಯೊಬ್ಬ ಅಧಿಕಾರಿಯನ್ನೂ ಕನಿಷ್ಠ ಒಮ್ಮೆ ಪರಿಶೀಲಿಸಲಾಗಿದೆ.")
money_html, ladder_html, bars_html, body_html = fragments(kn=True)
page_kn = f"""<!doctype html>
<html lang="kn">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ದಾಳಿಯ ನಂತರ</title>
<link rel="stylesheet" href="{FONTS_KN}">
{STYLE_KN}

<div class="wrap">
<header>
  <div><span class="draft">ಕರಡು · ಪ್ರಕಟಿಸಿಲ್ಲ</span></div>
  <div class="eyebrow">ಗಂಡಭೇರುಂಡ · ಕರ್ನಾಟಕದ ಅಧಿಕಾರಿಗಳು · {d_kn(checked)}ರವರೆಗಿನ ವರದಿಗಳನ್ನು ಓದಲಾಗಿದೆ</div>
  <h1><span>ದಾಳಿಯ</span> ನಂತರ</h1>
  <p class="lede">ಇದುವರೆಗೆ ಓದಿದ ವರದಿಗಳ ಪ್ರಕಾರ, {d_kn(first)} ಮತ್ತು {d_kn(last)} ನಡುವಿನ {days} ದಿನಗಳಲ್ಲಿ ಕರ್ನಾಟಕದ {n} ಅಧಿಕಾರಿಗಳ ಮೇಲೆ ದಾಳಿ, ಟ್ರ್ಯಾಪ್, ಶೋಧ, ಬಂಧನ, ಅಮಾನತು ಅಥವಾ ಆರೋಪ ದಾಖಲಾಗಿದೆ. ಆ ಮೊದಲ ದಿನದಿಂದ ತೀರ್ಪಿನತ್ತ ಪ್ರತಿಯೊಂದು ಪ್ರಕರಣವನ್ನೂ ಈ ಪುಟ ಹಿಂಬಾಲಿಸುತ್ತದೆ.</p>
  <p class="muted">ದಾಳಿ ಅಥವಾ ಬಂಧನ ಒಂದು ಆರೋಪ ಮಾತ್ರ, ತಪ್ಪಿತಸ್ಥರೆಂಬ ತೀರ್ಮಾನವಲ್ಲ. ಆಸ್ತಿಯ ಅಂಕಿಗಳು ತನಿಖಾ ಸಂಸ್ಥೆಯ ಮೊದಲ ದಿನದ ಅಂದಾಜುಗಳು. ಈ ಪುಟ ವ್ಯಕ್ತಿಯ ಹೆಸರನ್ನಲ್ಲ, ಹುದ್ದೆಯನ್ನು ನೀಡುತ್ತದೆ: ಹೆಸರುಗಳು ಲಿಂಕ್ ಮಾಡಿದ ವರದಿಗಳಲ್ಲಿವೆ; ಎಫ್‌ಐಆರ್ ಮತ್ತು ಆ ವ್ಯಕ್ತಿಯ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿದ ನಂತರವೇ ಅವನ್ನು ಇಲ್ಲಿ ಸೇರಿಸಲಾಗುತ್ತದೆ.</p>
  <p class="muted">ಪ್ರಕರಣಗಳ ವಿವರಗಳು (ಹುದ್ದೆ, ಇಲಾಖೆ, ಸ್ಥಳ, ಟಿಪ್ಪಣಿಗಳು ಮತ್ತು ನಂತರದ ಬೆಳವಣಿಗೆಗಳು) ಕೋಷ್ಟಕದಲ್ಲಿ ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿವೆ.</p>
</header>

<section>
  <h2>ಸರ್ಕಾರದ ಸ್ವಂತ ಲೆಕ್ಕ</h2>
  <ol class="ladder">
    <li><b>1,248</b><span>ಅಧಿಕಾರಿಗಳ ವಿರುದ್ಧ ಲೋಕಾಯುಕ್ತ ಪ್ರಕರಣಗಳು, 10 ಸೆಪ್ಟೆಂಬರ್ 2022ರಿಂದ 13 ಆಗಸ್ಟ್ 2026ರವರೆಗೆ</span></li>
    <li><b>364</b><span>ದೋಷಾರೋಪಣ ಪಟ್ಟಿ ಸಲ್ಲಿಕೆ</span></li>
    <li><b>648</b><span>ಇನ್ನೂ ತನಿಖೆಯಲ್ಲಿವೆ</span></li>
    <li><b>218</b><span>ನ್ಯಾಯಾಲಯಗಳ ತಡೆಯಾಜ್ಞೆ</span></li>
    <li class="zero"><b>0</b><span>ಇದುವರೆಗೆ ತಪ್ಪಿತಸ್ಥರೆಂದು ತೀರ್ಮಾನವಾದ ಸರ್ಕಾರಿ ನೌಕರರು</span></li>
  </ol>
  <p class="muted">ವಿಧಾನ ಪರಿಷತ್ತಿನ ಚುಕ್ಕೆ ಗುರುತಿಲ್ಲದ ಪ್ರಶ್ನೆ 452 (628)ಕ್ಕೆ ಮುಖ್ಯಮಂತ್ರಿಗಳು 20 ಆಗಸ್ಟ್ 2026ರಂದು ನೀಡಿದ ಲಿಖಿತ ಉತ್ತರದಿಂದ (ಮೂಲ ದಾಖಲೆಯನ್ನೇ ಓದಲಾಗಿದೆ): 939 ಲಂಚದ ಟ್ರ್ಯಾಪ್ ಪ್ರಕರಣಗಳು ಮತ್ತು 309 ಆದಾಯ ಮೀರಿದ ಆಸ್ತಿ ಪ್ರಕರಣಗಳು, ಒಟ್ಟು 1,451 ಅಧಿಕಾರಿಗಳು ಮತ್ತು ನೌಕರರು; ಇನ್ನೂ 18 ಪ್ರಕರಣಗಳನ್ನು ಮುಕ್ತಾಯಗೊಳಿಸಲಾಗಿದೆ. <a href="https://kla.kar.nic.in/council/Replies/unstarred/20082026/usq628(20082026).pdf">ಉತ್ತರ (PDF, ಕನ್ನಡ)</a>. ಈ ಉತ್ತರದ ಬಗ್ಗೆ ಪತ್ರಿಕಾ ವರದಿಗಳು 939 ಟ್ರ್ಯಾಪ್ ಪ್ರಕರಣಗಳನ್ನು ಆಸ್ತಿ ಪ್ರಕರಣಗಳೆಂದು ತಪ್ಪಾಗಿ ಹೆಸರಿಸಿದ್ದವು.</p>
</section>

<section>
  <h2>2026ರ ಪ್ರಕರಣಗಳು ಎಲ್ಲಿಯವರೆಗೆ ತಲುಪಿವೆ</h2>
  <ol class="ladder">{ladder_html}</ol>
  <p class="muted">ಓದಿದ ವರದಿಗಳು ತೋರಿಸುವ ಮಟ್ಟಿಗೆ, ಆ ಹಂತವನ್ನು ಅಥವಾ ಅದರ ನಂತರದ ಹಂತವನ್ನು ತಲುಪಿದ ಪ್ರಕರಣಗಳ ಅಧಿಕಾರಿಗಳನ್ನು ಪ್ರತಿ ಸಂಖ್ಯೆ ಎಣಿಸುತ್ತದೆ. ಸೊನ್ನೆ ಎಂದರೆ ಆ ಹಂತದ ಯಾವುದೇ ವರದಿ ಸಿಕ್ಕಿಲ್ಲ ಎಂದರ್ಥ. ಆ ಹಂತ ನಡೆದೇ ಇಲ್ಲ ಎಂದಲ್ಲ: {d_kn(checked)}ರ ಅನುಸರಣಾ ಪರಿಶೀಲನೆ ಇಂಗ್ಲಿಷ್ ಮತ್ತು ಕನ್ನಡದಲ್ಲಿ ಹೆಸರಿನ ಮೂಲಕ ಮಾಡಿದ ವೆಬ್ ಹುಡುಕಾಟವಾಗಿತ್ತು. ಅದು ಪ್ರಜಾವಾಣಿ, ಡೆಕ್ಕನ್ ಹೆರಾಲ್ಡ್ ಅಥವಾ ಲೋಕಾಯುಕ್ತದ ಸ್ವಂತ ಜಾಲತಾಣವನ್ನು ತಲುಪಲಾಗಲಿಲ್ಲ, ಮತ್ತು ನ್ಯಾಯಾಲಯದ ಪ್ರಕರಣ-ಸ್ಥಿತಿ ಜಾಲತಾಣಗಳನ್ನು ಒಳಗೊಂಡಿರಲಿಲ್ಲ.{unchecked_note_kn} {len(moved)} ಸಾಲುಗಳಲ್ಲಿ ಬೇರೆ ಬಗೆಯ ನಂತರದ ಬೆಳವಣಿಗೆ ಇದೆ (ನ್ಯಾಯಾಲಯದ ಆದೇಶ, ಮತ್ತಷ್ಟು ಶೋಧ, ಹೊಸ ಹುದ್ದೆಗೆ ನಿಯೋಜನೆ, ಪ್ರತ್ಯೇಕ ಪ್ರಕರಣ); ಪ್ರತಿಯೊಂದನ್ನೂ ಅದರ ಮೂಲದೊಂದಿಗೆ ಕೋಷ್ಟಕದಲ್ಲಿ ತೋರಿಸಲಾಗಿದೆ.</p>
</section>

<section>
  <h2>ಇಂತಹ ಪ್ರಕರಣಗಳು ಸಾಮಾನ್ಯವಾಗಿ ಹೇಗೆ ಮುಗಿಯುತ್ತವೆ</h2>
  <p class="muted">ಎಲ್ಲ ತನಿಖಾ ಸಂಸ್ಥೆಗಳ ಭ್ರಷ್ಟಾಚಾರ ಪ್ರಕರಣಗಳ ಬಗ್ಗೆ ರಾಜ್ಯವೇ ರಾಷ್ಟ್ರೀಯ ಅಪರಾಧ ದಾಖಲೆಗಳ ಬ್ಯೂರೋಗೆ (ಎನ್‌ಸಿಆರ್‌ಬಿ) 2023ಕ್ಕೆ ನೀಡಿದ ಅಂಕಿಗಳು (ಪ್ರಕಟವಾಗಿರುವ ಇತ್ತೀಚಿನ ವರ್ಷ). ಮೇಲಿನ ಪ್ರಕರಣಗಳ ಮುಂದಿರುವ ದಾರಿ ಇದು.</p>
  <ol class="ladder">
    <li><b>362</b><span>2023ರಲ್ಲಿ ಕರ್ನಾಟಕದಲ್ಲಿ ದಾಖಲಾದ ಹೊಸ ಭ್ರಷ್ಟಾಚಾರ ಪ್ರಕರಣಗಳು (245 ಲಂಚದ ಟ್ರ್ಯಾಪ್, 84 ಆಸ್ತಿ ಪ್ರಕರಣಗಳು)</span></li>
    <li><b>195</b><span>2023ರಲ್ಲಿ ದೋಷಾರೋಪಣ ಪಟ್ಟಿ ಸಲ್ಲಿಸಿದ ಪ್ರಕರಣಗಳು; ವರ್ಷಾಂತ್ಯದಲ್ಲಿ 1,448 ಇನ್ನೂ ತನಿಖೆಯಲ್ಲಿದ್ದವು</span></li>
    <li><b>120</b><span>2023ರಲ್ಲಿ ಮುಗಿದ ವಿಚಾರಣೆಗಳು, ವಿಚಾರಣೆಗೆ ಕಾಯುತ್ತಿದ್ದ 1,690 ಪ್ರಕರಣಗಳಲ್ಲಿ</span></li>
    <li class="zero"><b>35</b><span>ಶಿಕ್ಷೆಯಲ್ಲಿ ಕೊನೆಗೊಂಡವು: 29.2%, ಭಾರತದಲ್ಲಿ 46.2%. 74 ಖುಲಾಸೆಯಲ್ಲಿ ಕೊನೆಗೊಂಡವು</span></li>
  </ol>
  <p class="muted">2023ರ ಅಂತ್ಯದಲ್ಲಿ ಕರ್ನಾಟಕದ 1,529 ಭ್ರಷ್ಟಾಚಾರ ಪ್ರಕರಣಗಳು ವಿಚಾರಣೆಗೆ ಬಾಕಿ ಇದ್ದವು, ಆ ವರ್ಷ ವಿಚಾರಣೆಗೆ ಬರಬೇಕಿದ್ದ ಎಲ್ಲ ಪ್ರಕರಣಗಳ 90.5%. 2023ರ ವೇಗದಲ್ಲಿ, ಅಂದರೆ ವರ್ಷಕ್ಕೆ 120 ವಿಚಾರಣೆಗಳು, ಇದು ಸುಮಾರು 13 ವರ್ಷಗಳ ಕೆಲಸ (ನಮ್ಮ ಲೆಕ್ಕ). ಅದೇ ವರ್ಷ ನ್ಯಾಯಾಲಯಗಳು 28 ಪ್ರಕರಣಗಳನ್ನು ರದ್ದುಪಡಿಸಿದವು ಮತ್ತು 70ಕ್ಕೆ ತಡೆ ನೀಡಿದವು. ಆರೋಪಿಗಳಲ್ಲಿ 43 ಮಂದಿಗೆ ಶಿಕ್ಷೆಯಾಯಿತು, 4 ಮಂದಿಯನ್ನು ಸೇವೆಯಿಂದ ವಜಾ ಮಾಡಲಾಯಿತು. ಮೂಲ: <a href="https://www.ncrb.mha.gov.in/uploads/files/2CrimeinIndia2023PartII.pdf">ಎನ್‌ಸಿಆರ್‌ಬಿ, ಕ್ರೈಮ್ ಇನ್ ಇಂಡಿಯಾ 2023, ಸಂಪುಟ 2, ಕೋಷ್ಟಕ 8C.2-8C.5 (ಪುಟ 779-784)</a>; ಕರ್ನಾಟಕದ ಸಾಲುಗಳನ್ನು 18 ನವೆಂಬರ್ 2026ರಂದು ಪುಟದ ಚಿತ್ರಗಳೊಂದಿಗೆ ಹೋಲಿಸಲಾಗಿದೆ. ಇವು ರಾಜ್ಯದ ಎಲ್ಲ ಭ್ರಷ್ಟಾಚಾರ ಪ್ರಕರಣಗಳು, ಈ ಪುಟದ ಅಧಿಕಾರಿಗಳದ್ದು ಮಾತ್ರವಲ್ಲ.</p>
</section>

<section>
  <h2>ಹಣ ಎಲ್ಲಿ ಸಿಕ್ಕಿತು</h2>
  <p class="muted">{n} ಅಧಿಕಾರಿಗಳಲ್ಲಿ {na} ಮಂದಿಯ ವಿಷಯದಲ್ಲಿ, ತನಿಖಾ ಸಂಸ್ಥೆ ಯಾವ ಬಗೆಯ ಆಸ್ತಿಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಿತು ಎಂಬ ಪಟ್ಟಿ ವರದಿಯೊಂದರಲ್ಲಿತ್ತು. ಆ ಪಟ್ಟಿಗಳಲ್ಲಿ ಇರುವುದು ಇದು. ಸಂಪತ್ತನ್ನು ಎಲ್ಲಿ ಇಡಲಾಗಿದೆ ಎಂಬುದನ್ನು ಇದು ತೋರಿಸುತ್ತದೆ, ಅದರಲ್ಲಿ ಯಾವುದೂ ಅಕ್ರಮ ಎಂದಲ್ಲ: ಪ್ರತಿ ಅಂಕಿಯೂ ಮೊದಲ ದಿನದ ಹೇಳಿಕೆ, ಪ್ರಕರಣದಲ್ಲಿ ಅದನ್ನು ಇನ್ನೂ ಸಾಬೀತುಪಡಿಸಬೇಕಿದೆ.</p>
  <div class="tbl"><table>
    <thead><tr><th>ಆಸ್ತಿಯ ಬಗೆ</th><th class="n">ಅಧಿಕಾರಿಗಳು</th><th>ವರದಿಯಾದ ಪ್ರಮಾಣ</th></tr></thead>
    <tbody>{money_html}</tbody>
  </table></div>
  <p class="muted">ಎಣಿಕೆಗಳು ಕನಿಷ್ಠ ಮಟ್ಟದವು: ಅನೇಕ ವರದಿಗಳು ಸಂಖ್ಯೆ ಅಥವಾ ಮೌಲ್ಯವಿಲ್ಲದೆ ಆಸ್ತಿಯನ್ನು ಉಲ್ಲೇಖಿಸುತ್ತವೆ. ಪ್ರತಿ ಅಧಿಕಾರಿಯ ವಿವರ ಮತ್ತು ಮೂಲಗಳು ಈ ಪುಟದ ಜೊತೆಗಿರುವ assets.csv ಕಡತದಲ್ಲಿವೆ (ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ).</p>
</section>

<section>
  <h2>ಯಾವ ಹುದ್ದೆಗಳು ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತವೆ</h2>
  {bars_html}
  <p class="muted">ಅಂಕಿ ವರದಿಯಾದ {len(valued)} ಅಧಿಕಾರಿಗಳ ಮೊದಲ ಅಂದಾಜುಗಳ ಒಟ್ಟು ₹{total:.2f} ಕೋಟಿ (ನೀಡಿರುವಲ್ಲಿ ಒಟ್ಟು ಆಸ್ತಿ, ಇಲ್ಲದಿದ್ದರೆ ಆದಾಯ ಮೀರಿದ ಆಸ್ತಿಯ ಅಂಕಿ, ಅದನ್ನು DA ಎಂದು ಗುರುತಿಸಲಾಗಿದೆ); ಉಳಿದ {n - len(valued)} ಮಂದಿಯ ವರದಿಯಲ್ಲಿ ಯಾವುದೇ ಅಂಕಿ ಇರಲಿಲ್ಲ.</p>
</section>

<section>
  <h2>ಪ್ರತಿಯೊಬ್ಬ ಅಧಿಕಾರಿ, ದಿನಾಂಕವಾರು</h2>
  <div class="tbl"><table>
    <thead><tr><th>ದಿನಾಂಕ</th><th>ಹುದ್ದೆ</th><th>ಕ್ರಮ</th><th class="n">ಹೇಳಲಾದ ಆಸ್ತಿ (₹ ಕೋಟಿ)</th><th>ವರದಿಯಾದ ಕೊನೆಯ ಹಂತ</th><th>ಮೂಲ</th></tr></thead>
    <tbody>{body_html}</tbody>
  </table></div>
</section>

<section>
  <h2>ಇಲ್ಲಿ ಏನು ಇಲ್ಲ</h2>
  <ul>
    <li>ಇದು 2026ರ ಎಲ್ಲ ಪ್ರಕರಣಗಳಲ್ಲ. ಮೇ 2026ರಲ್ಲಿ ಯಾವುದೇ ಆಸ್ತಿ ದಾಳಿ ಕಂಡುಬಂದಿಲ್ಲ. 5 ಫೆಬ್ರವರಿ 2026ರಂದು ವರದಿಯಾದ ಮೈಸೂರಿನ ದಾಳಿ ಕೇವಲ ಒಂದು ಸುಳಿವು. ಲಂಚದ ಟ್ರ್ಯಾಪ್ ಪ್ರಕರಣಗಳನ್ನು ವ್ಯವಸ್ಥಿತವಾಗಿ ದಾಖಲಿಸುತ್ತಿಲ್ಲ: 2026ರಲ್ಲಿ ಅವು ಇಲ್ಲಿ ತೋರಿಸಿರುವ ಕೆಲವಕ್ಕಿಂತ ಎಷ್ಟೋ ಹೆಚ್ಚು ಇದ್ದವು.</li>
    <li>ಅನುಸರಣಾ ಪರಿಶೀಲನೆ ಪತ್ರಿಕಾ ವರದಿಗಳ ಹುಡುಕಾಟವಾಗಿತ್ತು. ದೋಷಾರೋಪಣ ಪಟ್ಟಿಗಳು, ಮಂಜೂರಾತಿ ಕೋರಿಕೆಗಳು, ನ್ಯಾಯಾಲಯದ ತಡೆಯಾಜ್ಞೆಗಳು ಮತ್ತು ತೀರ್ಪುಗಳು ವಿರಳವಾಗಿ ವರದಿಯಾಗುತ್ತವೆ; ಅವು ಲೋಕಾಯುಕ್ತದ ಉತ್ತರಗಳು, ಮಾಹಿತಿ ಹಕ್ಕು ಉತ್ತರಗಳು ಮತ್ತು ನ್ಯಾಯಾಲಯದ ದಾಖಲೆಗಳಿಂದಲೇ ಬರಬೇಕು. ಅಬಕಾರಿ ಪ್ರಕರಣದಲ್ಲಿ 22 ಜುಲೈ 2026ರಂದು ನಡೆದ ಉಚ್ಚ ನ್ಯಾಯಾಲಯದ ವಿಚಾರಣೆಯ ಫಲಿತಾಂಶ ಸಿಗಲಿಲ್ಲ.</li>
    <li>UNVERIFIED (ದೃಢಪಡಿಸಿಲ್ಲ) ಎಂದು ಗುರುತಿಸಿದ ಅನುಸರಣಾ ನಮೂದುಗಳು ಒಂದೇ ಮಾಧ್ಯಮವನ್ನು ಆಧರಿಸಿವೆ. ಪ್ರತ್ಯೇಕ ಪ್ರಕರಣದಲ್ಲಿನ ಬಂಧನವನ್ನು ಹೆಸರು ಮತ್ತು ಹಿಂದಿನ ಹುದ್ದೆಯ ಆಧಾರದ ಮೇಲೆ ಹೊಂದಿಸಲಾಗಿದೆ.</li>
    <li>ಹಲವು ಆಸ್ತಿ ಅಂಕಿಗಳು ಒಂದು ಸಣ್ಣ ಮಾಧ್ಯಮದಿಂದ ಬಂದಿವೆ, ಮತ್ತು ಒಂದೇ ದಾಳಿಯ ವರದಿಗಳು ಹುದ್ದೆ, ಇಲಾಖೆ ಅಥವಾ ಮೊತ್ತದ ಬಗ್ಗೆ ಆಗಾಗ ಭಿನ್ನವಾಗಿರುತ್ತವೆ; ಎಲ್ಲಿ ಎಂಬುದನ್ನು ಟಿಪ್ಪಣಿಗಳು ಹೇಳುತ್ತವೆ.</li>
  </ul>
</section>

<footer>
  <p class="muted">ಮೂಲಗಳು</p>
  <ul class="src">{src_html}</ul>
</footer>
</div>
</html>
"""
out_kn = HERE / "DRAFT_officials_tracker_kn.html"
out_kn.write_text(page_kn, encoding="utf-8")
print(f"{out.name} and {out_kn.name}: {n} officials, {days} days, ladder {reached}, Rs {total:.2f} crore over {len(valued)} valued rows")
print(groups)
