"""Render square (1080x1080) WhatsApp cards for the farmer scheme finder.

Facts come from research/farmer_schemes/SOURCES_DRAFT.md (checked 16 Nov 2026).
Only schemes whose amounts are confirmed at an official source or reputable press are carded.

    py tools/make_farmer_cards.py
writes cards/farmers/<id>-kn.png and <id>-en.png using headless Chrome.
"""
import html, pathlib, subprocess, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "cards" / "farmers"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LINK = "jarvisss007.github.io/know-your-mla/farmers.html"

# id, gov, big number, headline, three lines (who / where / note), source
CARDS = [
    ("pm-kisan",
     {"kn": ("ಕೇಂದ್ರ ಯೋಜನೆ", "₹6,000", "ವರ್ಷಕ್ಕೆ, ಪಿಎಂ-ಕಿಸಾನ್", ["ಮೂರು ಕಂತು, ತಲಾ ₹2,000, ನೇರವಾಗಿ ಬ್ಯಾಂಕ್‌ಗೆ", "e-KYC ಮಾಡಿಸದಿದ್ದರೆ ಹಣ ನಿಲ್ಲುತ್ತದೆ", "pmkisan.gov.in · ಆ್ಯಪ್ · ಗ್ರಾಮ ಒನ್"], "ಮೂಲ: PIB, 20 ಜೂನ್ 2026"),
      "en": ("Central scheme", "₹6,000", "a year, PM-KISAN", ["Three instalments of ₹2,000, straight to your bank", "Payments stop if e-KYC is not done", "pmkisan.gov.in · the app · Grama One"], "Source: PIB, 20 Jun 2026")}),
    ("zero-loan",
     {"kn": ("ರಾಜ್ಯ ಯೋಜನೆ", "0%", "ಬಡ್ಡಿ, ₹5 ಲಕ್ಷದವರೆಗೆ ಬೆಳೆ ಸಾಲ", ["ಮಧ್ಯಮ/ದೀರ್ಘಾವಧಿ ಸಾಲ ₹15 ಲಕ್ಷದವರೆಗೆ 3%", "ಸಮಯಕ್ಕೆ ಮರುಪಾವತಿ ಮಾಡಿದರೆ ಮಾತ್ರ", "ನಿಮ್ಮ ಊರಿನ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರ ಸಂಘ (PACS)"], "ಮೂಲ: ಕರ್ನಾಟಕ ಬಜೆಟ್ 2026-27 ಯೋಜನಾ ಪಟ್ಟಿ"),
      "en": ("State scheme", "0%", "interest on crop loans up to ₹5 lakh", ["Medium/long-term loans up to ₹15 lakh at 3%", "Only if you repay on time", "Your village cooperative society (PACS)"], "Source: Karnataka budget 2026-27 scheme list")}),
    ("crop-insurance",
     {"kn": ("ಕೇಂದ್ರ + ರಾಜ್ಯ", "2%", "ಮಾತ್ರ ನೀವು ಕಟ್ಟುವ ಬೆಳೆ ವಿಮೆ ಪ್ರೀಮಿಯಂ", ["ಮುಂಗಾರು 2% · ಹಿಂಗಾರು 1.5% · ತೋಟಗಾರಿಕೆ 5%", "ಉಳಿದದ್ದು ಕೇಂದ್ರ-ರಾಜ್ಯ ಅರ್ಧ ಅರ್ಧ; ಗೇಣಿದಾರರೂ ಸೇರಬಹುದು", "ಬ್ಯಾಂಕ್ · CSC · ಸಹಾಯವಾಣಿ 14447"], "ಮೂಲ: PIB, 29 ಆಗಸ್ಟ್ 2026"),
      "en": ("Centre + state", "2%", "is all you pay for crop insurance", ["Kharif 2% · rabi 1.5% · horticulture 5%", "Centre and state split the rest; tenants can join", "Bank · CSC · helpline 14447"], "Source: PIB, 29 Aug 2026")}),
    ("crop-loss",
     {"kn": ("ರಾಜ್ಯ ಪರಿಹಾರ", "₹17,000", "ಹೆಕ್ಟೇರ್‌ಗೆ, ಮಳೆಯಾಶ್ರಿತ ಬೆಳೆ ನಷ್ಟ", ["ನೀರಾವರಿ ₹25,500 · ಬಹುವಾರ್ಷಿಕ ₹31,000 · ಗರಿಷ್ಠ 2 ಹೆಕ್ಟೇರ್", "2026 ಬರ: ಪ್ರತಿ ರೈತರಿಗೆ ಕನಿಷ್ಠ ₹5,000 ಎಂದು ಸರ್ಕಾರ", "ಗ್ರಾಮದ ಪಟ್ಟಿ ನೋಡಿ; ಹೆಸರು ಇಲ್ಲದಿದ್ದರೆ ಆಕ್ಷೇಪಣೆ ಕೊಡಿ"], "ಮೂಲ: IANS, 27 ನವೆಂಬರ್ 2025 ಮತ್ತು 10 ನವೆಂಬರ್ 2026"),
      "en": ("State relief", "₹17,000", "a hectare for a lost rainfed crop", ["Irrigated ₹25,500 · perennial ₹31,000 · up to 2 ha", "2026 drought: at least ₹5,000 per farmer, says the government", "Check the village list; object if your name is missing"], "Source: IANS, 27 Nov 2025 and 10 Nov 2026")}),
    ("raitha-siri",
     {"kn": ("ರಾಜ್ಯ ಯೋಜನೆ", "₹10,000", "ಹೆಕ್ಟೇರ್‌ಗೆ, ಸಿರಿಧಾನ್ಯ ಬೆಳೆದರೆ (ರೈತ ಸಿರಿ)", ["ನವಣೆ, ಸಾಮೆ, ಹಾರಕ, ಬರಗು, ಕೊರಲೆ, ಊದಲು", "ಬೆಳೆ ಸಮೀಕ್ಷೆಯಲ್ಲಿ ದಾಖಲಾಗಿರಬೇಕು", "ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ (RSK)"], "ಮೂಲ: ಕರ್ನಾಟಕ ಬಜೆಟ್ 2026-27 ಯೋಜನಾ ಪಟ್ಟಿ"),
      "en": ("State scheme", "₹10,000", "a hectare for minor millets (Raitha Siri)", ["Foxtail, little, kodo, browntop, proso, barnyard", "Must be recorded in the crop survey", "Raitha Samparka Kendra (RSK)"], "Source: Karnataka budget 2026-27 scheme list")}),
    ("msp",
     {"kn": ("ಕೇಂದ್ರ ಬೆಂಬಲ ಬೆಲೆ", "₹5,205", "ಕ್ವಿಂಟಾಲ್ ರಾಗಿಗೆ, 2026-27", ["ಭತ್ತ ₹2,441 · ಜೋಳ ₹4,023 · ತೊಗರಿ ₹8,450 · ಮೆಕ್ಕೆಜೋಳ ₹2,410", "ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಕಡಿಮೆ ಇದ್ದರೆ ಸರ್ಕಾರಕ್ಕೆ ಮಾರಿ", "ಖರೀದಿ ಕೇಂದ್ರದಲ್ಲಿ FRUITS ID ಜೊತೆ ನೋಂದಣಿ"], "ಮೂಲ: ಕೇಂದ್ರ ಸಚಿವ ಸಂಪುಟ, 13 ಮೇ 2026"),
      "en": ("Central support price", "₹5,205", "a quintal for ragi, 2026-27", ["Paddy ₹2,441 · jowar ₹4,023 · tur ₹8,450 · maize ₹2,410", "Sell to the government when the market pays less", "Register at a procurement centre with your FRUITS ID"], "Source: Union Cabinet, 13 May 2026")}),
    ("machines-drip",
     {"kn": ("ಕೇಂದ್ರ ಯೋಜನೆ", "50%", "ಯಂತ್ರದ ಬೆಲೆಯ ಸಹಾಯಧನ", ["5 ಎಕರೆ ಒಳಗಿನ ರೈತರು ಮತ್ತು SC/ST: 50% · ಇತರರು 40%", "ಹನಿ/ತುಂತುರು ನೀರಾವರಿ: ಸಣ್ಣ ರೈತರಿಗೆ 55% · ಇತರರಿಗೆ 45%", "ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ (RSK)"], "ಮೂಲ: PIB, 9 ಜುಲೈ ಮತ್ತು 29 ಆಗಸ್ಟ್ 2026"),
      "en": ("Central scheme", "50%", "of a farm machine's price", ["Up to 5 acres, and SC/ST: 50% · others 40%", "Drip/sprinkler: 55% for small farmers · 45% others", "Raitha Samparka Kendra (RSK)"], "Source: PIB, 9 Jul and 29 Aug 2026")}),
    ("pension",
     {"kn": ("ಕೇಂದ್ರ ಯೋಜನೆ", "₹3,000", "ತಿಂಗಳಿಗೆ ಪಿಂಚಣಿ, 60ರ ನಂತರ", ["18-40 ವಯಸ್ಸಿನಲ್ಲಿ ಸೇರಿ; ತಿಂಗಳಿಗೆ ₹55 ರಿಂದ ₹200", "ಸರ್ಕಾರ ಅಷ್ಟೇ ಸೇರಿಸುತ್ತದೆ · 5 ಎಕರೆ ಒಳಗಿನ ರೈತರು", "ಹತ್ತಿರದ CSC · pmkmy.gov.in"], "ಮೂಲ: PIB (ಪಿಎಂ ಕಿಸಾನ್ ಮಾನ್‌ಧನ್)"),
      "en": ("Central scheme", "₹3,000", "a month pension after 60", ["Join at 18-40; pay ₹55 to ₹200 a month", "The government matches it · up to 5 acres", "Nearest CSC · pmkmy.gov.in"], "Source: PIB (PM Kisan Maandhan)")}),
    ("milk",
     {"kn": ("ರಾಜ್ಯ ಯೋಜನೆ", "₹5", "ಪ್ರತಿ ಲೀಟರ್ ಹಾಲಿಗೆ (ಕ್ಷೀರಧಾರೆ)", ["ದಿನಕ್ಕೆ 10 ಲೀಟರ್ = ತಿಂಗಳಿಗೆ ಸುಮಾರು ₹1,500", "ಹಿಂದೆ ತಿಂಗಳುಗಟ್ಟಲೆ ತಡವಾಗಿತ್ತು", "ಸಂಘದ ಕಾರ್ಯದರ್ಶಿಯನ್ನು ಕೇಳಿ: ನನ್ನ ಬಾಕಿ ಎಷ್ಟು?"], "ಮೂಲ: KMF, ಜೂನ್ 2026"),
      "en": ("State scheme", "₹5", "for every litre of milk (Ksheeradhare)", ["10 litres a day = about ₹1,500 a month", "Payments have run months late before", "Ask the society secretary: how much am I owed?"], "Source: KMF, Jun 2026")}),
    ("kcc",
     {"kn": ("ಕೇಂದ್ರ ಯೋಜನೆ", "4%", "ಬಡ್ಡಿ, ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ ಸಾಲ", ["7% ಬಡ್ಡಿ; ಸಮಯಕ್ಕೆ ಕಟ್ಟಿದರೆ 3% ವಾಪಸ್", "₹2 ಲಕ್ಷದವರೆಗೆ ಜಾಮೀನು ಬೇಡ · ಗೇಣಿದಾರರು, ಹೈನುಗಾರರೂ", "ಯಾವುದೇ ಬ್ಯಾಂಕ್, ಒಂದು ಪುಟದ ಅರ್ಜಿ"], "ಮೂಲ: PIB, 11 ಮಾರ್ಚ್ 2026"),
      "en": ("Central scheme", "4%", "interest on a Kisan Credit Card loan", ["7% interest; 3% back if you repay on time", "No collateral up to ₹2 lakh · tenants and dairy too", "Any bank, one-page form"], "Source: PIB, 11 Mar 2026")}),
]

