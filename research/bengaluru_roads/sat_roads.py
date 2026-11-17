"""Sentinel-2 test for white-topping: concrete is far brighter in visible light than asphalt.
For each pilot road, take dry-season (Jan-Apr) Sentinel-2 L2A scenes for 2019-2026, keep pixels whose
centre lies within 5 m of the OSM centreline and are cloud/shadow-free (SCL), and record the mean visible
reflectance (B02,B03,B04). Also split each road into 200 m pieces and report brightness per piece for the
earliest and latest year. Writes data/road_brightness.json. Free public data (Microsoft Planetary Computer)."""
import json, sys, collections, statistics
import numpy as np, rasterio
from rasterio.vrt import WarpedVRT
from rasterio.features import geometry_mask
from rasterio.enums import Resampling
from rasterio.transform import from_origin
from pyproj import Transformer
from shapely.geometry import shape, mapping, MultiLineString
from shapely.ops import transform as T, unary_union, substring, linemerge
import pystac_client, planetary_computer

CRS = "EPSG:32643"; to_utm = Transformer.from_crs("EPSG:4326", CRS, always_xy=True).transform
to_ll = Transformer.from_crs(CRS, "EPSG:4326", always_xy=True).transform
GOOD_SCL = [4, 5, 6, 7]  # vegetation, not-vegetated, water, unclassified
YEARS = range(2019, 2027)
cat = pystac_client.Client.open("https://planetarycomputer.microsoft.com/api/stac/v1", modifier=planetary_computer.sign_inplace)

roads = collections.defaultdict(list)
for f in json.load(open("data/roads.geojson"))["features"]:
    roads[f["properties"]["key"]].append(T(to_utm, shape(f["geometry"])))

def read(href, tr, w, h, rs):
    with rasterio.open(href) as src, WarpedVRT(src, crs=CRS, transform=tr, width=w, height=h, resampling=rs, nodata=0) as v:
        return v.read(1).astype("float32")

out = {}
for key, lines in roads.items():
    geom = unary_union(lines)
    area = geom.buffer(5)
    minx, miny, maxx, maxy = geom.buffer(60).bounds
    minx, maxy = np.floor(minx / 10) * 10, np.ceil(maxy / 10) * 10
    w, h = int((np.ceil(maxx / 10) * 10 - minx) / 10), int((maxy - np.floor(miny / 10) * 10) / 10)
    tr = from_origin(minx, maxy, 10, 10)
    mask = geometry_mask([mapping(area)], (h, w), tr, invert=True)
    # 200 m pieces
    merged = linemerge(geom) if geom.geom_type == "MultiLineString" else geom
    parts = list(merged.geoms) if hasattr(merged, "geoms") else [merged]
    pieces = []
    for p in parts:
        for s in np.arange(0, p.length, 200):
            seg = substring(p, s, min(s + 200, p.length))
            if seg.length > 60: pieces.append(seg)
    pmasks = [geometry_mask([mapping(seg.buffer(5))], (h, w), tr, invert=True) for seg in pieces]
    bbox_ll = T(to_ll, geom.buffer(60))
    rec = {"pixels": int(mask.sum()), "length_m": round(geom.length), "years": {}, "pieces": [mapping(T(to_ll, s)) for s in pieces]}
    for y in YEARS:
        items = list(cat.search(collections=["sentinel-2-l2a"], intersects=mapping(bbox_ll), datetime=f"{y}-01-01/{y}-04-30",
                                query={"eo:cloud_cover": {"lt": 15}}).items())
        items.sort(key=lambda it: it.properties["eo:cloud_cover"])
        vals, pv, used = [], [], []
        for it in items[:8]:
            try:
                scl = read(it.assets["SCL"].href, tr, w, h, Resampling.nearest)
                ok = mask & np.isin(scl, GOOD_SCL)
                if ok.sum() < 0.9 * mask.sum(): continue
                off = 1000 if str(it.properties.get("s2:processing_baseline", "0")) >= "04.00" else 0
                b = [(read(it.assets[n].href, tr, w, h, Resampling.bilinear) - off) / 10000 for n in ("B02", "B03", "B04")]
                vis = (b[0] + b[1] + b[2]) / 3
                vals.append(float(vis[ok].mean()))
                pv.append([float(vis[m & np.isin(scl, GOOD_SCL)].mean()) if (m & np.isin(scl, GOOD_SCL)).sum() >= 3 else None for m in pmasks])
                used.append(it.id)
            except Exception as e:
                print(key, y, it.id, repr(e)[:120], file=sys.stderr)
            if len(vals) >= 4: break
        if vals:
            piece_med = [statistics.median([s[i] for s in pv if s[i] is not None]) if any(s[i] is not None for s in pv) else None for i in range(len(pieces))]
            rec["years"][y] = {"median_vis": round(statistics.median(vals), 4), "scenes": used, "pieces": [round(v, 4) if v else None for v in piece_med]}
        print(key, y, len(items), "items", rec["years"].get(y, {}).get("median_vis"), file=sys.stderr)
    out[key] = rec
json.dump(out, open("data/road_brightness.json", "w"), indent=1)
