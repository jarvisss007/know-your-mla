"""Step 2: compute land-cover proxies for two Sentinel-2 L2A scenes inside the
Mahadevapura (AC 174) boundary, per-lake water area from OSM, and write
metrics.json + PNGs. Uses only free, no-account endpoints."""
import json, sys, datetime as dt
from pathlib import Path
import numpy as np
import requests
import rasterio
from rasterio.vrt import WarpedVRT
from rasterio.enums import Resampling
from rasterio.features import geometry_mask
from rasterio.transform import from_origin
from pyproj import Transformer
from shapely.geometry import shape, mapping, Polygon, MultiPolygon, LineString
from shapely.ops import transform as shp_transform, polygonize, unary_union
import pystac_client
import planetary_computer
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
STAC = "https://planetarycomputer.microsoft.com/api/stac/v1"
BOUNDARY = HERE / "data/boundary/mahadevapura_ac174.geojson"
DST_CRS = "EPSG:32643"  # UTM 43N, native CRS of tile 43PGQ
RES = 10.0
SCENES = {  # chosen from data/candidates.json: same orbit R019, same tile, ~same day-of-year
    "2019": "S2A_MSIL2A_20190213T050921_R019_T43PGQ_20201007T162011",
    "2026": "S2B_MSIL2A_20260211T050839_R019_T43PGQ_20260211T085923",
}
BAD_SCL = [0, 1, 3, 8, 9, 10]
SCL_NAMES = {0: "no data", 1: "saturated/defective", 2: "dark area", 3: "cloud shadow",
             4: "vegetation", 5: "not vegetated", 6: "water", 7: "unclassified",
             8: "cloud medium prob", 9: "cloud high prob", 10: "thin cirrus", 11: "snow"}
T_NDVI_VEG, T_WATER, T_NDBI, T_NDVI_BUILT = 0.4, 0.0, 0.0, 0.2
PIX_HA = RES * RES / 10000.0
BOUNDARY_FLAGS = {  # lakes whose inclusion looks doubtful against the DataMeet polygon; verify before use
    "Hosakote lake": "OSM name suggests Hoskote (Bengaluru Rural district, outside the city); its presence inside the polygon may reflect the DataMeet boundary shift. Verify against the official ECI/CEO Karnataka map before citing.",
    "Bellandur Lake": "Lake straddles the polygon edge; only the part inside the DataMeet polygon is counted.",
    "Yellamallappa Chetty Lake": "Near the K.R. Puram / Mahadevapura edge; inclusion depends on the approximate DataMeet boundary.",
}

poly_ll = shape(json.load(open(BOUNDARY))["features"][0]["geometry"])
to_utm = Transformer.from_crs("EPSG:4326", DST_CRS, always_xy=True).transform
poly_utm = shp_transform(to_utm, poly_ll)
minx, miny, maxx, maxy = poly_utm.bounds
pad = 200
minx = np.floor((minx - pad) / 20) * 20; maxy = np.ceil((maxy + pad) / 20) * 20
maxx = np.ceil((maxx + pad) / 20) * 20; miny = np.floor((miny - pad) / 20) * 20
W = int(round((maxx - minx) / RES)); H = int(round((maxy - miny) / RES))
TR = from_origin(minx, maxy, RES, RES)
INSIDE = geometry_mask([mapping(poly_utm)], (H, W), TR, invert=True)
POLY_HA = poly_utm.area / 10000.0
print("grid", W, H, "polygon ha", round(POLY_HA, 1), "pixels inside", int(INSIDE.sum()), file=sys.stderr)

cat = pystac_client.Client.open(STAC, modifier=planetary_computer.sign_inplace)


def read(href, resampling):
    with rasterio.open(href) as src:
        with WarpedVRT(src, crs=DST_CRS, transform=TR, width=W, height=H,
                       resampling=resampling, nodata=0) as v:
            return v.read(1)


def load(item_id):
    it = next(cat.search(collections=["sentinel-2-l2a"], ids=[item_id]).items())
    bl = float(it.properties.get("s2:processing_baseline", "0"))
    offset = -1000 if bl >= 4.0 else 0  # ESA added BOA_ADD_OFFSET=-1000 from baseline 04.00 (Jan 2022)
    bands = {}
    for b in ["B02", "B03", "B04", "B08", "B11"]:
        dn = read(it.assets[b].href, Resampling.bilinear if b == "B11" else Resampling.nearest).astype("float32")
        refl = (dn + offset) / 10000.0
        refl[dn == 0] = np.nan
        bands[b] = refl
    scl = read(it.assets["SCL"].href, Resampling.nearest)
    meta = {"id": it.id, "datetime": it.properties["datetime"],
            "platform": it.properties.get("platform"),
            "mgrs_tile": it.properties.get("s2:mgrs_tile"),
            "relative_orbit": it.properties.get("sat:relative_orbit"),
            "processing_baseline": it.properties.get("s2:processing_baseline"),
            "tile_cloud_cover_pct": it.properties.get("eo:cloud_cover"),
            "reflectance_offset_applied": offset,
            "stac_item_url": f"{STAC}/collections/sentinel-2-l2a/items/{it.id}"}
    return bands, scl, meta


