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

import sys
sys.path.insert(0, str(HERE))
from sat_chart import green_chart, CHART_CSS
rob = json.loads((HERE / "mahadevapura_datecheck" / "data" / "robustness_dates.json").read_text(encoding="utf-8"))["dates"]
chart = green_chart(rob, ["2019-02-13", "2026-02-11"], "Share of Mahadevapura with green cover on every clean satellite date, January to March, in 2019, 2025 and 2026")
page = ((HERE / "page_template.html").read_text(encoding="utf-8").replace("<!--LAKE_ROWS-->", "\n".join(rows))
        .replace("<!--CHART-->", chart).replace("/*CHART_CSS*/", CHART_CSS))
(HERE / "DRAFT_mahadevapura_scorecard.html").write_text(page, encoding="utf-8", newline="\n")
print("ok", len(rows), "lake rows")
