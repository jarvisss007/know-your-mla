"""Build the public "Evidence" page (English and Kannada) from one list of findings.

    py tools/make_evidence_page.py
writes research/evidence/DRAFT_evidence.html and DRAFT_evidence_kn.html;
tools/publish_reports.py then copies them to reports/evidence.html and reports/evidence_kn.html.

Rules for what goes in FINDINGS:
- only figures already published on a linked Gandaberunda page, where each is sourced and was checked;
- each says what kind of record it is (audit, government's own answer, court/agency, our count) and links the page;
- people by office, not by name, unless the record itself is about an office-holder's own public declaration;
- nothing from a private case file before its right-of-reply deadline.
Kannada text needs the native reviewer like the rest of the site.
"""
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "research" / "evidence"
CHECKED = "23 Nov 2026"
CHECKED_KN = "23 ನವೆಂಬರ್ 2026"

# Kannada form of each big number (keyed by the English form used in FINDINGS)
BIG_KN = {"No answer": "ಉತ್ತರವಿಲ್ಲ", "35 of 120": "120ರಲ್ಲಿ 35", "₹6,026 cr": "₹6,026 ಕೋಟಿ", "₹410 cr": "₹410 ಕೋಟಿ",
          "₹4,004 cr": "₹4,004 ಕೋಟಿ", "₹35,236 cr": "₹35,236 ಕೋಟಿ", "₹43,782 cr": "₹43,782 ಕೋಟಿ", "₹369 cr": "₹369 ಕೋಟಿ", "₹1,275 cr": "₹1,275 ಕೋಟಿ", "521 works": "521 ಕಾಮಗಾರಿ", "8.24 lakh": "8.24 ಲಕ್ಷ"}


def big_for(big, lang):
    return BIG_KN.get(big, big) if lang == "kn" else big

# kind: audit | govt | court | count   (label shown as a tag)
KIND = {"en": {"audit": "Audit finding", "govt": "Government's own answer", "court": "Court or agency record", "count": "Our count of official records"},
        "kn": {"audit": "ಲೆಕ್ಕಪರಿಶೋಧನಾ ತೀರ್ಮಾನ", "govt": "ಸರ್ಕಾರದ ಸ್ವಂತ ಉತ್ತರ", "court": "ನ್ಯಾಯಾಲಯ ಅಥವಾ ಸಂಸ್ಥೆಯ ದಾಖಲೆ", "count": "ಅಧಿಕೃತ ದಾಖಲೆಗಳ ನಮ್ಮ ಎಣಿಕೆ"}}

