"""Build rti.html: ready-to-file RTI letters about what happened after the 2026 raids.

    py tools/make_rti_page.py

Reads research/officials_tracker/tracker.csv. The page carries posts, places and dates only, never names
(the same rule as the tracker). Re-run after the tracker changes.
"""
import csv
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
rows = list(csv.DictReader(open(ROOT / "research/officials_tracker/tracker.csv", encoding="utf-8")))
lok = [r for r in rows if r["agency"].startswith("Lokayukta")]
stuck = sum(1 for r in rows if r["stage"] in ("Raided", "Searched"))

FORM = ("https://docs.google.com/forms/d/e/1FAIpQLSdGCs8oRCLplhyq3VxHH_olo9GzMJk9I7kv5q54yxgUFp2C3A/viewform"
        "?usp=pp_url&entry.503187352=Something+else&entry.878251699=RTI+reply:+")


def short_dept(d):
    return d.split(" per the ")[0].split(" (earlier")[0]


def d(s):
    import datetime as dt
    return dt.date.fromisoformat(s).strftime("%-d %b %Y") if False else dt.date.fromisoformat(s).strftime("%d %b %Y").lstrip("0")


DATA = [{"dept": short_dept(r["department"]), "post": r["post"], "place": r["district"],
         "date": d(r["action_date"]), "action": r["action"], "src": r["source_url"]} for r in lok]
DEPTS = sorted({x["dept"] for x in DATA if x["dept"] != "not stated"}, key=lambda k: (-sum(1 for x in DATA if x["dept"] == k), k))

HEAD = """To
The Public Information Officer
{to}

Subject: Application under Section 6(1) of the Right to Information Act, 2005

1. Name of applicant: {name}
2. Address for correspondence: {addr}
3. Fee: Rs 10 paid by Indian Postal Order / Demand Draft No. ______ dated ______
"""
FOOT = """
If any item is considered exempt, please give the remaining items, state the reasons under Section 7(8)(i), and consider partial disclosure under Section 10. If any item is held by another public authority, please transfer it under Section 6(3) and inform me.

I am a citizen of India.

Place: ______        Date: ______
Signature: ______
"""

LETTERS = [
    {"id": "l1", "title": "1. Lokayukta police: what happened to the 2026 cases",
     "to": "Office of the Additional Director General of Police, Karnataka Lokayukta\nM.S. Building, Dr B.R. Ambedkar Veedhi, Bengaluru 560 001",
     "why": "The Lokayukta police know whether each case has a chargesheet, a pending sanction request or a court stay. Part A asks only for totals, which should be answered even if Part B is refused.",
     "annex": "all",
     "body": """Period: 1 January 2026 to the date of this application.

Information sought

Part A (totals; no names are needed)
For cases registered by the Lokayukta police from 1 January 2026 to the date of this application under the Prevention of Corruption Act, 1988, please give, department by department:
a. the number of cases registered, separately for trap (bribery) cases and disproportionate-assets cases;
b. the number in which a final report (chargesheet) has been filed in court;
c. the number in which a request for sanction to prosecute (Section 19 of the PC Act) has been sent, and the number in which the competent authority has not decided it within the period allowed by the proviso to Section 19(1);
d. the number in which approval under Section 17A of the PC Act was sought and is pending;
e. the number stayed or quashed by a court, and the number closed by a B-report or other closure report.

Part B (status of the cases in the annex)
The annex lists officers reported in the press as searched or trapped by the Lokayukta police in 2026, by post, place and date of action. For each, please give:
a. the Lokayukta police station and crime number;
b. whether a chargesheet has been filed, and the date;
c. whether sanction to prosecute has been requested, the date, and the authority it was sent to;
d. whether that authority has granted or refused sanction, and the date;
e. whether any court has stayed or quashed the proceedings, with the date and court;
f. whether a closure (B) report has been filed, and the date.

Only dates and stages are sought. No part of the case diary, statements or evidence is requested.
"""},
    {"id": "l2", "title": "2. Government: sanction requests left pending",
     "to": "Department of Personnel and Administrative Reforms (Services)\nVidhana Soudha, Bengaluru 560 001",
     "why": "A case cannot go to trial until the officer's department gives sanction to prosecute. In 2024 the Lokayukta said 206 officials' sanctions had been pending for months. This asks for today's list, by department and designation, and the rules on time limits.",
     "annex": None,
     "body": """Information sought

1. A statement, as on the date of reply, of requests from the Karnataka Lokayukta (police wing, or Lokayukta / Upalokayukta) for sanction to prosecute government servants, or for approval under Section 17A of the Prevention of Corruption Act, 1988, pending with any department of the Government of Karnataka, showing for each: the department; the designation of the government servant; the date the request was received; and how long it has been pending.
2. For 1 January 2024 to the date of reply, the number of such requests decided by each department, separately for sanction granted and refused, and the number decided more than four months after receipt.
3. Copies of the circulars or government orders now in force that fix (a) the time limit for deciding a request for sanction to prosecute, and (b) who monitors pending requests.
4. Copies of the proceedings of any review meeting held in 2025 or 2026 on pending Lokayukta sanction requests.
5. If such a statement was furnished to the Legislative Assembly, the Legislative Council or the High Court in 2025 or 2026, a copy.
"""},
    {"id": "l3", "title": "3. One department: suspension, sanction, promotion",
     "to": "[Name of the department or company, and its head-office address]",
     "why": "Each department decides whether its officer is suspended, whether to allow prosecution, and whether to transfer or promote them. Suspension and posting orders are routine office orders. Pick a department below; its officers are added as the annex.",
     "annex": "dept",
     "body": """Information sought

The officers described in the annex (post, place and date of action), serving or retired from this department or company, were reported in the press as searched or trapped by the Karnataka Lokayukta police on the dates shown. For each of them, please give:
1. Whether the officer was placed under suspension (including deemed suspension on detention for more than 48 hours under the Karnataka Civil Services (Classification, Control and Appeal) Rules, 1957, or the equivalent rules of this body), with the date and a copy of the order; and whether the suspension has been revoked, with the date and a copy of that order.
2. Whether a request for sanction to prosecute, or for approval under Section 17A of the Prevention of Corruption Act, 1988, has been received from the Lokayukta; the date received; the date of decision; and the decision (granted / refused / pending).
3. Whether a departmental inquiry or disciplinary proceeding has been initiated after the Lokayukta action, with the date of the charge memo.
4. Any transfer, posting, promotion or additional charge given to the officer after the date of the Lokayukta action, with the date and a copy of the order.
5. The officer's present designation and place of posting, or the date of retirement.

Items 1, 4 and 5 are office orders issued in the ordinary course of business.
"""},
    {"id": "l4", "title": "4. Officers who never declared their property",
     "to": "Department of Personnel and Administrative Reforms (Services)\nVidhana Soudha, Bengaluru 560 001",
     "why": "Every government servant must file an annual statement of property. A missing return is often the first sign investigators look for. The government has given such lists to the Assembly before.",
     "annex": None,
     "body": """Information sought

Under the Karnataka Civil Services (Conduct) Rules, 2021 (declaration of assets and liabilities) and the All India Services (Conduct) Rules for IAS officers of the Karnataka cadre:
1. For the returns due in 2023-24, 2024-25 and 2025-26, the number of officers required to file annual property returns and the number who did not file by the due date, department by department, separately for IAS, KAS and other Group A and Group B officers.
2. The list of IAS and KAS officers who had not filed for 2024-25 and 2025-26 as on the date of reply.
3. The action taken against officers who did not file (notices, increments withheld, vigilance clearance refused, disciplinary proceedings), with numbers for each year.
4. Copies of any circular issued in 2024, 2025 or 2026 on filing property returns, including any instruction to publish them online.
"""},
    {"id": "l5", "title": "5. A corporation's bank accounts",
     "to": "[Name of the corporation, and its head-office address]",
     "why": "In 2024-25 the state auditor found development corporations keeping government money in bank accounts outside the treasury, against a 2023 order, while the books showed it as spent: ₹410 crore in 32 accounts, and ₹412 crore of unused grants in four corporations. Pick a corporation; the letter asks where its money is.",
     "annex": "corp",
     "body": """Information sought

For this corporation, as on 31 March 2025 and as on the date of reply:
1. A list of every bank account held in the corporation's name (bank, branch, type of account such as savings, current, escrow, recovery or fixed deposit, and purpose) with the balance in each. Account numbers may be masked.
2. Copies of the board resolutions or government orders under which each of these accounts was opened, and of any order allowing an account to remain open after the Finance Department's order of 28 February 2023 directing corporations to close their bank accounts and use Personal Deposit accounts.
3. For any escrow or recovery account: what money it holds, where that money came from, and on whose instructions it is held.
4. The grants received from the Government in 2022-23, 2023-24 and 2024-25, the amount spent each year, and the unspent balance, with where the unspent balance is held (bank account, fixed deposit or Personal Deposit account).
5. Interest earned on government grants in 2020-21 to 2024-25, and the amount remitted to the Government (head of account 0049), with dates.
6. The year of the latest audited annual accounts of the corporation, and a copy of those accounts and of the auditor's report on them.
"""},
    {"id": "l6", "title": "6. A deposit account's ledger (for example, the mining restoration fund)",
     "to": "Office of the Accountant General (Accounts and Entitlements), Karnataka\nPark House Road, Bengaluru 560 001",
     "why": "₹4,077 crore left the mining restoration fund's treasury deposit account in 2024-25, and ₹15,991 crore left all deposit accounts, but the published accounts give no account-by-account withdrawals. The office that keeps the accounts holds the ledger.",
     "annex": None,
     "body": """Information sought

1. The ledger, or a statement of transactions, for 2024-25 of the Personal Deposit account in the name of the Managing Director, Karnataka Mining Environment Restoration Corporation (KMERC), under head 8443-106 Personal Deposits: opening balance, each receipt and each withdrawal with date, amount and the voucher or transfer reference, and closing balance.
2. For 2024-25, a statement of receipts and withdrawals for every Personal Deposit account under head 8443-106, administrator by administrator, as compiled for the Finance Accounts (the Finance Accounts show total withdrawals of ₹15,991.01 crore but no breakdown).
3. Any correspondence in 2024-25 between your office and the Treasury or KMERC on reconciliation of the KMERC Personal Deposit account.
"""},
]

