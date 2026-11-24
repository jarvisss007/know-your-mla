# DRAFT: Bengaluru's lakes from space, February 2019 vs February 2026

Status: first-pass, unreviewed research for a non-partisan citizen site. Not for publication
until re-checked. This note describes only what two satellite pictures (and a set of extra
dates) show. It says nothing about who did or allowed anything, or why anything changed.

**How to read every number below.** More open water can mean weeds were cleared, the lake was
desilted, or it simply held more rain. Less open water can mean the lake dried, was covered
by weeds, or was encroached. The imagery cannot tell these apart. "Green on lake" is the area
inside the mapped lake outline that looks like living vegetation (NDVI > 0.4); on urban lakes
this is mostly floating weeds or reeds, which hide water from the water test. Read water and
green together.

## What was measured

- **Area**: the union of the 28 DataMeet Assembly Constituency outlines in Bengaluru Urban
  district, AC 150-177 (Yelahanka, K.R.Pura, Byatarayanapura, Yeshvanthapura,
  Rajarajeshwarinagar, Dasarahalli, Mahalakshmi Layout, Malleshwaram, Hebbal,
  Pulakeshinagar (SC), Sarvagnanagar, C.V. Raman Nagar (SC), Shivajinagar, Shanti Nagar,
  Gandhi Nagar, Rajaji Nagar, Govindraj Nagar, Vijay Nagar, Chamrajpet, Chickpet,
  Basavanagudi, Padmanaba Nagar, B.T.M Layout, Jayanagar, Mahadevapura, Bommanahalli,
  Bangalore South, Anekal (SC)), plus one DataMeet polygon in the same district that has no
  AC number or name (OBJECTID 2386, 970 ha, around 12.92-12.97 N, 77.62-77.66 E). It is a gap
  in the DataMeet layer, not a seat; it was kept so the city has no hole, and lakes in it are
  labelled "0 unnumbered DataMeet gap polygon". Union: 218,830 ha.
  (`data/boundary/bengaluru_urban_acs.geojson`, `data/boundary/bengaluru_urban_union.geojson`)
- **Lakes**: every OpenStreetMap polygon tagged `natural=water`, `water=lake|reservoir|pond`
  or `landuse=reservoir` in that area (Overpass, 24 Nov 2026, `data/osm_water_all.json`).
  Polygons tagged as river, stream, canal, drain, wastewater, basin and similar were left out
  (796). Same-named parts were merged only where they touch. 1,776 water bodies remain;
  **450 are 2 ha or larger and were measured**; 449 after one outline that sits entirely inside
  a larger one was set aside. 258 of the 450 carry a name in OSM (166 also a Kannada name).
- **Imagery**: Sentinel-2 L2A, tile 43PGQ, orbit R019, the same pair as the Byatarayanapura and
  Mahadevapura runs: 13 Feb 2019 (Sentinel-2A, baseline 02.12) and 11 Feb 2026 (Sentinel-2B,
  baseline 05.12, -1000 reflectance offset applied). Tile 43PGQ covers 100% of the union on both
  dates (`data/tile_coverage.json`), so no mosaic was needed.
- **Tests** (unchanged from `../byatarayanapura/analyze.py`): open water = MNDWI > 0; green on
  lake = NDVI > 0.4; SCL classes no data, saturated, cloud shadow, cloud medium/high, cirrus
  masked; 10 m grid. Each lake's row also gives the share of its pixels that were unmasked on
  each date (`valid_pct_2019`, `valid_pct_2026`).

## Counts

Over the union of the 449 lake outlines (6,657 ha; overlaps counted once):

| | 13 Feb 2019 | 11 Feb 2026 |
|---|---|---|
| Open water | 1,485.6 ha | 2,607.8 ha |
| Green on lake | 2,297.5 ha | 2,553.0 ha |
| Pixels unmasked | 98.55% | 99.98% |

