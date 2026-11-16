# DRAFT: Kanakapura (AC 184) from space, dry season 2019 vs 2026

Status: first-pass, unreviewed research. Not for the public site until re-checked.
All numbers live in `metrics.json`; this note explains how they were made, how this
run differs from the Mahadevapura one (`../METHOD.md`), and what the numbers cannot
tell you. It describes land cover only. It says nothing about who did or allowed any
change, whether anything was legal, or why it happened.

## What was measured

Two cloud-free Sentinel-2 satellite pictures, 13 February 2019 and 11 February 2026,
were compared pixel by pixel on a 10 m grid (0.01 ha per pixel). Same tests as
Mahadevapura:

- **Vegetation**: NDVI above 0.4 (green leaves: forest canopy, scrub in leaf, green crops,
  plantations, weeds on water all look alike).
- **Open water**: MNDWI above 0 (headline); NDWI above 0 reported for comparison.
- **Built-up / bare land (PROXY)**: NDBI above 0, NDVI below 0.2, not water. In a rural
  constituency like Kanakapura this mostly measures **bare and dry ground**: ploughed or
  harvested fields, fallow land, dry grass, rock, burnt ground, quarries, cleared plots,
  and also some construction. It is not a count of buildings.

The categories are separate tests and do not add up to 100%. Areas are counted on pixels
cloud-free in both pictures (100.0% of the constituency here).

## Results in brief (compared area 108,864 ha)

| | 13 Feb 2019 | 11 Feb 2026 | Net change |
|---|---|---|---|
| Vegetation (NDVI > 0.4) | 24,587 ha (22.6%) | 32,206 ha (29.6%) | +7,620 ha (+31%) |
| Open water (MNDWI > 0) | 551 ha (0.51%) | 670 ha (0.62%) | +120 ha (+22%) |
| Open water, NDWI > 0 (comparison only) | 665 ha | 708 ha | +43 ha |
| Built-up/bare PROXY | 14,418 ha (13.2%) | 8,052 ha (7.4%) | -6,366 ha (-44%) |

Gross transitions: vegetation lost 6,594 ha / gained 14,214 ha; water lost 75 ha /
gained 195 ha; built-up/bare proxy new 3,759 ha / no longer 10,126 ha (of the new proxy,
236 ha was vegetation in 2019).

**Read this table with the robustness section below.** The large rise in vegetation and
fall in bare ground is dominated by how green the forest and scrub happened to be on the
two days, not by a durable change in land cover (see "Is the date pair typical?").

### Vegetation inside vs outside OSM forest / protected areas

OpenStreetMap has seven forest/protected polygons touching the boundary (cached in
`data/osm_forest_protected.json`): Cauvery Wildlife Sanctuary (21,409 ha inside the
boundary), Chilandi State Forest (12,345 ha), Bannerghatta National Park (6,888 ha),
Bananthamari Reserved Forest (1,832 ha), Cauvery North WLS (253 ha), Gangadharagudda RF
(201 ha), Tenginakal RF (176 ha). Several overlap; their union covers 32,122 ha (29.5% of
the constituency). These are volunteer-drawn outlines, not official notified boundaries.

| Region | Area | Veg 2019 | Veg 2026 | Net | Veg lost | Veg gained | New bare proxy |
|---|---|---|---|---|---|---|---|
| Inside OSM protected/forest union | 32,122 ha | 3,116 ha (9.7%) | 7,747 ha (24.1%) | +4,632 ha | 906 ha | 5,537 ha | 463 ha |
| Outside | 76,747 ha | 21,471 ha (28.0%) | 24,459 ha (31.9%) | +2,988 ha | 5,688 ha | 8,676 ha | 3,297 ha |

(Protected-area polygons alone: 9.7% -> 25.2%; landuse=forest polygons alone: 9.6% -> 33.0%.)

The forest and scrub tracts are mostly dry deciduous; in February many trees have shed
leaves, so their NDVI swings strongly with how dry that particular winter was. Tripling of
"vegetation" inside the forest polygons in seven years is far more likely to be a
leaf-on/leaf-off and rainfall effect than new forest. Outside the forests (farmland,
villages, the town), the net change is smaller (+3.9 points) but gross change on both
sides is large, which is the signature of crop-cycle timing.

### Water bodies

OSM has only **3 English-named water bodies** inside the boundary (Harobele Reservoir,
Honaganahalli Kere, Swamana Kere) plus the Kaveri river polygon (Kannada name only); the
other 55 water polygons are unnamed. All 59 are listed in `metrics.json`; unnamed ones are
labelled by OSM id with a point inside them so they can be found on a map. 39 are 2 ha or
larger and were measured. Biggest changes in MNDWI water (2019 -> 2026):

