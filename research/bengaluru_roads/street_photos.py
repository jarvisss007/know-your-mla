"""List Mapillary photos within 20 m of each pilot road (token read from ~/.mapillary_token, never stored here).
Writes data/street_photos.json: id, captured date, lon/lat, distance to centreline, compass angle, sequence.
Thumbnails are not stored in the repo."""
import json, sys, time, urllib.request, urllib.parse, pathlib, datetime as dt, collections
from shapely.geometry import shape, Point, box
from shapely.ops import unary_union, transform as T
from pyproj import Transformer
TOKEN = (pathlib.Path.home() / ".mapillary_token").read_text().strip()
to_utm = Transformer.from_crs("EPSG:4326", "EPSG:32643", always_xy=True).transform
roads = collections.defaultdict(list)
for f in json.load(open("data/roads.geojson"))["features"]:
    roads[f["properties"]["key"]].append(shape(f["geometry"]))
out = {}
for key, ls in roads.items():
    g = unary_union(ls); gu = T(to_utm, g)
    minx, miny, maxx, maxy = g.buffer(0.0004).bounds
    found = {}
    step = 0.004
    x = minx
    while x < maxx:
        y = miny
        while y < maxy:
            cell = box(x, y, min(x + step, maxx), min(y + step, maxy))
            if cell.intersects(g.buffer(0.0004)):
                q = urllib.parse.urlencode({"access_token": TOKEN, "fields": "id,captured_at,geometry,compass_angle,sequence",
                                            "bbox": ",".join(f"{v:.6f}" for v in cell.bounds), "limit": 2000})
                for attempt in range(3):
                    try:
                        js = json.load(urllib.request.urlopen("https://graph.mapillary.com/images?" + q, timeout=60)); break
                    except Exception as e:
                        print(key, "retry", type(e).__name__, file=sys.stderr); time.sleep(5); js = {"data": []}
                for im in js.get("data", []):
                    lon, lat = im["geometry"]["coordinates"]
                    d = gu.distance(Point(to_utm(lon, lat)))
                    if d <= 20:
                        found[im["id"]] = {"id": im["id"], "date": dt.datetime.utcfromtimestamp(im["captured_at"] / 1000).strftime("%Y-%m-%d"),
                                           "lon": lon, "lat": lat, "dist_m": round(d, 1), "angle": im.get("compass_angle"), "seq": im.get("sequence")}
            y += step
        x += step
    out[key] = sorted(found.values(), key=lambda r: r["date"])
    yrs = collections.Counter(r["date"][:4] for r in out[key])
    print(key, len(out[key]), "photos", dict(sorted(yrs.items())), file=sys.stderr)
json.dump(out, open("data/street_photos.json", "w"), indent=1)