Pixel by pixel, 1,536 ha became water and 414 ha stopped being water; 1,322 ha became green
and 1,066 ha stopped being green. Of the 408 lakes used in the rankings (see below), 180 show
more than 1 ha more water, 42 more than 1 ha less; 142 show more than 1 ha more green, 78 more
than 1 ha less. Hesaraghatta Lake alone accounts for 221 ha of the 1,122 ha net rise in water.

**Rankings use 408 lakes**: those with at least 90% of their pixels unmasked on both dates.
42 lakes were under 90% unmasked on 13 Feb 2019 (down to 48%; for example Haralur,
Hebbagodi, Dasarahalli Tank, Devasandra, Puttenhalli, Byrasandra lakes), against 99.1% or
more for every lake on 11 Feb 2026. Their rows are in `lakes.csv` but their changes are not
ranked. The mask on those 2019 pixels was not investigated further.

## Biggest changes in open water

Top 10 gains (ha of MNDWI water inside the OSM outline):

| Lake | Lat, lon | Outline ha | Water 2019 -> 2026 | Change | Green 2019 -> 2026 | Change | Seat (primary) |
|---|---|---|---|---|---|---|---|
| Hesaraghatta Lake | 13.16711, 77.49220 | 598.05 | 24.5 -> 245.4 | +220.9 | 216.3 -> 182.5 | -33.8 | 150 Yelahanka |
| unnamed, way/28069768 (tagged pond) | 13.17756, 77.68543 | 77.55 | 0.3 -> 64.0 | +63.8 | 11.7 -> 10.9 | -0.9 | 152 Byatarayanapura |
| Nagadasanahalli Lake | 13.16104, 77.57136 | 102.12 | 0.0 -> 63.0 | +62.9 | 31.2 -> 12.8 | -18.4 | 150 Yelahanka |
| Varthur Lake | 12.94835, 77.73926 | 154.32 | 40.3 -> 90.3 | +50.0 | 110.8 -> 54.3 | -56.6 | 174 Mahadevapura |
| Kakolu Lake | 13.19854, 77.51375 | 123.74 | 3.0 -> 46.5 | +43.5 | 75.2 -> 56.3 | -18.9 | 150 Yelahanka |
| Ramapura Kere | 13.04692, 77.68494 | 51.79 | 0.0 -> 38.1 | +38.1 | 51.4 -> 4.8 | -46.6 | 174 Mahadevapura (crosses into 151) |
| Doddanekundi Lake | 12.97532, 77.68823 | 36.69 | 0.3 -> 32.0 | +31.8 | 32.3 -> 0.6 | -31.8 | 174 Mahadevapura |
| Bagaluru Kere | 13.14006, 77.65811 | 52.89 | 2.6 -> 32.6 | +29.9 | 10.1 -> 0.5 | -9.6 | 152 Byatarayanapura |
| Dodda Gubbi Kere | 13.07669, 77.67297 | 38.54 | 0.5 -> 29.1 | +28.6 | 18.1 -> 2.3 | -15.8 | 174 Mahadevapura |
| Gummanahalli Lake | 13.13954, 77.68932 | 56.91 | 3.1 -> 30.9 | +27.8 | 2.1 -> 24.8 | +22.7 | 152 Byatarayanapura |

Top 10 losses:

