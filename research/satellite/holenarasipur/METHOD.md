# DRAFT: Holenarasipur (AC 197) from space, dry season 2019 vs 2026

Status: first-pass, unreviewed research. Not for the public site until re-checked.
All numbers live in `metrics.json`; this note explains how they were made, how this
run differs from the Kanakapura one (`../kanakapura/METHOD.md`, itself adapted from the
Mahadevapura run in `../METHOD.md`), and what the numbers cannot tell you. It describes
land cover only. It says nothing about who did or allowed any change, whether anything
was legal, or why it happened.

## What was measured

Two cloud-free Sentinel-2 satellite pictures, 21 February 2019 and 19 February 2026,
were compared pixel by pixel on a 10 m grid (0.01 ha per pixel). Same tests and
thresholds as Kanakapura and Mahadevapura:

- **Vegetation**: NDVI above 0.4 (green leaves: tree cover, scrub in leaf, green crops,
  plantations, weeds on water all look alike).
- **Open water**: MNDWI above 0 (headline); NDWI above 0 reported for comparison.
- **Built-up / bare land (PROXY)**: NDBI above 0, NDVI below 0.2, not water. In a rural,
  mostly farmed constituency like Holenarasipur this mostly measures **bare and dry
  ground**: ploughed or harvested fields, fallow land, dry grass, rock, burnt ground,
  quarries, cleared plots, and also some construction. It is not a count of buildings.

The categories are separate tests and do not add up to 100%. Areas are counted on pixels
cloud-free in both pictures (99.97% of the constituency here).

## Results in brief (compared area 95,027 ha; boundary 95,053 ha)

| | 21 Feb 2019 | 19 Feb 2026 | Net change |
|---|---|---|---|
| Vegetation (NDVI > 0.4) | 32,091 ha (33.8%) | 38,961 ha (41.0%) | +6,871 ha (+21%) |
| Open water (MNDWI > 0) | 680 ha (0.72%) | 2,020 ha (2.13%) | +1,340 ha (+197%) |
| Open water, NDWI > 0 (comparison only) | 881 ha | 1,986 ha | +1,105 ha |
| Built-up/bare PROXY | 13,400 ha (14.1%) | 9,002 ha (9.5%) | -4,398 ha (-33%) |

Gross transitions: vegetation lost 7,858 ha / gained 14,729 ha; water lost 48 ha /
gained 1,388 ha; built-up/bare proxy new 4,510 ha / no longer 8,908 ha (of the new proxy,
397 ha was vegetation in 2019).

**Read this table with the robustness section below.** As in Kanakapura, the greener,
wetter 2026 picture is dominated by season and rainfall, not by a durable change in land
cover.

### Vegetation inside vs outside OSM forest / protected areas

Unlike Kanakapura, OpenStreetMap maps almost no forest here: **no protected area, national
park or nature reserve** touches the boundary, and only three `landuse=forest` polygons do
(cached in `data/osm_forest_protected.json`): an unnamed forest/wood polygon (522 ha inside
the boundary), "Gendekatte forest" (50 ha) and an unnamed forest/wood polygon (15 ha);
588 ha in all, 0.6% of the constituency. These are volunteer-drawn outlines, not notified
forest boundaries, and OSM coverage of Reserved Forests in this area appears thin.

| Region | Area | Veg 2019 | Veg 2026 | Net | Veg lost | Veg gained | New bare proxy |
|---|---|---|---|---|---|---|---|
| Inside OSM forest polygons | 588 ha | 190 ha (32.4%) | 201 ha (34.2%) | +11 ha | 68 ha | 79 ha | 1 ha |
| Outside | 94,465 ha | 31,900 ha (33.8%) | 38,760 ha (41.0%) | +6,860 ha | 7,790 ha | 14,650 ha | 4,509 ha |

Inside the mapped forest polygons the vegetation share barely moved (+1.8 points); the
whole net gain is in farmland and villages outside them. With only 588 ha mapped, this
split says little; it is reported for consistency with Kanakapura. (A bounding-box check
also found about 23 `natural=wood` polygons in the area; the template query, kept
unchanged, does not include `natural=wood` unless it is also tagged `landuse=forest`.)

None of the 15 largest new-proxy clusters lies inside an OSM forest polygon.

### Water bodies

