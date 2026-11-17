# LEAD (not a finding): consultancy bills bunched just under Rs 5 lakh

Status: DRAFT, found 17 Nov 2026 by the "Urban analysis with maps" session. Not for the site or any post until the procurement records below are seen. The pattern is in the corporation's own payment records; what it means is not yet known.

## What the records show

Source: BBMP work orders and payments 2024-25 and 2025-26 (OpenCity copies of accounts.bbmp.gov.in; files in `data/`), one row per bill ID (14,259 bills). Script: the analysis blocks recorded in this file's history; groups saved in `data/consultancy_split_groups.json`.

**1. A cliff at Rs 5 lakh, almost only for consultancy.** 1,397 bills are for consultancy (project reports, surveys, supervision and project management): Rs 102.4 crore. Counted in Rs 25,000 bands:

| Gross bill | Consultancy bills |
|---|---|
| Rs 3.00-4.75 lakh, each band | 21 to 52 |
| **Rs 4.75-5.00 lakh** | **231** |
| Rs 5.00-5.25 lakh | 16 |
| Rs 5.25-6.75 lakh, each band | 8 to 42 |

The single most common bill amount in the whole Rs 4.8-5.0 lakh range is exactly Rs 4,95,000 (69 bills). In ordinary pricing, amounts thin out smoothly; a pile-up just below a round number and a drop just above it usually means a rule applies at that number.

**2. One job, several bills, same day.** 58 times a consultant has two or more bills of Rs 4.5-5.0 lakh dated the same day (160 bills, Rs 7.81 crore). Many are different wards and may be genuinely separate jobs. Some plainly describe one project in pieces. Checked against the raw CSV rows:

| Bill IDs | Bill date | Each bill | What the descriptions say |
|---|---|---|---|
| 735712, 735714 | 31 Jul 2025 | Rs 4,95,000 | Survey and road inventory for "8 Major Roads ... under Package-3" (approved project cost Rs 50 crore), one bill for the Chamarajpete part, one for the Gandhinagara part |
| 735716, 735718 | 31 Jul 2025 | Rs 4,95,000 | Same survey for "6 Major roads ... under Package-04" (Rs 50 crore), one bill for Govindarajnagara, one for Rajajinagara and Malleshwaram |
| 563288, 563296, 563308 | 27 Feb 2023 | Rs 4,98,000; 4,98,000; 4,98,078 | Detailed Project Report for "Comprehensive development of Roads, Drains and other allied works in Malleshwaram division", work code 065-21-000001: the division as a whole, then Malleshwaram sub-division, then Mathikere sub-division |

Whole packages: Rs 9.9 lakh of survey for one Rs 50 crore package, paid as two bills each just under Rs 5 lakh; Rs 14.9 lakh of project report for one division, paid as three.

## The rule the line might relate to

The Karnataka Transparency in Public Procurements Act, 1999, section 4(e) as substituted by Act 21 of 2001 (text read in a copy of the Act and the Finance Department's clarification, keonics.in, and BBMP's own copy at site.bbmp.gov.in/PDF/kttpact_2000.pdf): for City Corporations the Act's tendering chapter does not apply to
- construction works of a value not exceeding **Rs 5 lakh**, and
- goods or services other than construction of a value not exceeding **Rs 1 lakh**.

Consultancy is a service. On that text, the no-tender limit for these bills would be Rs 1 lakh, and the Rs 5 lakh line would not exempt them. Three things could change that, and none is checked yet:
1. A later amendment or Finance Department order raising the services limit (searches found 4(g) exemptions and a 2023 change to section 6, nothing on 4(e) services; the current consolidated text was not read).
2. A specific exemption under section 4(g) for these works.
3. The corporation's own delegation of financial powers, under which an officer may approve consultancy up to Rs 5 lakh, with or without quotations.

## What this does NOT show

- The payment records do not say how any consultant was chosen. Every bill above could come from a tender or a quotation process. A gross bill is not the contract value, although for these one-off survey and report jobs it is likely to be the whole fee.
- Nothing here says any firm did anything wrong. Firms are named only because the public record names them; the question is about the corporation's procurement.

## How to settle it

1. **Karnataka e-procurement portal (kppp.karnataka.gov.in)**: search work codes 317-24-000023, 317-24-000028 and 065-21-000001 for tenders. The portal refused connections from outside India during this research; needs someone in India.
2. **RTI to the PIO of the West Zone (Road Infrastructure) office and the Malleshwaram division** (owner files): for bills 735712, 735714, 735716, 735718, 563288, 563296 and 563308, ask for (a) the work order or letter of award, (b) whether the consultant was chosen by tender, by quotations or by nomination, with the comparative statement if any, (c) the sanction order and the officer who approved it, and (d) the rule or order relied on for the procurement method.
3. **Ask the Finance Department (or check the gazette)** for the current text of KTPP Act section 4(e) and any order on the limit for consultancy services by urban local bodies.

If the awards were tendered, this closes. If they were nominated or quoted under a Rs 5 lakh limit, the pattern of one package paid in pieces is the story, with the corporation's answer alongside.
