# DRAFT: Rural roads by Assembly seat, Pragathi Patha and 2025-26 releases (25 Nov 2026)

Two scanned Assembly answers, each read twice independently (the second reading blind): Pragathi Patha matches on all 224 rows; the 2025-26 release amounts match as a set (189 values, Rs 1,396.50 cr), with seat pairing from the first reading.

## Sources
1. **Pragathi Patha allocation.** Legislative Assembly unstarred question 654, answered 10 Dec 2025, Annexure-1 (pp. 2-12, English, signed 30.5.2025): km of rural road and Rs crore allotted to each Assembly constituency. https://kla.kar.nic.in/assembly/answers/16assembly/pdf/10122025/654.pdf . Page 1: approved on 2 Jul 2024 for 189 rural constituencies at Rs 5,190 crore; Rs 100 crore earmarked in the 2025-26 budget; DPRs being prepared. Allocations, not releases.
2. **Rural road releases.** Unstarred question 2844, answered 18 Mar 2026, pp. 83-95: releases per constituency under head 5054-03-337-0-75 (general), Rs lakh, for 2023-24, 2024-25 and 2025-26 to date. https://kla.kar.nic.in/assembly/answers/16assembly/pdf/18032026/2844.pdf . The head is not printed on pp. 92-95; it is inferred from the table's position.

## Checks
- Pragathi Patha: 224 rows; km sums to exactly the printed 5,400.00 and all 31 district subtotals match. Crore sums to 3,936.74 against a printed 3,936.06 (rounding: every row is 0.7289 crore per km). The scan is skewed by about one row on alternate pages; values were paired with names by order within each district, confirmed by the district subtotals.
- 2025-26 releases: 189 rows (the 189 rural seats); no printed total.

## Findings
**Pragathi Patha (km allotted per seat)**

| Party of the seat | 30 km (Rs 21.87 cr) | 22 km (Rs 16.04 cr) | Other |
|---|---|---|---|
| Congress (137) | 125 | 1 (Channapatna) | 10 at 0 km (fully urban), Manvi 7 km (limited by road length) |
| BJP (65) | 0 | 50 | 12 at 0 km (urban), 3 limited (Mangalore City North 4, City South 19, Shimoga 6) |
| JD(S) (18) | 1 (Hagaribommanahalli) | 17 | - |
| Independents (2), KRPP, SKP | 0 | 4 | - |

- The split holds in every region. The exceptions run both ways: Channapatna (Congress since the Nov 2024 by-election) got 22 km; Hagaribommanahalli (JD(S)) got 30 km. Independents and the two MLAs the BJP expelled in May 2025, who got Rs 50 crore under the CM's infrastructure grant, got 22 km here.
- Gulbarga Uttar gets 30 km although its printed rural road length is 24.76 km and it is not marked "limited".
- Same seat-tiering as the CM's infrastructure grant (CM_GRANTS_BY_SEAT_DRAFT.md): ruling-party seats get the higher tier.

**Rural road releases (head 5054-03-337-0-75)**
- 2023-24 and 2024-25: not tiered by party (medians over the two years: Congress Rs 10.2 cr, BJP Rs 12.8 cr, JD(S) Rs 12.4 cr); probably payments on works sanctioned earlier. About Rs 46 cr sits in rows naming several seats or a taluk and is left unallocated.
- 2025-26 to date: tiered. Median seat: Congress Rs 7.4 cr (121 seats, Rs 1,065.7 cr), BJP Rs 4.0 cr (46, Rs 218.1 cr), JD(S) Rs 3.6 cr (18, Rs 74.0 cr). Congress higher in every region. Devadurga (JD(S)) Rs 0.
- Not yet checked: overlap with the CMIDP RDPR releases tabulated separately on pp. 147-150 of the same answer. Do not add the two.

## What this does and does not show
- Pragathi Patha: the government's own allocation gives seats held by the ruling party 30 km of rural road and opposition seats 22 km. It is an allocation, not money spent or roads built.
- Releases: the 2025-26 pattern is a pattern in money released, not a rule; earlier years show no such pattern.
- Not shown: anyone's personal gain. The public question is the same as for the CM's grants: should rural roads depend on who the voters elected?

## Files
- `pragathi_patha_allocation_by_seat.csv`: seat, MLA, party, region, km, crore, remark, CMIDP amount.
- `rural_roads_5054_releases_by_seat.csv`: seat, MLA, party, region, releases 2023-24, 2024-25, 2025-26 (Rs lakh), CMIDP amount.
