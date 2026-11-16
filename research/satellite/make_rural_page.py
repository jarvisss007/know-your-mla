"""Build a DRAFT constituency scorecard page (and a field-check CSV) from a config-driven run folder.

    py research/satellite/make_rural_page.py research/satellite/kanakapura

Reads <folder>/config.json, metrics.json, data/robustness_dates.json and page_notes.json (the
per-seat prose, written by a person after looking at the images). Writes
<folder>/DRAFT_<slug>_scorecard.html and <folder>/field_checks.csv.
Numbers come only from metrics.json; this script adds no numbers of its own.
"""
import csv, html, json, pathlib, sys
from datetime import date

E = html.escape
D = pathlib.Path(sys.argv[1]).resolve()
cfg = json.loads((D / "config.json").read_text(encoding="utf-8"))
m = json.loads((D / "metrics.json").read_text(encoding="utf-8"))
notes = json.loads((D / "page_notes.json").read_text(encoding="utf-8"))
rob_path = D / "data" / "robustness_dates.json"
rob = json.loads(rob_path.read_text(encoding="utf-8"))["dates"] if rob_path.exists() else []
slug = cfg["ac_name"].lower().replace(" ", "_")

VEG, WAT, BLT = "vegetation_ndvi_gt_0.4", "open_water_mndwi_gt_0", "builtup_bare_proxy"
R = m["results_inside_boundary"]
y19, y26, net = R["by_year"]["2019"], R["by_year"]["2026"], R["net_change"]
G = R["gross_pixel_transitions"]


def n0(v):
    return f"{v:,.0f}"


def n1(v):
    return f"{v:,.1f}"


def signed(v, fmt=n0):
    return ("+" if v > 0 else "−" if v < 0 else "") + fmt(abs(v))


def osm_link(lat, lon, text=None):
    url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=16/{lat}/{lon}"
    return f'<a href="{url}" target="_blank" rel="noopener">{text or f"{lat:.4f}, {lon:.4f}"}</a>'


# ---- tiles
tiles = f"""
    <div class="tile"><span class="k">Green cover (NDVI &gt; 0.4)</span><span class="v">{signed(net[VEG]['ha_change'])} ha</span><span class="s">{n0(y19[VEG]['ha'])} → {n0(y26[VEG]['ha'])} ha · {y19[VEG]['pct']:.1f}% → {y26[VEG]['pct']:.1f}% of the area</span></div>
    <div class="tile"><span class="k">Open water (MNDWI &gt; 0)</span><span class="v">{signed(net[WAT]['ha_change'])} ha</span><span class="s">{n0(y19[WAT]['ha'])} → {n0(y26[WAT]['ha'])} ha</span></div>
    <div class="tile"><span class="k">Bare or built-up (proxy)</span><span class="v">{signed(net[BLT]['ha_change'])} ha net</span><span class="s">{n0(y19[BLT]['ha'])} → {n0(y26[BLT]['ha'])} ha · {n0(G['builtup_proxy_new_ha'])} ha newly entered it</span></div>
    <div class="tile"><span class="k">Area compared</span><span class="v">{n0(m['method']['comparison_area_ha'])} ha</span><span class="s">{m['method']['comparison_area_pct_of_boundary']:.1f}% of the constituency clear in both pictures</span></div>"""

# ---- date-swing chart (inline SVG): vegetation share on every clean Jan-Mar date, one line per year
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sat_chart import green_chart
chart = green_chart(rob, notes["pick_dates"], "Share of the constituency with green cover on every clean satellite date, January to March, in 2019, 2025 and 2026") if rob else ""

# ---- forest inside vs outside
forest = ""
FR = m.get("vegetation_inside_vs_outside_osm_protected_forest")
if FR:
    rows = []
    for key, lab in (("protected_or_forest_union", "Inside protected areas and forests (OSM)"), ("outside_protected_and_forest", "Everywhere else")):
        r = FR["regions"][key]
        a, b = r["by_year"]["2019"][VEG], r["by_year"]["2026"][VEG]
        rows.append(f"<tr><td>{lab}</td><td>{n0(r['area_ha_inside_boundary'])}</td><td>{a['pct']:.1f}%</td><td>{b['pct']:.1f}%</td>"
                    f"<td>{n0(r['vegetation_lost_ha'])}</td><td>{n0(r['vegetation_gained_ha'])}</td><td>{n0(r['builtup_proxy_new_ha'])}</td></tr>")
    names = ", ".join(f"{E(f['name'])} ({n0(f['ha_inside_boundary'])} ha)" for f in sorted(FR["features"], key=lambda f: -f["ha_inside_boundary"]) if f.get("name"))
    forest = f"""
  <section class="sec">
    <h2>Forests and protected areas compared with the rest</h2>
    <div class="tablewrap"><table>
      <thead><tr><th>Area</th><th>Hectares</th><th>Green 2019</th><th>Green 2026</th><th>Green lost (ha)</th><th>Green gained (ha)</th><th>New bare (ha)</th></tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table></div>
    <p class="foot">OpenStreetMap outlines inside the boundary: {names}. {E(notes.get('forest_note', ''))}</p>
  </section>"""

