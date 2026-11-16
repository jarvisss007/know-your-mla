"""DRAFT. Step 2: query OpenStreetMap (Overpass API) for features inside the boundary
and cache the raw responses so analyze.py never depends on a live Overpass server:
  data/osm_water_all.json        natural=water and landuse=reservoir, named or not
  data/osm_forest_protected.json boundary=protected_area / national_park,
                                 leisure=nature_reserve, landuse=forest
Tries overpass-api.de, then overpass.kumi.systems. Re-run with --force to refresh."""
import json, sys, datetime as dt
from pathlib import Path
import requests
from shapely.geometry import shape

HERE = Path(__file__).parent
CFG = json.load(open(HERE / "config.json"))
ENDPOINTS = ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter"]

poly_ll = shape(json.load(open(HERE / CFG["boundary"]))["features"][0]["geometry"])
polystr = " ".join(f"{lat:.6f} {lon:.6f}" for lon, lat in poly_ll.exterior.coords)
P = f'(poly:"{polystr}")'

QUERIES = {
    # all water polygons, named or not: OSM has only 3 English-named water bodies here
    # (Mahadevapura had 62), so unnamed ones are kept and labelled by OSM id + centroid
    "osm_water_all.json":
        f'[out:json][timeout:180];(way["natural"="water"]{P};relation["natural"="water"]{P};'
        f'way["landuse"="reservoir"]{P};relation["landuse"="reservoir"]{P};);out geom;',
    "osm_forest_protected.json":
        f'[out:json][timeout:240];('
        f'way["boundary"="protected_area"]{P};relation["boundary"="protected_area"]{P};'
        f'way["boundary"="national_park"]{P};relation["boundary"="national_park"]{P};'
        f'way["leisure"="nature_reserve"]{P};relation["leisure"="nature_reserve"]{P};'
        f'way["landuse"="forest"]{P};relation["landuse"="forest"]{P};'
        f');out geom;',
}

force = "--force" in sys.argv
log = {}
logf = HERE / "data/osm_query_log.json"
if logf.exists():
    log = json.load(open(logf))
for fname, q in QUERIES.items():
    cache = HERE / "data" / fname
    if cache.exists() and not force:
        print(fname, "cached", file=sys.stderr)
        continue
    notes = []
    for ep in ENDPOINTS:
        try:
            r = requests.post(ep, data={"data": q}, timeout=300,
                              headers={"User-Agent": "open-data-landcover-study/0.1"})
            if r.ok and "elements" in r.json():
                els = r.json()["elements"]
                json.dump(els, open(cache, "w"))
                log[fname] = {"endpoint": ep, "queried_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                              "elements": len(els), "query": q[:400] + ("..." if len(q) > 400 else ""),
                              "earlier_failures": notes, "remark": r.json().get("remark")}
                print(fname, ep, len(els), "elements", file=sys.stderr)
                break
            notes.append(f"{ep} HTTP {r.status_code}")
        except Exception as e:
            notes.append(f"{ep} failed: {e!r}")
    else:
        log[fname] = {"failed": notes, "at_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
        print(fname, "FAILED", notes, file=sys.stderr)
json.dump(log, open(logf, "w"), indent=1)
