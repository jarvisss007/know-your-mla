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
