# DRAFT: Mahadevapura (AC 174) from space, dry season 2019 vs 2026

Status: first-pass, unreviewed research. Not for the public site until re-checked.
All numbers live in `metrics.json`; this note explains how they were made and what
they can and cannot tell you.

## What was measured

Two cloud-free Sentinel-2 satellite pictures of the constituency, one from
February 2019 and one from February 2026, were compared pixel by pixel (each
pixel is 10 m x 10 m, i.e. 0.01 hectare). For each picture we counted:

- **Vegetation**: pixels where NDVI is above 0.4. NDVI compares near-infrared and
  red light; healthy green leaves score high. This captures tree canopy, parks,
  green crops and weeds on lakes alike; it cannot tell them apart.
- **Open water**: pixels where MNDWI is above 0. MNDWI compares green and
  short-wave-infrared light (Xu 2006). It is the headline water measure because
  it confuses less with concrete than the older NDWI. NDWI (McFeeters 1996,
  green vs near-infrared) above 0 is reported alongside for comparison.
- **Built-up / bare land (PROXY)**: pixels where NDBI is above 0, NDVI is below 0.2,
  and the pixel is not counted as water. NDBI compares short-wave-infrared and
  near-infrared light. This is a **proxy**: it also flags bare soil, ploughed or
  harvested fields, cleared plots, construction sites, rock and drained lake beds.
  Many real rooftops (white or metal) do *not* pass it. It is not a count of buildings.

The three categories are separate tests; a pixel can be in none (for example
sparse or mixed vegetation with NDVI 0.2-0.4), so they do not add up to 100%.

Areas are counted only on pixels that are cloud- and shadow-free in **both**
pictures (99.8% of the constituency), so the two years are compared on the same ground.

The change map colours a pixel green where it was vegetation in 2019 and is not
in 2026, blue where it was water and is not, and red where it was not built-up/bare
proxy in 2019 and is in 2026. The rest is the 2026 picture in dimmed grey.

## Results in brief (compared area 25,099 ha)

| | 13 Feb 2019 | 11 Feb 2026 | Net change |
|---|---|---|---|
| Vegetation (NDVI > 0.4) | 7,263 ha (28.9%) | 6,515 ha (26.0%) | -748 ha (-10%) |
| Open water (MNDWI > 0) | 383 ha (1.5%) | 665 ha (2.7%) | +283 ha (+74%) |
| Open water, NDWI > 0 (comparison only) | 358 ha | 518 ha | +160 ha |
| Built-up/bare PROXY | 8,176 ha (32.6%) | 7,978 ha (31.8%) | -197 ha (-2%) |

The built-up/bare proxy going slightly *down* does not mean less construction: bare
farmland in 2019 that was green or built on with bright roofs by 2026 leaves the
proxy, while new bare plots enter it (3,453 ha in, 3,650 ha out). It is the weakest
of the three measures. Of the pixels that newly entered it, 1,049 ha were vegetation in 2019.

Lakes: of 62 named OSM water bodies, 52 are 2 ha or larger and are measured in
`metrics.json`. Examples that a reader should check against the pictures: Bellandur
(inside part) MNDWI water 86 -> 42 ha, the lake bed looks pale/drained in the 2026
image; Varthur 40 -> 90 ha while its vegetation (weed cover) fell 111 -> 54 ha;
Doddanekundi, Ramapura and Dodda Gubbi Keres went from almost no open water (vegetation
covered) to 29-38 ha. Hoodi and Cheemasandra lakes showed water in 2019 and none in 2026.

## Data sources