# ---- water bodies
wb = [x for x in m["water_bodies_osm"]["water_bodies"]
      if x.get("water_ha_2019") is not None and x["osm_polygon_ha_inside_boundary"] >= cfg.get("min_lake_ha", 2)]
wb.sort(key=lambda x: -abs(x["water_ha_2026"] - x["water_ha_2019"]))
wrows = []
for x in wb[:10]:
    d = x["water_ha_2026"] - x["water_ha_2019"]
    kn = f' <span lang="kn" class="kn">{E(x["name_kn"][0])}</span>' if x.get("name_kn") else ""
    name = E(x["name"]) if x.get("named_in_osm") else f'Unnamed ({E(x["osm_ids"][0])})'
    edge = ' <span class="flag">edge</span>' if x["osm_polygon_ha_total"] - x["osm_polygon_ha_inside_boundary"] > 0.5 else ""
    wrows.append(f"<tr><td>{name}{kn}{edge}</td><td>{osm_link(x['point_lat'], x['point_lon'])}</td><td>{n1(x['water_ha_2019'])}</td><td>{n1(x['water_ha_2026'])}</td>"
                 f"<td class=\"{'up' if d > 0 else 'dn'}\">{signed(d, n1)}</td><td>{n1(x['vegetation_ha_2019'])}</td><td>{n1(x['vegetation_ha_2026'])}</td></tr>")

# ---- clusters + field-check CSV
CL = m["new_bare_or_builtup_proxy_clusters"]
crow, csvrows = [], []
for c in CL["largest"]:
    lat, lon = c["nearest_member_pixel_lat"], c["nearest_member_pixel_lon"]
    crow.append(f"<tr><td>{c['rank']}</td><td>{n1(c['area_ha'])}</td><td>{osm_link(lat, lon)}</td><td>{c['pct_was_vegetation_2019']:.0f}%</td>"
                f"<td>{c['pct_inside_osm_protected_or_forest']:.0f}%</td><td>{c['median_dnbr']:.2f}</td></tr>")
    csvrows.append({"constituency": cfg["display_name"], "rank": c["rank"], "area_ha": c["area_ha"], "lat": lat, "lon": lon,
                    "osm_url": f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=16/{lat}/{lon}",
                    "pct_green_2019": c["pct_was_vegetation_2019"], "pct_in_osm_forest": c["pct_inside_osm_protected_or_forest"],
                    "median_dnbr": c["median_dnbr"], "label": "new bare or built-up ground (proxy)",
                    "what_is_there_now": "", "photo_date": "", "photo_file": "", "checked_by": "", "notes": ""})