# ---- Kannada (needs a native reader's review, like the rest of the site's Kannada) ----
HEAD_KN = """ಗೆ,
ಸಾರ್ವಜನಿಕ ಮಾಹಿತಿ ಅಧಿಕಾರಿಗಳು
{to}

ವಿಷಯ: ಮಾಹಿತಿ ಹಕ್ಕು ಅಧಿನಿಯಮ, 2005ರ ಸೆಕ್ಷನ್ 6(1)ರ ಅಡಿಯಲ್ಲಿ ಅರ್ಜಿ

1. ಅರ್ಜಿದಾರರ ಹೆಸರು: {name}
2. ಪತ್ರ ವ್ಯವಹಾರದ ವಿಳಾಸ: {addr}
3. ಶುಲ್ಕ: ರೂ. 10, ಭಾರತೀಯ ಅಂಚೆ ಆದೇಶ (IPO) / ಡಿಮ್ಯಾಂಡ್ ಡ್ರಾಫ್ಟ್ ಸಂಖ್ಯೆ ______ ದಿನಾಂಕ ______ ಮೂಲಕ ಪಾವತಿಸಲಾಗಿದೆ
"""
FOOT_KN = """
ಯಾವುದೇ ಅಂಶಕ್ಕೆ ವಿನಾಯಿತಿ ಅನ್ವಯಿಸುತ್ತದೆ ಎಂದು ಪರಿಗಣಿಸಿದರೆ, ಉಳಿದ ಅಂಶಗಳ ಮಾಹಿತಿಯನ್ನು ನೀಡಿ, ಸೆಕ್ಷನ್ 7(8)(i)ರ ಅಡಿ ಕಾರಣಗಳನ್ನು ತಿಳಿಸಿ, ಮತ್ತು ಸೆಕ್ಷನ್ 10ರ ಅಡಿ ಭಾಗಶಃ ಮಾಹಿತಿ ನೀಡುವುದನ್ನು ಪರಿಗಣಿಸಬೇಕೆಂದು ಕೋರುತ್ತೇನೆ. ಯಾವುದೇ ಮಾಹಿತಿ ಬೇರೆ ಸಾರ್ವಜನಿಕ ಪ್ರಾಧಿಕಾರದ ಬಳಿ ಇದ್ದರೆ, ಸೆಕ್ಷನ್ 6(3)ರ ಅಡಿ ಅರ್ಜಿಯನ್ನು ವರ್ಗಾಯಿಸಿ ನನಗೆ ತಿಳಿಸಬೇಕೆಂದು ಕೋರುತ್ತೇನೆ.

ನಾನು ಭಾರತದ ನಾಗರಿಕ/ನಾಗರಿಕಳು.

ಸ್ಥಳ: ______        ದಿನಾಂಕ: ______
ಸಹಿ: ______
"""
KN = {
    "l1": {"title": "1. ಲೋಕಾಯುಕ್ತ ಪೊಲೀಸ್: 2026ರ ಪ್ರಕರಣಗಳು ಏನಾದವು",
           "to": "ಅಪರ ಪೊಲೀಸ್ ಮಹಾನಿರ್ದೇಶಕರ ಕಚೇರಿ, ಕರ್ನಾಟಕ ಲೋಕಾಯುಕ್ತ\nಎಂ.ಎಸ್. ಕಟ್ಟಡ, ಡಾ. ಬಿ.ಆರ್. ಅಂಬೇಡ್ಕರ್ ವೀಧಿ, ಬೆಂಗಳೂರು 560 001",
           "why": "ಪ್ರತಿ ಪ್ರಕರಣದಲ್ಲಿ ದೋಷಾರೋಪಣ ಪಟ್ಟಿ ಸಲ್ಲಿಕೆಯಾಗಿದೆಯೇ, ಅಭಿಯೋಜನಾ ಮಂಜೂರಾತಿ ಬಾಕಿ ಇದೆಯೇ, ನ್ಯಾಯಾಲಯ ತಡೆ ನೀಡಿದೆಯೇ ಎಂಬುದು ಲೋಕಾಯುಕ್ತ ಪೊಲೀಸರಿಗೆ ಗೊತ್ತು. ಭಾಗ 'ಎ' ಒಟ್ಟು ಸಂಖ್ಯೆಗಳನ್ನು ಮಾತ್ರ ಕೇಳುತ್ತದೆ; ಭಾಗ 'ಬಿ' ನಿರಾಕರಿಸಿದರೂ ಇದಕ್ಕೆ ಉತ್ತರ ಸಿಗಬೇಕು.",
           "body": """ಅವಧಿ: 1 ಜನವರಿ 2026ರಿಂದ ಈ ಅರ್ಜಿಯ ದಿನಾಂಕದವರೆಗೆ.

ಕೋರಿರುವ ಮಾಹಿತಿ

ಭಾಗ ಎ (ಒಟ್ಟು ಸಂಖ್ಯೆಗಳು; ಹೆಸರುಗಳ ಅಗತ್ಯವಿಲ್ಲ)
1 ಜನವರಿ 2026ರಿಂದ ಈ ಅರ್ಜಿಯ ದಿನಾಂಕದವರೆಗೆ ಭ್ರಷ್ಟಾಚಾರ ನಿಯಂತ್ರಣ ಕಾಯ್ದೆ, 1988ರ ಅಡಿ ಲೋಕಾಯುಕ್ತ ಪೊಲೀಸರು ದಾಖಲಿಸಿದ ಪ್ರಕರಣಗಳ ಬಗ್ಗೆ, ಇಲಾಖಾವಾರು:
ಎ. ದಾಖಲಾದ ಪ್ರಕರಣಗಳ ಸಂಖ್ಯೆ, ಟ್ರ್ಯಾಪ್ (ಲಂಚ ಸ್ವೀಕಾರ) ಪ್ರಕರಣಗಳು ಮತ್ತು ಆದಾಯ ಮೀರಿದ ಆಸ್ತಿ ಪ್ರಕರಣಗಳು ಪ್ರತ್ಯೇಕವಾಗಿ;
ಬಿ. ನ್ಯಾಯಾಲಯಕ್ಕೆ ಅಂತಿಮ ವರದಿ (ದೋಷಾರೋಪಣ ಪಟ್ಟಿ) ಸಲ್ಲಿಸಲಾದ ಪ್ರಕರಣಗಳ ಸಂಖ್ಯೆ;
ಸಿ. ಅಭಿಯೋಜನಾ ಮಂಜೂರಾತಿಗಾಗಿ (ಭ್ರಷ್ಟಾಚಾರ ನಿಯಂತ್ರಣ ಕಾಯ್ದೆಯ ಸೆಕ್ಷನ್ 19) ಕೋರಿಕೆ ಕಳುಹಿಸಲಾದ ಪ್ರಕರಣಗಳ ಸಂಖ್ಯೆ, ಮತ್ತು ಸೆಕ್ಷನ್ 19(1)ರ ಪರಂತುಕದಲ್ಲಿ ನೀಡಿರುವ ಅವಧಿಯೊಳಗೆ ಸಕ್ಷಮ ಪ್ರಾಧಿಕಾರ ತೀರ್ಮಾನಿಸದ ಪ್ರಕರಣಗಳ ಸಂಖ್ಯೆ;
ಡಿ. ಸೆಕ್ಷನ್ 17ಎ ಅಡಿ ಅನುಮೋದನೆ ಕೋರಿ ಬಾಕಿ ಇರುವ ಪ್ರಕರಣಗಳ ಸಂಖ್ಯೆ;
ಇ. ನ್ಯಾಯಾಲಯ ತಡೆ ನೀಡಿದ ಅಥವಾ ರದ್ದುಪಡಿಸಿದ ಪ್ರಕರಣಗಳ ಸಂಖ್ಯೆ, ಮತ್ತು ಬಿ-ವರದಿ ಅಥವಾ ಇತರ ಮುಕ್ತಾಯ ವರದಿಯಿಂದ ಮುಕ್ತಾಯಗೊಂಡ ಪ್ರಕರಣಗಳ ಸಂಖ್ಯೆ.

ಭಾಗ ಬಿ (ಅನುಬಂಧದಲ್ಲಿರುವ ಪ್ರಕರಣಗಳ ಸ್ಥಿತಿ)
2026ರಲ್ಲಿ ಲೋಕಾಯುಕ್ತ ಪೊಲೀಸರು ಶೋಧ ನಡೆಸಿದ ಅಥವಾ ಟ್ರ್ಯಾಪ್ ಮಾಡಿದ ಎಂದು ಪತ್ರಿಕೆಗಳಲ್ಲಿ ವರದಿಯಾದ ಅಧಿಕಾರಿಗಳನ್ನು ಹುದ್ದೆ, ಸ್ಥಳ ಮತ್ತು ಕ್ರಮದ ದಿನಾಂಕದೊಂದಿಗೆ ಅನುಬಂಧದಲ್ಲಿ ಪಟ್ಟಿ ಮಾಡಲಾಗಿದೆ. ಪ್ರತಿಯೊಬ್ಬರ ಬಗ್ಗೆ:
ಎ. ಲೋಕಾಯುಕ್ತ ಪೊಲೀಸ್ ಠಾಣೆ ಮತ್ತು ಅಪರಾಧ ಸಂಖ್ಯೆ;
ಬಿ. ದೋಷಾರೋಪಣ ಪಟ್ಟಿ ಸಲ್ಲಿಸಲಾಗಿದೆಯೇ, ಮತ್ತು ದಿನಾಂಕ;
ಸಿ. ಅಭಿಯೋಜನಾ ಮಂಜೂರಾತಿ ಕೋರಲಾಗಿದೆಯೇ, ದಿನಾಂಕ, ಮತ್ತು ಯಾವ ಪ್ರಾಧಿಕಾರಕ್ಕೆ ಕಳುಹಿಸಲಾಗಿದೆ;
ಡಿ. ಆ ಪ್ರಾಧಿಕಾರ ಮಂಜೂರಾತಿ ನೀಡಿದೆಯೇ ಅಥವಾ ನಿರಾಕರಿಸಿದೆಯೇ, ಮತ್ತು ದಿನಾಂಕ;
ಇ. ಯಾವುದೇ ನ್ಯಾಯಾಲಯ ಪ್ರಕರಣಕ್ಕೆ ತಡೆ ನೀಡಿದೆಯೇ ಅಥವಾ ರದ್ದುಪಡಿಸಿದೆಯೇ, ದಿನಾಂಕ ಮತ್ತು ನ್ಯಾಯಾಲಯ;
ಎಫ್. ಮುಕ್ತಾಯ (ಬಿ) ವರದಿ ಸಲ್ಲಿಸಲಾಗಿದೆಯೇ, ಮತ್ತು ದಿನಾಂಕ.

ದಿನಾಂಕಗಳು ಮತ್ತು ಹಂತಗಳನ್ನು ಮಾತ್ರ ಕೋರಲಾಗಿದೆ. ಕೇಸ್ ಡೈರಿ, ಹೇಳಿಕೆಗಳು ಅಥವಾ ಸಾಕ್ಷ್ಯದ ಯಾವುದೇ ಭಾಗವನ್ನು ಕೋರಿಲ್ಲ.
"""},
    "l2": {"title": "2. ಸರ್ಕಾರ: ಬಾಕಿ ಉಳಿದ ಅಭಿಯೋಜನಾ ಮಂಜೂರಾತಿಗಳು",
           "to": "ಸಿಬ್ಬಂದಿ ಮತ್ತು ಆಡಳಿತ ಸುಧಾರಣೆ ಇಲಾಖೆ (ಸೇವೆಗಳು)\nವಿಧಾನಸೌಧ, ಬೆಂಗಳೂರು 560 001",
           "why": "ಅಧಿಕಾರಿಯ ಇಲಾಖೆ ಅಭಿಯೋಜನೆಗೆ ಮಂಜೂರಾತಿ ನೀಡುವವರೆಗೆ ಪ್ರಕರಣ ವಿಚಾರಣೆಗೆ ಹೋಗುವುದಿಲ್ಲ. 2024ರಲ್ಲಿ 206 ಅಧಿಕಾರಿಗಳ ಮಂಜೂರಾತಿ ತಿಂಗಳುಗಳಿಂದ ಬಾಕಿ ಇದೆ ಎಂದು ಲೋಕಾಯುಕ್ತ ಹೇಳಿತ್ತು. ಇಂದಿನ ಪಟ್ಟಿಯನ್ನು ಇಲಾಖೆ ಮತ್ತು ಹುದ್ದೆವಾರು, ಹಾಗೂ ಕಾಲಮಿತಿಯ ನಿಯಮಗಳನ್ನು ಈ ಪತ್ರ ಕೇಳುತ್ತದೆ.",
           "body": """ಕೋರಿರುವ ಮಾಹಿತಿ

1. ಸರ್ಕಾರಿ ನೌಕರರ ಅಭಿಯೋಜನೆಗೆ ಮಂಜೂರಾತಿ, ಅಥವಾ ಭ್ರಷ್ಟಾಚಾರ ನಿಯಂತ್ರಣ ಕಾಯ್ದೆ, 1988ರ ಸೆಕ್ಷನ್ 17ಎ ಅಡಿ ಅನುಮೋದನೆ ಕೋರಿ ಕರ್ನಾಟಕ ಲೋಕಾಯುಕ್ತದಿಂದ (ಪೊಲೀಸ್ ವಿಭಾಗ, ಅಥವಾ ಲೋಕಾಯುಕ್ತ / ಉಪಲೋಕಾಯುಕ್ತ) ಬಂದು, ಉತ್ತರದ ದಿನಾಂಕದಂದು ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಯಾವುದೇ ಇಲಾಖೆಯಲ್ಲಿ ಬಾಕಿ ಇರುವ ಕೋರಿಕೆಗಳ ವಿವರ ಪಟ್ಟಿ: ಇಲಾಖೆ; ಸರ್ಕಾರಿ ನೌಕರರ ಹುದ್ದೆ; ಕೋರಿಕೆ ಸ್ವೀಕರಿಸಿದ ದಿನಾಂಕ; ಮತ್ತು ಎಷ್ಟು ಸಮಯದಿಂದ ಬಾಕಿ ಇದೆ.
2. 1 ಜನವರಿ 2024ರಿಂದ ಉತ್ತರದ ದಿನಾಂಕದವರೆಗೆ ಪ್ರತಿ ಇಲಾಖೆ ತೀರ್ಮಾನಿಸಿದ ಇಂತಹ ಕೋರಿಕೆಗಳ ಸಂಖ್ಯೆ, ಮಂಜೂರಾತಿ ನೀಡಿದ ಮತ್ತು ನಿರಾಕರಿಸಿದವು ಪ್ರತ್ಯೇಕವಾಗಿ, ಹಾಗೂ ಸ್ವೀಕರಿಸಿದ ನಾಲ್ಕು ತಿಂಗಳ ನಂತರ ತೀರ್ಮಾನಿಸಿದವುಗಳ ಸಂಖ್ಯೆ.
3. (ಎ) ಅಭಿಯೋಜನಾ ಮಂಜೂರಾತಿ ಕೋರಿಕೆಯನ್ನು ತೀರ್ಮಾನಿಸಲು ಕಾಲಮಿತಿ, ಮತ್ತು (ಬಿ) ಬಾಕಿ ಕೋರಿಕೆಗಳ ಮೇಲ್ವಿಚಾರಣೆ ಯಾರದು ಎಂದು ನಿಗದಿಪಡಿಸುವ ಜಾರಿಯಲ್ಲಿರುವ ಸುತ್ತೋಲೆಗಳು ಅಥವಾ ಸರ್ಕಾರಿ ಆದೇಶಗಳ ಪ್ರತಿಗಳು.
4. ಬಾಕಿ ಇರುವ ಲೋಕಾಯುಕ್ತ ಮಂಜೂರಾತಿ ಕೋರಿಕೆಗಳ ಬಗ್ಗೆ 2025 ಅಥವಾ 2026ರಲ್ಲಿ ನಡೆದ ಯಾವುದೇ ಪರಿಶೀಲನಾ ಸಭೆಯ ನಡವಳಿಗಳ ಪ್ರತಿಗಳು.
5. ಇಂತಹ ವಿವರ ಪಟ್ಟಿಯನ್ನು 2025 ಅಥವಾ 2026ರಲ್ಲಿ ವಿಧಾನಸಭೆ, ವಿಧಾನ ಪರಿಷತ್ ಅಥವಾ ಉಚ್ಚ ನ್ಯಾಯಾಲಯಕ್ಕೆ ಸಲ್ಲಿಸಿದ್ದರೆ, ಅದರ ಪ್ರತಿ.
"""},
    "l3": {"title": "3. ಒಂದು ಇಲಾಖೆ: ಅಮಾನತು, ಮಂಜೂರಾತಿ, ಬಡ್ತಿ",
           "to": "[ಇಲಾಖೆ ಅಥವಾ ಕಂಪನಿಯ ಹೆಸರು, ಮತ್ತು ಕೇಂದ್ರ ಕಚೇರಿಯ ವಿಳಾಸ]",
           "why": "ತನ್ನ ಅಧಿಕಾರಿಯನ್ನು ಅಮಾನತು ಮಾಡಬೇಕೇ, ಅಭಿಯೋಜನೆಗೆ ಅನುಮತಿ ನೀಡಬೇಕೇ, ವರ್ಗಾವಣೆ ಅಥವಾ ಬಡ್ತಿ ನೀಡಬೇಕೇ ಎಂದು ಪ್ರತಿ ಇಲಾಖೆ ತೀರ್ಮಾನಿಸುತ್ತದೆ. ಅಮಾನತು ಮತ್ತು ನಿಯೋಜನೆ ಆದೇಶಗಳು ಸಾಮಾನ್ಯ ಕಚೇರಿ ಆದೇಶಗಳು. ಕೆಳಗೆ ಇಲಾಖೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ; ಅದರ ಅಧಿಕಾರಿಗಳನ್ನು ಅನುಬಂಧವಾಗಿ ಸೇರಿಸಲಾಗುತ್ತದೆ.",
           "body": """ಕೋರಿರುವ ಮಾಹಿತಿ

ಅನುಬಂಧದಲ್ಲಿ ವಿವರಿಸಿರುವ (ಹುದ್ದೆ, ಸ್ಥಳ ಮತ್ತು ಕ್ರಮದ ದಿನಾಂಕ) ಈ ಇಲಾಖೆ ಅಥವಾ ಕಂಪನಿಯ ಸೇವೆಯಲ್ಲಿರುವ ಅಥವಾ ನಿವೃತ್ತ ಅಧಿಕಾರಿಗಳ ಮೇಲೆ, ತೋರಿಸಿರುವ ದಿನಾಂಕಗಳಂದು ಕರ್ನಾಟಕ ಲೋಕಾಯುಕ್ತ ಪೊಲೀಸರು ಶೋಧ ನಡೆಸಿದರು ಅಥವಾ ಟ್ರ್ಯಾಪ್ ಮಾಡಿದರು ಎಂದು ಪತ್ರಿಕೆಗಳಲ್ಲಿ ವರದಿಯಾಗಿದೆ. ಪ್ರತಿಯೊಬ್ಬರ ಬಗ್ಗೆ:
1. ಅಧಿಕಾರಿಯನ್ನು ಅಮಾನತಿನಲ್ಲಿ ಇಡಲಾಗಿದೆಯೇ (ಕರ್ನಾಟಕ ನಾಗರಿಕ ಸೇವಾ (ವರ್ಗೀಕರಣ, ನಿಯಂತ್ರಣ ಮತ್ತು ಮೇಲ್ಮನವಿ) ನಿಯಮಗಳು, 1957, ಅಥವಾ ಈ ಸಂಸ್ಥೆಯ ಸಮಾನ ನಿಯಮಗಳ ಅಡಿ 48 ಗಂಟೆಗಳಿಗಿಂತ ಹೆಚ್ಚು ಬಂಧನದಿಂದಾಗಿ ಪರಿಗಣಿತ ಅಮಾನತು ಸೇರಿದಂತೆ), ಆದೇಶದ ದಿನಾಂಕ ಮತ್ತು ಪ್ರತಿ; ಮತ್ತು ಅಮಾನತು ಹಿಂಪಡೆಯಲಾಗಿದೆಯೇ, ದಿನಾಂಕ ಮತ್ತು ಆ ಆದೇಶದ ಪ್ರತಿ.
2. ಲೋಕಾಯುಕ್ತದಿಂದ ಅಭಿಯೋಜನಾ ಮಂಜೂರಾತಿ, ಅಥವಾ ಭ್ರಷ್ಟಾಚಾರ ನಿಯಂತ್ರಣ ಕಾಯ್ದೆ, 1988ರ ಸೆಕ್ಷನ್ 17ಎ ಅಡಿ ಅನುಮೋದನೆ ಕೋರಿಕೆ ಬಂದಿದೆಯೇ; ಸ್ವೀಕರಿಸಿದ ದಿನಾಂಕ; ತೀರ್ಮಾನದ ದಿನಾಂಕ; ಮತ್ತು ತೀರ್ಮಾನ (ನೀಡಲಾಗಿದೆ / ನಿರಾಕರಿಸಲಾಗಿದೆ / ಬಾಕಿ).
3. ಲೋಕಾಯುಕ್ತ ಕ್ರಮದ ನಂತರ ಯಾವುದೇ ಇಲಾಖಾ ವಿಚಾರಣೆ ಅಥವಾ ಶಿಸ್ತು ಕ್ರಮ ಆರಂಭಿಸಲಾಗಿದೆಯೇ, ಆರೋಪ ಪಟ್ಟಿಯ (ಚಾರ್ಜ್ ಮೆಮೊ) ದಿನಾಂಕದೊಂದಿಗೆ.
4. ಲೋಕಾಯುಕ್ತ ಕ್ರಮದ ದಿನಾಂಕದ ನಂತರ ಅಧಿಕಾರಿಗೆ ನೀಡಲಾದ ಯಾವುದೇ ವರ್ಗಾವಣೆ, ನಿಯೋಜನೆ, ಬಡ್ತಿ ಅಥವಾ ಹೆಚ್ಚುವರಿ ಪ್ರಭಾರ, ದಿನಾಂಕ ಮತ್ತು ಆದೇಶದ ಪ್ರತಿಯೊಂದಿಗೆ.
5. ಅಧಿಕಾರಿಯ ಈಗಿನ ಹುದ್ದೆ ಮತ್ತು ಕಾರ್ಯಸ್ಥಳ, ಅಥವಾ ನಿವೃತ್ತಿಯ ದಿನಾಂಕ.

ಅಂಶಗಳು 1, 4 ಮತ್ತು 5 ಸಾಮಾನ್ಯ ಕಾರ್ಯನಿರ್ವಹಣೆಯಲ್ಲಿ ಹೊರಡಿಸುವ ಕಚೇರಿ ಆದೇಶಗಳು.
"""},
    "l4": {"title": "4. ಆಸ್ತಿ ವಿವರ ಸಲ್ಲಿಸದ ಅಧಿಕಾರಿಗಳು",
           "to": "ಸಿಬ್ಬಂದಿ ಮತ್ತು ಆಡಳಿತ ಸುಧಾರಣೆ ಇಲಾಖೆ (ಸೇವೆಗಳು)\nವಿಧಾನಸೌಧ, ಬೆಂಗಳೂರು 560 001",
           "why": "ಪ್ರತಿ ಸರ್ಕಾರಿ ನೌಕರರು ವಾರ್ಷಿಕ ಆಸ್ತಿ ವಿವರ ಸಲ್ಲಿಸಬೇಕು. ವಿವರ ಸಲ್ಲಿಸದಿರುವುದು ತನಿಖಾಧಿಕಾರಿಗಳು ಮೊದಲು ಗಮನಿಸುವ ಸೂಚನೆಗಳಲ್ಲಿ ಒಂದು. ಸರ್ಕಾರ ಇಂತಹ ಪಟ್ಟಿಗಳನ್ನು ಹಿಂದೆ ವಿಧಾನಸಭೆಗೆ ನೀಡಿದೆ.",
           "body": """ಕೋರಿರುವ ಮಾಹಿತಿ

ಕರ್ನಾಟಕ ನಾಗರಿಕ ಸೇವಾ (ನಡತೆ) ನಿಯಮಗಳು, 2021 (ಆಸ್ತಿ ಮತ್ತು ಹೊಣೆಗಾರಿಕೆಗಳ ಘೋಷಣೆ) ಮತ್ತು ಕರ್ನಾಟಕ ವೃಂದದ ಐಎಎಸ್ ಅಧಿಕಾರಿಗಳಿಗೆ ಅಖಿಲ ಭಾರತ ಸೇವಾ (ನಡತೆ) ನಿಯಮಗಳ ಅಡಿ:
1. 2023-24, 2024-25 ಮತ್ತು 2025-26ರಲ್ಲಿ ಸಲ್ಲಿಸಬೇಕಾಗಿದ್ದ ವಾರ್ಷಿಕ ಆಸ್ತಿ ವಿವರಗಳ ಬಗ್ಗೆ, ಸಲ್ಲಿಸಬೇಕಾಗಿದ್ದ ಅಧಿಕಾರಿಗಳ ಸಂಖ್ಯೆ ಮತ್ತು ನಿಗದಿತ ದಿನಾಂಕದೊಳಗೆ ಸಲ್ಲಿಸದವರ ಸಂಖ್ಯೆ, ಇಲಾಖಾವಾರು, ಐಎಎಸ್, ಕೆಎಎಸ್ ಮತ್ತು ಇತರ ಗ್ರೂಪ್ ಎ ಹಾಗೂ ಗ್ರೂಪ್ ಬಿ ಅಧಿಕಾರಿಗಳು ಪ್ರತ್ಯೇಕವಾಗಿ.
2. ಉತ್ತರದ ದಿನಾಂಕದಂದು 2024-25 ಮತ್ತು 2025-26ರ ಆಸ್ತಿ ವಿವರ ಸಲ್ಲಿಸದ ಐಎಎಸ್ ಮತ್ತು ಕೆಎಎಸ್ ಅಧಿಕಾರಿಗಳ ಪಟ್ಟಿ.
3. ವಿವರ ಸಲ್ಲಿಸದ ಅಧಿಕಾರಿಗಳ ವಿರುದ್ಧ ಕೈಗೊಂಡ ಕ್ರಮ (ನೋಟಿಸ್‌ಗಳು, ವೇತನ ಬಡ್ತಿ ತಡೆ, ಜಾಗೃತ ದಳದ ಅನುಮತಿ ನಿರಾಕರಣೆ, ಶಿಸ್ತು ಕ್ರಮ), ಪ್ರತಿ ವರ್ಷದ ಸಂಖ್ಯೆಗಳೊಂದಿಗೆ.
4. ಆಸ್ತಿ ವಿವರ ಸಲ್ಲಿಕೆ ಕುರಿತು 2024, 2025 ಅಥವಾ 2026ರಲ್ಲಿ ಹೊರಡಿಸಿದ ಯಾವುದೇ ಸುತ್ತೋಲೆಯ ಪ್ರತಿಗಳು, ಅವುಗಳನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪ್ರಕಟಿಸುವ ಸೂಚನೆ ಇದ್ದರೆ ಅದೂ ಸೇರಿದಂತೆ.
"""},
    "l5": {"title": "5. ಒಂದು ನಿಗಮದ ಬ್ಯಾಂಕ್ ಖಾತೆಗಳು",
           "to": "[ನಿಗಮದ ಹೆಸರು, ಮತ್ತು ಕೇಂದ್ರ ಕಚೇರಿಯ ವಿಳಾಸ]",
           "why": "2024-25ರಲ್ಲಿ ಅಭಿವೃದ್ಧಿ ನಿಗಮಗಳು 2023ರ ಆದೇಶಕ್ಕೆ ವಿರುದ್ಧವಾಗಿ ಸರ್ಕಾರದ ಹಣವನ್ನು ಖಜಾನೆಯ ಹೊರಗಿನ ಬ್ಯಾಂಕ್ ಖಾತೆಗಳಲ್ಲಿ ಇಟ್ಟಿವೆ, ಲೆಕ್ಕದಲ್ಲಿ ಅದನ್ನು ಖರ್ಚಾಗಿದೆ ಎಂದು ತೋರಿಸಲಾಗಿದೆ ಎಂದು ರಾಜ್ಯದ ಲೆಕ್ಕಪರಿಶೋಧಕರು ಕಂಡುಕೊಂಡರು: 32 ಖಾತೆಗಳಲ್ಲಿ ₹410 ಕೋಟಿ, ಮತ್ತು ನಾಲ್ಕು ನಿಗಮಗಳಲ್ಲಿ ₹412 ಕೋಟಿ ಬಳಸದ ಅನುದಾನ. ಒಂದು ನಿಗಮವನ್ನು ಆಯ್ಕೆಮಾಡಿ; ಅದರ ಹಣ ಎಲ್ಲಿದೆ ಎಂದು ಪತ್ರ ಕೇಳುತ್ತದೆ.",
           "body": """ಕೋರಿರುವ ಮಾಹಿತಿ

ಈ ನಿಗಮದ ಬಗ್ಗೆ, 31 ಮಾರ್ಚ್ 2025ರಂದು ಮತ್ತು ಉತ್ತರದ ದಿನಾಂಕದಂದು ಇದ್ದಂತೆ:
1. ನಿಗಮದ ಹೆಸರಿನಲ್ಲಿರುವ ಎಲ್ಲ ಬ್ಯಾಂಕ್ ಖಾತೆಗಳ ಪಟ್ಟಿ (ಬ್ಯಾಂಕ್, ಶಾಖೆ, ಖಾತೆಯ ಪ್ರಕಾರ: ಉಳಿತಾಯ, ಚಾಲ್ತಿ, ಎಸ್ಕ್ರೋ, ವಸೂಲಾತಿ ಅಥವಾ ನಿಶ್ಚಿತ ಠೇವಣಿ, ಮತ್ತು ಉದ್ದೇಶ) ಪ್ರತಿ ಖಾತೆಯ ಶಿಲ್ಕಿನೊಂದಿಗೆ. ಖಾತೆ ಸಂಖ್ಯೆಗಳನ್ನು ಭಾಗಶಃ ಮರೆಮಾಡಬಹುದು.
2. ಈ ಪ್ರತಿ ಖಾತೆಯನ್ನು ತೆರೆಯಲು ಅನುಮತಿಸಿದ ಆಡಳಿತ ಮಂಡಳಿ ನಿರ್ಣಯಗಳು ಅಥವಾ ಸರ್ಕಾರಿ ಆದೇಶಗಳ ಪ್ರತಿಗಳು, ಮತ್ತು ಬ್ಯಾಂಕ್ ಖಾತೆಗಳನ್ನು ಮುಚ್ಚಿ ವೈಯಕ್ತಿಕ ಠೇವಣಿ (ಪಿಡಿ) ಖಾತೆ ಬಳಸುವಂತೆ ಆರ್ಥಿಕ ಇಲಾಖೆ 28 ಫೆಬ್ರವರಿ 2023ರಂದು ನೀಡಿದ ಆದೇಶದ ನಂತರವೂ ಯಾವುದೇ ಖಾತೆ ಮುಂದುವರಿಯಲು ಅನುಮತಿಸಿದ ಆದೇಶದ ಪ್ರತಿ.
3. ಯಾವುದೇ ಎಸ್ಕ್ರೋ ಅಥವಾ ವಸೂಲಾತಿ ಖಾತೆಯಲ್ಲಿ ಯಾವ ಹಣವಿದೆ, ಆ ಹಣ ಎಲ್ಲಿಂದ ಬಂತು, ಮತ್ತು ಯಾರ ಸೂಚನೆಯ ಮೇರೆಗೆ ಅದನ್ನು ಇಡಲಾಗಿದೆ.
4. 2022-23, 2023-24 ಮತ್ತು 2024-25ರಲ್ಲಿ ಸರ್ಕಾರದಿಂದ ಪಡೆದ ಅನುದಾನ, ಪ್ರತಿ ವರ್ಷ ಖರ್ಚು ಮಾಡಿದ ಮೊತ್ತ, ಮತ್ತು ಖರ್ಚಾಗದ ಶಿಲ್ಕು, ಹಾಗೂ ಆ ಶಿಲ್ಕನ್ನು ಎಲ್ಲಿ ಇಡಲಾಗಿದೆ (ಬ್ಯಾಂಕ್ ಖಾತೆ, ನಿಶ್ಚಿತ ಠೇವಣಿ ಅಥವಾ ವೈಯಕ್ತಿಕ ಠೇವಣಿ ಖಾತೆ).
5. 2020-21ರಿಂದ 2024-25ರವರೆಗೆ ಸರ್ಕಾರಿ ಅನುದಾನದ ಮೇಲೆ ಗಳಿಸಿದ ಬಡ್ಡಿ, ಮತ್ತು ಸರ್ಕಾರಕ್ಕೆ (ಲೆಕ್ಕ ಶೀರ್ಷಿಕೆ 0049) ಜಮೆ ಮಾಡಿದ ಮೊತ್ತ, ದಿನಾಂಕಗಳೊಂದಿಗೆ.
6. ನಿಗಮದ ಇತ್ತೀಚಿನ ಲೆಕ್ಕಪರಿಶೋಧಿತ ವಾರ್ಷಿಕ ಲೆಕ್ಕಪತ್ರಗಳ ವರ್ಷ, ಮತ್ತು ಆ ಲೆಕ್ಕಪತ್ರಗಳು ಹಾಗೂ ಅವುಗಳ ಮೇಲಿನ ಲೆಕ್ಕಪರಿಶೋಧಕರ ವರದಿಯ ಪ್ರತಿ.
"""},
    "l6": {"title": "6. ಒಂದು ಠೇವಣಿ ಖಾತೆಯ ಲೆಡ್ಜರ್ (ಉದಾಹರಣೆಗೆ, ಗಣಿ ಪುನಶ್ಚೇತನ ನಿಧಿ)",
           "to": "ಮಹಾಲೇಖಪಾಲರ (ಲೆಕ್ಕ ಮತ್ತು ಹಕ್ಕುಗಳು) ಕಚೇರಿ, ಕರ್ನಾಟಕ\nಪಾರ್ಕ್ ಹೌಸ್ ರಸ್ತೆ, ಬೆಂಗಳೂರು 560 001",
           "why": "2024-25ರಲ್ಲಿ ಗಣಿ ಪುನಶ್ಚೇತನ ನಿಧಿಯ ಖಜಾನೆ ಠೇವಣಿ ಖಾತೆಯಿಂದ ₹4,077 ಕೋಟಿ ಮತ್ತು ಎಲ್ಲ ಠೇವಣಿ ಖಾತೆಗಳಿಂದ ₹15,991 ಕೋಟಿ ಹೊರಹೋಯಿತು, ಆದರೆ ಪ್ರಕಟಿತ ಲೆಕ್ಕಗಳಲ್ಲಿ ಖಾತೆವಾರು ಹಿಂಪಡೆತಗಳಿಲ್ಲ. ಲೆಕ್ಕ ಇಡುವ ಕಚೇರಿಯ ಬಳಿ ಲೆಡ್ಜರ್ ಇದೆ.",
           "body": """ಕೋರಿರುವ ಮಾಹಿತಿ

1. ಲೆಕ್ಕ ಶೀರ್ಷಿಕೆ 8443-106 ವೈಯಕ್ತಿಕ ಠೇವಣಿಗಳ ಅಡಿ, ವ್ಯವಸ್ಥಾಪಕ ನಿರ್ದೇಶಕರು, ಕರ್ನಾಟಕ ಗಣಿ ಪರಿಸರ ಪುನಶ್ಚೇತನ ನಿಗಮ (ಕೆಎಂಇಆರ್‌ಸಿ) ಇವರ ಹೆಸರಿನಲ್ಲಿರುವ ವೈಯಕ್ತಿಕ ಠೇವಣಿ ಖಾತೆಯ 2024-25ರ ಲೆಡ್ಜರ್ ಅಥವಾ ವ್ಯವಹಾರಗಳ ವಿವರ ಪಟ್ಟಿ: ಆರಂಭಿಕ ಶಿಲ್ಕು, ಪ್ರತಿ ಜಮೆ ಮತ್ತು ಪ್ರತಿ ಹಿಂಪಡೆತ ದಿನಾಂಕ, ಮೊತ್ತ ಮತ್ತು ರಸೀದಿ ಅಥವಾ ವರ್ಗಾವಣೆ ಉಲ್ಲೇಖದೊಂದಿಗೆ, ಮತ್ತು ಅಂತಿಮ ಶಿಲ್ಕು.
2. 2024-25ಕ್ಕೆ, ಶೀರ್ಷಿಕೆ 8443-106ರ ಅಡಿಯ ಪ್ರತಿ ವೈಯಕ್ತಿಕ ಠೇವಣಿ ಖಾತೆಯ ಜಮೆ ಮತ್ತು ಹಿಂಪಡೆತಗಳ ವಿವರ, ನಿರ್ವಾಹಕರವಾರು, ಹಣಕಾಸು ಲೆಕ್ಕಗಳಿಗಾಗಿ ಸಂಕಲಿಸಿದಂತೆ (ಹಣಕಾಸು ಲೆಕ್ಕಗಳು ಒಟ್ಟು ₹15,991.01 ಕೋಟಿ ಹಿಂಪಡೆತ ತೋರಿಸುತ್ತವೆ, ಆದರೆ ವಿವರ ನೀಡುವುದಿಲ್ಲ).
3. ಕೆಎಂಇಆರ್‌ಸಿ ವೈಯಕ್ತಿಕ ಠೇವಣಿ ಖಾತೆಯ ಹೊಂದಾಣಿಕೆ ಕುರಿತು 2024-25ರಲ್ಲಿ ನಿಮ್ಮ ಕಚೇರಿ ಮತ್ತು ಖಜಾನೆ ಅಥವಾ ಕೆಎಂಇಆರ್‌ಸಿ ನಡುವಿನ ಯಾವುದೇ ಪತ್ರ ವ್ಯವಹಾರ.
"""},
}
for _l in LETTERS:
    _k = KN[_l["id"]]
    _l.update({"title_kn": _k["title"], "to_kn": _k["to"], "why_kn": _k["why"], "body_kn": _k["body"]})

