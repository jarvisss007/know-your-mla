# DRAFT: Byatarayanapura (AC 152) from space, dry season 2019 vs 2026

Status: first-pass, unreviewed research. Not for the public site until re-checked.
All numbers live in `metrics.json` (and `data/robustness_dates.json`); this note explains
how they were made, how this run differs from the Holenarasipur one
(`../holenarasipur/METHOD.md`, itself adapted from Kanakapura and Mahadevapura), and what
the numbers cannot tell you. It describes land cover only. It says nothing about who did
or allowed any change, whether anything was legal, or why it happened.

## What was measured

Two cloud-free Sentinel-2 pictures, 13 February 2019 and 11 February 2026 (the same dates
as the Mahadevapura run, same tile 43PGQ), compared pixel by pixel on a 10 m grid. Same
tests and thresholds as the earlier runs:

- **Vegetation**: NDVI above 0.4 (tree cover, parks, green crops, scrub in leaf, and weeds
  on lakes all look alike).
- **Open water**: MNDWI above 0 (headline); NDWI above 0 for comparison.
- **Built-up / bare land (PROXY)**: NDBI above 0, NDVI below 0.2, not water. In this mixed
  urban/peri-urban seat it catches roofs, roads and paved land together with bare plots,
  ploughed or dry fields, dry grass and quarries. Dense older built-up areas often fail
  the test. It is not a count of buildings.

Categories are separate tests and do not add up to 100%. Areas are counted on pixels
cloud-free in both pictures: 21,387.5 ha, 99.76% of the 21,440.5 ha boundary.

## Results in brief

| | 13 Feb 2019 | 11 Feb 2026 | Net change |
|---|---|---|---|
| Vegetation (NDVI > 0.4) | 4,902.8 ha (22.92%) | 5,975.6 ha (27.94%) | +1,072.8 ha (+21.9%) |
| Open water (MNDWI > 0) | 174.6 ha (0.82%) | 511.6 ha (2.39%) | +337.0 ha (+193%) |
| Open water, NDWI > 0 (comparison only) | 152.2 ha | 425.0 ha | +272.8 ha |
| Built-up/bare PROXY | 8,258.6 ha (38.61%) | 5,917.7 ha (27.67%) | -2,340.9 ha (-28.3%) |

Gross transitions: vegetation lost 1,860.7 ha / gained 2,933.5 ha; water lost 42.9 ha /
gained 379.9 ha; proxy new 2,034.5 ha / no longer 4,375.4 ha (of the new proxy, 514.8 ha
was vegetation in 2019).

**Read this table with the date check below.** The net figures are no bigger than the
swing between dates and years.

### Vegetation inside vs outside OSM forest / protected areas

OSM has 29 forest/protected features touching the boundary (`data/osm_forest_protected.json`),
600.9 ha inside it in all: Marasandra Reserve Forest (365.4 ha), Jarakabande Sandal Reserve
Forest (128.9 ha), Botanical Garden (25.8 ha, tagged protected area / Biodiversity Heritage
Site), Bettakote Reserved Forest (21.0 ha) and 25 small unnamed `landuse=forest` polygons.
Volunteer-drawn outlines, not notified boundaries.

| Region | Area | Veg 2019 | Veg 2026 | Veg lost | Veg gained | New bare proxy |
|---|---|---|---|---|---|---|
| Inside OSM forest/protected | 600.9 ha | 238.1 ha (39.63%) | 492.0 ha (81.88%) | 17.7 ha | 271.6 ha | 2.4 ha |
| Outside | 20,838.6 ha | 4,664.7 ha (22.44%) | 5,483.6 ha (26.38%) | 1,843.0 ha | 2,661.9 ha | 2,032.0 ha |

The 40% -> 82% jump inside the forest outlines is far larger than outside and most likely
reflects the condition of dry scrub/deciduous cover on the two dates; it is not evidence
of a change in tree cover without other dates.

### Water bodies and "green on lake"

`fetch_osm.py` fetched 440 OSM water elements (`natural=water`, `landuse=reservoir`, named
or not); 437 water bodies touch the boundary after grouping, 42 named. 51 are 2 ha or larger
and are measured. As in Mahadevapura, each lake also reports **green on lake**
(`vegetation_ha_<year>`: NDVI > 0.4 inside the OSM outline), because floating weeds hide
open water from the MNDWI test; read the two together.

