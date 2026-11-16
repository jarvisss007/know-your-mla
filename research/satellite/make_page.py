"""Build DRAFT_mahadevapura_scorecard.html from metrics.json.   py research/satellite/make_page.py"""
import html, json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
m = json.loads((HERE / "metrics.json").read_text(encoding="utf-8"))
lakes = [x for x in m["lakes_osm"]["lakes"] if x.get("water_ha_2019") is not None]
lakes.sort(key=lambda x: -abs(x["water_ha_2026"] - x["water_ha_2019"]))


def f(v):
    return f"{v:,.1f}"


rows = []
for x in lakes[:12]:
    edge = ' <span class="flag">edge</span>' if x.get("boundary_flag") else ""
    d = x["water_ha_2026"] - x["water_ha_2019"]
    cls = "up" if d > 0 else "dn"
    sign = "+" if d > 0 else ""
    rows.append(
        f"<tr><td>{html.escape(x['name'])}{edge}</td><td>{f(x['water_ha_2019'])}</td><td>{f(x['water_ha_2026'])}</td>"
        f"<td class=\"{cls}\">{sign}{f(d)}</td><td>{f(x['vegetation_ha_2019'])}</td><td>{f(x['vegetation_ha_2026'])}</td></tr>"
    )

page = (HERE / "page_template.html").read_text(encoding="utf-8").replace("<!--LAKE_ROWS-->", "\n".join(rows))
(HERE / "DRAFT_mahadevapura_scorecard.html").write_text(page, encoding="utf-8", newline="\n")
print("ok", len(rows), "lake rows")
