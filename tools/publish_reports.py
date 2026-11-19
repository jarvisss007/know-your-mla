"""Copy research pages to the public site under reports/, as TEST VERSIONS.

    py tools/publish_reports.py

The research/ files stay the working drafts. This script makes the public copies:
adds a full <head>, a "back to Gandaberunda" bar, swaps the DRAFT badge for a
TEST VERSION badge, and copies the images. Re-run it after editing a draft.
"""
import pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "reports"

BADGES = {
    "DRAFT · NOT PUBLISHED": "TEST VERSION · UNDER REVIEW",
    "DRAFT · NOT FOR PUBLICATION": "TEST VERSION · UNDER REVIEW",
    "DRAFT · PILOT · NOT FOR PUBLICATION": "TEST VERSION · UNDER REVIEW",
    "ಕರಡು · ಪ್ರಕಟಿಸಿಲ್ಲ": "ಪರೀಕ್ಷಾ ಆವೃತ್ತಿ · ಪರಿಶೀಲನೆಯಲ್ಲಿದೆ",
    "ಕರಡು · ಪ್ರಕಟಣೆಗೆ ಅಲ್ಲ": "ಪರೀಕ್ಷಾ ಆವೃತ್ತಿ · ಪರಿಶೀಲನೆಯಲ್ಲಿದೆ",
}

MAHADEVAPURA_NOTE = ('<div style="background:var(--surface);border:1px solid var(--yellow);border-left:4px solid var(--yellow);'
                     'border-radius:10px;padding:12px 16px;max-width:75ch"><strong>Check in progress.</strong> In Kanakapura, a check of '
                     'every clean date showed that most of the change in green cover was season and rainfall, not land use. The same '
                     'check is being run here. Until it is done, treat the green-cover figure below as unconfirmed.</div>\n  ')

# (source, destination, title, description, alternate-language page or None, extra files, prepend-to-lede)
PAGES = [
    ("research/paper_vs_ground/DRAFT_paper_vs_ground.html", "paper_vs_ground.html", "Paper vs Ground · Gandaberunda",
     "What Karnataka's audits and official replies say was sanctioned or recovered, beside what the same records say happened.",
     ("paper_vs_ground_kn.html", "ಕನ್ನಡ"), [], None),
    ("research/paper_vs_ground/DRAFT_paper_vs_ground_kn.html", "paper_vs_ground_kn.html", "ಕಾಗದದಲ್ಲಿ ಮತ್ತು ನೆಲದಲ್ಲಿ · Gandaberunda",
     "Paper vs Ground in Kannada (test version).", ("paper_vs_ground.html", "English"), [], None),
    ("research/farmer_schemes/DRAFT_delivery_ledger.html", "farm_money_ledger.html", "Farm Money Ledger · Gandaberunda",
     "Nine places where Karnataka's farm money can be followed from the announcement to the farmer.",
     ("farm_money_ledger_kn.html", "ಕನ್ನಡ"), [], None),
    ("research/farmer_schemes/DRAFT_delivery_ledger_kn.html", "farm_money_ledger_kn.html", "ಕೃಷಿ ಹಣದ ಲೆಕ್ಕಪುಸ್ತಕ · Gandaberunda",
     "Farm money ledger in Kannada (test version).", ("farm_money_ledger.html", "English"), [], None),
    ("research/satellite/kanakapura/DRAFT_kanakapura_scorecard.html", "satellite/kanakapura/index.html", "Kanakapura From Space · Gandaberunda",
     "Sentinel-2 land-cover comparison of Kanakapura constituency, February 2019 and February 2026.", None,
     ["truecolor_2019_2026.png", "change_map_2019_2026.png", "clusters.png", "field_checks.csv"], None),
    ("research/satellite/holenarasipur/DRAFT_holenarasipur_scorecard.html", "satellite/holenarasipur/index.html", "Holenarasipur From Space · Gandaberunda",
     "Sentinel-2 land-cover comparison of Holenarasipur constituency, February 2019 and February 2026.", None,
     ["truecolor_2019_2026.png", "change_map_2019_2026.png", "clusters.png", "field_checks.csv"], None),
    ("research/satellite/DRAFT_mahadevapura_scorecard.html", "satellite/mahadevapura/index.html", "Mahadevapura From Space · Gandaberunda",
     "Sentinel-2 land-cover comparison of Mahadevapura constituency, February 2019 and February 2026.", None,
     ["truecolor_2019_2026.png", "change_map_2019_2026.png"], None),
    ("research/follow_the_money/DRAFT_follow_the_money.html", "follow_the_money.html", "Follow the Rupee · Gandaberunda",
     "How Karnataka's public money travels from the budget to the recipient, where the state's auditor found it parked or unaccounted for, and the record that traces it back.",
     ("follow_the_money_kn.html", "ಕನ್ನಡ"), [], None),
    ("research/follow_the_money/DRAFT_follow_the_money_kn.html", "follow_the_money_kn.html", "ರೂಪಾಯಿಯನ್ನು ಹಿಂಬಾಲಿಸಿ · Gandaberunda",
     "Follow the rupee in Kannada (test version).", ("follow_the_money.html", "English"), [], None),
    ("research/rural_jobs/DRAFT_photo_check_ranking.html", "photo_check.html", "Where the Work Photos Are Taken · Gandaberunda",
     "All 236 Karnataka blocks ranked on where 8.24 lakh MGNREGA completion photos were taken, from the government's own records.", None,
     ["photo_check_blocks_2024-25.csv"], None),
    ("research/rural_jobs/findings/DRAFT_tank_findings.html", "tank_findings.html", "One Tank, Many Works · Gandaberunda",
     "Two village tanks in Koppal and Ballari carry 246 MGNREGA works from 18 panchayats and Rs 13.05 crore, all photographed at the same spot: the records, the satellite images and the open questions.", None,
     ["kampli_photos.jpg", "kampli_satellite.jpg", "jeerala_photos.jpg", "one_tank_three_works.jpg", "one_pit_two_works.jpg", "kampli_tank_152_works.csv", "jeerala_tank_works.csv"], None),
    ("research/rural_jobs/findings/DRAFT_letters.html", "mgnrega_letters.html", "The Paper Trail · Gandaberunda",
     "The full text of the RTI applications and Ombudsperson requests behind 'One tank, many works', for anyone to read or file again.", None, [], None),
    ("research/officials_tracker/DRAFT_officials_tracker.html", "officials_tracker.html", "After the Raid · Gandaberunda",
     "Karnataka officials raided, trapped or charged in 2026, followed from the first day towards a verdict. Posts, not names.",
     ("officials_tracker_kn.html", "ಕನ್ನಡ"), [], None),
    ("research/officials_tracker/DRAFT_officials_tracker_kn.html", "officials_tracker_kn.html", "ದಾಳಿಯ ನಂತರ · Gandaberunda",
     "After the raid in Kannada (test version).", ("officials_tracker.html", "English"), [], None),
]


