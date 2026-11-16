"""DRAFT. Step 3: land-cover proxies for two Sentinel-2 L2A dates inside one Assembly
Constituency boundary, adapted from ../analyze.py (Mahadevapura AC 174).

Differences from the original:
  * every constituency-specific value (name, number, boundary, scene IDs, titles) comes
    from config.json;
  * each year can be a MOSAIC of several same-date, same-orbit tiles (first tile wins
    where they overlap; ESA reflectance offset decided per tile from its own baseline);
  * vegetation is also reported inside vs outside OSM protected-area / forest polygons;
  * OSM water polygons are used named or unnamed (unnamed labelled by OSM id + centroid);
  * connected clusters of new bare/built-up PROXY pixels are listed (area, centroid);
  * change-map classes are block-aggregated (not nearest-sampled) when downsized.
Inputs it needs first: extract_boundary.py, search_scenes.py (to pick scenes),
fetch_osm.py (cached Overpass responses). Free, no-account endpoints only."""
import json, sys, datetime as dt
from pathlib import Path
import numpy as np
import rasterio
from rasterio.vrt import WarpedVRT
from rasterio.enums import Resampling
from rasterio.features import geometry_mask
from rasterio.transform import from_origin
from pyproj import Transformer
from shapely.geometry import shape, mapping, Polygon, LineString
from shapely.ops import transform as shp_transform, polygonize, unary_union
from scipy import ndimage
import pystac_client
import planetary_computer
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
CFG = json.load(open(HERE / "config.json"))
NAME = CFG["display_name"]
STAC = "https://planetarycomputer.microsoft.com/api/stac/v1"
BOUNDARY = HERE / CFG["boundary"]
DST_CRS = CFG["dst_crs"]
RES = float(CFG["res_m"])
SCENES = CFG["scenes"]  # {"2019": [item ids...], "2026": [...]}
Y0, Y1 = sorted(SCENES)
BAD_SCL = [0, 1, 3, 8, 9, 10]
SCL_NAMES = {0: "no data", 1: "saturated/defective", 2: "dark area", 3: "cloud shadow",
             4: "vegetation", 5: "not vegetated", 6: "water", 7: "unclassified",
             8: "cloud medium prob", 9: "cloud high prob", 10: "thin cirrus", 11: "snow"}
T_NDVI_VEG, T_WATER, T_NDBI, T_NDVI_BUILT = 0.4, 0.0, 0.0, 0.2
PIX_HA = RES * RES / 10000.0
DARK = (18, 18, 20)

poly_ll = shape(json.load(open(BOUNDARY))["features"][0]["geometry"])
to_utm = Transformer.from_crs("EPSG:4326", DST_CRS, always_xy=True).transform
to_ll = Transformer.from_crs(DST_CRS, "EPSG:4326", always_xy=True).transform
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


def load(item_ids):
    """Mosaic same-date tiles. Returns reflectance bands (float32, NaN = no data), SCL, meta."""
    items = [next(cat.search(collections=["sentinel-2-l2a"], ids=[i]).items()) for i in item_ids]
    bands = {b: np.full((H, W), np.nan, "float32") for b in ["B02", "B03", "B04", "B08", "B11", "B12"]}
    scl = np.zeros((H, W), "uint8")
    tiles = []
    for it in items:
        bl = float(it.properties.get("s2:processing_baseline", "0"))
        offset = -1000 if bl >= 4.0 else 0  # ESA BOA_ADD_OFFSET=-1000 from baseline 04.00 (Jan 2022)
        s = read(it.assets["SCL"].href, Resampling.nearest)
        take = (scl == 0) & (s != 0)  # first tile wins in the overlap
        scl[take] = s[take]
        for b in bands:
            dn = read(it.assets[b].href, Resampling.bilinear if b in ("B11", "B12") else Resampling.nearest)
            fill = take & (dn != 0)
            bands[b][fill] = (dn[fill].astype("float32") + offset) / 10000.0
            del dn
        tiles.append({"id": it.id, "mgrs_tile": it.properties.get("s2:mgrs_tile"),
                      "processing_baseline": it.properties.get("s2:processing_baseline"),
                      "tile_cloud_cover_pct": it.properties.get("eo:cloud_cover"),
                      "reflectance_offset_applied": offset,
                      "pixels_supplied_inside_boundary": int((take & INSIDE).sum()),
                      "stac_item_url": f"{STAC}/collections/sentinel-2-l2a/items/{it.id}"})
        print("  tile", it.id, "pixels inside", tiles[-1]["pixels_supplied_inside_boundary"], file=sys.stderr)
    p = items[0].properties
    meta = {"datetime": p["datetime"], "platform": p.get("platform"),
            "relative_orbit": p.get("sat:relative_orbit"), "tiles": tiles}
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
    return dict(valid=valid, veg=veg, water=water, water_ndwi=water_ndwi, built=built)


