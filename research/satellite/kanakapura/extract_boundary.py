"""DRAFT. Step 0: pull one Assembly Constituency feature out of the cached DataMeet
ac.geojson (matched on state + AC name + AC number from config.json) and save it alone."""
import json
from pathlib import Path
from shapely.geometry import shape
from pyproj import Transformer
from shapely.ops import transform as shp_transform

HERE = Path(__file__).parent
CFG = json.load(open(HERE / "config.json"))

src = json.load(open(HERE / CFG["boundary_source"]))
hits = [f for f in src["features"]
        if f["properties"].get("ST_NAME") == CFG["state"]
        and (f["properties"].get("AC_NAME") or "").strip().lower() == CFG["ac_name"].lower()]
assert len(hits) == 1, f"expected 1 match, got {len(hits)}"
p = hits[0]["properties"]
assert int(p["AC_NO"]) == CFG["ac_no"], p
out = HERE / CFG["boundary"]
out.parent.mkdir(parents=True, exist_ok=True)
json.dump({"type": "FeatureCollection", "features": hits}, open(out, "w"))
g = shape(hits[0]["geometry"])
to_utm = Transformer.from_crs("EPSG:4326", CFG["dst_crs"], always_xy=True).transform
print(p)
print("vertices", len(g.exterior.coords) if g.geom_type == "Polygon" else "multi",
      "bounds", g.bounds, "area_ha", round(shp_transform(to_utm, g).area / 1e4, 1))
