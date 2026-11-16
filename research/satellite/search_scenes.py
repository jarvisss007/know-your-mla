"""Step 1: find candidate dry-season Sentinel-2 L2A scenes over the boundary and
score each by the SCL cloud/shadow fraction INSIDE the polygon.
Writes data/candidates.json. Read-only use of free public endpoints."""
import json, sys
import numpy as np
import rasterio
from rasterio.vrt import WarpedVRT
from rasterio.features import geometry_mask
from rasterio.enums import Resampling
from pyproj import Transformer
from shapely.geometry import shape, mapping
from shapely.ops import transform as shp_transform
import pystac_client
import planetary_computer

STAC = "https://planetarycomputer.microsoft.com/api/stac/v1"
BOUNDARY = "data/boundary/mahadevapura_ac174.geojson"
DST_CRS = "EPSG:32643"
BAD_SCL = [0, 1, 3, 8, 9, 10]  # nodata, saturated, cloud shadow, cloud med, cloud high, cirrus

poly_ll = shape(json.load(open(BOUNDARY))["features"][0]["geometry"])
to_utm = Transformer.from_crs("EPSG:4326", DST_CRS, always_xy=True).transform
poly_utm = shp_transform(to_utm, poly_ll)


def grid(res):
    from rasterio.transform import from_origin
    minx, miny, maxx, maxy = poly_utm.bounds
    minx = np.floor(minx / 20) * 20 - 40; maxy = np.ceil(maxy / 20) * 20 + 40
    maxx = np.ceil(maxx / 20) * 20 + 40; miny = np.floor(miny / 20) * 20 - 40
    w = int(round((maxx - minx) / res)); h = int(round((maxy - miny) / res))
    return from_origin(minx, maxy, res, res), w, h


def scl_fraction(href):
    tr, w, h = grid(20)
    with rasterio.open(href) as src:
        with WarpedVRT(src, crs=DST_CRS, transform=tr, width=w, height=h,
                       resampling=Resampling.nearest, nodata=0) as v:
            a = v.read(1)
    inside = geometry_mask([mapping(poly_utm)], (h, w), tr, invert=True)
    vals = a[inside]
    return float(np.isin(vals, BAD_SCL).mean()), float((vals == 0).mean())


cat = pystac_client.Client.open(STAC, modifier=planetary_computer.sign_inplace)
out = []
for year, rng in [(2019, "2019-01-01/2019-03-31"), (2026, "2026-01-01/2026-03-31"),
                  (2025, "2025-01-01/2025-03-31")]:
    items = list(cat.search(collections=["sentinel-2-l2a"], intersects=mapping(poly_ll),
                            datetime=rng, query={"eo:cloud_cover": {"lt": 20}}).items())
    print(year, len(items), "items", file=sys.stderr)
    for it in items:
        from shapely.geometry import shape as sh
        covers = sh(it.geometry).contains(poly_ll)
        rec = {"year": year, "id": it.id, "datetime": it.properties["datetime"],
               "tile": it.properties.get("s2:mgrs_tile"),
               "tile_cloud_pct": it.properties.get("eo:cloud_cover"),
               "baseline": it.properties.get("s2:processing_baseline"),
               "covers_polygon": bool(covers)}
        if covers:
            try:
                rec["poly_bad_frac"], rec["poly_nodata_frac"] = scl_fraction(it.assets["SCL"].href)
            except Exception as e:
                rec["error"] = repr(e)
        print(rec, file=sys.stderr)
        out.append(rec)
json.dump(out, open("data/candidates.json", "w"), indent=1)