# Each finding: (group, kind, big number, EN line, KN line, EN source, KN source, page_en, page_kn)
FINDINGS = [
    ("cases", "govt", "1,248 → 0",
     "Lokayukta corruption cases against officials registered September 2022 to August 2026. Government servants held guilty in those cases so far: none. (The same reply counts 148 convictions since 2023 in older cases, and in November 2026 the Lokayukta reported 153 convictions in four years without saying in which cases.)",
     "ಸೆಪ್ಟೆಂಬರ್ 2022ರಿಂದ ಆಗಸ್ಟ್ 2026ರವರೆಗೆ ಅಧಿಕಾರಿಗಳ ವಿರುದ್ಧ ದಾಖಲಾದ ಲೋಕಾಯುಕ್ತ ಭ್ರಷ್ಟಾಚಾರ ಪ್ರಕರಣಗಳು. ಆ ಪ್ರಕರಣಗಳಲ್ಲಿ ಇದುವರೆಗೆ ತಪ್ಪಿತಸ್ಥರೆಂದು ಸಾಬೀತಾದ ಸರ್ಕಾರಿ ನೌಕರರು: ಯಾರೂ ಇಲ್ಲ. (ಅದೇ ಉತ್ತರ 2023ರಿಂದ ಹಳೆಯ ಪ್ರಕರಣಗಳಲ್ಲಿ 148 ಶಿಕ್ಷೆಗಳನ್ನು ಎಣಿಸುತ್ತದೆ; ನವೆಂಬರ್ 2026ರಲ್ಲಿ ಲೋಕಾಯುಕ್ತ ನಾಲ್ಕು ವರ್ಷಗಳಲ್ಲಿ 153 ಶಿಕ್ಷೆಗಳನ್ನು ವರದಿ ಮಾಡಿದೆ, ಯಾವ ಪ್ರಕರಣಗಳಲ್ಲಿ ಎಂದು ಹೇಳದೆ.)",
     "Chief Minister's written reply, Legislative Council question 452 (628), 20 Aug 2026",
     "ಮುಖ್ಯಮಂತ್ರಿಗಳ ಲಿಖಿತ ಉತ್ತರ, ವಿಧಾನ ಪರಿಷತ್ ಪ್ರಶ್ನೆ 452 (628), 20 ಆಗಸ್ಟ್ 2026",
     "officials_tracker.html", "officials_tracker_kn.html"),
    ("cases", "govt", "195 → 0",
     "Lokayukta cases against IAS, IPS, KAS and other senior officers, September 2022 to February 2026. Ended in conviction or acquittal: none. 89 were still under investigation.",
     "ಸೆಪ್ಟೆಂಬರ್ 2022ರಿಂದ ಫೆಬ್ರವರಿ 2026ರವರೆಗೆ ಐಎಎಸ್, ಐಪಿಎಸ್, ಕೆಎಎಸ್ ಮತ್ತು ಇತರ ಹಿರಿಯ ಅಧಿಕಾರಿಗಳ ವಿರುದ್ಧ ಲೋಕಾಯುಕ್ತ ಪ್ರಕರಣಗಳು. ಶಿಕ್ಷೆ ಅಥವಾ ಖುಲಾಸೆಯಲ್ಲಿ ಮುಗಿದವು: ಒಂದೂ ಇಲ್ಲ. 89 ಇನ್ನೂ ತನಿಖೆಯಲ್ಲಿದ್ದವು.",
     "Written reply of then Chief Minister Siddaramaiah, Assembly question 1324, 10 Mar 2026",
     "ಅಂದಿನ ಮುಖ್ಯಮಂತ್ರಿ ಸಿದ್ದರಾಮಯ್ಯ ಅವರ ಲಿಖಿತ ಉತ್ತರ, ವಿಧಾನಸಭೆ ಪ್ರಶ್ನೆ 1324, 10 ಮಾರ್ಚ್ 2026",
     "officials_tracker.html", "officials_tracker_kn.html"),
    ("cases", "govt", "No answer",
     "On 25 August 2026 MLAs asked how many requests to prosecute corrupt officials are waiting for the government's permission, and for how long. Three months later, no answer is on the Assembly's website.",
     "ಭ್ರಷ್ಟ ಅಧಿಕಾರಿಗಳ ಅಭಿಯೋಜನೆಗೆ ಸರ್ಕಾರದ ಅನುಮತಿಗಾಗಿ ಎಷ್ಟು ಕೋರಿಕೆಗಳು, ಎಷ್ಟು ಕಾಲದಿಂದ ಕಾಯುತ್ತಿವೆ ಎಂದು 25 ಆಗಸ್ಟ್ 2026ರಂದು ಶಾಸಕರು ಕೇಳಿದ್ದರು. ಮೂರು ತಿಂಗಳ ನಂತರವೂ ವಿಧಾನಸಭೆಯ ಜಾಲತಾಣದಲ್ಲಿ ಉತ್ತರವಿಲ್ಲ.",
     "Assembly unstarred questions 1558 and 1652, 25 Aug 2026; website checked 23 Nov 2026",
     "ವಿಧಾನಸಭೆ ಪ್ರಶ್ನೆ 1558 ಮತ್ತು 1652, 25 ಆಗಸ್ಟ್ 2026; ಜಾಲತಾಣ ಪರಿಶೀಲನೆ 23 ನವೆಂಬರ್ 2026",
     "officials_tracker.html", "officials_tracker_kn.html"),
    ("cases", "count", "35 of 120",
     "Corruption trials that Karnataka's courts finished in 2023 ended in conviction (29%; all India 46%). 1,529 cases were still waiting for trial at the year's end.",
     "2023ರಲ್ಲಿ ಕರ್ನಾಟಕದ ನ್ಯಾಯಾಲಯಗಳು ಮುಗಿಸಿದ ಭ್ರಷ್ಟಾಚಾರ ವಿಚಾರಣೆಗಳಲ್ಲಿ ಶಿಕ್ಷೆ (29%; ಭಾರತ 46%). ವರ್ಷಾಂತ್ಯದಲ್ಲಿ 1,529 ಪ್ರಕರಣಗಳು ವಿಚಾರಣೆಗೆ ಕಾಯುತ್ತಿದ್ದವು.",
     "National Crime Records Bureau, Crime in India 2023, Vol. II, Table 8C.4",
     "ರಾಷ್ಟ್ರೀಯ ಅಪರಾಧ ದಾಖಲೆಗಳ ಬ್ಯೂರೋ, ಕ್ರೈಮ್ ಇನ್ ಇಂಡಿಯಾ 2023, ಕೋಷ್ಟಕ 8C.4",
     "officials_tracker.html", "officials_tracker_kn.html"),
    ("money", "audit", "₹6,026 cr",
     "Moved into deposit accounts in March 2025 alone, at the year's end. The auditor's words for one such transfer: “mere parking of funds to avoid lapse of grants”.",
     "ಮಾರ್ಚ್ 2025 ಒಂದೇ ತಿಂಗಳಲ್ಲಿ, ವರ್ಷಾಂತ್ಯದಲ್ಲಿ ಠೇವಣಿ ಖಾತೆಗಳಿಗೆ ವರ್ಗಾಯಿಸಿದ ಹಣ. ಅಂತಹ ಒಂದು ವರ್ಗಾವಣೆಯ ಬಗ್ಗೆ ಲೆಕ್ಕಪರಿಶೋಧಕರ ಮಾತು: ಅನುದಾನ ವ್ಯಪಗತವಾಗದಂತೆ ಹಣವನ್ನು “ಕೇವಲ ನಿಲ್ಲಿಸಿಡುವುದು”.",
     "CAG, State Finances Audit Report 2024-25, paras 3.5.1 and 2.7.1.2A",
     "ಸಿಎಜಿ, ರಾಜ್ಯ ಹಣಕಾಸು ಲೆಕ್ಕಪರಿಶೋಧನಾ ವರದಿ 2024-25, ಕಂಡಿಕೆ 3.5.1, 2.7.1.2A",
     "follow_the_money.html#journey", "follow_the_money_kn.html#journey"),
    ("money", "audit", "₹410 cr",
     "Kept in 32 bank accounts that ten development corporations had been ordered in 2023 to close (31 March 2025).",
     "2023ರಲ್ಲಿ ಮುಚ್ಚಲು ಆದೇಶಿಸಲಾಗಿದ್ದ 32 ಬ್ಯಾಂಕ್ ಖಾತೆಗಳಲ್ಲಿ ಹತ್ತು ಅಭಿವೃದ್ಧಿ ನಿಗಮಗಳು ಇಟ್ಟಿದ್ದ ಹಣ (31 ಮಾರ್ಚ್ 2025).",
     "CAG, State Finances Audit Report 2024-25, Appendix 2.16",
     "ಸಿಎಜಿ, ರಾಜ್ಯ ಹಣಕಾಸು ಲೆಕ್ಕಪರಿಶೋಧನಾ ವರದಿ 2024-25, ಅನುಬಂಧ 2.16",
     "follow_the_money.html#corporations", "follow_the_money_kn.html#corporations"),
    ("money", "audit", "₹4,004 cr",
     "Collected by district mineral funds for mining-hit villages up to March 2023; ₹1,826 crore spent; 2,190 projects had not started by March 2023. The steering committee headed by the Chief Minister did not meet once from 2018 to June 2023.",
     "ಗಣಿಬಾಧಿತ ಹಳ್ಳಿಗಳಿಗಾಗಿ ಜಿಲ್ಲಾ ಖನಿಜ ಪ್ರತಿಷ್ಠಾನಗಳು ಮಾರ್ಚ್ 2023ರವರೆಗೆ ಸಂಗ್ರಹಿಸಿದ ಹಣ; ಖರ್ಚು ₹1,826 ಕೋಟಿ; 2,190 ಯೋಜನೆಗಳು ಮಾರ್ಚ್ 2023ರವರೆಗೆ ಆರಂಭವಾಗಿರಲಿಲ್ಲ. ಮುಖ್ಯಮಂತ್ರಿ ಅಧ್ಯಕ್ಷತೆಯ ಸಮಿತಿ 2018ರಿಂದ ಜೂನ್ 2023ರವರೆಗೆ ಒಮ್ಮೆಯೂ ಸಭೆ ಸೇರಲಿಲ್ಲ.",
     "CAG, Report 7 of 2025",
     "ಸಿಎಜಿ, ವರದಿ 7/2025",
     "follow_the_money.html#mining", "follow_the_money_kn.html#mining"),
    ("money", "govt", "₹35,236 cr",
     "Owed to contractors for work already done, in six departments (our sum of the figures in the government's answer). In the Public Works department's North zone, 31% of the money owed was more than a year old.",
     "ಈಗಾಗಲೇ ಮಾಡಿದ ಕೆಲಸಕ್ಕೆ ಗುತ್ತಿಗೆದಾರರಿಗೆ ಆರು ಇಲಾಖೆಗಳು ನೀಡಬೇಕಾದ ಹಣ (ಸರ್ಕಾರದ ಉತ್ತರದ ಅಂಕಿಗಳ ನಮ್ಮ ಮೊತ್ತ). ಲೋಕೋಪಯೋಗಿ ಇಲಾಖೆಯ ಉತ್ತರ ವಲಯದಲ್ಲಿ ಬಾಕಿ ಹಣದ 31% ಒಂದು ವರ್ಷಕ್ಕಿಂತ ಹಳೆಯದು.",
     "Chief Minister's written reply to the Assembly, 9 Dec 2025; Assembly question 1485, 24 Aug 2026",
     "ವಿಧಾನಸಭೆಗೆ ಮುಖ್ಯಮಂತ್ರಿಗಳ ಲಿಖಿತ ಉತ್ತರ, 9 ಡಿಸೆಂಬರ್ 2025; ವಿಧಾನಸಭೆ ಪ್ರಶ್ನೆ 1485, 24 ಆಗಸ್ಟ್ 2026",
     "follow_the_money.html", "follow_the_money_kn.html"),
    ("money", "audit", "67%",
     "Of the Yettinahole drinking-water project's ₹22,194 crore of contracts, the share held by seven contractors (₹14,806 crore of works, our arithmetic). ₹2,966 crore of finished assets could not be used because the canal was not complete.",
     "ಎತ್ತಿನಹೊಳೆ ಕುಡಿಯುವ ನೀರಿನ ಯೋಜನೆಯ ₹22,194 ಕೋಟಿ ಗುತ್ತಿಗೆಗಳಲ್ಲಿ ಏಳು ಗುತ್ತಿಗೆದಾರರ ಪಾಲು (₹14,806 ಕೋಟಿ ಕಾಮಗಾರಿ, ನಮ್ಮ ಲೆಕ್ಕ). ಕಾಲುವೆ ಪೂರ್ಣಗೊಳ್ಳದ ಕಾರಣ ₹2,966 ಕೋಟಿ ಮೌಲ್ಯದ ಆಸ್ತಿಗಳನ್ನು ಬಳಸಲಾಗಲಿಲ್ಲ.",
     "CAG, Performance Audit of the Yettinahole project, Report 10 of 2025",
     "ಸಿಎಜಿ, ಎತ್ತಿನಹೊಳೆ ಯೋಜನೆಯ ಕಾರ್ಯನಿರ್ವಹಣಾ ಲೆಕ್ಕಪರಿಶೋಧನೆ, ವರದಿ 10/2025",
     "follow_the_money.html", "follow_the_money_kn.html"),
    ("ground", "count", "521 works",
     "Booked as completed at two village tanks on the Tungabhadra, ₹29.24 crore, from 28 panchayats. Every completion photo was taken at the tanks. (Revised 23 Nov 2026 from 246 works, ₹13.05 crore, once the exact location of every work was obtained.)",
     "ತುಂಗಭದ್ರೆಯ ಎರಡು ಹಳ್ಳಿ ಕೆರೆಗಳಲ್ಲಿ ಪೂರ್ಣಗೊಂಡಿವೆ ಎಂದು ದಾಖಲಾದ ಕಾಮಗಾರಿಗಳು, ₹29.24 ಕೋಟಿ, 28 ಪಂಚಾಯಿತಿಗಳಿಂದ. ಪ್ರತಿ ಪೂರ್ಣಗೊಂಡ ಫೋಟೋ ಆ ಕೆರೆಗಳಲ್ಲೇ ತೆಗೆದದ್ದು. (ಪ್ರತಿ ಕಾಮಗಾರಿಯ ನಿಖರ ಸ್ಥಳ ಸಿಕ್ಕ ನಂತರ 23 ನವೆಂಬರ್ 2026ರಂದು 246 ಕಾಮಗಾರಿ, ₹13.05 ಕೋಟಿಯಿಂದ ಪರಿಷ್ಕರಿಸಲಾಗಿದೆ.)",
     "MGNREGA public records (government's own), read by us",
     "ನರೇಗಾ ಸಾರ್ವಜನಿಕ ದಾಖಲೆಗಳು (ಸರ್ಕಾರದ್ದೇ), ನಾವು ಓದಿದಂತೆ",
     "tank_findings.html", "tank_findings.html"),
    ("ground", "count", "8.24 lakh",
     "Completion photos of Karnataka's 2024-25 rural job works, every one checked for where it was taken. The ranking shows which blocks' proof of work breaks down.",
     "ಕರ್ನಾಟಕದ 2024-25ರ ಗ್ರಾಮೀಣ ಉದ್ಯೋಗ ಕಾಮಗಾರಿಗಳ ಪೂರ್ಣಗೊಂಡ ಫೋಟೋಗಳು; ಪ್ರತಿಯೊಂದನ್ನೂ ಎಲ್ಲಿ ತೆಗೆಯಲಾಯಿತು ಎಂದು ಪರಿಶೀಲಿಸಲಾಗಿದೆ. ಯಾವ ಬ್ಲಾಕ್‌ಗಳಲ್ಲಿ ಕೆಲಸದ ಪುರಾವೆ ಮುರಿಯುತ್ತದೆ ಎಂದು ಶ್ರೇಣಿ ತೋರಿಸುತ್ತದೆ.",
     "MGNREGA public records (government's own), read by us",
     "ನರೇಗಾ ಸಾರ್ವಜನಿಕ ದಾಖಲೆಗಳು (ಸರ್ಕಾರದ್ದೇ), ನಾವು ಓದಿದಂತೆ",
     "statewide_check.html", "statewide_check.html"),
    # added 23 Nov 2026 from money.html "Checked against the source" (money-sources session; each re-read at source)
    ("money", "audit", "₹43,782 cr",
     "Less given to village, taluk and district panchayats than the state itself had accepted from its own Finance Commissions, 2017-18 to 2021-22.",
     "2017-18ರಿಂದ 2021-22ರವರೆಗೆ ರಾಜ್ಯ ತನ್ನದೇ ಹಣಕಾಸು ಆಯೋಗಗಳಿಂದ ಒಪ್ಪಿಕೊಂಡದ್ದಕ್ಕಿಂತ ಗ್ರಾಮ, ತಾಲ್ಲೂಕು ಮತ್ತು ಜಿಲ್ಲಾ ಪಂಚಾಯಿತಿಗಳಿಗೆ ಕಡಿಮೆ ನೀಡಿದ ಹಣ.",
     "CAG, Report 10 of 2024, para 3.2.2.3",
     "ಸಿಎಜಿ, ವರದಿ 10/2024, ಕಂಡಿಕೆ 3.2.2.3",
     "../money.html#checked", "../money.html#checked"),
    ("money", "audit", "₹369 cr",
     "Of central Finance Commission grants lost because zilla and taluk panchayat elections have not been held since 2021. The state offered no comment to the auditor.",
     "2021ರಿಂದ ಜಿಲ್ಲಾ ಮತ್ತು ತಾಲ್ಲೂಕು ಪಂಚಾಯಿತಿ ಚುನಾವಣೆಗಳು ನಡೆಯದ ಕಾರಣ ಕಳೆದುಹೋದ ಕೇಂದ್ರ ಹಣಕಾಸು ಆಯೋಗದ ಅನುದಾನ. ರಾಜ್ಯ ಲೆಕ್ಕಪರಿಶೋಧಕರಿಗೆ ಯಾವುದೇ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡಲಿಲ್ಲ.",
     "CAG, Report 10 of 2024, para 3.2.1",
     "ಸಿಎಜಿ, ವರದಿ 10/2024, ಕಂಡಿಕೆ 3.2.1",
     "../money.html#checked", "../money.html#checked"),
    ("money", "audit", "₹1,275 cr",
     "Health cess collected from Bengaluru property owners by the city corporation and never passed on, 2017-18 to 2021-22 (plus ₹256 crore of library cess).",
     "2017-18ರಿಂದ 2021-22ರವರೆಗೆ ಬೆಂಗಳೂರಿನ ಆಸ್ತಿ ಮಾಲೀಕರಿಂದ ನಗರ ಪಾಲಿಕೆ ಸಂಗ್ರಹಿಸಿ ವರ್ಗಾಯಿಸದ ಆರೋಗ್ಯ ಸೆಸ್ (ಜೊತೆಗೆ ₹256 ಕೋಟಿ ಗ್ರಂಥಾಲಯ ಸೆಸ್).",
     "CAG inspection report on local bodies 2020-22, para 2.10.5",
     "ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳ ಮೇಲಿನ ಸಿಎಜಿ ತಪಾಸಣಾ ವರದಿ 2020-22, ಕಂಡಿಕೆ 2.10.5",
     "../money.html#checked", "../money.html#checked"),

]

