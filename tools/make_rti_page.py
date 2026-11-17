"""Build rti.html: ready-to-file RTI letters about what happened after the 2026 raids.

    py tools/make_rti_page.py

Reads research/officials_tracker/tracker.csv. The page carries posts, places and dates only, never names
(the same rule as the tracker). Re-run after the tracker changes.
"""
import csv
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
rows = list(csv.DictReader(open(ROOT / "research/officials_tracker/tracker.csv", encoding="utf-8")))
lok = [r for r in rows if r["agency"].startswith("Lokayukta")]
stuck = sum(1 for r in rows if r["stage"] in ("Raided", "Searched"))

FORM = ("https://docs.google.com/forms/d/e/1FAIpQLSdGCs8oRCLplhyq3VxHH_olo9GzMJk9I7kv5q54yxgUFp2C3A/viewform"
        "?usp=pp_url&entry.503187352=Something+else&entry.878251699=RTI+reply:+")


def short_dept(d):
    return d.split(" per the ")[0].split(" (earlier")[0]


def d(s):
    import datetime as dt
    return dt.date.fromisoformat(s).strftime("%-d %b %Y") if False else dt.date.fromisoformat(s).strftime("%d %b %Y").lstrip("0")


DATA = [{"dept": short_dept(r["department"]), "post": r["post"], "place": r["district"],
         "date": d(r["action_date"]), "action": r["action"], "src": r["source_url"]} for r in lok]
DEPTS = sorted({x["dept"] for x in DATA}, key=lambda k: (-sum(1 for x in DATA if x["dept"] == k), k))

HEAD = """To
The Public Information Officer
{to}

Subject: Application under Section 6(1) of the Right to Information Act, 2005

1. Name of applicant: {name}
2. Address for correspondence: {addr}
3. Fee: Rs 10 paid by Indian Postal Order / Demand Draft No. ______ dated ______
"""
FOOT = """
If any item is considered exempt, please give the remaining items, state the reasons under Section 7(8)(i), and consider partial disclosure under Section 10. If any item is held by another public authority, please transfer it under Section 6(3) and inform me.

I am a citizen of India.

Place: ______        Date: ______
Signature: ______
"""

