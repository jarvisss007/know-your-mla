# DRAFT: How old are the unpaid PWD bills? (22 Nov 2026)

Owner: officials / Follow the rupee lane. Figures below are re-derived from the spreadsheets; rerun the steps before quoting.

## Source

Karnataka Legislative Assembly, unstarred question 1485 (Sri Sunil Kumar V, Karkala), answered 24-08-2026 by the PWD Minister (signed Satish Jarkiholi), file no. ಲೋಇ/865/ಐಎಫ್‌ಎ/2026. Part 2 asks for the bills payable to contractors "as at the end of last July", district-wise and work-wise. The answer refers to Annexure-1, published only as an archive:
https://kla.kar.nic.in/assembly/answers/16assembly/pdf/24082026/1485.rar (18.45 MB, RAR5). Unpacked on 22 Nov 2026 with node-unrar-js in a scratch folder (Windows tar cannot read its Kannada file names).

Contents: zone-wise workbooks (Central, North, North-East, South), two National Highways workbooks, KRDCL and K-SHIP files and the signed answer sheet. Kannada text in the workbooks is in a legacy (Nudi-style) font encoding and shows as garbled characters; numbers, dates and English work names read normally.

Only two workbooks give a **date for each pending bill**:
- North zone (Belagavi): `NORTH/A-1 LAQ 1485 Sunil Kumar V July-2026 Work & DBR Wise Pending Bill.xlsx`. One sheet per account head; columns Sl No, Division, Name of Work, Contractor, Date, DBR No (divisional bill register), Bill Amount (Rs lakh).
- Chikkamagaluru division (Central zone): `CENTRAL/5. chikkamagalur.xlsx`, sheet "anu -2": head, work, estimate, contractor, B R number, B-R date, pending bill amount (Rs).

The other zones list works with amounts but no bill dates.

## Checks

- North zone: 4,770 dated bill rows parsed, Rs 1,809.20 crore. The workbook's own abstract sheet gives Rs 1,882.12 crore (188,212.19 lakh) across nine divisions. Parsed totals match the abstract exactly for Dharwad, Gadag, Sirsi, Belagavi, Chikkodi and Bagalkot; Haveri is Rs 0.10 crore short and Vijayapura Rs 4.64 crore short; Karwar has Rs 7.72 crore parsed against Rs 75.91 crore in the abstract (most Karwar rows carry no usable date). Coverage: 96% of the zone's pending value.
- 26 North rows have impossible dates (after July 2026, e.g. 2026-12-06, or 1993, 2000, and "5526-03-04"); most are Karwar entries that look day/month-swapped. They are excluded from the age figures (4,744 bills, Rs 1,807.53 crore remain).
- Ages are measured from the bill date to 31 July 2026 (the "end of July" in the question).

## Findings (North zone, nine divisions)

| Age of pending bill at 31 Jul 2026 | Bills | Rs crore | Share of value |
|---|---|---|---|
| under 6 months | 2,248 | 760.17 | 42.1% |
| 6-12 months | 967 | 492.21 | 27.2% |
| 1-2 years | 911 | 358.86 | 19.9% |
| 2-3 years | 445 | 148.53 | 8.2% |
| over 3 years | 173 | 47.76 | 2.6% |
| total | 4,744 | 1,807.53 | |

- 30.7% of the pending value (Rs 555 crore) was more than a year old; 173 bills were more than three years old.
- Oldest: three bills of March 2018 under the 2059 "sand" head in Belagavi division (Rs 9.49 lakh in all); one bill of Rs 188.16 lakh dated 24 Feb 2022 under state highway improvements, Belagavi.
- By account head: state highway improvements (5054 SH Impts) Rs 471.92 crore pending, 53% of it over a year old; district road improvements (5054 MDR Impts) Rs 662.10 crore, 22% over a year; district road maintenance (3054 MDR M) Rs 173.98 crore, 38%; flood repairs to district roads (3054 MDR M Flood) Rs 19.66 crore, 90%.
- 2,243 distinct contractor names appear (not published).

## Findings (Chikkamagaluru division)

740 dated bills, Rs 286.08 crore pending; Rs 92.17 crore (32.2%) more than a year old; 23 bills over three years; oldest dated 19 Mar 2021. One row with an impossible date excluded.

## What this does and does not show

- It shows how long bills have waited. The March 2026 answer (Q.3041) says bills are paid "by seniority and priority as grant allows".
- It does not show the order of payment: the annexure lists only bills still unpaid, not bills paid. Old bills may wait because their account head received no grant, not because newer bills were paid first. RTI letter 7 (rti.html) asks a division for the paid list with dates, which is what that test needs.
- Bill amounts are as printed; whether each is a full or part bill is not stated.

## Files

- `research/follow_the_money/pwd_north_pending_bills_jul2026.csv`: one row per North-zone bill (division, account-head sheet, date, DBR number, amount in lakh, date_ok, age_days). Contractor names and work names are left out.