GROUPS = {"en": {"cases": "After the raid: does anyone get punished?", "money": "Where the money goes", "ground": "On the ground"},
          "kn": {"cases": "ದಾಳಿಯ ನಂತರ: ಯಾರಿಗಾದರೂ ಶಿಕ್ಷೆಯಾಗುತ್ತದೆಯೇ?", "money": "ಹಣ ಎಲ್ಲಿಗೆ ಹೋಗುತ್ತದೆ", "ground": "ನೆಲದ ಮೇಲೆ"}}

# What a citizen can do. Rules here are checked against the Acts (see research/evidence/ACCOUNTABILITY_TOOLS.md).
ACTIONS = {
"en": [
 ("Ask for the record (RTI)", "Any citizen can ask any government office for its records. A Karnataka application costs ₹10 (free for families below the poverty line); the office must reply within 30 days. If it does not, or refuses, appeal to the officer's senior within 30 days, then to the Karnataka Information Commission within 90 days. Seven ready letters, in Kannada and English, are on our RTI page.", "../rti.html", "RTI letters"),
 ("Complain to the Lokayukta", "If you have evidence that a public servant took a bribe or misused office, any person may complain to the Lokayukta, on its form, with a sworn affidavit. Complain only about what you can show: a knowingly false complaint is itself an offence. If someone demands a bribe, tell the Lokayukta police; they can lay a trap, as in most cases on our tracker.", "officials_tracker.html", "See the cases"),
 ("Ask why permission to prosecute is stuck", "The law asks a department to decide a request to prosecute within three months, plus one month if it needs legal advice (Prevention of Corruption Act, Section 19), and the Supreme Court has held that time limit binding. Ask your department, by RTI, which requests are waiting and since when.", "../rti.html#letter-l2", "RTI letter 2"),
 ("Make your MLA or MLC ask", "Any legislator can put a written question to the government, and the answer is published on the Assembly or Council website. Ask yours to ask: how many sanction requests are pending, which bills are oldest, what happened after a raid in your district.", "https://kla.kar.nic.in/", "Assembly and Council answers"),
 ("Go to the Gram Sabha and the social audit", "Rural job works must be checked at a social audit in the village; the new rural jobs law that replaced MGNREGA in July 2026 keeps social audits compulsory. Ask to see the work, the photo and the payment. If a work on the list does not exist, say so on the record.", "tank_findings.html", "One tank, many works"),
 ("Share the evidence, not the anger", "Every figure here has a document behind it. Send the page or the leaflet, not a rumour: a fact with a source is harder to dismiss.", "#share", "Share"),
],
"kn": [
 ("ದಾಖಲೆಯನ್ನು ಕೇಳಿ (ಆರ್‌ಟಿಐ)", "ಯಾವುದೇ ನಾಗರಿಕರು ಯಾವುದೇ ಸರ್ಕಾರಿ ಕಚೇರಿಯಿಂದ ಅದರ ದಾಖಲೆಗಳನ್ನು ಕೇಳಬಹುದು. ಕರ್ನಾಟಕದಲ್ಲಿ ಅರ್ಜಿ ಶುಲ್ಕ ₹10 (ಬಡತನ ರೇಖೆಗಿಂತ ಕೆಳಗಿನ ಕುಟುಂಬಗಳಿಗೆ ಉಚಿತ); ಕಚೇರಿ 30 ದಿನಗಳಲ್ಲಿ ಉತ್ತರಿಸಬೇಕು. ಉತ್ತರಿಸದಿದ್ದರೆ ಅಥವಾ ನಿರಾಕರಿಸಿದರೆ 30 ದಿನಗಳಲ್ಲಿ ಮೇಲಧಿಕಾರಿಗೆ, ನಂತರ 90 ದಿನಗಳಲ್ಲಿ ಕರ್ನಾಟಕ ಮಾಹಿತಿ ಆಯೋಗಕ್ಕೆ ಮೇಲ್ಮನವಿ ಸಲ್ಲಿಸಿ. ಏಳು ಸಿದ್ಧ ಪತ್ರಗಳು ನಮ್ಮ ಆರ್‌ಟಿಐ ಪುಟದಲ್ಲಿವೆ.", "../rti.html#kn", "ಆರ್‌ಟಿಐ ಪತ್ರಗಳು"),
 ("ಲೋಕಾಯುಕ್ತಕ್ಕೆ ದೂರು ನೀಡಿ", "ಸರ್ಕಾರಿ ನೌಕರರು ಲಂಚ ಪಡೆದ ಅಥವಾ ಅಧಿಕಾರ ದುರುಪಯೋಗ ಮಾಡಿದ ಸಾಕ್ಷ್ಯ ನಿಮ್ಮ ಬಳಿ ಇದ್ದರೆ, ಯಾರಾದರೂ ಲೋಕಾಯುಕ್ತಕ್ಕೆ ಅದರ ನಮೂನೆಯಲ್ಲಿ, ಪ್ರಮಾಣಪತ್ರದೊಂದಿಗೆ ದೂರು ನೀಡಬಹುದು. ನೀವು ತೋರಿಸಬಲ್ಲದ್ದರ ಬಗ್ಗೆ ಮಾತ್ರ ದೂರು ನೀಡಿ: ಗೊತ್ತಿದ್ದೂ ಸುಳ್ಳು ದೂರು ನೀಡುವುದೇ ಅಪರಾಧ. ಯಾರಾದರೂ ಲಂಚ ಕೇಳಿದರೆ ಲೋಕಾಯುಕ್ತ ಪೊಲೀಸರಿಗೆ ತಿಳಿಸಿ; ಅವರು ಟ್ರ್ಯಾಪ್ ಮಾಡಬಹುದು, ನಮ್ಮ ಪಟ್ಟಿಯ ಹೆಚ್ಚಿನ ಪ್ರಕರಣಗಳಂತೆ.", "officials_tracker_kn.html", "ಪ್ರಕರಣಗಳನ್ನು ನೋಡಿ"),
 ("ಅಭಿಯೋಜನಾ ಅನುಮತಿ ಏಕೆ ನಿಂತಿದೆ ಎಂದು ಕೇಳಿ", "ಅಭಿಯೋಜನೆಯ ಕೋರಿಕೆಯನ್ನು ಇಲಾಖೆ ಮೂರು ತಿಂಗಳಲ್ಲಿ, ಕಾನೂನು ಸಲಹೆ ಬೇಕಿದ್ದರೆ ಇನ್ನೊಂದು ತಿಂಗಳಲ್ಲಿ, ತೀರ್ಮಾನಿಸಬೇಕೆಂದು ಕಾನೂನು ಹೇಳುತ್ತದೆ (ಭ್ರಷ್ಟಾಚಾರ ನಿಯಂತ್ರಣ ಕಾಯ್ದೆ, ಕಲಂ 19); ಈ ಕಾಲಮಿತಿ ಬದ್ಧವೆಂದು ಸರ್ವೋಚ್ಚ ನ್ಯಾಯಾಲಯ ಹೇಳಿದೆ. ಯಾವ ಕೋರಿಕೆಗಳು ಯಾವಾಗಿನಿಂದ ಕಾಯುತ್ತಿವೆ ಎಂದು ಆರ್‌ಟಿಐ ಮೂಲಕ ಕೇಳಿ.", "../rti.html#letter-l2", "ಆರ್‌ಟಿಐ ಪತ್ರ 2"),
 ("ನಿಮ್ಮ ಶಾಸಕರು ಅಥವಾ ಪರಿಷತ್ ಸದಸ್ಯರಿಂದ ಕೇಳಿಸಿ", "ಯಾವುದೇ ಶಾಸಕರು ಸರ್ಕಾರಕ್ಕೆ ಲಿಖಿತ ಪ್ರಶ್ನೆ ಕೇಳಬಹುದು; ಉತ್ತರ ವಿಧಾನಸಭೆ ಅಥವಾ ಪರಿಷತ್ತಿನ ಜಾಲತಾಣದಲ್ಲಿ ಪ್ರಕಟವಾಗುತ್ತದೆ. ಎಷ್ಟು ಅನುಮತಿ ಕೋರಿಕೆಗಳು ಬಾಕಿ, ಯಾವ ಬಿಲ್ಲುಗಳು ಅತ್ಯಂತ ಹಳೆಯವು, ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ದಾಳಿಯ ನಂತರ ಏನಾಯಿತು ಎಂದು ಕೇಳುವಂತೆ ನಿಮ್ಮ ಪ್ರತಿನಿಧಿಗೆ ಹೇಳಿ.", "https://kla.kar.nic.in/", "ವಿಧಾನಸಭೆ ಮತ್ತು ಪರಿಷತ್ ಉತ್ತರಗಳು"),
 ("ಗ್ರಾಮಸಭೆ ಮತ್ತು ಸಾಮಾಜಿಕ ಲೆಕ್ಕಪರಿಶೋಧನೆಗೆ ಹೋಗಿ", "ಗ್ರಾಮೀಣ ಉದ್ಯೋಗ ಕಾಮಗಾರಿಗಳನ್ನು ಹಳ್ಳಿಯ ಸಾಮಾಜಿಕ ಲೆಕ್ಕಪರಿಶೋಧನೆಯಲ್ಲಿ ಪರಿಶೀಲಿಸಬೇಕು; ಜುಲೈ 2026ರಲ್ಲಿ ನರೇಗಾ ಬದಲಿಗೆ ಬಂದ ಹೊಸ ಗ್ರಾಮೀಣ ಉದ್ಯೋಗ ಕಾಯ್ದೆಯಲ್ಲೂ ಸಾಮಾಜಿಕ ಲೆಕ್ಕಪರಿಶೋಧನೆ ಕಡ್ಡಾಯ. ಕಾಮಗಾರಿ, ಫೋಟೋ ಮತ್ತು ಪಾವತಿಯನ್ನು ತೋರಿಸಲು ಕೇಳಿ. ಪಟ್ಟಿಯಲ್ಲಿರುವ ಕಾಮಗಾರಿ ಇಲ್ಲದಿದ್ದರೆ ಅದನ್ನು ದಾಖಲೆಯಲ್ಲಿ ಹೇಳಿ.", "tank_findings.html", "ಒಂದು ಕೆರೆ, ಹಲವು ಕಾಮಗಾರಿಗಳು"),
 ("ಕೋಪವಲ್ಲ, ಸಾಕ್ಷ್ಯವನ್ನು ಹಂಚಿ", "ಇಲ್ಲಿರುವ ಪ್ರತಿ ಅಂಕಿಯ ಹಿಂದೆ ಒಂದು ದಾಖಲೆ ಇದೆ. ವದಂತಿ ಅಲ್ಲ, ಈ ಪುಟ ಅಥವಾ ಕರಪತ್ರವನ್ನು ಕಳುಹಿಸಿ: ಮೂಲವಿರುವ ಸತ್ಯವನ್ನು ತಳ್ಳಿಹಾಕುವುದು ಕಷ್ಟ.", "#share", "ಹಂಚಿ"),
]}