LETTERS = [
    {"id": "l1", "title": "1. Lokayukta police: what happened to the 2026 cases",
     "to": "Office of the Additional Director General of Police, Karnataka Lokayukta\nM.S. Building, Dr B.R. Ambedkar Veedhi, Bengaluru 560 001",
     "why": "The Lokayukta police know whether each case has a chargesheet, a pending sanction request or a court stay. Part A asks only for totals, which should be answered even if Part B is refused.",
     "annex": "all",
     "body": """Period: 1 January 2026 to the date of this application.

Information sought

Part A (totals; no names are needed)
For cases registered by the Lokayukta police from 1 January 2026 to the date of this application under the Prevention of Corruption Act, 1988, please give, department by department:
a. the number of cases registered, separately for trap (bribery) cases and disproportionate-assets cases;
b. the number in which a final report (chargesheet) has been filed in court;
c. the number in which a request for sanction to prosecute (Section 19 of the PC Act) has been sent, and the number in which the competent authority has not decided it within the period allowed by the proviso to Section 19(1);
d. the number in which approval under Section 17A of the PC Act was sought and is pending;
e. the number stayed or quashed by a court, and the number closed by a B-report or other closure report.

Part B (status of the cases in the annex)
The annex lists officers reported in the press as searched or trapped by the Lokayukta police in 2026, by post, place and date of action. For each, please give:
a. the Lokayukta police station and crime number;
b. whether a chargesheet has been filed, and the date;
c. whether sanction to prosecute has been requested, the date, and the authority it was sent to;
d. whether that authority has granted or refused sanction, and the date;
e. whether any court has stayed or quashed the proceedings, with the date and court;
f. whether a closure (B) report has been filed, and the date.

Only dates and stages are sought. No part of the case diary, statements or evidence is requested.
"""},
    {"id": "l2", "title": "2. Government: sanction requests left pending",
     "to": "Department of Personnel and Administrative Reforms (Services)\nVidhana Soudha, Bengaluru 560 001",
     "why": "A case cannot go to trial until the officer's department gives sanction to prosecute. In 2024 the Lokayukta said 206 officials' sanctions had been pending for months. This asks for today's list, by department and designation, and the rules on time limits.",
     "annex": None,
     "body": """Information sought

1. A statement, as on the date of reply, of requests from the Karnataka Lokayukta (police wing, or Lokayukta / Upalokayukta) for sanction to prosecute government servants, or for approval under Section 17A of the Prevention of Corruption Act, 1988, pending with any department of the Government of Karnataka, showing for each: the department; the designation of the government servant; the date the request was received; and how long it has been pending.
2. For 1 January 2024 to the date of reply, the number of such requests decided by each department, separately for sanction granted and refused, and the number decided more than four months after receipt.
3. Copies of the circulars or government orders now in force that fix (a) the time limit for deciding a request for sanction to prosecute, and (b) who monitors pending requests.
4. Copies of the proceedings of any review meeting held in 2025 or 2026 on pending Lokayukta sanction requests.
5. If such a statement was furnished to the Legislative Assembly, the Legislative Council or the High Court in 2025 or 2026, a copy.
"""},
    {"id": "l3", "title": "3. One department: suspension, sanction, promotion",
     "to": "[Name of the department or company, and its head-office address]",
     "why": "Each department decides whether its officer is suspended, whether to allow prosecution, and whether to transfer or promote them. Suspension and posting orders are routine office orders. Pick a department below; its officers are added as the annex.",
     "annex": "dept",
     "body": """Information sought

The officers described in the annex (post, place and date of action), serving or retired from this department or company, were reported in the press as searched or trapped by the Karnataka Lokayukta police on the dates shown. For each of them, please give:
1. Whether the officer was placed under suspension (including deemed suspension on detention for more than 48 hours under the Karnataka Civil Services (Classification, Control and Appeal) Rules, 1957, or the equivalent rules of this body), with the date and a copy of the order; and whether the suspension has been revoked, with the date and a copy of that order.
2. Whether a request for sanction to prosecute, or for approval under Section 17A of the Prevention of Corruption Act, 1988, has been received from the Lokayukta; the date received; the date of decision; and the decision (granted / refused / pending).
3. Whether a departmental inquiry or disciplinary proceeding has been initiated after the Lokayukta action, with the date of the charge memo.
4. Any transfer, posting, promotion or additional charge given to the officer after the date of the Lokayukta action, with the date and a copy of the order.
5. The officer's present designation and place of posting, or the date of retirement.

Items 1, 4 and 5 are office orders issued in the ordinary course of business.
"""},
    {"id": "l4", "title": "4. Officers who never declared their property",
     "to": "Department of Personnel and Administrative Reforms (Services)\nVidhana Soudha, Bengaluru 560 001",
     "why": "Every government servant must file an annual statement of property. A missing return is often the first sign investigators look for. The government has given such lists to the Assembly before.",
     "annex": None,
     "body": """Information sought

Under the Karnataka Civil Services (Conduct) Rules, 2021 (declaration of assets and liabilities) and the All India Services (Conduct) Rules for IAS officers of the Karnataka cadre:
1. For the returns due in 2023-24, 2024-25 and 2025-26, the number of officers required to file annual property returns and the number who did not file by the due date, department by department, separately for IAS, KAS and other Group A and Group B officers.
2. The list of IAS and KAS officers who had not filed for 2024-25 and 2025-26 as on the date of reply.
3. The action taken against officers who did not file (notices, increments withheld, vigilance clearance refused, disciplinary proceedings), with numbers for each year.
4. Copies of any circular issued in 2024, 2025 or 2026 on filing property returns, including any instruction to publish them online.
"""},
]

