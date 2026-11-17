# Debts figures check (open issue in PROJECT_STATE, 16 Nov 2026)

Checked by the "Urban analysis with maps" session, read-only. No site data was changed.

## Result: the 12 mismatches are a definition difference, not wrong numbers

`data/liabilities_myneta.csv` vs `l` in `index.html`: 12 MLAs differ (PROJECT_STATE said 13; Hangal 3.04 vs 3.03 is rounding of myneta's headline).
The myneta candidate page has three liability figures:

1. "Grand Total of Liabilities (as per affidavit)": loans only (affidavit part i). This is `affidavit_total_cr`.
2. part i plus "Grand Total of all Govt Dues" (income tax, property tax, utility dues; affidavit part ii).
3. "Totals (Calculated as Sum of Values)": part i + part ii + liabilities the candidate lists as **in dispute**. This is myneta's headline, `myneta_total_cr`.

Our `l` matches figure 2 (loans + government dues, disputed excluded). Worked through on three pages read on 16 Nov 2026:

| Seat | Loans (part i) | Govt dues | Disputed | Our `l` | myneta headline |
|---|---|---|---|---|---|
| Kalaghatgi (id 7428) | 22.42 | 1.75 (income tax) | 2.23 | 24.17 = 22.42 + 1.75 | 26.39 |
| Malur (id 7541) | 4.12 | 0.44 | 35.60 | 4.55 = 4.12 + 0.44 | 40.14 |
| Muddebihal (id 6867) | 0.67 bank + 1.00 other liability | nil | nil | 1.67 | 1.67 |

- Muddebihal: myneta's affidavit "Grand Total" prints Rs 0 although the itemised rows add to Rs 1.67 crore. That is a myneta parsing error; our 1.67 is right.
- The other nine (Hanur, Ramanagaram, Bidar, Gokak, Sira, Gundlupet, Bellary (ST), Tiptur, Hangal) have `l` equal to myneta's headline, which suggests disputed amounts are nil for them and the gap to `affidavit_total_cr` is government dues. Not opened one by one.

## Suggested action (for the owning session)

- Keep `l`. Label it on report cards as "loans and government dues; disputed liabilities not included", and show disputed amounts separately where non-zero (Malur Rs 35.6 crore, Kalaghatgi Rs 2.23 crore).
- Before relying on the nine unopened seats, open each page and confirm disputed = nil.

## The 25 MLAs with no row

All 25 have an empty `id` in `D`, so `tools/fetch_liabilities.py` skips them (`if not d.get("id"): continue`). They are not parse failures. Fix: add their myneta candidate ids to `D`. Seats: Bagepalli, Davanagere South, Yemkanamardi (ST), Hukkeri, Padmanabanagar, Chintamani, Nippani, C.V. Ramannnagar (SC), Basavana Bagevadi, Bantwal, Bijapur City, Mandya, Gulbarga Uttar, Chittapur (SC), Raybag (SC), Hagaribommanahalli (SC), Humnabad, Madikeri, Nelamangala (SC), Badami, Bidar South, T. Narasipur (SC), Chincholi (SC), Hubli-Dharwad-Central, Sarvagnanagar.


## Second pass, 17 Nov 2026

### The nine seats not opened yesterday: all confirmed

Read on myneta on 17 Nov 2026. For each, our `l` = loans (affidavit part i) + government dues (part ii), and disputed liabilities are nil:
Hanur 61.16 + 0.07 = 61.23; Ramanagaram 8.61 + 0.22 = 8.83; Bidar 5.08 + 0.03 = 5.10 (rounding 5.11); Gokak 37.09 + 6.39 = 43.48; Sira 1.95 + 0.10 = 2.05; Gundlupet 16.28 + 0.59 = 16.87; Tiptur 3.94 + 0.84 = 4.78; Hangal 2.93 + 0.12 = 3.04 (myneta prints 3.03).

**Bellary (ST), B Nagendra: the CSV is wrong, the site is right.** His loans are nil; government dues are Rs 3.79 crore (income tax Rs 2.07 crore for AY 2010-11 and 2011-12, sales tax Rs 1.72 crore for 2007-11). `data/liabilities_myneta.csv` shows 2.07 as his affidavit total because `tools/fetch_liabilities.py` takes the first "Rs" after "Grand Total of Liabilities (as per affidavit)", and when that row is "Nil" the first Rs is the income-tax line. Fix for the owning session: treat a "Nil" grand total as 0 before searching for Rs (the same bug may affect any MLA whose part i is nil and part ii is not).

So all 12 mismatches are explained, and none of our 12 figures needs changing.

### myneta candidate ids for the MLAs missing one

Matched by constituency on myneta's 2023 winners list (https://www.myneta.info/Karnataka2023/index.php?action=show_winners&sort=default), 17 Nov 2026. Add to `D` (owning session) and re-run `tools/fetch_liabilities.py`.

| Seat | MLA in `D` | myneta id | Name on myneta |
|---|---|---|---|
| Bagepalli | S.N. Subbareddy | 7115 | S.N. Subbareddy (Chinnakayalapalli) |
| Davanagere South | Samarth Shamanur Mallikarjuna | 7225 | Shamanur Shivashankarappa |
| Yemkanamardi (ST) | Satish Laxmanrao Jarkiholi | 8416 | Satish Laxmanrao Jarkiholi |
| Hukkeri | Katti Nikhil Umesh | 7656 | Katti Nikhil Umesh |
| Padmanabanagar | R. Ashoka | 7628 | R. Ashoka |
| Chintamani | Dr M C Sudhakar | - | - |
| Nippani | Jolle Shashikala Annasaheb | 7624 | Jolle Shashikala Annasaheb |
| C.V. Ramannnagar (SC) | S. Raghu | 7163 | S. Raghu |
| Basavana Bagevadi | Shivanand Patil | 6775 | Shivanand Patil |
| Bantwal | Rajesh Naik U | 6931 | Rajesh Naik U |
| Bijapur City | Basanagouda R Patil (Yatnal) | 6944 | Basanagouda R Patil (Yatnal) |
| Mandya | Ravikumar Gowda (Ganiga) | - | - |
| Gulbarga Uttar | Kaneez Fatima | 9186 | Kaneez Fatima |
| Chittapur (SC) | Priyank Kharge | 7211 | Priyank Kharge |
| Raybag (SC) | Aihole Duryodhan Mahalingappa | 7731 | Aihole Duryodhan Mahalingappa |
| Hagaribommanahalli (SC) | Nemarajanaik.K | 8946 | Nemarajanaik.K |
| Humnabad | Siddu Patil | - | - |
| Madikeri | Dr. Mantar Gowda | 7523 | Dr. Mantar Gowda |
| Nelamangala (SC) | Shreenivasaiah N | 7619 | Shreenivasaiah N |
| Badami | B.B.Chimmanakatti | 7110 | B.B.Chimmanakatti |
| Bidar South | Dr. Shailendra Beldale | 7151 | Dr. Shailendra Beldale |
| T. Narasipur (SC) | Dr. H C Mahadevappa | 8348 | Dr. H C Mahadevappa |
| Chincholi (SC) | Avinash Umesh Jadhav | 7205 | Avinash Umesh Jadhav |
| Hubli-Dharwad-Central | Mahesh Tenginakai | 7771 | Mahesh Tenginakai |
| Sarvagnanagar | K. J. George | - | - |

- **Davanagere South: do not use 7225.** It is the 2023 winner, Shamanur Shivashankarappa; the sitting MLA in `D` is Samarth Shamanur Mallikarjuna, elected later, whose affidavit is in a by-election dataset on myneta, not Karnataka2023.
- Chintamani, Mandya, Humnabad and Sarvagnanagar are not on myneta's winners page (it lists 204 of 224 seats) and myneta's search did not find them. Open each constituency on myneta by hand.
