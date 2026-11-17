# DRAFT: the photo check on rural job scheme works almost never says no

Status: DRAFT, 17 Nov 2026, "Urban analysis with maps" session. Figures from an official public report; second check pending.

## What the official report shows

Source: Bhuvan GeoMGNREGA statistics report (NRSC/ISRO for the Ministry of Rural Development), https://bhuvan-app2.nrsc.gov.in/bhugram/usrtasks/nrega_phase2/get/stats.php, "Report generated on 2026-11-17 18:00:06". Snapshot saved: `data/bhuvan_geomgnrega_stats_2026-11-17.html`.

Every rural job scheme (MGNREGA) work is meant to be photographed with location at three stages: before, during and after. A moderator then accepts or rejects each photo. Karnataka:

| Stage | Photos submitted (total) | Yet to geotag | Accepted | Rejected | Rejected share | All-India rejected share |
|---|---|---|---|---|---|---|
| Phase I assets (older works) | 31,32,049 | 246 | 31,31,739 | 1 | 0.00003% | 0.003% |
| Before | 54,51,657 | 2,34,783 | 51,96,327 | 18,850 | 0.36% | 0.23% |
| During | 48,66,847 | 64,000 | 47,99,461 | 1,764 | 0.04% | 0.08% |
| **After (finished work)** | **43,13,996** | **46,265** | **42,48,542** | **419** | **0.010%** | **0.040%** |

- For finished works, moderators accepted 42.5 lakh photos and rejected 419: about 1 in 10,000, a quarter of the national rate. Madhya Pradesh rejects 0.20%, twenty times Karnataka's rate.
- Near-total acceptance is national, not only Karnataka's: across India, 0.04% of "after" photos are rejected.
- Karnataka has about 54.5 lakh "before" entries and 43.1 lakh "after" entries: roughly 11 lakh works have a before-photo record and no after-photo record. That fits the CAG's finding that most approved works were not completed, but this report cannot say which.

## Set against what auditors found on the ground

The CAG's performance audit of MGNREGS in Karnataka (Report No. 13 of 2025, 2019-20 to 2023-24; figures checked earlier in this project against the report text) test-checked a sample of gram panchayats and found:
- 163 completed work files with not a single geotagged photo of the asset;
- 275 works whose photos were not taken from the same angle or landmark, so the three stages could not be matched;
- three social forestry works in Yelburga taluk (Rs 34.55 lakh) "suspect" after comparing photos with satellite imagery.

In a small sample, auditors found hundreds of photo failures. Across the whole state, the moderation system rejected 419 "after" photos. The likeliest reading is that moderation checks that a photo exists and carries a location, not that it shows the finished asset at the right place.

## What this does not show

- It does not show any particular work is fake. Rejection rates measure the checking, not the works.
- The report gives no breakdown by district or year in the public view, so Karnataka cannot yet be split by district.

## Next

1. Spot-check a sample of "after" photos in one block on the public map (Yelburga, where the CAG found suspect works): does each photo show a finished asset, and does the satellite image at that point show it? Done by hand in a browser, a few panchayats at a time.
2. RTI to the state MGNREGA cell (Rural Development and Panchayat Raj): the moderation guidelines, who moderates "after" photos in Karnataka, and how many were reviewed per moderator per day.

## Spot check on the public map: Benakal panchayat, Yelburga block (17 Nov 2026)

Bhuvan-BHUGRAM public map, filters Karnataka > Koppal > Yelburga > Benakal, stage "Phase II (BDA): Assets": 22 points. Two opened in full (the map's own detail panel, read in a normal browser session):

| | Asset 1 | Asset 2 |
|---|---|---|
| Work | Desilting of Benakal village's big public tank, phase 2 | House construction for an individual beneficiary (PMAY-G convergence) |
| Work code | 1520004029/WH/93393042892194910 | 1520004029/IF/93393042892252060 |
| Work dates | started 7 Jun 2019, completed 1 Jan 2020 | started 28 May 2018, completed 1 May 2019 |
| Wages recorded | Rs 1,61,150, 706 person-days | Rs 17,168 |
| Work type field | "Individual Beneficiary" (for a public tank) | "Individual Beneficiary" |
| Photo record created | 13 Feb 2020, 15:10:51 | 13 Feb 2020, 15:32:54 |
| **Accepted by** | **GAS_YELBURGA** | **GAS_YELBURGA** |
| **Validated** | **13 Feb 2020, 16:03:12** | **13 Feb 2020, 16:02:18** |

What this shows:
- The photos were checked by the account "GAS_YELBURGA", by its name the block-level geotagging account, so the block that carries out the works also approves the proof that they were done. That reading of the account name needs confirming (RTI item below).
- Two unrelated works, a tank and a house, were approved 54 seconds apart, under an hour after upload. That pace fits clicking through a batch, not comparing three stages of photos with the record.
- The tank record calls a public tank "Individual Beneficiary" and gives its area as 0.00, both fields a reviewer would be expected to catch.

Two records are an illustration, not a sample. The map's own photo-point service did not respond to direct requests, and the detail panel can only be opened one point at a time, so a proper sample (say 50 works across 5 panchayats) needs either patient manual work or the data from the state.

## RTI to add (Rural Development and Panchayat Raj Department, MGNREGA cell; owner files)

1. Who operates the Bhuvan moderation accounts for Karnataka blocks (for example "GAS_YELBURGA"): designation and office, and whether they are the same officers who sanction and measure the works.
2. The moderation guidelines in force since 2019: what a moderator must check before accepting a stage-3 photo.
3. For Yelburga block, 2019-20 to 2024-25: the number of stage-3 photos accepted and rejected per moderator per day.