css = """
:root { --bg:#f5f6f8; --surface:#fff; --fg:#161a22; --muted:#5b6474; --line:#dde1e8; --red:#c21f30; --yellow:#f2b705; --chip:#eef0f4; --focus:#1d4ed8;
  --display:"Space Grotesk","Segoe UI",system-ui,sans-serif; --body:Inter,"Segoe UI",system-ui,sans-serif; color-scheme:light }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#11141a; --surface:#1a1e27; --fg:#eceef2; --muted:#9aa3b2; --line:#2b313d; --red:#ef5261; --yellow:#f5c93a; --chip:#232835; --focus:#7aa7ff; color-scheme:dark } }
:root[data-theme="dark"] { --bg:#11141a; --surface:#1a1e27; --fg:#eceef2; --muted:#9aa3b2; --line:#2b313d; --red:#ef5261; --yellow:#f5c93a; --chip:#232835; --focus:#7aa7ff; color-scheme:dark }
* { box-sizing:border-box } html { -webkit-text-size-adjust:100% }
body { margin:0; background:var(--bg); color:var(--fg); font:15px/1.55 var(--body) }
a { color:inherit; text-decoration-color:var(--red); text-underline-offset:2px }
:focus-visible { outline:2px solid var(--focus); outline-offset:2px }
.bar { position:sticky; top:0; z-index:5; background:#11141a; color:#eceef2; padding:10px 16px; border-bottom:3px solid #f2b705; font:600 14px/1.4 var(--body) }
.bar a { color:#f5c93a; text-decoration:none }
main { max-width:780px; margin:0 auto; padding:24px 16px 64px }
.kick { font:600 12px/1.3 var(--body); letter-spacing:.08em; text-transform:uppercase; color:var(--muted) }
h1 { font:700 clamp(30px,6vw,42px)/1.05 var(--display); margin:6px 0 12px; text-wrap:balance }
h1 em { font-style:normal; color:var(--red) }
h2 { font:700 22px/1.2 var(--display); margin:36px 0 10px }
.lede { font-size:17px; max-width:62ch }
.note { color:var(--muted); font-size:14px }
ol.steps { padding-left:22px } ol.steps li { margin:0 0 10px }
.card { background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:16px; margin:16px 0 }
.card h3 { font:700 18px/1.25 var(--display); margin:0 0 6px }
.you { display:grid; gap:10px; grid-template-columns:1fr } @media (min-width:600px) { .you { grid-template-columns:1fr 2fr } }
label { font-weight:600; font-size:13px; display:block; margin-bottom:4px }
input, select, textarea { width:100%; font:15px/1.4 var(--body); color:var(--fg); background:var(--bg); border:1px solid var(--line); border-radius:8px; padding:9px 10px }
textarea.letter { font:13px/1.5 ui-monospace,Consolas,monospace; min-height:320px; resize:vertical; white-space:pre-wrap }
.row { display:flex; flex-wrap:wrap; gap:8px; margin-top:10px }
button { font:600 14px/1 var(--body); padding:10px 14px; border-radius:8px; border:1px solid var(--line); background:var(--chip); color:var(--fg); cursor:pointer }
button.primary { background:var(--red); border-color:var(--red); color:#fff }
.ok { color:var(--muted); font-size:13px; align-self:center }
.warn { border-left:4px solid var(--yellow) }
ul.plain { padding-left:18px } ul.plain li { margin-bottom:6px }
@media print { .bar, .row, .you, select { display:none } body { background:#fff; color:#000 } }
"""