New in this run, to name more lakes from OSM: a third Overpass query
(`data/osm_water_labels.json`: anything named like lake/kere/tank/katte/kunte/pond, plus
`natural=wetland`). A label is used only if it lies inside an UNNAMED water polygon (node)
or covers at least half of it (polygon); residential/commercial names, gates, roads,
places and "...view" names are excluded, and a trailing "Park" is stripped. Result: no
unnamed polygon gained a name (`names_from_label_features` is empty); the named lakes all
carry their names on the water polygon itself. 21 wetland polygons were seen, none named,
so none were added. Generic names (Water Tank, quarry water/catchment) are kept per OSM id
rather than merged across places.

Totals over the union of the 51 measured outlines (735.6 ha, overlaps counted once):
open water 133.6 ha -> 380.4 ha (gained 265.1, lost 18.2); green on lake 199.6 ha -> 245.5 ha
(gained 155.2, lost 109.4); bare proxy 146.6 ha -> 56.5 ha.

Biggest changes in MNDWI water:

| Water body | Point (lat, lon) | OSM area inside | Water 2019 | Water 2026 | Change | Green on lake 2019 -> 2026 |
|---|---|---|---|---|---|---|
| unnamed, way/28069768 (tagged pond) | 13.17756, 77.68543 | 77.55 ha | 0.2 ha | 64.0 ha | +63.8 | 11.7 -> 10.9 |
| Bagaluru Kere | 13.14006, 77.65811 | 52.89 ha | 2.6 ha | 32.5 ha | +29.9 | 10.1 -> 0.5 |
| Gummanahalli Lake | 13.13954, 77.68932 | 56.91 ha | 3.1 ha | 30.9 ha | +27.8 | 2.1 -> 24.8 |
| Doddabommasandra Kere | 13.06502, 77.56302 | 33.72 ha | 0.0 ha | 27.8 ha | +27.8 | 19.4 -> 6.3 |
| Thimmasandra | 13.17050, 77.58753 | 24.70 ha | 0.0 ha | 17.5 ha | +17.5 | 0.4 -> 4.2 |

Lakes named in the brief:
- **Jakkur Lake** crosses the boundary (36.42 of 49.69 ha inside): water 31.1 -> 31.1 ha,
  green on lake 22.9 -> 26.9 ha.
- **Rachenahalli Lake** (35.85 ha): water 29.8 -> 31.8 ha, green on lake 30.2 -> 2.9 ha,
  i.e. the weed cover visible in 2019 is mostly gone on 11 Feb 2026.
- **Allalasandra Lake** is in OSM (relation/16048376, 13.09101, 77.58639) but its point is
  0.5 km OUTSIDE the DataMeet outline, so it is not measured. Yelahanka, Puttenahalli and
  Attur lakes are also outside (1.2, 1.9, 1.4 km). Checked by a Nominatim name search
  (`data/osm_name_probe.json`, folded into `metrics.json` as
  `named_lakes_checked_by_search`). If the official delimitation map puts Allalasandra
  inside the seat, the DataMeet boundary is shifted here.
- **Hebbal Lake** (45.34 ha, wholly inside this outline): water 37.4 -> 31.1 ha.
  **Nagawara Lake** crosses the boundary (14.74 of 29.24 ha inside): water 5.1 -> 0.0 ha.
  Both sit at the southern edge, where boundary error matters most.

### Largest areas of new bare or built-up ground (proxy)

4-connected groups of pixels not proxy on 13 Feb 2019 and proxy on 11 Feb 2026: 38,798
groups; 276 are 1 ha or larger (590.0 ha), 12 are 5 ha or larger, 1,444.5 ha sits in groups
under 1 ha (mostly field-scale speckle). The 15 largest are in `metrics.json`,
`clusters.png` and `field_checks.csv`. Five largest:

| # | Area | Point (lat, lon) | Was vegetation 2019 | In OSM forest | Median dNBR |
|---|---|---|---|---|---|
| 1 | 16.74 ha | 13.12281, 77.69226 | 58.5% | 0.0% | 0.13 |
| 2 | 10.99 ha | 13.18470, 77.64776 | 2.3% | 0.0% | -0.196 |
| 3 | 10.39 ha | 13.14800, 77.61556 | 22.1% | 0.0% | -0.012 |
| 4 | 9.18 ha | 13.14802, 77.63040 | 44.9% | 9.3% | 0.075 |
| 5 | 9.11 ha | 13.11818, 77.71166 | 3.4% | 0.0% | -0.05 |

(Points are the member pixel nearest the cluster centre, as used on the page and in the
CSV.) Labels are "new bare or built-up ground (proxy)" only: quarry, construction,
clearing, ploughing, harvest, dry grass or fire all look alike here.