FOOT = {"kn": ("ನಿಮಗೆ ಯಾವ ಯೋಜನೆ ಸಿಗುತ್ತದೆ? 8 ಪ್ರಶ್ನೆ ಉತ್ತರಿಸಿ:", "ಗಂಡಭೇರುಂಡ · ನಾವು ಯಾವುದೇ ಹಣ ಅಥವಾ ದಾಖಲೆ ಕೇಳುವುದಿಲ್ಲ"),
        "en": ("Which schemes do you qualify for? Answer 8 questions:", "Gandaberunda · we never ask for money or documents")}

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+Kannada:wght@400;600;800&display=swap">
<style>
html,body{{margin:0;width:1080px;height:1080px;background:#0e1014;color:#f2f2ee;font-family:"Noto Sans Kannada","Segoe UI",sans-serif}}
.c{{box-sizing:border-box;width:1080px;height:1080px;padding:72px 80px;display:flex;flex-direction:column;gap:22px}}
.bar{{width:90px;height:8px;background:#f5b51b}}
.gov{{color:#f5b51b;font-weight:800;font-size:34px;letter-spacing:.02em}}
.big{{font-size:190px;font-weight:800;line-height:1;color:#f5b51b;margin-top:6px}}
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
            for lang, (gov, big, head, lines, src) in langs.items():
                e = html.escape
                page = PAGE.format(gov=e(gov), big=e(big), head=e(head), lis="".join(f"<li>{e(x)}</li>" for x in lines),
                                   q=e(FOOT[lang][0]), link=LINK, src=e(src), brand=e(FOOT[lang][1]))
                src_file = pathlib.Path(tmp) / f"{cid}-{lang}.html"
                src_file.write_text(page, encoding="utf-8")
                png = OUT / f"{cid}-{lang}.png"
                subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1080",
                                "--virtual-time-budget=6000", f"--screenshot={png}", src_file.as_uri()],
                               check=True, capture_output=True, timeout=90)
                print(png.name, png.stat().st_size)


if __name__ == "__main__":
    main()