css += """
.lang { float:right; background:none; border:1px solid #f5c93a; color:#f5c93a; padding:4px 10px; font:600 14px/1.2 "Noto Sans Kannada",var(--body) }
html[lang="kn"] body, html[lang="kn"] textarea.letter { font-family:"Noto Sans Kannada",var(--body) }
html[lang="kn"] textarea.letter { font-size:14px }
html[lang="kn"] .kick { letter-spacing:0; text-transform:none }
"""

js = """
const DATA = __DATA__;
const L = __LETTERS__;
const $ = id => document.getElementById(id);
let lang = 'en';
try { if (localStorage.getItem('gb-lang') === 'kn' || location.hash === '#kn') lang = 'kn' } catch (e) {}
const T = {
  en: { annex: 'Annex: officers reported in the press as searched or trapped by the Karnataka Lokayukta police (post, department, place, date of action, press report)',
        dept: dp => '[' + dp + ': head office, or the company\\'s PIO]', copied: 'Copied.', select: 'Select the text and copy it.' },
  kn: { annex: 'ಅನುಬಂಧ: ಕರ್ನಾಟಕ ಲೋಕಾಯುಕ್ತ ಪೊಲೀಸರು ಶೋಧ ನಡೆಸಿದ ಅಥವಾ ಟ್ರ್ಯಾಪ್ ಮಾಡಿದ ಎಂದು ಪತ್ರಿಕೆಗಳಲ್ಲಿ ವರದಿಯಾದ ಅಧಿಕಾರಿಗಳು (ಹುದ್ದೆ, ಇಲಾಖೆ, ಸ್ಥಳ, ಕ್ರಮದ ದಿನಾಂಕ, ಪತ್ರಿಕಾ ವರದಿ; ವಿವರಗಳು ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ)',
        dept: dp => '[' + dp + ': ಕೇಂದ್ರ ಕಚೇರಿ, ಅಥವಾ ಕಂಪನಿಯ ಸಾರ್ವಜನಿಕ ಮಾಹಿತಿ ಅಧಿಕಾರಿ]', copied: 'ನಕಲು ಮಾಡಲಾಗಿದೆ.', select: 'ಪಠ್ಯವನ್ನು ಆಯ್ಕೆಮಾಡಿ ನಕಲು ಮಾಡಿ.' } };
function annex(rows) {
  if (!rows.length) return '';
  return '\\n' + T[lang].annex + '\\n' +
    rows.map((r, i) => `${i + 1}. ${r.post}, ${r.dept}, ${r.place}; ${r.action}, ${r.date}; ${r.src}`).join('\\n') + '\\n';
}
function build(l) {
  const k = lang === 'kn';
  const name = $('nm').value.trim() || '______', addr = $('ad').value.trim().replace(/\\n+/g, ', ') || '______';
  let to = k ? l.to_kn : l.to, rows = [];
  if (l.annex === 'all') rows = DATA;
  if (l.annex === 'corp') { const cp = $('corp').value; to = cp + (k ? ', ಕೇಂದ್ರ ಕಚೇರಿ, ಬೆಂಗಳೂರು [ವಿಳಾಸ]' : ', Head Office, Bengaluru [address]'); }
  if (l.annex === 'dept') { const dp = $('dept').value; rows = DATA.filter(r => r.dept === dp); to = T[lang].dept(dp); }
  return (k ? L.head_kn : L.head).replace('{to}', to).replace('{name}', name).replace('{addr}', addr) + '\\n' + (k ? l.body_kn : l.body) + annex(rows) + (k ? L.foot_kn : L.foot);
}
function render() { L.items.forEach(l => { $(l.id).value = build(l); }); }
function setLang(x) {
  lang = x; document.documentElement.lang = x;
  try { localStorage.setItem('gb-lang', x) } catch (e) {}
  document.querySelectorAll('[data-kn]').forEach(el => {
    if (el.dataset.en === undefined) el.dataset.en = el.innerHTML;
    el.innerHTML = x === 'kn' ? el.dataset.kn : el.dataset.en;
  });
  document.title = x === 'kn' ? 'ಆರ್‌ಟಿಐ ಸಲ್ಲಿಸಿ · Gandaberunda' : 'File an RTI · Gandaberunda';
  $('lang').textContent = x === 'kn' ? 'English' : 'ಕನ್ನಡ';
  $('lang').setAttribute('lang', x === 'kn' ? 'en' : 'kn');
  render();
}
$('lang').addEventListener('click', () => setLang(lang === 'kn' ? 'en' : 'kn'));
['nm', 'ad', 'dept', 'corp'].forEach(id => $(id).addEventListener('input', render));
document.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', async () => {
  const t = $(b.dataset.copy); let ok = false;
  try { await navigator.clipboard.writeText(t.value); ok = true } catch (e) { t.select(); try { ok = document.execCommand('copy') } catch (e2) {} }
  b.parentElement.querySelector('.ok').textContent = ok ? T[lang].copied : T[lang].select;
}));
document.querySelectorAll('[data-dl]').forEach(b => b.addEventListener('click', () => {
  const t = $(b.dataset.dl), a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([t.value.replace(/\\n/g, '\\r\\n')], { type: 'text/plain;charset=utf-8' }));
  a.download = 'RTI_' + b.dataset.dl + (lang === 'kn' ? '_kn' : '') + '.txt'; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}));
setLang(lang);
"""