T = {
"en": dict(lang="en", title="The Evidence", eyebrow=f"Gandaberunda · Karnataka · checked {CHECKED}",
  h1='The <span>evidence</span>, in one place',
  lede="What Karnataka's own records, auditors and courts show about where public money goes and what happens to those who misuse it, and what you can do about it. Every figure below has a document behind it; open the linked page for the source, the exact table and the government's side.",
  rules="Read it fairly: an audit finding is the auditor's conclusion, not a court's; a raid or a chargesheet is an accusation, not guilt. We name offices, not officials, until a court rules. Both parties have governed in the years these records cover.",
  act_h="What you can do", act_p="Six things any citizen can do, starting this week. None needs a lawyer.",
  share_h="Share it", share_p="Send the page, or print the one-page leaflet for a notice board, a Gram Sabha or a WhatsApp group.",
  leaflet="Leaflet (English, PDF)", leaflet_alt="Leaflet (Kannada, PDF)",
  wa="Karnataka's own records, in one place: 1,248 Lokayukta cases against officials since 2022, none held guilty yet; ₹6,026 crore parked at the year's end; ₹35,236 crore owed to contractors. Every figure with its document:",
  open="Open the source page", src="Source", alt=("evidence_kn.html", "ಕನ್ನಡ"),
  more_h="More on the site", more=[("../index.html#tunnel", "The tunnel road: cost, findings and court position"), ("../index.html#loans", "Money between politicians, declared on both sides"), ("../index.html#find", "Your MLA's declared assets and cases"), ("farm_money_ledger.html", "Farm money: promised vs what reached the field")],
  foot="Gandaberunda is an independent citizen publication. Official records, not allegations. Seen an error? Corrections are published openly on the home page."),
"kn": dict(lang="kn", title="ಸಾಕ್ಷ್ಯ", eyebrow=f"ಗಂಡಭೇರುಂಡ · ಕರ್ನಾಟಕ · ಪರಿಶೀಲನೆ {CHECKED_KN}",
  h1='<span>ಸಾಕ್ಷ್ಯ</span>, ಒಂದೇ ಕಡೆ',
  lede="ಸಾರ್ವಜನಿಕ ಹಣ ಎಲ್ಲಿಗೆ ಹೋಗುತ್ತದೆ, ಅದನ್ನು ದುರುಪಯೋಗ ಮಾಡಿದವರಿಗೆ ಏನಾಗುತ್ತದೆ ಎಂಬ ಬಗ್ಗೆ ಕರ್ನಾಟಕದ ಸ್ವಂತ ದಾಖಲೆಗಳು, ಲೆಕ್ಕಪರಿಶೋಧಕರು ಮತ್ತು ನ್ಯಾಯಾಲಯಗಳು ಏನು ತೋರಿಸುತ್ತವೆ, ಮತ್ತು ನೀವು ಏನು ಮಾಡಬಹುದು. ಕೆಳಗಿನ ಪ್ರತಿ ಅಂಕಿಯ ಹಿಂದೆ ಒಂದು ದಾಖಲೆ ಇದೆ; ಮೂಲ, ನಿಖರ ಕೋಷ್ಟಕ ಮತ್ತು ಸರ್ಕಾರದ ಪಕ್ಷಕ್ಕಾಗಿ ಲಿಂಕ್ ಮಾಡಿದ ಪುಟವನ್ನು ತೆರೆಯಿರಿ.",
  rules="ನ್ಯಾಯಯುತವಾಗಿ ಓದಿ: ಲೆಕ್ಕಪರಿಶೋಧನಾ ತೀರ್ಮಾನ ಲೆಕ್ಕಪರಿಶೋಧಕರದ್ದು, ನ್ಯಾಯಾಲಯದ್ದಲ್ಲ; ದಾಳಿ ಅಥವಾ ದೋಷಾರೋಪಣ ಪಟ್ಟಿ ಆರೋಪ, ಅಪರಾಧ ಸಾಬೀತಲ್ಲ. ನ್ಯಾಯಾಲಯ ತೀರ್ಪು ನೀಡುವವರೆಗೆ ನಾವು ಹುದ್ದೆಗಳನ್ನು ಹೆಸರಿಸುತ್ತೇವೆ, ಅಧಿಕಾರಿಗಳನ್ನಲ್ಲ. ಈ ದಾಖಲೆಗಳ ವರ್ಷಗಳಲ್ಲಿ ಎರಡೂ ಪಕ್ಷಗಳು ಆಡಳಿತ ನಡೆಸಿವೆ.",
  act_h="ನೀವು ಏನು ಮಾಡಬಹುದು", act_p="ಯಾವುದೇ ನಾಗರಿಕರು ಈ ವಾರದಿಂದಲೇ ಮಾಡಬಹುದಾದ ಆರು ಕೆಲಸಗಳು. ಯಾವುದಕ್ಕೂ ವಕೀಲರು ಬೇಕಿಲ್ಲ.",
  share_h="ಹಂಚಿ", share_p="ಪುಟವನ್ನು ಕಳುಹಿಸಿ, ಅಥವಾ ಸೂಚನಾ ಫಲಕ, ಗ್ರಾಮಸಭೆ ಅಥವಾ ವಾಟ್ಸ್‌ಆ್ಯಪ್ ಗುಂಪಿಗಾಗಿ ಒಂದು ಪುಟದ ಕರಪತ್ರವನ್ನು ಮುದ್ರಿಸಿ.",
  leaflet="ಕರಪತ್ರ (ಕನ್ನಡ, PDF)", leaflet_alt="Leaflet (English, PDF)",
  wa="ಕರ್ನಾಟಕದ ಸ್ವಂತ ದಾಖಲೆಗಳು, ಒಂದೇ ಕಡೆ: 2022ರಿಂದ ಅಧಿಕಾರಿಗಳ ವಿರುದ್ಧ 1,248 ಲೋಕಾಯುಕ್ತ ಪ್ರಕರಣಗಳು, ಇನ್ನೂ ಯಾರೂ ತಪ್ಪಿತಸ್ಥರೆಂದು ಸಾಬೀತಾಗಿಲ್ಲ; ವರ್ಷಾಂತ್ಯದಲ್ಲಿ ₹6,026 ಕೋಟಿ ನಿಲ್ಲಿಸಿಡಲಾಗಿದೆ; ಗುತ್ತಿಗೆದಾರರಿಗೆ ₹35,236 ಕೋಟಿ ಬಾಕಿ. ಪ್ರತಿ ಅಂಕಿ ದಾಖಲೆಯೊಂದಿಗೆ:",
  open="ಮೂಲ ಪುಟ ತೆರೆಯಿರಿ", src="ಮೂಲ", alt=("evidence.html", "English"),
  more_h="ಜಾಲತಾಣದಲ್ಲಿ ಇನ್ನಷ್ಟು", more=[("../index.html#tunnel", "ಸುರಂಗ ರಸ್ತೆ: ವೆಚ್ಚ, ತೀರ್ಮಾನಗಳು, ನ್ಯಾಯಾಲಯ"), ("../index.html#loans", "ರಾಜಕಾರಣಿಗಳ ನಡುವಿನ ಸಾಲ, ಎರಡೂ ಕಡೆ ಘೋಷಿತ"), ("../index.html#find", "ನಿಮ್ಮ ಶಾಸಕರ ಘೋಷಿತ ಆಸ್ತಿ ಮತ್ತು ಪ್ರಕರಣಗಳು"), ("farm_money_ledger_kn.html", "ಕೃಷಿ ಹಣ: ಭರವಸೆ ಮತ್ತು ಹೊಲ ತಲುಪಿದ್ದು")],
  foot="ಗಂಡಭೇರುಂಡ ಒಂದು ಸ್ವತಂತ್ರ ನಾಗರಿಕ ಪ್ರಕಟಣೆ. ಅಧಿಕೃತ ದಾಖಲೆಗಳು, ಆರೋಪಗಳಲ್ಲ. ತಪ್ಪು ಕಂಡಿರಾ? ತಿದ್ದುಪಡಿಗಳನ್ನು ಮುಖಪುಟದಲ್ಲಿ ಬಹಿರಂಗವಾಗಿ ಪ್ರಕಟಿಸಲಾಗುತ್ತದೆ."),
}