| Lake | Lat, lon | Outline ha | Water 2019 -> 2026 | Change | Green 2019 -> 2026 | Change | Seat (primary) |
|---|---|---|---|---|---|---|---|
| Bellandur Lake | 12.93714, 77.67202 | 315.36 | 86.0 -> 43.1 | -42.9 | 220.8 -> 130.0 | -90.8 | 174 Mahadevapura (crosses; 22.6% in the gap polygon) |
| unnamed, relation/8415449 (tagged reservoir) | 12.97040, 77.33675 | 124.85 of 310.42 | 85.6 -> 55.4 | -30.2 | 1.5 -> 67.5 | +66.1 | 153 Yeshvanthapura (60% of the outline lies outside the area) |
| Muthanalluru Lake | 12.82263, 77.72900 | 108.53 | 45.9 -> 18.3 | -27.6 | 43.9 -> 87.0 | +43.1 | 177 Anekal (SC) |
| Kalkere Lake | 13.04830, 77.66424 | 48.65 | 37.6 -> 15.4 | -22.2 | 10.8 -> 39.2 | +28.4 | 151 K.R.Pura |
| Nagawara Lake | 13.04485, 77.60692 | 29.24 | 18.8 -> 0.0 | -18.8 | 9.4 -> 8.5 | -0.9 | 152 Byatarayanapura / 160 Sarvagnanagar (50/50) |
| Madiwala Lake | 12.90823, 77.61773 | 82.84 | 60.7 -> 46.0 | -14.7 | 12.5 -> 34.1 | +21.6 | 172 B.T.M Layout (crosses into 175) |
| Hennagara Lake | 12.77872, 77.66123 | 121.30 | 106.9 -> 94.1 | -12.8 | 8.0 -> 25.4 | +17.4 | 176 Bangalore South |
| Yellamallappa Chetty Lake | 13.02697, 77.72789 | 137.74 | 74.9 -> 62.3 | -12.6 | 62.9 -> 75.0 | +12.2 | 174 Mahadevapura (crosses into 151) |
| Gattahalli Lake | 12.87568, 77.69102 | 25.64 | 22.9 -> 13.7 | -9.2 | 0.3 -> 12.1 | +11.8 | 177 Anekal (SC) |
| unnamed, way/45921399 | 13.02138, 77.49520 | 17.39 | 8.4 -> 0.1 | -8.3 | 15.0 -> 7.6 | -7.4 | 153 Yeshvanthapura |

In most of the losses, green on lake rose by a similar amount (Muthanalluru, Kalkere,
Madiwala, Hennagara, Yellamallappa Chetty, Gattahalli, relation/8415449): the outline holds
less open water and more vegetation. Nagawara and way/45921399 are different: water fell
and green did not rise.

## Biggest changes in green on lake

Top 10 rises in green (NDVI > 0.4 inside the outline):

| Lake | Lat, lon | Green 2019 -> 2026 | Change | Water 2019 -> 2026 | Seat (primary) |
|---|---|---|---|---|---|
| unnamed, relation/8415449 | 12.97040, 77.33675 | 1.5 -> 67.5 | +66.1 | 85.6 -> 55.4 | 153 Yeshvanthapura |
| Muthanalluru Lake | 12.82263, 77.72900 | 43.9 -> 87.0 | +43.1 | 45.9 -> 18.3 | 177 Anekal (SC) |
| Sarjapur Doddakere Lake | 12.87136, 77.78136 | 29.7 -> 60.5 | +30.8 | 0.3 -> 4.1 | 177 Anekal (SC) |
| Kalkere Lake | 13.04830, 77.66424 | 10.8 -> 39.2 | +28.4 | 37.6 -> 15.4 | 151 K.R.Pura |
| Gummanahalli Lake | 13.13954, 77.68932 | 2.1 -> 24.8 | +22.7 | 3.1 -> 30.9 | 152 Byatarayanapura |
| unnamed, way/28069711 | 13.14129, 77.71444 | 10.3 -> 32.4 | +22.1 | 0.1 -> 8.7 | 152 Byatarayanapura |
| Madiwala Lake | 12.90823, 77.61773 | 12.5 -> 34.1 | +21.6 | 60.7 -> 46.0 | 172 B.T.M Layout |
| unnamed, way/41662642 | 13.21273, 77.53825 | 37.2 -> 57.4 | +20.2 | 0.0 -> 0.0 | 150 Yelahanka |
| unnamed, way/379036231 | 13.13693, 77.50344 | 6.4 -> 25.8 | +19.5 | 0.0 -> 6.6 | 150 Yelahanka |
| Hennagara Lake | 12.77872, 77.66123 | 8.0 -> 25.4 | +17.4 | 106.9 -> 94.1 | 176 Bangalore South |