esc = html.escape
CORPS = ['Nijasharana Ambigara Chowdaiah Development Corporation Ltd', 'Karnataka Veerashaiva-Lingayath Development Corporation Ltd', 'Karnataka Vokkaliga Community Development Corporation Ltd', 'Karnataka State Kadugolla Development Corporation Ltd', 'Karnataka Maratha Communities Development Corporation Ltd', 'Karnataka SC/ST Nomadic Development Corporation Ltd', 'Karnataka State Safai Karmachari Development Corporation Ltd', 'Dr Babu Jagjivan Ram Leather Industries Development Corporation Ltd', 'Karnataka Bhovi Development Corporation Ltd', 'Karnataka Vishwakarma Communities Development Corporation Ltd', 'Karnataka Uppara Development Corporation Ltd', 'Karnataka Maharshi Valmiki Scheduled Tribes Development Corporation Ltd', 'Dr B R Ambedkar Development Corporation Ltd', 'D Devaraj Urs Backward Classes Development Corporation Ltd', 'Karnataka Thanda Development Corporation', 'Karnataka Adi Jambava Development Corporation']


def K(s):
    """data-kn attribute holding Kannada inner HTML."""
    return ' data-kn="' + esc(s, quote=True) + '"'


opts = "".join(f'<option>{esc(k)}</option>' for k in DEPTS)
cards = []
for l in LETTERS:
    extra = ""
    if l["annex"] == "dept":
        extra = f'<label for="dept"{K("ಇಲಾಖೆ")}>Department</label><select id="dept">{opts}</select>'
    if l["annex"] == "corp":
        extra = f'<label for="corp"{K("ನಿಗಮ")}>Corporation</label><select id="corp">' + "".join(f"<option>{esc(c)}</option>" for c in CORPS) + "</select>"
    if l["annex"] == "all":
        extra = (f'<p class="note"{K(f"ಟ್ರ್ಯಾಕರ್‌ನಲ್ಲಿ ಲೋಕಾಯುಕ್ತ ಕ್ರಮ ಕೈಗೊಂಡ ಎಲ್ಲ {len(DATA)} ಅಧಿಕಾರಿಗಳನ್ನು ಹುದ್ದೆ, ಸ್ಥಳ ಮತ್ತು ದಿನಾಂಕದೊಂದಿಗೆ ಅನುಬಂಧದಲ್ಲಿ ಪಟ್ಟಿ ಮಾಡಲಾಗಿದೆ.")}>'
                 f'The annex lists all {len(DATA)} officers the Lokayukta acted against in the tracker, by post, place and date.</p>')
    cards.append(f"""<section class="card" id="letter-{l['id']}"><h3{K(esc(l['title_kn']))}>{esc(l['title'])}</h3><p{K(esc(l['why_kn']))}>{esc(l['why'])}</p>{extra}
<textarea class="letter" id="{l['id']}" aria-label="{esc(l['title'])}" spellcheck="false"></textarea>
<div class="row"><button class="primary" data-copy="{l['id']}"{K("ಪತ್ರ ನಕಲು ಮಾಡಿ")}>Copy letter</button><button data-dl="{l['id']}"{K(".txt ಡೌನ್‌ಲೋಡ್")}>Download .txt</button><span class="ok" aria-live="polite"></span></div></section>""")