def truecolor(bands):
    rgb = np.dstack([bands["B04"], bands["B03"], bands["B02"]])
    rgb = np.clip(rgb / 0.30, 0, 1) ** (1 / 1.4)  # fixed stretch, same for both years
    rgb = np.nan_to_num(rgb)
    return (rgb * 255).astype("uint8")


def ha(mask, region=INSIDE):
    return round(float((mask & region).sum()) * PIX_HA, 1)


data = {}
for yr, ids in SCENES.items():
    print("loading", yr, ids, file=sys.stderr)
    bands, scl, meta = load(ids)
    c = classify(bands, scl)
    inside_scl = scl[INSIDE]
    meta["scl_class_pct_inside_boundary"] = {SCL_NAMES[k]: round(float((inside_scl == k).mean() * 100), 3)
                                             for k in range(12) if (inside_scl == k).any()}
    meta["masked_pct_inside_boundary"] = round(float((~c["valid"][INSIDE]).mean() * 100), 3)
    w = (scl == 6) & INSIDE
    meta["sanity_median_B08_on_SCL_water"] = round(float(np.nanmedian(bands["B08"][w])), 4) if w.any() else None
    meta["sanity_median_B04_inside"] = round(float(np.nanmedian(bands["B04"][INSIDE])), 4)
    nbr = nd(bands["B08"], bands["B12"]).astype("float16")  # Normalised Burn Ratio, only used to describe clusters
    data[yr] = dict(tc=truecolor(bands), meta=meta, cls=c, nbr=nbr)
    del bands, scl

a, b = data[Y0]["cls"], data[Y1]["cls"]
both = a["valid"] & b["valid"] & INSIDE
LABELS = [("veg", "vegetation_ndvi_gt_0.4"), ("water", "open_water_mndwi_gt_0"),
          ("water_ndwi", "open_water_ndwi_mcfeeters_gt_0_secondary"), ("built", "builtup_bare_proxy")]


def summary(c, region):
    n = float(region.sum()) * PIX_HA
    return {lab: {"ha": ha(c[k], region), "pct": round(ha(c[k], region) / n * 100, 2) if n else None}
            for k, lab in LABELS}


def net(m0, m1):
    out = {}
    for lab in m0:
        h0, h1 = m0[lab]["ha"], m1[lab]["ha"]
        out[lab] = {"ha_change": round(h1 - h0, 1),
                    "pct_point_change": round(m1[lab]["pct"] - m0[lab]["pct"], 2) if m0[lab]["pct"] is not None else None,
                    "relative_change_pct": round((h1 - h0) / h0 * 100, 1) if h0 else None}
    return out