def nd(a, b):
    with np.errstate(divide="ignore", invalid="ignore"):
        return (a - b) / (a + b)


def classify(bands, scl):
    ndvi = nd(bands["B08"], bands["B04"])
    mndwi = nd(bands["B03"], bands["B11"])
    ndwi = nd(bands["B03"], bands["B08"])
    ndbi = nd(bands["B11"], bands["B08"])
    valid = ~np.isin(scl, BAD_SCL) & np.isfinite(ndvi) & np.isfinite(mndwi) & np.isfinite(ndbi)
    veg = valid & (ndvi > T_NDVI_VEG)
    water = valid & (mndwi > T_WATER)
    water_ndwi = valid & (ndwi > T_WATER)
    built = valid & (ndbi > T_NDBI) & (ndvi < T_NDVI_BUILT) & ~water
    return dict(valid=valid, veg=veg, water=water, water_ndwi=water_ndwi, built=built,
                ndvi=ndvi, mndwi=mndwi)


def ha(mask, region=INSIDE):
    return round(float((mask & region).sum()) * PIX_HA, 1)


data = {}
for yr, sid in SCENES.items():
    print("loading", yr, sid, file=sys.stderr)
    bands, scl, meta = load(sid)
    c = classify(bands, scl)
    inside_scl = scl[INSIDE]
    meta["scl_class_pct_inside_boundary"] = {SCL_NAMES[k]: round(float((inside_scl == k).mean() * 100), 3)
                                             for k in range(12) if (inside_scl == k).any()}
    meta["masked_pct_inside_boundary"] = round(float((~c["valid"][INSIDE]).mean() * 100), 3)
    # sanity: median reflectance of SCL water pixels (should be low, ~0.02-0.08 in B08)
    w = (scl == 6) & INSIDE
    meta["sanity_median_B08_on_SCL_water"] = round(float(np.nanmedian(bands["B08"][w])), 4) if w.any() else None
    meta["sanity_median_B04_inside"] = round(float(np.nanmedian(bands["B04"][INSIDE])), 4)
    data[yr] = dict(bands=bands, scl=scl, meta=meta, cls=c)

a, b = data["2019"]["cls"], data["2026"]["cls"]
both = a["valid"] & b["valid"] & INSIDE


def summary(c, region):
    n = float(region.sum()) * PIX_HA
    out = {}
    for k, lab in [("veg", "vegetation_ndvi_gt_0.4"), ("water", "open_water_mndwi_gt_0"),
                   ("water_ndwi", "open_water_ndwi_mcfeeters_gt_0_secondary"),
                   ("built", "builtup_bare_proxy")]:
        h = ha(c[k], region)
        out[lab] = {"ha": h, "pct": round(h / n * 100, 2)}
    return out


metrics_by_year = {yr: summary(data[yr]["cls"], both) for yr in SCENES}
change = {}
for lab in metrics_by_year["2019"]:
    h0, h1 = metrics_by_year["2019"][lab]["ha"], metrics_by_year["2026"][lab]["ha"]
    change[lab] = {"ha_change": round(h1 - h0, 1),
                   "pct_point_change": round(metrics_by_year["2026"][lab]["pct"] - metrics_by_year["2019"][lab]["pct"], 2),
                   "relative_change_pct": round((h1 - h0) / h0 * 100, 1) if h0 else None}
veg_lost = a["veg"] & ~b["veg"] & both
veg_gain = ~a["veg"] & b["veg"] & both
water_lost = a["water"] & ~b["water"] & both
water_gain = ~a["water"] & b["water"] & both
built_new = ~a["built"] & b["built"] & both
built_gone = a["built"] & ~b["built"] & both
gross = {"vegetation_lost_ha": ha(veg_lost), "vegetation_gained_ha": ha(veg_gain),
         "water_lost_ha": ha(water_lost), "water_gained_ha": ha(water_gain),
         "builtup_proxy_new_ha": ha(built_new), "builtup_proxy_no_longer_ha": ha(built_gone),
         "of_new_builtup_proxy_was_vegetation_2019_ha": ha(built_new & a["veg"])}