LJSON = json.dumps({"head": HEAD, "foot": FOOT, "head_kn": HEAD_KN, "foot_kn": FOOT_KN,
                    "items": [{k: l[k] for k in ("id", "to", "body", "annex", "to_kn", "body_kn")} for l in LETTERS]}, ensure_ascii=False)
asof = d(max(r['checked_on'] for r in rows if r['checked_on']))
A_TR = '<a href="reports/officials_tracker.html">After the raid</a>'
A_TR_KN = '<a href="reports/officials_tracker.html">ದಾಳಿಯ ನಂತರ</a>'
A_KIC = '<a href="https://kic.karnataka.gov.in/" rel="noopener">{}</a>'
A_FORM = f'<a href="{FORM}" rel="noopener">{{}}</a>'

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>File an RTI · Gandaberunda</title>
<meta property="og:type" content="article">
<meta property="og:title" content="File an RTI · Gandaberunda">
<meta property="og:description" content="Ready-to-file RTI letters, in English and Kannada, asking what happened after the Lokayukta raids on Karnataka officials in 2026: chargesheets, sanction to prosecute, suspensions, property returns.">
<meta property="og:url" content="https://jarvisss007.github.io/know-your-mla/rti.html">
<meta property="og:image" content="https://jarvisss007.github.io/know-your-mla/brand/gandaberunda-banner.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="description" content="Ready-to-file RTI letters, in English and Kannada, asking what happened after the Lokayukta raids on Karnataka officials in 2026: chargesheets, sanction to prosecute, suspensions, property returns.">
<link rel="icon" type="image/svg+xml" href="brand/mark.svg">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Noto+Sans+Kannada:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap">
<style>{css}</style>
</head>
<body>
<div class="bar"><button id="lang" class="lang" type="button" lang="kn">ಕನ್ನಡ</button><a href="index.html#officials"{K("← Gandaberunda · ಅಧಿಕಾರಿಗಳು")}>← Gandaberunda · Officials</a></div>
<main>
<div class="kick"{K("Gandaberunda · ಮಾಹಿತಿ ಹಕ್ಕು · ಭಾರತದ ಯಾವುದೇ ನಾಗರಿಕರಿಗಾಗಿ")}>Gandaberunda · Right to Information · for any citizen of India</div>
<h1{K("ಉತ್ತರವನ್ನು <em>ನೀವೇ</em> ಕೇಳಿ")}>Ask for the answer <em>yourself</em></h1>
<p class="lede"{K(f"ನಾವು ಹಿಂಬಾಲಿಸುತ್ತಿರುವ ವರದಿಗಳ ಪ್ರಕಾರ, 2026ರಲ್ಲಿ ಕರ್ನಾಟಕದ {len(rows)} ಅಧಿಕಾರಿಗಳ ಮೇಲೆ ದಾಳಿ, ಟ್ರ್ಯಾಪ್ ಅಥವಾ ಆರೋಪ ದಾಖಲಾಗಿದೆ. ಅವರಲ್ಲಿ {stuck} ಮಂದಿಯ ವಿಷಯದಲ್ಲಿ ಮುಂದಿನ ಯಾವುದೇ ಹಂತ ವರದಿಯಾಗಿಲ್ಲ: ದೋಷಾರೋಪಣ ಪಟ್ಟಿ ಇಲ್ಲ, ಮಂಜೂರಾತಿ ಇಲ್ಲ, ತೀರ್ಪು ಇಲ್ಲ. ಉತ್ತರ ಗೊತ್ತಿರುವ ಕಚೇರಿಗಳು ಯಾವುದೇ ನಾಗರಿಕರಿಗೆ 30 ದಿನಗಳೊಳಗೆ ಉತ್ತರಿಸಬೇಕು. ಇಲ್ಲಿ ಆರು ಪತ್ರಗಳಿವೆ: ಮುದ್ರಿಸಿ, ಸಹಿ ಮಾಡಿ, ಅಂಚೆಯಲ್ಲಿ ಕಳುಹಿಸಿ.")}>{len(rows)} Karnataka officials were raided, trapped or charged in 2026, according to the reports we track. For {stuck} of them, no later step has been reported: no chargesheet, no sanction, no verdict. The offices that know the answer must reply to any citizen within 30 days. Here are six letters, ready to print, sign and post.</p>
<p class="note"{K(f"ಪ್ರತಿ ಪ್ರಕರಣವನ್ನು {A_TR_KN} ಪುಟದಲ್ಲಿ ನೋಡಿ. ಟ್ರ್ಯಾಕರ್‌ನಂತೆಯೇ ಪತ್ರಗಳಲ್ಲಿ ಹೆಸರುಗಳಿಲ್ಲ, ಹುದ್ದೆ ಮತ್ತು ಸ್ಥಳಗಳು ಮಾತ್ರ; ಹುದ್ದೆ, ಸ್ಥಳ, ದಿನಾಂಕ ಮತ್ತು ಲಿಂಕ್ ಮಾಡಿದ ಪತ್ರಿಕಾ ವರದಿಯಿಂದ ಮಾಹಿತಿ ಅಧಿಕಾರಿ ಪ್ರತಿಯೊಬ್ಬ ಅಧಿಕಾರಿಯನ್ನು ಗುರುತಿಸಬಹುದು. ಪ್ರತಿ ಪತ್ರ ಇಂಗ್ಲಿಷ್ ಮತ್ತು ಕನ್ನಡದಲ್ಲಿದೆ; ಮೇಲಿನ ಬಟನ್‌ನಿಂದ ಭಾಷೆ ಬದಲಿಸಿ.")}>See every case on {A_TR}. Letters carry posts and places, not names, the same as the tracker; the PIO can identify each officer from the post, place, date and the linked press report. Every letter is in English and Kannada; switch with the button at the top.</p>

