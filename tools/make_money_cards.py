"""Render square (1080x1080) cards for findings already published on the site and on X.

Every figure here is on the linked page with its source, and was checked there first:
courts (NCRB Crime in India 2023 Vol. II Table 8C.4), corporations (CAG SFAR 2024-25 Appendix 2.16),
mining (CAG Report 7 of 2025, Chart 3.2 and para 4.6.1), parking (CAG SFAR 2024-25 para 3.5.1, 2.7.1.2A).

    py tools/make_money_cards.py
writes cards/money/<id>-kn.png and <id>-en.png using headless Chrome. Posting them is the owner's call.
"""
import html, pathlib, subprocess, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "cards" / "money"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = "jarvisss007.github.io/know-your-mla/"

# id, {lang: (kicker, big number, headline, three lines, source, page)}
CARDS = [
    ("courts",
     {"en": ("Corruption cases, Karnataka, 2023", "35 of 120", "corruption trials ended in conviction", ["Conviction rate 29%; all India 46%", "1,529 cases still waiting for trial at year end", "72 officials on our 2026 tracker: no verdict yet"], "Source: NCRB, Crime in India 2023, Vol. II, Table 8C.4", "reports/officials_tracker.html"),
      "kn": ("ಭ್ರಷ್ಟಾಚಾರ ಪ್ರಕರಣಗಳು, ಕರ್ನಾಟಕ, 2023", "120ರಲ್ಲಿ 35", "ಭ್ರಷ್ಟಾಚಾರ ವಿಚಾರಣೆಗಳಲ್ಲಿ ಮಾತ್ರ ಶಿಕ್ಷೆ", ["ಶಿಕ್ಷೆಯ ಪ್ರಮಾಣ 29%; ಭಾರತ 46%", "ವರ್ಷಾಂತ್ಯದಲ್ಲಿ 1,529 ಪ್ರಕರಣಗಳು ವಿಚಾರಣೆಗೆ ಬಾಕಿ", "2026ರ ನಮ್ಮ ಪಟ್ಟಿಯ 72 ಅಧಿಕಾರಿಗಳು: ಇನ್ನೂ ತೀರ್ಪಿಲ್ಲ"], "ಮೂಲ: ಎನ್‌ಸಿಆರ್‌ಬಿ, ಕ್ರೈಮ್ ಇನ್ ಇಂಡಿಯಾ 2023, ಕೋಷ್ಟಕ 8C.4", "reports/officials_tracker_kn.html")}),
    ("corporations",
     {"en": ("State auditor (CAG), 31 March 2025", "₹410 crore", "in 32 bank accounts that ten corporations were told to close", ["The closing order was issued in 2023", "Grants the books show as spent can sit in such accounts", "The auditor's tables, traced on our page"], "Source: CAG State Finances Audit 2024-25, Appendix 2.16", "reports/follow_the_money.html#corporations"),
      "kn": ("ಸಿಎಜಿ ಲೆಕ್ಕಪರಿಶೋಧನೆ, 31 ಮಾರ್ಚ್ 2025", "₹410 ಕೋಟಿ", "ಮುಚ್ಚಲು ಆದೇಶವಿದ್ದ 32 ಬ್ಯಾಂಕ್ ಖಾತೆಗಳಲ್ಲಿ, ಹತ್ತು ನಿಗಮಗಳು", ["ಮುಚ್ಚುವ ಆದೇಶ 2023ರಲ್ಲಿ ಬಂದಿತ್ತು", "ಲೆಕ್ಕದಲ್ಲಿ ಖರ್ಚಾಗಿದೆ ಎಂದ ಅನುದಾನ ಇಂತಹ ಖಾತೆಗಳಲ್ಲಿ ಉಳಿಯಬಹುದು", "ಸಿಎಜಿ ಕೋಷ್ಟಕಗಳು ನಮ್ಮ ಪುಟದಲ್ಲಿ"], "ಮೂಲ: ಸಿಎಜಿ ರಾಜ್ಯ ಹಣಕಾಸು ಲೆಕ್ಕಪರಿಶೋಧನೆ 2024-25, ಅನುಬಂಧ 2.16", "reports/follow_the_money_kn.html#corporations")}),
    ("mining",
     {"en": ("District mineral funds, to March 2023", "₹4,004 crore", "collected; ₹1,826 crore spent", ["2,190 projects never started", "The CM-led steering committee did not meet once, 2018 to June 2023", "Money meant for mining-hit villages"], "Source: CAG Report 7 of 2025", "reports/follow_the_money.html#mining"),
      "kn": ("ಜಿಲ್ಲಾ ಖನಿಜ ಪ್ರತಿಷ್ಠಾನಗಳು, ಮಾರ್ಚ್ 2023ರವರೆಗೆ", "₹4,004 ಕೋಟಿ", "ಸಂಗ್ರಹ; ಖರ್ಚು ₹1,826 ಕೋಟಿ", ["2,190 ಯೋಜನೆಗಳು ಆರಂಭವೇ ಆಗಲಿಲ್ಲ", "ಮುಖ್ಯಮಂತ್ರಿ ಅಧ್ಯಕ್ಷತೆಯ ಸಮಿತಿ 2018ರಿಂದ ಜೂನ್ 2023ರವರೆಗೆ ಒಮ್ಮೆಯೂ ಸಭೆ ಸೇರಲಿಲ್ಲ", "ಗಣಿಬಾಧಿತ ಹಳ್ಳಿಗಳಿಗಾಗಿ ಇದ್ದ ಹಣ"], "ಮೂಲ: ಸಿಎಜಿ ವರದಿ 7/2025", "reports/follow_the_money_kn.html#mining")}),
    ("parking",
     {"en": ("Karnataka, March 2025 alone", "₹6,026 crore", "moved into deposit accounts at year end", ["The auditor's phrase: “mere parking of funds to avoid lapse of grants”", "Money voted for one year, kept for later", "Seven stages of a rupee, traced on our page"], "Source: CAG State Finances Audit 2024-25, paras 3.5.1, 2.7.1.2A", "reports/follow_the_money.html"),
      "kn": ("ಕರ್ನಾಟಕ, ಮಾರ್ಚ್ 2025 ಒಂದೇ ತಿಂಗಳು", "₹6,026 ಕೋಟಿ", "ವರ್ಷಾಂತ್ಯದಲ್ಲಿ ಠೇವಣಿ ಖಾತೆಗಳಿಗೆ", ["ಸಿಎಜಿ ಮಾತಿನಲ್ಲಿ: ಅನುದಾನ ವ್ಯಪಗತವಾಗದಂತೆ ಹಣವನ್ನು ಕೇವಲ ನಿಲ್ಲಿಸಿಡುವುದು", "ಒಂದು ವರ್ಷಕ್ಕೆ ಮಂಜೂರಾದ ಹಣ, ನಂತರಕ್ಕೆ ಇಟ್ಟದ್ದು", "ರೂಪಾಯಿಯ ಏಳು ಹಂತಗಳು ನಮ್ಮ ಪುಟದಲ್ಲಿ"], "ಮೂಲ: ಸಿಎಜಿ ರಾಜ್ಯ ಹಣಕಾಸು ಲೆಕ್ಕಪರಿಶೋಧನೆ 2024-25, ಕಂಡಿಕೆ 3.5.1", "reports/follow_the_money_kn.html")}),
    ("bills",
     {"en": ("PWD North zone, Belagavi to Vijayapura, end of July 2026", "₹555 crore", "of contractors' bills unpaid for more than a year", ["₹1,808 crore owed on 4,744 dated bills", "173 bills over three years old; the oldest from March 2018", "The lists show unpaid bills only, not who was paid first"], "Source: Assembly question 1485 (24 Aug 2026), annexure spreadsheets", "reports/follow_the_money.html#bills"),
      "kn": ("ಲೋಕೋಪಯೋಗಿ ಉತ್ತರ ವಲಯ, ಬೆಳಗಾವಿಯಿಂದ ವಿಜಯಪುರ, ಜುಲೈ 2026 ಅಂತ್ಯ", "₹555 ಕೋಟಿ", "ಗುತ್ತಿಗೆದಾರರ ಬಿಲ್ಲುಗಳು ಒಂದು ವರ್ಷಕ್ಕೂ ಹೆಚ್ಚು ಕಾಲದಿಂದ ಬಾಕಿ", ["4,744 ಬಿಲ್ಲುಗಳಲ್ಲಿ ₹1,808 ಕೋಟಿ ಬಾಕಿ", "173 ಬಿಲ್ಲುಗಳು ಮೂರು ವರ್ಷಕ್ಕಿಂತ ಹಳೆಯವು; ಅತ್ಯಂತ ಹಳೆಯದು ಮಾರ್ಚ್ 2018", "ಪಟ್ಟಿಯಲ್ಲಿ ಬಾಕಿ ಬಿಲ್ಲುಗಳು ಮಾತ್ರ; ಯಾರಿಗೆ ಮೊದಲು ಪಾವತಿ ಎಂಬುದಿಲ್ಲ"], "ಮೂಲ: ವಿಧಾನಸಭೆ ಪ್ರಶ್ನೆ 1485 (24 ಆಗಸ್ಟ್ 2026), ಅನುಬಂಧ", "reports/follow_the_money_kn.html#bills")}),
    ("seats",
     {"en": ("PWD works listed by Assembly seat, 2023-26", "₹56 cr vs ₹34 cr", "median Congress-held seat vs median BJP-held seat (JD(S): ₹20 cr)", ["₹11,035 crore of works across 199 seats; same gap in every zone", "Varuna, the CM's seat, 2nd at ₹210 crore; the PWD Minister's Yemkanamardi 9th", "Estimates, not spending; seats differ in need. A question for the department"], "Source: Assembly question 1485 (24 Aug 2026), Annexure-1", "reports/follow_the_money.html#seats"),
      "kn": ("ಕ್ಷೇತ್ರವಾರು ಲೋಕೋಪಯೋಗಿ ಕಾಮಗಾರಿಗಳು, 2023-26", "₹56 ಕೋಟಿ / ₹34 ಕೋಟಿ", "ಕಾಂಗ್ರೆಸ್ ಮಧ್ಯಮ ಕ್ಷೇತ್ರ / ಬಿಜೆಪಿ ಮಧ್ಯಮ ಕ್ಷೇತ್ರ (ಜೆಡಿ(ಎಸ್): ₹20 ಕೋಟಿ)", ["199 ಕ್ಷೇತ್ರಗಳಲ್ಲಿ ₹11,035 ಕೋಟಿ; ಪ್ರತಿ ವಲಯದಲ್ಲೂ ಇದೇ ಅಂತರ", "ಮುಖ್ಯಮಂತ್ರಿಗಳ ವರುಣ ₹210 ಕೋಟಿಯೊಂದಿಗೆ 2ನೇ; ಲೋಕೋಪಯೋಗಿ ಸಚಿವರ ಯಮಕನಮರಡಿ 9ನೇ", "ಅಂದಾಜು, ಖರ್ಚಲ್ಲ; ಅಗತ್ಯ ಬೇರೆ ಬೇರೆ. ಇಲಾಖೆಗೆ ಒಂದು ಪ್ರಶ್ನೆ"], "ಮೂಲ: ವಿಧಾನಸಭೆ ಪ್ರಶ್ನೆ 1485 (24 ಆಗಸ್ಟ್ 2026), ಅನುಬಂಧ-1", "reports/follow_the_money_kn.html#seats")}),
]