metrics_by_year = {yr: summary(data[yr]["cls"], both) for yr in SCENES}
change = net(metrics_by_year[Y0], metrics_by_year[Y1])
veg_lost = a["veg"] & ~b["veg"] & both
veg_gain = ~a["veg"] & b["veg"] & both
water_lost = a["water"] & ~b["water"] & both
water_gain = ~a["water"] & b["water"] & both
built_new = ~a["built"] & b["built"] & both
built_gone = a["built"] & ~b["built"] & both
gross = {"vegetation_lost_ha": ha(veg_lost), "vegetation_gained_ha": ha(veg_gain),
         "water_lost_ha": ha(water_lost), "water_gained_ha": ha(water_gain),
         "builtup_proxy_new_ha": ha(built_new), "builtup_proxy_no_longer_ha": ha(built_gone),
         f"of_new_builtup_proxy_was_vegetation_{Y0}_ha": ha(built_new & a["veg"])}


# ---------------- OSM geometry helpers ----------------
def osm_geom(e):
    if e["type"] == "way" and len(e.get("geometry", [])) >= 4:
        pts = [(p["lon"], p["lat"]) for p in e["geometry"]]
        if pts[0] == pts[-1]:
            return Polygon(pts).buffer(0)
    elif e["type"] == "relation":
        mem = lambda role: [LineString([(p["lon"], p["lat"]) for p in m["geometry"]]) for m in e.get("members", [])
                            if m.get("role") == role and m.get("geometry") and len(m["geometry"]) >= 2]
        outers, inners = mem("outer"), mem("inner")
        po = unary_union(list(polygonize(unary_union(outers)))) if outers else None
        if po is not None and not po.is_empty:
            if inners:
                po = po.difference(unary_union(list(polygonize(unary_union(inners)))))
            return po.buffer(0)
    return None


def raster(g_ll):
    g = shp_transform(to_utm, g_ll)
    if g.is_empty:
        return np.zeros((H, W), bool)
    return geometry_mask([mapping(g)], (H, W), TR, invert=True)


osm_log = json.load(open(HERE / "data/osm_query_log.json")) if (HERE / "data/osm_query_log.json").exists() else {}

# ---------------- vegetation inside vs outside OSM protected / forest ----------------
forest_out = {}
try:
    els = json.load(open(HERE / "data/osm_forest_protected.json"))
    prot, forest, listed = [], [], []
    for e in els:
        t = e.get("tags", {})
        g = osm_geom(e)
        if g is None or g.is_empty:
            continue
        gi = g.intersection(poly_ll)
        is_prot = t.get("boundary") in ("protected_area", "national_park") or t.get("leisure") == "nature_reserve"
        is_forest = t.get("landuse") == "forest"
        if is_prot:
            prot.append(gi)
        if is_forest:
            forest.append(gi)
        listed.append({"osm": f"{e['type']}/{e['id']}", "name": t.get("name"),
                       "tags": {k: t[k] for k in ("boundary", "leisure", "landuse", "natural", "protect_class", "protection_title") if k in t},
                       "ha_inside_boundary": round(shp_transform(to_utm, gi).area / 1e4, 1) if not gi.is_empty else 0.0})
    prot_u, forest_u = unary_union(prot) if prot else Polygon(), unary_union(forest) if forest else Polygon()
    M_prot, M_forest = raster(prot_u) & INSIDE, raster(forest_u) & INSIDE
    M_union = M_prot | M_forest
    regions = {"osm_protected_area": M_prot, "osm_landuse_forest": M_forest,
               "protected_or_forest_union": M_union, "outside_protected_and_forest": INSIDE & ~M_union}
    forest_out = {"source": "OpenStreetMap via Overpass: boundary=protected_area|national_park, leisure=nature_reserve, landuse=forest; "
                            + json.dumps(osm_log.get("osm_forest_protected.json", {}).get("endpoint")) + " queried "
                            + json.dumps(osm_log.get("osm_forest_protected.json", {}).get("queried_utc")),
                  "features": sorted(listed, key=lambda d: -d["ha_inside_boundary"]), "regions": {}}
    for rn, m in regions.items():
        rb = m & both
        m0, m1 = summary(data[Y0]["cls"], rb), summary(data[Y1]["cls"], rb)
        forest_out["regions"][rn] = {
            "area_ha_inside_boundary": round(float(m.sum()) * PIX_HA, 1),
            "compared_ha": round(float(rb.sum()) * PIX_HA, 1),
            "by_year": {Y0: m0, Y1: m1}, "net_change": net(m0, m1),
            "vegetation_lost_ha": ha(veg_lost, rb), "vegetation_gained_ha": ha(veg_gain, rb),
            "builtup_proxy_new_ha": ha(built_new, rb)}