<h2{K("ನಿಮ್ಮ ವಿವರಗಳು")}>Your details</h2>
<div class="card you">
<div><label for="nm"{K("ನಿಮ್ಮ ಹೆಸರು")}>Your name</label><input id="nm" autocomplete="name"></div>
<div><label for="ad"{K("ಉತ್ತರಕ್ಕಾಗಿ ಭಾರತದಲ್ಲಿನ ಅಂಚೆ ವಿಳಾಸ")}>Postal address in India for the reply</label><textarea id="ad" rows="2" autocomplete="street-address"></textarea></div>
</div>
<p class="note"{K("ಇವು ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲೇ ಉಳಿಯುತ್ತವೆ. ನೀವು ಬರೆದದ್ದು ಎಲ್ಲಿಗೂ ಕಳುಹಿಸಲಾಗುವುದಿಲ್ಲ ಅಥವಾ ಉಳಿಸಲಾಗುವುದಿಲ್ಲ; ಕೆಳಗಿನ ಪತ್ರಗಳನ್ನು ತುಂಬಲು ಮಾತ್ರ ಬಳಕೆಯಾಗುತ್ತವೆ.")}>These stay in your browser. Nothing you type is sent or saved anywhere; they only fill the letters below.</p>

<h2{K("ಪತ್ರಗಳು")}>The letters</h2>
{''.join(cards)}