with open(D / "field_checks.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=list(csvrows[0]))
    w.writeheader()
    w.writerows(csvrows)
st = CL["stats"]

S19, S26 = m["imagery"]["scenes"]["2019"], m["imagery"]["scenes"]["2026"]
limits = "".join(f"<li>{E(x)}</li>" for x in notes["limits"])
caveat = notes.get("caveat", "")

page = f"""<title>{E(cfg['ac_name'])} From Space</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;600&family=Noto+Sans+Kannada:wght@400;600&display=swap">
<style>
/* Layout: headline tiles, the "is it real?" date check, images, forest/water/cluster tables, limits. */
:root {{
  --bg: #f5f6f8; --surface: #ffffff; --fg: #161a22; --muted: #5b6474; --line: #dde1e8; --grid: #e7eaef;
  --red: #c21f30; --yellow: #f2b705; --blue: #1f6fbf; --warn-bg: #fff6d6; --warn-line: #e8c547;
  --s19: #8a6d3b; --s25: #9aa3b2; --s26: #1f6fbf;
  --display: "Space Grotesk", system-ui, sans-serif; --body: "Inter", system-ui, "Segoe UI", sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d; --grid: #232834;
  --red: #ef5261; --yellow: #f5c93a; --blue: #6aaef0; --warn-bg: #2a2410; --warn-line: #7a6420;
  --s19: #d2a764; --s25: #6b7383; --s26: #6aaef0; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d; --grid: #232834;
  --red: #ef5261; --yellow: #f5c93a; --blue: #6aaef0; --warn-bg: #2a2410; --warn-line: #7a6420;
  --s19: #d2a764; --s25: #6b7383; --s26: #6aaef0; color-scheme: dark }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--fg); font-family: var(--body); font-size: 16px; line-height: 1.6; }}
.wrap {{ max-width: 960px; margin: 0 auto; padding-block: 28px 64px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); display: grid; gap: 28px; }}
h1, h2 {{ font-family: var(--display); text-wrap: balance; margin: 0; line-height: 1.2; }}
h1 {{ font-size: clamp(1.8rem, 4.5vw, 2.6rem); }} h2 {{ font-size: 1.25rem; }}
p {{ margin: 0; }}
a {{ color: var(--blue); }}
.eyebrow {{ font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; color: var(--red); font-weight: 600; }}
.draft {{ display: inline-block; font-size: .75rem; font-weight: 700; letter-spacing: .06em; background: var(--yellow); color: #161a22; padding: 2px 8px; border-radius: 4px; }}
.lede {{ color: var(--muted); max-width: 66ch; }}
.sec {{ display: grid; gap: 12px; min-width: 0; }}
.warn {{ background: var(--warn-bg); border: 1px solid var(--warn-line); border-radius: 10px; padding: 14px 18px; display: grid; gap: 6px; max-width: 75ch; }}
.warn strong {{ font-family: var(--display); }}
.tiles {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(210px, 100%), 1fr)); gap: 12px; }}
.tile {{ background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 16px 18px; display: grid; gap: 4px; align-content: start; }}
.tile .k {{ font-size: .78rem; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); font-weight: 600; }}
.tile .v {{ font-family: var(--display); font-size: 2rem; font-weight: 700; font-variant-numeric: tabular-nums; line-height: 1.1; }}
.tile .s {{ font-size: .88rem; color: var(--muted); font-variant-numeric: tabular-nums; }}
.chart {{ background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 12px; }}
.chart svg {{ width: 100%; height: auto; display: block; }}
.grid {{ stroke: var(--grid); stroke-width: 1; }}
.ax {{ fill: var(--muted); font: 12px var(--body); }}
.ln {{ fill: none; stroke-width: 2; }}
.lab {{ font: 600 13px var(--body); }}
.s19 {{ stroke: var(--s19); fill: var(--s19); }} .s25 {{ stroke: var(--s25); fill: var(--s25); }} .s26 {{ stroke: var(--s26); fill: var(--s26); }}
.ln.s19, .ln.s25, .ln.s26 {{ fill: none; }}
.pt {{ stroke: var(--surface); stroke-width: 1.5; }} .pt.pick {{ stroke: var(--fg); stroke-width: 2; }}
figure {{ margin: 0; display: grid; gap: 8px; min-width: 0; }}
figure img {{ width: 100%; max-width: 100%; height: auto; border-radius: 8px; border: 1px solid var(--line); display: block; }}
figcaption {{ font-size: .85rem; color: var(--muted); }}
.maps {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }}
@media (max-width: 720px) {{ .maps {{ grid-template-columns: 1fr; }} }}
.tablewrap {{ overflow-x: auto; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; }}
table {{ border-collapse: collapse; width: 100%; font-size: .92rem; font-variant-numeric: tabular-nums; min-width: 600px; }}
th, td {{ padding: 8px 12px; text-align: right; border-bottom: 1px solid var(--line); }}
th:first-child, td:first-child {{ text-align: left; }}
th {{ font-size: .75rem; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); font-weight: 600; }}
td.up {{ color: var(--blue); font-weight: 600; }} td.dn {{ color: var(--red); font-weight: 600; }}
.kn {{ font-family: "Noto Sans Kannada", var(--body); color: var(--muted); font-size: .85rem; }}
.flag {{ font-size: .7rem; border: 1px solid var(--muted); color: var(--muted); border-radius: 999px; padding: 0 6px; margin-left: 4px; }}
ul.limits {{ margin: 0; padding-left: 1.2em; display: grid; gap: 6px; max-width: 72ch; }}
.foot {{ font-size: .85rem; color: var(--muted); max-width: 80ch; }}
.foot a {{ color: inherit; }}
</style>

<div class="wrap">
  <div style="display:grid;gap:8px">
    <span class="eyebrow">Gandaberunda · What changed on the ground</span>
    <h1>{E(cfg['ac_name'])} from space, {E(notes['date_phrase'])}</h1>
    <span><span class="draft">DRAFT · PILOT · NOT FOR PUBLICATION</span></span>
  </div>
  <p class="lede">{E(notes['lede'])}</p>

  <div class="warn"><strong>{E(notes['warning_title'])}</strong><p>{E(notes['warning'])}</p></div>

  <div class="tiles">{tiles}
  </div>

  {'<section class="sec"><h2>' + E(notes['chart_title']) + '</h2><div class="chart">' + chart + '</div><p class="foot">' + E(notes['chart_note']) + '</p></section>' if chart else ''}

  <div class="maps">
    <figure><img src="truecolor_2019_2026.png" alt="True-colour satellite images of {E(cfg['ac_name'])}, {E(notes['date_phrase'])}, with the boundary in yellow"><figcaption>True colour. Left: {E(notes['d19'])}. Right: {E(notes['d26'])}. Yellow line: constituency boundary.</figcaption></figure>
    <figure><img src="change_map_2019_2026.png" alt="Change map: green marks green cover lost, blue marks water lost, red marks new bare or built-up ground"><figcaption>Change map. Green: green cover lost. Blue: water lost. Red: new bare or built-up ground (proxy). {E(notes.get('change_caption', ''))}</figcaption></figure>
  </div>
{forest}
  <section class="sec">
    <h2>Water bodies: the ten biggest changes in open water (hectares)</h2>
    <div class="tablewrap"><table>
      <thead><tr><th>Water body (OpenStreetMap)</th><th>Location</th><th>Water 2019</th><th>Water 2026</th><th>Change</th><th>Green on it 2019</th><th>Green on it 2026</th></tr></thead>
      <tbody>{''.join(wrows)}</tbody>
    </table></div>
    <p class="foot">{m['water_bodies_osm']['total_count']} water polygons in OpenStreetMap touch the boundary and {m['water_bodies_osm']['named_count']} have names; those of at least {cfg.get('min_lake_ha', 2):g} ha are measured. "Green on it" is usually weeds or crops on a dry bed. Tanks fill and empty with each monsoon, so one February picture says little about a tank's long-term state. "Edge" marks a polygon that crosses the boundary; only the part inside is counted.</p>
  </section>

  <section class="sec">
    <h2>Places to check on the ground: the {len(crow)} largest patches of new bare or built-up ground</h2>
    <figure><img src="clusters.png" alt="Map of {E(cfg['ac_name'])} with the {len(crow)} largest new bare-ground patches numbered"><figcaption>Numbers match the table. Background: the 2026 picture.</figcaption></figure>
    <div class="tablewrap"><table>
      <thead><tr><th>#</th><th>Hectares</th><th>Location (opens map)</th><th>Green in 2019</th><th>In OSM forest</th><th>Burn index (dNBR)</th></tr></thead>
      <tbody>{''.join(crow)}</tbody>
    </table></div>
    <p class="foot">Each patch went from not bare in 2019 to bare or built-up on the 2026 date. It could be a quarry, construction, a ploughed or harvested field, dry grass, burnt scrub or a drained tank. This analysis cannot tell which and says nothing about cause, ownership or legality. A dNBR above about 0.1 is often seen on burnt ground but also on harvest and clearing. In all, {n0(st['regions_ge_1ha'])} patches are 1 ha or larger and {n0(st['regions_ge_5ha'])} are 5 ha or larger. A blank field-check sheet for these locations is in field_checks.csv in the repo: a photo and one line on what is there turns a proxy into a fact.</p>
  </section>

  <section class="sec">
    <h2>Limits</h2>
    <ul class="limits">{limits}</ul>
  </section>

  <p class="foot">Data: Copernicus Sentinel-2 L2A via Microsoft Planetary Computer ({E(notes['scene_credit'])}); boundary from <a href="https://github.com/datameet/maps" target="_blank" rel="noopener">DataMeet</a> (CC BY 2.5 India); water, forest and protected-area outlines from OpenStreetMap (ODbL). Method, scripts and every number are in research/satellite/{D.name}/ in the repo (METHOD.md, metrics.json). DRAFT, {E(notes['as_of'])}.</p>
</div>
"""
out = D / f"DRAFT_{slug}_scorecard.html"
out.write_text(page, encoding="utf-8", newline="\n")
print("ok", out.name, len(wrows), "water rows", len(crow), "clusters", "chart" if chart else "no chart")