css = """
:root { --bg:#f5f6f8; --surface:#fff; --fg:#161a22; --muted:#5b6474; --line:#dde1e8; --red:#c21f30; --yellow:#f2b705; --chip:#eef0f4; --focus:#1d4ed8;
  --display:"Space Grotesk","Segoe UI",system-ui,sans-serif; --body:Inter,"Segoe UI",system-ui,sans-serif; color-scheme:light }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#11141a; --surface:#1a1e27; --fg:#eceef2; --muted:#9aa3b2; --line:#2b313d; --red:#ef5261; --yellow:#f5c93a; --chip:#232835; --focus:#7aa7ff; color-scheme:dark } }
:root[data-theme="dark"] { --bg:#11141a; --surface:#1a1e27; --fg:#eceef2; --muted:#9aa3b2; --line:#2b313d; --red:#ef5261; --yellow:#f5c93a; --chip:#232835; --focus:#7aa7ff; color-scheme:dark }
* { box-sizing:border-box } html { -webkit-text-size-adjust:100% }
body { margin:0; background:var(--bg); color:var(--fg); font:15px/1.55 var(--body) }
a { color:inherit; text-decoration-color:var(--red); text-underline-offset:2px }
:focus-visible { outline:2px solid var(--focus); outline-offset:2px }
.bar { position:sticky; top:0; z-index:5; background:#11141a; color:#eceef2; padding:10px 16px; border-bottom:3px solid #f2b705; font:600 14px/1.4 var(--body) }
.bar a { color:#f5c93a; text-decoration:none }
main { max-width:780px; margin:0 auto; padding:24px 16px 64px }
.kick { font:600 12px/1.3 var(--body); letter-spacing:.08em; text-transform:uppercase; color:var(--muted) }
h1 { font:700 clamp(30px,6vw,42px)/1.05 var(--display); margin:6px 0 12px; text-wrap:balance }
h1 em { font-style:normal; color:var(--red) }
h2 { font:700 22px/1.2 var(--display); margin:36px 0 10px }
.lede { font-size:17px; max-width:62ch }
.note { color:var(--muted); font-size:14px }
ol.steps { padding-left:22px } ol.steps li { margin:0 0 10px }
.card { background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:16px; margin:16px 0 }
.card h3 { font:700 18px/1.25 var(--display); margin:0 0 6px }
.you { display:grid; gap:10px; grid-template-columns:1fr } @media (min-width:600px) { .you { grid-template-columns:1fr 2fr } }
label { font-weight:600; font-size:13px; display:block; margin-bottom:4px }
input, select, textarea { width:100%; font:15px/1.4 var(--body); color:var(--fg); background:var(--bg); border:1px solid var(--line); border-radius:8px; padding:9px 10px }
textarea.letter { font:13px/1.5 ui-monospace,Consolas,monospace; min-height:320px; resize:vertical; white-space:pre-wrap }
.row { display:flex; flex-wrap:wrap; gap:8px; margin-top:10px }
button { font:600 14px/1 var(--body); padding:10px 14px; border-radius:8px; border:1px solid var(--line); background:var(--chip); color:var(--fg); cursor:pointer }
button.primary { background:var(--red); border-color:var(--red); color:#fff }
.ok { color:var(--muted); font-size:13px; align-self:center }
.warn { border-left:4px solid var(--yellow) }
ul.plain { padding-left:18px } ul.plain li { margin-bottom:6px }
@media print { .bar, .row, .you, select { display:none } body { background:#fff; color:#000 } }
"""

