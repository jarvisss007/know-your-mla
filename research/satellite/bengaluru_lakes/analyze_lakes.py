"""DRAFT. Step 2: open water and "green on lake" for every OSM water body of >= min_lake_ha in the
union of the Bengaluru Urban Assembly Constituencies, on the two configured Sentinel-2 L2A dates.

Lake-only adaptation of ../byatarayanapura/analyze.py: SAME thresholds (MNDWI > 0 water,
NDVI > 0.4 green), SAME SCL mask, SAME per-tile -1000 reflectance offset for processing
baseline >= 04.00, SAME resampling (10 m bands nearest, B11 bilinear, SCL nearest).
Differences: the whole-city grid is read band by band and indices are computed only at lake
pixels (memory); same-named OSM parts are merged only when they touch (a city has many
lakes sharing a name); river/canal/wastewater-type polygons are excluded (config
excluded_water_tags); each lake gets area-weighted constituency shares; an outline mostly
(>= 80%) covered by a larger measured outline is flagged and left out of rankings and totals.
Outputs: lakes.csv, by_constituency.csv, data/lakes_metrics.json, data/measured_lakes.geojson,
lakes_change_overview.png."""
import json, re, sys, time, csv, datetime as dt
from pathlib import Path
import numpy as np
import rasterio
from rasterio.vrt import WarpedVRT
from rasterio.enums import Resampling
from rasterio.features import geometry_mask, rasterize
from rasterio.transform import from_origin
from pyproj import Transformer
from shapely.geometry import shape, mapping, Polygon, LineString
from shapely.ops import transform as shp_transform, polygonize, unary_union
from shapely.strtree import STRtree
import pystac_client
import planetary_computer
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
CFG = json.load(open(HERE / "config.json"))
STAC = "https://planetarycomputer.microsoft.com/api/stac/v1"
DST_CRS, RES = CFG["dst_crs"], float(CFG["res_m"])
SCENES = CFG["scenes"]
Y0, Y1 = sorted(SCENES)
BAD_SCL = [0, 1, 3, 8, 9, 10]
T_NDVI_VEG, T_WATER = 0.4, 0.0
PIX_HA = RES * RES / 1e4
DARK = (18, 18, 20)
KN = re.compile(r"[ಀ-೿]")
SHARE_MIN = CFG["cross_boundary_min_share_pct"]

to_utm = Transformer.from_crs("EPSG:4326", DST_CRS, always_xy=True).transform
to_ll = Transformer.from_crs(DST_CRS, "EPSG:4326", always_xy=True).transform
union_ll = shape(json.load(open(HERE / "data/boundary/bengaluru_urban_union.geojson"))["features"][0]["geometry"])
union_utm = shp_transform(to_utm, union_ll)
ACS = []
for f in json.load(open(HERE / "data/boundary/bengaluru_urban_acs.geojson"))["features"]:
    p = f["properties"]
    no = int(p.get("AC_NO") or 0)
    nm = p.get("AC_NAME") or "unnumbered DataMeet gap polygon"
    ACS.append({"ac_no": no, "ac_name": nm, "label": f"{no} {nm}" if no else "0 unnumbered DataMeet gap polygon",
                "g_utm": shp_transform(to_utm, shape(f["geometry"]).buffer(0))})
minx, miny, maxx, maxy = union_utm.bounds
minx = np.floor((minx - 200) / 40) * 40; maxy = np.ceil((maxy + 200) / 40) * 40
maxx = np.ceil((maxx + 200) / 40) * 40; miny = np.floor((miny - 200) / 40) * 40
W = int(round((maxx - minx) / RES)); H = int(round((maxy - miny) / RES))
TR = from_origin(minx, maxy, RES, RES)
print("grid", W, H, file=sys.stderr)


# ---------------- OSM lakes ----------------
def osm_geom(e):  # identical to ../byatarayanapura/analyze.py
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


