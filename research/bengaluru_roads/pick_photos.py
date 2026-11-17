"""Pick before/after photos per road, spread along the road, and download 1024px thumbnails to a scratch folder
(passed as argv[1]; not the repo). Writes data/photo_picks.json."""
import json, sys, pathlib, urllib.request, urllib.parse, collections
TOKEN = (pathlib.Path.home() / ".mapillary_token").read_text().strip()
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
P = json.load(open("data/street_photos.json"))
# periods relative to each road's bills (from parse_orders.py)
PER = {"jn_road_rrnagar": [("before", "2021", "2023-10")],
       "taralabalu_road": [("before", "2018", "2023-11"), ("after", "2024", "2026-12")],
       "indiranagar_100ft": [("before", "2022", "2023-04"), ("after", "2024", "2026-12")],
       "cmh_road": [("before", "2022", "2023-04"), ("after", "2024", "2026-12")],
       "patalamma_temple_road": [("before", "2020", "2023-03"), ("after", "2023-05", "2026-12")]}
picks = {}
for key, pers in PER.items():
    picks[key] = []
    for label, a, b in pers:
        cand = [p for p in P[key] if a <= p["date"][:len(a)] and p["date"][:len(b)] <= b and p["dist_m"] <= 8]
        if not cand: continue
        cand.sort(key=lambda p: (p["lon"], p["lat"]))
        n = min(4, len(cand)); idx = [round(i * (len(cand) - 1) / max(n - 1, 1)) for i in range(n)]
        for i in dict.fromkeys(idx):
            p = cand[i]
            js = json.load(urllib.request.urlopen(f"https://graph.mapillary.com/{p['id']}?" + urllib.parse.urlencode({"access_token": TOKEN, "fields": "thumb_1024_url"}), timeout=60))
            f = OUT / f"{key}_{label}_{p['date']}_{p['id']}.jpg"
            f.write_bytes(urllib.request.urlopen(js["thumb_1024_url"], timeout=60).read())
            picks[key].append({**p, "period": label, "file": f.name, "url": f"https://www.mapillary.com/app/?pKey={p['id']}"})
        print(key, label, len(cand), "candidates,", len(dict.fromkeys(idx)), "picked", file=sys.stderr)
json.dump(picks, open("data/photo_picks.json", "w"), indent=1)
