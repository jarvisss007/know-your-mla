# DRAFT: Chief Minister's grants by Assembly seat (24 Nov 2026)

Owner: Follow the rupee lane. Two scanned Assembly answers, transcribed twice independently (the second reading done blind); both readings agree on every one of the 346 amounts. Re-check against the PDFs before quoting a single seat.

## Sources

1. **CMIDP 2025-26.** Legislative Assembly unstarred question 1727, asked by Vithal Somanna Halagekar (Khanapur, BJP), answered 16 Dec 2025 by the Chief Minister (signed Siddaramaiah). https://kla.kar.nic.in/assembly/answers/16assembly/pdf/16122025/1727.pdf . Annexure-1 (pp. 2-13): "special grant given to Hon'ble MLAs in 2025-26 under the Chief Minister's Infrastructure Development Programme", amount per seat in Rs crore. Page 1: these are amounts sanctioned so far in 2025-26; releases are made by department and account head, and the Finance Department has no seat-wise release process. Khanapur: Rs 25 crore. Question 883 (17 Dec 2025, Rural Development Minister) describes the programme as a maximum of Rs 50 crore and a minimum of Rs 25 crore per seat.
2. **Chief Minister's special grant.** Unstarred question 1119, same member, answered 11 Mar 2025 by the Chief Minister. https://kla.kar.nic.in/assembly/answers/16assembly/pdf/11032025/1119.pdf . The question asks what was released to each seat in the last two years; the annexure (pp. 2-8, English) is headed as the total of works sanctioned under the CM's special grant in the last two years, Rs crore. Page 1: no works were sanctioned for Khanapur; future grants depend on resources, liabilities and regional need.

## Checks
- CMIDP: 203 rows, serials 1-203, Rs 8,567.00 crore (no printed total). 137 rows at 50, 62 at 25, and 40, 39, 37.5, 50.5. Row 73 prints an MLA's name ("Siddu Patil") instead of a seat: Humnabad.
- Special grant: 143 rows, Rs 3,885.00 crore (no printed total). Two seat names are blacked out in the PDF (Rs 25 crore each) and cannot be read.
- Party: the sitting MLA's party in data/mlas.csv (by-elections included). S.T. Somashekar (Yeshwanthapura) and A. Shivaram Hebbar (Yellapur) are listed as BJP there but were expelled by the BJP on 27 May 2025 (The News Minute, Deccan Herald), before the December 2025 answer.

## Findings

**CMIDP 2025-26 (sanctioned per seat)**

| Party of the seat | Seats listed | Amount |
|---|---|---|
| Congress | 135 of 137 | Rs 50 crore for 132; Rs 37.5-40 crore for Jevargi, Ranebennur, Basavana Bagevadi |
| BJP | 47 of 65 | Rs 25 crore for 44; Rs 50 crore for Padmanabhanagar (R. Ashoka, Leader of the Opposition) and for the two MLAs the BJP had expelled (Yeshwanthapura Rs 50 crore, Yellapur Rs 50.5 crore) |
| JD(S) | 17 of 18 | Rs 25 crore each |
| Independents (2), SKP | 3 | Rs 50 crore each |
| KRPP | 1 | Rs 25 crore |

- Not in the list (21 seats): 18 BJP seats (all five Udupi seats, Mangalore City North, Moodabidri, Bantwal, Belthangady, Belgaum Dakshin, Hubli-Dharwad-Central, Holalkere, Nargund, Shirahatti, Sakaleshpur, Tirthahalli, Basavakalyan, Chincholi), Devadurga (JD(S)), Mangalore (the Speaker's seat) and Varuna (the Chief Minister's own seat). The answer does not say why.
- In every region the median Congress seat had Rs 50 crore and the median BJP and JD(S) seat Rs 25 crore.

**CM's special grant (works sanctioned, two years before March 2025)**
- All 137 Congress-held seats are listed, most at Rs 25 crore. One BJP seat (Raichur), two independents and the SKP member are listed at Rs 25 crore; two more rows are blacked out. No JD(S) seat is listed.
- Largest: Channapatna Rs 150 crore, Sandur Rs 125 crore, Shiggaon Rs 100 crore (the three seats that held by-elections in November 2024; the list gives no sanction dates, so whether these came before or after the vote is not known), Mangalore Rs 35 crore.

## What this does and does not show
- It shows the government's own allocation rule as applied: seats held by the ruling party (and by members who backed it) got twice the CMIDP amount, and the CM's special grant went almost only to them.
- It does not show money spent: both lists are sanctions. It does not show any individual's wrongdoing. Discretionary grants are lawful; the question is whether citizens in opposition-held seats should get half.
- CMIDP money for roads may also appear in the PWD works list (Q.1485); do not add the two.

## Files
- `cm_infra_grant_cmidp_2025_26_by_seat.csv`: all 224 seats; serial, name as printed, seat, Rs crore, MLA, party, zone, whether listed.
- `cm_special_grant_by_seat.csv`: all 224 seats with the special-grant amount (0 if not listed) and the CMIDP amount.
