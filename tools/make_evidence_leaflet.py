"""One-page A4 leaflets (English and Kannada) of the Evidence page, for printing and WhatsApp.

    py tools/make_evidence_leaflet.py
writes reports/evidence_leaflet.pdf and reports/evidence_leaflet_kn.pdf with headless Chrome.
Figures come from tools/make_evidence_page.py (FINDINGS), so the page and the leaflet never disagree.
Print pages stay white (site rule).
"""
import html, pathlib, subprocess, tempfile, importlib.util

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
spec = importlib.util.spec_from_file_location("ev", ROOT / "tools" / "make_evidence_page.py")
ev = importlib.util.module_from_spec(spec); spec.loader.exec_module(ev)

URL = {"en": "jarvisss007.github.io/know-your-mla/reports/evidence.html",
       "kn": "jarvisss007.github.io/know-your-mla/reports/evidence_kn.html"}
TXT = {
 "en": dict(h="Karnataka's own records say:", sub=f"Every figure from an official document: auditors, the government's answers to the Legislature, national crime records. Checked {ev.CHECKED}.",
            act="What you can do", acts=["Ask for the record by RTI: ₹10, answer due in 30 days. Ready letters on the site.",
                                         "Ask your MLA or MLC to put a written question; the answer is published.",
                                         "Go to the Gram Sabha and the social audit; ask to see the work, the photo and the payment."],
            fair="An audit finding is not a court verdict; a raid is an accusation, not guilt. Both parties governed in these years.",
            more="Sources, the government's side and more:", brand="Gandaberunda · independent citizen publication · official records, not allegations"),
 "kn": dict(h="ಕರ್ನಾಟಕದ ಸ್ವಂತ ದಾಖಲೆಗಳು ಹೇಳುವುದು:", sub=f"ಪ್ರತಿ ಅಂಕಿಯೂ ಅಧಿಕೃತ ದಾಖಲೆಯಿಂದ: ಲೆಕ್ಕಪರಿಶೋಧಕರು, ಶಾಸನಸಭೆಗೆ ಸರ್ಕಾರದ ಉತ್ತರಗಳು, ರಾಷ್ಟ್ರೀಯ ಅಪರಾಧ ದಾಖಲೆಗಳು. ಪರಿಶೀಲನೆ {ev.CHECKED_KN}.",
            act="ನೀವು ಏನು ಮಾಡಬಹುದು", acts=["ಆರ್‌ಟಿಐ ಮೂಲಕ ದಾಖಲೆ ಕೇಳಿ: ₹10, 30 ದಿನಗಳಲ್ಲಿ ಉತ್ತರ. ಸಿದ್ಧ ಪತ್ರಗಳು ಜಾಲತಾಣದಲ್ಲಿ.",
                                         "ನಿಮ್ಮ ಶಾಸಕರು ಅಥವಾ ಪರಿಷತ್ ಸದಸ್ಯರಿಗೆ ಲಿಖಿತ ಪ್ರಶ್ನೆ ಕೇಳಲು ಹೇಳಿ; ಉತ್ತರ ಪ್ರಕಟವಾಗುತ್ತದೆ.",
                                         "ಗ್ರಾಮಸಭೆ ಮತ್ತು ಸಾಮಾಜಿಕ ಲೆಕ್ಕಪರಿಶೋಧನೆಗೆ ಹೋಗಿ; ಕಾಮಗಾರಿ, ಫೋಟೋ, ಪಾವತಿ ತೋರಿಸಲು ಕೇಳಿ."],
            fair="ಲೆಕ್ಕಪರಿಶೋಧನಾ ತೀರ್ಮಾನ ನ್ಯಾಯಾಲಯದ ತೀರ್ಪಲ್ಲ; ದಾಳಿ ಆರೋಪ, ಅಪರಾಧ ಸಾಬೀತಲ್ಲ. ಈ ವರ್ಷಗಳಲ್ಲಿ ಎರಡೂ ಪಕ್ಷಗಳು ಆಡಳಿತ ನಡೆಸಿವೆ.",
            more="ಮೂಲಗಳು, ಸರ್ಕಾರದ ಪಕ್ಷ ಮತ್ತು ಇನ್ನಷ್ಟು:", brand="ಗಂಡಭೇರುಂಡ · ಸ್ವತಂತ್ರ ನಾಗರಿಕ ಪ್ರಕಟಣೆ · ಅಧಿಕೃತ ದಾಖಲೆಗಳು, ಆರೋಪಗಳಲ್ಲ"),
}
PICK = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # ten findings fit one page

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+Kannada:wght@400;600;800&family=Space+Grotesk:wght@700&display=swap">
<style>
@page {{ size: A4; margin: 12mm; }}
html,body {{ margin:0; background:#fff; color:#111; font-family:"Noto Sans Kannada","Segoe UI",sans-serif; }}
.bar {{ height:6px; background:#c21f30; width:70px; margin-bottom:8px; }}
h1 {{ font: 800 25px/1.2 "Noto Sans Kannada","Segoe UI",sans-serif; margin:0 0 4px; }}
.sub {{ font-size:11.5px; color:#444; margin:0 0 10px; }}
.grid {{ display:grid; grid-template-columns:1fr 1fr; gap:8px; }}
.f {{ border:1px solid #ccc; border-left:4px solid #c21f30; border-radius:6px; padding:7px 9px; break-inside:avoid; }}
.f b {{ display:block; font: 700 21px/1.1 "Space Grotesk","Segoe UI",sans-serif; }}
.f p {{ margin:3px 0 0; font-size:11.2px; line-height:1.38; }}
.f small {{ display:block; margin-top:3px; color:#555; font-size:9.3px; line-height:1.3; }}
h2 {{ font-size:15px; margin:12px 0 5px; }}
ol {{ margin:0; padding-left:18px; font-size:11.5px; line-height:1.45; }}
.fair {{ font-size:10.5px; color:#333; margin:9px 0 0; }}
.foot {{ margin-top:10px; border-top:1px solid #ccc; padding-top:7px; font-size:11px; }}
.foot b {{ font-size:13px; }}
</style></head><body>
<div class="bar"></div><h1>{h}</h1><p class="sub">{sub}</p>
<div class="grid">{cards}</div>
<h2>{act}</h2><ol>{acts}</ol>
<p class="fair">{fair}</p>
<div class="foot">{more}<br><b>{url}</b><br>{brand}</div>
</body></html>"""


def main():
    e = html.escape
    with tempfile.TemporaryDirectory() as tmp:
        for lang, suffix in (("en", ""), ("kn", "_kn")):
            t = TXT[lang]; cards = []
            for i in PICK:
                (g, kind, big, l_en, l_kn, s_en, s_kn, p_en, p_kn) = ev.FINDINGS[i]
                line, src = (l_en, s_en) if lang == "en" else (l_kn, s_kn)
                cards.append(f'<div class="f"><b>{e(ev.big_for(big, lang))}</b><p>{e(line)}</p><small>{e(src)}</small></div>')
            doc = PAGE.format(h=e(t["h"]), sub=e(t["sub"]), cards="".join(cards), act=e(t["act"]),
                              acts="".join(f"<li>{e(a)}</li>" for a in t["acts"]), fair=e(t["fair"]),
                              more=e(t["more"]), url=URL[lang], brand=e(t["brand"]))
            src_file = pathlib.Path(tmp) / f"leaflet{suffix}.html"
            src_file.write_text(doc, encoding="utf-8")
            out = ROOT / "reports" / f"evidence_leaflet{suffix}.pdf"
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                            f"--print-to-pdf={out}", src_file.as_uri()], check=True, capture_output=True, timeout=120)
            print(out.name, out.stat().st_size)


if __name__ == "__main__":
    main()
