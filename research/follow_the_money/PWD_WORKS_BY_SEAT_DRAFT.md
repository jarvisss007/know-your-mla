# DRAFT: Which seats got the PWD's works, 2023-24 to 2025-26 (22 Nov 2026)

Owner: officials / Follow the rupee lane. Figures are re-derived from the spreadsheets; rerun the steps before quoting.

## Source

Same archive as the bill-age check: Assembly unstarred question 1485 (Sri Sunil Kumar V, Karkala), answered 24-08-2026 by the PWD Minister. Part (a) asks for the works the department took up in the last three years; the answer's Annexure-1 lists them division by division, each work with its **Assembly constituency**, account head, work name and **estimated cost** (Rs lakh). Archive: https://kla.kar.nic.in/assembly/answers/16assembly/pdf/24082026/1485.rar

Workbooks used (zone, file inside the archive):
- Central: Shivamogga, Chitradurga (the "Special Division" file is an exact duplicate and is skipped), Davanagere, Chikkamagaluru (four year sheets), Mangaluru, Udupi (sheet "Anubanda - 1 (2)").
- North-East (Kalaburagi): sheet "Annexure-1 (2023 to 2026)".
- North (Belagavi): sheets "Anu-1 2023-24" to "Anu-1 2026-27".
- South (Bengaluru): one sheet per division.
National Highways, KRDCL and K-SHIP files are not part of this count.

Most Kannada text is in a legacy (Nudi) font encoding. `tools/nudi.py` converts it to Unicode and transliterates it; each constituency name was then matched to the 224 seats in `data/mlas.csv`, by hand-checked alias table where the spelling differs (e.g. "Belagavi gramina" = Belgaum Rural, "Hosapete" = Vijayanagara, "Pandavapura" = Melukote).

## Checks

- Parsed counts and estimates match the zones' own abstract sheets closely: South Rs 2,086 crore parsed against Rs 2,116 crore in its abstract (795 works); North 2024-25 Rs 1,243 crore against Rs 1,239 crore, 2025-26 Rs 2,569 crore against Rs 2,560 crore. North 2023-24 is 292 rows against 230 in the abstract (Rs 465 crore against Rs 488 crore): not fully reconciled.
- Window: works listed for 2023-24, 2024-25 and 2025-26. 382 rows marked 2026-27 (Rs 1,285 crore) are left out. Shivamogga's file has no year column; its heading says 2023-24 to 2025-26.
- 7,081 works, Rs 11,379 crore in the window. 6,952 works (Rs 11,035 crore, 97%) map to a single seat. Not mapped: rows naming two seats, plain "Davanagere" (102 works; there are two Davanagere seats), plain "Kalaburagi", "Belagavi city", "Mysuru", Kadaba, Brahmavara and one New Delhi work.
- 199 of 224 seats appear. Missing: 20 Bengaluru city seats (city roads are not PWD's), Shimoga, Shimoga Rural, Bhadravathi, Bidar South and Srinivasapur.
- Amounts are **estimates of the works listed**, not money spent; some divisions include works only proposed (e.g. a Rs 100 crore Tungabhadra bridge at Kampli, sent for approval on 26 May 2026). One work can dominate a seat (Bailahongal's Rs 210 crore town bypass), so comparisons use medians.

## Findings

Party is the sitting MLA's (data/mlas.csv, by-elections included).

| Party of MLA | Seats in lists | Median per seat (Rs crore) | Total (Rs crore) |
|---|---|---|---|
| Congress | 128 | 56.1 | 8,124.8 |
| BJP | 51 | 33.5 | 2,350.5 |
| JD(S) | 16 | 19.7 | 387.0 |
| others (2 Ind, KRPP, SKP) | 4 | | 172.8 |
| all seats | 199 | 43.5 | 11,035.0 |

Same comparison inside each zone (median per seat, Rs crore):

| Zone | Congress | BJP | JD(S) |
|---|---|---|---|
| Central | 53.3 (20 seats) | 43.3 (15) | - |
| North | 66.2 (38) | 37.0 (17) | 37.0 (1) |
| North-East | 78.1 (27) | 36.8 (9) | 19.4 (3) |
| South | 26.0 (44) | 13.2 (10) | 18.9 (12) |

- In every zone the median Congress-held seat had more works listed than the median BJP-held or JD(S)-held seat. Leaving out works of Rs 50 crore or more does not change this (Congress 54.0, BJP 33.4, JD(S) 19.7).
- Top seats: Bailahongal Rs 300 crore (Congress; Rs 210 crore of it one bypass), Varuna Rs 210 crore (Congress; Siddaramaiah's seat, Chief Minister until May 2026), Sagar Rs 193 crore, Kampli Rs 192 crore, Shikaripura Rs 177 crore (BJP), Indi Rs 174 crore, Arabhavi Rs 160 crore (BJP), Baindur Rs 141 crore (BJP), Yemkanamardi Rs 141 crore (Congress, the PWD Minister's own seat, 9th of 199).
- Kanakapura (D.K. Shivakumar: Deputy Chief Minister until May 2026, Chief Minister since 3 June 2026) is 124th, Rs 36 crore.

## What this does and does not show

- It shows how the department's own lists spread estimated work value across seats, by the party holding each seat.
- It does not show favouritism by itself. Seats differ in road length, area, flood damage and population; works under the Chief Minister's and legislators' special programmes are included; the lists are estimates, some only proposed. A fair test would compare like with like (road kilometres per seat, needs surveys), which these lists do not contain.
- Different divisions filled the annexure differently (Shivamogga lists many small maintenance works; others only larger ones), which is why the zone tables matter.

## Files

- `research/follow_the_money/pwd_works_by_seat_2023_26.csv`: one row per seat (MLA, party, works, Rs crore, largest single work, rank).
- `research/follow_the_money/pwd_works_rows_2023_26.csv`: one row per work (zone, file, sheet, year, constituency as printed, matched seat, how matched, estimate in lakh). Work names left out to keep the file small; they are in the archive.
- `tools/nudi.py`: legacy Kannada font converter used to read the files.
