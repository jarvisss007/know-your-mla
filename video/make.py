# Builds the pay-rise pilot: HTML scenes -> PNG (headless Chrome) -> MP4 (OpenCV).
import io, os, subprocess, sys
import cv2, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
W, H, FPS = 1080, 1920, 15
MARK = io.open(sys.argv[1], encoding='utf-8').read()

CSS = '''*{box-sizing:border-box;margin:0}
body{width:1080px;height:1920px;background:#11141a;color:#eceef2;font-family:"Nirmala UI","Segoe UI",sans-serif;overflow:hidden}
.flag{position:absolute;left:0;right:0;top:0;height:16px;display:flex}.flag i{flex:1}.flag i:first-child{background:#f2b705}.flag i:last-child{background:#c21f30}
.brand{position:absolute;left:80px;top:110px;display:flex;align-items:center;gap:18px;color:#9aa3b2;font:600 34px "Segoe UI",sans-serif}.brand svg{width:72px;height:72px}
.main{position:absolute;left:80px;right:150px;top:330px;height:1100px;display:flex;flex-direction:column;justify-content:center}
.k{color:#f2b705;font-weight:700;font-size:40px;letter-spacing:.04em;margin-bottom:34px}
h1{font-size:104px;line-height:1.18;font-weight:800}
h2{font-size:78px;line-height:1.22;font-weight:700}
.big{font:800 170px/1 "Segoe UI",sans-serif;color:#f2b705}.big.r{color:#ef5261}
.mid{font-size:56px;color:#c9cdd3;margin:26px 0}
.en{font:400 44px/1.4 "Segoe UI",sans-serif;color:#9aa3b2;margin-top:44px}
.row{margin-top:44px;font:800 84px/1.15 "Segoe UI",sans-serif;white-space:nowrap}.row small{display:block;font:600 40px "Nirmala UI","Segoe UI",sans-serif;color:#9aa3b2;margin-bottom:8px}.row b{color:#f2b705}
.src{position:absolute;left:80px;right:150px;top:1470px;font:400 28px/1.45 "Segoe UI",sans-serif;color:#6f7888}
.url{font:700 44px "Segoe UI",sans-serif;color:#f2b705;margin-top:40px;white-space:nowrap}'''

def page(body, src=''):
    return ('<!doctype html><html><head><meta charset="utf-8"><style>' + CSS + '</style></head><body>'
            '<div class="flag"><i></i><i></i></div><div class="brand">' + MARK + 'Gandaberunda</div>'
            '<div class="main">' + body + '</div>' + ('<div class="src">' + src + '</div>' if src else '') + '</body></html>')

import importlib.util
_name = sys.argv[2] if len(sys.argv) > 2 else None
if _name:
    _spec = importlib.util.spec_from_file_location('scenes', os.path.join(HERE, _name))
    _m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
    SCENES, OUT = _m.SCENES, _m.OUT
