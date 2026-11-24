"""DRAFT. Step 3, multi-date check for the lakes with the biggest changes (not used for the headline
numbers). For the robustness_n_lakes largest |water change| in lakes.csv (duplicate outlines
skipped), plus any of the 5 largest water losses and 5 largest green-on-lake changes not already
in that list, re-measures open water (MNDWI > 0) and green on lake (NDVI > 0.4) on EVERY
Jan-Mar acquisition of 2019, 2025 and 2026 on relative orbit R019, tile 43PGQ. A date counts
for a lake only if at least robustness_min_lake_valid_pct of the lake's pixels pass the SCL
mask on that date. Same 10 m grid, resampling, thresholds, mask and offset as analyze_lakes.py.
Writes data/robustness_lakes.json and robustness_lakes.csv."""
import json, sys, time, csv
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import rasterio
from rasterio.vrt import WarpedVRT
from rasterio.enums import Resampling
from rasterio.features import geometry_mask
from rasterio.transform import from_origin
from pyproj import Transformer
from shapely.geometry import shape, mapping
from shapely.ops import transform as shp_transform
import pystac_client
import planetary_computer

HERE = Path(__file__).parent
CFG = json.load(open(HERE / "config.json"))
STAC = "https://planetarycomputer.microsoft.com/api/stac/v1"
DST_CRS, RES = CFG["dst_crs"], float(CFG["res_m"])
BAD_SCL = [0, 1, 3, 8, 9, 10]
MINV = CFG["robustness_min_lake_valid_pct"]
to_utm = Transformer.from_crs("EPSG:4326", DST_CRS, always_xy=True).transform

feats = json.load(open(HERE / "data/measured_lakes.geojson", encoding="utf-8"))["features"]
lk = [f for f in feats if not f["properties"]["overlaps_larger_outline"]
      and min(f["properties"]["valid_pct_2019"], f["properties"]["valid_pct_2026"]) >= 90]
pick = sorted(lk, key=lambda f: -abs(f["properties"]["water_change_ha"]))[:CFG["robustness_n_lakes"]]
extra = sorted(lk, key=lambda f: f["properties"]["water_change_ha"])[:5] + \
        sorted(lk, key=lambda f: -abs(f["properties"]["green_change_ha"]))[:5]
for f in extra:
    if f not in pick:
        pick.append(f)
LAKES = []
for f in pick:
    g = shp_transform(to_utm, shape(f["geometry"]))
    x0, y0, x1, y1 = g.bounds
    x0 = np.floor(x0 / 20) * 20 - 40; y1 = np.ceil(y1 / 20) * 20 + 40
    x1 = np.ceil(x1 / 20) * 20 + 40; y0 = np.floor(y0 / 20) * 20 - 40
    w, h = int(round((x1 - x0) / RES)), int(round((y1 - y0) / RES))
    tr = from_origin(x0, y1, RES, RES)
    LAKES.append({"p": f["properties"], "tr": tr, "w": w, "h": h,
                  "m": geometry_mask([mapping(g)], (h, w), tr, invert=True)})
print(len(LAKES), "lakes", file=sys.stderr)

RESUM = "--resummarize" in sys.argv  # recompute verdicts from data/robustness_lakes.json, no imagery reads
cat = pystac_client.Client.open(STAC, modifier=planetary_computer.sign_inplace)
union_ll = shape(json.load(open(HERE / "data/boundary/bengaluru_urban_union.geojson"))["features"][0]["geometry"])
items = []
for yr, rng in ({} if RESUM else CFG["search_windows"]).items():
    for it in cat.search(collections=["sentinel-2-l2a"], intersects=mapping(union_ll.centroid), datetime=rng).items():
        if it.properties.get("s2:mgrs_tile") == "43PGQ" and it.properties.get("sat:relative_orbit") == CFG["robustness_orbit"]:
            items.append(it)
by_day = {}
for it in sorted(items, key=lambda i: i.id):  # one item per day (latest processing)
    by_day[it.properties["datetime"][:10]] = it
print(len(by_day), "dates", file=sys.stderr)


def one(day):
    it = by_day[day]
    off = -1000 if float(it.properties.get("s2:processing_baseline", "0")) >= 4.0 else 0
    srcs = {k: rasterio.open(it.assets[k].href) for k in ["B03", "B04", "B08", "B11", "SCL"]}
    out = []
    try:
        for L in LAKES:
            arr = {}
            for k, s in srcs.items():
                rs = Resampling.bilinear if k == "B11" else Resampling.nearest
                with WarpedVRT(s, crs=DST_CRS, transform=L["tr"], width=L["w"], height=L["h"], resampling=rs, nodata=0) as v:
                    arr[k] = v.read(1)
            b = {k: np.where(arr[k] == 0, np.nan, (arr[k].astype("float32") + off) / 1e4) for k in ["B03", "B04", "B08", "B11"]}
            with np.errstate(divide="ignore", invalid="ignore"):
                ndvi = (b["B08"] - b["B04"]) / (b["B08"] + b["B04"])
                mndwi = (b["B03"] - b["B11"]) / (b["B03"] + b["B11"])
                ndbi = (b["B11"] - b["B08"]) / (b["B11"] + b["B08"])
            valid = ~np.isin(arr["SCL"], BAD_SCL) & np.isfinite(ndvi) & np.isfinite(mndwi) & np.isfinite(ndbi) & L["m"]
            vp = float(valid.sum() / L["m"].sum() * 100)
            out.append({"lake": L["p"]["name"], "valid_pct": round(vp, 1),
                        "water_ha": round(float((valid & (mndwi > 0)).sum()) * RES * RES / 1e4, 2),
                        "green_ha": round(float((valid & (ndvi > 0.4)).sum()) * RES * RES / 1e4, 2)})
    finally:
        for s in srcs.values():
            s.close()
    return {"date": day, "platform": it.properties.get("platform"), "id": it.id,
            "tile_cloud_pct": it.properties.get("eo:cloud_cover"), "offset": off, "lakes": out}


