# Kannada names: sources (data/names_kn.csv)

Built 2026-11-24. One row per entry of `const D` in `index.html`, in D's order (224 rows).

## Result

| status | rows |
|---|---|
| official | 224 |
| unchecked | 0 |
| missing | 0 |

Every row's `constituency_kn`, `name_kn` and `ac_no` come from one official page:

**Karnataka Legislative Assembly, Sixteenth Assembly member list**
https://kla.kar.nic.in/assembly/member/16assemblymemberslist.htm
(fetched 2026-11-24; SHA-256 of the HTML as fetched:
`fe3ebee3be4b9b5f42da8f9b7799b26b61c483001a6fd80ca78f19ebe83d38f8`).
The page lists each seat as "English (AC no) | Kannada" and each member as
"ENGLISH NAME | Kannada name", with by-election winners added as extra rows
marked "[By Ele: from dd/mm/yyyy]" and earlier members marked
"[Remarks: Resigned/Died on ...]".

Kannada strings are copied exactly as the page gives them, including the
zero-width non-joiner (U+200C) the page uses after a virama (e.g. `ಡಿ ಸುಧಾಕರ್‌`).
Nothing was transliterated by hand.

## Lookup log

| # | URL | Result |
|---|---|---|
| 1 | https://kla.kar.nic.in/assembly/member/membersList.htm | HTTP 404 (guessed URL) |
| 2 | https://kla.kar.nic.in/ | 200, home page; used to find links |
| 3 | https://ceo.karnataka.gov.in/ | Connection timed out (not reachable from this machine) |
| 4 | https://results.eci.gov.in/ | 200, a redirect stub only; not needed further |
| 5 | https://kla.kar.nic.in/assembly/assembly.htm | 200, link index |
| 6 | https://kla.kar.nic.in/assembly/election/election.htm | 200, only Council/Rajya Sabha/President election pages |
| 7 | https://kla.kar.nic.in/assembly/member/members.htm | 200, menu; points to 16assemblymemberslist.htm |
| 8 | https://kla.kar.nic.in/assembly/member/16assemblymemberslist.htm | 200, **used**: all 224 seats with English + Kannada seat and member names |
| 9 | https://kla.kar.nic.in/assembly/member/membersdownload.htm | 200, old member downloads; not relevant |

Not tried, because #8 covered every row: CEO Karnataka Form-20/21, ECI
affidavit portal, gazette notifications, Kannada Wikipedia, newspapers.
The same page also links an official Kannada address book PDF
(`https://kla.kar.nic.in/assembly/member/16membersaddress_kan.pdf`), not fetched.

## How rows were matched

- D's `c` (minus a trailing " (SC)"/" (ST)") was matched to the KLA English
  seat name. 35 seats are spelt differently in D (e.g. Gauribidanur /
  Gowribidanur, Kundapur / "Coonadapur/Kundapura", Sorab / Soraba); each was
  matched by closest spelling and checked by hand. Every ac_no 1-224 is used
  exactly once.
- Where a seat has more than one KLA row (by-elections, Dharwad), the row
  whose English name matches D's `n` was used.

## Things a reader should know

1. **SC/ST suffixes are not on the KLA page.** `constituency_kn` therefore has
   no "(ಪ.ಜಾ)"/"(ಪ.ಪಂ)" suffix, even where `constituency_en` has "(SC)"/"(ST)".
   None was added by hand. If the site needs them, take them from an official
   Kannada delimitation or CEO list (not reached this time).
2. **By-elections** (all on the KLA page, so the current MLA's Kannada name is official):
   Shiggaon 83 Pathan Yasir Ahmed Khan, Sandur 95 E Annapoorna, Channapatna 185
   C P Yogeeshwara (all from 09/12/2024); Bagalkot 24 Umesh Hullappa Meti and
   Davanagere South 107 Samarth Shamanuru Mallikarjuna (from 04/05/2026).
3. **Hiriyur (100):** the KLA page marks D. Sudhakar "Died on 10/05/2026"
   and lists no successor. D still lists him; the row keeps his official
   Kannada name. The site may need to show this seat as vacant.
4. **Dharwad (71):** the KLA page lists Vinay Kulkarni twice; one row says
   "Disqualified from 15/04/2026" (notification KLAS/LEG/46/N.CCH/2026 dated
   02/05/2026, after a Sessions Court judgement). D still lists him. Check his
   status before the site calls him the sitting MLA.
5. **Names that differ from D's English** (official Kannada follows the KLA
   English, not D's): Sakaleshpur, D "S Manjunatha", KLA "CEMENT MANJU" /
   `ಸಿಮೆಂಟ್‌ ಮಂಜು`; Nagamangala, KLA adds the alias "ಅಲಿಯಾಸ್‌ ಸ್ವಾಮಿಗೌಡ";
   Mangalore, D "U.T. Khader Fareed", KLA `ಯು ಟಿ ಖಾದರ್‌`. Other differences
   are spelling only (e.g. Bhojaraj / BHOJ RAJ).