els = json.load(open(HERE / "data/osm_water_all.json"))
osm_log = json.load(open(HERE / "data/osm_query_log.json"))["osm_water_all.json"]
EXCL = set(CFG["excluded_water_tags"])
GENERIC = {"water tank", "quarry water", "quarry catchment", "pond", "lake", "kere", "tank", "quarry", "water",
           "temple pond", "kalyani", "pushkarni", "swimming pool"}
parts, excluded, no_geom, outside = [], {}, 0, 0
seen = set()
for e in els:
    oid = f"{e['type']}/{e['id']}"
    if oid in seen:
        continue
    seen.add(oid)
    t = e.get("tags", {})
    if t.get("water") in EXCL:
        excluded[t["water"]] = excluded.get(t["water"], 0) + 1
        continue
    g = osm_geom(e)
    if g is None or g.is_empty:
        no_geom += 1
        continue
    if not g.intersects(union_ll):
        outside += 1
        continue
    nm = (t.get("name") or t.get("name:en") or "").strip()
    parts.append({"oid": oid, "g": g, "t": t, "name": nm})
print(len(els), "elements;", len(parts), "lake-type polygons in area; excluded", excluded, "no geom", no_geom,
      "outside", outside, file=sys.stderr)

# group: same non-generic name AND touching (within ~50 m); unnamed / generic names stay one polygon each
groups, by_name = [], {}
for p in parts:
    key = p["name"].lower()
    if key and key not in GENERIC:
        by_name.setdefault(key, []).append(p)
    else:
        groups.append([p])
for key, ps in by_name.items():
    gs = [[q] for q in ps]
    merged = True
    while merged:
        merged = False
        for i in range(len(gs)):
            for j in range(i + 1, len(gs)):
                if unary_union([q["g"] for q in gs[i]]).distance(unary_union([q["g"] for q in gs[j]])) < 0.0005:
                    gs[i] += gs.pop(j)
                    merged = True
                    break
            if merged:
                break
    groups += gs

lakes = []
for ps in groups:
    g_all = unary_union([q["g"] for q in ps])
    g_ll = g_all.intersection(union_ll)
    if g_ll.is_empty:
        continue
    g_utm = shp_transform(to_utm, g_ll)
    name = ps[0]["name"]
    kn = sorted({q["t"]["name:kn"] for q in ps if q["t"].get("name:kn")} | {q["name"] for q in ps if KN.search(q["name"])})
    named = bool(name or kn)
    disp = name if name else (kn[0] if kn else f"unnamed {ps[0]['oid']}")
    if name.lower() in GENERIC:
        disp = f"{name} ({ps[0]['oid']})"
    cen = g_ll.representative_point()
    lakes.append({"name": disp, "named_in_osm": named, "name_kn": "; ".join(kn),
                  "osm_ids": [q["oid"] for q in ps],
                  "water_tag": sorted({q["t"].get("water") or q["t"].get("landuse") or q["t"].get("natural") or "" for q in ps} - {""}),
                  "lat": round(cen.y, 5), "lon": round(cen.x, 5),
                  "osm_ha_in_area": round(g_utm.area / 1e4, 2), "osm_ha_total": round(shp_transform(to_utm, g_all).area / 1e4, 2),
                  "_g_utm": g_utm, "_g_ll": g_ll})
meas = [l for l in lakes if l["osm_ha_in_area"] >= CFG["min_lake_ha"]]
meas.sort(key=lambda l: -l["osm_ha_in_area"])
print(len(lakes), "water bodies;", len(meas), f">= {CFG['min_lake_ha']} ha", file=sys.stderr)
for l in meas:
    shares = []
    for ac in ACS:
        a = ac["g_utm"].intersection(l["_g_utm"]).area
        if a > 0:
            shares.append((ac["label"], round(a / l["_g_utm"].area * 100, 1)))
    l["constituency_shares"] = sorted(shares, key=lambda s: -s[1])

