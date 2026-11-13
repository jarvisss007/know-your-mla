import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chars import stage, stage2, mallanna, neta, kaveri, STYLE

CAG_Y = 'Source: CAG Report No. 10 (Yettinahole project), tabled 29 January 2026'
CM27 = "Sources: CAG Report No. 10, 2026; Chief Minister's statement on the end-2027 target, 2026"
CAG_M = 'Source: CAG Report No. 2 of 2017 (Mysuru 24x7 water supply)'
UB = "Sources: Lok Sabha reply, August 2024; Chief Minister's statement, August 2026"
END = 'Fictional characters. Every figure in this video comes from a public record. If one is wrong, tell us and we will correct it.'
S = STYLE
SCENES = [
 (5.0, S + '<div class="k">ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 5 · ಬಾರದ ನೀರು</div>'
  '<div class="b n">ಈ ಸಲ ಗ್ಯಾರಂಟಿ! ನಿಮ್ಮ ಊರಿಗೆ ನೀರು!<small>This time, guaranteed! Water for your town!</small></div>'
  '<div class="b m">ಹೊಸ ಮಾತು ಹೇಳಿ ಸ್ವಾಮಿ. ಇದು 2012ರದ್ದು.<small>Say something new, sir. That one is from 2012.</small></div>'
  + stage('skeptic', 'namaste'), ''),

 (6.5, S + '<div class="k">ಎತ್ತಿನಹೊಳೆ ಕುಡಿಯುವ ನೀರಿನ ಯೋಜನೆ</div>'
  '<div class="row"><small>2012 · ಅನುಮೋದಿತ ವೆಚ್ಚ</small>₹8,323 ಕೋಟಿ</div>'
  '<div class="row"><small>2023 · ಪರಿಷ್ಕೃತ ವೆಚ್ಚ</small><b style="color:#ef5261">₹23,252 ಕೋಟಿ</b></div>'
  '<div class="row"><small>ಮಾರ್ಚ್ 2024ರ ವರೆಗೆ ಖರ್ಚು</small><b>₹15,297 ಕೋಟಿ</b></div>'
  '<div class="en">Yettinahole: approved at Rs 8,323 crore, now Rs 23,252 crore. Rs 15,297 crore spent by March 2024. The auditor: "could not be made operational even after 12 years".</div>', CAG_Y),

 (5.0, S + '<div class="b m">ಕೋಲಾರ, ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಇನ್ನೂ ಕಾಯ್ತಿದೆ.<small>Kolar and Chikkaballapura are still waiting.</small></div>'
  + stage2([(mallanna('neutral'), 10, -40, 0.9), (kaveri('sad'), 520, 80, 1.0)]) +
  '<div class="en" style="margin-top:16px">The government\'s new promise: water by the end of 2027.</div>', CM27),

 (6.0, S + '<div class="k">ಮೈಸೂರು · 24x7 ನೀರು ಯೋಜನೆ</div>'
  '<div class="big r">₹271.56 ಕೋಟಿ</div>'
  '<h2 style="margin-top:24px">ಖರ್ಚು. 24x7 ನೀರು ಬರಲಿಲ್ಲ.</h2>'
  '<div class="en">Mysuru: Rs 271.56 crore spent on round-the-clock water, and the city still did not get it. The coverage area was cut from 69 zones to 47.</div>', CAG_M),

 (6.5, S + '<div class="k">ಭದ್ರಾ ಮೇಲ್ದಂಡೆ · ಚಿತ್ರದುರ್ಗ, ದಾವಣಗೆರೆ</div>'
  '<div class="row"><small>2003 · ಮೊದಲ ಹಂತ</small>₹2,813 ಕೋಟಿ</div>'
  '<div class="row"><small>2020 · ಪರಿಷ್ಕೃತ</small><b style="color:#ef5261">₹21,474 ಕೋಟಿ</b></div>'
  '<div class="en">Upper Bhadra: Rs 5,300 crore was announced in the 2023-24 Union Budget. The Centre later told Parliament the project is under no central scheme. In August 2026 the state said the money never came. Two governments, two parties, one unfinished project.</div>', UB),

 (5.0, S + '<div class="b" style="background:#8fd3ff">ಅಪ್ಪಾ, ನೀರು ಬರಲ್ಲ. ಬಿಲ್ ಮಾತ್ರ ಬರುತ್ತೆ.<small>Dad, the water never comes. Only the bill does.</small></div>'
  + stage2([(mallanna('firm'), 10, -40, 0.9), (kaveri('ask'), 520, 80, 1.0)]), ''),

 (5.0, S + '<h1>2012ರಿಂದ ಪ್ರತಿ ಸರ್ಕಾರವೂ ಇದನ್ನು ನಡೆಸಿದೆ.</h1><div class="mid">ಬಿಜೆಪಿ · ಕಾಂಗ್ರೆಸ್ · ಸಮ್ಮಿಶ್ರ</div>'
  '<div class="en">Every government since 2012 has run Yettinahole: BJP, Congress and coalition.</div>', CAG_Y),

 (6.5, S + '<h1 style="font-size:92px">ಕೆಲಸ ತೋರಿಸಿ.<br><span style="color:#f2b705">ಆಮೇಲೆ ಮತ.</span></h1>'
  + stage('firm', 'namaste', 'point', show_neta=False) +
  '<div class="mid" style="font-size:40px;margin:14px 0 0">ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ #5: ನೀರು ನಮ್ಮ ಊರಿಗೆ ಯಾವಾಗ? ಬರೆದು ಕೊಡಿ.</div>'
  '<div class="en" style="margin-top:8px;font-size:36px">Kaveri\'s question: when will the water reach our town? Put it in writing.</div>'
  '<div class="url" style="margin-top:10px">jarvisss007.github.io/know-your-mla</div>', END),
]
OUT = 'mallanna5-kn.mp4'
FPS = 10
