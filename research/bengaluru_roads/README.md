# DRAFT: Bengaluru road check (paid vs visible)

Status: first-pass research by the "Urban analysis with maps" session, started 16 Nov 2026. Not for the public site until a second check.

## Question

Bengaluru's corporation (BBMP, now the Greater Bengaluru Authority's corporations) pays contractors for road works. Can free satellite pictures show whether the road works that were paid for actually appear on the ground?

## Data

| File | What it is | Source |
|---|---|---|
| `data/bbmp_2024-25_work_orders_payments.csv`, `data/opencity_bbmp_05_*.csv`, `data/opencity_bbmp_06_*.csv` | Work orders and payments 2024-25 (198-ward file and the two other ward regimes) | OpenCity, dataset `bbmp-work-orders-and-payments-2024-25`, compiled from accounts.bbmp.gov.in |
| `data/bbmp_2025-26_*.csv` | Work orders and payments 2025-26 (198, 225, 243 wards and common wards) | OpenCity, dataset `bbmp-work-orders-and-payments-2025-26` (last updated 14 May 2026) |
| `data/opencity_bbmp_07..10_*.csv` | Ward- and constituency-level spend by category, 2018-2023 | OpenCity, dataset `bbmp-work-orders-categorised-2018-2023` |
| `data/payments.csv` | One row per payment line, parsed by `parse_orders.py` | derived |
| `data/roads.geojson` | Road centrelines for the pilot roads | OpenStreetMap via Overpass (`roads.py`) |
| `data/road_brightness.json` | Sentinel-2 visible brightness on each road by dry season, 2019-2026 | Microsoft Planetary Computer, Sentinel-2 L2A (`sat_roads.py`) |

Downloaded 16 Nov 2026 through a normal browser session (the site blocks scripts).

## Method

White-topping lays a concrete layer over an asphalt road. Concrete reflects far more visible light than asphalt, so a white-topped road should get clearly brighter in 10 m Sentinel-2 pictures from the year the concrete is laid. For each pilot road we take up to four cloud-free dry-season (January-April) scenes a year, keep the pixels within 5 m of the road's centreline, and record the median of their mean blue-green-red reflectance. Each road is also cut into 200 m pieces so we can see which stretches changed.

Limits: a 10 m pixel on a 15-30 m road also sees trees, parked vehicles and footpaths; tree canopy over a road can hide it entirely; asphalt laid over concrete would show the opposite change. A road that does not brighten is a question for a field visit, not proof that no work was done.

## Lead found while parsing (NOT a finding)

2,972 bill IDs appear two or more times with a different payment (RTGS) number and date; 2,872 of them match in every other field, including the net amount. 2,274 span the 2024-25 and 2025-26 files; the second listing is typically 7 to 12 months after the first. Summed, the repeats would be Rs 2,918.67 crore if each were a real payment. That size points to how the public view lists bills (re-listing, a new payment register, or the OpenCity compilation) rather than double payment, but this data cannot tell which. `data/repeated_bills.json` holds every case. Ask OpenCity how the files were compiled, and the corporation's accounts department what a second RTGS reference on the same bill means, before using it.

### Follow-up on the repeated bills (17 Nov 2026): almost certainly a one-time records event

- The payment (RTGS) numbering restarts in November 2024: April-October 2024 numbers run up to about 5,600, and from November 2024 they start again at 1. (It restarts again in October 2025.)
- Bills first listed between April and November 2024 are listed a second time 37-75% of the time, depending on the month. Bills first listed from December 2024 onwards are almost never listed again (0-2% a month, and 0% from August 2025).
- The second restart, in October 2025, produced no relisting.

So the repeats cluster around one change in November 2024, not a steady habit of paying bills twice. The likeliest readings: payments recorded in the old series were re-recorded in the new one, or payment advices issued in the old series were not credited and were issued again. Either way, most of these bills were probably paid once. Which listing reflects the money actually leaving the account cannot be told from this data, so **the Rs 2,918.67 crore figure must not be used**.

Questions to put (the owner sends them):
1. To OpenCity (data.opencity.in): were the 2024-25 and 2025-26 files scraped at different times, and does the public view show a bill again when its payment is re-issued?
2. To the accounts department of the Greater Bengaluru Authority (or by RTI): what changed in the payment register in November 2024, and for a sample of bill IDs listed twice (for example 604582, 613688, 632144 from `data/repeated_bills.json`), on which date was the money credited to the contractor?

