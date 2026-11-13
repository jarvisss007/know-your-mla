import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chars import stage, STYLE

EC = 'Source: Election Commission figures, 8 May 2023 (reported by Business Today and Udayavani)'
BNS = 'Source: Bharatiya Nyaya Sanhita, 2023, sections 170 and 173. A promise of public policy is not bribery under the law.'
PRS = 'Source: PRS Legislative Research, Karnataka Budget Analysis 2026-27'
FIN = 'Sources: PRS Legislative Research; Karnataka Finance Department note, 17 September 2026'
PAY = "Sources: Karnataka Legislative Assembly, 2022 and 21 March 2025; MLAs' own sworn affidavits, 2018 and 2023"
END = 'Every figure in this video comes from a public record. If one is wrong, tell us and we will correct it.'

S = STYLE
SCENES = [
 (4.5, S + '<div class="k">ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 1</div>'
  '<div class="b n">ನಮಸ್ಕಾರ ಮಲ್ಲಣ್ಣ! ಈ ಸಲ ವೋಟು ನನಗೇ!<small>Namaskara Mallanna! Your vote is mine this time!</small></div>'
  '<div class="b m">ನೀವು ಯಾರು ಸ್ವಾಮಿ? ಐದು ವರ್ಷ ಆಯ್ತು ನೋಡಿ.<small>Who are you, sir? It has been five years.</small></div>'
  + stage('skeptic', 'namaste'), ''),

 (6.0, S + '<div class="b n">ಇಗೋ, ಸೀರೆ, ಕುಕ್ಕರ್, ಸ್ವಲ್ಪ ಕಾಸು…<small>Here, a sari, a cooker, a little cash…</small></div>'
  + stage('skeptic', 'gift') +
  '<div class="fact"><b>₹375.61 ಕೋಟಿ</b><span>2023ರ ಚುನಾವಣೆಯಲ್ಲಿ ವಶಪಡಿಸಿಕೊಂಡ ನಗದು, ಮದ್ಯ, ಚಿನ್ನ, ಉಡುಗೊರೆ</span><i>Cash, liquor, gold and gifts seized in Karnataka\'s 2023 election: 4.5 times 2018.</i></div>', EC),

 (5.5, S + '<div class="b m">ಕೊಡೋದೂ ಅಪರಾಧ. ತಗೊಳ್ಳೋದೂ ಅಪರಾಧ.<small>Giving it is a crime. Taking it is a crime.</small></div>'
  + stage('firm', 'gift', 'stop') +
  '<div class="fact"><b>1 ವರ್ಷ ಜೈಲು</b><span>ಮತಕ್ಕಾಗಿ ಹಣ ಕೊಟ್ಟರೂ, ಪಡೆದರೂ</span><i>Up to one year in jail, or a fine, for giving or taking anything for a vote.</i></div>', BNS),

 (6.0, S + '<div class="b n">ಹಾಗಾದ್ರೆ ಉಚಿತ ಯೋಜನೆ ಕೊಡ್ತೀವಿ!<small>Fine, then we will give free schemes!</small></div>'
  '<div class="b m">ಒಳ್ಳೇದು. ದುಡ್ಡು ಎಲ್ಲಿಂದ?<small>Good. Where does the money come from?</small></div>'
  + stage('skeptic', 'smug') +
  '<div class="fact" style="border-color:#f2b705"><b style="color:#f2b705">₹51,286 ಕೋಟಿ</b><span>ಐದು ಗ್ಯಾರಂಟಿಗಳು, 2026-27 ಬಜೆಟ್</span><i>The five guarantee schemes, 2026-27 budget.</i></div>', PRS),

 (6.5, S + '<div class="k">ರಾಜ್ಯದ ಖಾತೆ</div>'
  '<div class="row"><small>2022-23 · ಆದಾಯ ಖಾತೆ ಹೆಚ್ಚುವರಿ</small>+₹13,496 ಕೋಟಿ</div>'
  '<div class="row"><small>2025-26 · ಆದಾಯ ಕೊರತೆ</small><b style="color:#ef5261">−₹25,449 ಕೋಟಿ</b></div>'
  '<div class="row"><small>ಗುತ್ತಿಗೆದಾರರಿಗೆ ಬಾಕಿ</small><b style="color:#ef5261">₹36,136 ಕೋಟಿ</b></div>'
  '<div class="en">From a revenue surplus to a deficit, and Rs 36,136 crore owed to contractors. 59% of the state\'s revenue already goes on salaries, pensions and interest.</div>', FIN),

 (5.5, S + '<div class="b m">ಸಹಾಯ ಬೇಕು. ಆದರೆ ಸಾಲದ ಮೇಲೆ ಕೊಟ್ರೆ, ಬಿಲ್ ನಮ್ಮ ಮಕ್ಕಳ ಹೆಸರಿಗೆ.<small>Help is needed. But paid for on loans, the bill goes in our children\'s name.</small></div>'
  + stage('firm', 'smug', 'point') +
  '<div class="en" style="margin-top:20px">Free schemes are a legal policy choice. Cash for votes is a crime. Both cost you.</div>', ''),

 (6.0, S + '<div class="k">ಅದೇ ಸಮಯದಲ್ಲಿ</div>'
  '<div class="row"><small>ಶಾಸಕರ ಮೂಲ ವೇತನ</small>₹25,000 → <b>₹80,000</b></div>'
  '<div class="row"><small>ಮರು ಆಯ್ಕೆಯಾದ 81 ಶಾಸಕರ ಸರಾಸರಿ ಆಸ್ತಿ</small>₹39.7 → <b>₹69.4 ಕೋಟಿ</b></div>'
  + stage('skeptic', 'smug') , PAY),

 (6.5, S + '<h1 style="font-size:96px">ಕೆಲಸ ತೋರಿಸಿ.<br><span style="color:#f2b705">ಆಮೇಲೆ ಮತ.</span></h1>'
  '<div class="en" style="margin-top:18px">Show me the work. Then you get my vote.</div>'
  + stage('firm', 'namaste', 'point', show_neta=False) +
  '<div class="mid" style="font-size:44px;margin:16px 0 0">ನಿಮ್ಮ ಶಾಸಕ ಏನು ಕೆಲಸ ತೋರಿಸಿದ್ದಾರೆ? ಕಾಮೆಂಟ್ ಮಾಡಿ.</div>'
  '<div class="url" style="margin-top:14px">jarvisss007.github.io/know-your-mla</div>', END),
]
OUT = 'mallanna1-kn.mp4'
FPS = 10
