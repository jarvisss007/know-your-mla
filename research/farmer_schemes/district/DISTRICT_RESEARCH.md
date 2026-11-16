# DRAFT: District view, 2023-24 drought relief and PMFBY crop insurance

Status: DRAFT research, not for the site until re-checked. Compiled 16 Nov 2026 from outside India (about 22 web lookups).
Data file: `district_data.csv` (565 rows; blank `value` = gap, never filled in by estimate).
Drought (item A) and crop insurance (item B) are kept separate and must never be added together.

## Coverage summary (31 districts)

| Item | Metric | Districts with a value | Confidence | Note |
|---|---|---|---|---|
| A. Drought 2023 | Taluks declared, severe / moderate / total | 31 of 31 | HIGH | Phase 1 only (195 taluks, GO 13 Sep 2023). Later 22 + 7 taluks not attributed to districts. |
| A. Drought 2023 | Crop-loss area (ha) | 0 of 31 | none | Gap |
| A. Drought 2023 | Input subsidy / relief paid (Rs cr) | 0 of 31 confirmed; 1 LOW (Belagavi) | LOW | Belagavi figure unverified, year not confirmed |
| A. Drought 2023 | Farmers paid (count) | 0 of 31 confirmed; 1 LOW (Belagavi) | LOW | same |
| B. PMFBY | Claims reported / paid / pending, Rs cr | 31 of 31 | HIGH | Cumulative 2020-21 to 2024-25, PMFBY + RWBCIS, as on 31.12.2025. Not per season. |
| B. PMFBY | Farmers insured, kharif 2023 / rabi 2023-24 / kharif 2024 | 0 of 31 | none | Gap |
| B. PMFBY | Claims paid per season | 0 of 31 | none | Gap |
| B. PMFBY | Premium collected | 0 of 31 | none | Gap |

## Sources used

1. **Government of Karnataka order RD 449 TNR 2023, 13.09.2023** (drought declaration, 195 taluks: 161 severe in Annexure-1, 34 moderate in Annexure-2). Translated copy filed as Annexure I to NGT OA 196 of 2024, Reply Statement by R2: https://www.greentribunal.gov.in/sites/default/files/news_updates/OA%20196%20of%202024%20Reply%20Statement%20by%20R2.pdf. Printed pages 6-13 (PDF pages 7-14). Taluk lists transcribed and counted per district; counts check to 161 and 34. HIGH (government order; the copy is an English translation filed in a tribunal, so taluk spellings are the translator's).
2. **Lok Sabha Unstarred Question 662, "Pending Claims of PMFBY", answered 03.02.2026** (asked by Shri E Tukaram; answered by MoS Shri Ramnath Thakur). Official PDF: https://sansad.in/getFile/loksabhaquestions/annex/187/AU662_dnteed.pdf?source=pqals. Annexure-I (p. 3) state-wise kharif/rabi; Annexure-II (p. 4) Karnataka district-wise claims reported, paid and pending, 2020-21 to 2024-25, as on 31.12.2025. HIGH. The official file's SHA-256 matches the PolicyIndex mirror (92d7b7e2...475f15). District sums check to the printed total (Rs 11,251.80 cr reported, Rs 11,182.78 cr paid, Rs 69.02 cr pending), and that total equals the Annexure-I Karnataka kharif + rabi figures.
3. **All About Belgaum, "Belagavi District Receives 247 Crore Drought Relief: DC Nitesh Patil"**: https://allaboutbelgaum.com/news/belagavi-district-receives-247-crore-drought-relief-dc-nitesh-patil/. LOW. The page would not open (timeout); figures come only from a search-engine summary. Year not confirmed.

