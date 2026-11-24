"""DRAFT. Step 2: query OpenStreetMap (Overpass API) for features inside the boundary
and cache the raw responses so analyze.py never depends on a live Overpass server:
  data/osm_water_all.json        natural=water and landuse=reservoir, named or not
  data/osm_forest_protected.json boundary=protected_area / national_park,
                                 leisure=nature_reserve, landuse=forest
  data/osm_water_labels.json     named lake/kere/tank/katte/kunte/pond features of any kind,
                                 and natural=wetland (used only to name unnamed water polygons)
Tries overpass-api.de, then overpass.kumi.systems, four rounds with backoff. Re-run with --force to refresh."""
import json, sys, time, datetime as dt
from pathlib import Path
import requests
from shapely.geometry import shape

HERE = Path(__file__).parent
CFG = json.load(open(HERE / "config.json"))
ENDPOINTS = ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter"]

poly_ll = shape(json.load(open(HERE / CFG["boundary"]))["features"][0]["geometry"])
# Overpass poly: filter takes one ring; a MultiPolygon boundary (e.g. an exclave) gets one
# filter per part, and every statement below is repeated for each part.
POLYS = [" ".join(f"{lat:.6f} {lon:.6f}" for lon, lat in q.exterior.coords)
         for q in getattr(poly_ll, "geoms", [poly_ll])]


def stmts(kinds):
    return "".join(f'{k}(poly:"{ps}");' for ps in POLYS for k in kinds)

QUERIES = {
    # all water polygons, named or not (unnamed ones are kept and labelled by OSM id + centroid)
    "osm_water_all.json":
        '[out:json][timeout:180];(' + stmts(['way["natural"="water"]', 'relation["natural"="water"]',
                                             'way["landuse"="reservoir"]', 'relation["landuse"="reservoir"]']) + ');out geom;',
    "osm_forest_protected.json":
        '[out:json][timeout:240];(' + stmts([
            'way["boundary"="protected_area"]', 'relation["boundary"="protected_area"]',
            'way["boundary"="national_park"]', 'relation["boundary"="national_park"]',
            'way["leisure"="nature_reserve"]', 'relation["leisure"="nature_reserve"]',
            'way["landuse"="forest"]', 'relation["landuse"="forest"]']) + ');out geom;',
    # labels only (added for urban seats): anything named like a lake/tank, and wetland polygons.
    # analyze.py uses a named point or polygon that falls inside an UNNAMED water polygon to name it.
    "osm_water_labels.json":
        '[out:json][timeout:180];(' + stmts(['node["name"~"lake|kere|tank|katte|kunte|pond",i]',
                                             'way["name"~"lake|kere|tank|katte|kunte|pond",i]',
                                             'relation["name"~"lake|kere|tank|katte|kunte|pond",i]',
                                             'way["natural"="wetland"]', 'relation["natural"="wetland"]']) + ');out geom;',
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
    notes, done = [], False
    for attempt in range(4):  # Overpass is flaky: retry every endpoint with backoff (0, 30, 60, 120 s)
        if attempt:
            time.sleep(30 * 2 ** (attempt - 1))
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
                    done = True
                    break
                notes.append(f"{ep} HTTP {r.status_code} (attempt {attempt + 1})")
            except Exception as e:
                notes.append(f"{ep} failed (attempt {attempt + 1}): {e!r}")
        if done:
            break
    if not done:
        log[fname] = {"failed": notes, "at_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
        print(fname, "FAILED", notes, file=sys.stderr)
json.dump(log, open(logf, "w"), indent=1)
