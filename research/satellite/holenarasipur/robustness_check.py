"""DRAFT. Robustness check (not used for headline numbers): is the chosen date pair
typical of its season? Re-computes vegetation (NDVI>0.4) and the bare/built-up PROXY
share inside the boundary for every clean Jan-Mar date on the configured relative orbit in
2019, 2025 and 2026, on a coarser 20 m grid from the single configured tile (config.json
robustness_tile / robustness_orbit; the tile must cover the whole boundary).
Same thresholds, SCL mask and per-scene reflectance offset as analyze.py.
Writes data/robustness_dates.json."""
import json, sys
from pathlib import Path
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
DST_CRS, RES, TILE, ORBIT = CFG["dst_crs"], 20.0, CFG["robustness_tile"], CFG["robustness_orbit"]
BAD_SCL = [0, 1, 3, 8, 9, 10]
poly_ll = shape(json.load(open(HERE / CFG["boundary"]))["features"][0]["geometry"])
poly_utm = shp_transform(Transformer.from_crs("EPSG:4326", DST_CRS, always_xy=True).transform, poly_ll)
minx, miny, maxx, maxy = poly_utm.bounds
minx = np.floor(minx / 20) * 20 - 200; maxy = np.ceil(maxy / 20) * 20 + 200
maxx = np.ceil(maxx / 20) * 20 + 200; miny = np.floor(miny / 20) * 20 - 200
W = int(round((maxx - minx) / RES)); H = int(round((maxy - miny) / RES))
TR = from_origin(minx, maxy, RES, RES)
INSIDE = geometry_mask([mapping(poly_utm)], (H, W), TR, invert=True)

cands = json.load(open(HERE / "data/candidates.json"))
dates = [c for c in cands if c.get("poly_bad_frac") is not None and c["poly_bad_frac"] < 0.01
         and c["date"][5:7] in ("01", "02", "03") and c.get("relative_orbit") == ORBIT
         and any(f"_T{TILE}_" in i for i in c["ids"])]
cat = pystac_client.Client.open(STAC, modifier=planetary_computer.sign_inplace)


def read(href, rs):
    with rasterio.open(href) as src:
        with WarpedVRT(src, crs=DST_CRS, transform=TR, width=W, height=H, resampling=rs, nodata=0) as v:
            return v.read(1)


def one(c):
    iid = [i for i in c["ids"] if f"_T{TILE}_" in i][0]
    it = next(cat.search(collections=["sentinel-2-l2a"], ids=[iid]).items())
    off = -1000 if float(it.properties.get("s2:processing_baseline", "0")) >= 4.0 else 0
    b = {}
    for k in ["B03", "B04", "B08", "B11"]:
        dn = read(it.assets[k].href, Resampling.nearest if k == "B11" else Resampling.average).astype("float32")
        r = (dn + off) / 10000.0
        r[dn == 0] = np.nan
        b[k] = r
    scl = read(it.assets["SCL"].href, Resampling.nearest)
    with np.errstate(divide="ignore", invalid="ignore"):
        ndvi = (b["B08"] - b["B04"]) / (b["B08"] + b["B04"])
        ndbi = (b["B11"] - b["B08"]) / (b["B11"] + b["B08"])
        mndwi = (b["B03"] - b["B11"]) / (b["B03"] + b["B11"])
    valid = INSIDE & ~np.isin(scl, BAD_SCL) & np.isfinite(ndvi) & np.isfinite(ndbi)
    n = valid.sum()
    return {"date": c["date"], "platform": it.properties.get("platform"), "id": iid,
            "baseline": it.properties.get("s2:processing_baseline"), "offset": off,
            "valid_pct": round(float(n / INSIDE.sum() * 100), 2),
            "veg_pct": round(float((valid & (ndvi > 0.4)).sum() / n * 100), 2),
            "builtup_bare_proxy_pct": round(float((valid & (ndbi > 0) & (ndvi < 0.2) & ~(mndwi > 0)).sum() / n * 100), 2),
            "median_ndvi": round(float(np.nanmedian(ndvi[valid])), 4)}


def with_retry(c, tries=3):
    for t in range(tries):
        try:
            return one(c)
        except Exception as e:  # Planetary Computer COG reads occasionally fail mid-tile
            err = repr(e)
            print("retry", c["date"], t, err[:120], file=sys.stderr)
    return {"date": c["date"], "error": err[:300]}


from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(4) as ex:
    out = sorted(ex.map(with_retry, dates), key=lambda r: r["date"])
for r in out:
    print(r, file=sys.stderr)
json.dump({"note": f"DRAFT robustness check, 20 m grid, tile {TILE} only, all Jan-Mar R{ORBIT:03d} dates with <1% masked inside the boundary (60 m scoring). Not the headline numbers.",
           "dates": out}, open(HERE / "data/robustness_dates.json", "w"), indent=1)