def with_retry(day, tries=4):
    for t in range(tries):
        if t:
            time.sleep(15 * 2 ** (t - 1))
        try:
            r = one(day)
            print(day, "ok", file=sys.stderr)
            return r
        except Exception as e:
            err = repr(e)
            print("retry", day, t, err[:120], file=sys.stderr)
    return {"date": day, "error": err[:300]}


if RESUM:
    res = json.load(open(HERE / "data/robustness_lakes.json", encoding="utf-8"))["dates"]
else:
    with ThreadPoolExecutor(4) as ex:
        res = sorted(ex.map(with_retry, sorted(by_day)), key=lambda r: r["date"])

# per-lake summary and verdict
summ = []
for L in LAKES:
    p = L["p"]
    series = {}
    for r in res:
        for x in r.get("lakes", []):
            if x["lake"] == p["name"] and x["valid_pct"] >= MINV:
                series.setdefault(r["date"][:4], []).append((r["date"], x["water_ha"], x["green_ha"]))
    s = {"name": p["name"], "lat": p["lat"], "lon": p["lon"], "osm_ha_in_area": p["osm_ha_in_area"],
         "headline_water_2019": p["water_ha_2019"], "headline_water_2026": p["water_ha_2026"], "headline_water_change": p["water_change_ha"],
         "headline_green_2019": p["green_on_lake_ha_2019"], "headline_green_2026": p["green_on_lake_ha_2026"], "headline_green_change": p["green_change_ha"]}
    for yr in ["2019", "2025", "2026"]:
        v = series.get(yr, [])
        s[f"n_dates_{yr}"] = len(v)
        for key, idx in [("water", 1), ("green", 2)]:
            vals = [q[idx] for q in v]
            s[f"{key}_min_{yr}"] = min(vals) if vals else None
            s[f"{key}_median_{yr}"] = round(float(np.median(vals)), 2) if vals else None
            s[f"{key}_max_{yr}"] = max(vals) if vals else None
    s["series"] = series

    def verdict(key, change):
        a0, a1 = s[f"{key}_min_2019"], s[f"{key}_max_2019"]
        b0, b1 = s[f"{key}_min_2026"], s[f"{key}_max_2026"]
        if None in (a0, b0):
            return "not enough clean dates"
        if abs(change) < 2:
            return f"small headline change ({change:+.1f} ha), not assessed"
        m19, m26, m25 = s[f"{key}_median_2019"], s[f"{key}_median_2026"], s[f"{key}_median_2025"]
        med = m26 - m19
        if (change > 0 and b0 > a1) or (change < 0 and b1 < a0):
            v = f"holds: every clean 2026 date {'above' if change > 0 else 'below'} every clean 2019 date (median change {med:+.1f} ha)"
        elif med * change > 0 and abs(med) >= 0.5 * abs(change) and not (a0 <= m26 <= a1):
            v = f"mostly holds: 2026 median outside the 2019 range, same direction ({med:+.1f} ha), but single dates overlap"
        else:
            v = f"does not hold: swings with the date (median change {med:+.1f} ha vs headline {change:+.1f} ha)"
        if m25 is not None:
            side = "2026" if (m25 - m19) * change > 0 and abs(m25 - m19) >= 0.5 * abs(med) else "2019" if abs(m25 - m19) < 0.5 * abs(med) or (m25 - m19) * change < 0 else "neither"
            v += f"; 2025 median {m25:.1f} ha is {'on the 2026 side' if side == '2026' else 'closer to 2019 or beyond it'}"
        return v
    s["verdict_water"] = verdict("water", p["water_change_ha"])
    s["verdict_green"] = verdict("green", p["green_change_ha"])
    summ.append(s)
    print(p["name"], s["verdict_water"], "|", s["verdict_green"], file=sys.stderr)

json.dump({"note": f"DRAFT multi-date check: tile 43PGQ, orbit R{CFG['robustness_orbit']:03d}, every Jan-Mar 2019/2025/2026 acquisition; a date counts for a lake only if >= {MINV}% of its pixels are unmasked. Not the headline numbers.",
           "lakes": summ, "dates": res}, open(HERE / "data/robustness_lakes.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
cols = [k for k in summ[0] if k != "series"]
with open(HERE / "robustness_lakes.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    w.writerows(summ)