Top 10 falls in green:

| Lake | Lat, lon | Green 2019 -> 2026 | Change | Water 2019 -> 2026 | Seat (primary) |
|---|---|---|---|---|---|
| Bellandur Lake | 12.93714, 77.67202 | 220.8 -> 130.0 | -90.8 | 86.0 -> 43.1 | 174 Mahadevapura |
| Varthur Lake | 12.94835, 77.73926 | 110.8 -> 54.3 | -56.6 | 40.3 -> 90.3 | 174 Mahadevapura |
| Ramapura Kere | 13.04692, 77.68494 | 51.4 -> 4.8 | -46.6 | 0.0 -> 38.1 | 174 Mahadevapura |
| Hesaraghatta Lake | 13.16711, 77.49220 | 216.3 -> 182.5 | -33.8 | 24.5 -> 245.4 | 150 Yelahanka |
| Doddanekundi Lake | 12.97532, 77.68823 | 32.3 -> 0.6 | -31.8 | 0.3 -> 32.0 | 174 Mahadevapura |
| Rachenahalli Lake | 13.06246, 77.61241 | 30.3 -> 2.9 | -27.4 | 29.8 -> 31.8 | 152 Byatarayanapura |
| Shingena Agrahara Lake | 12.84587, 77.71764 | 33.7 -> 8.7 | -25.1 | 0.0 -> 12.6 | 177 Anekal (SC) |
| Kakolu Lake | 13.19854, 77.51375 | 75.2 -> 56.3 | -18.9 | 3.0 -> 46.5 | 150 Yelahanka |
| Nagadasanahalli Lake | 13.16104, 77.57136 | 31.2 -> 12.8 | -18.4 | 0.0 -> 63.0 | 150 Yelahanka |
| Dodda Gubbi Kere | 13.07669, 77.67297 | 18.1 -> 2.3 | -15.8 | 0.5 -> 29.1 | 174 Mahadevapura |

Several lakes swap green for water almost one for one (Ramapura Kere, Doddanekundi, Varthur,
Dodda Gubbi): on 11 Feb 2026 open water shows where vegetation showed on 13 Feb 2019.
Rachenahalli lost most of its green while its open water stayed about the same.

## Does the change hold across dates? (multi-date check)

`robustness_lakes.py` re-measured the 10 largest water changes, plus the 5 largest losses and
5 largest green changes not already in that list (13 lakes), on every Jan-Mar 2019, 2025 and
2026 acquisition of tile 43PGQ, orbit R019 (57 dates). A date counts for a lake only if at
least 95% of its pixels are unmasked. Full series: `data/robustness_lakes.json`; summary:
`robustness_lakes.csv`.

Open water, range over clean dates (ha) and verdict:

| Lake | Headline 2019 -> 2026 | Jan-Mar 2019 | Jan-Mar 2025 | Jan-Mar 2026 | Water verdict | Green verdict |
|---|---|---|---|---|---|---|
| Hesaraghatta Lake | 24.5 -> 245.4 | 5.1-40.6 (15 dates) | 212.5-280.1 (14) | 190.8-261.0 (13) | **holds** | does not hold |
| unnamed way/28069768 | 0.3 -> 64.0 | 0.0-1.5 (15) | 52.3-58.6 (12) | 52.3-64.8 (17) | **holds** | small change |
| Nagadasanahalli Lake | 0.0 -> 63.0 | 0.0-2.2 (15) | 40.7-58.8 (13) | 25.0-74.0 (15) | **holds** | does not hold |
| Varthur Lake | 40.3 -> 90.3 | 11.9-51.8 (16) | 7.6-28.4 (13) | 79.6-93.1 (13) | **holds** (2025 was lower than 2019) | **holds** |
| Kakolu Lake | 3.0 -> 46.5 | 0.0-5.4 (17) | 36.5-47.2 (14) | 37.6-48.7 (16) | **holds** | does not hold |
| Bellandur Lake | 86.0 -> 43.1 | 29.2-103.0 (17) | 35.8-73.2 (13) | 26.8-61.4 (14) | does not hold over Jan-Mar (see note) | mostly holds |
| Ramapura Kere | 0.0 -> 38.1 | 0.0-0.8 (17) | 1.9-10.1 (14) | 34.5-38.3 (15) | **holds** (2025 still near 2019) | **holds** |
| Doddanekundi Lake | 0.3 -> 32.0 | 0.0-3.1 (17) | 9.7-18.3 (14) | 28.4-32.7 (14) | **holds** | mostly holds |
| unnamed relation/8415449 | 85.6 -> 55.4 | 65.2-96.2 (14) | 58.8-117.5 (15) | 13.1-114.5 (16) | swings with the date | mostly holds |
| Bagaluru Kere | 2.6 -> 32.6 | 0.9-2.6 (16) | 0.0-43.5 (12) | 11.8-43.9 (15) | **holds** | does not hold |
| Muthanalluru Lake | 45.9 -> 18.3 | 29.4-57.7 (16) | 0.0-25.6 (13) | 0.0-23.1 (14) | **holds** | **holds** |
| Kalkere Lake | 37.6 -> 15.4 | 41.6-43.1 (7) | 16.8-33.8 (14) | 0.0-18.1 (15) | **holds** | does not hold |
| Nagawara Lake | 18.8 -> 0.0 | 16.6-19.4 (16) | 16.7-17.8 (12) | 0.0-18.1 (14) | holds from 6 Feb 2026 only (see note) | small change |

Verdict rules: **holds** = every clean 2026 date is on the same side of every clean 2019 date;
**mostly holds** = the 2026 median lies outside the 2019 range in the same direction, but some
single dates overlap; **does not hold** = the change depends on which dates are picked;
**small change** = headline change under 2 ha, not assessed. (The script's own label for
relation/8415449 water and for Nagawara water is "mostly holds"; the notes below explain why
they are described differently here.)

Notes:
- **The large rises in water hold.** Hesaraghatta, way/28069768, Nagadasanahalli, Varthur,
  Kakolu, Ramapura Kere, Doddanekundi and Bagaluru show more water on every clean 2026 date
  than on any clean 2019 date. For most, 2025 already looked like 2026; for Varthur, Ramapura
  Kere and Doddanekundi, 2025 was still close to 2019, so the change in those three shows up
  between the 2025 and 2026 seasons.
- **Losses holding across dates:** Muthanalluru (2025 and 2026 both far below 2019, green on
  lake roughly doubled) and Kalkere (only 7 clean 2019 dates).
- **Bellandur**: in January and early February, 2026 is consistently lower (2019: 80-103 ha;
  2026: 42-61 ha), but 2019 water fell through March to 29-52 ha, overlapping 2026. Green on
  lake is much lower in 2026 on most dates (median 142 vs 236 ha). Partly seasonal; the
  February-to-February comparison is not robust on its own.
- **Nagawara**: open water was 12-18 ha on every clean date up to 1 Feb 2026, about the same
  as 2019 and 2025, and 0-0.2 ha on every clean date from 6 Feb 2026 to 28 Mar 2026. The change
  is recent (between 1 and 6 Feb 2026) and green did not take its place. The imagery does not
  show what happened.
- **relation/8415449** (unnamed reservoir at the western edge, 60% of it outside the study
  area): water swings between 13 and 115 ha within 2026 alone; its headline loss should not
  be quoted.
- **Green on lake is less stable than water**: Hesaraghatta's green varied from 53 to 338 ha
  within Jan-Mar 2019. Single-date green figures are weaker than water figures.

## Per constituency

