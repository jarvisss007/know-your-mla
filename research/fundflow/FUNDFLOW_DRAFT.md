> DRAFT, 17 Nov 2026. Not for the site until a second check. Audit observations describe systems and departments; they are not findings of theft by any person.

# How public money moves in Karnataka, where it can leak, and how to trace it back

Private working draft for the citizen accountability project. Prepared 17 Nov 2026. Public records only.

**How to read this draft.** It describes systems and audit findings. An audit observation is a finding about a system or a department. It is not proof that anyone stole money. Where the CAG (Comptroller and Auditor General of India, the national auditor) uses words like "misappropriation", "fraudulent" or "doubtful", we quote them exactly and say where they appear. Rupee amounts are in crore (1 crore = 10 million rupees) unless stated.

**Confidence labels.**
- **High:** read in the original CAG text (local copy or PDF) for this draft.
- **Medium:** comes from the text of an Act or official rule, or from a CAG summary, but the current version is not confirmed.
- **Low:** comes from news or secondary sources only. Verify before use.

**Main sources read in the original**

| Short name | Report | Where |
|---|---|---|
| SFAR 23-24 | CAG State Finances Audit Report (SFAR) for 2023-24, Report No. 4 of 2025 | [PDF](https://cag.gov.in/uploads/download_audit_report/2024/Report-of-the-Comptroller-and-Auditor-General-of-India-on-State-Finances-for-the-year-2023-24,-Government-of-Karnataka-(Report-No.-4-of-2025)---English-version-068a5681816b4d4.80809774.pdf); local copy `sweep/devwork/docs/sfar2324.txt` |
| SFAR 24-25 | CAG SFAR for 2024-25, Report No. 2 of 2026 | [cag.gov.in/en/audit-report/details/124514](https://cag.gov.in/en/audit-report/details/124514); local copy `c26_cag_sfar_2024-25_report2of2026.txt` |
| MGNREGS PA | CAG Performance Audit of MGNREGS in Karnataka, Report No. 13 of 2025. Government replies are dated May 2025; news coverage is from March 2026. | [full report PDF](https://cag.gov.in/webroot/uploads/download_audit_report/2025/English-final-pdf-MGNREGS-with-signature-069c27a99698a17.10858290.pdf); local copies in `fundflow/src/` |
| Yettinahole PA | CAG Performance Audit of the Yettinahole Integrated Drinking Water Project, Report No. 10, tabled 29 Jan 2026 | [details/123863](https://cag.gov.in/en/audit-report/details/123863); local copies of chapters 2 and 3 |
| Smart City PA | CAG Performance Audit of the Smart City Mission, Report No. 11 of 2025, tabled 29 Jan 2026 | [details/123892](https://cag.gov.in/ag2/karnataka/en/audit-report/details/123892) |
| KKRDB PA | CAG Performance Audit of the Kalyana Karnataka Region Development Board (2022). Report number not confirmed. | [Chapter 5](https://cag.gov.in/uploads/download_audit_report/2022/Chapter-5-Financial-Management-063f74dd8781799.85859702.pdf), [Executive summary](https://cag.gov.in/uploads/download_audit_report/2022/Executive-summary-063f74dd849f3e5.57928385.pdf) |
| CA 6/2025 | CAG Compliance Audit Report for the year ended March 2023, Report No. 6 of 2025: Skill Mission, Labour, Urban Development and Social Welfare | [Preface and Overview PDF](https://cag.gov.in/uploads/download_audit_report/2025/Preface-and-Overview-068a700e008a068.58099381.pdf) |
| CA 1/2026 | CAG Compliance Audit Report No. 1 of 2026: Sports, Health and others | [Chapter I](https://cag.gov.in/uploads/download_audit_report/2026/Chapter-I-Introduction-069c51cb19b47e0.37854804.pdf), [Chapter II](https://cag.gov.in/uploads/download_audit_report/2026/Chapter-II-Subject-Specific-Compliance-Audit-and-other-Compliance-Audit-Paragraphs-069c51cb19faa70.21082389.pdf) |
| KTPP Act | Karnataka Transparency in Public Procurements Act 1999, consolidated text | [casemine copy](https://www.casemine.com/act/in/5ed4fb0a894ef23297d8bbd6). The India Code PDF returned "403 Forbidden". |

---

## Part 0. The plumbing in one page

Before the routes, here is what the main pieces are.

- **Consolidated Fund of the State.** The state's main account. All taxes, central transfers and borrowing go in. Nothing can come out without a law passed by the Legislature: the budget (Appropriation Act) under Articles 204 and 266(3) of the Constitution.
- **Grant.** The budget is split into numbered "grants", for example Grant 10 Social Welfare and Grant 17 Education. Each grant is split into "heads of account". A head of account is a 15-17 digit code, such as 2225-01-102-0-11-059, that says what the money is for. The 4-digit start is the **Major Head**. The next 3 digits are the **Minor Head**.
- **Public Account.** Money the government holds but does not own outright: deposits, provident funds, and **Personal Deposit (PD) accounts** (head 8443-106). Money moved here from the Consolidated Fund is counted as "spent" even though it has not reached anyone yet.
- **DDO (Drawing and Disbursing Officer).** The officer in each office who can draw money from the treasury by presenting a bill.
- **Khajane-II.** Karnataka's online integrated treasury system. DDOs raise bills in it. The treasury checks each bill against the budget and pays electronically to the payee's bank account. Each payment produces a voucher.
- **Accountant General (Accounts and Entitlement), AG (A&E).** Part of the CAG. It compiles the state's accounts from treasury vouchers and publishes the yearly **Finance Accounts** and **Appropriation Accounts**.
- **Accountant General (Audit).** Also part of the CAG. It audits departments, sends **Inspection Reports** to them, and writes reports that go to the Legislature. The Legislature's **Public Accounts Committee (PAC)** examines those reports.

---

## Part 1. The path of a rupee: six routes

Each step shows who acts, what document is created, and where it is recorded. "Rule basis" names the rule or document behind the step. We checked a rule only where it is cited in a CAG report or in an Act we read. Other rule names come from general knowledge of the system and are marked *(unverified)*.

### Route A. State budget to a works contractor (a road, a building, a canal)

| # | Step | Who acts | Document created | Where it is recorded | Rule basis |
|---|---|---|---|---|---|
| A1 | Budget estimates prepared | Departments, then the Finance Department (FD) | Budget estimates, "Detailed Estimates of Expenditure", grant-wise demands | Budget books placed in the Legislature | Karnataka Budget Manual (KBM). Para 110 KBM requires a look at the past three years' performance (cited in SFAR 23-24 para 3.8.2.4). |
| A2 | Legislature votes the money | Legislature | Appropriation Act, plus supplementary grants during the year | Gazette; later the Appropriation Accounts | Art. 204 and 205 of the Constitution; Art. 266(3) bars withdrawal without appropriation (SFAR 24-25 para 2.5.1.1) |
| A3 | Release of funds | FD, then the department's Chief Controlling Officer | Release order and grant allotment, entered in Khajane-II as a budget allocation to DDOs | Khajane-II budget module; FD release orders | FD instructions of 9 Sept 2004 on release, drawal and accounting (SFAR 24-25 para 2.5.8.1) |
| A4 | Work is proposed | Executing division, for example the Public Works Department (PWD), Irrigation or Panchayat Raj Engineering | Detailed estimate, then **administrative approval** (the department agrees the work is needed and has funds), then **technical sanction** (an engineer certifies the design and cost) | Division work register; estimate file | Karnataka PWD (KPWD) Code; Karnataka Financial Code (KFC) para 14 (no spending without sanction and funds; SFAR 24-25 para 2.5.1). The MGNREGS PA Table 5.4 shows the delegation for panchayat works: up to Rs 3 lakh, Rs 3-10 lakh and Rs 10-30 lakh each have a different sanctioning officer. |
| A5 | Tender | Tender-inviting authority | Tender notice on the Karnataka Public Procurement Portal (KPPP), bids, comparative statement, Tender Scrutiny Committee note | KPPP e-procurement portal | KTPP Act and Rules. See "Tender thresholds" below. |
| A6 | Award | Accepting authority | Letter of acceptance, agreement, **work order**, security deposit or performance security | Division agreement register | KTPP Rules; contract clauses (for example the 5% retention money in the Yettinahole contracts, Yettinahole PA para 3.2.2.6) |
| A7 | Work done and measured | Junior or Assistant Engineer measures; the Assistant Executive Engineer or Executive Engineer check-measures | **Measurement Book (MB)** entries, photos (geo-tagged in some schemes) | MB (paper or e-MB); scheme portals | KPWD Code. Rule 202: work measured in one month is ordinarily paid the next month (KKRDB PA para 5.2.9). |
| A8 | Bill | Executive Engineer acting as DDO | Running Account or Part bill, then the final bill, with deductions | Khajane-II bill | KFC; Karnataka Treasury Code *(rule numbers unverified)* |
| A9 | Treasury check and payment | District or taluk treasury | Treasury voucher; e-payment to the contractor's bank account | Khajane-II; the bank's scroll (its daily list of payments) to the treasury | Karnataka Treasury Code *(unverified)* |
| A10 | Deductions sent on | Treasury and DDO | Income-tax deducted at source (TDS), GST TDS, **1% construction-workers' welfare cess**, royalty, security deposit or retention | Deposit and remittance heads, for example 8443 Civil Deposits and 8449 for the cess (SFAR 24-25 para 3.2.3) | BOCW Cess Act 1996 (1% of construction cost). Tax rates are under central law. |
| A11 | Accounts compiled | AG (A&E) | Monthly civil accounts, then Finance Accounts and Appropriation Accounts | CAG publications | Art. 150 and 151 of the Constitution |
| A12 | Reconciliation | Controlling Officers with the AG every month; divisions with the treasury | Reconciliation certificates | AG records (SFAR 24-25 paras 3.7 and 3.8) | "State Financial Rules" requiring monthly reconciliation (SFAR 24-25 para 3.8) |
| A13 | Audit | AG (Audit) | Inspection Report, then a draft paragraph, then the Audit Report, then PAC review | cag.gov.in | CAG (DPC) Act 1971 |

**Tender thresholds (KTPP Act, consolidated text, medium confidence; check against the latest amendments).** The Act's open-tender rules (Chapter II) do **not** apply to the following:
- **Section 4(e).** Departments and listed boards: construction works "the value of which does not exceed rupees five lakhs", and goods or services "not exceed[ing] rupees one lakh".
- **Section 4(ee).** Panchayats and municipal bodies: up to Rs 2 lakh for mini water-supply works or school rooms, and Rs 1 lakh for anything else.
- **Section 4(g).** Any "specific procurements as may be notified by the Government from time to time". This clause is used to hand works straight to government agencies such as KRIDL (Karnataka Rural Infrastructure Development Ltd) and Nirmithi Kendra; see KKRDB PA paras 5.2.10-5.2.11.
- **Section 10.** A Tender Scrutiny Committee looks at tenders above Rs 5 crore in PWD, Irrigation and Minor Irrigation, and above Rs 1 crore elsewhere.
- **Rule 17, KTPP Rules.** Minimum bidding time is 30 days for works up to Rs 2 crore. Above Rs 2 crore it was 60 days, cut to 30 days in Sept 2019 (Yettinahole PA, Table 3.4).
- **Section 6.** Works up to Rs 50 lakh can be reserved for Scheduled Caste and Scheduled Tribe contractors (17.15% and 6.95% of works). News reports say this limit was raised to Rs 1 crore, but that is not confirmed in the Act text.

**Why the thresholds matter.** Anything just under Rs 5 lakh, for works, avoids open tendering. Another research session is already analysing Bengaluru city payment records for bills split just under Rs 5 lakh and for repeated bill IDs. This draft does not repeat that work.

### Route B. State budget to a welfare beneficiary by Direct Benefit Transfer (DBT)

| # | Step | Who acts | Document | Where recorded |
|---|---|---|---|---|
| B1 | Scheme and budget | Department and FD | Government order setting eligibility; budget line under the scheme head | Budget books; Government Order |
| B2 | Applications and beneficiary list | Applicant, village accountant or Gram Panchayat, department field officer | Application (often online, Seva Sindhu); the beneficiary record is linked to Aadhaar, a ration card or the state family database *(the Kutumba family database is named from general knowledge, unverified)* | Scheme portal or database |
| B3 | Verification | Field officer or tahsildar; automatic checks (Aadhaar, income, duplicate removal) | Verification report; approved list | Scheme portal |
| B4 | Payment file | DDO or scheme nodal officer | Beneficiary bill in Khajane-II, or a payment file pushed through the state DBT platform | Khajane-II; state DBT portal *(state DBT platform details unverified)* |
| B5 | Bank transfer | Treasury, the Reserve Bank's e-Kuber system or an agency bank, then NPCI's Aadhaar Payment Bridge | Credit to the beneficiary's account | Bank records; success and failure reports |
| B6 | Failed or returned payments | Bank and department | Return file; re-payment or refund | Often parked in deposit heads or bank accounts until settled *(practice unverified)* |
| B7 | Variant: through a corporation | Department releases a grant to a welfare corporation, for example Dr B.R. Ambedkar Development Corporation or the Backward Classes corporations. The corporation then pays beneficiaries or loans. | Grant-in-aid bill. **At this point the state accounts show the money as "spent".** The corporation runs its own beneficiary selection and payment. | Corporation's PD account or bank account; corporation's annual accounts |

The CAG found that this corporation variant is where money stalls. See leak points B-1 to B-3.

### Route C. Central money for a centrally sponsored scheme (CSS)

| # | Step | Who acts | Document | Where recorded |
|---|---|---|---|---|
| C1 | Central release | Union ministry, through PFMS (the Centre's Public Financial Management System) | Sanction order; transfer to the state's Consolidated Fund through the Reserve Bank | PFMS; Finance Accounts (grants from the Centre) |
| C2 | State adds its share | FD | Matching share released, for example 25% for MGNREGS material, 40% for Samagra Shiksha and 50% for Urban Rejuvenation (SFAR 24-25 para 2.6.1) | Khajane-II, budget head of the "state-linked scheme" |
| C3 | Transfer to a **Single Nodal Agency (SNA)** | FD | Centre's share plus state share credited to the SNA's own bank account **within 21 days** (SFAR 24-25 para 2.5.1.1, government reply) | Bank account of the SNA; PFMS SNA module. **In the state accounts this counts as expenditure.** |
| C3' | Newer model: **SNA-SPARSH** ("just-in-time" release, from July 2023) | Ministry of Finance, PFMS, the state's financial system and e-Kuber | Money stays in the Consolidated Funds until the moment of payment; the old SNA accounts must be closed and balances refunded | PFMS. In Karnataka, 29 of 140 schemes had moved fully by the 2024-25 report (SFAR 24-25 para 2.6.3). |
| C4 | Implementing agencies | SNA, then district or taluk agencies or vendors | Zero-balance subsidiary accounts or limits; payment advice | PFMS, bank |
| C5 | Spend on the ground | Agencies | Bills, vouchers, MB for works | Agency books |
| C6 | Utilisation Certificate (UC) back to the Centre | SNA, then the state department | UC, a statement that the money was used for its purpose, plus the unspent balance and interest earned | Union ministry; next instalment depends on it (SFAR 24-25 para 2.7.1.3) |
| C7 | Interest | SNA | Interest on balances refunded to the Centre and the state "by first week of April" | (SFAR 23-24 para 3.8.2.7) |

**Side channel.** The Centre also sends money **directly to state-level implementing agencies, bypassing the state budget**: Rs 22,308.76 crore in 2023-24 (SFAR 23-24 para 4.4).

### Route D. Money to local bodies

**D-1. Panchayats.** Karnataka has a three-tier panchayat system. The Zilla Panchayat works at district level, the Taluk Panchayat at taluk level, and the Gram Panchayat (GP) at village level.

| # | Step | Who acts | Document | Where recorded |
|---|---|---|---|---|
| D1 | State grants: district-sector schemes and statutory State Finance Commission devolution | FD, then Rural Development and Panchayat Raj Department (RDPR), then Zilla and Taluk Panchayats | Link documents (the district-sector budget); releases | Zilla Panchayat and Taluk Panchayat **"Fund II"** accounts. SFAR 24-25 notes Rs 5,000 crore of unspent balances in these accounts was "written back" in 2024-25 (Executive Summary). |
| D2 | Fifteenth Finance Commission (XV-FC) grants | Ministry of Panchayati Raj, then the state (to be passed on within a set time), then panchayats | Basic (untied) and tied grants | **eGramSwaraj**, the national panchayat accounting portal, linked to PFMS. Payment is supposed to go only through the eGramSwaraj-PFMS link. The CAG Local Bodies report on the period ended March 2024 has a chapter on non-compliance with that link (contents page). |
| D3 | GP planning | Gram Sabha and GP | Gram Panchayat Development Plan; action plan | eGramSwaraj |
| D4 | MGNREGA wages | GP, Programme Officer (taluk), District Programme Coordinator | Work sanction, **muster roll** (attendance sheet, generated in NREGASoft), MB, **Fund Transfer Order (FTO)**, a payment order signed online | NREGASoft and the public NREGA MIS reports. Wages are paid by the Centre directly to workers' accounts. Material and semi-skilled wages come out of the State Employment Guarantee Fund, which carries a 25% state share. |
| D5 | MGNREGA social audit | Social Audit Unit (SAU), Gram Sabha | Social audit report, Action Taken Report (ATR), recovery | NREGA MIS reports R9.x; Karnataka Social Audit Rules 2011 (MGNREGS PA para 6.4) |
| D6 | Local audit | Karnataka State Audit and Accounts Department (primary auditor); CAG technical guidance | Audit reports; CAG Local Bodies reports | cag.gov.in |

**D-2. City corporations.** This covers BBMP, the Bruhat Bengaluru Mahanagara Palike, and from 2025 the Greater Bengaluru Authority (GBA) and its city corporations; the GBA transition details are not verified in this draft.
- **Money in.** City corporations raise own revenue: property tax and fees. They also get state grants, such as Amruth Nagarothana and special Bengaluru grants, and central or CSS money such as AMRUT 2.0 ("Urban Rejuvenation Mission - 500 Cities", SFAR 24-25 para 2.6.1E), XV-FC urban grants and Smart City.
- **Money out.** The corporation has its own budget. Works go through engineers, tender, work order, MB and bill. Payment is made by the corporation's own finance system, not by the state treasury.
- **Smart City is a special case.** The money goes to a **Special Purpose Vehicle (SPV)**, which is a company. CAG found SPVs passed Rs 153.38 crore directly to departments against central rules (Smart City PA para 3.5.2).
- **Bengaluru payment records.** The bill-level analysis (bill splitting under Rs 5 lakh, repeated bill IDs) is being done by another session. See that work.

### Route E. Money that leaves the budget into companies, boards, corporations and societies

| # | Path | Example | What the state accounts show | Where the money really is |
|---|---|---|---|---|
| E1 | Grant-in-aid to a board or society | Kalyana Karnataka Region Development Board (KKRDB); Skill Mission; Sports Authority | "Expenditure" when the grant is drawn | Board's bank or PD account. The board then releases advances to implementing agencies such as KRIDL, Nirmithi Kendra and PWD. KKRDB "treated the advances made to the implementing agencies also as final expenditure" (KKRDB PA para 5.1). |
| E2 | Deposit works | Departments drawing money and handing it to construction agencies: Karnataka Housing Board, KRIDL, RITES | "Expenditure" | Advance sitting with the agency. There was "no mechanism in place to ascertain the progress of expenditure" (SFAR 23-24 para 3.8.1.6(d)). |
| E3 | Equity and loans | Irrigation corporations: Krishna Bhagya Jala Nigam (KBJNL), Karnataka Neeravari Nigam (KNNL), Visvesvaraya Jala Nigam (VJNL), Cauvery Neeravari Nigam (CNNL); public sector undertakings | Capital outlay or loans | Company books, audited by the CAG and Chartered Accountants |
| E4 | **Off-budget borrowing (OBB)** | The corporation borrows from the market or banks; the state repays principal and interest from its budget | Not in the state's debt figures. Only disclosed in budget papers and the Medium Term Fiscal Plan. | Rs 14,154.91 crore outstanding on 31 Mar 2025 (SFAR 24-25 para 3.1) |
| E5 | Guarantees | State guarantees loans of 146 institutions | Contingent liability only | Rs 45,889 crore outstanding on 31 Mar 2025 (SFAR 24-25 para 1.5.6) |

### Route F. Where money sits after it is "spent"

| # | Place | How money gets there | Why it matters |
|---|---|---|---|
| F1 | **Personal Deposit (PD) accounts** (8443-106) | Transfer from the Consolidated Fund. This counts as expenditure. | Money no longer lapses at year end. KFC Article 286 says PD accounts fed from the Consolidated Fund should be closed at year end. |
| F2 | Deposit heads (8443 Civil Deposits, 8449 Other Deposits) | Deductions such as the construction cess, security deposits and refunds | Can sit untransferred; the cess was Rs 640.44 crore at 31 Mar 2025 (SFAR 24-25 para 3.2.3) |
| F3 | Suspense and remittance heads (8658, 8782) | Items not yet matched between treasury, divisions and the AG | Public Works Remittances: Rs 964.68 crore debit at 31 Mar 2025 |
| F4 | Bank accounts of SNAs, corporations, boards and societies | Grants, CSS transfers | Outside the treasury. Balances counted as spent. |
| F5 | Minor Head 800 "Other Expenditure" | Booking choice | Hides what the money was for |
| F6 | Abstract Contingent (AC) bills | Advance drawn without vouchers | Spent in the accounts, with detail to follow |

---

## Part 2. The leak points

**Read this first.** These are control failures that the auditor documented. The rupee figure is the amount the CAG says was affected: unreconciled, unaccounted, irregular, or at risk. It is **not** an amount stolen, unless the CAG itself uses words like "misappropriation" or "fraudulent", and those are quoted. The same records with sources and URLs are in `leak_points.json`.

### 2.1 Leak-point table

| ID | Route / step | Leak point (plain words) | How it works | Control that should stop it | Evidence (CAG, Karnataka) | Rs crore |
|---|---|---|---|---|---|---|
| A-1 | A2-A3 | Money released before the Legislature approves it | FD issues "additionality" executive orders mid-year; supplementary grants approve them later | Art. 266(3); PAC 2015 advice to limit this to emergencies | SFAR 24-25 para 2.5.1.1: "10,035.13 crore covering 21 grants ... was released through 118 executive orders". Para 2.5.1: 261.75 crore spent in 15 cases "without having any provision in the original budget estimates/ supplementary demands and without issuing any re-appropriation orders". | 10,035.13 |
| A-2 | A2 | Spending more than the Legislature voted | Departments overspend a grant, to be regularised years later | Art. 205; PAC | SFAR 24-25 para 2.5.2: "excess disbursement of 4,388.75 crore over the authorisation ... under three grants during 2024-25". Para 2.8: 5,175.21 crore for 2020-21, 2022-23 and 2023-24 "are yet to be regularised". | 4,388.75 |
| A-3 | A3-A9 | March rush and last-day shuffles | Funds pushed out in the last weeks so they don't lapse; re-appropriation (shifting money between heads) on 31 March | GFR 62(3); FD instructions of 9 Sept 2004 | SFAR 24-25 para 2.5.8: Rs 72,958.85 crore (18.94%) spent in March 2025; **Rs 10,093.17 crore on 31 March 2025 alone**. Para 2.8: "re-appropriation orders amounting to 33,106.23 crore were issued on last day of the year". | 10,093.17 (last day) |
| A-4 | A8 | Advances drawn without vouchers (AC bills not followed by DC bills) | A DDO draws cash on an Abstract Contingent bill. The supporting Detailed Contingent (DC) bill, also called the Non-payment Detailed Contingent (NDC) bill, never arrives. | Manual of Contingent Expenditure Rule 37(b)(3): DC bill due by the 15th of the next month | SFAR 24-25 para 3.4: 1,111 AC bills, Rs 63.90 crore pending at 31 Mar 2025; 638 bills (Rs 36.86 crore) date from 2023-24 or earlier. "Non-adjustment of advances for long periods is fraught with the risk of misappropriation." Biggest: Elections Rs 32.1 crore, Police Rs 18.37 crore. SFAR 23-24 para 4.6: 934 bills, Rs 45.58 crore. | 63.90 |
| A-5 | A3 then E2 | "Spent" money is really an advance to a construction agency | Department draws the full amount and hands it to KHB, KRIDL, RITES or PWD; the books show it as spent | KFC UC rules; monthly expenditure statements (Budget Manual forms 15A and 15B) | SFAR 23-24 para 3.8.1.6(d): "there was no mechanism in place to ascertain the progress of expenditure ... the expenditure amount in the budget refers only to the transfer of funds to the implementing agencies and not the actual expenditure". Example: polytechnic and engineering college works, Rs 445.90 crore over 2021-24. | 445.90 |
| A-6 | A5 | Tendering rules bent | Short bidding times, non-standard tender documents, bid capacity not checked, direct award under 4(g) beyond the exempt limit | KTPP Rule 17; standard tender documents; 4(g) limits | Yettinahole PA para 3.2.1, Table 3.4: short-term tenders gave "bidding time of 9 to 33 days only", including "14 turn-key contracts valuing 8,989.09 crore"; "52 out of 53 works awarded on short-term tender basis were remaining incomplete". KKRDB PA para 5.2.11: "the Board had released the funds to KRIDL in violation of the provisions of the KTPP act" (amount not legible in the text copy). | 8,989.09 (value tendered) |
| A-7 | A4-A5 | Splitting works to stay under sanction or tender limits | One job cut into several smaller "works" so a lower officer can approve it, or so it avoids tender | Delegation tables; KTPP Sec 4(e) limits | MGNREGS PA para 5.6: "13 GPs had split 65 works (estimated cost of 42.15 crore) into 463 works with cost ranging from 2.41 lakh to 10 lakh", "irregular expenditure of 28.17 crore ... without obtaining the sanction of competent authority"; photos "appeared to be taken from existing/old photographs". Bengaluru bill-splitting under Rs 5 lakh: see the other session. | 28.17 |
| A-8 | A7-A9 | Overpaying the contractor | Recoveries not made, wrong price-escalation indices, items paid twice, security released early | Contract clauses; check measurement; Executive Engineer and Accounts scrutiny | Yettinahole PA: para 3.2.2.2, non-recovery of excess pipe, "excess benefit to the contractors amounting to 181.21 crore"; para 3.2.2.4, "excess payment of 27.73 crore"; para 3.2.2.5, "excess expenditure amounting to 21.02 crore"; para 3.2.2.6, retention money of 35.36 crore released early and further security deposit of 64.60 crore released, "undue financial favour to the Contractor". | 181.21 (largest single) |
| A-9 | A7 | Paying without proper measurement, or on fabricated records | MB not written up, no check-measurement, recycled photos, muster rolls made outside the official system | KPWD Code; MGNREGA Operational Guidelines para 7.13.2 | MGNREGS PA para 5.14.3: weekly measurement not done in 38% of test-checked works; check measurement not done in 163 of 400 (41%). Para 5.14.7: wages of "4.21 crore made on these musters was not only questionable but was also doubtful" (unofficial muster rolls in 39 GPs). Para 5.2.2, "Fraudulent payment for housing works": Rs 1.19 crore in 653 cases, including 462 where houses were "already completed during previous periods". | 4.21 + 1.19 |
| A-10 | A9-A12 | Treasury, division and bank books do not match | Remittances by works divisions not acknowledged; bank scrolls missing; Controlling Officers do not reconcile | Monthly reconciliation; treasury, RBI and AG reconciliation | SFAR 24-25 para 3.7: Public Works Remittances debit of Rs 964.68 crore "due to non-reconciliation ... these differences could lead to non-detection of cases of defalcation". Para 3.9: cash balance "unreconciled difference of 1,443.23 crore". Para 3.8: 82 Controlling Officers had not reconciled expenditure in 2024-25. SFAR 23-24 para 4.11: difference of Rs 4,636.81 crore at Mar 2024. | 964.68 / 1,443.23 |
| A-11 | A4-A7 | Projects started and never finished; assets idle | Work begins before land is acquired or funds are secured; costs escalate; assets rot | KPWD Code bar on tendering before land; FMRC (state fiscal monitoring committee) advice to fund near-complete works first | SFAR 24-25 para 1.6.2(B): 4,328 incomplete projects, estimated Rs 11,500 crore, "Capital Expenditure of 5,066 crore remained blocked"; 276 shown incomplete over pending bills of Rs 2,298 crore. Yettinahole PA para 3.1.2: Phase-I assets of Rs 2,965.77 crore idle; para 2.1: cost up from Rs 8,323.50 crore to Rs 23,251.66 crore. | 5,066 |
| A-12 | All | Known loss cases left open | Cases of misappropriation, loss or theft not closed for years | KFC para 349 (personal liability) | SFAR 24-25 para 3.12: "41 cases of misappropriation, losses, theft, etc., involving 149.83 crore were pending"; 14 cases more than 10 years old; HESCOM (Hubli Electricity Supply Company) 4 cases, Rs 115.47 crore. SFAR 23-24 para 4.17: 47 cases, Rs 43.19 crore. | 149.83 |
| B-1 | B7 / F1 | Year-end grants to welfare corporations parked to avoid lapse | Department releases in the last quarter and tells corporations to draw within 10 days and deposit in PD accounts | KFC Art. 286; FD 2004 instructions | SFAR 24-25 para 2.5.8.1: Rs 760.25 crore released to 20 corporations (Scheduled Caste, Scheduled Tribe and Backward Classes welfare) in Q4 2024-25, "depositing them in the PD Account to avoid the lapse of funds". Para 2.7.1.2(A): Rs 145 crore moved on 30 Mar 2025 from a "vacant posts" provision; "mere parking of funds to avoid lapse of grants"; unused until August 2025. | 760.25 |
| B-2 | B7 | Grants shown as spent but sitting in corporation banks | Corporations do not spend; money stays outside government accounts | Grants-in-aid register (KFC Art. 162(c)); UCs | SFAR 24-25 para 2.7.1.2(B): "un-utilised grant of 412 crore remained in the bank accounts of the Corporations ... in-spite of being shown as expended". Para 2.7.1.5: 32 bank accounts with Rs 410.43 crore kept open despite the FD order of Feb 2023 to close them. Para 2.7.1.6: three of four welfare departments kept no grants-in-aid register. | 412.00 |
| B-3 | B2-B3 | Ineligible or ghost beneficiaries | Weak identity and eligibility checks; job cards not updated | Aadhaar and eligibility checks; annual updating of job cards | CA 6/2025 para 2.1 (Skill Mission): "3,487 were ineligible as they exceeded the age limits". MGNREGS PA ch. IV: low active job cards "could be attributable to the existence of ghost workers"; unpaid material dues of Rs 723.44 crore "raised the possibility of ghost workers and fake bills". **No CAG audit of duplicate beneficiaries in the five guarantee schemes was found.** | not quantified |
| C-1 | C3 | SNA transfers that don't match; balances parked in SNA banks | State short-releases or over-releases shares; SNA balances are counted as spent | SNA guidelines (March 2021): transfer within 21 days | SFAR 24-25 para 2.6.2: Saksham Anganwadi, short release of state share Rs 409.99 crore and Centre's share transferred differs by Rs 409.74 crore between the accounts (VLC) and PFMS; Urban Rejuvenation, short release Rs 97.83 crore; health, "Excess amount of 263.55 crore has been transferred as State share"; Rs 144.59 crore central commodity assistance not released to the SNA. Balances outstanding in five SNAs at 31 Mar 2025 total Rs 1,242.41 crore. "Reply is awaited." | 409.99 |
| C-2 | C3-C6 | "Expenditure" that comes back as refunds | Money booked as spent comes back from SNA accounts in later years | Real-time release (SNA-SPARSH) | SFAR 23-24 para 3.8.1.6(g): Samagra Shiksha refunds of Rs 2,171.03 crore (Avalokana, a state decision-support system) against Rs 1,393.28 crore (accounts): "the expenditure reported in the previous years was merely a transfer of funds". SFAR 23-24: revenue expenditure "understated by 2,256.06 crore on account of refunds of unutilized amounts from SNA Accounts". | 2,171.03 |
| C-3 | C1 | Central money that bypasses the state budget | Centre pays agencies directly | Policy since 2014-15 to route through the state budget | SFAR 23-24 para 4.4: "GoI transferred 22,308.76 crore directly to the implementing agencies", of which 8,873.10 crore was for CSS, "bypassing the Consolidated Fund of the State". | 22,308.76 |
| C-4 | C6 / E1 | Utilisation certificates not given | Grantee never proves use | KFC Rule 161: UCs within 18 months | SFAR 24-25 para 3.3: 142 UCs, Rs 239.45 crore outstanding (Medical and Public Health Rs 225.64 crore). SFAR 23-24 para 4.5: "around 90 per cent of the grants-in-aid organisations are out of ambit of monitoring". CA 1/2026 para 2.1.2.5: sports bodies, Rs 94.40 crore. CA 6/2025 para 2.1: Skill Mission "could not obtain UCs for the balance amount of 136.54 crore". KKRDB PA para 5.2.5: Rs 64.07 crore. | 239.45 |
| C-5 | C7 / E1 | Interest on parked public money kept by the agency | Interest earned on grants not sent back to the treasury (head 0049) | FD orders of July 2003 and Aug 2019; CSS interest rules | SFAR 23-24 para 4.2: "had not remitted the interest earned amounting to 14,549.91 crore", 64 institutions. **Caution:** Appendix 4.1 shows Rs 11,850 crore of this (11,85,015 lakh) against the Karnataka Biodiversity Board alone, which looks implausible and may be a data error. Treat the total as unverified. Also: KKRDB PA para 5.2.6, "the implementing agencies subsumed the interest earned"; Smart City PA para 3.3, Rs 2.69 crore not remitted. | 14,549.91 (as stated; unverified) |
| D-1 | D4-D5 | MGNREGA money misappropriated, found by social audit, never recovered | Social audit finds it; cases are closed as "not recoverable" or left pending | Schedule I para 25(c)(ix) (recover within 6 months); Karnataka Social Audit Rules VIII(3)(c) | MGNREGS PA para 6.4.8: 79,284 misappropriation issues worth Rs 187.38 crore (2019-24). ATRs pending in 27,115 cases (Rs 75.30 crore). "an amount of 90.14 crore (80 per cent) was settled without any recovery". The claimed 94% recovery "was incorrect and misleading". Para 6.4.7: Rs 8,264.39 crore (48%) of spending could not be verified "for want of records". 91% of 3,55,393 observations still open (Oct 2024). Short reporting of misappropriation by Rs 59.84 crore between MIS and the SAU annual reports. | 187.38 |
| D-2 | D4 | Late state releases to the MGNREGA fund | State sits on the central and state shares | Release norms | MGNREGS PA ch. III: delay "entailed a penal interest of 36.26 crore"; inadmissible expenditure Rs 32.78 crore. | 36.26 |
| D-3 | D1-D2 | Local-body balances swept back or unused | Unspent balances in Zilla and Taluk Panchayat Fund II written back to help the deficit; XV-FC grants unspent | Finance Commission conditions | SFAR 24-25 Executive Summary: fiscal deficit target met "by writing back the unspent balances of 5,000 crore in the PRIs Fund II account and refund of unspent balances in the State Nodal Agency (SNA) account (1,333 crore)". XV-FC unspent Rs 1,764.83 crore and diversion in 261 GPs (Rs 4.25 crore): **news only (Organiser, Aug 2026), low confidence**, from a 2026 local bodies audit not read in the original. | 5,000 |
| D-4 | D-2 (cities) | Smart City SPVs passing money to departments; overpaying consultants | SPV gives money to a department instead of paying contractors against milestones | MoHUA (Union housing ministry) instruction of Jan 2019 | Smart City PA para 3.5.2: "153.38 crore was transferred to the departments/agencies in contravention of MoHUA instructions". Ch. 3 summary: "excess payment of 2.56 crore" to the Project Management Consultant (PMC). | 153.38 |
| E-1 | E4 | Off-budget borrowing | Corporations borrow; the state repays from the budget; this is outside debt limits and accounts | KFRA 2002 as amended 2014 (Karnataka Fiscal Responsibility Act); Art. 293(3) | SFAR 24-25 para 3.1: outstanding OBB Rs 14,154.91 crore, including Rs 5,257.70 crore borrowed through Power Company of Karnataka to securitise GP dues. SFAR 23-24 para 2.7.1.1: "All the seven entities ... do not have their own source of revenue and are incurring losses". Para 4.1: "the accounts of the State Government is therefore not complete to that extent". | 14,154.91 |
| E-2 | E5 | Guarantees | State backs loans that may fall due on it | Karnataka Ceiling on Government Guarantees Act 1999 | SFAR 24-25 para 1.5.6: outstanding Rs 45,889 crore (31 Mar 2025). SFAR 23-24 para 2.8.2: only Rs 306.69 crore of Rs 647.70 crore guarantee commission received. | 45,889 |
| E-3 | E1 | Boards and bodies that don't produce audited accounts | No auditor appointed; accounts years late; departments don't report who got grants | Board orders; CAG (DPC) Act Secs 14 and 15 | KKRDB PA para 5.3.1: "the State Government has not appointed auditor for audit of the accounts of the Board since the constitution of the Board". Para 5.1: actual unspent balances with agencies "could not be assessed". SFAR 23-24 para 4.16: 13 departments did not report 1,065 grantee institutions. SFAR 24-25 para 3.11: 16 accounts of 9 autonomous bodies pending. | not quantified |
| E-4 | E1 | Board keeps unspent money above its limit | Carry-forward beyond 20% | KKRDB Board Order 2013, cl. 16(c) | KKRDB PA para 5.2.3: retained above the 20% limit every year after 2016-17. Para 5.2.2: "loss of assistance of 387.52 crore". | 387.52 |
| F-1 | F1 | Money parked in PD accounts | Year-end transfers into PD accounts; balances carried over; negative balances | KFC Art. 286 and 286A | SFAR 24-25 para 3.5: closing balance Rs 29,770.45 crore (Rs 22,115.31 crore of it is KMERC, the Karnataka Mining Environment Restoration Corporation, under a Supreme Court order). Rs 6,026.22 crore moved into PD accounts in March 2025. 25 accounts inoperative for more than 3 years. Negative balances Rs 1,911.92 crore. Para 3.14: "Retention of such large sums of money was against principle of Legislative financial control." | 29,770.45 |
| F-2 | F5 | Hiding spending under "Other Expenditure" | Booking to Minor Head 800 even where a proper head exists | Accounts classification rules | SFAR 24-25 para 3.6: Rs 7,588.39 crore under 31 Major Heads; Rs 2,532.53 crore "despite availability of appropriate Minor Heads"; it "renders the accounts opaque". SFAR 23-24 para 4.8: Rs 10,836.47 crore. | 7,588.39 |
| F-3 | F2 / F4 | Deductions and bank balances held back | Cess not passed on; inoperative department bank accounts | BOCW Cess Act; FD bank-account directives (Jan 2017) | SFAR 24-25 para 3.2.3: cess balance of Rs 640.44 crore "required to be transferred to the Welfare Board". SFAR 23-24 para 3.8.2.6: forest divisions, 22 inoperative accounts with Rs 59.95 crore. | 640.44 |
| F-4 | A3 / budget | Revenue spending booked as capital | Misclassification that flatters the deficit | IGAS-2 (accounting standard for grants-in-aid); classification rules | SFAR 24-25 para 2.8: Rs 2,020.87 crore of revenue expenditure booked as capital; revenue deficit understated by Rs 1,948.41 crore. | 2,020.87 |

### 2.2 Do departments answer the auditor?

- **Inspection Reports pending.** "A total of 8,522 Inspection Reports containing 44,174 Paragraphs were outstanding against 47 departments as at the end of March 2023" (CA 6/2025, Overview, para 1.10.1). A later figure (March 2024 or 2025) could not be extracted from the PDF text.
- **Paragraphs pending before the PAC.** 204 as of 31 Mar 2025 (CA 1/2026, Chapter I). Three departments "did not submit ATNs for four paragraphs for the period 2020-21 and 2021-22 even as of 31 March 2025". ATNs are Action Taken Notes, which departments must send within four months of a report being tabled.
- **State finance reports.** Replies to the State Finances reports for 2022-23 and 2023-24 "is awaited" (SFAR 24-25 para 3.13).
- **Specific items with no reply.** The SNA mismatch tables in SFAR 24-25 para 2.6.2 repeatedly say "Reply is awaited".
- **Where the State did reply** (January 2026), it mostly promised action, for example: "persons responsible for non-submission of UCs to be held accountable" (para 3.3).

---

## Part 3. Backtracking: tracing one rupee from the ground to the budget line

**General method.** Start with the thing you can see, such as a road, a borewell or a person who should have been paid. Get its **identifier**: work ID, job card number, beneficiary ID, agreement number. Then climb the steps of the route in reverse. At each step, ask for the document that the step creates (Part 1). For anything not online, file an RTI request under the Right to Information Act 2005 with the Public Information Officer (PIO) of the office that holds it. The state RTI portal is rtionline.karnataka.gov.in (not verified that it covers every office); a paper application to the PIO always works.

### What is public online, what needs RTI, and what is not public

| Record | Route | Status | Where |
|---|---|---|---|
| Budget books, link documents, Medium Term Fiscal Plan, budget overview (lists off-budget borrowing) | All | **Public** | Finance Department, finance.karnataka.gov.in (URL not re-checked for this draft) |
| Finance Accounts (Vol I and II: PD balances, Minor Head 800, guarantees, incomplete projects in Appendix IX) and Appropriation Accounts | All | **Public**, yearly, about 9-12 months late | cag.gov.in, AG Karnataka pages |
| CAG audit reports (SFAR, performance and compliance audits) | All | **Public** after tabling | cag.gov.in/en/audit-report and the AG Karnataka sub-site |
| CAG Inspection Reports, draft paragraphs | All | **Not public as a rule.** Whether RTI works is not confirmed. | AG (Audit), Bengaluru |
| Tender notices, bid lists, award details (KPPP) | A, D, E | **Public** for tenders on the portal. Works under Rs 5 lakh or 4(g) direct awards **may not appear**. | kppp.karnataka.gov.in |
| Administrative approval and technical sanction orders, estimates | A | **RTI** (some departments publish Government Orders) | Executing division |
| Agreement, work order, MB, check-measurement records, RA bills, deductions | A, D | **RTI only.** The MB is the key document. Ask for certified copies plus the site inspection. | Executive Engineer, Assistant Executive Engineer |
| Treasury voucher, payment date and amount to the contractor | A | **RTI** to the DDO or treasury. Khajane-II has no public payment search that we could confirm. | DDO, District Treasury |
| Bengaluru city bill and payment lists | D-2 | Partly public (city finance pages). **See the other session's work**; not repeated here. | — |
| DBT scheme aggregates (beneficiaries and amounts by district) | B | **Public dashboards** for some schemes; the content and URL are not verified | State DBT portal (unverified) |
| Beneficiary lists with names | B | Mostly **RTI**, and personal data may be refused under RTI s.8(1)(j). Some lists are read out or displayed at Gram Sabhas. | Department, GP |
| Payment success and failure files, bank return files | B | **Not public.** RTI may give aggregates. | Department, banks |
| Welfare corporations' annual accounts, PD account statements, bank balances | B, E, F | Annual accounts: sometimes in Legislature papers or on websites. **PD ledgers and bank statements: RTI.** Account-level PD figures are in Finance Accounts Vol II (Appendix) — **public, but in aggregate**. | Corporation; AG (A&E) |
| PFMS releases to the state and SNA (scheme-wise) | C | **Partly public** (PFMS public reports on releases); SNA account-level transactions **not public** | pfms.nic.in |
| Utilisation certificates | C, E | **RTI** to the sanctioning department; UCs for CSS go to the Union ministry (RTI there too) | Department; Union ministry |
| MGNREGA: job cards, muster rolls, FTOs, works, geo-tagged photos, MIS R-reports including social audit (R9.x) and misappropriation recovery (R9.2.6) | D | **Public online**, down to the individual job card and muster roll | nrega.nic.in (MIS reports) |
| MGNREGA social audit reports, ATRs | D | Social audit reports: **public** through the MIS and Gram Sabha; Taluk ad-hoc committee decisions and Gram Sabha closures: **no public data** (MGNREGS PA para 6.4.8(i)(d)) | NREGA MIS; Social Audit Unit Karnataka |
| XV-FC grant plans and payments by panchayat | D | **Public**: plans, vouchers and payments where routed through the portal. Payments by cheque outside the portal **will not show**. | egramswaraj.gov.in |
| State panchayat accounts and the Karnataka GP software | D | Partly public *(Panchatantra 2.0, URL and content unverified)* | RDPR |
| Board and society accounts (KKRDB and others) | E | KKRDB has had **no statutory audit** since it was set up (KKRDB PA para 5.3.1). Ask by RTI for the internal audit reports and the Hykasoft (KKRDB's works and payments software) works-and-payments data. | KKRDB, Kalaburagi |
| Off-budget loan agreements of corporations | E | **Not public.** Totals are in the budget overview and Finance Accounts; company annual reports carry the loans. RTI to the company (public authority). | KBJNL, KNNL, VJNL, CNNL and others |
| Avalokana (state decision-support system for releases and sanctions, cited by CAG) | All | **Not public** (internal government system, as far as we know) | FD |

### Route-by-route backtracking recipes

**A. A road or building.**
1. Start with the board at the site: work name, agency, cost, contractor. Find the tender on KPPP using the work name or the tender ID.
2. If it is not on KPPP, it may be under Rs 5 lakh or a 4(g) direct award. Ask the division by RTI for the "work register entry, administrative approval, technical sanction, agreement, MB pages, RA and final bills, and treasury voucher numbers with dates and deductions".
3. The administrative approval names the head of account. Check that head in the budget book and in the Appropriation Account for that year: was it overspent, re-appropriated on 31 March, or booked under 800?
4. If a corporation or KRIDL did the work, ask the department for the release order and UC, and ask the agency for the "deposit work" ledger.

**B. A beneficiary.**
1. Get the person's application or acknowledgment number and bank passbook entries.
2. RTI to the department or corporation for the sanction list for that GP or ward, and the payment file reference.
3. If the scheme runs through a corporation, ask for the grant release order (head of account), the PD account statement and bank statements for the quarter. CAG shows money can wait there for months (B-1, B-2).

**C. A CSS-funded asset.**
1. Find the scheme name and component.
2. On PFMS public reports, find the central release for the state and year.
3. In Finance Accounts, find the state-linked scheme head and the transfer to the SNA.
4. RTI to the SNA for the account balance at 31 March, the interest earned and remitted, and UCs sent. Compare with the CAG tables in SFAR 24-25 para 2.6.2.

**D. A panchayat work.**
1. For MGNREGA, start from the work code on nrega.nic.in: muster rolls, FTOs, material bills, geo-tag stages, then the social audit report and ATR (R9.x).
2. For XV-FC, start from eGramSwaraj vouchers for that GP.
3. Ask the GP by RTI for the cash book, cheque register and MB. CAG found XV-FC payments made by cheque outside the portal (news, low confidence) and photos recycled across works (MGNREGS PA para 5.6).

**E. Board or corporation money.**
1. Start with the board's annual action plan (KKRDB publishes it; unverified) and its works list.
2. RTI to the board for releases to each implementing agency and the agency's UC and interest refunds.
3. For off-budget loans, read the budget overview and Finance Accounts statement on OBB and guarantees; then the company's annual report.

**F. Parked money.**
1. Finance Accounts Vol II gives PD balances by administrator. SFAR 24-25 Table 3.8 already lists the largest: KMERC Rs 22,115.31 crore, Deputy Commissioners' accounts, Land Acquisition Officers, the KKRDB Secretary and others.
2. RTI to the administrator for the PD ledger and the FD permission to keep the account open past year end (KFC Art. 286).

---

## Part 4. The treasury: what is locked in, what is owed, what the answers say (added 20 Nov 2026)

Source: research/treasury/FACTS_DRAFT.md (compiled by the "Urban analysis with maps" session from CAG, PRS and Assembly answers; full citations there). Rs crore. **Checked at source** means this session re-read the figure on the original PDF on 20 Nov 2026.

### 4.1 Money that is spoken for before the year starts
- Salaries, pensions and interest: 1,16,479 in 2024-25, 45.1% of revenue receipts (CAG SFAR 2024-25, Table 1.18). With explicit subsidies: 64.5%.
- CAG's own words: committed spending plus all subsidies is "nearly 77 per cent" of revenue receipts, and 82% once the State's share of central schemes is added (SFAR 2024-25, para 1.6(A); Executive Summary).
- The five guarantee schemes: 52,525.60 in 2024-25, about 20% of revenue receipts (SFAR25 Table 1.20; page check of the budget column pending).

### 4.2 Borrowing that is not in the budget, and promises the State has underwritten
- Off-budget borrowing outstanding: 14,154.91 at 31 Mar 2025, through seven corporations including the irrigation nigams and Power Company of Karnataka (5,257.70, "securitization of Gram Panchayat dues"). CAG: these entities "do not have their own source of revenue and are incurring losses" (SFAR24, para 2.7.1.1).
- Guarantees outstanding: 45,889 at 31 Mar 2025, 34,749 of it for power (SFAR25, Table 1.33).

### 4.3 Bills the State owes contractors (official, replaces the press figures)
- **Checked at source:** LAQ 401, answered 9 Dec 2025 by the Chief Minister (question by Basanagouda R. Patil Yatnal): pending bills Water Resources 17,533; Public Works 8,804; Minor Irrigation 3,762; RDPR 2,534; Urban Development 2,403; Health 200. Sum 35,236. On corruption in bill payment: no provable cases have come to notice.
- LAQ 6 (9 Dec 2025): 3,612.44 pending across the Greater Bengaluru city corporations; the paid figure 11,583.34 has no unit printed and the annexures are missing from the PDF. LAQ 1355: PWD pending 8,804.45 in the text, 8,804.41 in the head-wise annexure; the paid period ends on a printed "31-11-2025". (Second read: research/treasury/ASSEMBLY_ANSWERS_VERIFIED.md.)
- CAG's only comparable figure is 2,298 behind 276 incomplete works (SFAR25, para 1.6(B)), a narrower scope.

### 4.4 Where the government's answers and the auditor differ
- **Capital expenditure. Checked at source:** LAQ 1658 (17 Mar 2026, Chief Minister; question by S. Suresh Kumar) gives 61,204 (2022-23), 56,852 (2023-24), 68,233 (2024-25), 83,200 (2025-26) and says capital expenditure has not decreased. CAG gives 57,349, 52,120, 57,906 and says 2023-24 capital expenditure "decreased by 5,229 crore". The gap for 2023-24 equals loans and advances (4,473) plus about 259; the answer does not define its figure. Frame as "two official figures, different definitions", not as a false statement.
- **Update (second read, ASSEMBLY_ANSWERS_VERIFIED.md):** the Chief Minister's own answers give capital expenditure three ways. LAQ 422 (9 Dec 2025): 57,953.20 / 52,378.86 / 60,601.15 / 81,554.38 for 2022-23 to 2025-26. LAQ 1658 (17 Mar 2026): 61,204 / 56,852 / 68,233 / 83,200. LAQ 907: 56,851 for 2023-24. LAQ 422 is close to CAG (52,120 for 2023-24). So the story is "the same government gave the Assembly two different capital-spending series three months apart", and only the later, higher one says spending has not decreased. The 17.5% interest share in LAQ 1658 is a budget estimate.
- **SC/ST sub-plan money in the guarantees. Checked at source:** LAQ 1777 (16 Dec 2025, Chief Minister; question by V. Sunil Kumar). Asked whether SCSP and TSP money was used for the five guarantees, the answer is "Yes". Annexure 1: 2023-24 SCSP 6,845 + TSP 3,081; 2024-25 SCSP 9,971 + TSP 4,292; 2025-26 budget 9,513 + 3,921; to end November 2025 3,299 + 1,388. The answer says the allocation follows population share under Rule 7(C) of the sub-plan Act, and that community-wise beneficiary data is not available.
- Interest share and debt stock: the answers use budget-document figures, not CAG's; see the treasury file, section D2.

### 4.5 New leak points for the table in 2.1 (spec sent to the Follow-the-rupee page owner)
- L33. Pending bills: works done, bill unpaid. The queue is where "commission for release" is alleged. Official stock 35,236 (LAQ 401). Trace: the department's bill register by RTI; the order of payment against the order of submission.
- L34. Sub-plan money counted for a general scheme: 14,263 of SCSP/TSP in the guarantees in 2024-25 (LAQ 1777). Lawful under Rule 7(C) as the answer states; the question is whether SC/ST households got that share, and the government says it does not have the data. Caution: the Finance answer (LAQ 1777) and the Social Welfare answer (LAQ 2550) give different SCSP/TSP guarantee figures for the same years; quote each with its source, never one as "the" figure.
- L35. Capital-expenditure figures that change between the government's own answers (LAQ 422 vs 1658) and against the audit. Trace: the Finance Accounts capital heads against the answer.

### 4.6 Where the auditor caught money leaving without the work (CAG compliance reports; added 20 Nov 2026)

Source: research/treasury/CAG_FINDINGS_DRAFT.md (about 150 findings, read once by the "Urban analysis with maps" session; Report 1/2026 read by OCR; NOT page-checked by this session; several carry Government replies that dispute them). These are the ground-level proof for leak points already in table 2.1 (measurement, payment, supply):
- L36. **Payment without the work.** Tank desilting, 137 works where the logbook "excavators" were two-wheelers and cars; CAG: "probable embezzlement" (Rs 3.22 cr; R4/2026 para 3.10). PWD Yadgir: the same 925 m paid under two works (Rs 1.33 cr; Government disputes). KBJNL Shorapur drain "not executed", measurement book manipulated (Rs 33.95 lakh). KRIDL stadium items paid in full but not built or supplied.
- L37. **Advance or payment on paper.** KNNL 70% advance for pipes on "fraudulent invoices" (Rs 40.16 cr; PSE-R1/2025 para 6.12). KEONICS paid "without actual delivery" (Rs 9.36 cr) and on fake challans and forged reports (Rs 85.98 cr). ESIS Bagalkote: 902 fake reimbursement claims (Rs 4.03 cr).
- L38. **Measured too fast to be real.** PWD Ballari and Koppal concrete works measured and paid within 1 to 21 days of the agreement (Rs 21.32 cr; R3/2025 para 3.2).
- L39. **Money collected for a purpose, never passed on.** BBMP health cess not remitted, Rs 1,275.18 cr, plus library and beggary cess (ATIR 2020-22 para 2.10.5).
Before any of these is quoted: open the CAG page cited, copy the sentence, and include the Government's reply where the report prints one.

### 4.7 Irrigation: the biggest single pool of owed money (added 20 Nov 2026)

Source: research/treasury/IRRIGATION_MONEY_DRAFT.md (113 items, "Urban analysis with maps" session; Assembly answers read once from scans, not second-read; not page-checked by this session).
- Pending bills in the four irrigation Nigams on 24 Mar 2026 (LAQ 3223): KNNL 6,164.50; VJNL 4,993.16; KBJNL 3,760.12; CNNL 3,629.38; total 18,547.16.
- The four Nigams hold Rs 7,278 cr (51%) of the Rs 14,155 cr off-budget borrowing; Power Company of Karnataka holds Rs 5,258 cr. (Say "half", not "most".)
- Upper Bhadra: Rs 5,300 cr provided in the Union Budget 2023-24, nothing released to Dec 2025 (Lok Sabha USQ 3200); the State had spent 11,375 by Feb 2026.
- UKP Stage III: 1,04,301 of 1,33,867 acres still to be acquired (LAQ 419).
- Yettinahole (CAG): seven contractors hold 67% of 43 works by number (by value, about 66.7% of all 55 contracts, derived); Rs 181.21 cr not recovered for pipeline not laid.
- Leak point L40: lump-sum or advance payments not reduced when the scope shrinks (Yettinahole pipeline; see also KBJNL and MI Koppal in 4.6).

### 4.8 Money meant for panchayats, disasters and mining districts (added 20 Nov 2026)

Source: research/treasury/CAG_FINDINGS_2_DRAFT.md (158 findings from CAG reports 8/2025, 7/2025, 6/2025, 10/2024, 4/2024, 13/2025; one read; Report 10/2024 by OCR; not page-checked by this session).
- L41. **Devolution held back:** Rs 43,782 cr less to panchayats than the State Finance Commission recommendations the government accepted (Report 10/2024, OCR-read: check the page first).
- L42. **Central money lost to a delayed election:** Rs 369.45 cr of 15th Finance Commission grants lost because Zilla and Taluk Panchayat elections were not held.
- L43. **Disaster money without accounts or unused:** Rs 5,791 cr of drought spending with no district-wise details or utilisation certificates; Rs 421.60 cr of the disaster mitigation fund unused (Report 8/2025).
- L44. **Mining-district fund off its rules:** District Mineral Foundation Rs 300.44 cr spent on works "not envisaged in the guidelines" (Ballari, 169 works); Rs 433.20 cr of sanctioned works never started (Report 7/2025).

## What could not be confirmed

1. **Rule numbers in the Karnataka Treasury Code, Financial Code and Budget Manual** were not checked against the current texts. Only rules quoted inside CAG reports are cited with confidence: KFC para 14, Rule 161, Arts. 162(c), 286, 286A and 349; Manual of Contingent Expenditure Rule 37(b)(3); KPWD Code Rule 202; KBM para 110 and Rule 264.
2. **Khajane-II public access.** Whether any public payment-search exists was not confirmed.
3. **Current KTPP thresholds.** The text read is a consolidated version on casemine; the India Code PDF returned 403. Later amendments (for example the SC/ST limit reported as raised to Rs 1 crore) are not confirmed.
4. **The Rs 14,549.91 crore unremitted-interest figure** (SFAR 23-24 para 4.2). About 81% of it sits in one appendix row (Karnataka Biodiversity Board, 11,85,015 lakh), which looks implausible. Treat it as reported, not verified.
5. **2026 Local Bodies audit of XV-FC grants**: Rs 1,764.83 crore unspent; diversion in 261 GPs. Seen only in news; the original was not read. Who performed that audit is also unclear.
6. **Up-to-date Inspection Report pendency.** The latest confirmed figure is March 2023 (8,522 IRs; 44,174 paragraphs).
7. **KKRDB report number**, and several rupee figures in KKRDB Chapter 5. The text copy lost digits, for example in paras 5.2.11 and 5.2.12.
8. **DBT ghost or duplicate beneficiaries in Karnataka's five guarantee schemes.** No CAG audit was found that tests this. CAG's SFAR chapters describe the schemes' fiscal cost and impact, not beneficiary-level checks.
9. **The DBT pipeline details** (state DBT platform, the family database, the Aadhaar payment bridge, how failed payments are handled) are described from general knowledge and are not sourced.
10. **The BBMP/GBA transition and the Amruth Nagarothana release mechanics** are not verified here. Bengaluru bill records are handled by the other session.
11. **The MGNREGS PA tabling date.** Inferred as March 2026 from news; its report-details page URL was not found. The PDF is cited.