except Exception as e:
    forest_out = {"error": f"FOREST/PROTECTED STEP FAILED: {e!r}"}
    M_union = np.zeros((H, W), bool)
    print("forest step failed", e, file=sys.stderr)

# ---------------- water bodies from OSM ----------------
lakes_out, lake_note = [], ""
try:
    els = json.load(open(HERE / "data/osm_water_all.json"))
    lg = osm_log.get("osm_water_all.json", {})
    lake_note = f"Overpass endpoint {lg.get('endpoint')}, queried {lg.get('queried_utc')}; response cached in data/osm_water_all.json and reused."
    feats = {}
    for e in els:
        t = e.get("tags", {})
        g = osm_geom(e)
        if g is None or g.is_empty:
            continue
        name = (t.get("name") or t.get("name:en") or "").strip()
        named = bool(name or t.get("name:kn"))
        key = name or (f"{t['name:kn']} (name:kn only)" if t.get("name:kn") else f"unnamed {e['type']}/{e['id']}")
        feats.setdefault(key, []).append((f"{e['type']}/{e['id']}", g, t, named))
    for name, parts in feats.items():
        g_all = unary_union([p[1] for p in parts])
        g_ll = g_all.intersection(poly_ll)
        if g_ll.is_empty:
            continue
        g_utm = shp_transform(to_utm, g_ll)
        cen = g_ll.representative_point()
        m = raster(g_ll)
        lake = {"name": name, "named_in_osm": parts[0][3], "osm_ids": [p[0] for p in parts],
                "water_tag": sorted({p[2].get("water", "") or p[2].get("landuse", "") for p in parts} - {""}),
                "name_kn": sorted({p[2]["name:kn"] for p in parts if p[2].get("name:kn")}),
                "point_lat": round(cen.y, 5), "point_lon": round(cen.x, 5),
                "osm_polygon_ha_inside_boundary": round(g_utm.area / 10000, 2),
                "osm_polygon_ha_total": round(shp_transform(to_utm, g_all).area / 10000, 2),
                "pixels": int(m.sum())}
        if g_utm.area >= CFG["min_lake_ha"] * 10000:
            for yr in SCENES:
                c = data[yr]["cls"]
                lake[f"water_ha_{yr}"] = ha(c["water"], m)
                lake[f"vegetation_ha_{yr}"] = ha(c["veg"], m)
                lake[f"valid_pct_{yr}"] = round(float((c["valid"] & m).sum() / max(m.sum(), 1) * 100), 1)
            lake["water_ha_change"] = round(lake[f"water_ha_{Y1}"] - lake[f"water_ha_{Y0}"], 2)
        else:
            lake["note"] = f"under {CFG['min_lake_ha']} ha mapped area; too few pixels for a meaningful water estimate"
        lakes_out.append(lake)
    lakes_out.sort(key=lambda d: -d["osm_polygon_ha_inside_boundary"])
except Exception as e:
    lake_note += f" LAKE STEP FAILED: {e!r}"
    print("lake step failed", e, file=sys.stderr)