<h2{K("ಸಲ್ಲಿಸುವುದು ಹೇಗೆ")}>How to file</h2>
<ol class="steps">
<li{K("<b>ತುಂಬಿ, ಸಹಿ ಮಾಡಿ.</b> ಪತ್ರವನ್ನು ನಕಲು ಮಾಡಿ ಅಥವಾ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ, ಮುದ್ರಿಸಿ, ಖಾಲಿ ಜಾಗಗಳನ್ನು (ಅಂಚೆ ಆದೇಶ ಸಂಖ್ಯೆ, ಸ್ಥಳ, ದಿನಾಂಕ) ತುಂಬಿ ಸಹಿ ಮಾಡಿ. ಪತ್ರ 3ಕ್ಕೆ, ಇಲಾಖೆಯ ವೆಬ್‌ಸೈಟ್‌ನಿಂದ ಅದರ ಕೇಂದ್ರ ಕಚೇರಿ ವಿಳಾಸ ಸೇರಿಸಿ.")}><b>Fill and sign.</b> Copy or download a letter, print it, fill the blanks (postal order number, place, date) and sign. For letter 3, add the department's head-office address from its website.</li>
<li{K("<b>ರೂ. 10 ಪಾವತಿಸಿ.</b> ಕಚೇರಿಯ ಆರ್‌ಟಿಐ ಪುಟದಲ್ಲಿ ಹೆಸರಿಸಿರುವ ಲೆಕ್ಕಾಧಿಕಾರಿಯ ಹೆಸರಿಗೆ ರೂ. 10ರ ಭಾರತೀಯ ಅಂಚೆ ಆದೇಶ (ಅಥವಾ ಡಿಮ್ಯಾಂಡ್ ಡ್ರಾಫ್ಟ್) ಲಗತ್ತಿಸಿ. ಬಡತನ ರೇಖೆಗಿಂತ ಕೆಳಗಿರುವ ಅರ್ಜಿದಾರರು ಅದರ ಬದಲು ಬಿಪಿಎಲ್ ಕಾರ್ಡ್‌ನ ಪ್ರತಿ ಲಗತ್ತಿಸಬೇಕು. ಪ್ರತಿಗಳ ಶುಲ್ಕ ಪುಟಕ್ಕೆ ಕೆಲವು ರೂಪಾಯಿಗಳು; ಮಾರ್ಗದರ್ಶಿಗಳಲ್ಲಿ ವ್ಯತ್ಯಾಸವಿರುವುದರಿಂದ ಕಚೇರಿಯ ಆರ್‌ಟಿಐ ಪುಟ ನೋಡಿ.")}><b>Pay Rs 10.</b> Attach an Indian Postal Order (or demand draft) for Rs 10, payable to the office's accounting officer as named on its RTI page. Applicants below the poverty line attach a copy of their BPL card instead. Copying charges are a few rupees a page; check the office's RTI page, since guides differ.</li>
<li{K("<b>ಅಂಚೆಯಲ್ಲಿ ಕಳುಹಿಸಿ</b>: ಸ್ಪೀಡ್ ಪೋಸ್ಟ್ ಅಥವಾ ಸ್ವೀಕೃತಿಯೊಂದಿಗೆ ನೋಂದಾಯಿತ ಅಂಚೆ. ಪತ್ರದ ಪ್ರತಿ, ಅಂಚೆ ರಸೀದಿ ಮತ್ತು ಅಂಚೆ ಆದೇಶದ ಕೌಂಟರ್‌ಫಾಯಿಲ್ ಇಟ್ಟುಕೊಳ್ಳಿ. ಕೆಲವು ಇಲಾಖೆಗಳು ಆನ್‌ಲೈನ್ ಆರ್‌ಟಿಐ ಸಹ ಸ್ವೀಕರಿಸುತ್ತವೆ; ಇಲಾಖೆಯ ವೆಬ್‌ಸೈಟ್ ಅಥವಾ " + A_KIC.format("ಕರ್ನಾಟಕ ಮಾಹಿತಿ ಆಯೋಗ") + " ನೋಡಿ.")}><b>Post it</b> by Speed Post or registered post with acknowledgement. Keep a copy, the postal receipt and the postal-order counterfoil. Some departments also accept online RTI; check the department's site or the {A_KIC.format("Karnataka Information Commission")}.</li>
<li{K("<b>30 ದಿನ ಕಾಯಿರಿ.</b> ಅರ್ಜಿ ತಲುಪಿದ 30 ದಿನಗಳೊಳಗೆ ಉತ್ತರ ಬರಬೇಕು. ನಿಮ್ಮ ಪತ್ರವನ್ನು ಬೇರೆ ಕಚೇರಿಗೆ ವರ್ಗಾಯಿಸಿದರೆ, ಆ ಕಚೇರಿಗೆ ತನ್ನದೇ 30 ದಿನಗಳಿರುತ್ತವೆ.")}><b>Wait 30 days.</b> The reply is due within 30 days of receipt. If your letter is sent on to another office, that office has its own 30 days.</li>
<li{K("<b>ಉತ್ತರ ಬರದಿದ್ದರೆ ಅಥವಾ ನಿರಾಕರಿಸಿದರೆ?</b> 30 ದಿನಗಳೊಳಗೆ ಪ್ರಥಮ ಮೇಲ್ಮನವಿ ಪ್ರಾಧಿಕಾರಕ್ಕೆ (ಸಾಮಾನ್ಯವಾಗಿ ಉತ್ತರದಲ್ಲಿ ಅಥವಾ ಕಚೇರಿಯ ಆರ್‌ಟಿಐ ಪುಟದಲ್ಲಿ ಹೆಸರಿಸಲಾಗಿರುತ್ತದೆ) ಮೊದಲ ಮೇಲ್ಮನವಿ ಸಲ್ಲಿಸಿ. ಎರಡನೇ ಮೇಲ್ಮನವಿ 90 ದಿನಗಳೊಳಗೆ ಕರ್ನಾಟಕ ಮಾಹಿತಿ ಆಯೋಗಕ್ಕೆ.")}><b>No reply, or refused?</b> File a first appeal within 30 days to the First Appellate Authority (usually named in the reply or on the office's RTI page). A second appeal goes to the Karnataka Information Commission within 90 days.</li>
<li{K("<b>ಉತ್ತರವನ್ನು ನಮಗೆ ತಿಳಿಸಿ.</b> " + A_FORM.format("ನಿಮಗೆ ಬಂದ ಉತ್ತರವನ್ನು ಕಳುಹಿಸಿ") + "; ಅದನ್ನು ಹುದ್ದೆ ಮತ್ತು ಹಂತದೊಂದಿಗೆ ಟ್ರ್ಯಾಕರ್‌ಗೆ ಸೇರಿಸುತ್ತೇವೆ, ನಿಮ್ಮ ಹೆಸರನ್ನು ಎಂದಿಗೂ ಅಲ್ಲ.")}><b>Tell us the answer.</b> {A_FORM.format("Send us what you received")} and we will add it to the tracker, with the post and the step, never your name.</li>
</ol>

<section class="card warn">
<h3{K("ಕಚೇರಿ ನಿರಾಕರಿಸಿದರೆ")}>If the office refuses</h3>
<ul class="plain">
<li{K("<b>'ತನಿಖೆ ನಡೆಯುತ್ತಿದೆ' (ಸೆಕ್ಷನ್ 8(1)(ಎಚ್)).</b> ಉತ್ತರ ನೀಡುವುದರಿಂದ ತನಿಖೆಗೆ ಹೇಗೆ ಅಡ್ಡಿಯಾಗುತ್ತದೆ ಎಂದು ಕಚೇರಿ ವಿವರಿಸಬೇಕು; ಸೆಕ್ಷನ್ ಉಲ್ಲೇಖಿಸುವುದಷ್ಟೇ ಸಾಲದು. ದೋಷಾರೋಪಣ ಪಟ್ಟಿ ಅಥವಾ ಮಂಜೂರಾತಿ ಕೋರಿಕೆಯ ದಿನಾಂಕಗಳು ಯಾವುದೇ ಸಾಕ್ಷ್ಯವನ್ನು ಬಹಿರಂಗಪಡಿಸುವುದಿಲ್ಲ.")}><b>"Ongoing investigation" (Section 8(1)(h)).</b> The office must explain how answering would hamper the investigation; quoting the section is not enough. Dates of a chargesheet or a sanction request reveal no evidence.</li>
<li{K("<b>'ವೈಯಕ್ತಿಕ ಮಾಹಿತಿ' (ಸೆಕ್ಷನ್ 8(1)(ಜೆ)).</b> ದಾಳಿಗಳನ್ನು ಲೋಕಾಯುಕ್ತವೇ ಪ್ರಕಟಿಸಿದೆ ಮತ್ತು ಪತ್ರಿಕೆಗಳಲ್ಲಿ ವರದಿಯಾಗಿದೆ. ನಿರಾಕರಿಸುವ ಬದಲು ಹೆಸರುಗಳನ್ನು ತೆಗೆದು ಮಾಹಿತಿ ನೀಡುವಂತೆ ಕೇಳಿ (ಸೆಕ್ಷನ್ 10). ಪತ್ರ 1ರ ಭಾಗ 'ಎ' ಒಟ್ಟು ಸಂಖ್ಯೆಗಳನ್ನು ಮಾತ್ರ ಕೇಳುತ್ತದೆ.")}><b>"Personal information" (Section 8(1)(j)).</b> The raids were announced by the Lokayukta and reported in the press. Ask for the information with names removed rather than refused (Section 10). Part A of letter 1 asks only for totals.</li>
<li{K("<b>'ಆರ್‌ಟಿಐನಿಂದ ವಿನಾಯಿತಿ' (ಸೆಕ್ಷನ್ 24).</b> ಮಧ್ಯಪ್ರದೇಶದ ಲೋಕಾಯುಕ್ತ ಪೊಲೀಸ್ ವಿನಾಯಿತಿ ನೀಡಬಹುದಾದ ಗುಪ್ತಚರ ಅಥವಾ ಭದ್ರತಾ ಸಂಸ್ಥೆಯಲ್ಲ ಎಂದು 2026ರಲ್ಲಿ ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ತೀರ್ಪು ನೀಡಿದೆ. ಕಚೇರಿ ವಿನಾಯಿತಿ ಅಧಿಸೂಚನೆಯನ್ನು ಉಲ್ಲೇಖಿಸಿದರೆ, ಅದರ ಪ್ರತಿಯನ್ನು ಕೇಳಿ.")}><b>"Exempt from RTI" (Section 24).</b> In 2026 the Supreme Court held that Madhya Pradesh's Lokayukta police is not an intelligence or security organisation that can be exempted. If an office cites an exemption notification, ask for a copy.</li>
</ul>
</section>

<h2{K("ದಯವಿಟ್ಟು")}>Please</h2>
<ul class="plain">
<li{K("ಅಭಿಪ್ರಾಯಗಳಲ್ಲ, ದಾಖಲೆಗಳನ್ನು ಕೇಳಿ, ಮತ್ತು ಪ್ರಶ್ನೆಗಳಿಗೆ ಸೀಮಿತವಾಗಿರಿ. ಚಿಕ್ಕ, ನಿರ್ದಿಷ್ಟ ಪತ್ರಕ್ಕೆ ಉತ್ತಮ ಉತ್ತರ ಸಿಗುತ್ತದೆ.")}>Ask for records, not opinions, and keep to the questions. A short, specific letter gets a better answer.</li>
<li{K("ಪತ್ರದಲ್ಲಿ ಯಾರ ಖಾಸಗಿ ವಿವರಗಳನ್ನೂ ಸೇರಿಸಬೇಡಿ, ಯಾರ ಮೇಲೂ ಆರೋಪ ಮಾಡಬೇಡಿ. ದಾಳಿ ಎಂದರೆ ಆರೋಪ, ತಪ್ಪು ಸಾಬೀತಾಗಿದೆ ಎಂದಲ್ಲ.")}>Do not add anyone's private details, and do not accuse anyone in the letter. A raid is an allegation, not a finding of guilt.</li>
<li{K("ಶುಲ್ಕ ಮತ್ತು ಸಲ್ಲಿಕೆಯ ವಿಧಾನವನ್ನು ನವೆಂಬರ್ 2026ರ ಆರ್‌ಟಿಐ ಮಾರ್ಗದರ್ಶಿಗಳು ಮತ್ತು ಕಚೇರಿಗಳ ಪುಟಗಳ ಪ್ರಕಾರ ನೀಡಲಾಗಿದೆ; ಕಳುಹಿಸುವ ಮೊದಲು ಪರಿಶೀಲಿಸಿ.")}>The fee and filing route are as described by RTI guides and offices' own pages as of Nov 2026; check them before you post.</li>
<li{K("ಕನ್ನಡ ಅನುವಾದವನ್ನು ಇನ್ನೂ ಕನ್ನಡ ಭಾಷಾ ತಜ್ಞರು ಪರಿಶೀಲಿಸಬೇಕಿದೆ. ಸಂದೇಹವಿದ್ದರೆ ಇಂಗ್ಲಿಷ್ ಪತ್ರ ಬಳಸಿ; ಎರಡನ್ನೂ ಸ್ವೀಕರಿಸಲಾಗುತ್ತದೆ.")}>The Kannada translation has not yet been reviewed by a native editor. If in doubt, use the English letter; both are accepted.</li>
</ul>
<p class="note"{K(f"ಮೂಲಗಳು: ಮಾಹಿತಿ ಹಕ್ಕು ಅಧಿನಿಯಮ, 2005 (ಸೆಕ್ಷನ್ 6, 7, 8, 10, 19, 24); ಕರ್ನಾಟಕ ಮಾಹಿತಿ ಹಕ್ಕು ನಿಯಮಗಳು (ಶುಲ್ಕ); Special Police Establishment v. Kamta Prasad Mishra, 2026 INSC 644; ಪ್ರಕರಣಗಳ ಪಟ್ಟಿ {A_TR_KN} ಪುಟದಿಂದ, ಅಲ್ಲಿ ಲಿಂಕ್ ಮಾಡಿದ ಪತ್ರಿಕಾ ವರದಿಗಳ ಆಧಾರದ ಮೇಲೆ. ಟ್ರ್ಯಾಕರ್ ಅನ್ನು {asof} ರಂದು ಓದಿದಂತೆ.")}>Sources: Right to Information Act, 2005 (Sections 6, 7, 8, 10, 19, 24); Karnataka RTI Rules (fee); Special Police Establishment v. Kamta Prasad Mishra, 2026 INSC 644; case list from {A_TR}, built from press reports linked there. Page built from the tracker as read on {asof}.</p>
</main>
<script>{js.replace('__DATA__', json.dumps(DATA, ensure_ascii=False)).replace('__LETTERS__', LJSON)}</script>
<script data-goatcounter="https://gandaberunda.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
"""
(ROOT / "rti.html").write_text(page, encoding="utf-8", newline="\n")
print("rti.html", len(page) // 1024, "KB;", len(DATA), "Lokayukta rows;", len(DEPTS), "departments; stuck", stuck, "of", len(rows))