- **Boundary**: DataMeet `maps` repository, `docs/data/geojson/ac.geojson`
  (https://github.com/datameet/maps), feature AC_NO 174 "Mahadevapura", Karnataka,
  PC 25 Bangalore Central. Licence CC BY 2.5 India. The constituencies were
  scraped from the Election Commission's polling-station site. Delimitation year:
  **2008** (inferred: Bangalore Central was created by the 2008 delimitation; the
  file's STATUS field marks only pre-delimitation states). DataMeet warns there is
  "some shift in the data"; the polygon has only 73 corners, so edges are
  approximate. Saved as `data/boundary/mahadevapura_ac174.geojson` (area 25,149 ha).
  The DataMeet ECI shapefile for Karnataka (`eci/AC_Data/States/S10`) was tried
  first and rejected: it is not georeferenced.
- **Imagery**: Copernicus Sentinel-2 Level-2A (surface reflectance), served free
  and without an account by Microsoft Planetary Computer
  (https://planetarycomputer.microsoft.com/api/stac/v1, collection
  `sentinel-2-l2a`; asset links signed with the anonymous token endpoint via the
  `planetary-computer` Python package).
  - 2019: `S2A_MSIL2A_20190213T050921_R019_T43PGQ_20201007T162011`, 13 Feb 2019,
    tile cloud 0.07%, 0.20% of the constituency masked.
  - 2026: `S2B_MSIL2A_20260211T050839_R019_T43PGQ_20260211T085923`, 11 Feb 2026,
    tile cloud 0.002%, 0.00% masked.
  - Choice: every Jan-Mar scene with under 20% tile cloud was scored by the cloud
    and shadow fraction inside the boundary (`data/candidates.json`). The pair was
    chosen from the same tile (43PGQ) and same orbit track (R019), two days apart in
    the calendar, to keep sun angle, season and viewing angle as similar as possible.
    The 2026 dry season had many clean scenes, so the 2025 fallback was not needed.
- **Lakes**: OpenStreetMap via the Overpass API (https://overpass-api.de),
  named `natural=water` features inside the boundary, queried 16 Nov 2026
  (`data/osm_named_water.json`). © OpenStreetMap contributors, ODbL. A later
  re-query timed out on both Overpass servers, so `analyze.py` reuses this saved response.

## Processing details

- Everything was put on one 10 m grid in UTM zone 43N (EPSG:32643). The 20 m
  short-wave-infrared band (B11) was resampled to 10 m (bilinear); the 20 m scene
  classification layer (SCL) by nearest neighbour.
- Cloud mask: SCL classes no-data, saturated, cloud shadow, cloud medium, cloud
  high and thin cirrus were excluded.
- Reflectance = (DN + offset) / 10000. ESA added an offset of -1000 to products from
  processing baseline 04.00 (January 2022) onward; it was applied to the 2026
  scene (baseline 05.12) and not to the 2019 scene (baseline 02.12). Skipping this
  step would bias every index between the years.
- Lake water area = pixels with MNDWI > 0 inside each OSM lake outline (clipped to
  the boundary). Lakes under 2 ha are listed but not measured.
- Code: `search_scenes.py` (scene search and scoring), `analyze.py` (everything
  else). Re-running them reproduces `metrics.json` and both PNGs.

## Limits (read before quoting any number)

1. **One picture per year.** Each year is a single day. A field that happened to be
   green on 13 Feb 2019 and freshly harvested on 11 Feb 2026 counts as "vegetation
   lost" and "new built-up proxy". In the farmland of the north and east this crop
   cycle produces much of the speckle on the change map. The gross transitions
   (about 3,250 ha of vegetation lost against 2,500 ha gained) are far larger than
   the net change, which is the sign of this noise.
2. **Seasonal and year-to-year weather.** Lake water in February depends on the
   previous monsoon; a wetter 2025 than 2018 alone could explain more water.
   Vegetation greenness also depends on recent rain.
3. **10 m pixels.** Roads, narrow tree lines, small ponds and buildings smaller than
   a few pixels are blurred into mixed pixels. Lakes under ~2 ha are not measurable.
4. **Thresholds are choices.** 0.4 for NDVI, 0 for MNDWI and NDBI are common
   textbook values, not calibrated for Bengaluru. Different thresholds give different
   hectares; the direction of change is more trustworthy than the exact figure.
5. **The built-up measure is a proxy.** It cannot tell a new apartment block from a
   ploughed field, a cleared plot or a drained lake bed. Dense older built-up areas
   often fail the NDBI test entirely. Do not quote it as "construction".
6. **Lake weeds and drained lakes.** A lake covered in water hyacinth counts as
   vegetation, not water; clearing the weeds turns "vegetation" into "water". A lake
   drained for desilting turns "water" into "bare/built-up proxy". Lake numbers need a
   look at the picture before interpretation.
7. **Two different satellites** (Sentinel-2A in 2019, 2B in 2026) and different ESA
   processing versions. They are designed to match, but small radiometric differences
   remain; the 2026 picture looks slightly brighter and greyer.
8. **Boundary accuracy.** The DataMeet polygon is approximate and may be shifted.
   80 ha of a 307 ha OSM lake named "Hosakote lake" (north-east edge, likely the
   Hoskote lake in Bengaluru Rural district) falls inside it; this should be checked against the official CEO Karnataka map
   before any lake figure near the edges is used. Bellandur Lake is split by the
   boundary and only its inside part is counted.
9. **OSM lake outlines** are volunteer-drawn, reflect today's mapping, and may be
   out of date or include the lake's dry margin.

## What this does not say

These numbers describe what the ground looked like to a satellite on two days.
They say nothing about who did or allowed any change, whether any change was legal,
or why it happened. Any such claim needs separate records.