FOOT = {"kn": ("ಪ್ರತಿ ಅಂಕಿಯ ಮೂಲ, ನಿಮ್ಮ ಶಾಸಕರನ್ನು ತಿಳಿಯಿರಿ ಜಾಲತಾಣದಲ್ಲಿ:", "ಗಂಡಭೇರುಂಡ · ಆರೋಪವಲ್ಲ, ಅಧಿಕೃತ ದಾಖಲೆ"),
        "en": ("Every figure, with its source, on Know Your MLA:", "Gandaberunda · official records, not allegations")}

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+Kannada:wght@400;600;800&display=swap">
<style>
html,body{{margin:0;width:1080px;height:1080px;background:#0e1014;color:#f2f2ee;font-family:"Noto Sans Kannada","Segoe UI",sans-serif}}
.c>*{{flex-shrink:0}} .c{{box-sizing:border-box;width:1080px;height:1080px;padding:72px 80px;display:flex;flex-direction:column;gap:22px}}
.bar{{width:90px;height:8px;background:#f5b51b}}
.gov{{color:#f5b51b;font-weight:800;font-size:34px;letter-spacing:.02em}}
.big{{font-size:{bigpx}px;font-weight:800;line-height:1;color:#f5b51b;margin-top:6px}}
.head{{font-size:50px;font-weight:800;line-height:1.25}}
ul{{margin:8px 0 0;padding:0;list-style:none;display:flex;flex-direction:column;gap:14px;font-size:33px;line-height:1.35;color:#d8d8d2}}
li{{padding-left:30px;position:relative}} li:before{{content:"";position:absolute;left:0;top:.55em;width:12px;height:12px;background:#f5b51b}}
.sp{{flex:1}}
.foot{{border-top:2px solid #2a2d33;padding-top:22px;display:flex;flex-direction:column;gap:6px}}
.q{{font-size:28px;color:#d8d8d2}} .l{{font-size:31px;font-weight:800;color:#f2f2ee}}
.s{{font-size:22px;color:#8f939b}}
</style></head><body><div class="c">
<div class="bar"></div><div class="gov">{gov}</div><div class="big">{big}</div><div class="head">{head}</div>
<ul>{lis}</ul><div class="sp"></div>
<div class="foot"><div class="q">{q}</div><div class="l">{link}</div><div class="s">{src}</div><div class="s">{brand}</div></div>
</div></body></html>"""

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for cid, langs in CARDS:
            for lang, (gov, big, head, lines, src, link) in langs.items():
                e = html.escape
                bigpx = 190 if len(big) <= 6 else (150 if len(big) <= 9 else 120)
                page = PAGE.format(bigpx=bigpx, gov=e(gov), big=e(big), head=e(head), lis="".join(f"<li>{e(x)}</li>" for x in lines),
                                   q=e(FOOT[lang][0]), link=e(BASE.rstrip("/")), src=e(src), brand=e(FOOT[lang][1]))
                src_file = pathlib.Path(tmp) / f"{cid}-{lang}.html"
                src_file.write_text(page, encoding="utf-8")
                png = OUT / f"{cid}-{lang}.png"
                subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1080",
                                "--virtual-time-budget=6000", f"--screenshot={png}", src_file.as_uri()],
                               check=True, capture_output=True, timeout=90)
                print(png.name, png.stat().st_size)


if __name__ == "__main__":
    main()