else:
    SRC_PAY = 'Source: Karnataka Legislative Assembly proceedings, 21 March 2025'
    # (seconds, html body, source line)
    SCENES = [
     (4.0, '<h1>ಕರ್ನಾಟಕ ವಿಧಾನಸಭೆಯಲ್ಲಿ ಅತಿ ವೇಗವಾಗಿ ಮುಗಿದ ಕೆಲಸ ಯಾವುದು?</h1><div class="en">What is the fastest job the Karnataka Assembly ever finished?</div>', ''),
     (3.5, '<div class="k">ಉತ್ತರ</div><h1>ಶಾಸಕರ ಸ್ವಂತ ಸಂಬಳ ಏರಿಕೆ.</h1><div class="en">The MLAs\' own pay rise.</div>', ''),
     (5.0, '<div class="k">ಮಾರ್ಚ್ 2025 · ಮೂಲ ವೇತನ, ತಿಂಗಳಿಗೆ</div><div class="big">₹40,000</div><div class="mid">ಇದ್ದದ್ದು</div><div class="big r">₹80,000</div><div class="en">March 2025. Basic monthly salary: Rs 40,000 became Rs 80,000.</div>', SRC_PAY),
     (4.0, '<div class="k">ಚರ್ಚೆ ಎಷ್ಟು ಹೊತ್ತು?</div><h1>ಚರ್ಚೆಯೇ ಇಲ್ಲ.</h1><div class="en">How long was the debate? There was none. It passed without discussion.</div>', SRC_PAY),
     (6.0, '<div class="k">ಇದು ಒಂದೇ ಪಕ್ಷದ ಕಥೆಯಲ್ಲ</div><div class="row"><small>2022 · ಬಿಜೆಪಿ ಸರ್ಕಾರ</small>₹25,000 → <b>₹40,000</b></div><div class="row"><small>2025 · ಕಾಂಗ್ರೆಸ್ ಸರ್ಕಾರ</small>₹40,000 → <b>₹80,000</b></div><div class="en">Not one party. BJP raised it in 2022, Congress doubled it in 2025. On this, they agree.</div>', SRC_PAY),
     (6.0, '<div class="k">ಅದೇ ಸಮಯದಲ್ಲಿ · ಆರೋಗ್ಯ ಇಲಾಖೆ</div><div class="big r">32,870</div><h2 style="margin-top:30px">ಹುದ್ದೆಗಳು ಖಾಲಿ</h2><div class="mid">ಒಟ್ಟು 69,915 ಹುದ್ದೆಗಳಲ್ಲಿ</div><div class="en">Meanwhile: 32,870 of 69,915 Health Department posts are vacant.</div>', "Source: Health Minister's reply in the Legislative Council, December 2024"),
     (5.0, '<h1>ತಮ್ಮ ಸಂಬಳಕ್ಕೆ ಸಮಯ ಸಿಕ್ಕಿತು.</h1><h2 style="margin-top:44px;color:#f2b705">ಆಸ್ಪತ್ರೆಯ ಹುದ್ದೆಗಳಿಗೆ?</h2><div class="en">They found time for their own pay. For the hospital posts?</div>', ''),
     (6.5, '<div class="k">ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ</div><h2>ನಿಮ್ಮ ಶಾಸಕರ ಆಸ್ತಿ, ಸಾಲ, ಪ್ರಕರಣಗಳನ್ನು ನೀವೇ ನೋಡಿ.</h2><div class="url">jarvisss007.github.io/know-your-mla</div><div class="en">Ask your MLA. Look up their sworn wealth, debts and cases yourself. All 224, every party.</div>', 'Every figure in this video comes from a public record. If one is wrong, tell us and we will correct it.'),
    ]
    OUT = 'pay-rise-pilot-kn.mp4'

frames = []
for i, (sec, body, src) in enumerate(SCENES):
    h = os.path.join(HERE, OUT[:-4] + '-s%d.html' % i); p = os.path.join(HERE, OUT[:-4] + '-s%d.png' % i)
    io.open(h, 'w', encoding='utf-8').write(page(body, src))
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--window-size=%d,%d' % (W, H), '--user-data-dir=' + os.path.join(HERE, 'prof'),
                    '--screenshot=' + p, 'file:///' + h.replace('\\', '/')], stderr=subprocess.DEVNULL, check=True)
    img = cv2.imdecode(np.fromfile(p, dtype=np.uint8), cv2.IMREAD_COLOR)
    assert img is not None and img.shape[:2] == (H, W), (p, None if img is None else img.shape)
    frames.append((sec, img))

out = os.path.join(HERE, OUT)
vw = cv2.VideoWriter(out, cv2.VideoWriter_fourcc(*'mp4v'), FPS, (W, H))
if not vw.isOpened():
    print('avc1 unavailable, using mp4v')
    vw = cv2.VideoWriter(out, cv2.VideoWriter_fourcc(*'mp4v'), FPS, (W, H))
assert vw.isOpened()
total = sum(s for s, _ in frames); done = 0.0
FADE = int(0.35 * FPS)
prev = None
for sec, img in frames:
    n = int(sec * FPS)
    for f in range(n):
        fr = img
        if prev is not None and f < FADE:
            a = (f + 1) / FADE
            fr = cv2.addWeighted(img, a, prev, 1 - a, 0)
        fr = fr.copy()
        x = int(W * (done + f / FPS) / total)           # thin progress line under the flag stripe
        cv2.rectangle(fr, (0, 16), (x, 22), (236, 238, 242), -1)
        vw.write(fr)
    prev = img; done += sec
vw.release()
print(out, round(total, 1), 'seconds', os.path.getsize(out) // 1024, 'KB')
