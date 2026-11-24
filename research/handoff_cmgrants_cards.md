# Handoff to the site session: CM's grants on each report card (25 Nov 2026)

From the Follow the rupee / officials session. The site and index.html belong to the site session; this is a spec, not an edit. The finding is live on Follow the rupee (#cmgrants, commit 56ea265) and was read twice independently from the scanned answers.

## Data
`research/follow_the_money/cm_grants_by_seat.json`: `{"<constituency as in data/mlas.csv>": [cmidp_2025_26_crore_or_null, cm_special_grant_crore]}` for all 224 seats.
- First value: CM's Infrastructure Development Programme 2025-26, amount sanctioned (Assembly USQ 1727, 16 Dec 2025). `null` = the seat is not in the list (21 seats, incl. Varuna and the Speaker's Mangalore).
- Second value: works sanctioned under the CM's special grant in the two years before March 2025 (USQ 1119, 11 Mar 2025). `0` = not listed. Two listed rows have their seat names blacked out in the PDF and cannot be assigned, so a 0 for a non-Congress seat may be one of those two (say so if you show it).

## Suggested card box (EN)
Heading: "The Chief Minister's development grants for this seat"
- If cmidp is a number: "CM's infrastructure programme, 2025-26: Rs {c} crore sanctioned." If null: "Not in the CM's infrastructure programme list for 2025-26."
- Then: "Most seats held by the ruling party got Rs 50 crore; most opposition seats got Rs 25 crore."
- Special grant: if > 0: "CM's special grant, two years to March 2025: Rs {g} crore of works sanctioned." If 0: "Not listed for the CM's special grant in the two years to March 2025."
- Fine print: "Sanctions, not money spent. Source: the Chief Minister's answers to Assembly questions 1727 (16 Dec 2025) and 1119 (11 Mar 2025). How we read them: Follow the rupee" linking to reports/follow_the_money.html#cmgrants (KN page for KN).

## Suggested card box (KN)
- ಶೀರ್ಷಿಕೆ: "ಈ ಕ್ಷೇತ್ರಕ್ಕೆ ಮುಖ್ಯಮಂತ್ರಿಗಳ ಅಭಿವೃದ್ಧಿ ಅನುದಾನ"
- "ಮುಖ್ಯಮಂತ್ರಿಗಳ ಮೂಲಸೌಕರ್ಯ ಯೋಜನೆ, 2025-26: ₹{c} ಕೋಟಿ ಮಂಜೂರು." / null: "2025-26ರ ಮುಖ್ಯಮಂತ್ರಿಗಳ ಮೂಲಸೌಕರ್ಯ ಯೋಜನೆಯ ಪಟ್ಟಿಯಲ್ಲಿ ಈ ಕ್ಷೇತ್ರ ಇಲ್ಲ."
- "ಆಡಳಿತ ಪಕ್ಷದ ಹೆಚ್ಚಿನ ಕ್ಷೇತ್ರಗಳಿಗೆ ₹50 ಕೋಟಿ; ವಿರೋಧ ಪಕ್ಷದ ಹೆಚ್ಚಿನ ಕ್ಷೇತ್ರಗಳಿಗೆ ₹25 ಕೋಟಿ."
- ವಿಶೇಷ ಅನುದಾನ > 0: "ಮುಖ್ಯಮಂತ್ರಿಗಳ ವಿಶೇಷ ಅನುದಾನ, ಮಾರ್ಚ್ 2025ಕ್ಕೆ ಮುಂಚಿನ ಎರಡು ವರ್ಷ: ₹{g} ಕೋಟಿ ಕಾಮಗಾರಿ ಮಂಜೂರು." / 0: "ಮಾರ್ಚ್ 2025ಕ್ಕೆ ಮುಂಚಿನ ಎರಡು ವರ್ಷಗಳ ಮುಖ್ಯಮಂತ್ರಿಗಳ ವಿಶೇಷ ಅನುದಾನ ಪಟ್ಟಿಯಲ್ಲಿ ಇಲ್ಲ."
- ಸಣ್ಣ ಅಕ್ಷರ: "ಮಂಜೂರಾತಿಗಳು, ಖರ್ಚಾದ ಹಣವಲ್ಲ. ಮೂಲ: ವಿಧಾನಸಭೆ ಪ್ರಶ್ನೆ 1727 (16 ಡಿಸೆಂಬರ್ 2025) ಮತ್ತು 1119 (11 ಮಾರ್ಚ್ 2025)ಕ್ಕೆ ಮುಖ್ಯಮಂತ್ರಿಗಳ ಉತ್ತರಗಳು."

## Notes
- Party labels: Yeshwanthapura and Yellapur MLAs were expelled by the BJP on 27 May 2025; data/mlas.csv still says BJP. If the card shows a party, note "expelled from the BJP, May 2025" for those two.
- Do not add this to the PWD works box (the two may overlap; CMIDP money for roads can also appear in the PWD list).
- Not for X in Kannada (English only on X since 24 Nov).