`by_constituency.csv`. Water and green are summed pixel by pixel over the part of each lake
outline that falls inside the seat (overlaps counted once); "Lakes" counts lakes whose
largest share is in that seat. Seven seats in the city core contain no measured lake of 2 ha
or more (Hebbal, Pulakeshinagar (SC), Gandhi Nagar, Rajaji Nagar, Vijay Nagar, Chamrajpet,
Jayanagar); three more hold only parts of lakes based in a neighbouring seat (Mahalakshmi
Layout, Shanti Nagar, Basavanagudi).

| AC | Seat | Lakes | Outline ha in seat | Water 2019 | Water 2026 | Green 2019 | Green 2026 |
|---|---|---|---|---|---|---|---|
| 150 | Yelahanka | 75 | 1,694.9 | 176.0 | 629.6 | 539.9 | 621.8 |
| 151 | K.R.Pura | 16 | 186.8 | 73.9 | 74.4 | 82.8 | 103.2 |
| 152 | Byatarayanapura | 50 | 734.3 | 133.7 | 392.5 | 197.8 | 245.2 |
| 153 | Yeshvanthapura | 60 | 692.3 | 316.3 | 314.1 | 125.5 | 225.8 |
| 154 | Rajarajeshwarinagar | 7 | 72.5 | 10.8 | 10.0 | 30.8 | 41.6 |
| 155 | Dasarahalli | 8 | 77.5 | 13.4 | 37.8 | 32.4 | 15.8 |
| 156 | Mahalakshmi Layout | 0 | 1.3 | 0.0 | 0.0 | 0.0 | 0.1 |
| 157 | Malleshwaram | 2 | 15.8 | 9.0 | 10.0 | 1.2 | 1.2 |
| 158 | Hebbal | 0 | 0 | - | - | - | - |
| 159 | Pulakeshinagar (SC) | 0 | 0 | - | - | - | - |
| 160 | Sarvagnanagar | 1 | 20.5 | 13.7 | 0.0 | 1.5 | 0.1 |
| 161 | C.V. Raman Nagar (SC) | 6 | 46.6 | 4.5 | 12.5 | 35.0 | 16.8 |
| 162 | Shivajinagar | 1 | 30.7 | 23.5 | 22.9 | 4.2 | 2.0 |
| 163 | Shanti Nagar | 0 | 0.9 | 0.0 | 0.0 | 0.3 | 0.7 |
| 164 | Gandhi Nagar | 0 | 0 | - | - | - | - |
| 165 | Rajaji Nagar | 0 | 0 | - | - | - | - |
| 166 | Govindraj Nagar | 1 | 4.8 | 0.0 | 2.2 | 1.7 | 0.7 |
| 167 | Vijay Nagar | 0 | 0 | - | - | - | - |
| 168 | Chamrajpet | 0 | 0 | - | - | - | - |
| 169 | Chickpet | 3 | 20.4 | 11.0 | 15.3 | 3.8 | 6.2 |
| 170 | Basavanagudi | 0 | 1.8 | 0.9 | 1.4 | 0.3 | 1.7 |
| 171 | Padmanaba Nagar | 1 | 4.0 | 2.1 | 3.0 | 0.5 | 0.6 |
| 172 | B.T.M Layout | 2 | 78.5 | 64.1 | 61.5 | 4.6 | 11.9 |
| 173 | Jayanagar | 0 | 0 | - | - | - | - |
| 174 | Mahadevapura | 62 | 1,093.9 | 255.1 | 446.6 | 522.0 | 353.2 |
| 175 | Bommanahalli | 6 | 102.1 | 19.1 | 22.1 | 52.0 | 54.8 |
| 176 | Bangalore South | 62 | 660.1 | 249.9 | 334.0 | 215.3 | 234.8 |
| 177 | Anekal (SC) | 86 | 1,046.8 | 108.6 | 217.6 | 379.5 | 565.6 |
| 0 | gap polygon (no AC) | 0 | 71.3 | 0.0 | 0.4 | 66.3 | 49.1 |
| | **All** | **449** | **6,657.5** | **1,485.6** | **2,607.8** | **2,297.5** | **2,553.0** |