OSM has **245 water polygons** touching the boundary (tanks/kere, ponds, river segments
of the Hemavathi). Only **12 carry a name** (Shantigrama Kere, Koushika Kere, Mosale Kere,
Ambuga Kere, Koravangala Kere, Sathenahalli Lake, K Hirihalli Doddakere, Maavinakatte,
Balagatte, Annayyakere, Kunakatte, Thippegundi); the rest are labelled by OSM id with a
point inside them. 147 are 2 ha or larger and were measured; all 245 are in `metrics.json`.
Biggest changes in MNDWI water (2019 -> 2026):

| Water body | Point (lat, lon) | OSM area inside | Water 2019 | Water 2026 | Change |
|---|---|---|---|---|---|
| unnamed tank, way/59748146 | 13.0721, 76.2079 | 140 ha | 1.1 ha | 109.8 ha | +108.7 |
| unnamed tank, way/119067640 | 12.9933, 76.3358 | 61 ha | 0.0 ha | 47.8 ha | +47.8 |
| unnamed tank, way/59748151 | 13.1216, 76.2252 | 61 ha | 0.1 ha | 41.5 ha | +41.4 |
| Shantigrama Kere | 12.9929, 76.2128 | 65 ha | 12.7 ha | 52.1 ha | +39.4 |
| unnamed tank, way/119067636 | 12.9619, 76.2425 | 69 ha | 1.7 ha | 39.5 ha | +37.8 |

Almost every measured tank held more open water on 19 Feb 2026 than on 21 Feb 2019 (water
gained 1,388 ha, lost only 48 ha). That fits a much wetter preceding monsoon in 2025 than
in 2018, not a change in the tanks themselves. Small tanks fill and empty with each
monsoon, so single-date water is a weather reading, not a trend.

### Largest areas of new bare or built-up ground (proxy)

Connected (4-neighbour) groups of pixels that were **not** bare/built proxy on 21 Feb 2019
and **are** on 19 Feb 2026. 91,468 such groups exist; 387 are 1 ha or larger (907 ha in
total), 17 are 5 ha or larger, and 3,603 ha sits in groups under 1 ha, i.e. mostly
field-scale speckle. The 15 largest are listed in `metrics.json` and numbered on
`clusters.png`. They are labelled only as "new bare or built-up ground (proxy)". They
could be quarries, construction, cleared, ploughed or harvested fields, dry grass, or burnt
ground. Nothing here says which. The five largest:

| # | Area | Centroid (lat, lon) | Was vegetation 2019 | Median dNBR |
|---|---|---|---|---|
| 1 | 40.0 ha | 12.8014, 76.3087 | 0.4% | 0.05 |
| 2 | 34.0 ha | 12.9346, 76.3505 | 27.6% | 0.12 |
| 3 | 29.1 ha | 12.9721, 76.1304 | 6.7% | -0.10 |
| 4 | 24.6 ha | 12.9593, 76.1316 | 21.6% | 0.05 |
| 5 | 15.0 ha | 12.9082, 76.1901 | 5.5% | 0.07 |

Most of these were already non-green in 2019 (low "was vegetation" share): they changed
from other non-bare cover (dark soil, stubble, moist ground) to bright bare ground, not
from green cover. dNBR is near zero for most of them, so unlike several Kanakapura
clusters there is no burn-like signal in the top five. Unverified spectral readings only.

## Data sources

- **Boundary**: DataMeet `maps`, `docs/data/geojson/ac.geojson` (CC BY 2.5 India), cached
  at `../data/boundary/datameet_ac.geojson`. Feature OBJECTID **2353**, AC_NO **197**
  "Holenarasipur", PC_NO 16 "HASSAN", DIST_NAME "HASSAN". It is a **MultiPolygon**: a main
  part of 94,948 ha (160 vertices) and a small detached part of 105 ha (6 vertices) about
  0.3 km north of the main part, between the Arsikere and Hassan polygons; total
  **95,053 ha** (UTM 43N). The detached part is kept as drawn (it may be a real exclave or a
  digitising artefact; not checked against the official delimitation map). Saved alone as
  `data/boundary/holenarasipur_ac197.geojson` by `extract_boundary.py`. Delimitation 2008
  (inferred as for Mahadevapura). DataMeet warns of "some shift in the data".
- **Projection**: the polygon spans 76.10-76.38 E, centroid 76.24 E, inside UTM zone 43
  (72-78 E), so EPSG:32643 applies, as for Kanakapura.