js = """
const DATA = __DATA__;
const L = __LETTERS__;
const $ = id => document.getElementById(id);
function annex(rows) {
  if (!rows.length) return '';
  return '\\nAnnex: officers reported in the press as searched or trapped by the Karnataka Lokayukta police (post, department, place, date of action, press report)\\n' +
    rows.map((r, i) => `${i + 1}. ${r.post}, ${r.dept}, ${r.place}; ${r.action}, ${r.date}; ${r.src}`).join('\\n') + '\\n';
}
function build(l) {
  const name = $('nm').value.trim() || '______', addr = $('ad').value.trim().replace(/\\n+/g, ', ') || '______';
  let to = l.to, rows = [];
  if (l.annex === 'all') rows = DATA;
  if (l.annex === 'dept') { const dp = $('dept').value; rows = DATA.filter(r => r.dept === dp); to = '[' + dp + ': head office, or the company\\'s PIO]'; }
  return L.head.replace('{to}', to).replace('{name}', name).replace('{addr}', addr) + '\\n' + l.body + annex(rows) + L.foot;
}
function render() { L.items.forEach(l => { $(l.id).value = build(l); }); }
['nm', 'ad', 'dept'].forEach(id => $(id).addEventListener('input', render));
document.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', async () => {
  const t = $(b.dataset.copy); let ok = false;
  try { await navigator.clipboard.writeText(t.value); ok = true } catch (e) { t.select(); try { ok = document.execCommand('copy') } catch (e2) {} }
  b.nextElementSibling.nextElementSibling.textContent = ok ? 'Copied.' : 'Select the text and copy it.';
}));
document.querySelectorAll('[data-dl]').forEach(b => b.addEventListener('click', () => {
  const t = $(b.dataset.dl), a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([t.value.replace(/\\n/g, '\\r\\n')], { type: 'text/plain' }));
  a.download = 'RTI_' + b.dataset.dl + '.txt'; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}));
render();
"""

esc = html.escape
opts = "".join(f'<option>{esc(k)}</option>' for k in DEPTS)
cards = []
for l in LETTERS:
    extra = ""
    if l["annex"] == "dept":
        extra = f'<label for="dept">Department</label><select id="dept">{opts}</select>'
    if l["annex"] == "all":
        extra = f'<p class="note">The annex lists all {len(DATA)} officers the Lokayukta acted against in the tracker, by post, place and date.</p>'
    cards.append(f"""<section class="card"><h3>{esc(l['title'])}</h3><p>{esc(l['why'])}</p>{extra}
<textarea class="letter" id="{l['id']}" aria-label="{esc(l['title'])} letter text" spellcheck="false"></textarea>
<div class="row"><button class="primary" data-copy="{l['id']}">Copy letter</button><button data-dl="{l['id']}">Download .txt</button><span class="ok" aria-live="polite"></span></div></section>""")

LJSON = json.dumps({"head": HEAD, "foot": FOOT, "items": [{k: l[k] for k in ("id", "to", "body", "annex")} for l in LETTERS]}, ensure_ascii=False)
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>File an RTI · Gandaberunda</title>
<meta name="description" content="Ready-to-file RTI letters asking what happened after the Lokayukta raids on Karnataka officials in 2026: chargesheets, sanction to prosecute, suspensions, property returns.">
<link rel="icon" type="image/svg+xml" href="brand/mark.svg">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Space+Grotesk:wght@500;700&display=swap">
<style>{css}</style>
</head>
<body>
<div class="bar"><a href="index.html#officials">← Gandaberunda · Officials</a></div>
<main>
<div class="kick">Gandaberunda · Right to Information · for any citizen of India</div>
<h1>Ask for the answer <em>yourself</em></h1>
<p class="lede">{len(rows)} Karnataka officials were raided, trapped or charged in 2026, according to the reports we track. For {stuck} of them, no later step has been reported: no chargesheet, no sanction, no verdict. The offices that know the answer must reply to any citizen within 30 days. Here are four letters, ready to print, sign and post.</p>
<p class="note">See every case on <a href="reports/officials_tracker.html">After the raid</a>. Letters carry posts and places, not names, the same as the tracker; the PIO can identify each officer from the post, place, date and the linked press report.</p>