# ---------------- lakes from OSM ----------------
lakes_out, lake_note = [], ""
try:
    coords = list(poly_ll.exterior.coords)
    polystr = " ".join(f"{lat:.6f} {lon:.6f}" for lon, lat in coords)
    q = f'[out:json][timeout:90];(way["natural"="water"]["name"](poly:"{polystr}");relation["natural"="water"]["name"](poly:"{polystr}"););out geom;'
    cache = HERE / "data/osm_named_water.json"
    if cache.exists():  # reuse the saved Overpass response (first queried 2026-11-16 21:18 UTC from overpass-api.de)
        els = json.load(open(cache))
        lake_note = "Overpass endpoint https://overpass-api.de/api/interpreter, queried 2026-11-16T21:18:25Z; response cached in data/osm_named_water.json and reused."
    else:
        els = None
        for ep in ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter"]:
            try:
                r = requests.post(ep, data={"data": q}, timeout=180,
                                  headers={"User-Agent": "open-data-landcover-study/0.1"})
                if r.ok:
                    els = r.json()["elements"]
                    lake_note = f"Overpass endpoint: {ep}; queried {dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}"
                    break
                lake_note += f"{ep} HTTP {r.status_code}; "
            except Exception as e:
                lake_note += f"{ep} failed: {e!r}; "
        if els is None:
            raise RuntimeError("all Overpass endpoints failed")
        (HERE / "data").mkdir(exist_ok=True)
        json.dump(els, open(cache, "w"))
    feats = {}
    for e in els:
        name = e.get("tags", {}).get("name")
        geom = None
        if e["type"] == "way" and len(e.get("geometry", [])) >= 4:
            pts = [(p["lon"], p["lat"]) for p in e["geometry"]]
            if pts[0] == pts[-1]:
                geom = Polygon(pts)
        elif e["type"] == "relation":
            outers = [LineString([(p["lon"], p["lat"]) for p in m["geometry"]]) for m in e.get("members", [])
                      if m.get("role") == "outer" and m.get("geometry")]
            inners = [LineString([(p["lon"], p["lat"]) for p in m["geometry"]]) for m in e.get("members", [])
                      if m.get("role") == "inner" and m.get("geometry")]
            po = unary_union(list(polygonize(unary_union(outers)))) if outers else None
            if po is not None and not po.is_empty:
                if inners:
                    pi = unary_union(list(polygonize(unary_union(inners))))
                    po = po.difference(pi)
                geom = po
        if geom is None or geom.is_empty:
            continue
        geom = geom.buffer(0)
        key = name.strip()
        feats.setdefault(key, []).append((f"{e['type']}/{e['id']}", geom, e.get("tags", {})))
    for name, parts in sorted(feats.items()):
        g_ll = unary_union([p[1] for p in parts]).intersection(poly_ll)
        if g_ll.is_empty:
            continue
        g_utm = shp_transform(to_utm, g_ll)
        m = geometry_mask([mapping(g_utm)], (H, W), TR, invert=True, all_touched=False)
        lake = {"name": name, "osm_ids": [p[0] for p in parts],
                "water_tag": sorted({p[2].get("water", "") for p in parts} - {""}),
                "osm_polygon_ha_inside_boundary": round(g_utm.area / 10000, 2),
                "osm_polygon_ha_total": round(shp_transform(to_utm, unary_union([p[1] for p in parts])).area / 10000, 2),
                "pixels": int(m.sum())}
        if name in BOUNDARY_FLAGS:
            lake["boundary_flag"] = BOUNDARY_FLAGS[name]
        if g_utm.area >= 20000:  # >= 2 ha: enough 10 m pixels to say something
            for yr in SCENES:
                c = data[yr]["cls"]
                vm = c["valid"] & m
                lake[f"water_ha_{yr}"] = ha(c["water"], m)
                lake[f"vegetation_ha_{yr}"] = ha(c["veg"], m)
                lake[f"valid_pct_{yr}"] = round(float(vm.sum() / max(m.sum(), 1) * 100), 1)
            lake["water_ha_change"] = round(lake["water_ha_2026"] - lake["water_ha_2019"], 2)
        else:
            lake["note"] = "under 2 ha mapped area; too few 10 m pixels for a meaningful water estimate"
        lakes_out.append(lake)
    lakes_out.sort(key=lambda d: -d["osm_polygon_ha_inside_boundary"])
except Exception as e:
    lake_note += f" LAKE STEP FAILED: {e!r}"
    print("lake step failed", e, file=sys.stderr)