CSS = """<style>
/* One reading column. The page is a stack of evidence cards (number, what it means, what kind of record, link to the source page), then actions. */
:root {
  --bg: #f5f6f8; --surface: #ffffff; --fg: #161a22; --muted: #5b6474; --line: #dde1e8;
  --red: #c21f30; --yellow: #f2b705; --blue: #1d4ed8; --green: #1a8f4c;
  --display: "Space Grotesk", "Segoe UI", system-ui, sans-serif;
  --body: Inter, "Noto Sans Kannada", "Segoe UI", system-ui, sans-serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d;
  --red: #ef5261; --yellow: #f5c93a; --blue: #7aa7ff; --green: #4fcf86; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #11141a; --surface: #1a1e27; --fg: #eceef2; --muted: #9aa3b2; --line: #2b313d;
  --red: #ef5261; --yellow: #f5c93a; --blue: #7aa7ff; --green: #4fcf86; color-scheme: dark }
body { background: var(--bg); color: var(--fg); font: 16px/1.55 var(--body); margin: 0;
  padding-block: 28px 64px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.wrap { max-width: 860px; margin: 0 auto; display: flex; flex-direction: column; gap: 40px; }
a { color: inherit; text-underline-offset: 3px; }
a:focus-visible { outline: 2px solid var(--red); outline-offset: 2px; }
h1, h2, h3 { font-family: var(--display); text-wrap: balance; margin: 0; }
h1 { font-size: clamp(2.2rem, 7vw, 3.6rem); line-height: 1.05; letter-spacing: -0.02em; }
h1 span { color: var(--red); }
h2 { font-size: 1.45rem; }
p { margin: 0; max-width: 66ch; }
header { display: flex; flex-direction: column; gap: 14px; }
.eyebrow { font-size: .75rem; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); font-weight: 600; }
.draft { display: inline-block; align-self: flex-start; background: var(--yellow); color: #161a22; font-weight: 600; font-size: .8rem; padding: 3px 10px; border-radius: 3px; letter-spacing: .04em; }
.lede { font-size: 1.12rem; }
.muted { color: var(--muted); font-size: .92rem; }
section { display: flex; flex-direction: column; gap: 14px; }
.cards { display: grid; gap: 12px; }
.card { background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--red); border-radius: 10px; padding: 16px 18px; display: grid; grid-template-columns: minmax(120px, 190px) 1fr; gap: 6px 18px; align-items: start; }
.card.k-audit { border-left-color: var(--green); } .card.k-govt { border-left-color: var(--blue); } .card.k-count { border-left-color: var(--yellow); }
.card b.n { font: 700 1.7rem/1.1 var(--display); font-variant-numeric: tabular-nums; grid-row: span 3; }
.card .src { font-size: .82rem; color: var(--muted); }
.card .tag { font-size: .7rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); }
.card a.go { font-size: .85rem; font-weight: 600; }
@media (max-width: 560px) { .card { grid-template-columns: 1fr; } .card b.n { grid-row: auto; } }
ol.act { margin: 0; padding: 0; list-style: none; counter-reset: a; display: grid; gap: 12px; }
ol.act li { counter-increment: a; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px 14px 56px; position: relative; display: flex; flex-direction: column; gap: 6px; }
ol.act li::before { content: counter(a); position: absolute; left: 16px; top: 13px; width: 28px; height: 28px; border-radius: 50%; background: var(--fg); color: var(--bg); font: 700 .95rem/28px var(--display); text-align: center; }
ol.act h3 { font-size: 1.05rem; }
.share { display: flex; flex-wrap: wrap; gap: 10px; }
.btn { display: inline-flex; align-items: center; gap: 6px; border: 1px solid var(--line); background: var(--surface); border-radius: 999px; padding: 8px 14px; font-weight: 600; font-size: .9rem; text-decoration: none; cursor: pointer; color: var(--fg); font-family: inherit; }
.btn:hover { border-color: var(--red); }
ul.more { margin: 0; padding-left: 20px; display: grid; gap: 4px; }
footer { border-top: 1px solid var(--line); padding-top: 16px; }
@media print { body { background: #fff; color: #000; } .share, .draft { display: none; } .card, ol.act li { break-inside: avoid; } }
</style>"""