## Result of the satellite pilot (16 Nov 2026): the method does not work at 10 m

Six roads with white-topping payments were tested (`data/road_brightness.json`). None got brighter in any year 2019-2026: no 200 m stretch rose by more than 0.03 in visible reflectance, and every road stayed between about 0.05 and 0.12.

The control failed too. Stretches that OpenStreetMap already tags as concrete are not brighter than the asphalt stretches next to them (CMH Road: concrete 0.082, asphalt 0.140 in 2026; Patalamma Temple Road: 0.067 vs 0.077). Street trees, building shadow, vehicles and footpaths dominate a 10 m pixel on these roads. **So Sentinel-2 can neither confirm nor rule out white-topping here, and none of these numbers should be read as "work not done".**

| Road (work code) | Paid, gross, each bill counted once | Bills dated | OSM surface tag today |
|---|---|---|---|
| Nagarabhavi 80 Feet Road, ORR to Kengunte Circle (303-23-000005) | Rs 15.45 cr | Mar 2023 - Jul 2025 | asphalt on all 6 ways |
| Jawaharlal Nehru Road, RR Nagar (303-23-000026) | Rs 20.49 cr | Nov 2023 - May 2025 | concrete (or untagged) |
| Taralabalu Road, RT Nagar (303-23-000008) | Rs 24.03 cr | Dec 2023 - Jul 2025 | mixed asphalt/concrete |
| 100 Feet Road Indiranagar, CMH Road, Inner Ring Road, balance portions (303-23-000004) | Rs 8.64 cr | May 2023 - Jan 2024 | concrete on most ways |
| Patalamma Temple Road (167-20-000089) | Rs 2.98 cr | Apr 2023 | mixed |

OSM tags are volunteer edits and can be years old, so the table is a list of places to look, not evidence. The one worth a visit first is Nagarabhavi 80 Feet Road: tagged asphalt throughout despite Rs 15.45 crore paid for white-topping.

## What would work instead

1. **Dated street-level photos.** Mapillary or KartaView pictures taken before and after the bill dates show concrete plainly. Both need a free account and API key (the owner's decision); or readers send dated photos through Have your say.
2. **Field visits** to the roads in the table, photographing the surface at each end and the middle with the date.
3. **Sub-metre imagery** (commercial) or Google Earth's historical imagery, viewed by a person. Google's terms do not allow automated extraction.

## Street photos (Mapillary, checked 17 Nov 2026)

`street_photos.py` lists every Mapillary photo within 20 m of each road (`data/street_photos.json`); `pick_photos.py` picks up to four per period, spread along the road, within 8 m (`data/photo_picks.json`, with a Mapillary link for each). Photos are judged by eye; images are not stored in this repo (Mapillary licence CC BY-SA; open them from the links). The access token lives only in the owner's home folder.

| Road | Photos within 20 m | Before the bills | After the bills | Reading |
|---|---|---|---|---|
| Nagarabhavi 80 Feet Road | 0 | none | none | **No coverage. First road for a field visit.** |
| JN Road, RR Nagar | 144 (2021-22 only) | dark asphalt in all 4 picked (Jan 2021, Aug 2022) | none | Before state is asphalt; after is unknown |
| Taralabalu Road | 58 | asphalt (Feb 2018, Mar 2021; the 2021 frame may be Bellary Road) | none within 8 m | Open |
| 100 Feet Road, Indiranagar | 6,542 (mostly 2016-18) | asphalt with patches (Jul 2022, one usable frame) | pale grey, concrete-looking surface at one junction under the metro (Sep 2026, 3 frames from one spot) | Consistent with white-topping at that spot only |
| CMH Road | 2,918 | none of the 4 picked shows the carriageway (metro platform, footpaths, rooftop) | pale grey, concrete-looking surface with yellow box markings (dashcam, Jul 2025 by its own overlay; Mapillary dates it 18 Aug 2025) | Consistent with white-topping on the stretch shown |
| Patalamma Temple Road | 211 | night photos (Aug 2022); surface type cannot be told | none | Open |

Nothing seen contradicts a payment. Two roads look consistent with concrete where photographed, three have no after-photos, and one has no photos at all. Picks were automatic and several "before" frames point away from the road; a person choosing frames road by road would do better, and the 2016-18 photos on Indiranagar and CMH Road can show which stretches were already concrete from the earlier phase.