| Water body | Point (lat, lon) | OSM area inside | Water 2019 | Water 2026 | Change |
|---|---|---|---|---|---|
| Honaganahalli Kere | 12.4356, 77.2739 | 62 ha | 0.0 ha | 27.9 ha | +27.9 (vegetation 24.1 -> 7.2 ha) |
| unnamed reservoir, way/127303374 | 12.3972, 77.6106 | 19 ha | 3.9 ha | 18.0 ha | +14.1 |
| unnamed, way/56139378 | 12.4214, 77.3717 | 151 ha | 44.7 ha | 50.9 ha | +6.2 |
| unnamed lake, way/1159138439 | 12.5056, 77.4451 | 8 ha | 1.4 ha | 6.9 ha | +5.5 |
| unnamed lake, way/1159138442 | 12.4994, 77.5227 | 15 ha | 6.4 ha | 2.0 ha | -4.4 |

Harobele Reservoir (493 ha OSM outline) held almost the same open water on both days:
337.5 vs 338.5 ha. Small tanks fill and empty with each monsoon, so single-date water is
a weather reading, not a trend.

### Largest areas of new bare or built-up ground (proxy)

Connected (4-neighbour) groups of pixels that were **not** bare/built proxy on 13 Feb 2019
and **are** on 11 Feb 2026. 88,482 such groups exist; 305 are 1 ha or larger (893 ha in
total) and 2,866 ha sits in groups under 1 ha, i.e. mostly field-scale speckle. The 15
largest are listed in `metrics.json` and numbered on `clusters.png`. They are labelled only
as "new bare or built-up ground (proxy)". They could be quarries, construction, cleared,
ploughed or harvested fields, dry grass, or burnt ground. Nothing here says which.

A visual check of clusters 1-5, 7 and 12 (west/south-west, around 12.40 N, 77.32-77.35 E)
on the two pictures shows dark patches on the 2026 image, along the edge of the hill
forest, that are also dark red in a short-wave-infrared false-colour view; that
appearance is consistent with recently burnt vegetation, and the median dNBR (a burn
index, reported per cluster in `metrics.json`) is 0.10-0.34 for these seven (above ~0.1 is commonly read as a possible burn signal;
dry soil and harvest can also raise it). This is
an unverified spectral reading, not a finding; field or high-resolution checks are needed.

## Data sources

- **Boundary**: DataMeet `maps`, `docs/data/geojson/ac.geojson` (CC BY 2.5 India), cached
  at `../data/boundary/datameet_ac.geojson`. Feature OBJECTID 2404, AC_NO **184**
  "Kanakapura", PC_NO 23 "BANGALORE RURAL", DIST_NAME "BANGALORE RURAL" (the file uses the
  pre-2007 district; the AC is in Ramanagara district, renamed Bengaluru South in 2025).
  136 vertices, area **108,869 ha** (UTM 43N). Saved alone as
  `data/boundary/kanakapura_ac184.geojson` by `extract_boundary.py`. Delimitation 2008
  (inferred as for Mahadevapura). DataMeet warns of "some shift in the data".
- **Imagery**: Copernicus Sentinel-2 L2A via Microsoft Planetary Computer (no account).
  - 2019: 13 Feb 2019, Sentinel-2A, orbit R019, processing baseline 02.12.
    `S2A_MSIL2A_20190213T050921_R019_T43PGP_20201007T162012` (tile cloud 0.008%) and
    `S2A_MSIL2A_20190213T050921_R019_T43PGQ_20201007T162011` (0.067%). 0.004% of the
    constituency masked.
  - 2026: 11 Feb 2026, Sentinel-2B, orbit R019, baseline 05.12.
    `S2B_MSIL2A_20260211T050839_R019_T43PGP_20260211T085923` (0.35%) and
    `S2B_MSIL2A_20260211T050839_R019_T43PGQ_20260211T085923` (0.002%). 0.000% masked.
  - Choice (`search_scenes.py`, `data/candidates.json`): every Jan-Mar acquisition over the
    boundary was grouped by date and orbit (all are orbit R019, tiles 43PGP + 43PGQ) and
    scored by masked fraction inside the boundary on a 60 m SCL mosaic. 13 Feb 2019 was the
    cleanest 2019 date; 11 Feb 2026 was fully clean and two calendar days from it. This is
    the same date pair as Mahadevapura. 6 Feb 2026 (Sentinel-2C) was equally clean but
    further in day-of-year. No 2025 fallback was needed.
  - The pipeline mosaics both tiles, but in practice tile 43PGP alone covers the whole
    polygon (43PGQ contributed 0 pixels: first tile wins in the overlap).
- **OSM**: Overpass API (overpass-api.de), queried 16 Nov 2026 (`fetch_osm.py`; log in
  `data/osm_query_log.json`). The first attempt at the water query got HTTP 502 from
  overpass-api.de and a read timeout from overpass.kumi.systems; a retry minutes later
  succeeded. Responses are cached and reused. © OpenStreetMap contributors, ODbL.

## What differs from the Mahadevapura run

1. All constituency-specific values (name, AC number, boundary, scene IDs, titles) are in
   `config.json`; the scripts carry no Kanakapura or Mahadevapura text.
2. Multi-tile support: same-date, same-orbit tiles are mosaicked, and the ESA -1000
   reflectance offset is decided per tile from its own processing baseline (applied to
   2026, not 2019, exactly as before).
3. Still 10 m: the 4,496 x 4,482 grid (20 M pixels) fitted in memory, so no coarser
   working resolution was needed. (The robustness check alone runs at 20 m.)
