# DRAFT: Karnataka legislators' annual property statements (Lokayukta Act, s.22)

**Status: DRAFT, not verified for publication.** Research run 16 Nov 2026. Companion data: `defaulters.csv` in this folder.

**Read this first.** Not filing a statement under Section 22 is a legal default under the Karnataka Lokayukta Act. It is **not** evidence of hidden wealth, wrongdoing or corruption. News reports summarise Lokayukta releases and may be incomplete, and they sometimes differ from each other. Names below are "as reported" and should not be republished as a finding until checked against the official Lokayukta notice.

## 1. What the Lokayukta publishes

**Defaulter lists only. No per-MLA statements were found.**

- **The legal basis.** Section 22(1) requires every public servant (MLAs and MLCs included) to file a statement of their own and their family's assets and liabilities by 30 June each year. Under s.22(2), the Lokayukta reports defaulters to the competent authority. If a defaulter still has not filed within two months of that report, the Lokayukta may publish their names. Sources: the PTI copy at NewsDrum (6 Nov 2025) quotes the Lokayukta release, https://www.newsdrum.in/national/100-legislators-including-5-ministers-failed-to-file-statement-of-assets-liabilities-to-lokayukta-10629032 , and Republic (1 Jul 2023) describes the process, https://www.republicworld.com/india/70-percent-of-karnataka-mlas-and-mlcs-neglect-asset-disclosure-reports-articleshow
- **Official site.** https://lokayukta.kar.nic.in did not resolve from this machine's shell, from WebFetch, or from Chrome (error page). The new domain https://lokayukta.karnataka.gov.in refused the connection and redirected to the dead kar.nic.in host.
- **Wayback Machine.** I checked the archived site instead: the homepage snapshot of 21 May 2025, downloads.php of 21 May 2025, and the Wayback CDX index of all archived lokayukta.kar.nic.in URLs (about 1,330 unique URLs).
  - I found no legislator statement PDFs and no defaulter-list pages.
  - The only asset-related pages are statements of the Lokayukta institution's own office-holders and staff. These are `assliab.htm` (snapshot 21 Jul 2011: "Assets & Liabilities of Lokayukta / Upalokayukta / Police Wing / Admin Wing ..."), `ASSETS OF lok.pdf`, `ASSETS OF upalok.pdf` and `Assets and Liabilities statement of registrar.pdf`.
  - The site also hosts the blank filing form, `pdf/Form-IVEnglish.pdf` ("Form No. IV – for submitting statement of assets and liabilities").
- **Conclusion.** The defaulter lists reach the public through press releases and newspaper notices, which the news reports below cite. As far as can be seen, the filed statements are not published online. This could not be confirmed against the live site (see "What is not verified").

## 2. Defaulter lists by year

### 2022-23 (statements due 30 Jun 2023). Not asked for, but it is the only earlier list found.
- **Source:** RevenueFacts (Kannada), 30 Nov 2023, https://revenuefacts.com/lokayukta-published-names-of-mlas-who-did-not-submit-asset-details/ . The article does not state the financial year. It says the deadline was "last June 30", so 2022-23 is **inferred**.
- **Counts:** 51 legislators, made up of 30 MLAs and 21 MLCs. The same article also says 81 MLAs from the previous Assembly did not file.
- **Current ministers named:** K.N. Rajanna, Ramalinga Reddy, Zameer Ahmed, K.H. Muniyappa and Raheem Khan. No other MLA names are given.
- **Earlier context:** Republic (1 Jul 2023, link above) reported that at the 30 June 2023 deadline, 60 MLAs and 36 MLCs had not filed. That is the count at the deadline, not the published defaulter list.

### 2023-24 (statements due 30 Jun 2024). **NOT FOUND.**
Several web searches turned up no news report of a 2023-24 list: English, Kannada, Deccan Herald site search and the DH "assets and liabilities" tag. I cannot tell whether the list was never published or just wasn't covered.

### 2024-25 (statements due 30 Jun 2025). Published 6 Nov 2025.
- **Counts.** Reports differ:
  - PTI/NewsDrum: 100 legislators, including 5 ministers, 67 MLAs and 28 MLCs.
  - TNM: 66 MLAs and 28 MLCs.
  - Deccan Herald: "200 legislators including six ministers, 66 MLAs and 28 MLCs", while its own headline says 100.
- **Report date.** The Lokayukta report on the defaulters was dated 28 Aug 2025 (PTI quotation).
- **Sources:**
  - Mangalorean, 7 Nov 2025 (fullest list, MLAs with constituencies): https://www.mangalorean.com/karnataka-lokayukta-releases-list-of-ministers-and-legislators-failing-to-declare-assets/
  - Deccan Herald, 6 Nov 2025 (party labels): https://www.deccanherald.com/india/karnataka/lokayukta-flags-100-legislators-including-five-ministers-for-defaulting-over-asset-declaration-3789152
  - The News Minute, 7 Nov 2025: https://www.thenewsminute.com/karnataka/100-karnataka-lawmakers-fail-to-declare-assets-for-the-year-2024-25-lokayukta
  - NewsDrum/PTI, 6 Nov 2025 (link above)
- **Ministers (5):** K.H. Muniyappa, Dinesh Gundu Rao, B.Z. Zameer Ahmed Khan, Rahim Khan, K. Venkatesh.
- **MLAs named (27 of 66/67).** Mangalorean names 23 "among others". Deccan Herald adds 4 that Mangalorean does not name: C.P. Yogeshwar, C. Puttarangashetty, B. Suresh Gowda and K. Gopalaiah. All 27, with constituency and party taken from `data/mlas.csv`, are in `defaulters.csv`.
- **Coverage gap.** About 40 of the 66/67 MLA defaulters are **not named** in any source opened.
- **Late filers.** These filed after the deadline and are listed as late, not as defaulters: Minister D. Sudhakar, B.M. Nagaraj (Siruguppa), M.T. Krishnappa (Turuvekere) and Pathan Yaseer Ahmad Khan (Shiggaon). The MLC late filer is Chidananda M. Gowda. Source: Mangalorean. They appear in the CSV with year "2024-25 LATE FILER (not defaulter)".
- **MLCs (28).** Their names are in the Mangalorean article. MLCs are outside the scope of `mlas.csv`, so they are not in the CSV.