# ---------------- images ----------------
def truecolor(bands):
    rgb = np.dstack([bands["B04"], bands["B03"], bands["B02"]])
    rgb = np.clip(rgb / 0.30, 0, 1) ** (1 / 1.4)  # fixed stretch, same for both years
    rgb = np.nan_to_num(rgb)
    return (rgb * 255).astype("uint8")


ring_px = [(~TR * (x, y)) for x, y in poly_utm.exterior.coords]


def draw_boundary(img, scale, color, width=3):
    d = ImageDraw.Draw(img)
    d.line([(x * scale, y * scale) for x, y in ring_px], fill=color, width=width, joint="curve")


def font(sz):
    for f in ["arialbd.ttf", "arial.ttf", "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(f, sz)
        except Exception:
            pass
    return ImageFont.load_default()


# side-by-side true colour: each panel 590 px wide
panel_w = 590
scale = panel_w / W
panel_h = int(round(H * scale))
head = 56
foot = 34
canvas = Image.new("RGB", (panel_w * 2 + 20, panel_h + head + foot), (18, 18, 20))
d = ImageDraw.Draw(canvas)
for i, yr in enumerate(["2019", "2026"]):
    im = Image.fromarray(truecolor(data[yr]["bands"])).resize((panel_w, panel_h), Image.LANCZOS)
    draw_boundary(im, scale, (255, 220, 0), 2)
    x0 = i * (panel_w + 20)
    canvas.paste(im, (x0, head))
    day = data[yr]["meta"]["datetime"][:10]
    d.text((x0 + 4, 6), f"{yr}: Sentinel-2 true colour, {day}", fill=(240, 240, 240), font=font(20))
    d.text((x0 + 4, 32), f"tile {data[yr]['meta']['mgrs_tile']}, masked {data[yr]['meta']['masked_pct_inside_boundary']}% inside boundary",
           fill=(170, 170, 170), font=font(14))
d.text((4, head + panel_h + 8), "Yellow line: Mahadevapura AC 174 boundary (DataMeet, 2008 delimitation). Contains modified Copernicus Sentinel data.",
       fill=(170, 170, 170), font=font(13))
canvas.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG).save(HERE / "truecolor_2019_2026.png", optimize=True)

# change map at up to 1100 px wide; class colours drawn from full-res masks with max-pooling so small patches survive
target_w = min(1100, W)
s = target_w / W
th = int(round(H * s))
base = truecolor(data["2026"]["bands"]).mean(axis=2)
base = (base * 0.45).astype("uint8")
rgb = np.dstack([base] * 3)
layers = [(built_new, (230, 40, 40)), (veg_lost, (40, 210, 70)), (water_lost, (40, 120, 255))]
for m, col in layers:  # later layers drawn on top: water lost > veg lost > new built-up
    rgb[m] = col
rgb[~INSIDE] = (rgb[~INSIDE] * 0.5).astype("uint8")
im = Image.fromarray(rgb)
if s < 1:
    im = im.resize((target_w, th), Image.NEAREST)
draw_boundary(im, s, (255, 220, 0), 2)
legend_h = 120
cm = Image.new("RGB", (target_w, th + legend_h), (18, 18, 20))
cm.paste(im, (0, legend_h))
d = ImageDraw.Draw(cm)
d.text((8, 6), "Mahadevapura (AC 174): change between 13 Feb 2019 and 11 Feb 2026 (Sentinel-2, 10 m)",
       fill=(240, 240, 240), font=font(18))
items = [((40, 210, 70), f"vegetation lost (NDVI>0.4 -> not): {gross['vegetation_lost_ha']} ha"),
         ((40, 120, 255), f"water lost (MNDWI>0 -> not): {gross['water_lost_ha']} ha"),
         ((230, 40, 40), f"new built-up/bare PROXY (NDBI>0, NDVI<0.2): {gross['builtup_proxy_new_ha']} ha")]
for i, (col, txt) in enumerate(items):
    y = 36 + i * 24
    d.rectangle([10, y, 28, y + 16], fill=col)
    d.text((36, y), txt, fill=(225, 225, 225), font=font(15))
d.text((8, 36 + 3 * 24), "Grey = 2026 image, dimmed. Yellow = boundary. Single-scene comparison; see METHOD.md for limits.",
       fill=(160, 160, 160), font=font(13))
