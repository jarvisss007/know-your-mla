"""DRAFT. Step 0: pull the Bengaluru Urban Assembly Constituencies (config ac_numbers, ST_NAME
KARNATAKA, DIST_NAME BANGALORE) out of the cached DataMeet ac.geojson, plus the one
DIST_NAME BANGALORE polygon that has AC_NO 0 / no name (a gap in the DataMeet layer), and save
them with their dissolved union. Also checks which Sentinel-2 tiles cover the union."""
import json, sys
from pathlib import Path
from shapely.geometry import shape, mapping
from shapely.ops import unary_union, transform as shp_transform
from pyproj import Transformer

HERE = Path(__file__).parent
CFG = json.load(open(HERE / "config.json"))
src = json.load(open(HERE / CFG["boundary_source"]))
feats = [f for f in src["features"] if f["properties"].get("ST_NAME") == CFG["state"]
         and f["properties"].get("DIST_NAME") == "BANGALORE"]
acs = [f for f in feats if int(f["properties"].get("AC_NO") or 0) in CFG["ac_numbers"]]
gap = [f for f in feats if int(f["properties"].get("AC_NO") or 0) == 0]
got = sorted(int(f["properties"]["AC_NO"]) for f in acs)
assert got == sorted(CFG["ac_numbers"]), got
other = [f["properties"] for f in feats if f not in acs and f not in gap]
assert not other, other
to_utm = Transformer.from_crs("EPSG:4326", CFG["dst_crs"], always_xy=True).transform
use = acs + (gap if CFG["include_unnumbered_bangalore_polygon"] else [])
for f in use:
    g = shape(f["geometry"])
    f["properties"]["area_ha"] = round(shp_transform(to_utm, g).area / 1e4, 1)
    print(int(f["properties"]["AC_NO"]), f["properties"]["AC_NAME"], f["properties"]["OBJECTID"], f["properties"]["area_ha"], file=sys.stderr)
json.dump({"type": "FeatureCollection", "features": use}, open(HERE / "data/boundary/bengaluru_urban_acs.geojson", "w"))
u = unary_union([shape(f["geometry"]).buffer(0) for f in use])
uu = shp_transform(to_utm, u)
json.dump({"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": mapping(u),
           "properties": {"name": "union of DataMeet ACs " + ",".join(map(str, got)) + (" + AC_NO 0 gap polygon" if gap else ""),
                          "area_ha": round(uu.area / 1e4, 1)}}]}, open(HERE / "data/boundary/bengaluru_urban_union.geojson", "w"))
print("union", u.geom_type, "parts", len(getattr(u, "geoms", [u])), "area ha", round(uu.area / 1e4, 1), "bounds", u.bounds, file=sys.stderr)

# tile coverage check for the configured scenes
import pystac_client, planetary_computer
cat = pystac_client.Client.open("https://planetarycomputer.microsoft.com/api/stac/v1", modifier=planetary_computer.sign_inplace)
rep = {}
for yr, ids in CFG["scenes"].items():
    for i in ids:
        it = next(cat.search(collections=["sentinel-2-l2a"], ids=[i]).items())
        fp = shape(it.geometry)
        rep[i] = round(fp.intersection(u).area / u.area, 5)
    day = ids[0].split("_")[2][:8]
    same = list(cat.search(collections=["sentinel-2-l2a"], intersects=mapping(u),
                           datetime=f"{day[:4]}-{day[4:6]}-{day[6:]}").items())
    rep[f"{yr}_all_items_that_day"] = {s.id: round(shape(s.geometry).intersection(u).area / u.area, 5) for s in same}
print(json.dumps(rep, indent=1))
json.dump(rep, open(HERE / "data/tile_coverage.json", "w"), indent=1)