### 2025-26 (statements due 30 Jun 2026). **NOT FOUND as of 16 Nov 2026.**
A Deccan Herald site search (results up to Sep 2026) and web searches show no 2025-26 list. Last year's timeline was a report on 28 Aug and names on 6 Nov, so a list may still be pending.

## 3. Current MLAs named in more than one year

There are only two years with names: 2022-23 (ministers only, year inferred) and 2024-25. On that basis:

| MLA (mlas.csv) | Constituency | Party (2023) | 2022-23 | 2024-25 |
|---|---|---|---|---|
| K.H. Muniyappa | Devanahalli (SC) | Congress | named (minister) | named (minister) |
| B.Z. Zameer Ahmed Khan | Chamrajapet | Congress | named (minister) | named (minister) |
| Rahim Khan | Bidar | Congress | named ("Raheem Khan") | named (minister) |
| K.N. Rajanna (Kyathasandra N. Rajanna) | Madhugiri | Congress | named (minister) | named (as MLA, Madhugiri) |

- **Ramalinga Reddy** (B.T.M Layout) is named for 2022-23 but **not** in the 2024-25 names found. He could still be among the roughly 40 unnamed 2024-25 MLAs.
- **Why the four repeat names are all ministers from one party.** The 2022-23 source names only ministers (all serving in the government formed in May 2023), so only ministers can appear in both years. This is an artefact of what was published, not evidence that one party defaults more. Do not present it as a party comparison.
- **Checked again on 16 Nov 2026** by the research session: the four repeat names appear in RevenueFacts (30 Nov 2023, "the last date was June 30") and Mangalorean (7 Nov 2025, 2024-25 list).
- **Why this is a floor, not a full count.** The 2022-23 source names only ministers, and the 2024-25 sources name 32 of about 72 (ministers plus MLAs). Other repeat defaulters may exist among the unnamed.

### Counts of current MLAs (16th Assembly) named per year
| Year | Defaulting MLAs named in the sources | Officially reported total (MLAs) |
|---|---|---|
| 2022-23 (inferred) | 5 (ministers only) | 30 MLAs (RevenueFacts) |
| 2023-24 | not found | not found |
| 2024-25 | 32 (5 ministers + 27 MLAs). 31 of them match a current row in mlas.csv | 66 or 67 MLAs + 5 ministers |
| 2025-26 | not found | not found |

### Name-match notes (see `match_confidence` in the CSV)
- **H.Y. Meti (Bagalkot, 2024-25)** is not in mlas.csv. The CSV's Bagalkot row is Umesh Hullappa Meti (by-election Apr 2026), so the 2024-25 defaulter does not match the current seat-holder. Treat them as different people.
- **K. Venkatesh (minister)** matches K Venkatesh, Piriyapatna (medium). The CSV also has H.V. Venkatesh (Pavagada), but the minister title fits Piriyapatna.
- **B. Suresh Gowda** matches B.Suresh Gowda, Tumkur Rural, BJP (medium). DH gives his party as BJP, and no constituency was given.
- **D. Sudhakar (late filer)** matches "D Sudakar", Hiriyur (medium, spelling). The CSV also has Dr M C Sudhakar (Chintamani).
- **G. Janardhana Reddy.** mlas.csv says KRPP (his 2023 party), DH (2025) says KRPP, and TNM says BJP. The CSV party column reflects the 2023 affidavit, not current affiliation.

## 4. Statement vs 2023 affidavit comparison

**Not possible.** No individual Section 22 statement was found in public, so there is no "statement year" figure to compare with the 2023 affidavit totals in mlas.csv. No comparison has been made, and none should be inferred.

## What is not verified
- **No official notice.** None of the Lokayukta notices or press releases were seen. lokayukta.kar.nic.in and lokayukta.karnataka.gov.in could not be reached. All names come from news reports.
- **Archive limits.** "No statements are published" rests on the Wayback archive, last snapshot 21 May 2025. The live site may have added pages since then.
- **2022-23 year.** The year is inferred from "last June 30" in a Kannada article dated 30 Nov 2023. That article names ministers only.
- **No 2023-24 or 2025-26 list found.** Absence in searches is not proof that no list exists.
- **2024-25 counts.** The totals conflict (66 vs 67 MLAs; 5 vs 6 ministers; DH's "200"). Only 32 of about 72 MLA and minister names are known.
- **Parties.** These come from mlas.csv (2023 election), not current affiliation.
- **Corrections.** The Lokayukta has corrected published lists before. DH (2014, https://www.deccanherald.com/india/karnataka/lokayukta-drops-four-mlcs-defaulters-2205608) reported names withdrawn because the people were not members in the year concerned. Some named defaulters may have filed later.
- **Sources that would not open:**
  - lokayukta.kar.nic.in (DNS failure, shell, WebFetch and Chrome)
  - lokayukta.karnataka.gov.in (connection refused / redirect)
  - Deccan Herald via WebFetch (403; opened fine in Chrome)
  - NewsDrum via WebFetch (403; opened in Chrome)
  - english.udayavani.com (DNS) and udayavani.com/?p=228898 (empty page), a "67 MLAs" story of unknown date
  - Lokayukta "general press note.pdf" on Wayback (image-only, unreadable)