State-level context found while searching (not district figures, not in the CSV, from search summaries of press reports, MEDIUM at best; some already in `../DELIVERY_LEDGER_RESEARCH.md`):
- 223 of 236 taluks drought-declared by Nov 2023 after three phases (195, then 22 in Oct, then 7 on 4 Nov). South First, Oct 2023: https://thesouthfirst.com/karnataka/karnataka-set-to-seek-additional-relief-funds-from-union-government-declares-22-more-taluks-as-drought-hit/ (14 Oct 2023; gives 11 severe + 11 moderate but no taluk names).
- State interim relief Rs 636.45 cr to 33.58 lakh farmers; NDRF-funded payments to 27.38 lakh farmers, Rs 2,425.13 cr by early May 2024. Deccan Herald (via search): https://www.deccanherald.com/india/karnataka/all-farmers-to-get-drought-relief-in-2-3-days-says-revenue-minister-3010799. Not opened (Deccan Herald returned 403).
- Karnataka PMFBY/RWBCIS farmer applications, state only: 30,15,023 in 2023-24 (PIB release https://www.pib.gov.in/PressReleasePage.aspx?PRID=2148513, seen in a search summary only, not opened).

## Gaps

- **Drought crop-loss area by district (ha):** not found anywhere reachable. Statewide 48.19 lakh ha is widely reported; the district split sits in the state memoranda to the Centre (22 Sep, Oct and 15 Nov 2023) and in Revenue Department records.
- **Drought relief paid by district (Rs cr, farmers):** not found from an official source. Belagavi only, LOW.
- **Phase 2 and phase 3 drought taluks (22 + 7):** the orders were not found, so the district taluk counts in the CSV are the 13 Sep 2023 order only. Press says that after phase 2 all taluks of Dharwad, Gadag and Haveri were severe; the CSV still shows the phase 1 count for those districts.
- **PMFBY per season by district:** the only district table found is a five-year cumulative. Nothing for kharif 2023, rabi 2023-24 or kharif 2024 by district, and no district premium or farmers-insured figures.
- Ramanagara district was renamed Bengaluru South in 2024; both sources use Ramanagara.

## Needs a person in India (sites unreachable from here)

These Karnataka government sites refused or timed out from outside India:
1. **revenue.karnataka.gov.in Annual Report 2023-24**: https://revenue.karnataka.gov.in/uploads/media_to_upload1712395448.pdf (connection refused). Check for district-wise drought 2023 tables: crop loss ha, input subsidy paid, farmers paid.
2. **Parihara portal** (Revenue Department crop-loss payment portal; exact URL not verified from here): district and taluk payment reports for "Drought 2023-24 Kharif", both the state interim relief (up to Rs 2,000) and the NDRF input subsidy. Record amount and number of farmers per district.
3. **Samrakshane** (samrakshane.karnataka.gov.in, timed out): district-wise reports for kharif 2023, rabi 2023-24 and kharif 2024. Record farmers insured (applications), premium (farmer share), and claims paid.
4. **KSNDMC / Revenue (Disaster Management)**: the later drought GOs (about Oct 2023, 22 taluks; 4 Nov 2023, 7 taluks) and the memorandum annexures with district crop-loss area.
5. **Karnataka Legislative Assembly / Council question answers** (kla.kar.nic.in), Feb and Jul 2024 sessions: search for district-wise drought relief questions ("ಬರ ಪರಿಹಾರ ಜಿಲ್ಲಾವಾರು").

## Open checks (can be done from anywhere)

- **pmfby.gov.in dashboard** (https://pmfby.gov.in/adminStatistics/dashboard): reachable, but the data loads in a JavaScript app, so it needs a browser session. It may give state > district farmers insured, premium and claims per season.
- Search Lok Sabha / Rajya Sabha for other answers by Karnataka MPs asking for PMFBY figures district-wise and season-wise (the 03.02.2026 answer shows the Ministry will give district tables for Karnataka when asked).
- Open the Belagavi article (or the Belagavi DC's press note) to confirm the date, the drought year and the figures before using them.
- Get a copy of Karnataka's writ petition in the Supreme Court (2024, NDRF drought assistance). Its annexures may include the memorandum with district tables.

## Reading rules for anyone using this file

- PMFBY claim values are five-year sums (2020-21 to 2024-25) of PMFBY and RWBCIS together. Do not call them "2023-24 claims".
- `taluks_declared_total_phase1` is severe + moderate from the same order, not an estimate.
- No figure here supports a comparison between districts' drought relief and insurance payouts; they are different schemes and periods.
