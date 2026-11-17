# DRAFT: Lokayukta PC Act cases, notes on the annexures of LC USQ 452 (628)

**Status: DRAFT.** Extracted by reading scanned page images. Nobody has checked it against the original yet.
Extracted on 16 Nov 2026.

## Source

- Karnataka Legislative Council, unstarred question 452 (628), asked by Dr Dhananjaya Sarji. Written reply by the Chief Minister, dated 20.08.2026.
  URL: https://kla.kar.nic.in/council/Replies/unstarred/20082026/usq628(20082026).pdf (231 pages, scanned Kannada).
- Not used here: USQ 489 (560), Madhu G. Madegowda (887 trap cases from 1 Jan 2023). That reply has its own annexure and was not read for these tables.

## What the reply says (cover pages 1-2)

- Lokayukta police registered **1,248** PC Act cases from 10/09/2022 to 13/08/2026: **939 trap** and **309 disproportionate-assets (DA, ದಾಳಿ)**. Details are in Annexure-1.
- Cases by stage (state total only): **218 stayed by courts**, **18 B-final reports**, **364 chargesheeted**, **648 under investigation**. These add up to 1,248.
- Officials and staff by class. These are PERSONS, not cases: IAS 1, IPS 1, KAS 27, Group A 212, Group B 376, Group C 733, Group D 28, elected representatives 24, outsourced 49. Total 1,451.
- Courts have convicted in 148 cases since 2023. These are older PC Act cases that finished trial.
- There were **115** other cases that were neither trap nor DA. The reply says Annexure-2 gives them department-wise. The annexure itself turns out to cover more than that; see below.

## Structure of the annexures

**Annexure-1 (pdf pages 3-134).** Title: trap and DA cases registered 10/09/2022 to 13/08/2026. It has 7 columns:
1. serial number (runs 1-1,248 without a break)
2. district / Lokayukta police station
3. crime number and section
4. case type (trap or DA)
5. name and address of the accused
6. class (ವರ್ಗ: A/B/C/D/KAS/IAS/OUTSOURCE...)
7. department

Rows are grouped by district. The order is roughly alphabetical in English, with Bengaluru first. There are no district subtotal rows. **There is no stage, status or stay column.**

**Annexure-2 (pdf pages 135-231).** Title: department-wise details of ALL cases registered 10/09/2022 to 13/08/2026. Each department has its own sub-table under an English heading, and serial numbers restart at 1 in each one. It has 6 columns:
1. serial number
2. district / police station
3. crime number and section
4. case type: trap, DA (ದಾಳಿ / ಡಿ.ಎ) or other (ಇತರೆ, "criminal misconduct", "ಅಪರಾಧಿಕ ದುರ್ನಡತೆ" and so on)
5. accused
6. accused's department

It mixes trap and DA cases that also appear in Annexure-1 (for example Bengaluru City-1 67/2022 and 72/2022 under Energy) with "other" cases. **It has no stage or stay column either.**

## Tables in this folder

- `by_district.csv` counts Annexure-1 cases by Lokayukta unit. Counts are taken from the serial numbers where each district starts and ends, checked page by page. The serials are continuous from page 3 to page 134, and the total is 1,248, which matches the cover answer exactly. Bengaluru Urban is split into the City-1 and City-2 police stations, and the `revenue_district` column merges them back. Hosapete is Vijayanagara, Karwar is Uttara Kannada, Madikeri is Kodagu and Mangaluru is Dakshina Kannada. All 31 districts appear.
- `by_department.csv` counts Annexure-2 cases by department heading. The count is the last serial number in each sub-table, cross-checked by reading every page's serial numbers for continuity. `rows_present_in_pdf` is different only for Urban Development.

## Pages read

- Pages 1-2 (cover answer) were read in full.
- Annexure-1, pages 3-134: I read the serial number and district columns of **every page**. Every district boundary was found directly; none was estimated. On pages 3-14 I also saw the type column. I did not read the department, class or type column row by row for the whole annexure.
- Annexure-2, pages 135-231: I read the serial number, case-number, type and heading area of **every page**. Page 191 is scanned upside down and was rotated to read it. I did not read the per-row district for this annexure.
- I did not record any accused names.

## Totals cross-check

| Check | Result |
|---|---|
| Annexure-1 rows vs cover (1,248) | **1,248 = 1,248.** Serials are continuous. |
| Districts summed | 1,248 |
| Stage split (648 + 364 + 218 + 18) | Adds to 1,248 on the cover, but **cannot be broken down by district or department**: neither annexure has a stage column. |
| Annexure-2, summed by last serials (33 headings) | **1,347** |
| Annexure-2, rows actually in the PDF | **1,292** (Urban Development serials 83-137 are missing) |
| Expected if Annexure-2 = 1,248 trap/DA + 115 other | 1,363. The serial total is 16 short. The cause is unexplained. |

## Uncertain or not possible

1. **Stays (question 3): not answerable from these annexures.** The 218 court stays appear only as one state-wide number. No row carries a stay flag, so stays cannot be ranked by department or district. Possible routes: a follow-up question, a Karnataka Lokayukta RTI, or the High Court's stay orders. The USQ 560 annexure (887 trap cases) was not checked for a status column. That is worth a look.
2. **Urban Development gap.** On page 222 the last serial is 82 (Davanagere). Page 223 starts at serial 138 (Mysuru). The districts in between (Dharwad through Mangaluru) are absent. This looks like 5-6 pages missing from the published PDF rather than a numbering slip, but it is unconfirmed. Urban Development is counted as 159 by serial, 104 rows actually present.
3. **Annexure-2 vs the cover.** The cover calls Annexure-2 "115 other cases". In fact it lists all case types. Its department totals therefore measure all accused-department exposure, not "other" cases. A case with accused from several departments may appear under more than one heading. I have not checked this.
4. **Department labels are as printed.** One heading reads "Law, Justice and Women Rights", probably meaning Human Rights. "Out Source" and "Elected Members" are categories of accused, not departments.
5. **Annexure-1 has a department column** that could support a second, independent department count, but I did not read it row by row (1,248 rows). The class, trap/DA and department columns per district are all readable at the resolution I used. A full row-level pass would add trap/DA by district, class by district and a cross-check of the Annexure-2 department totals.
6. **Read visually with no OCR.** District boundaries are high confidence, because the serial numbers and district names are both large and clear. Department sub-table ends are high confidence. Any single misread of a serial would show up as a break in continuity, and none was found except the Urban Development jump.