cm.quantize(colors=128, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(HERE / "change_map_2019_2026.png", optimize=True)

# ---------------- metrics.json ----------------
out = {
    "title": "Mahadevapura (Karnataka AC 174) Sentinel-2 land-cover change, dry season 2019 vs 2026",
    "generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    "status": "DRAFT - first-pass, unreviewed. Proxies from two single scenes, not a land-use survey.",
    "boundary": {
        "source": "DataMeet maps repo, docs/data/geojson/ac.geojson (Assembly Constituencies scraped from ECI polling-station site psleci.nic.in)",
        "url": "https://github.com/datameet/maps/blob/master/docs/data/geojson/ac.geojson",
        "license": "CC BY 2.5 India (DataMeet)",
        "feature_properties": json.load(open(BOUNDARY))["features"][0]["properties"],
        "delimitation": "2008 (Delimitation of Parliamentary and Assembly Constituencies Order, 2008; Karnataka first used it in the 2008 election). Inferred: the feature sits in PC 25 'Bangalore Central', a seat created by the 2008 delimitation; the STATUS field is empty (DataMeet marks only pre-delimitation states).",
        "known_issues": "DataMeet README: 'There is some shift in the data'. Polygon is coarse (73 vertices). Treat edges as approximate to tens of metres.",
        "area_ha_utm43n": round(POLY_HA, 1),
        "rejected_alternative": "DataMeet eci/AC_Data/States/S10 shapefile: coordinates not georeferenced (bbox around -12,1), unusable.",
    },
    "imagery": {
        "collection": "sentinel-2-l2a (Microsoft Planetary Computer STAC, anonymous SAS-signed asset URLs)",
        "stac_api": STAC,
        "selection": "All Jan-Mar scenes with tile cloud <20% were scored by SCL cloud/shadow fraction inside the boundary (data/candidates.json). Chose one scene per year from the same tile (43PGQ) and relative orbit (R019) with near-identical day of year (13 Feb vs 11 Feb) to minimise seasonal and viewing-geometry differences; both have <0.3% masked pixels inside the boundary. 2026 dry season had clean scenes, so no 2025 fallback was needed.",
        "scenes": {yr: data[yr]["meta"] for yr in SCENES},
    },
    "method": {
        "grid": f"{DST_CRS}, {RES} m pixels; 10 m bands nearest-neighbour, B11 (20 m) bilinear-resampled to 10 m, SCL (20 m) nearest",
        "reflectance": "L2A DN/10000 after adding BOA_ADD_OFFSET (-1000 for processing baseline >= 04.00, i.e. the 2026 scene; 0 for the 2019 reprocessed baseline 02.12 scene)",
        "cloud_mask": f"SCL classes excluded: {[SCL_NAMES[k] for k in BAD_SCL]}. Areas are counted only on pixels valid in BOTH scenes inside the boundary.",
        "thresholds": {
            "vegetation": "NDVI = (B08-B04)/(B08+B04) > 0.4",
            "open_water_headline": "MNDWI = (B03-B11)/(B03+B11) > 0  (Xu 2006, modified NDWI using SWIR)",
            "open_water_secondary": "NDWI = (B03-B08)/(B03+B08) > 0  (McFeeters 1996), reported for comparison only",
            "builtup_bare_proxy": "NDBI = (B11-B08)/(B11+B08) > 0 AND NDVI < 0.2 AND not MNDWI water. A PROXY: also catches bare soil, dry fields, cleared plots, quarries, rock",
        },
        "pixel_area_ha": PIX_HA,
        "comparison_area_ha": round(float(both.sum()) * PIX_HA, 1),
        "comparison_area_pct_of_boundary": round(float(both.sum() / INSIDE.sum() * 100), 2),
        "note_categories": "Categories are independent thresholds; a pixel can be in none of them (e.g. NDVI 0.2-0.4 sparse vegetation/mixed pixels). They do not sum to 100%.",
    },
    "results_inside_boundary": {
        "by_year": metrics_by_year,
        "net_change_2019_to_2026": change,
        "gross_pixel_transitions": gross,
    },
    "lakes_osm": {
        "query": "Overpass API: way/relation natural=water with a name tag, inside the boundary polygon",
        "note": lake_note + " Water ha = pixels with MNDWI>0 inside the OSM outline (clipped to the boundary). Lakes covered by weeds (e.g. water hyacinth) count as vegetation, not water. OSM outlines are volunteer-drawn and current-day.",
        "lakes": lakes_out,
    },
    "outputs": ["metrics.json", "truecolor_2019_2026.png", "change_map_2019_2026.png", "METHOD.md",
                "search_scenes.py", "analyze.py", "data/candidates.json", "data/osm_named_water.json",
                "data/boundary/mahadevapura_ac174.geojson"],
}
json.dump(out, open(HERE / "metrics.json", "w"), indent=2)
print(json.dumps(out["results_inside_boundary"], indent=1))
print(json.dumps({yr: data[yr]["meta"] for yr in SCENES}, indent=1))
print(len(lakes_out), "lakes")
