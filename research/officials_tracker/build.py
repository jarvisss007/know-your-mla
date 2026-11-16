"""Build DRAFT_officials_tracker.html from tracker.csv.

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

LADDER = ["Action taken", "Suspended", "Chargesheet filed", "Sanction to prosecute", "Trial under way", "Verdict"]
STAGE_RANK = {"Raided": 0, "Searched": 0, "Arrested": 0, "Suspended": 1, "Chargesheet filed": 2,
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
reached = [sum(1 for r in rows if STAGE_RANK[r["stage"]] >= i) for i in range(len(LADDER))]
groups = Counter(group(r) for r in rows).most_common()
gmax = groups[0][1]
first, last = rows[0]["action_date"], rows[-1]["action_date"]
checked = max(r["checked_on"] for r in rows)
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


ladder_html = "".join(
    f'<li class="{"zero" if c == 0 else ""}"><b>{c}</b><span>{e(name)}</span></li>'
    for name, c in zip(LADDER, reached))

bars_html = "".join(
    f'<div class="brow"><span>{e(g)}</span><div class="bar"><i style="width:{c / gmax * 100:.0f}%"></i></div><b>{c}</b></div>'
    for g, c in groups)

body = []
for r in rows:
    a, tag = claimed(r)
    fu = e(r["followup"])
    if r["followup_url"]:
        fu = f'{fu} <a href="{e(r["followup_url"])}">source</a> · {d(r["followup_date"])}'
    host = urlparse(r["source_url"]).netloc.replace("www.", "")
    note = f'<div class="nt">{e(r["notes"])}</div>' if r["notes"] else ""
    body.append(
        f'<tr><td class="dt">{d(r["action_date"])}</td>'
        f'<td><strong>{e(r["post"])}</strong><div class="sub">{e(r["department"])} · {e(r["district"])}</div>{note}<div class="fu"><b>Since then:</b> {fu}</div></td>'
        f'<td>{e(r["action"])}<div class="sub">{e(r["agency"])}</div></td>'
        f'<td class="n">{f"{a:.2f}{tag}" if a is not None else "not stated"}</td>'
        f'<td><span class="st s{STAGE_RANK[r["stage"]]}">{e(r["stage"])}</span><div class="sub">{d(r["stage_date"])}</div></td>'
        f'<td><a href="{e(r["source_url"])}">{e(host)}</a><div class="sub">{d(r["source_published"])}</div></td></tr>')

src_html = "".join(f'<li><a href="{e(u)}">{e(u)}</a></li>' for u in sources)

page = f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>After the Raid</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap">
<style>
/* One reading column. The ladder is the page: how far each case has got since the raid. */
:root {{
  --bg: #f5f6f8; --surface: #ffffff; --fg: #161a22; --muted: #5b6474; --line: #dde1e8;
  --red: #c21f30; --yellow: #f2b705; --track: #e3e6ec; --ok: #1a8f4c; --warn: #b45309;
  --display: "Space Grotesk", "Segoe UI", system-ui, sans-serif;
  --body: Inter, "Segoe UI", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d;
  --red: #ef5261; --yellow: #f5c93a; --track: #2b313d; --ok: #4fcf86; --warn: #f0a04b; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d;
  --red: #ef5261; --yellow: #f5c93a; --track: #2b313d; --ok: #4fcf86; --warn: #f0a04b; color-scheme: dark }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--fg); font: 16px/1.55 var(--body); padding: 28px 16px 64px; }}
.wrap {{ max-width: 920px; margin: 0 auto; display: flex; flex-direction: column; gap: 40px; }}
a {{ color: inherit; text-underline-offset: 3px; }}
a:focus-visible {{ outline: 2px solid var(--red); outline-offset: 2px; }}
h1, h2 {{ font-family: var(--display); text-wrap: balance; margin: 0; }}
h1 {{ font-size: clamp(2.2rem, 7vw, 3.6rem); line-height: 1; letter-spacing: -0.02em; }}
h1 span {{ color: var(--red); }}
h2 {{ font-size: 1.5rem; }}
p {{ margin: 0; max-width: 66ch; }}
.eyebrow {{ font-size: .75rem; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); font-weight: 600; }}
.draft {{ display: inline-block; background: var(--yellow); color: #161a22; font-weight: 600; font-size: .8rem; padding: 3px 10px; border-radius: 3px; letter-spacing: .04em; }}
header, section {{ display: flex; flex-direction: column; gap: 14px; }}
.lede {{ font-size: 1.1rem; }}
.muted {{ color: var(--muted); font-size: .9rem; }}
.ladder {{ list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); border-block: 2px solid var(--fg); }}
.ladder li {{ padding: 16px 12px 16px 0; display: flex; flex-direction: column; gap: 4px; min-width: 0; }}
.ladder b {{ font: 700 2.6rem/1 var(--display); font-variant-numeric: tabular-nums; }}
.ladder li.zero b {{ color: var(--red); }}
.ladder span {{ font-size: .88rem; }}
.brow {{ display: grid; grid-template-columns: minmax(0, 190px) minmax(0, 1fr) 2.5ch; gap: 12px; align-items: center; font-size: .92rem; }}
.brow b {{ font-variant-numeric: tabular-nums; text-align: right; }}
.bar {{ height: 12px; background: var(--track); border-radius: 2px; overflow: hidden; }}
.bar i {{ display: block; height: 100%; background: var(--red); }}
.tbl {{ overflow-x: auto; }}
table {{ border-collapse: collapse; width: 100%; font-size: .9rem; min-width: 760px; }}
th, td {{ text-align: left; padding: 10px 14px 10px 0; border-top: 1px solid var(--line); vertical-align: top; }}
th {{ font-size: .75rem; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); border-top: 2px solid var(--fg); }}
td.n, th.n {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
td.dt {{ white-space: nowrap; font-variant-numeric: tabular-nums; }}
.fu {{ font-size: .82rem; margin-top: 6px; }}
.nt {{ overflow-wrap: anywhere; }}
.sub, .nt {{ color: var(--muted); font-size: .8rem; }}
.st {{ font-weight: 600; white-space: nowrap; }}
.st.s1 {{ color: var(--warn); }}
.st.s2, .st.s3, .st.s4, .st.s5 {{ color: var(--ok); }}
ul {{ margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 8px; max-width: 74ch; }}
.src {{ font-size: .82rem; word-break: break-all; }}
footer {{ border-top: 2px solid var(--fg); padding-top: 14px; }}
</style>

<div class="wrap">
<header>
  <div><span class="draft">DRAFT · NOT PUBLISHED</span></div>
  <div class="eyebrow">Gandaberunda · Karnataka officials · reports read up to {d(checked)}</div>
  <h1>After the <span>raid</span></h1>
  <p class="lede">{n} Karnataka officials were raided, trapped, searched or suspended on {days} days between {d(first)} and {d(last)}, in the reports read so far. This page follows each one from that first day towards a verdict.</p>
  <p class="muted">A raid or an arrest is an allegation, not a finding of guilt. Asset figures are the agency's first-day estimates. The page gives the post, not the person: names are in the linked reports and are added here only after the FIR and the person's reply are checked.</p>
</header>

<section>
  <h2>How far the cases have got</h2>
  <ol class="ladder">{ladder_html}</ol>
  <p class="muted">Each number counts officials whose case reached that step or a later one, as far as the reports read show. A zero means no report of that step was found. It does not mean the step has not happened: the follow-up check on {d(checked)} was a web search by name, mostly in English, and did not cover court case-status sites or Lokayukta records. {unchecked} officials added from a later report have not been checked yet. {len(moved)} rows carry a later development of another kind (a court order, further searches, a posting, a separate case); each is shown in the table with its source.</p>
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
    <tbody>{''.join(body)}</tbody>
  </table></div>
</section>

<section>
  <h2>What is missing</h2>
  <ul>
    <li>This is not every case of 2026. No raid report for May, October or November 2026 has been found. A Deccan Herald report dated 20 Aug 2026 on a single Bengaluru official would not open and is not in the table.</li>
    <li>The follow-up check was a press search. Chargesheets, sanction requests, court stays and verdicts are rarely reported and must come from Lokayukta replies, RTI answers and court records. The outcome of the High Court hearing of 22 Jul 2026 in the excise matter was not found.</li>
    <li>Two follow-up entries are weak and marked as such: a posting reported by one outlet with the order unseen, and an arrest in a separate case matched by name and former post.</li>
    <li>Several rows rest on a single news report. Where the district or department is "not stated", the report did not give it.</li>
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
print(f"{out.name}: {n} officials, {days} days, ladder {reached}, Rs {total:.2f} crore over {len(valued)} valued rows")
print(groups)
