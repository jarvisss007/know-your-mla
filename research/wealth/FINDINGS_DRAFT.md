# DRAFT: What Karnataka MLAs declared, 2013 vs 2018 vs 2023

**Status: DRAFT research, not for the site until re-checked.** Built 24 Nov 2026 from myneta.info (ADR's transcription of the Election Commission affidavits). Every figure is self-declared by the candidate, covers the candidate plus spouse and dependants, and is a lead for checking against the scanned affidavit, not a finding about anyone's conduct.

Files in this folder: `affidavits_2013_2018_2023.csv` (one row per sitting MLA, all three affidavits, growth and checks), `MATCH_REVIEW.csv` (matches a person must confirm), and the scripts that produced them (`fetch_myneta.py`, `myneta_parse.py`, `match_affidavits.py`, `link_groups.py`, `build_wealth.py`, `analyze.py`, `make_findings.py`). Raw pages were cached outside the repo.

## Method

1. **Who.** The 224 rows of `data/mlas.csv`. The "2023" affidavit is the one that elected the sitting member: the May 2023 general election for 219, the Nov 2024 by-elections for Channapatna, Shiggaon and Sandur, and the Apr 2026 by-election for Bagalkot. Davanagere South's Apr 2026 winner (Samarth Shamanur Mallikarjuna) has no affidavit on myneta yet. K. J. George (Sarvagnanagar) is not on myneta for 2023; his 2023 totals come from the site's existing opencity figure, with no movable/immovable split.
2. **Candidate lists.** Every candidate myneta lists for Karnataka 2023, 2018 and 2013 (2,593 / 2,576 / 2,788 candidates; some list rows are hidden behind an obfuscated script on myneta and were decoded). One request a second.
3. **Matching.** Seats were matched by name (delimitation was 2008, so 2013 and 2018 use the same 224 seats; spellings such as Kaup/Kapu, Byndoor/Baindur, Karkal/Karkala were mapped by hand). Within the seat, names were compared after removing case, dots, titles and word order. Confidence: **exact** = same name, same seat; **probable** = a name variant in the same seat (initials expanded, spelling variant, a father's name added), where every word of the MLA's name is present; **uncertain** = anything else (a word of the MLA's name missing, which is how a father or son with the family name shows up; the same name in a different seat; two candidates that fit equally). Nothing uncertain is used in the rankings or medians.
4. **Second check.** Each MLA's myneta page has an "Other Elections" box, ADR's own grouping of a person's affidavits. It was read for every MLA and compared with the name match. Where it agreed with a same-seat name variant the match is probable; where it pointed to a different affidavit than an exact or probable name match, the match was downgraded to uncertain. Grouped affidavits from by-elections held between general elections (2019 to 2021) sit in the same myneta folders and were not used as "2018".
5. **Numbers.** From each matched page: total assets and liabilities (myneta's headline), movable and immovable totals (the affidavit's stated totals; where a stated total is nil but the itemised rows are not, the row sum, choosing the pair that reproduces the headline total), and the income shown in income-tax returns. The 2023 affidavits list five years of ITR income (FY2018-19 to FY2022-23 for most) for self, spouse and dependants; that five-year family sum is the "declared income" for 2018 to 2023. The 2018 and 2013 affidavits list a single year, so no income comparison is made for 2013 to 2018.
6. **Growth.** Change in total assets 2013 to 2018, 2018 to 2023 and 2013 to 2023, in crore and per cent; the change in movable and in immovable assets; the change in liabilities and in net worth (assets minus liabilities). Composition: "mostly immovable" when the immovable change is at least 60% of the total change, "mostly movable" likewise, else "mixed". Percentage rankings only include MLAs who started at Rs 1 crore or more (otherwise a Rs 20 lakh start dominates).
7. **Income test (2018 to 2023 only).** The phrase "growth larger than declared income would suggest" is used only where net worth rose by at least twice the family's five-year ITR income *and* by at least Rs 5 crore more than that income, and at least four ITR years are listed. Even then it is arithmetic, not a conclusion: affidavits value land differently across years, agricultural income is exempt and not in ITR "total income", and gifts and inheritance are not income.
8. **Add-up check.** Where the affidavit's stated movable, immovable or liability total differs from the sum of its itemised rows (as myneta transcribed them) by more than 10% and more than Rs 1 crore. This can be the candidate's arithmetic, a nil total line, or myneta's transcription; only the scanned affidavit settles it.

## Match counts

| Affidavit | exact | probable | uncertain (to review) | no match |
|---|---|---|---|---|
| 2023 | 221 | 1 | 1 | 1 |
| 2018 | 102 | 53 | 29 | 40 |
| 2013 | 76 | 46 | 39 | 63 |

Of the 155 usable 2018 matches, myneta's own grouping agrees with 145; of the 122 usable 2013 matches, it agrees with 112. "No match" mostly means the MLA did not contest that year (first-time candidates, or contested elsewhere under a name we could not tie). MATCH_REVIEW.csv has 71 rows for a person to decide. In the 2018 to 2023 comparison, 23 MLAs stood for a different party in 2018 than the one they sit with now; results by party use the current party.

## The overall picture

- Sitting MLAs with a usable 2018 and 2023 affidavit: **154**. Median declared assets 10.06 crore in 2018, 18.13 crore in 2023 (same people). Median change **+7.62 crore (69%)**.
- Of these, the rise was mostly immovable (land, buildings) for 81, mostly movable (cash, deposits, shares, loans given, vehicles, jewellery) for 22, mixed for 31; 20 declared less in 2023 than in 2018. Median movable change +1.84 crore, median immovable change +4.46 crore.
- With a usable 2013 affidavit too: 121 MLAs; median change 2013 to 2023 +12.89 crore (222%).
- The income test phrase applies to 53 MLAs (listed below); for most of them the rise is mostly immovable, where land revaluation alone can produce it.

## Largest increases, 2018 to 2023 (crore)

Amounts in Rs crore, as declared. "Family ITR income, 5 yrs" is the sum of income shown in returns by self, spouse and dependants in the 2023 affidavit.

| # | MLA (seat) | Party now | 2018 | 2023 | Change, crore | Change % | Movable change | Immovable change | Mostly | Family ITR income, 5 yrs | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | D K Shivakumar (Kanakapura) | Congress | 840.02 | 1,413.80 | 573.78 | 68% | 172.10 | 401.69 | mostly immovable | 143.54 cr | growth larger than declared income would suggest; an affidavit's totals do not add up (see below) |
| 2 | Munirathna (Rajarajeshwarinagar) | BJP | 43.72 | 293.60 | 249.88 | 572% | 23.24 | 226.64 | mostly immovable | 3.37 cr | not tested: the 2023 affidavit lists fewer than four years of ITR income |
| 3 | N. A. Haris (Shantinagar) | Congress | 190.25 | 439.21 | 248.96 | 131% | 52.59 | 196.37 | mostly immovable | 34.67 cr | growth larger than declared income would suggest |
| 4 | M.R. Manjunath (Hanur) | JD(S) | 110.82 | 316.68 | 205.86 | 186% | 11.42 | 194.44 | mostly immovable | 9.38 cr | growth larger than declared income would suggest (movable rise alone, net of new loans, also exceeds it) |
| 5 | S.N. Subbareddy (Bagepalli) | Congress | 157.57 | 313.62 | 156.05 | 99% | 60.32 | 95.73 | mostly immovable | 17.32 cr | growth larger than declared income would suggest (movable rise alone, net of new loans, also exceeds it) |
| 6 | Deshpande Raghunath (Haliyal) | Congress | 215.16 | 363.21 | 148.05 | 69% | 104.08 | 43.97 | mostly movable | 21.87 cr | growth larger than declared income would suggest (movable rise alone, net of new loans, also exceeds it); probable match |
| 7 | Priyakrishna (Govindarajanagar) | Congress | 1,020.54 | 1,156.84 | 136.30 | 13% | 74.57 | 61.73 | mixed | 3.53 cr | within declared income |
| 8 | Satish Laxmanrao Jarkiholi (Yemkanamardi (ST)) | Congress | 42.51 | 175.30 | 132.79 | 312% | 11.19 | 121.60 | mostly immovable | 10.45 cr | growth larger than declared income would suggest |
| 9 | K. Gopalaiah (Mahalakshmi Layout) | BJP | 10.78 | 110.65 | 99.86 | 926% | 9.79 | 90.07 | mostly immovable | 7.43 cr | growth larger than declared income would suggest; an affidavit's totals do not add up (see below) |
| 10 | D Sudakar (Hiriyur) | Congress | 41.35 | 135.69 | 94.35 | 228% | 74.10 | 20.25 | mostly movable | 2.09 cr | growth larger than declared income would suggest; probable match |
| 11 | Bhimanna T. Naik (Sirsi) | Congress | 31.22 | 122.97 | 91.75 | 294% | 17.45 | 74.31 | mostly immovable | 6.70 cr | growth larger than declared income would suggest; probable match |
| 12 | Rahim Khan (Bidar) | Congress | 12.90 | 83.84 | 70.94 | 550% | 3.14 | 67.80 | mostly immovable | 4.70 cr | growth larger than declared income would suggest |
| 13 | M Krishnappa (Vijayanagar) | Congress | 236.18 | 296.27 | 60.09 | 25% | 30.98 | 29.11 | mixed | 22.81 cr | growth larger than declared income would suggest |
| 14 | H K Suresh (Belur) | BJP | 380.95 | 435.31 | 54.36 | 14% | 24.09 | 30.27 | mixed | 23.26 cr | within declared income; an affidavit's totals do not add up (see below) |
| 15 | Samruddhi V. Manjunath (Mulbagal (SC)) | JD(S) | 5.78 | 59.70 | 53.92 | 932% | 3.22 | 50.70 | mostly immovable | 2.85 cr | growth larger than declared income would suggest; probable match |
| 16 | Mankal Vaidya (Bhatkal) | Congress | 11.80 | 64.24 | 52.45 | 445% | 14.14 | 38.30 | mostly immovable | 2.18 cr | growth larger than declared income would suggest; an affidavit's totals do not add up (see below) |
| 17 | H D Revanna (Holenarasipur) | JD(S) | 29.71 | 80.02 | 50.32 | 169% | 7.88 | 42.44 | mostly immovable | 13.55 cr | growth larger than declared income would suggest; probable match |
| 18 | S.S.Mallikarjun (Davanagere North) | Congress | 140.95 | 189.20 | 48.26 | 34% | 0.32 | 47.94 | mostly immovable | 28.73 cr | above declared income, but not clearly (margin small) |
| 19 | R. Ashoka (Padmanabanagar) | BJP | 40.63 | 87.35 | 46.73 | 115% | 8.58 | 38.15 | mostly immovable | 2.38 cr | growth larger than declared income would suggest |
| 20 | Dr M C Sudhakar (Chintamani) | Congress | 19.70 | 65.54 | 45.84 | 233% | 1.60 | 44.24 | mostly immovable | 5.93 cr | growth larger than declared income would suggest |

## Largest increases, 2018 to 2023 (per cent; 2018 assets at least Rs 1 crore)

| # | MLA (seat) | Party now | 2018 | 2023 | Change, crore | Change % | Movable change | Immovable change | Mostly | Family ITR income, 5 yrs | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Samruddhi V. Manjunath (Mulbagal (SC)) | JD(S) | 5.78 | 59.70 | 53.92 | 932% | 3.22 | 50.70 | mostly immovable | 2.85 cr | growth larger than declared income would suggest; probable match |
| 2 | K. Gopalaiah (Mahalakshmi Layout) | BJP | 10.78 | 110.65 | 99.86 | 926% | 9.79 | 90.07 | mostly immovable | 7.43 cr | growth larger than declared income would suggest; an affidavit's totals do not add up (see below) |
| 3 | Dr. Sharanprakash Rudrappa Patil (Sedam) | Congress | 3.80 | 28.71 | 24.91 | 655% | 2.76 | 22.14 | mostly immovable | 5.12 cr | growth larger than declared income would suggest; probable match |
| 4 | Munirathna (Rajarajeshwarinagar) | BJP | 43.72 | 293.60 | 249.88 | 572% | 23.24 | 226.64 | mostly immovable | 3.37 cr | not tested: the 2023 affidavit lists fewer than four years of ITR income |
| 5 | Rahim Khan (Bidar) | Congress | 12.90 | 83.84 | 70.94 | 550% | 3.14 | 67.80 | mostly immovable | 4.70 cr | growth larger than declared income would suggest |
| 6 | Manappa D Vajjal (Lingsugur (SC)) | BJP | 5.25 | 30.75 | 25.50 | 486% | 23.13 | 2.37 | mostly movable | 43.10 cr | within declared income |
| 7 | A.B. Ramesha Bandisiddegowda (Shrirangapattana) | Congress | 2.73 | 15.93 | 13.20 | 484% | 1.13 | 12.07 | mostly immovable | 1.90 cr | growth larger than declared income would suggest; an affidavit's totals do not add up (see below) |
| 8 | Anil Chikkamadhu (Heggadadevankote (ST)) | Congress | 2.64 | 14.94 | 12.30 | 466% | 1.87 | 10.44 | mostly immovable | 1.07 cr | growth larger than declared income would suggest (movable rise alone, net of new loans, also exceeds it); probable match; an affidavit's totals do not add up (see below) |
| 9 | K M Shivalingegowda (Arsikere) | Congress | 1.68 | 9.43 | 7.75 | 461% | 5.88 | 1.87 | mostly movable | 5.36 cr | within declared income |
| 10 | Mankal Vaidya (Bhatkal) | Congress | 11.80 | 64.24 | 52.45 | 445% | 14.14 | 38.30 | mostly immovable | 2.18 cr | growth larger than declared income would suggest; an affidavit's totals do not add up (see below) |
| 11 | Basanagouda Daddal (Raichur Rural (ST)) | Congress | 2.47 | 10.62 | 8.15 | 330% | 2.78 | 5.37 | mostly immovable | 4.57 cr | above declared income, but not clearly (margin small); probable match |
| 12 | C. Puttarangashetty (Chamarajanagar) | Congress | 3.39 | 14.15 | 10.75 | 317% | -0.09 | 10.84 | mostly immovable | 2.75 cr | within declared income |
| 13 | Satish Laxmanrao Jarkiholi (Yemkanamardi (ST)) | Congress | 42.51 | 175.30 | 132.79 | 312% | 11.19 | 121.60 | mostly immovable | 10.45 cr | growth larger than declared income would suggest |
| 14 | C N Balakrishna (Shravanabelagola) | JD(S) | 2.31 | 9.50 | 7.19 | 311% | 0.60 | 6.59 | mostly immovable | 0.94 cr | above declared income, but not clearly (margin small); an affidavit's totals do not add up (see below) |
| 15 | Bhimanna T. Naik (Sirsi) | Congress | 31.22 | 122.97 | 91.75 | 294% | 17.45 | 74.31 | mostly immovable | 6.70 cr | growth larger than declared income would suggest; probable match |
| 16 | K. Raghavendra Basavaraj Hitnal (Koppal) | Congress | 3.79 | 14.67 | 10.88 | 287% | 2.23 | 8.65 | mostly immovable | 2.47 cr | within declared income; probable match |
| 17 | T. Raghumurthy (Challakere (ST)) | Congress | 6.37 | 22.18 | 15.81 | 248% | 0.83 | 14.98 | mostly immovable | 6.74 cr | growth larger than declared income would suggest; an affidavit's totals do not add up (see below) |
| 18 | K S Anand (Kadur) | Congress | 1.38 | 4.63 | 3.26 | 236% | 0.58 | 2.68 | mostly immovable | 1.16 cr | above declared income, but not clearly (margin small) |
| 19 | Nemarajanaik.K (Hagaribommanahalli (SC)) | JD(S) | 2.99 | 10.01 | 7.02 | 235% | 0.52 | 6.50 | mostly immovable | 0.71 cr | above declared income, but not clearly (margin small) |
| 20 | Dr M C Sudhakar (Chintamani) | Congress | 19.70 | 65.54 | 45.84 | 233% | 1.60 | 44.24 | mostly immovable | 5.93 cr | growth larger than declared income would suggest |

## Largest increases, 2013 to 2023 (crore)

No income comparison: the 2013 and 2018 affidavits list one year of ITR income only.

| # | MLA (seat) | Party now | 2013 | 2018 | 2023 | Change, crore | Change % | Movable change | Immovable change | Mostly | Family ITR income, 5 yrs | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | D K Shivakumar (Kanakapura) | Congress | 251.51 | 840.02 | 1,413.80 | 1,162.29 | 462% | 213.07 | 949.22 | mostly immovable | n/a | an affidavit's totals do not add up (see below) |
| 2 | N. A. Haris (Shantinagar) | Congress | 133.76 | 190.25 | 439.21 | 305.45 | 228% | 73.69 | 231.76 | mostly immovable | n/a |  |
| 3 | Munirathna (Rajarajeshwarinagar) | BJP | 28.83 | 43.72 | 293.60 | 264.77 | 918% | 24.29 | 240.49 | mostly immovable | n/a |  |
| 4 | Deshpande Raghunath (Haliyal) | Congress | 113.93 | 215.16 | 363.21 | 249.28 | 219% | 210.89 | 38.39 | mostly movable | n/a | probable match |
| 5 | Priyakrishna (Govindarajanagar) | Congress | 910.99 | 1,020.54 | 1,156.84 | 245.85 | 27% | 119.63 | 126.22 | mixed | n/a |  |
| 6 | S.N. Subbareddy (Bagepalli) | Congress | 86.42 | 157.57 | 313.62 | 227.20 | 263% | 102.00 | 125.20 | mixed | n/a | probable match |
| 7 | M Krishnappa (Vijayanagar) | Congress | 147.43 | 236.18 | 296.27 | 148.83 | 101% | 44.19 | 104.64 | mostly immovable | n/a |  |
| 8 | Uday B. Garudachar (Chickpet) | BJP | 95.75 | 196.09 | 241.59 | 145.85 | 152% | 84.22 | 61.63 | mixed | n/a |  |
| 9 | S.S.Mallikarjun (Davanagere North) | Congress | 60.20 | 140.95 | 189.20 | 129.00 | 214% | 54.86 | 74.14 | mixed | n/a |  |
| 10 | Satish Laxmanrao Jarkiholi (Yemkanamardi (ST)) | Congress | 63.05 | 42.51 | 175.30 | 112.25 | 178% | -17.37 | 129.61 | mostly immovable | n/a | probable match |
| 11 | D Sudakar (Hiriyur) | Congress | 29.78 | 41.35 | 135.69 | 105.91 | 356% | 82.00 | 23.92 | mostly movable | n/a | probable match |
| 12 | K. Gopalaiah (Mahalakshmi Layout) | BJP | 7.18 | 10.78 | 110.65 | 103.47 | 1,441% | 11.86 | 91.61 | mostly immovable | n/a |  |
| 13 | M B Patil (Babaleshwar) | Congress | 40.16 | 104.89 | 141.31 | 101.15 | 252% | 10.99 | 90.15 | mostly immovable | n/a | probable match; an affidavit's totals do not add up (see below) |
| 14 | Sathish Reddy .M (Bommanahalli) | BJP | 42.96 | 87.00 | 122.50 | 79.53 | 185% | 29.65 | 49.88 | mostly immovable | n/a | an affidavit's totals do not add up (see below) |
| 15 | Rahim Khan (Bidar) | Congress | 6.99 | 12.90 | 83.84 | 76.85 | 1,099% | 4.12 | 72.73 | mostly immovable | n/a | probable match |
| 16 | B. A. Basavaraja (K.R. Pura) | BJP | 46.38 | 90.91 | 122.52 | 76.14 | 164% | 16.35 | 59.79 | mostly immovable | n/a | an affidavit's totals do not add up (see below) |
| 17 | Ramalinga Reddy (B.T.M Layout) | Congress | 35.94 | 66.62 | 110.68 | 74.74 | 208% | 28.67 | 46.07 | mostly immovable | n/a | an affidavit's totals do not add up (see below) |
| 18 | B.Z.Zameer Ahmed Khan (Chamrajapet) | Congress | 9.45 | 40.34 | 72.73 | 63.27 | 669% | 6.02 | 57.26 | mostly immovable | n/a |  |
| 19 | R. Ashoka (Padmanabanagar) | BJP | 26.21 | 40.63 | 87.35 | 61.15 | 233% | 9.34 | 51.81 | mostly immovable | n/a |  |
| 20 | Arvind Bellad (Hubli-Dharwad-West) | BJP | 48.06 | 75.20 | 106.57 | 58.51 | 122% | 19.74 | 38.77 | mostly immovable | n/a | probable match; an affidavit's totals do not add up (see below) |

## Largest increases, 2013 to 2023 (per cent; 2013 assets at least Rs 1 crore)

| # | MLA (seat) | Party now | 2013 | 2018 | 2023 | Change, crore | Change % | Movable change | Immovable change | Mostly | Family ITR income, 5 yrs | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | T. Raghumurthy (Challakere (ST)) | Congress | 1.34 | 6.37 | 22.18 | 20.85 | 1,559% | 4.45 | 16.39 | mostly immovable | n/a |  |
| 2 | K. Gopalaiah (Mahalakshmi Layout) | BJP | 7.18 | 10.78 | 110.65 | 103.47 | 1,441% | 11.86 | 91.61 | mostly immovable | n/a |  |
| 3 | Rahim Khan (Bidar) | Congress | 6.99 | 12.90 | 83.84 | 76.85 | 1,099% | 4.12 | 72.73 | mostly immovable | n/a | probable match |
| 4 | Munirathna (Rajarajeshwarinagar) | BJP | 28.83 | 43.72 | 293.60 | 264.77 | 918% | 24.29 | 240.49 | mostly immovable | n/a |  |
| 5 | Kashappanavara Vijayanand Shivashankrappa (Hungund) | Congress | 1.01 | 9.74 | 9.91 | 8.90 | 879% | 3.18 | 5.72 | mostly immovable | n/a | probable match |
| 6 | C. Puttarangashetty (Chamarajanagar) | Congress | 1.51 | 3.39 | 14.15 | 12.64 | 839% | 0.80 | 11.84 | mostly immovable | n/a |  |
| 7 | K. Raghavendra Basavaraj Hitnal (Koppal) | Congress | 1.60 | 3.79 | 14.67 | 13.07 | 819% | 2.59 | 10.48 | mostly immovable | n/a | probable match |
| 8 | S R Srinivas (Vasu) (Gubbi) | Congress | 1.91 | 5.58 | 17.27 | 15.36 | 805% | 4.49 | 10.87 | mostly immovable | n/a | probable match |
| 9 | Sharanabasappa Darshanapur (Shahapur) | Congress | 1.85 | 6.18 | 15.27 | 13.42 | 725% | 6.49 | 6.94 | mixed | n/a | probable match; an affidavit's totals do not add up (see below) |
| 10 | B.Z.Zameer Ahmed Khan (Chamrajapet) | Congress | 9.45 | 40.34 | 72.73 | 63.27 | 669% | 6.02 | 57.26 | mostly immovable | n/a |  |
| 11 | Dr. Sharanprakash Rudrappa Patil (Sedam) | Congress | 3.85 | 3.80 | 28.71 | 24.86 | 646% | 3.86 | 21.00 | mostly immovable | n/a | probable match |
| 12 | B. M. Nagaraja (Siraguppa (ST)) | Congress | 1.27 | n/a | 9.30 | 8.02 | 630% | 0.33 | 7.69 | mostly immovable | n/a | probable match |
| 13 | G.H. Srinivasa (Tarikere) | Congress | 2.34 | n/a | 15.70 | 13.36 | 570% | 1.75 | 11.61 | mostly immovable | n/a | an affidavit's totals do not add up (see below) |
| 14 | V Sunill Kumar (Karkala) | BJP | 1.20 | 2.92 | 7.98 | 6.78 | 565% | 2.56 | 4.22 | mostly immovable | n/a | probable match |
| 15 | H. K. Patil (Gadag) | Congress | 3.46 | 7.63 | 21.36 | 17.89 | 517% | 1.66 | 16.23 | mostly immovable | n/a | probable match |
| 16 | Kyathasandra N. Rajanna (Madhugiri) | Congress | 5.74 | 14.62 | 35.05 | 29.31 | 510% | 11.64 | 17.67 | mostly immovable | n/a | probable match |
| 17 | K M Shivalingegowda (Arsikere) | Congress | 1.57 | 1.68 | 9.43 | 7.86 | 499% | 5.90 | 1.96 | mostly movable | n/a |  |
| 18 | Siddu Savadi (Terdal) | BJP | 2.32 | 6.33 | 13.83 | 11.51 | 496% | 2.66 | 8.84 | mostly immovable | n/a | probable match |
| 19 | G B Jyothi Ganesh (Tumkur City) | BJP | 5.84 | 14.16 | 34.59 | 28.76 | 493% | -1.06 | 29.82 | mostly immovable | n/a |  |
| 20 | D K Shivakumar (Kanakapura) | Congress | 251.51 | 840.02 | 1,413.80 | 1,162.29 | 462% | 213.07 | 949.22 | mostly immovable | n/a | an affidavit's totals do not add up (see below) |

## Largest decreases

2018 to 2023 (all MLAs whose declared assets fell, largest first):

| MLA (seat) | Party now | 2018 | 2023 | Change | Movable change | Immovable change | Liabilities change |
|---|---|---|---|---|---|---|---|
| Jarkiholi Ramesh Laxmanrao (Gokak) | BJP | 122.79 | 49.27 | -73.52 | -12.22 | -61.30 | -3.01 |
| Santosh S Lad (Kalaghatgi) | Congress | 188.85 | 138.83 | -50.02 | -39.30 | -10.72 | -2.17 |
| Ravikumar Gowda (Ganiga) (Mandya) | Congress | 49.08 | 21.54 | -27.54 | -27.89 | 0.35 | 0.13 |
| Laxmi R. Hebbalkar (Belgaum Rural) | Congress | 28.79 | 13.18 | -15.61 | 1.17 | -16.78 | -1.11 |
| S. Muniraju (Dasarahalli) | BJP | 36.67 | 28.36 | -8.31 | 5.48 | -13.79 | 2.20 |
| Satish Krishna Sail (Karwar) | Congress | 63.73 | 56.84 | -6.88 | -11.11 | 4.23 | -6.16 |
| P.M.Narendraswamy (Malavalli (SC)) | Congress | 29.04 | 23.02 | -6.02 | 2.73 | -8.75 | 2.54 |
| Sharath Kumar Bachegowda (Hosakote) | Congress | 112.50 | 107.75 | -4.75 | 11.75 | -16.50 | -0.76 |
| Dr Y Bharath Shetty (Mangalore City North) | BJP | 16.09 | 11.39 | -4.70 | 1.45 | -6.15 | -0.36 |
| Bhojaraj (Aland) | Congress | 8.26 | 4.17 | -4.09 | -0.36 | -3.73 | -1.20 |
| Dr Ashwath Narayan C N (Malleshwaram) | BJP | 21.50 | 17.53 | -3.97 | -0.02 | -3.94 | -0.73 |
| C B Suresh Babu (Chikknayakanhalli) | JD(S) | 5.79 | 1.86 | -3.92 | -1.53 | -2.39 | -0.41 |
| Sharada Puryanaik (Shimoga Rural (SC)) | JD(S) | 5.17 | 3.01 | -2.16 | -1.58 | -0.58 | 0.32 |
| Eshwar Khandre (Bhalki) | Congress | 10.36 | 8.74 | -1.62 | 0.65 | -2.27 | -0.18 |
| K.Y.Nanjegowda (Malur) | Congress | 26.52 | 25.28 | -1.24 | -0.95 | -0.29 | 0.65 |
| M.T.Krishnappa (Turuvekere) | JD(S) | 3.36 | 2.14 | -1.22 | -0.19 | -1.03 | -0.17 |
| J. T. Patil (Bilgi) | Congress | 4.93 | 3.84 | -1.09 | -0.48 | -0.62 | 4.09 |
| Tanveer Sait (Narasimharaja) | Congress | 10.04 | 9.04 | -1.00 | -0.20 | -0.80 | -0.38 |
| Babasaheb Patil (Kittur) | Congress | 6.10 | 5.17 | -0.93 | 0.17 | -1.10 | 0.44 |
| B N Ravikumar (Sidlaghatta) | JD(S) | 2.30 | 2.26 | -0.04 | -0.19 | 0.15 | 0.00 |

2013 to 2023 decreases: Santosh S Lad (Kalaghatgi, Congress) 186.40 to 138.83 crore; Satish Krishna Sail (Karwar, Congress) 66.46 to 56.84 crore; Jarkiholi Ramesh Laxmanrao (Gokak, BJP) 57.94 to 49.27 crore; C B Suresh Babu (Chikknayakanhalli, JD(S)) 4.06 to 1.86 crore; M.T.Krishnappa (Turuvekere, JD(S)) 2.27 to 2.14 crore.

A fall can be a sale, a gift to a family member who is no longer a dependant, a lower valuation, or a debt written off; the affidavit does not say which.

## Where growth is larger than declared income would suggest (2018 to 2023)

Net worth change against the family's five-year ITR income in the 2023 affidavit. Affidavits value land differently across years (purchase cost in one, an estimate of market value in the next), agricultural income is exempt and not in these figures, and inheritance and gifts are not income. Read each row as "the arithmetic does not close on the declared figures alone", nothing more.

| MLA (seat) | Party now | Net worth change, crore | Family ITR income, 5 yrs, crore | Asset rise mostly | Movable rise net of new loans also exceeds income? |
|---|---|---|---|---|---|
| D K Shivakumar (Kanakapura) | Congress | 304.78 | 143.54 | mostly immovable | no |
| N. A. Haris (Shantinagar) | Congress | 229.86 | 34.67 | mostly immovable | no |
| M.R. Manjunath (Hanur) | JD(S) | 213.05 | 9.38 | mostly immovable | yes |
| Deshpande Raghunath (Haliyal) | Congress | 149.43 | 21.87 | mostly movable | yes |
| Satish Laxmanrao Jarkiholi (Yemkanamardi (ST)) | Congress | 131.82 | 10.45 | mostly immovable | no |
| S.N. Subbareddy (Bagepalli) | Congress | 117.29 | 17.32 | mostly immovable | yes |
| Rahim Khan (Bidar) | Congress | 70.09 | 4.70 | mostly immovable | no |
| M B Patil (Babaleshwar) | Congress | 56.60 | 23.04 | mostly immovable | no |
| Uday B. Garudachar (Chickpet) | BJP | 54.46 | 10.94 | mixed | yes |
| M Krishnappa (Vijayanagar) | Congress | 49.36 | 22.81 | mixed | no |
| Dr M C Sudhakar (Chintamani) | Congress | 49.13 | 5.93 | mostly immovable | no |
| Bhimanna T. Naik (Sirsi) | Congress | 45.68 | 6.70 | mostly immovable | no |
| K. Gopalaiah (Mahalakshmi Layout) | BJP | 42.62 | 7.43 | mostly immovable | no |
| H D Revanna (Holenarasipur) | JD(S) | 40.61 | 13.55 | mostly immovable | no |
| R. Ashoka (Padmanabanagar) | BJP | 40.09 | 2.38 | mostly immovable | no |
| N. Chaluvarayaswamy (Nagamangala) | Congress | 38.70 | 7.51 | mostly immovable | no |
| Samruddhi V. Manjunath (Mulbagal (SC)) | JD(S) | 36.57 | 2.85 | mostly immovable | no |
| Arvind Bellad (Hubli-Dharwad-West) | BJP | 36.31 | 16.31 | mostly immovable | no |
| Ramalinga Reddy (B.T.M Layout) | Congress | 24.40 | 11.95 | mostly immovable | no |
| C P Yogeeshwara (Channapatna) | Congress | 23.65 | 2.92 | mostly immovable | yes |
| G B Jyothi Ganesh (Tumkur City) | BJP | 22.29 | 0.37 | mostly immovable | no |
| B. A. Basavaraja (K.R. Pura) | BJP | 22.11 | 6.58 | mostly immovable | no |
| S R Vishwanath (Yelahanka) | BJP | 21.32 | 6.28 | mostly immovable | yes |
| Shivanand Patil (Basavana Bagevadi) | Congress | 20.49 | 3.92 | mostly immovable | no |
| Laxman Sangappa Savadi (Athani) | Congress | 20.13 | 3.29 | mostly immovable | no |
| T B Jayachandra (Sira) | Congress | 18.84 | 3.44 | mostly immovable | no |
| Mankal Vaidya (Bhatkal) | Congress | 18.76 | 2.18 | mostly immovable | no |
| T. Raghumurthy (Challakere (ST)) | Congress | 18.40 | 6.74 | mostly immovable | no |
| S.N. Narayanaswamy. K.M (Bangarapet (SC)) | Congress | 17.48 | 4.31 | mostly immovable | no |
| M.Chandrappa (Holalkere (SC)) | BJP | 17.31 | 2.00 | mostly immovable | yes |
| D.Vedavyasa Kamath (Mangalore City South) | BJP | 16.52 | 4.53 | mixed | yes |
| Balachandra Laxmanrao Jarkiholi (Arabhavi) | BJP | 16.37 | 1.26 | mostly immovable | no |
| Arabail Hebbar Shivaram (Yellapur) | BJP | 16.15 | 5.12 | mixed | yes |
| Dinesh Gundu Rao (Gandhinagar) | Congress | 15.75 | 2.00 | mostly immovable | no |
| H. K. Patil (Gadag) | Congress | 14.85 | 2.77 | mostly immovable | no |
| Anil Chikkamadhu (Heggadadevankote (ST)) | Congress | 13.24 | 1.07 | mostly immovable | yes |
| B.Z.Zameer Ahmed Khan (Chamrajapet) | Congress | 12.78 | 1.15 | mostly immovable | no |
| Basavaraj Rayareddi (Yelburga) | Congress | 12.07 | 2.15 | mixed | yes |
| Kyathasandra N. Rajanna (Madhugiri) | Congress | 11.89 | 3.32 | mostly immovable | no |
| Bharamgouda Alagouda Kage (Kagwad) | Congress | 11.58 | 3.43 | mixed | yes |
| A.B. Ramesha Bandisiddegowda (Shrirangapattana) | Congress | 11.23 | 1.90 | mostly immovable | no |
| Dr. Sharanprakash Rudrappa Patil (Sedam) | Congress | 10.65 | 5.12 | mostly immovable | no |
| B. Shivanna (Anekal (SC)) | Congress | 10.16 | 1.12 | mostly immovable | no |
| Appaji Aliyas Channabasavaraj S/O Shankarao Nadagouda (Muddebihal) | Congress | 10.00 | 0.87 | mostly immovable | no |
| Sharanabasappa Darshanapur (Shahapur) | Congress | 9.43 | 0.93 | mostly movable | yes |
| T.D.Rajegowda (Sringeri) | Congress | 9.05 | 0.85 | mixed | yes |
| Aihole Duryodhan Mahalingappa (Raybag (SC)) | BJP | 9.05 | 0.44 | mostly immovable | yes |
| D Sudakar (Hiriyur) | Congress | 8.26 | 2.09 | mostly movable | no |
| Koujalagi Mahantesh Shivanand (Bailahongal) | Congress | 8.07 | 1.13 | mostly movable | yes |
| Basawaraj Mattimudu (Gulbarga Rural (SC)) | BJP | 7.76 | 2.18 | mostly immovable | no |
| Yashavantaraygoud. Vittalagoud. Patil (Indi) | Congress | 7.19 | 1.02 | mostly immovable | no |
| C. C. Patil (Nargund) | BJP | 6.76 | 1.07 | mixed | yes |
| Raja Venkatappa Naik (Shorapur (ST)) | Congress | 6.04 | 0.75 | mostly immovable | yes |

## Affidavits whose totals do not add up

Stated total vs the sum of itemised rows, more than 10% and more than Rs 1 crore apart. Years used in the comparison only.

| MLA (seat) | Party now | Discrepancy |
|---|---|---|
| D K Shivakumar (Kanakapura) | Congress | 2023: liabilities stated 265.0693 cr vs rows add to 503.073 cr |
| K H Puttaswamy Gowda (Gauribidanur) | Independent | 2023: movable stated 990.4477 cr vs rows add to 11.8893 cr; 2023: immovable stated 276.586 cr vs rows add to 0.0 cr; 2023: liabilities stated 5.1006 cr vs rows add to 0.0 cr |
| H K Suresh (Belur) | BJP | 2023: movable stated 34.4929 cr vs rows add to 3.2185 cr; 2023: liabilities stated 12.6128 cr vs rows add to 47.5523 cr |
| C P Yogeeshwara (Channapatna) | Congress | 2018: liabilities stated 7.2807 cr vs rows add to 30.2807 cr |
| M B Patil (Babaleshwar) | Congress | 2023: liabilities stated 47.25 cr vs rows add to 25.5987 cr |
| Santosh S Lad (Kalaghatgi) | Congress | 2013: liabilities stated 9.1835 cr vs rows add to 14.0588 cr; 2018: liabilities stated 17.9172 cr vs rows add to 28.5669 cr; 2023: liabilities stated 22.4175 cr vs rows add to 26.3933 cr |
| K.C.Veerendra Puppy (Chitradurga) | Congress | 2023: movable stated 89.9545 cr vs rows add to 102.7323 cr |
| B. A. Basavaraja (K.R. Pura) | BJP | 2013: immovable stated 0.0 cr vs rows add to 26.1022 cr; 2013: liabilities stated 4.265 cr vs rows add to 5.5327 cr |
| Sathish Reddy .M (Bommanahalli) | BJP | 2013: movable stated 0.0 cr vs rows add to 9.7135 cr; 2018: movable stated 0.0 cr vs rows add to 23.8565 cr |
| Ramalinga Reddy (B.T.M Layout) | Congress | 2013: immovable stated 28.4744 cr vs rows add to 0.0 cr |
| K. Gopalaiah (Mahalakshmi Layout) | BJP | 2018: liabilities stated 3.7509 cr vs rows add to 5.3085 cr |
| Sharath Kumar Bachegowda (Hosakote) | Congress | 2018: immovable stated 79.5 cr vs rows add to 89.0 cr |
| Arvind Bellad (Hubli-Dharwad-West) | BJP | 2023: movable stated 25.4854 cr vs rows add to 21.0403 cr |
| H. A. Iqbal Hussain (Ramanagaram) | Congress | 2023: immovable stated 88.733 cr vs rows add to 0.0 cr |
| Ashok Kumar Rai (Puttur) | Congress | 2023: movable stated 4.9669 cr vs rows add to 26.8969 cr |
| Mankal Vaidya (Bhatkal) | Congress | 2018: movable stated 6.2819 cr vs rows add to 7.3824 cr |
| S R Vishwanath (Yelahanka) | BJP | 2013: immovable stated 0.0 cr vs rows add to 18.2122 cr; 2018: movable stated 0.0 cr vs rows add to 2.7118 cr; 2018: immovable stated 0.0 cr vs rows add to 40.4042 cr |
| Jarkiholi Ramesh Laxmanrao (Gokak) | BJP | 2013: liabilities stated 8.8366 cr vs rows add to 12.1106 cr; 2018: liabilities stated 40.1332 cr vs rows add to 46.4952 cr; 2023: liabilities stated 37.092 cr vs rows add to 43.4813 cr |
| Krishna Nayaka (Hadagali (SC)) | BJP | 2023: liabilities stated 0.0 cr vs rows add to 34.7172 cr |
| S. Raghu (C.V. Ramannnagar (SC)) | BJP | 2013: immovable stated 31.12 cr vs rows add to 27.8775 cr |
| A. Manju (Arakalgud) | JD(S) | 2023: immovable stated 25.8822 cr vs rows add to 31.2067 cr |
| Laxman Sangappa Savadi (Athani) | Congress | 2018: immovable stated 0.0 cr vs rows add to 12.99 cr |
| Shivanand Patil (Basavana Bagevadi) | Congress | 2018: immovable stated 5.84 cr vs rows add to 10.24 cr; 2023: movable stated 11.6642 cr vs rows add to 8.0752 cr; 2023: immovable stated 23.7271 cr vs rows add to 12.4565 cr |
| Asif (Raju) Sait (Belgaum Uttar) | Congress | 2023: movable stated 15.0167 cr vs rows add to 23.4016 cr |
| T.D.Rajegowda (Sringeri) | Congress | 2013: movable stated 16.7376 cr vs rows add to 12.8446 cr; 2018: immovable stated 0.0 cr vs rows add to 5.2436 cr; 2023: liabilities stated 4.6249 cr vs rows add to 10.4254 cr |
| Rajesh Naik U (Bantwal) | BJP | 2018: immovable stated 0.0 cr vs rows add to 23.3021 cr |
| Basanagouda R Patil (Yatnal) (Bijapur City) | BJP | 2013: liabilities stated 2.3755 cr vs rows add to 3.653 cr |
| M.Chandrappa (Holalkere (SC)) | BJP | 2018: movable stated 0.0 cr vs rows add to 1.3492 cr |
| K.Y.Nanjegowda (Malur) | Congress | 2018: liabilities stated 0.1318 cr vs rows add to 39.491 cr; 2023: liabilities stated 4.1157 cr vs rows add to 40.1423 cr |
| P.M.Narendraswamy (Malavalli (SC)) | Congress | 2013: immovable stated 0.0 cr vs rows add to 3.945 cr |
| T. Raghumurthy (Challakere (ST)) | Congress | 2018: liabilities stated 0.0 cr vs rows add to 14.4082 cr |
| Appaji Aliyas Channabasavaraj S/O Shankarao Nadagouda (Muddebihal) | Congress | 2023: liabilities stated 0.0 cr vs rows add to 1.6657 cr |
| Dr. G. Parameshwara (Koratagere (SC)) | Congress | 2023: immovable stated 11.6247 cr vs rows add to 4.8709 cr; 2023: liabilities stated 9.2318 cr vs rows add to 15.3909 cr |
| Shanthana Gowda.D.G. (Honnali) | Congress | 2018: immovable stated 0.0 cr vs rows add to 10.45 cr; 2023: immovable stated 14.1586 cr vs rows add to 17.5586 cr |
| A Kiran Kumar Kodgi (Kundapur) | BJP | 2023: immovable stated 9.8875 cr vs rows add to 6.4745 cr |
| Bharamgouda Alagouda Kage (Kagwad) | Congress | 2013: movable stated 1.1206 cr vs rows add to 2.3256 cr; 2018: movable stated 2.9775 cr vs rows add to 4.084 cr; 2023: movable stated 7.7984 cr vs rows add to 9.0034 cr |
| B Nagendra (Bellary (ST)) | Congress | 2018: liabilities stated 0.0 cr vs rows add to 4.3502 cr; 2023: liabilities stated 0.0 cr vs rows add to 3.7878 cr |
| Dr Ashwath Narayan C N (Malleshwaram) | BJP | 2013: movable stated 3.9979 cr vs rows add to 14.7479 cr |
| Tangadagi Shivaraj Sangappa (Kanakagiri (SC)) | Congress | 2023: immovable stated 9.1358 cr vs rows add to 6.5892 cr |
| Priyank Kharge (Chittapur (SC)) | Congress | 2023: movable stated 6.1969 cr vs rows add to 7.2026 cr |
| A.B. Ramesha Bandisiddegowda (Shrirangapattana) | Congress | 2023: immovable stated 13.6576 cr vs rows add to 15.4326 cr |
| G.K. Venkatashivareddy (Srinivasapur) | JD(S) | 2023: immovable stated 15.1625 cr vs rows add to 24.72 cr |
| G.H. Srinivasa (Tarikere) | Congress | 2023: immovable stated 0.0 cr vs rows add to 13.3563 cr |
| Sharanabasappa Darshanapur (Shahapur) | Congress | 2013: movable stated 0.6819 cr vs rows add to 2.0317 cr; 2013: immovable stated 1.1699 cr vs rows add to 3.9437 cr; 2013: liabilities stated 0.4477 cr vs rows add to 1.777 cr |
| Anil Chikkamadhu (Heggadadevankote (ST)) | Congress | 2018: immovable stated 0.0 cr vs rows add to 2.1354 cr |
| Aihole Duryodhan Mahalingappa (Raybag (SC)) | BJP | 2018: movable stated 0.0 cr vs rows add to 2.0196 cr; 2018: immovable stated 0.0 cr vs rows add to 3.2937 cr |
| Laxmi R. Hebbalkar (Belgaum Rural) | Congress | 2023: liabilities stated 5.6869 cr vs rows add to 6.8864 cr |
| Roopa Kala. M (Kolar Gold Field (SC)) | Congress | 2023: immovable stated 2.54 cr vs rows add to 1.44 cr |
| Yashavantaraygoud. Vittalagoud. Patil (Indi) | Congress | 2023: immovable stated 9.1708 cr vs rows add to 5.9986 cr |
| Umesh Hullappa Meti (Bagalkot) | Congress | 2023: immovable stated 0.0 cr vs rows add to 9.79 cr |
| Prabhu Chavan (Aurad (SC)) | BJP | 2013: movable stated 0.0 cr vs rows add to 1.9267 cr; 2013: immovable stated 2.113 cr vs rows add to 0.5 cr; 2018: immovable stated 0.0 cr vs rows add to 7.8983 cr |
| Nayana Motamma (Mudigere (SC)) | Congress | 2023: liabilities stated 3.3292 cr vs rows add to 1.6472 cr |
| K Shadakshari (Tiptur) | Congress | 2013: movable stated 0.0 cr vs rows add to 1.0332 cr; 2013: immovable stated 0.0 cr vs rows add to 1.15 cr |
| C N Balakrishna (Shravanabelagola) | JD(S) | 2018: liabilities stated 0.0 cr vs rows add to 1.1886 cr |
| Ravishankar D (Krishnarajanagara) | Congress | 2018: immovable stated 0.0 cr vs rows add to 5.68 cr; 2023: liabilities stated 0.2102 cr vs rows add to 3.069 cr |
| B.K. Sanagameshwara (Bhadravathi) | Congress | 2013: immovable stated 1.5 cr vs rows add to 0.0 cr; 2013: liabilities stated 0.0 cr vs rows add to 1.5788 cr; 2018: movable stated 0.3703 cr vs rows add to 2.5303 cr |
| Yashpal (Udupi) | BJP | 2023: immovable stated 0.0 cr vs rows add to 2.65 cr |
| Gurupadagouda Sanganagouda Patil (Ron) | Congress | 2013: immovable stated 0.0 cr vs rows add to 1.95 cr; 2018: immovable stated 4.15 cr vs rows add to 3.05 cr; 2023: movable stated 1.8602 cr vs rows add to 0.3147 cr |
| Katakadhond Vitthal Dondiba (Nagthan (SC)) | Congress | 2018: immovable stated 1.7825 cr vs rows add to 2.7975 cr |
| Gopala Krishna Beluru (Sagar) | Congress | 2023: immovable stated 0.0 cr vs rows add to 1.52 cr |
| Dr. Shailendra Beldale (Bidar South) | BJP | 2013: immovable stated 0.0 cr vs rows add to 1.2584 cr |
| Basavaraj Neelappa Shivannanavar (Byadgi) | Congress | 2023: immovable stated 1.24 cr vs rows add to 2.8 cr |
| Doddanagouda Hanamagouda Patil (Kushtagi) | BJP | 2018: immovable stated 0.0 cr vs rows add to 1.148 cr |
| B N Ravikumar (Sidlaghatta) | JD(S) | 2018: immovable stated 0.0 cr vs rows add to 1.5 cr |

## By party

Current party. Medians over MLAs with a usable affidavit in both years. Independents, KRPP and SKP members have no usable 2018 match.

| Party | MLAs | Median assets 2023 (all) | n, 2018 to 2023 | Median 2018 | Median 2023 | Median change, crore | Median change % | Median movable change | Median immovable change | Mostly immovable / movable / mixed / fell | Income-test phrase applies | n, 2013 to 2023 | Median change 2013 to 2023 | % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Congress | 137 | 17.63 | 96 | 10.66 | 17.97 | 7.77 | 71% | 1.83 | 4.26 | 53 / 13 / 18 / 12 | 36 | 73 | 13.36 | 252% |
| BJP | 65 | 19.68 | 44 | 9.83 | 25.93 | 9.44 | 61% | 2.63 | 5.21 | 21 / 8 / 11 / 4 | 14 | 38 | 12.57 | 186% |
| JD(S) | 18 | 9.76 | 14 | 5.48 | 9.76 | 5.46 | 56% | 0.53 | 4.03 | 7 / 1 / 2 / 4 | 3 | 10 | 7.69 | 188% |
| Independent | 2 | 637.16 | 0 | n/a | n/a | n/a | n/a | n/a | n/a | 0 / 0 / 0 / 0 | 0 | 0 | n/a | n/a |
| KRPP | 1 | 246.51 | 0 | n/a | n/a | n/a | n/a | n/a | n/a | 0 / 0 / 0 / 0 | 0 | 0 | n/a | n/a |
| SKP | 1 | 40.15 | 0 | n/a | n/a | n/a | n/a | n/a | n/a | 0 / 0 / 0 / 0 | 0 | 0 | n/a | n/a |
| ALL | 224 | 17.58 | 154 | 10.06 | 18.13 | 7.62 | 69% | 1.84 | 4.46 | 81 / 22 / 31 / 20 | 53 | 121 | 12.89 | 222% |

The party medians are close to one another; the differences are smaller than the spread inside each party, and the samples are small for JD(S). The same pattern (most of the rise in land and buildings) holds in every party.

## Caveats

- Self-declared figures, transcribed by myneta. Before anything is published about a named MLA, open the scanned affidavit on the Election Commission's site and check the totals by hand.
- Land is valued inconsistently: some affidavits give purchase cost, some an estimate of current market value, and the same plot can jump in value between affidavits with no transaction. Immovable growth is the least reliable part of these numbers.
- Totals include spouse and dependants, whose membership changes (a child who becomes independent drops out).
- Five years of ITR income is taxable income after deductions; it is not spending money, and agricultural income is exempt and absent.
- Nominal rupees, no inflation adjustment (prices rose roughly a third between 2018 and 2023).
- A match marked probable is a name variant in the same seat, usually confirmed by myneta's grouping; it is still not a document check.
- "Uncertain" and "no match" rows are left out of every ranking and median. That leaves out first-term MLAs and people who changed seats (for example Siddaramaiah, who contested Badami and Chamundeshwari in 2018 and Varuna in 2023), until a person confirms them.

## Needs a person

- **MATCH_REVIEW.csv (71 rows).** Each row has the candidate found, why it is uncertain, other candidates, myneta's grouping, and the page link. Several look like the same person under a different seat or spelling (Siddaramaiah 2018, A C Srinivasa, N Y Gopalakrishna, B Nagendra 2013, Madhu Bangarappa 2018, Nayana Motamma 2018, U T Khader 2013, Basavaraj Rayareddi 2013); several look like a relative who shares the family name and must not be used (B S Yediyurappa for Vijayendra, Umesh Katti for Nikhil Katti, Umesh Jadhav for Avinash Jadhav, K B Koliwad for Prakash Koliwad, M C Managuli for Ashok Managuli, Hullappa Meti for Umesh Meti); the rest need a look. Confirmed rows can then be re-run into the rankings.
- **K H Puttaswamy Gowda (Gauribidanur, Independent):** myneta's 2023 headline is Rs 1,267 crore, but the itemised rows it transcribed add to about Rs 12 crore movable and nothing immovable. Check the scan before using his figure anywhere.
- **D K Shivakumar 2023 liabilities:** stated Rs 265 crore, itemised rows add to Rs 503 crore on myneta.
- **Davanagere South:** no affidavit for the Apr 2026 by-election winner on myneta yet.
- **K. J. George:** 2023 from opencity (totals only); add the movable/immovable split from the scan.
- **Hiriyur and Dharwad:** `data/mlas.csv` still carries the members who died (Hiriyur, 10 May 2026) and were disqualified (Dharwad, from 15 Apr 2026); their rows are kept here as elected in 2023.
- **By-election winners** (Channapatna, Shiggaon, Sandur, Bagalkot): their "2023" column is the later by-election affidavit, so their 2018 to 2023 change actually runs to 2024 or 2026.