# duplicates: an outline >= 80% covered by a LARGER measured outline is flagged
tree = STRtree([l["_g_utm"] for l in meas])
for i, l in enumerate(meas):
    l["overlaps_larger_outline"], l["partial_overlap"] = "", ""
    for j in sorted(tree.query(l["_g_utm"])):
        if j < i:
            ov = meas[j]["_g_utm"].intersection(l["_g_utm"]).area / l["_g_utm"].area
            if ov >= 0.8:
                l["overlaps_larger_outline"] = f"{meas[j]['name']} ({ov * 100:.0f}% covered)"
                break
            if ov >= 0.05 and not l["partial_overlap"]:
                l["partial_overlap"] = f"{meas[j]['name']} ({ov * 100:.0f}%)"

# pixel index per lake (local window rasterisation)
for l in meas:
    x0, y0, x1, y1 = l["_g_utm"].bounds
    c0 = max(int((x0 - minx) // RES) - 1, 0); c1 = min(int((x1 - minx) // RES) + 2, W)
    r0 = max(int((maxy - y1) // RES) - 1, 0); r1 = min(int((maxy - y0) // RES) + 2, H)
    tr = from_origin(minx + c0 * RES, maxy - r0 * RES, RES, RES)
    m = geometry_mask([mapping(l["_g_utm"])], (r1 - r0, c1 - c0), tr, invert=True)
    rr, cc = np.nonzero(m)
    l["_idx"] = ((rr + r0) * W + (cc + c0)).astype("int64")
    l["pixels"] = int(m.sum())
keep = [l for l in meas if not l["overlaps_larger_outline"]]
ALL_IDX = np.unique(np.concatenate([l["_idx"] for l in meas]))
UNION_IDX = np.unique(np.concatenate([l["_idx"] for l in keep]))
ac_lab = rasterize([(mapping(ac["g_utm"]), k + 1) for k, ac in enumerate(ACS)], out_shape=(H, W), transform=TR,
                   fill=0, dtype="uint8")
AC_AT_UNION = ac_lab.ravel()[UNION_IDX]
del ac_lab

# ---------------- imagery ----------------
cat = pystac_client.Client.open(STAC, modifier=planetary_computer.sign_inplace)


def read(href, resampling, tr=TR, w=W, h=H, tries=4):
    # Planetary Computer COG reads fail now and then: retry with backoff (15, 30, 60 s)
    for t in range(tries):
        try:
            with rasterio.open(href) as src:
                with WarpedVRT(src, crs=DST_CRS, transform=tr, width=w, height=h, resampling=resampling, nodata=0) as v:
                    return v.read(1)
        except Exception as e:
            if t == tries - 1:
                raise
            print("read retry", t + 1, repr(e)[:120], file=sys.stderr)
            time.sleep(15 * 2 ** t)


data = {}
for yr, ids in SCENES.items():
    assert len(ids) == 1, "tile 43PGQ covers the whole union (data/tile_coverage.json); no mosaic"
    it = next(cat.search(collections=["sentinel-2-l2a"], ids=ids).items())
    bl = float(it.properties.get("s2:processing_baseline", "0"))
    off = -1000 if bl >= 4.0 else 0  # ESA BOA_ADD_OFFSET=-1000 from baseline 04.00 (Jan 2022)
    print("loading", yr, it.id, "offset", off, file=sys.stderr)
    scl = read(it.assets["SCL"].href, Resampling.nearest).ravel()[ALL_IDX]
    b = {}
    for k in ["B03", "B04", "B08", "B11"]:
        dn = read(it.assets[k].href, Resampling.bilinear if k == "B11" else Resampling.nearest).ravel()[ALL_IDX]
        r = (dn.astype("float32") + off) / 1e4
        r[dn == 0] = np.nan
        b[k] = r
        print("  ", k, file=sys.stderr)
    with np.errstate(divide="ignore", invalid="ignore"):
        ndvi = (b["B08"] - b["B04"]) / (b["B08"] + b["B04"])
        mndwi = (b["B03"] - b["B11"]) / (b["B03"] + b["B11"])
        ndbi = (b["B11"] - b["B08"]) / (b["B11"] + b["B08"])
    valid = ~np.isin(scl, BAD_SCL) & np.isfinite(ndvi) & np.isfinite(mndwi) & np.isfinite(ndbi)
    tc = None
    if yr == Y1:  # quicklook background, true colour on a 40 m grid
        tr4 = from_origin(minx, maxy, RES * 4, RES * 4)
        tc = np.dstack([read(it.assets[k].href, Resampling.average, tr4, W // 4, H // 4) for k in ["B04", "B03", "B02"]]).astype("float32")
        tc = np.clip((tc + off) / 1e4 / 0.30, 0, 1) ** (1 / 1.4)
        tc = (np.nan_to_num(tc) * 255).astype("uint8")
    data[yr] = {"valid": valid, "water": valid & (mndwi > T_WATER), "veg": valid & (ndvi > T_NDVI_VEG), "tc": tc,
                "meta": {"id": it.id, "datetime": it.properties["datetime"], "platform": it.properties.get("platform"),
                         "relative_orbit": it.properties.get("sat:relative_orbit"), "mgrs_tile": it.properties.get("s2:mgrs_tile"),
                         "processing_baseline": it.properties.get("s2:processing_baseline"),
                         "tile_cloud_cover_pct": it.properties.get("eo:cloud_cover"), "reflectance_offset_applied": off,
                         "masked_pct_of_measured_lake_pixels": round(float((~valid).mean() * 100), 3),
                         "stac_item_url": f"{STAC}/collections/sentinel-2-l2a/items/{it.id}"}}
    del b, ndvi, mndwi, ndbi, scl

for l in meas:
    p = np.searchsorted(ALL_IDX, l["_idx"])
    for yr in SCENES:
        d = data[yr]
        l[f"valid_pct_{yr}"] = round(float(d["valid"][p].mean() * 100), 1)
        l[f"water_ha_{yr}"] = round(float(d["water"][p].sum()) * PIX_HA, 2)
        l[f"green_on_lake_ha_{yr}"] = round(float(d["veg"][p].sum()) * PIX_HA, 2)
    l["water_change_ha"] = round(l[f"water_ha_{Y1}"] - l[f"water_ha_{Y0}"], 2)
    l["green_change_ha"] = round(l[f"green_on_lake_ha_{Y1}"] - l[f"green_on_lake_ha_{Y0}"], 2)
    l[f"water_pct_of_outline_{Y0}"] = round(l[f"water_ha_{Y0}"] / l["osm_ha_in_area"] * 100, 1)
    l[f"water_pct_of_outline_{Y1}"] = round(l[f"water_ha_{Y1}"] / l["osm_ha_in_area"] * 100, 1)

# per seat, over the union of non-duplicate outlines (overlaps counted once), pixel exact
pu = np.searchsorted(ALL_IDX, UNION_IDX)
for l in meas:
    l["primary_constituency"] = l["constituency_shares"][0][0] if l["constituency_shares"] else ""
    l["crosses_constituency_boundary"] = sum(1 for s in l["constituency_shares"] if s[1] >= SHARE_MIN) > 1
    l["partly_outside_study_area"] = l["osm_ha_total"] - l["osm_ha_in_area"] > 0.1
seats = []
for k, ac in enumerate(ACS):
    pk = pu[AC_AT_UNION == k + 1]
    prim = [l for l in keep if l["primary_constituency"] == ac["label"]]
    touch = [l for l in keep if any(s[0] == ac["label"] and s[1] >= SHARE_MIN for s in l["constituency_shares"])]
    row = {"ac_no": ac["ac_no"], "ac_name": ac["ac_name"], "lakes_counted_primary_seat": len(prim),
           f"lakes_with_ge_{SHARE_MIN}pct_of_outline_in_seat": len(touch),
           "lakes_crossing_into_other_seats": sum(1 for l in touch if l["crosses_constituency_boundary"]),
           "lake_outline_ha_in_seat": round(len(pk) * PIX_HA, 1)}
    for pre, key in [("water_ha_", "water"), ("green_on_lake_ha_", "veg")]:
        for yr in SCENES:
            row[pre + yr] = round(float(data[yr][key][pk].sum()) * PIX_HA, 1)
    row["water_change_ha"] = round(row[f"water_ha_{Y1}"] - row[f"water_ha_{Y0}"], 1)
    row["green_change_ha"] = round(row[f"green_on_lake_ha_{Y1}"] - row[f"green_on_lake_ha_{Y0}"], 1)
    for yr in SCENES:
        row[f"valid_pct_{yr}"] = round(float(data[yr]["valid"][pk].mean() * 100), 1) if len(pk) else ""
    seats.append(row)
seats.sort(key=lambda r: r["ac_no"])
tot = {"lakes": len(keep), "outline_ha": round(len(pu) * PIX_HA, 1)}
for yr in SCENES:
    tot[f"water_ha_{yr}"] = round(float(data[yr]["water"][pu].sum()) * PIX_HA, 1)
    tot[f"green_on_lake_ha_{yr}"] = round(float(data[yr]["veg"][pu].sum()) * PIX_HA, 1)
    tot[f"valid_pct_{yr}"] = round(float(data[yr]["valid"][pu].mean() * 100), 2)
w0, w1 = data[Y0]["water"][pu], data[Y1]["water"][pu]
g0, g1 = data[Y0]["veg"][pu], data[Y1]["veg"][pu]
tot.update({"water_gained_ha": round(float((~w0 & w1).sum()) * PIX_HA, 1), "water_lost_ha": round(float((w0 & ~w1).sum()) * PIX_HA, 1),
            "green_gained_ha": round(float((~g0 & g1).sum()) * PIX_HA, 1), "green_lost_ha": round(float((g0 & ~g1).sum()) * PIX_HA, 1)})

# ---------------- outputs ----------------
COLS = ["rank_by_area", "name", "named_in_osm", "name_kn", "osm_ids", "water_tag", "lat", "lon", "osm_ha_in_area",
        "osm_ha_total", "pixels", f"valid_pct_{Y0}", f"valid_pct_{Y1}", f"water_ha_{Y0}", f"water_ha_{Y1}", "water_change_ha",
        f"water_pct_of_outline_{Y0}", f"water_pct_of_outline_{Y1}",
        f"green_on_lake_ha_{Y0}", f"green_on_lake_ha_{Y1}", "green_change_ha",
        "primary_constituency", "constituency_shares", "crosses_constituency_boundary", "partly_outside_study_area",
        "overlaps_larger_outline", "partial_overlap"]
for i, l in enumerate(meas, 1):
    l["rank_by_area"] = i
with open(HERE / "lakes.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(COLS)
    for l in meas:
        row = []
        for c in COLS:
            v = l.get(c, "")
            if c in ("osm_ids", "water_tag"):
                v = " ".join(v)
            elif c == "constituency_shares":
                v = "; ".join(f"{a}: {s}%" for a, s in v)
            row.append(v)
        w.writerow(row)
with open(HERE / "by_constituency.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=list(seats[0]))
    w.writeheader()
    w.writerows(seats)
    allrow = {k: "" for k in seats[0]}
    allrow.update({"ac_name": "ALL SEATS (union of outlines, overlaps once)", "lakes_counted_primary_seat": tot["lakes"],
                   "lake_outline_ha_in_seat": tot["outline_ha"],
                   **{k: v for k, v in tot.items() if k.startswith(("water_ha_", "green_on_lake_ha_", "valid_pct_"))},
                   "water_change_ha": round(tot[f"water_ha_{Y1}"] - tot[f"water_ha_{Y0}"], 1),
                   "green_change_ha": round(tot[f"green_on_lake_ha_{Y1}"] - tot[f"green_on_lake_ha_{Y0}"], 1)})
    w.writerow(allrow)
json.dump({"type": "FeatureCollection", "features": [
    {"type": "Feature", "geometry": mapping(l["_g_ll"]),
     "properties": {k: (json.dumps(v, ensure_ascii=False) if isinstance(v, (list, tuple)) else v)
                    for k, v in l.items() if not k.startswith("_")}} for l in meas]},
    open(HERE / "data/measured_lakes.geojson", "w", encoding="utf-8"), ensure_ascii=False)
json.dump({"title": f"Bengaluru Urban lakes, Sentinel-2 open water and green-on-lake, {Y0} vs {Y1}",
           "status": "DRAFT - first-pass, unreviewed. Two single dates. Describes what the imagery shows only.",
           "generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
           "scenes": {yr: data[yr]["meta"] for yr in SCENES}, "grid": f"{DST_CRS}, {RES} m, {W}x{H}",
           "osm": {**osm_log, "elements_returned": len(els), "lake_type_polygons_in_area": len(parts),
                   "excluded_by_water_tag": excluded, "no_polygon_geometry": no_geom,
                   "water_bodies_after_grouping": len(lakes), "under_min_ha": len(lakes) - len(meas),
                   "measured_ge_min_ha": len(meas), "measured_named": sum(l["named_in_osm"] for l in meas),
                   "flagged_duplicate_outlines": len(meas) - len(keep)},
           "totals_union_of_outlines": tot, "by_constituency": seats,
           "acs_used": [{"ac_no": a["ac_no"], "ac_name": a["ac_name"], "area_ha": round(a["g_utm"].area / 1e4, 1)} for a in ACS]},
          open(HERE / "data/lakes_metrics.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)


# ---------------- overview PNG ----------------
def font(sz, bold=False):
    for f in (["arialbd.ttf"] if bold else []) + ["arial.ttf", "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(f, sz)
        except Exception:
            pass
    return ImageFont.load_default()


tc = data[Y1]["tc"]
th, tw = tc.shape[:2]
S = 1250 / th
mw, mh = int(tw * S), int(th * S)
g = np.asarray(Image.fromarray(tc).resize((mw, mh), Image.LANCZOS).convert("L")).astype("float32") * 0.42
px = lambda x, y: ((x - minx) / (RES * 4) * S, (maxy - y) / (RES * 4) * S)
outside = Image.new("L", (mw, mh), 255)
ImageDraw.Draw(outside).polygon([px(x, y) for x, y in union_utm.exterior.coords], fill=0)
g[np.asarray(outside) > 0] *= 0.35
bg = Image.fromarray(np.dstack([g.astype("uint8")] * 3))
dr = ImageDraw.Draw(bg)
for ac in ACS:
    for q in getattr(ac["g_utm"], "geoms", [ac["g_utm"]]):
        dr.line([px(x, y) for x, y in q.exterior.coords], fill=(105, 105, 115), width=1)
dr.line([px(x, y) for x, y in union_utm.exterior.coords], fill=(255, 220, 0), width=2)


BINS = [(50, (30, 110, 255), "+50 or more"), (20, (70, 160, 255), "+20 to +50"), (5, (150, 200, 245), "+5 to +20"),
        (-5, (150, 150, 150), "within +/-5"), (-20, (250, 200, 150), "-5 to -20"), (-50, (255, 140, 50), "-20 to -50"),
        (-1e9, (230, 60, 30), "-50 or less")]


def col(dv):  # change in open water, percentage points of the outline, discrete bins
    for k, lo in enumerate([50, 20, 5, -5 + 1e-9, -20 + 1e-9, -50 + 1e-9]):
        if dv >= lo:
            return BINS[k][1]
    return BINS[6][1]


for l in sorted(keep, key=lambda l: -l["osm_ha_in_area"]):
    c = col(l[f"water_pct_of_outline_{Y1}"] - l[f"water_pct_of_outline_{Y0}"])
    for q in getattr(l["_g_utm"], "geoms", [l["_g_utm"]]):
        pts = [px(x, y) for x, y in q.exterior.coords]
        if len(pts) > 2:
            dr.polygon(pts, fill=c)
    x, y = px(*shp_transform(to_utm, l["_g_ll"].representative_point()).coords[0])
    r = max(2.5, min(8, (l["osm_ha_in_area"] ** 0.5) * 0.8))
    dr.ellipse([x - r, y - r, x + r, y + r], fill=c, outline=(15, 15, 15))
top = sorted(keep, key=lambda l: -abs(l["water_change_ha"]))[:10]
for i, l in enumerate(top, 1):
    x, y = px(*shp_transform(to_utm, l["_g_ll"].representative_point()).coords[0])
    dr.text((x + 8, y - 9), str(i), fill=(255, 255, 255), font=font(15, True), stroke_width=2, stroke_fill=(0, 0, 0))
head, side = 92, 390
cv = Image.new("RGB", (mw + side, mh + head + 30), DARK)
cv.paste(bg, (0, head))
d = ImageDraw.Draw(cv)
d.text((10, 8), "DRAFT. Bengaluru Urban lakes: open water, 13 Feb 2019 vs 11 Feb 2026 (Sentinel-2, 10 m)",
       fill=(240, 240, 240), font=font(20, True))
d.text((10, 38), f"{len(keep)} OSM water bodies of 2 ha or more, coloured by the change in open water (MNDWI>0) as a share of each OSM outline.",
       fill=(200, 200, 200), font=font(14))
d.text((10, 62), "Yellow: union of the 28 DataMeet AC outlines (AC 150-177). Grey lines: AC boundaries. Background: 11 Feb 2026, dimmed.",
       fill=(160, 160, 160), font=font(13))
lx, ly = mw + 16, head + 6
d.text((lx, ly), "Change in open water", fill=(240, 240, 240), font=font(15, True)); ly += 24
d.text((lx, ly), "(percentage points of the outline)", fill=(170, 170, 170), font=font(13)); ly += 24
for _, c, lab in BINS:
    d.rectangle([lx, ly, lx + 22, ly + 16], fill=c)
    d.text((lx + 30, ly), lab, fill=(220, 220, 220), font=font(14)); ly += 23
ly += 10
d.text((lx, ly), "10 largest changes in water (ha):", fill=(240, 240, 240), font=font(14, True)); ly += 22
for i, l in enumerate(top, 1):
    nm = l["name"] if len(l["name"]) <= 34 else l["name"][:33] + "..."
    d.text((lx, ly), f"{i:>2}. {nm}", fill=(220, 220, 220), font=font(13)); ly += 17
    d.text((lx + 24, ly), f"{l[f'water_ha_{Y0}']:.1f} -> {l[f'water_ha_{Y1}']:.1f} ha ({l['water_change_ha']:+.1f})",
           fill=(170, 170, 170), font=font(12)); ly += 19
ly += 10
for s in ["More water can mean weed clearance,", "desilting or rain; less water can mean", "drying, weed cover or encroachment.",
          "The imagery cannot tell which.", "Single dates: see FINDINGS_DRAFT.md for", "the multi-date check."]:
    d.text((lx, ly), s, fill=(170, 170, 170), font=font(12)); ly += 16
d.text((10, mh + head + 8), "Contains modified Copernicus Sentinel data (2019, 2026). Lake outlines (c) OpenStreetMap contributors, ODbL. "
       "AC boundaries: DataMeet, CC BY 2.5 IN.", fill=(150, 150, 150), font=font(12))
out = HERE / "lakes_change_overview.png"
cv.save(out, optimize=True)
if out.stat().st_size > 1.45e6:  # fall back to a 256-colour palette that keeps the legend colours exact
    pal = cv.convert("P", palette=Image.Palette.ADAPTIVE, colors=240)
    pal.save(out, optimize=True)
print("png bytes", out.stat().st_size, file=sys.stderr)
print(json.dumps(tot, indent=1))