4. Water: all OSM water polygons, named or not (OSM names only 3 here, vs 62 in
   Mahadevapura). Overlapping OSM features (e.g. river and reservoir polygons) are listed
   separately and can double count.
5. New: vegetation inside vs outside OSM protected/forest polygons; clusters of new
   bare/built proxy with centroids, % inside forest, and NBR/dNBR as a descriptor.
6. Change map: each output pixel is a 5 x 5 block of analysis pixels, coloured where the
   class covers at least 25% of the block (the original sampled nearest pixels).

## Is the date pair typical? (robustness check)

`robustness_check.py` recomputed the vegetation and bare-proxy shares for every clean
Jan-Mar date on the same orbit in 2019, 2025 and 2026 (20 m grid, tile 43PGP, same
thresholds; results in `data/robustness_dates.json` and `metrics.json`). The 20 m figure
for 13 Feb 2019 (22.1% vegetation) matches the 10 m one (22.6%), so the coarser grid is
comparable. Vegetation share inside the boundary, selected dates:

| Period | 2019 | 2025 | 2026 |
|---|---|---|---|
| early Jan | 48.5% (4 Jan) | 86.8% (12 Jan) | 57.3% (7 Jan) |
| ~6-8 Feb | 18.7% (8 Feb) | 60.5% (6 Feb) | 33.0% (6 Feb) |
| ~11-13 Feb (headline pair) | **22.1% (13 Feb)** | 51.8% (11 Feb) | **29.3% (11 Feb)** |
| ~16-18 Feb | 22.1% (18 Feb) | 41.1% (16 Feb) | 24.7% (16 Feb) |
| mid-March | 16.7% (15 Mar) | 24.8% (15 Mar) | 23.6% (10 Mar) |

Bare/built proxy at the same dates: 2019 11.8-13.9% in mid-Feb and 24-29% in March;
2026 6.3-11.9% in mid-Feb and 9-10% in March.

What this shows:

- Greenness falls very fast through the dry season: in 2019 the vegetation share halved
  between early January and mid-February. A few days' shift in date moves the headline by
  several points.
- Between years at the same calendar date the swing is far larger than the 2019-2026
  difference: on ~11 Feb it was 22% (2019), 52% (2025) and 29% (2026). That is weather and
  leaf phenology, not land-use change.
- 2026 was greener than 2019 at every matched date pair checked (within 3 days: +2.6 to +16.9 points),
  and the 2019 dry season was markedly barer by March. So the direction "2026 greener than
  2019 in the dry season" is consistent, but its size depends on the date picked, and these
  data cannot separate a lasting change in cover from a wetter preceding year.

Conclusion: the headline net changes in vegetation and in the bare/built proxy should
**not** be quoted as land-cover change. The more defensible outputs are the localised
items (individual clusters, individual water bodies) that someone checks on the ground or
in high-resolution imagery. A proper trend would need many dates per year (e.g. annual
median composites or peak-season NDVI), which this single-pair pipeline does not do.

## Limits (read before quoting any number)

1. **One day per year.** February greenness in dry deciduous forest, scrub and rain-fed
   farmland depends heavily on how much rain fell in the preceding months and on crop
   timing. Kanakapura is mostly such land, so single-date comparisons here are much
   noisier than in urban Mahadevapura. The gross changes (14,214 ha of vegetation gained,
   6,594 ha lost) dwarf any plausible real land-use change.
2. **The built-up proxy is mostly bare-ground in a rural area.** Its 44% fall means the
   ground was greener on 11 Feb 2026, not that buildings disappeared.
3. **Thresholds are textbook values** (NDVI 0.4, MNDWI 0, NDBI 0), not calibrated here.
4. **Different satellites and processing** (2A in 2019, 2B in 2026; baselines 02.12 vs
   05.12). Designed to match, but small radiometric differences remain.
5. **Boundary accuracy.** The DataMeet polygon is approximate; OSM forest/protected
   outlines are volunteer-drawn and may differ from notified boundaries.
6. **Water**: small tanks are monsoon-dependent; weed-covered water counts as vegetation;
   10 m pixels cannot measure ponds under ~2 ha.
7. **Clusters** are spectral change only. The 15 largest are 8-40 ha; their nature (fire
   scar, harvest, quarry, construction, clearing) needs a look on the ground or in
   high-resolution imagery. The burn-index reading is a hint, not a finding.

## Files

`config.json` (parameters), `extract_boundary.py`, `search_scenes.py`, `fetch_osm.py`,
`analyze.py`, `robustness_check.py`; outputs `metrics.json`, `truecolor_2019_2026.png`,
`change_map_2019_2026.png`, `clusters.png`; data in `data/` (`candidates.json`,
`osm_water_all.json`, `osm_forest_protected.json`, `osm_query_log.json`,
`robustness_dates.json`, `run_log.txt`, `boundary/kanakapura_ac184.geojson`).
Run order: extract_boundary, search_scenes, fetch_osm, analyze, robustness_check.
Contains modified Copernicus Sentinel data (2019, 2026).
