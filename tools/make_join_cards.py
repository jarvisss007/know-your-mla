"""Render square (1080x1080) WhatsApp cards inviting people to the Have your say page.

    py tools/make_join_cards.py
writes cards/join/<id>-kn.png and <id>-en.png using headless Chrome (same look as the farmer cards).
Kannada text is a draft for native review, like the rest of the site.
"""
import html, pathlib, subprocess, tempfile, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from make_farmer_cards import PAGE, CHROME  # one card design for the whole project

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "cards" / "join"
LINK = "jarvisss007.github.io/know-your-mla/#join"

# id, {lang: (kicker, big, headline, three lines, small print)}
CARDS = [
    ("you-decide",
     {"kn": ("ಗಂಡಭೇರುಂಡ", "ನೀವೇ", "ಹೇಳಿ: ಮುಂದೆ ನಾವು ಏನನ್ನು ಪರಿಶೀಲಿಸಬೇಕು?",
             ["ಹಣ ಪಾವತಿಯಾದರೂ ಆಗದ ಕಾಮಗಾರಿ", "ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಬರ ಪರಿಹಾರ ಎಲ್ಲಿ ಹೋಯಿತು", "ಜನರಿಗೆ ತಲುಪದ ಯೋಜನೆ"],
             "ಖಾತೆ ಬೇಕಿಲ್ಲ · ನಿಮ್ಮ ಹೆಸರು ಕೇಳುವುದಿಲ್ಲ"),
      "en": ("Gandaberunda", "You", "decide what we dig into next",
             ["A public work that was paid for but never built", "Where your district's drought relief went", "A scheme that is not reaching people"],
             "No account needed · we don't ask your name")}),
    ("from-space",
     {"kn": ("ಉಪಗ್ರಹದಿಂದ", "224", "ಕ್ಷೇತ್ರಗಳಲ್ಲಿ ನಿಮ್ಮದನ್ನು ಉಪಗ್ರಹದಿಂದ ನೋಡಲು ಕೇಳಿ",
             ["2019 ಮತ್ತು 2026ರ ಚಿತ್ರಗಳ ಹೋಲಿಕೆ", "ಹಸಿರು, ಕೆರೆಗಳು, ಹೊಸದಾಗಿ ಬಯಲಾದ ಜಾಗ", "ಹೆಚ್ಚು ಜನ ಕೇಳಿದ ಕ್ಷೇತ್ರ ಮೊದಲು"],
             "ಈಗಾಗಲೇ: ಕನಕಪುರ · ಹೊಳೆನರಸೀಪುರ · ಮಹದೇವಪುರ"),
      "en": ("From space", "224", "constituencies: ask for yours to be checked",
             ["Satellite pictures from 2019 and 2026, side by side", "Green cover, lakes and tanks, new bare ground", "The most-requested seats go next"],
             "Done so far: Kanakapura · Holenarasipur · Mahadevapura")}),
    ("be-there",
     {"kn": ("ಸ್ಥಳದಲ್ಲಿ ನೋಡಿ", "30", "ಜಾಗಗಳು ಬಯಲಾಗಿವೆ. ಅಲ್ಲಿ ಏನಿದೆ?",
             ["ಕನಕಪುರ ಮತ್ತು ಹೊಳೆನರಸೀಪುರದಲ್ಲಿ, ನಕ್ಷೆ ಸಹಿತ", "ಕಟ್ಟಡವೇ, ಕಲ್ಲುಗಣಿಯೇ, ಹೊಲವೇ? ನೀವು ಹೇಳಿ", "ಖಾಸಗಿ ಜಮೀನಿಗೆ ಹೋಗಬೇಡಿ"],
             "ಉಪಗ್ರಹ ತೋರಿಸುತ್ತದೆ; ನಿಜ ಏನು ಎಂದು ಸ್ಥಳದವರೇ ಹೇಳಬಲ್ಲರು"),
      "en": ("On the ground", "30", "patches turned bare. What is there?",
             ["In Kanakapura and Holenarasipur, with maps", "Buildings, a quarry, a field? Tell us", "Never enter private land"],
             "Satellites show change; only people there know what it is")}),
]
FOOT = {"kn": ("ನಿಮ್ಮ ಅಭಿಪ್ರಾಯ ತಿಳಿಸಿ:", "ಗಂಡಭೇರುಂಡ · ಎರಡೂ ಕಡೆ ನೋಡುತ್ತದೆ"),
        "en": ("Have your say:", "Gandaberunda · watching both sides")}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    e = html.escape
    with tempfile.TemporaryDirectory() as tmp:
        for cid, langs in CARDS:
            for lang, (gov, big, head, lines, small) in langs.items():
                page = PAGE.format(gov=e(gov), big=e(big), head=e(head), lis="".join(f"<li>{e(x)}</li>" for x in lines),
                                   q=e(FOOT[lang][0]), link=LINK, src=e(small), brand=e(FOOT[lang][1]))
                src_file = pathlib.Path(tmp) / f"{cid}-{lang}.html"
                src_file.write_text(page, encoding="utf-8")
                png = OUT / f"{cid}-{lang}.png"
                subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1080",
                                "--virtual-time-budget=6000", f"--screenshot={png}", src_file.as_uri()],
                               check=True, capture_output=True, timeout=90)
                print(png.name, png.stat().st_size)


if __name__ == "__main__":
    main()