## Data sources

- **Boundary**: DataMeet `maps`, `docs/data/geojson/ac.geojson` (CC BY 2.5 India), cached
  at `../data/boundary/datameet_ac.geojson`. Feature OBJECTID **2355**, AC_NO **152**
  "Byatarayanapura", PC_NO 24 "BANGALORE NORTH", DIST_NAME "BANGALORE". One polygon,
  76 vertices, **21,440.5 ha** (UTM 43N). Saved alone as
  `data/boundary/byatarayanapura_ac152.geojson`. Delimitation 2008 (inferred).
- **Projection**: the polygon spans 77.52-77.74 E, inside UTM zone 43 (72-78 E), so
  EPSG:32643 applies (verified).
- **Imagery**: Copernicus Sentinel-2 L2A via Microsoft Planetary Computer.
  - 2019: 13 Feb 2019, Sentinel-2A, orbit R019, baseline 02.12,
    `S2A_MSIL2A_20190213T050921_R019_T43PGQ_20201007T162011` (tile cloud 0.067%).
    0.238% of the constituency masked at 10 m (0.237% in 60 m scoring).
  - 2026: 11 Feb 2026, Sentinel-2B, orbit R019, baseline 05.12,
    `S2B_MSIL2A_20260211T050839_R019_T43PGQ_20260211T085923` (tile cloud 0.0018%).
    0.005% masked at 10 m (0.000% at 60 m).
  - Tile 43PGQ covers the whole polygon on every date; no mosaic needed.
- **OSM**: Overpass API, queried 24 Nov 2026 (`data/osm_query_log.json`). Water:
  overpass.kumi.systems after overpass-api.de returned 502. Forest/protected:
  overpass-api.de on the third round after four 502/504 failures. Labels: overpass-api.de.
  A regex name query over a bounding box timed out on both servers three times; the name
  check was then done with Nominatim. © OpenStreetMap contributors, ODbL.

## Scene choice

All Jan-Mar items in 2019 (18), 2025 (18) and 2026 (21) are orbit R019, tile 43PGQ
(`data/candidates.json`, `data/search_log.txt`). No February 2019 date is under 0.1%
masked (the Holenarasipur rule): the lowest is 23 Feb (0.101%), whose 2026 partner 21 Feb
is 0.754% masked. Chosen: 13 Feb 2019 (0.237%) / 11 Feb 2026 (0.000%), two days apart,
the same pair as Mahadevapura. Slightly cleaner 2-day pairs: 3 Feb 2019 / 1 Feb 2026
(0.131% / 0.000%; but the 2019 tile had 7.3% cloud nearby, a higher risk of unflagged
haze) and 24 Jan 2019 / 22 Jan 2026 (0.154% / 0.000%; 24 Jan 2019 also gives an outlying
8.2% vegetation in the date check, consistent with haze). The masked difference is about
0.1% of the area.

## Is the date pair typical? (date check)

`robustness_check.py` recomputed vegetation and bare-proxy shares on all 37 clean
Jan-Mar R019 dates (14 in 2019, 12 in 2025, 11 in 2026; 20 m grid; `data/robustness_dates.json`).
At 20 m the headline dates give 21.62% and 26.65% vegetation (10 m: 22.92%, 27.94%).

2019 and 2026 dates within 3 days of each other (20 m):

| 2019 | 2026 | Veg 2019 | Veg 2026 | Diff | Bare 2019 | Bare 2026 | Diff |
|---|---|---|---|---|---|---|---|
| 4 Jan | 7 Jan | 30.18% | 35.76% | +5.58 | 23.56% | 24.42% | +0.86 |
| 9 Jan | 7 Jan | 28.60% | 35.76% | +7.16 | 24.80% | 24.42% | -0.38 |
| 19 Jan | 17 Jan | 26.12% | 36.65% | +10.53 | 27.80% | 22.46% | -5.34 |
| 24 Jan | 22 Jan | 8.21% | 32.47% | +24.26 | 41.03% | 23.32% | -17.71 |
| 3 Feb | 1 Feb | 15.59% | 27.48% | +11.89 | 37.51% | 30.83% | -6.68 |
| **13 Feb** | **11 Feb** | **21.62%** | **26.65%** | **+5.03** | **38.82%** | **28.68%** | **-10.14** |
| 18 Feb | 21 Feb | 16.83% | 21.00% | +4.17 | 41.32% | 39.47% | -1.85 |
| 23 Feb | 21 Feb | 17.90% | 21.00% | +3.10 | 40.93% | 39.47% | -1.46 |
| 28 Feb | 3 Mar | 17.04% | 23.87% | +6.83 | 44.53% | 34.39% | -10.14 |
| 10 Mar | 8 Mar | 9.24% | 26.22% | +16.98 | 50.26% | 36.77% | -13.49 |