<h2>Your details</h2>
<div class="card you">
<div><label for="nm">Your name</label><input id="nm" autocomplete="name"></div>
<div><label for="ad">Postal address in India for the reply</label><textarea id="ad" rows="2" autocomplete="street-address"></textarea></div>
</div>
<p class="note">These stay in your browser. Nothing you type is sent or saved anywhere; they only fill the letters below.</p>

<h2>The letters</h2>
{''.join(cards)}

<h2>How to file</h2>
<ol class="steps">
<li><b>Fill and sign.</b> Copy or download a letter, print it, fill the blanks (postal order number, place, date) and sign. For letter 3, add the department's head-office address from its website.</li>
<li><b>Pay Rs 10.</b> Attach an Indian Postal Order (or demand draft) for Rs 10, payable to the office's accounting officer as named on its RTI page. Applicants below the poverty line attach a copy of their BPL card instead. Copying charges are a few rupees a page; check the office's RTI page, since guides differ.</li>
<li><b>Post it</b> by Speed Post or registered post with acknowledgement. Keep a copy, the postal receipt and the postal-order counterfoil. Some departments also accept online RTI; check the department's site or the <a href="https://kic.karnataka.gov.in/" rel="noopener">Karnataka Information Commission</a>.</li>
<li><b>Wait 30 days.</b> The reply is due within 30 days of receipt. If your letter is sent on to another office, that office has its own 30 days.</li>
<li><b>No reply, or refused?</b> File a first appeal within 30 days to the First Appellate Authority (usually named in the reply or on the office's RTI page). A second appeal goes to the Karnataka Information Commission within 90 days.</li>
<li><b>Tell us the answer.</b> <a href="{FORM}" rel="noopener">Send us what you received</a> and we will add it to the tracker, with the post and the step, never your name.</li>
</ol>

<section class="card warn">
<h3>If the office refuses</h3>
<ul class="plain">
<li><b>"Ongoing investigation" (Section 8(1)(h)).</b> The office must explain how answering would hamper the investigation; quoting the section is not enough. Dates of a chargesheet or a sanction request reveal no evidence.</li>
<li><b>"Personal information" (Section 8(1)(j)).</b> The raids were announced by the Lokayukta and reported in the press. Ask for the information with names removed rather than refused (Section 10). Part A of letter 1 asks only for totals.</li>
<li><b>"Exempt from RTI" (Section 24).</b> In 2026 the Supreme Court held that Madhya Pradesh's Lokayukta police is not an intelligence or security organisation that can be exempted. If an office cites an exemption notification, ask for a copy.</li>
</ul>
</section>

<h2>Please</h2>
<ul class="plain">
<li>Ask for records, not opinions, and keep to the questions. A short, specific letter gets a better answer.</li>
<li>Do not add anyone's private details, and do not accuse anyone in the letter. A raid is an allegation, not a finding of guilt.</li>
<li>The fee and filing route are as described by RTI guides and offices' own pages as of Nov 2026; check them before you post.</li>
</ul>
<p class="note">Sources: Right to Information Act, 2005 (Sections 6, 7, 8, 10, 19, 24); Karnataka RTI Rules (fee); Special Police Establishment v. Kamta Prasad Mishra, 2026 INSC 644; case list from <a href="reports/officials_tracker.html">After the raid</a>, built from press reports linked there. Page built from the tracker as read on {d(max(r['checked_on'] for r in rows if r['checked_on']))}.</p>
</main>
<script>{js.replace('__DATA__', json.dumps(DATA, ensure_ascii=False)).replace('__LETTERS__', LJSON)}</script>
</body>
</html>
"""
(ROOT / "rti.html").write_text(page, encoding="utf-8", newline="\n")
print("rti.html", len(page) // 1024, "KB;", len(DATA), "Lokayukta rows;", len(DEPTS), "departments; stuck", stuck, "of", len(rows))