Seat totals include the 42 lakes with a partly masked 2019 picture (seat-level unmasked share
is in the CSV; lowest: Malleshwaram 84.2% and Padmanaba Nagar 84.3% in 2019), so 2019 water
there may be undercounted. Seat totals are dominated by a few big lakes (Hesaraghatta is 598
of Yelahanka's 1,695 ha) and inherit their date sensitivity.

**31 lakes cross a seat boundary** (at least 5% of the outline in a second seat). Notable:
Bellandur (174: 73.5%, gap polygon 22.6%, 161: 3.6%), Yellamallappa Chetty (174 / 151),
Madiwala (172 / 175), Ramapura Kere (174 / 151), Jakkur (152 / 150), Ulsoor (162 / 161),
Nagawara (152 / 160, 50/50), Iblur (174 / 175, 51/49), Gangondanahalli (153 / 150, 50/50),
Hosakere (176 / 177). Full shares are in `lakes.csv` (`constituency_shares`).

## Limits

1. **Cause is unknown.** Every number is "what the pixel looked like". More water: weed
   clearance, desilting or rain. Less water: drying, weeds or encroachment. The imagery
   cannot separate these, and this study does not try.
2. **One date per year for the headline.** The multi-date check covers only 13 lakes; for the
   other 436, a change could be seasonal. Green on lake moves more between dates than water.
3. **Boundaries**: DataMeet outlines (2008 delimitation, inferred) with a known shift; one
   970 ha piece in the south-east has no AC number, and Bellandur Lake is 22.6% inside it.
   Lakes near a seat edge may belong to the neighbouring seat on the official map.
4. **OSM outlines** are volunteer-drawn and current-day; a lake drawn smaller today than in
   2019 makes any lost area invisible to this method. Lakes not mapped in OSM, or mapped under
   2 ha, are not counted. Two channel polygons without a river tag (Vrishabhavati,
   Nagarbhavi Thorai) are in the 450 because OSM tags them only as `natural=water`; one
   quarry-water polygon is too. Nine outlines extend outside the study area and are measured
   only inside it.
5. **2019 masking**: 42 lakes had 48-90% of pixels unmasked on 13 Feb 2019; they are kept in
   `lakes.csv` and seat totals but left out of the rankings.
6. **Thresholds** are textbook values (MNDWI > 0, NDVI > 0.4), not calibrated for Bengaluru
   lakes. Shallow, turbid or algae-covered water can fall either side of them.
7. **Different satellites and processing** (Sentinel-2A, baseline 02.12 in 2019; 2B, 05.12
   in 2026; offset applied to 2026 only).
8. **10 m pixels**: edges of small lakes are mixed pixels; a 2 ha lake is about 200 pixels.

## Files

- `config.json`; scripts `extract_boundary.py`, `fetch_osm.py`, `analyze_lakes.py`,
  `robustness_lakes.py` (run in that order; `robustness_lakes.py --resummarize` recomputes
  verdicts without reading imagery).
- `lakes.csv` (450 rows), `by_constituency.csv`, `robustness_lakes.csv`,
  `lakes_change_overview.png`.
- `data/`: `boundary/`, `tile_coverage.json`, `osm_water_all.json`, `osm_chunks/`,
  `osm_query_log.json`, `measured_lakes.geojson`, `lakes_metrics.json`,
  `robustness_lakes.json`, `run_log.txt`, `robustness_log.txt`.

Sources: Copernicus Sentinel-2 L2A via Microsoft Planetary Computer (contains modified
Copernicus Sentinel data 2019, 2025, 2026); (c) OpenStreetMap contributors, ODbL; DataMeet
Assembly Constituency boundaries, CC BY 2.5 India.