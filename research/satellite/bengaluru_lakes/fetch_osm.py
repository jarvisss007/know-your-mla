"""DRAFT. Step 1: query OpenStreetMap (Overpass API) for every water polygon in the union of the
Bengaluru Urban ACs and cache the raw response, so analyze_lakes.py never depends on a live server:
  data/osm_water_all.json   way/relation natural=water, water=lake|reservoir|pond, landuse=reservoir
A single polygon-filtered query for the whole city returned HTTP 502 from all three servers, so the
union's bounding box is split into a 2 x 2 grid of bbox queries (lighter for Overpass); results are
merged by OSM id and analyze_lakes.py clips to the exact union. Each chunk tries overpass-api.de,
overpass.kumi.systems and overpass.private.coffee, five rounds with 0/30/60/120/240 s backoff.
Chunks already fetched are kept in data/osm_chunks/. --force re-queries."""
import json, sys, time, datetime as dt
from pathlib import Path
import requests
from shapely.geometry import shape

HERE = Path(__file__).parent
ENDPOINTS = ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter",
             "https://overpass.private.coffee/api/interpreter"]
u = shape(json.load(open(HERE / "data/boundary/bengaluru_urban_union.geojson"))["features"][0]["geometry"])
x0, y0, x1, y1 = u.bounds
x0, y0, x1, y1 = x0 - 0.005, y0 - 0.005, x1 + 0.005, y1 + 0.005
N = 2
kinds = ['way["natural"="water"]', 'relation["natural"="water"]',
         'way["water"~"^(lake|reservoir|pond)$"]', 'relation["water"~"^(lake|reservoir|pond)$"]',
         'way["landuse"="reservoir"]', 'relation["landuse"="reservoir"]']
cache = HERE / "data/osm_water_all.json"
logf = HERE / "data/osm_query_log.json"
cdir = HERE / "data/osm_chunks"
cdir.mkdir(exist_ok=True)
if cache.exists() and "--force" not in sys.argv:
    sys.exit("cached; use --force to refresh")
log = {"earlier_attempt": "one poly-filtered query (union buffered 300 m, simplified, 198 vertices): HTTP 502 from all three endpoints, round 1, 24 Nov 2026",
       "chunks": []}
merged, failed = {}, []
for i in range(N):
    for j in range(N):
        bb = (y0 + (y1 - y0) * j / N, x0 + (x1 - x0) * i / N, y0 + (y1 - y0) * (j + 1) / N, x0 + (x1 - x0) * (i + 1) / N)
        bbs = ",".join(f"{v:.5f}" for v in bb)
        cf = cdir / f"chunk_{i}{j}.json"
        Q = '[out:json][timeout:300];(' + "".join(f"{k}({bbs});" for k in kinds) + ');out geom;'
        if cf.exists() and "--force" not in sys.argv:
            els = json.load(open(cf))
            log["chunks"].append({"bbox_s_w_n_e": bbs, "elements": len(els), "from_cache": True})
        else:
            notes, els = [], None
            for attempt in range(5):
                if attempt:
                    time.sleep(30 * 2 ** (attempt - 1))
                for ep in ENDPOINTS:
                    try:
                        r = requests.post(ep, data={"data": Q}, timeout=400, headers={"User-Agent": "open-data-landcover-study/0.1"})
                        if r.ok and "elements" in r.json():
                            els = r.json()["elements"]
                            json.dump(els, open(cf, "w"))
                            log["chunks"].append({"bbox_s_w_n_e": bbs, "endpoint": ep, "elements": len(els),
                                                  "queried_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                                                  "earlier_failures": notes, "remark": r.json().get("remark")})
                            break
                        notes.append(f"{ep} HTTP {r.status_code} (attempt {attempt + 1})")
                    except Exception as e:
                        notes.append(f"{ep} failed (attempt {attempt + 1}): {e!r}"[:300])
                    print(bbs, notes[-1], file=sys.stderr, flush=True)
                if els is not None:
                    break
            if els is None:
                failed.append(bbs)
                log["chunks"].append({"bbox_s_w_n_e": bbs, "failed": notes})
                continue
        print("chunk", bbs, len(els), "elements", file=sys.stderr, flush=True)
        for e in els:
            merged[f"{e['type']}/{e['id']}"] = e
log.update({"query_kinds": kinds, "elements_merged": len(merged), "failed_chunks": failed,
            "queried_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "endpoint": sorted({c.get("endpoint") for c in log["chunks"] if c.get("endpoint")})})
json.dump({"osm_water_all.json": log}, open(logf, "w"), indent=1)
if failed:
    sys.exit(f"FAILED chunks {failed}")
json.dump(list(merged.values()), open(cache, "w"))
print("merged", len(merged), "elements", file=sys.stderr)