# ---------------- clusters of new bare / built-up PROXY ground ----------------
# pixels NOT built/bare proxy in Y0 (i.e. vegetation or other non-bare cover) and built/bare proxy in Y1
cand = built_new  # = ~a.built & b.built & both
lab, n = ndimage.label(cand, structure=[[0, 1, 0], [1, 1, 1], [0, 1, 0]])  # 4-connectivity limits chaining through field speckle
counts = np.bincount(lab.ravel())
counts[0] = 0
order = np.argsort(-counts)[:CFG["n_clusters"]]
rows, cols = np.nonzero(lab)
lv = lab[rows, cols]
sel = np.isin(lv, order)
rows, cols, lv = rows[sel], cols[sel], lv[sel]
clusters = []
for rank, k in enumerate(order, 1):
    if counts[k] == 0:
        break
    mk = lv == k
    r, cc = rows[mk], cols[mk]
    x, y = TR * (cc.mean() + 0.5, r.mean() + 0.5)
    lon, lat = to_ll(x, y)
    # nearest member pixel to the mean, so the marker falls on the cluster even if it is crescent-shaped
    j = np.argmin((r - r.mean()) ** 2 + (cc - cc.mean()) ** 2)
    xn, yn = TR * (cc[j] + 0.5, r[j] + 0.5)
    lonn, latn = to_ll(xn, yn)
    x0, y0 = TR * (cc.min(), r.max() + 1); x1, y1 = TR * (cc.max() + 1, r.min())
    (lo0, la0), (lo1, la1) = to_ll(x0, y0), to_ll(x1, y1)
    clusters.append({"rank": rank, "label": "new bare or built-up ground (proxy)",
                     "area_ha": round(float(counts[k]) * PIX_HA, 2),
                     "centroid_lat": round(lat, 5), "centroid_lon": round(lon, 5),
                     "nearest_member_pixel_lat": round(latn, 5), "nearest_member_pixel_lon": round(lonn, 5),
                     "bbox_lonlat": [round(lo0, 5), round(la0, 5), round(lo1, 5), round(la1, 5)],
                     f"pct_was_vegetation_{Y0}": round(float(a["veg"][r, cc].mean() * 100), 1),
                     "pct_inside_osm_protected_or_forest": round(float(M_union[r, cc].mean() * 100), 1),
                     f"median_nbr_{Y0}": round(float(np.nanmedian(data[Y0]["nbr"][r, cc].astype("float32"))), 3),
                     f"median_nbr_{Y1}": round(float(np.nanmedian(data[Y1]["nbr"][r, cc].astype("float32"))), 3),
                     "median_dnbr": round(float(np.nanmedian(data[Y0]["nbr"][r, cc].astype("float32") - data[Y1]["nbr"][r, cc].astype("float32"))), 3),
                     "_px": (float(cc.mean()), float(r.mean()))})
sizes_ha = counts[1:] * PIX_HA
cluster_stats = {"n_regions": int(n), "regions_ge_1ha": int((sizes_ha >= 1).sum()),
                 "regions_ge_5ha": int((sizes_ha >= 5).sum()),
                 "ha_in_regions_ge_1ha": round(float(sizes_ha[sizes_ha >= 1].sum()), 1),
                 "ha_in_regions_lt_1ha": round(float(sizes_ha[sizes_ha < 1].sum()), 1)}
del lab, rows, cols, lv

# ---------------- images ----------------
RINGS_PX = [[(~TR * (x, y)) for x, y in q.exterior.coords] for q in getattr(poly_utm, "geoms", [poly_utm])]  # one ring per part (MultiPolygon-safe)


def draw_boundary(img, scale, color, width=3):
    for ring_px in RINGS_PX:
        ImageDraw.Draw(img).line([(x * scale, y * scale) for x, y in ring_px], fill=color, width=width, joint="curve")


