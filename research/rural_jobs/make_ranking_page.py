"""Build DRAFT_photo_check_ranking.html from photo_check_blocks_2024-25.csv (block-level aggregates only).
    py research/rural_jobs/make_ranking_page.py
Then publish with: py tools/publish_reports.py"""
import csv, json, pathlib, html
H = pathlib.Path(__file__).resolve().parent
rows = list(csv.DictReader(open(H / 'photo_check_blocks_2024-25.csv', encoding='utf-8')))
for r in rows:
    for k in list(r)[2:]:
        r[k] = float(r[k]) if r[k] != '' else None
R = [r for r in rows if (r['works_2024_25'] or 0) >= 200]
FAR, CL = 'pct_photos_over_10km_from_own_panchayat', 'pct_in_5plus_work_spots_across_panchayats'


def med(k):
    v = sorted(r[k] or 0 for r in R)
    return v[len(v) // 2]


def p90(k):
    v = sorted(r[k] or 0 for r in R)
    return v[int(len(v) * .9)]


total = int(sum(r['works_2024_25'] or 0 for r in rows))


def bars(k, top=15):
    s = sorted(R, key=lambda r: -(r[k] or 0))[:top]
    mx = s[0][k]
    out = []
    for i, r in enumerate(s, 1):
        w = 100 * r[k] / mx
        out.append(f'<li><span class="rk">{i}</span><span class="nm">{html.escape(r["block"])} <small>{html.escape(r["district"])}</small></span>'
                   f'<span class="bar"><span style="width:{w:.1f}%"></span></span><span class="v">{r[k]:.2f}%</span></li>')
    return '\n'.join(out)


data = [[r['district'], r['block'], int(r['works_2024_25'] or 0), r[FAR], r[CL], r['pct_sharing_exact_gps_point'], r['pct_phone_moves_over_60kmh']] for r in rows]
g = next(r for r in R if r['block'] == 'Gangavathi')
k = next(r for r in R if r['block'] == 'Karatagi')

CSS = """
:root { --bg:#f5f6f8; --surface:#fff; --fg:#161a22; --muted:#5b6474; --line:#dde1e8; --red:#c21f30; --yellow:#f2b705; --track:#e3e6ec;
  --display:"Space Grotesk","Segoe UI",system-ui,sans-serif; --body:Inter,"Segoe UI",system-ui,sans-serif; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#11141a; --surface:#1a1e27; --fg:#eceef2; --muted:#9aa3b2; --line:#2b313d; --red:#ef5261; --yellow:#f5c93a; --track:#2b313d; color-scheme:dark } }
:root[data-theme="dark"] { --bg:#11141a; --surface:#1a1e27; --fg:#eceef2; --muted:#9aa3b2; --line:#2b313d; --red:#ef5261; --yellow:#f5c93a; --track:#2b313d; color-scheme:dark }
body { background:var(--bg); color:var(--fg); font:16px/1.55 var(--body); padding-block:28px 64px; padding-left:max(16px,env(safe-area-inset-left,0px)); padding-right:max(16px,env(safe-area-inset-right,0px)); }
.wrap { max-width:860px; margin:0 auto; display:flex; flex-direction:column; gap:40px; }
a { color:inherit; text-underline-offset:3px; }
h1,h2,h3 { font-family:var(--display); text-wrap:balance; margin:0; }
h1 { font-size:clamp(2.1rem,7vw,3.4rem); line-height:1.02; letter-spacing:-.02em; } h1 span { color:var(--red); }
h2 { font-size:1.45rem; } p { margin:0; max-width:66ch; }
section { display:flex; flex-direction:column; gap:14px; }
.eyebrow { font-size:.75rem; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); font-weight:600; }
.draft { display:inline-block; background:var(--yellow); color:#161a22; font-weight:600; font-size:.8rem; padding:3px 10px; border-radius:3px; letter-spacing:.04em; align-self:flex-start; }
header { display:flex; flex-direction:column; gap:14px; } .lede { font-size:1.1rem; } .muted { color:var(--muted); font-size:.9rem; }
.tiles { display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); border-block:2px solid var(--fg); }
.tile { padding:16px 14px 16px 0; display:flex; flex-direction:column; gap:4px; }
.tile b { font-family:var(--display); font-size:2rem; line-height:1; } .tile.hot b { color:var(--red); }
ol.bars { list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:6px; }
ol.bars li { display:grid; grid-template-columns:2ch minmax(9ch,15ch) 1fr 6ch; gap:10px; align-items:center; font-size:.95rem; }
.rk { color:var(--muted); text-align:right; font-variant-numeric:tabular-nums; } .nm small { color:var(--muted); display:block; font-size:.75rem; }
.bar { background:var(--track); height:12px; border-radius:2px; overflow:hidden; } .bar span { display:block; height:100%; background:var(--red); }
.v { text-align:right; font-variant-numeric:tabular-nums; font-weight:600; }
.note { background:var(--surface); border:1px solid var(--line); border-left:4px solid var(--yellow); border-radius:10px; padding:14px 16px; display:flex; flex-direction:column; gap:8px; }
.note ul { margin:0; padding-left:1.2em; }
input[type=search] { font:inherit; padding:10px 12px; border:1px solid var(--line); border-radius:8px; background:var(--surface); color:var(--fg); max-width:420px; width:100%; box-sizing:border-box; }
.tablewrap { overflow-x:auto; border:1px solid var(--line); border-radius:10px; background:var(--surface); max-height:70vh; }
table { border-collapse:collapse; width:100%; font-size:.9rem; font-variant-numeric:tabular-nums; }
th, td { padding:7px 10px; border-bottom:1px solid var(--line); text-align:right; white-space:nowrap; }
th:nth-child(-n+2), td:nth-child(-n+2) { text-align:left; }
th { position:sticky; top:0; background:var(--surface); cursor:pointer; font-weight:600; } th[aria-sort] { color:var(--red); }
td.hi { color:var(--red); font-weight:600; }
ol.steps { margin:0; padding-left:1.3em; display:flex; flex-direction:column; gap:6px; max-width:66ch; }
"""

JS = """
const tb = document.querySelector('#t tbody'), q = document.getElementById('q');
const cut = {};
[3,4,5,6].forEach(i => { const v = D.filter(r => r[2] >= 200).map(r => r[i] || 0).sort((a,b) => a-b); cut[i] = v[Math.floor(v.length*.9)]; });
let key = 3, dir = -1;
function draw() {
  const s = q.value.trim().toLowerCase();
  const rows = D.filter(r => !s || (r[0]+' '+r[1]).toLowerCase().includes(s)).sort((a,b) => {
    const x = a[key], y = b[key];
    return (typeof x === 'string' ? x.localeCompare(y) : ((x ?? -1) - (y ?? -1))) * dir; });
  tb.innerHTML = rows.map(r => '<tr><td>'+r[0]+'</td><td>'+r[1]+'</td><td>'+r[2].toLocaleString('en-IN')+'</td>' +
    [3,4,5,6].map(i => '<td'+(r[2] >= 200 && r[i] != null && r[i] > cut[i] ? ' class="hi"' : '')+'>'+(r[i] == null ? '–' : r[i].toFixed(2))+'</td>').join('') + '</tr>').join('');
  document.querySelectorAll('#t th').forEach(th => th.toggleAttribute('aria-sort', +th.dataset.k === key));
}
document.querySelectorAll('#t th').forEach(th => th.addEventListener('click', () => {
  const k = +th.dataset.k; dir = (k === key) ? -dir : (k < 2 ? 1 : -1); key = k; draw(); }));
q.addEventListener('input', draw); draw();
"""

page = f'''<title>Where the Work Photos Are Taken</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header>
  <span class="draft">DRAFT · NOT PUBLISHED</span>
  <span class="eyebrow">Rural job scheme (MGNREGA) · all 236 blocks of Karnataka · 2024-25</span>
  <h1>Where the work photos <span>are taken</span></h1>
  <p class="lede">Every finished MGNREGA work needs a geotagged photo as proof. We read the location of all {total:,} completion photos the government accepted in Karnataka for 2024-25 and asked one question: was the photo taken near the panchayat the work belongs to?</p>
  <p class="muted">Source: Bhuvan-BHUGRAM public dashboard (NRSC/ISRO for the Ministry of Rural Development), "Accepted Geotags", Phase II after-photos geotagged 1 April 2024 to 31 March 2025, read on 18 November 2026. Block-level figures only: no names, no individual works.</p>
</header>

<div class="tiles">
  <div class="tile"><b>{total/1e5:.2f} lakh</b><span class="muted">completion photos read, 236 blocks</span></div>
  <div class="tile"><b>{med(FAR):.2f}%</b><span class="muted">typical block: photos taken more than 10 km from the work's own panchayat</span></div>
  <div class="tile hot"><b>{g[FAR]:.1f}%</b><span class="muted">Gangavathi (Koppal), 1st of {len(R)} blocks</span></div>
  <div class="tile hot"><b>{k[FAR]:.1f}%</b><span class="muted">Karatagi (Koppal), 2nd of {len(R)} blocks</span></div>
</div>

<section>
  <h2>Photos taken more than 10 km from the work's own panchayat</h2>
  <p>For each panchayat we take the middle point of all its completion photos, then count the photos taken more than 10 km from it. In a typical block that is {med(FAR):.2f}% of photos, and nine blocks in ten are under {p90(FAR):.2f}%. These are the 15 highest (blocks with at least 200 works):</p>
  <ol class="bars">
{bars(FAR)}
  </ol>
</section>

<section>
  <h2>Five or more works from different panchayats photographed at one spot</h2>
  <p>The share of a block's works whose photo was taken at a spot of about 50 metres shared by at least five different works from two or more panchayats. In most blocks this is zero, and nine in ten are under {p90(CL):.2f}%.</p>
  <ol class="bars">
{bars(CL, 10)}
  </ol>
</section>

<div class="note">
  <strong>What these numbers mean, and what they do not</strong>
  <ul>
    <li>They do <b>not</b> show that any work is fake. They show where the government's own location check tells us little, or where something unusual is happening and the records are worth asking for.</li>
    <li>There are innocent explanations. Labourers from several panchayats can be sent to one big tank, so many works get photographed there. A panchayat with two villages far apart can look "far" from its own middle point. A phone without a GPS fix can report an old location.</li>
    <li>The check meant to catch problems almost never says no: Karnataka's moderators rejected 419 of 42.5 lakh after-photos (0.010%), a quarter of the national rate (<a href="https://bhuvan-app2.nrsc.gov.in/bhugram/usrtasks/nrega_phase2/get/stats.php">Bhuvan statistics report</a>).</li>
    <li>Right to Information requests for the estimates and measurement books behind the highest-ranked blocks are being prepared. We will publish what comes back, including any explanation from the officials concerned.</li>
  </ul>
</div>

<section>
  <h2>Find your block</h2>
  <p class="muted">All 236 blocks. Tap a column to sort. Red marks the top tenth of blocks on that measure. The last two columns are less reliable (see below).</p>
  <input type="search" id="q" placeholder="Type a district or block" aria-label="Filter blocks">
  <div class="tablewrap"><table id="t"><thead><tr>
    <th data-k="0">District</th><th data-k="1">Block</th><th data-k="2">Works</th><th data-k="3">Far from panchayat %</th>
    <th data-k="4">Shared spot, 2+ panchayats %</th><th data-k="5">Same exact GPS point %</th><th data-k="6">Phone "moved" over 60 km/h %</th>
  </tr></thead><tbody></tbody></table></div>
  <p class="muted"><a href="photo_check_blocks_2024-25.csv">Download the table (CSV)</a>. Four newly created taluks returned no rows: Harohalli, Hubballi Nagara, Kushalnagar and Arakera.</p>
</section>

<section>
  <h2>Two measures to treat with care</h2>
  <p><b>Same exact GPS point.</b> In some blocks many different works carry the identical location, to about a metre. Where we looked, the photos showed different places: the phone's location had stuck or been set by hand, rather than photos being reused. That still matters, because for those works the geotag proves nothing, and the system accepted it.</p>
  <p><b>Phone "moving" faster than 60 km/h between photos.</b> This is high across the whole north-east of the state (Yadgir, Raichur, Vijayapura). A pattern that broad is more likely wrong phone clocks or photos uploaded in batches than anything in one block.</p>
</section>

<section>
  <h2>How to check this yourself</h2>
  <ol class="steps">
    <li>Open the <a href="https://bhuvan-app2.nrsc.gov.in/bhugram/bhugram_dashboard/">Bhuvan-BHUGRAM dashboard</a>. Choose the report "Accepted Geotags", stage "PHASE II: AFTER", state Karnataka, your district and block, and dates 01-04-2024 to 31-03-2025.</li>
    <li>Each row gives the work code, panchayat, location and two photo links. The photo's file name contains the phone's ID and the time it was taken.</li>
    <li>Group the photos by panchayat, take the middle location, and measure each photo's distance from it.</li>
  </ol>
  <p class="muted">Method notes: blocks with fewer than 200 works are left out of the rankings but kept in the table. A "spot" is a cell of about 50 m. Coordinates outside Karnataka's bounding box are dropped. The calculation reproduces figures first computed from the dashboard's own Excel export for Koppal district.</p>
</section>

<p class="muted">Corrections and replies: if you are an official or a resident with an explanation or a correction, use <a href="../index.html#join">Have your say</a>. We publish replies in full.</p>
<p class="muted">Related: <a href="tank_findings.html">One tank, many works</a>, the cases behind the top of this ranking.</p>
<footer style="border-top:2px solid var(--fg);padding-top:16px"><p class="muted"><b>© 2026 Gandaberunda (Know Your MLA).</b> The analysis, rankings, text and charts are original work by Gandaberunda. News organisations may quote and reproduce them with the credit "Gandaberunda / Know Your MLA" and a link to this page. The underlying records are public (NRSC/ISRO, Ministry of Rural Development).</p></footer>
</div>
<script>
const D = {json.dumps(data, ensure_ascii=False)};
{JS}
</script>
'''
(H / 'DRAFT_photo_check_ranking.html').write_text(page, encoding='utf-8')
print('ok', len(page) // 1024, 'KB')