- **Imagery**: Copernicus Sentinel-2 L2A via Microsoft Planetary Computer (no account).
  - 2019: 21 Feb 2019, Sentinel-2B, orbit R062, processing baseline 02.12.
    `S2B_MSIL2A_20190221T051839_R062_T43PFQ_20201007T191241` (tile cloud 0.015%).
    0.027% of the constituency masked at 10 m (0.023% in 60 m scoring).
  - 2026: 19 Feb 2026, Sentinel-2C, orbit R062, baseline 05.12.
    `S2C_MSIL2A_20260219T051851_R062_T43PFQ_20260219T102113` (tile cloud 0.030%).
    0.000% masked.
  - One tile, 43PFQ, covers the whole polygon on every date, so no mosaic was needed (the
    mosaic code still runs, with one tile per year).
- **OSM**: Overpass API, queried 16 Nov 2026 (`fetch_osm.py`; log in
  `data/osm_query_log.json`). Water: overpass-api.de, first try. Forest/protected:
  overpass-api.de returned HTTP 502, overpass.kumi.systems answered (3 elements); a
  separate bounding-box query to overpass-api.de afterwards returned the same three
  `landuse=forest` polygons plus two outside the boundary and no protected areas, so the
  small count is OSM's coverage, not a truncated response. Responses are cached and
  reused. © OpenStreetMap contributors, ODbL.

## Scene choice and the date check