def font(sz):
    for f in ["arialbd.ttf", "arial.ttf", "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(f, sz)
        except Exception:
            pass
    return ImageFont.load_default()


def fmt_day(yr):
    return dt.date.fromisoformat(data[yr]["meta"]["datetime"][:10]).strftime("%d %b %Y").lstrip("0")


tile_str = lambda yr: "+".join(t["mgrs_tile"] for t in data[yr]["meta"]["tiles"])

# side-by-side true colour: each panel 590 px wide
panel_w = 590
scale = panel_w / W
panel_h = int(round(H * scale))
head, foot = 56, 34
canvas = Image.new("RGB", (panel_w * 2 + 20, panel_h + head + foot), DARK)
d = ImageDraw.Draw(canvas)
for i, yr in enumerate([Y0, Y1]):
    im = Image.fromarray(data[yr]["tc"]).resize((panel_w, panel_h), Image.LANCZOS)
    draw_boundary(im, scale, (255, 220, 0), 2)
    x0 = i * (panel_w + 20)
    canvas.paste(im, (x0, head))
    d.text((x0 + 4, 6), f"{yr}: Sentinel-2 true colour, {fmt_day(yr)}", fill=(240, 240, 240), font=font(20))
    d.text((x0 + 4, 32), f"tiles {tile_str(yr)}, masked {data[yr]['meta']['masked_pct_inside_boundary']}% inside boundary",
           fill=(170, 170, 170), font=font(14))
d.text((4, head + panel_h + 8), f"DRAFT. Yellow line: {NAME} boundary (DataMeet, 2008 delimitation). Contains modified Copernicus Sentinel data.",
       fill=(170, 170, 170), font=font(13))
canvas.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG).save(HERE / f"truecolor_{Y0}_{Y1}.png", optimize=True)

# change map: classes aggregated per output block (class drawn if it covers >= 25% of the block)
target_w = min(1100, W)
f = int(np.ceil(W / target_w))
Hb, Wb = int(np.ceil(H / f)), int(np.ceil(W / f))


def block_frac(m):
    p = np.zeros((Hb * f, Wb * f), "float32")
    p[:H, :W] = m
    return p.reshape(Hb, f, Wb, f).mean(axis=(1, 3))


base_img = Image.fromarray(data[Y1]["tc"]).resize((Wb, Hb), Image.LANCZOS)
base = (np.asarray(base_img).mean(axis=2) * 0.45).astype("uint8")
rgb = np.dstack([base] * 3)
ins_b = block_frac(INSIDE) >= 0.5
rgb[~ins_b] = (rgb[~ins_b] * 0.5).astype("uint8")
for m, col in [(built_new, (230, 40, 40)), (veg_lost, (40, 210, 70)), (water_lost, (40, 120, 255))]:
    rgb[(block_frac(m) >= 0.25) & ins_b] = col  # later layers drawn on top: water lost > veg lost > new built-up
im = Image.fromarray(rgb)
draw_boundary(im, 1 / f, (255, 220, 0), 2)
legend_h = 120
cm = Image.new("RGB", (Wb, Hb + legend_h), DARK)
cm.paste(im, (0, legend_h))
d = ImageDraw.Draw(cm)
d.text((8, 6), f"DRAFT. {NAME}: change between {fmt_day(Y0)} and {fmt_day(Y1)} (Sentinel-2, {RES:.0f} m)",
       fill=(240, 240, 240), font=font(18))
items = [((40, 210, 70), f"vegetation lost (NDVI>0.4 -> not): {gross['vegetation_lost_ha']:,} ha"),
         ((40, 120, 255), f"water lost (MNDWI>0 -> not): {gross['water_lost_ha']:,} ha"),
         ((230, 40, 40), f"new bare/built-up PROXY (NDBI>0, NDVI<0.2): {gross['builtup_proxy_new_ha']:,} ha")]
for i, (col, txt) in enumerate(items):
    y = 36 + i * 24
    d.rectangle([10, y, 28, y + 16], fill=col)
    d.text((36, y), txt, fill=(225, 225, 225), font=font(15))
d.text((8, 36 + 3 * 24), f"Grey = {Y1} image, dimmed. Each map pixel = {f}x{f} analysis pixels; colour shown where the class covers >=25%. See METHOD.md.",
       fill=(160, 160, 160), font=font(13))