def page(lang):
    t = T[lang]; e = html.escape
    groups = []
    for g, gname in GROUPS[lang].items():
        cards = []
        for (gg, kind, big, l_en, l_kn, s_en, s_kn, p_en, p_kn) in FINDINGS:
            if gg != g: continue
            line, src, link = (l_en, s_en, p_en) if lang == "en" else (l_kn, s_kn, p_kn)
            cards.append(f'<div class="card k-{kind}"><b class="n">{e(big_for(big, lang))}</b><span class="tag">{e(KIND[lang][kind])}</span>'
                         f'<p>{e(line)}</p><p class="src">{e(t["src"])}: {e(src)} · <a class="go" href="{link}">{e(t["open"])}</a></p></div>')
        groups.append(f'<section>\n  <h2>{e(gname)}</h2>\n  <div class="cards">\n    ' + "\n    ".join(cards) + '\n  </div>\n</section>')
    acts = "".join(f'<li><h3>{e(h)}</h3><p>{e(p)}</p><a href="{href}">{e(lbl)}</a></li>' for h, p, href, lbl in ACTIONS[lang])
    more = "".join(f'<li><a href="{h}">{e(x)}</a></li>' for h, x in t["more"])
    leaf = "evidence_leaflet_kn.pdf" if lang == "kn" else "evidence_leaflet.pdf"
    leaf_alt = "evidence_leaflet.pdf" if lang == "kn" else "evidence_leaflet_kn.pdf"
    wa = e(t["wa"])
    badge = "ಕರಡು · ಪ್ರಕಟಿಸಿಲ್ಲ" if lang == "kn" else "DRAFT · NOT PUBLISHED"
    return f"""<!doctype html>
<html lang="{t['lang']}">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Noto+Sans+Kannada:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap">
{CSS}
<div class="wrap">
<header>
  <span class="draft">{badge}</span>
  <div class="eyebrow">{e(t['eyebrow'])}</div>
  <h1>{t['h1']}</h1>
  <p class="lede">{e(t['lede'])}</p>
  <p class="muted">{e(t['rules'])}</p>
</header>

{chr(10).join(groups)}

<section id="act">
  <h2>{e(t['act_h'])}</h2>
  <p class="muted">{e(t['act_p'])}</p>
  <ol class="act">{acts}</ol>
</section>

<section id="share">
  <h2>{e(t['share_h'])}</h2>
  <p class="muted">{e(t['share_p'])}</p>
  <div class="share">
    <a class="btn" href="{leaf}">{e(t['leaflet'])}</a>
    <a class="btn" href="{leaf_alt}">{e(t['leaflet_alt'])}</a>
    <a class="btn" id="wa" href="#" data-text="{wa}">WhatsApp</a>
  </div>
</section>

<section>
  <h2>{e(t['more_h'])}</h2>
  <ul class="more">{more}</ul>
</section>

<footer><p class="muted">{e(t['foot'])}</p></footer>
</div>
<script>
(function(){{var a=document.getElementById('wa');if(!a)return;var u=location.href.split('#')[0];
a.href='https://wa.me/?text='+encodeURIComponent(a.getAttribute('data-text')+' '+u);a.target='_blank';a.rel='noopener';}})();
</script>
</html>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "DRAFT_evidence.html").write_text(page("en"), encoding="utf-8")
    (OUT / "DRAFT_evidence_kn.html").write_text(page("kn"), encoding="utf-8")
    print("evidence pages:", len(FINDINGS), "findings,", len(ACTIONS["en"]), "actions")


if __name__ == "__main__":
    main()
