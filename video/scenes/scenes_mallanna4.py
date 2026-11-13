import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chars import stage, stage2, mallanna, neta, kaveri, amma, STYLE

VAC = "Source: Karnataka Health Department figures, December 2024 (reported by Medical Dialogues)"
PRS = 'Source: PRS Legislative Research, Karnataka Budget Analysis 2026-27'
NFHS = 'Sources: CAG Report No. 10 of 2022 (NFHS figures); NFHS-5 district factsheet, Tumakuru'
SRS = 'Source: Sample Registration System bulletins, 2018 and 2023'
END = 'Fictional characters. Every figure in this video comes from a public record. If one is wrong, tell us and we will correct it.'
S = STYLE
SCENES = [
 (5.0, S + '<div class="k">ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 4 · ಅಮ್ಮನ ಆಸ್ಪತ್ರೆ</div>'
  '<div class="b n">ನಿಮ್ಮ ಊರಿಗೆ ದೊಡ್ಡ ಆಸ್ಪತ್ರೆ ಕಟ್ಟಿಸ್ತೀನಿ!<small>I will build your town a big hospital!</small></div>'
  '<div class="b m">ಕಟ್ಟಡ ಇದೆ ಸ್ವಾಮಿ. ಡಾಕ್ಟರ್ ಇಲ್ಲ.<small>The building is there, sir. The doctor is not.</small></div>'
  + stage('skeptic', 'namaste'), ''),

 (6.0, S + '<div class="b m">ಅಮ್ಮನ ಶುಗರ್ ಚೆಕ್‌ಅಪ್‌ಗೆ ಮೂರನೇ ಸಲ ಬಂದ್ವಿ.<small>Third trip for Amma\'s sugar check-up.</small></div>'
  + stage2([(mallanna('neutral'), 10, -40, 0.9), (amma(), 470, 30, 0.95)]) +
  '<div class="fact"><b>32,870 / 69,915</b><span>ಆರೋಗ್ಯ ಇಲಾಖೆ ಹುದ್ದೆಗಳು ಖಾಲಿ</span><i>Health Department posts vacant in Karnataka, December 2024: 47%.</i></div>', VAC),

 (5.5, S + '<div class="b" style="background:#8fd3ff">ಅಪ್ಪಾ, ನೂರು ಜನ ಬೇಕಾದಲ್ಲಿ 47 ಜನ ಇಲ್ಲ ಅಂದ್ರೆ, ಕೆಲಸ ಯಾರು ಮಾಡ್ತಾರೆ?<small>Dad, if 47 of every 100 people needed are missing, who does the work?</small></div>'
  + stage2([(mallanna('skeptic'), 10, -40, 0.9), (kaveri('ask'), 520, 80, 1.0)]), ''),

 (5.5, S + '<div class="k">ಬಜೆಟ್‌ನಲ್ಲಿ ಆರೋಗ್ಯದ ಪಾಲು · 2026-27</div>'
  '<div class="row"><small>ಕರ್ನಾಟಕ</small><b style="color:#ef5261">4.3%</b></div>'
  '<div class="row"><small>ಎಲ್ಲ ರಾಜ್ಯಗಳ ಸರಾಸರಿ</small>6.2%</div>'
  '<div class="en">Karnataka spends 4.3% of its budget on health. The average state spends 6.2%.</div>', PRS),

 (6.5, S + '<div class="k">ಮಕ್ಕಳ ರಕ್ತಹೀನತೆ (6-59 ತಿಂಗಳು) · 2015-16 → 2019-21</div>'
  '<div class="row"><small>ಯಾದಗಿರಿ</small>74% → <b style="color:#ef5261">76%</b></div>'
  '<div class="row"><small>ಕಲಬುರಗಿ</small>72.4% → <b style="color:#ef5261">75.1%</b></div>'
  '<div class="row"><small>ತುಮಕೂರು</small>53.8% → <b style="color:#ef5261">67.6%</b></div>'
  '<div class="en">Children with anaemia went up in these districts between the last two national health surveys.</div>', NFHS),

 (5.0, S + '<div class="k">ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ</div>'
  '<h2>ಶಿಶು ಮರಣ ದರ ಇಳಿದಿದೆ: 1,000 ಜನನಕ್ಕೆ 23 ರಿಂದ 14.</h2>'
  '<div class="en">To be fair: infant deaths fell from 23 to 14 per 1,000 births (2018 to 2023), below the national 25. Imagine it with every post filled.</div>', SRS),

 (5.5, S + '<div class="b m">ಆಸ್ಪತ್ರೆ ಉದ್ಘಾಟನೆಗೆ ರಿಬ್ಬನ್ ಕತ್ತರಿಸೋಕೆ ಬರ್ತೀರಾ. ಡಾಕ್ಟರ್ ನೇಮಕಕ್ಕೆ?<small>You come to cut the ribbon on the hospital. And to appoint the doctors?</small></div>'
  + stage('firm', 'smug', 'point'), ''),

 (6.5, S + '<h1 style="font-size:92px">ಕೆಲಸ ತೋರಿಸಿ.<br><span style="color:#f2b705">ಆಮೇಲೆ ಮತ.</span></h1>'
  + stage2([(mallanna('firm'), 10, -40, 0.9), (kaveri('smile'), 520, 80, 1.0)], label=False) +
  '<div class="mid" style="font-size:40px;margin:14px 0 0">ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ #4: ನಮ್ಮ ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ಎಷ್ಟು ಹುದ್ದೆ ಖಾಲಿ? ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ.</div>'
  '<div class="en" style="margin-top:8px;font-size:36px">Kaveri\'s question: how many posts are empty at our hospital? Ask your MLA.</div>'
  '<div class="url" style="margin-top:10px">jarvisss007.github.io/know-your-mla</div>', END),
]
OUT = 'mallanna4-kn.mp4'
FPS = 10