cm.quantize(colors=128, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(HERE / f"change_map_{Y0}_{Y1}.png", optimize=True)

# clusters: Y1 true colour with new-proxy clusters outlined and numbered
cw = min(1150, W, int(W * 1400 / H))  # also cap height at 1400 px so tall constituencies stay under ~1.5 MB
fc = W / cw
ch = int(round(H / fc))
im = Image.fromarray(data[Y1]["tc"]).resize((cw, ch), Image.LANCZOS)
im = Image.fromarray((np.asarray(im) * 0.8).astype("uint8"))
draw_boundary(im, 1 / fc, (255, 220, 0), 2)
dd = ImageDraw.Draw(im)
for cl in clusters:
    px, py = cl["_px"][0] / fc, cl["_px"][1] / fc
    r = 11
    dd.ellipse([px - r, py - r, px + r, py + r], outline=(255, 60, 200), width=3, fill=(30, 10, 30))
    t = str(cl["rank"])
    tw = dd.textlength(t, font=font(13))
    dd.text((px - tw / 2, py - 8), t, fill=(255, 255, 255), font=font(13))
head = 64
cvw = max(cw, 1150)  # keep the header readable when the map itself is narrow
cv = Image.new("RGB", (cvw, ch + head), DARK)
cv.paste(im, ((cvw - cw) // 2, head))
d = ImageDraw.Draw(cv)
d.text((8, 6), f"DRAFT. {NAME}: {len(clusters)} largest areas of new bare or built-up ground (proxy), {fmt_day(Y0)} -> {fmt_day(Y1)}",
       fill=(240, 240, 240), font=font(16))
d.text((8, 32), f"Background: {fmt_day(Y1)} true colour. Numbers match metrics.json clusters. Could be quarries, construction, cleared, harvested or burnt ground.",
       fill=(170, 170, 170), font=font(13))
cv.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG).save(HERE / "clusters.png", optimize=True)
for cl in clusters:
    cl.pop("_px")

# ---------------- metrics.json ----------------
bprops = json.load(open(BOUNDARY))["features"][0]["properties"]
out = {
    "title": f"{NAME} Sentinel-2 land-cover change, dry season {Y0} vs {Y1}",
    "generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    "status": "DRAFT - first-pass, unreviewed. Proxies from two single dates, not a land-use survey. Describes land cover only.",
    "boundary": {
        "source": "DataMeet maps repo, docs/data/geojson/ac.geojson (Assembly Constituencies scraped from ECI polling-station site psleci.nic.in)",
        "url": "https://github.com/datameet/maps/blob/master/docs/data/geojson/ac.geojson",
        "license": "CC BY 2.5 India (DataMeet)",
        "feature_properties": bprops,
        "district_note": CFG["district_note"],
        "delimitation": "2008 (Delimitation Order 2008; Karnataka first used it in the 2008 election). Inferred: STATUS field empty (DataMeet marks only pre-delimitation states).",
        "known_issues": f"DataMeet README: 'There is some shift in the data'. Polygon has {len(RINGS_PX)} part(s), {sum(len(r) for r in RINGS_PX)} vertices. Treat edges as approximate.",
        "area_ha_" + DST_CRS.replace(":", "").lower(): round(POLY_HA, 1),
        "part_areas_ha": [round(q.area / 1e4, 1) for q in getattr(poly_utm, "geoms", [poly_utm])],
    },
    "imagery": {
        "collection": "sentinel-2-l2a (Microsoft Planetary Computer STAC, anonymous SAS-signed asset URLs)",
        "stac_api": STAC,
        "selection": CFG["scene_choice_note"],
        "scenes": {yr: data[yr]["meta"] for yr in SCENES},
    },
    "method": {
        "grid": f"{DST_CRS}, {RES} m pixels, {W}x{H}; 10 m bands nearest-neighbour, B11 (20 m) bilinear, SCL (20 m) nearest. Same-date tiles mosaicked (first listed tile wins in overlaps).",
        "reflectance": "L2A (DN + BOA_ADD_OFFSET)/10000; offset -1000 for processing baseline >= 04.00 (decided per tile), 0 before",
        "cloud_mask": f"SCL classes excluded: {[SCL_NAMES[k] for k in BAD_SCL]}. Areas counted only on pixels valid in BOTH dates inside the boundary.",
        "thresholds": {
            "vegetation": "NDVI = (B08-B04)/(B08+B04) > 0.4",
            "open_water_headline": "MNDWI = (B03-B11)/(B03+B11) > 0  (Xu 2006)",
            "open_water_secondary": "NDWI = (B03-B08)/(B03+B08) > 0  (McFeeters 1996), comparison only",
            "builtup_bare_proxy": "NDBI = (B11-B08)/(B11+B08) > 0 AND NDVI < 0.2 AND not MNDWI water. A PROXY: also catches bare soil, dry/harvested fields, cleared plots, quarries, rock, dry grass",
        },
        "pixel_area_ha": PIX_HA,
        "comparison_area_ha": round(float(both.sum()) * PIX_HA, 1),
        "comparison_area_pct_of_boundary": round(float(both.sum() / INSIDE.sum() * 100), 2),
        "note_categories": "Categories are independent thresholds; a pixel can be in none of them. They do not sum to 100%.",
    },
    "results_inside_boundary": {
        "by_year": metrics_by_year,
        "net_change": change,
        "gross_pixel_transitions": gross,
    },
    "vegetation_inside_vs_outside_osm_protected_forest": forest_out,
    "water_bodies_osm": {
        "query": "Overpass API: way/relation natural=water or landuse=reservoir intersecting the boundary polygon, named or not",
        "note": lake_note + f" Water ha = pixels with MNDWI>0 inside the OSM outline (clipped to the boundary); measured only if >= {CFG['min_lake_ha']} ha. Water bodies covered by weeds count as vegetation. OSM outlines are volunteer-drawn and current-day; overlapping OSM features (e.g. a river polygon and a reservoir polygon) are listed separately and can double count.",
        "named_count": sum(1 for l in lakes_out if l["named_in_osm"]),
        "total_count": len(lakes_out),
        "water_bodies": lakes_out,
    },
    "new_bare_or_builtup_proxy_clusters": {
        "definition": f"4-connected regions of pixels that were NOT built-up/bare proxy on {fmt_day(Y0)} (vegetation or other non-bare cover) and ARE built-up/bare proxy on {fmt_day(Y1)}, valid in both dates, inside the boundary. Label: 'new bare or built-up ground (proxy)'. Each could be a quarry, construction, a cleared or ploughed field, harvested cropland, dry grass or burnt vegetation or a drained water body; this analysis does not and cannot say which, nor anything about cause, ownership or legality.",
        "nbr_note": "NBR = (B08-B12)/(B08+B12); dNBR = NBR(first date) - NBR(second date), median over the cluster. Reported only as a spectral descriptor: dNBR above ~0.1 is commonly read in the literature as a possible recent-burn signal, but dry soil, harvest and clearing can also raise it. Unverified; no ground truth.",
        "stats": cluster_stats,
        "largest": clusters,
    },
    "robustness_other_dates": (json.load(open(HERE / "data/robustness_dates.json"))
                               if (HERE / "data/robustness_dates.json").exists() else "not run (robustness_check.py)"),
    "outputs": ["metrics.json", f"truecolor_{Y0}_{Y1}.png", f"change_map_{Y0}_{Y1}.png", "clusters.png", "METHOD.md",
                "config.json", "extract_boundary.py", "search_scenes.py", "fetch_osm.py", "analyze.py",
                "data/candidates.json", "data/osm_water_all.json", "data/osm_forest_protected.json",
                "data/osm_query_log.json", "robustness_check.py", "data/robustness_dates.json", "data/run_log.txt", f"data/boundary/{BOUNDARY.name}"],
}
json.dump(out, open(HERE / "metrics.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(json.dumps(out["results_inside_boundary"], indent=1))
print(json.dumps({yr: data[yr]["meta"] for yr in SCENES}, indent=1))
print(len(lakes_out), "water bodies;", cluster_stats)