def build(src, dst, title, desc, alt, extra, note):
    s = ROOT / src
    body = s.read_text(encoding="utf-8")
    # drop the artifact-style title line; the page gets a real head below
    lines = body.split("\n")
    # also drop a standalone page's own doctype/html/meta/title lines (the officials tracker is one)
    standalone = lines[0].lstrip().lower().startswith("<!doctype")
    while lines and lines[0].lstrip().lower().startswith(("<!doctype", "<html", "<meta charset", '<meta name="viewport"', "<title>")):
        lines = lines[1:]
    while standalone and lines and lines[-1].strip().lower() in ("", "</html>", "</body>"):
        lines = lines[:-1]
    body = "\n".join(lines)
    for a, b in BADGES.items():
        body = body.replace(f'class="draft">{a}<', f'class="draft">{b}<')
    if note:
        i = body.index('<p class="lede">')
        body = body[:i] + note + body[i:]
    d = OUT / dst
    depth = len(pathlib.Path("reports", dst).parts) - 1
    up = "../" * depth
    alt_link = f' · <a href="{alt[0]}" style="color:#eceef2">{alt[1]}</a>' if alt else ""
    bar = (f'<div style="position:sticky;top:0;z-index:20;background:#11141a;color:#eceef2;font:600 14px/1.4 Inter,system-ui,sans-serif;'
           f'padding:10px max(16px,env(safe-area-inset-left,0px));display:flex;gap:8px 16px;flex-wrap:wrap;align-items:center;'
           f'border-bottom:3px solid #f2b705">'
           f'<a href="{up}index.html#research" style="color:#f5c93a;text-decoration:none">← Gandaberunda · Research</a>'
           f'<span style="color:#9aa3b2;font-weight:400">Test version: still being checked{alt_link}</span></div>\n')
    head = ("<!doctype html>\n<html lang=\"" + ("kn" if dst.endswith("_kn.html") else "en") + "\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            f"<title>{title}</title>\n<meta name=\"description\" content=\"{desc}\">\n"
            f"<link rel=\"icon\" type=\"image/svg+xml\" href=\"{up}brand/mark.svg\">\n"
            "<style>:root{padding-top:env(safe-area-inset-top,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n")
    # split head-ish material (meta/link/style at the top of the body) from content: keep it all in <head> up to the first <div
    i = body.index("<div")
    page = head + body[:i] + "</head>\n<body>\n" + bar + body[i:] + "\n</body>\n</html>\n"
    d.parent.mkdir(parents=True, exist_ok=True)
    d.write_text(page, encoding="utf-8", newline="\n")
    for x in extra:
        shutil.copy2(s.parent / x, d.parent / x)
    print("ok", d.relative_to(ROOT), len(page) // 1024, "KB", "+", len(extra), "files")


for p in PAGES:
    build(*p)