`search_scenes.py` found 19 (2019), 20 (2025) and 19 (2026) Jan-Mar items, all orbit R062,
tile 43PFQ, and scored each date by the masked (cloud, shadow, cirrus, no-data) fraction
inside the boundary on a 60 m SCL grid (`data/candidates.json`). Rule used: among dates
under 0.1% masked, the 2019/2026 pair closest in day-of-year, keeping to February like the
Kanakapura and Mahadevapura pairs (11-13 Feb). 21 Feb 2019 (0.023%) and 19 Feb 2026
(0.000%) are two calendar days apart. Other two-day pairs that clean: 7 Jan 2019 / 5 Jan
2026 (0.032% / 0.000%) and 28 Mar 2019 / 26 Mar 2026 (0.008% / 0.001%; marginally cleaner,
but late in the dry season and six weeks off the other constituencies' dates). The masked
difference between these choices is a few hundredths of a percent and does not matter.
2026 had clean dates, so no 2025 fallback was needed.

## Is the date pair typical? (robustness check)

`robustness_check.py` recomputed the vegetation and bare-proxy shares for every clean
Jan-Mar date on orbit R062 in 2019, 2025 and 2026 (30 dates, 20 m grid, tile 43PFQ, same
thresholds; results in `data/robustness_dates.json` and `metrics.json`). The 20 m figures
for the headline dates (33.5% and 41.0% vegetation) match the 10 m ones (33.8% and 41.0%).

2019 and 2026 dates within 3 days of each other:

| 2019 date | 2026 date | Veg 2019 | Veg 2026 | Difference | Bare proxy 2019 | Bare proxy 2026 |
|---|---|---|---|---|---|---|
| 2 Jan | 5 Jan | 57.1% | 65.2% | +8.0 | 1.7% | 1.6% |
| 17 Jan | 20 Jan | 39.5% | 54.6% | +15.1 | 2.8% | 1.9% |
| 22 Jan | 20 Jan | 37.1% | 54.6% | +17.5 | 3.9% | 1.9% |
| 6 Feb | 4 Feb | 26.7% | 51.5% | +24.8 | 10.3% | 4.5% |
| 16 Feb | 14 Feb | 30.4% | 45.8% | +15.4 | 10.0% | 6.7% |
| **21 Feb** | **19 Feb** | **33.5%** | **41.0%** | **+7.5** | **12.4%** | **8.1%** |
| 13 Mar | 11 Mar | 28.7% | 44.6% | +15.9 | 21.0% | 8.7% |
| 28 Mar | 26 Mar | 27.1% | 44.6% | +17.5 | 20.6% | 10.1% |

Swing within one February: 2019 26.7-33.5% vegetation (6.8 points), 2025 43.2-53.4% (10.2),
2026 41.0-51.5% (10.5). Between years at about 19-21 Feb: 33.5% (2019), 46.6% (2025), 41.0%
(2026), so 2025 to 2026 alone moved -5.6 points with no reason to expect land-cover change.
Bare proxy in February: 2019 10.0-14.1%, 2025 3.1-5.0%, 2026 4.5-8.1%; in March 2019 it
reached 20-22%, 2026 only 7.6-10.1%.

Conclusion: **the 2019 -> 2026 difference in the headline pair (+7.2 points vegetation,
-4.6 points bare proxy) is not bigger than the swing between dates in a single February
(7-10 points) or between neighbouring years (2025 vs 2026: about 6 points).** The headline
pair actually shows the smallest vegetation gap of all matched pairs (+7.5 at 20 m; others
+8 to +25). The direction is consistent (2026 greener and less bare than 2019 at every
matched date), which fits a dry 2018-19 season against a wet 2025-26 one, but these data
cannot separate that from any lasting change in cover. The headline net changes should
**not** be quoted as land-cover change. 2019 vegetation also does not fall smoothly
through February (26.7% on 6 Feb, 33.5% on 21 Feb), which hints at a small
sensor-to-sensor effect (Sentinel-2A vs 2B) or a passing shower; another reason to treat
single dates with caution. The more defensible outputs are localised items (individual
clusters, individual tanks) that someone checks on the ground or in high-resolution
imagery.

## What differs from the Kanakapura run

1. `config.json`: Holenarasipur name, AC 197, Hassan district, boundary OBJECTID 2353
   (now also asserted by `extract_boundary.py`), scene IDs, and two new keys
   `robustness_tile` (43PFQ) and `robustness_orbit` (62), which were hard-coded (43PGP, R019)
   in Kanakapura's `robustness_check.py`; that script now also filters candidates by orbit
   and tile.
2. MultiPolygon boundary: `fetch_osm.py` sends one Overpass `poly:` filter per part;
   `analyze.py` draws every part's outline and reports part areas; `extract_boundary.py`
   prints per-part areas. A single-polygon boundary gives the same results as before.
3. `clusters.png` is capped at 1,400 px tall (the constituency is tall and narrow; the first
   render was 2.1 MB) and the canvas kept 1,150 px wide so the heading is not cut off.
   The metrics JSON key `area_ha_utm43n` is now named from the CRS (`area_ha_epsg32643`).
4. Single tile, so no mosaic; still a 10 m grid (3,074 x 5,318).
5. No other change to thresholds, masks, offsets, or the cluster method.

## Limits (read before quoting any number)

1. **One day per year.** February greenness in rain-fed farmland, scrub and plantations
   depends on the preceding monsoon and on crop timing; the robustness check shows date
   and year swings as large as the headline change.
2. **The built-up proxy is mostly bare ground here.** Its 33% fall means the ground was
   greener on 19 Feb 2026, not that buildings disappeared.
3. **Thresholds are textbook values** (NDVI 0.4, MNDWI 0, NDBI 0), not calibrated here.
4. **Different satellites and processing** (2B in 2019, 2C in 2026; baselines 02.12 vs
   05.12, reflectance offset applied only to 2026). Designed to match, but small radiometric
   differences remain.
5. **Boundary accuracy.** The DataMeet polygon is approximate, and its 105 ha detached part
   is unverified. OSM forest outlines are volunteer-drawn and here cover only 588 ha.
6. **Water**: tanks are monsoon-dependent; weed-covered water counts as vegetation; 10 m
   pixels cannot measure ponds under ~2 ha; overlapping OSM features (river and tank
   polygons) can double count.
7. **Clusters** are spectral change only. The 15 largest are 6-40 ha; their nature
   (harvest, ploughing, quarry, construction, clearing, fire) needs a look on the ground
   or in high-resolution imagery.

## Files

`config.json` (parameters), `extract_boundary.py`, `search_scenes.py`, `fetch_osm.py`,
`analyze.py`, `robustness_check.py`; outputs `metrics.json`, `truecolor_2019_2026.png`,
`change_map_2019_2026.png`, `clusters.png`; data in `data/` (`candidates.json`,
`search_log.txt`, `osm_water_all.json`, `osm_forest_protected.json`, `osm_query_log.json`,
`robustness_dates.json`, `robustness_log.txt`, `run_log.txt`,
`boundary/holenarasipur_ac197.geojson`).
Run order: extract_boundary, search_scenes, fetch_osm, analyze, robustness_check (then
analyze again to fold the robustness results into `metrics.json`).
Contains modified Copernicus Sentinel data (2019, 2026).