Swing within one February (vegetation): 2019 15.59-21.62% (6.03 points), 2025
25.08-32.19% (7.11), 2026 21.00-27.48% (6.48). Between years at 11-13 Feb: 21.62% (2019),
32.16% (2025), 26.65% (2026); 2025 -> 2026 alone is -5.51 points, and 2025 was greener
than 2026 on every matched January/February date. Bare proxy in February: 2019
37.51-44.53%, 2025 24.28-32.84%, 2026 28.68-39.47%.

Conclusion: **the 2019 -> 2026 difference in the headline pair (+5.0 points vegetation,
-10.1 points bare proxy at 20 m) is not bigger than the swing between dates in one
February (6-7 points vegetation, 7-11 points bare proxy) or between neighbouring years
(2025 -> 2026: -5.5 points vegetation).** The direction of the vegetation difference is
consistent (2026 greener at every matched pair, +3.1 to +24.3), but the bare-proxy drop
ranges from -17.7 to +0.9 depending on the pair and is only about -1.5 to -1.9 around
21 February. 13 Feb 2019 is also the greenest February 2019 date. The headline net changes
should **not** be quoted as land-cover change. Localised items (individual lakes, the
cluster list) are the more defensible outputs, after a look on the ground or in
high-resolution imagery.

## What differs from the Holenarasipur run

1. `config.json`: Byatarayanapura, AC 152, Bengaluru Urban, OBJECTID 2355, scenes,
   `robustness_tile` 43PGQ, `robustness_orbit` 19.
2. `fetch_osm.py`: four rounds over both Overpass endpoints with 0/30/60/120 s backoff;
   new cached query `osm_water_labels.json`.
3. `analyze.py`: Planetary Computer reads retried with 15/30/60 s backoff; unnamed water
   polygons can take a name from an OSM label feature (none did here); generic names not
   merged; named wetlands with no water polygon would be added (none here);
   `totals_measured_water_bodies` (water / green on lake / bare proxy over the union of
   measured outlines) and `named_lakes_checked_by_search` added to `metrics.json`;
   change-map canvas kept at least 1,150 px wide so the title and legend are not cut off
   (the map is 798 px wide here).
4. `robustness_check.py`: retries with backoff.
5. No change to thresholds, masks, offsets or the cluster method.

## Limits (read before quoting any number)

1. **One day per year**; the date check shows date and year swings as large as the
   headline change.
2. **The built-up proxy mixes buildings with bare and dry ground**; its fall means the
   ground was greener on 11 Feb 2026, not that buildings went away.
3. **Thresholds are textbook values**, not calibrated for Bengaluru.
4. **Different satellites and processing** (2A in 2019, 2B in 2026; baselines 02.12 vs
   05.12; -1000 offset applied only to 2026).
5. **Boundary accuracy**: DataMeet polygon, may be shifted; Allalasandra Lake falls just
   outside it, Jakkur and Nagawara lakes cross it, Hebbal Lake sits at its southern edge.
6. **Lakes**: weed cover counts as vegetation; clearing weeds turns green into water;
   outlines are current OSM; water bodies under 2 ha not measured; overlapping OSM
   features can double count in per-lake rows (not in the union totals).
7. **Clusters** are spectral change only (5-17 ha for the 15 largest).

## Files

`config.json`, `extract_boundary.py`, `search_scenes.py`, `fetch_osm.py`, `analyze.py`,
`robustness_check.py`, `page_notes.json`; outputs `metrics.json`,
`truecolor_2019_2026.png`, `change_map_2019_2026.png`, `clusters.png`, `field_checks.csv`,
`DRAFT_byatarayanapura_scorecard.html` (from `../make_rural_page.py`); data in `data/`
(`candidates.json`, `search_log.txt`, `osm_water_all.json`, `osm_forest_protected.json`,
`osm_water_labels.json`, `osm_name_probe.json`, `osm_query_log.json`,
`robustness_dates.json`, `robustness_log.txt`, `run_log.txt`,
`boundary/byatarayanapura_ac152.geojson`).
Run order: extract_boundary, search_scenes, fetch_osm, robustness_check, analyze, then
`py research/satellite/make_rural_page.py research/satellite/byatarayanapura`.
Contains modified Copernicus Sentinel data (2019, 2026).
