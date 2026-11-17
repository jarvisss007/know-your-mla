"""Fetch centrelines for pilot white-topping roads from OpenStreetMap (Overpass), clip to the
segment named in the work order where possible, write data/roads.geojson. Road names only are sent."""
import json, urllib.request, urllib.parse, sys
# (key, work_code, OSM name regex, search box s,w,n,e) -- boxes drawn around the locality in the work order
PILOT = [
 ("nagarabhavi_80ft", "303-23-000005", "^(80 Feet Road|Nagarabhavi Main Road|80 Feet Main Road)", (12.955, 77.495, 12.985, 77.525)),
 ("jn_road_rrnagar", "303-23-000026", "Jawaharlal Nehru Road|JN Road|Jawaharlal Nehru", (12.905, 77.505, 12.935, 77.535)),
 ("taralabalu_road", "303-23-000008", "Taralabalu", (13.010, 77.580, 13.030, 77.600)),
 ("indiranagar_100ft", "303-23-000004", "^100 Feet Road", (12.960, 77.630, 12.985, 77.650)),
 ("cmh_road", "303-23-000004", "^CMH Road|Chinmaya Mission Hospital Road", (12.970, 77.625, 12.990, 77.650)),
 ("patalamma_temple_road", "167-20-000089", "Patalamma|Pattalamma", (12.935, 77.570, 12.950, 77.590)),
]
feats = []
for key, code, rx, (s, w, n, e) in PILOT:
    q = f'[out:json][timeout:60];way["highway"]["name"~"{rx}",i]({s},{w},{n},{e});out geom;'
    js = None
    for ep in 2*["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter", "https://overpass.private.coffee/api/interpreter"]:
        try:
            req = urllib.request.Request(ep, data=urllib.parse.urlencode({"data": q}).encode(), headers={"User-Agent": "road-check research script"})
            js = json.load(urllib.request.urlopen(req, timeout=90)); break
        except Exception as ex:
            print(key, ep, ex, file=sys.stderr); __import__("time").sleep(10)
    if js is None:
        print(key, "SKIPPED: Overpass unavailable", file=sys.stderr); continue
    names = set()
    for el in js["elements"]:
        coords = [[p["lon"], p["lat"]] for p in el["geometry"]]
        names.add(el["tags"].get("name"))
        feats.append({"type": "Feature", "properties": {"key": key, "work_code": code, "osm_id": el["id"], "name": el["tags"].get("name"),
                      "highway": el["tags"].get("highway"), "surface": el["tags"].get("surface")}, "geometry": {"type": "LineString", "coordinates": coords}})
    print(key, len(js["elements"]), "ways", names, file=sys.stderr)
json.dump({"type": "FeatureCollection", "features": feats}, open("data/roads.geojson", "w"))
