"""DRAFT. Step 1 (adapted from ../search_scenes.py for multi-tile constituencies):
find dry-season Sentinel-2 L2A acquisitions over the boundary, group same-date tiles
of the same relative orbit, mosaic their SCL layers on a coarse 60 m grid and score
the cloud/shadow fraction INSIDE the polygon. Writes data/candidates.json.
Read-only use of free public endpoints."""
import json, sys
from collections import defaultdict
from pathlib import Path
import numpy as np
import rasterio
from rasterio.vrt import WarpedVRT
from rasterio.features import geometry_mask
from rasterio.enums import Resampling
from rasterio.transform import from_origin
from pyproj import Transformer
from shapely.geometry import shape, mapping
from shapely.ops import transform as shp_transform, unary_union
import pystac_client
import planetary_computer

HERE = Path(__file__).parent
CFG = json.load(open(HERE / "config.json"))
STAC = "https://planetarycomputer.microsoft.com/api/stac/v1"
DST_CRS = CFG["dst_crs"]
BAD_SCL = [0, 1, 3, 8, 9, 10]  # nodata, saturated, cloud shadow, cloud med, cloud high, cirrus
SCORE_RES = 60.0  # scoring only; analysis runs at config res_m

poly_ll = shape(json.load(open(HERE / CFG["boundary"]))["features"][0]["geometry"])
to_utm = Transformer.from_crs("EPSG:4326", DST_CRS, always_xy=True).transform
poly_utm = shp_transform(to_utm, poly_ll)
minx, miny, maxx, maxy = poly_utm.bounds
minx = np.floor(minx / 60) * 60 - 120; maxy = np.ceil(maxy / 60) * 60 + 120
maxx = np.ceil(maxx / 60) * 60 + 120; miny = np.floor(miny / 60) * 60 - 120
W = int(round((maxx - minx) / SCORE_RES)); H = int(round((maxy - miny) / SCORE_RES))
TR = from_origin(minx, maxy, SCORE_RES, SCORE_RES)
INSIDE = geometry_mask([mapping(poly_utm)], (H, W), TR, invert=True)


def scl_mosaic(hrefs):
    mos = np.zeros((H, W), "uint8")
    for href in hrefs:
        with rasterio.open(href) as src:
            with WarpedVRT(src, crs=DST_CRS, transform=TR, width=W, height=H,
                           resampling=Resampling.nearest, nodata=0) as v:
                a = v.read(1)
        fill = (mos == 0) & (a != 0)
        mos[fill] = a[fill]
    return mos


cat = pystac_client.Client.open(STAC, modifier=planetary_computer.sign_inplace)
out = []
for year, rng in CFG["search_windows"].items():
    items = list(cat.search(collections=["sentinel-2-l2a"], intersects=mapping(poly_ll),
                            datetime=rng).items())
    groups = defaultdict(list)
    for it in items:
        groups[(it.properties["datetime"][:10], it.properties.get("sat:relative_orbit"),
                it.properties.get("platform"))].append(it)
    print(year, len(items), "items in", len(groups), "date/orbit groups", file=sys.stderr)
    for (day, orbit, plat), its in sorted(groups.items()):
        # keep one item per tile (latest processing) in case of duplicates
        by_tile = {}
        for it in sorted(its, key=lambda i: i.id):
            by_tile[it.properties.get("s2:mgrs_tile")] = it
        its = list(by_tile.values())
        cover = unary_union([shape(i.geometry) for i in its])
        rec = {"year": int(year), "date": day, "relative_orbit": orbit, "platform": plat,
               "ids": [i.id for i in its], "tiles": sorted(by_tile),
               "tile_cloud_pct": {i.properties.get("s2:mgrs_tile"): i.properties.get("eo:cloud_cover") for i in its},
               "baseline": sorted({i.properties.get("s2:processing_baseline") for i in its}),
               "footprint_covers_polygon": bool(cover.buffer(1e-6).contains(poly_ll)),
               "footprint_cover_frac": round(cover.intersection(poly_ll).area / poly_ll.area, 4)}
        if rec["footprint_cover_frac"] > 0.98 and max(v or 0 for v in rec["tile_cloud_pct"].values()) < CFG["max_tile_cloud_pct"]:
            try:
                m = scl_mosaic([i.assets["SCL"].href for i in its])
                vals = m[INSIDE]
                rec["poly_bad_frac"] = round(float(np.isin(vals, BAD_SCL).mean()), 5)
                rec["poly_nodata_frac"] = round(float((vals == 0).mean()), 5)
            except Exception as e:
                rec["error"] = repr(e)
        print(rec["date"], rec["relative_orbit"], rec["tiles"], rec["tile_cloud_pct"],
              rec.get("poly_bad_frac"), rec.get("poly_nodata_frac"), file=sys.stderr)
        out.append(rec)
(HERE / "data").mkdir(exist_ok=True)
json.dump(out, open(HERE / "data/candidates.json", "w"), indent=1)
