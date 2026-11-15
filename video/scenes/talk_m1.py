# Mallanna Asks, Episode 1: "Show me the work, then my vote" (ಕೆಲಸ ತೋರಿಸಿ, ಆಮೇಲೆ ಮತ)
# Talking-character version of scenes_mallanna1.py (+ en_wrap1.py). Every figure and source is carried over
# unchanged from that file and the published description in upload_all.json. Nothing new added.
BPM = 96

EC = 'Source: Election Commission figures, 8 May 2023 (reported by Business Today and Udayavani)'
BNS = 'Source: Bharatiya Nyaya Sanhita, 2023, sections 170 and 173. A promise of public policy is not bribery under the law.'
PRS = 'Source: PRS Legislative Research, Karnataka Budget Analysis 2026-27'
FIN = 'Sources: PRS Legislative Research; Karnataka Finance Department note, 17 September 2026'
PAY = "Sources: Karnataka Legislative Assembly, 2022 and 21 March 2025; MLAs' own sworn affidavits, 2018 and 2023"
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-3 s hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 1 · ಕೆಲಸ ತೋರಿಸಿ, ಆಮೇಲೆ ಮತ', 'Mallanna Asks · Episode 1 · Show me the work, then my vote'),
      hit=True, m_expr='skeptic', k_expr='sad',
      card_kn='<div class="big r">₹375.61</div><div class="h">ಕೋಟಿ ಮೌಲ್ಯದ ನಗದು, ಮದ್ಯ, ಚಿನ್ನ, ಉಡುಗೊರೆ ವಶ · 2023 ಚುನಾವಣೆ</div><div class="sub">2018ರ 4.5 ಪಟ್ಟು</div>',
      card_en='<div class="big r">₹375.61</div><div class="h">crore of cash, liquor, gold and gifts seized in the 2023 election</div><div class="sub">4.5 times 2018</div>',
      lines=[('m', 'ಐದು ವರ್ಷ ಆಯ್ತು ಸ್ವಾಮಿ. ಈಗ ಉಡುಗೊರೆ ಚೀಲ ತಂದ್ರಾ?', 'Five years, sir. And now you bring a bag of gifts?')], src=EC),

 dict(kicker=('ಕಾನೂನು ಏನು ಹೇಳುತ್ತೆ', 'What the law says'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="big r">1<small> ವರ್ಷ ಜೈಲು</small></div><div class="h">ಅಥವಾ ದಂಡ: ಮತಕ್ಕಾಗಿ ಕೊಟ್ಟರೂ, ಪಡೆದರೂ</div>',
      card_en='<div class="big r">1<small> year in jail</small></div><div class="h">or a fine, for giving or taking anything for a vote</div>',
      lines=[('m', 'ಕೊಡೋದೂ ಅಪರಾಧ. ತಗೊಳ್ಳೋದೂ ಅಪರಾಧ.', 'Giving it is a crime. Taking it is a crime.')], src=BNS),

 dict(kicker=('ಐದು ಗ್ಯಾರಂಟಿಗಳು · 2026-27 ಬಜೆಟ್', 'The five guarantees · 2026-27 budget'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="big">₹51,286</div><div class="h">ಕೋಟಿ: ಐದು ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳ ವೆಚ್ಚ</div>',
      card_en='<div class="big">₹51,286</div><div class="h">crore: the cost of the five guarantee schemes</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಈಗ ಉಚಿತ ಯೋಜನೆ ಕೊಡ್ತೀವಿ ಅಂತಾರೆ.', 'Dad, now they say they will give free schemes.'),
             ('m', 'ಒಳ್ಳೇದು. ದುಡ್ಡು ಎಲ್ಲಿಂದ?', 'Good. Where does the money come from?')], src=PRS),

 dict(kicker=('ರಾಜ್ಯದ ಖಾತೆ', "The state's accounts"), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="row"><small>2022-23 · ಆದಾಯ ಖಾತೆ ಹೆಚ್ಚುವರಿ</small>+₹13,496 ಕೋಟಿ</div><div class="row"><small>2025-26 · ಆದಾಯ ಕೊರತೆ</small><b class="r">−₹25,449 ಕೋಟಿ</b></div><div class="row"><small>ಗುತ್ತಿಗೆದಾರರಿಗೆ ಬಾಕಿ</small><b class="r">₹36,136 ಕೋಟಿ</b></div><div class="sub">ಆದಾಯದ 59% ಸಂಬಳ, ಪಿಂಚಣಿ, ಬಡ್ಡಿಗೇ ಹೋಗುತ್ತದೆ.</div>',
      card_en='<div class="row"><small>2022-23 · revenue surplus</small>+Rs 13,496 cr</div><div class="row"><small>2025-26 · revenue deficit</small><b class="r">−Rs 25,449 cr</b></div><div class="row"><small>Owed to contractors</small><b class="r">Rs 36,136 cr</b></div><div class="sub">59% of revenue already goes on salaries, pensions and interest.</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಉಳಿತಾಯದ ಖಾತೆ ಈಗ ಕೊರತೆಯಲ್ಲಿದೆ!', 'Dad, the surplus has turned into a deficit!')], src=FIN),

 # fairness / contrast
 dict(kicker=('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ಉಚಿತ ಯೋಜನೆ ಕಾನೂನುಬದ್ಧ ನೀತಿ. ಮತಕ್ಕೆ ಹಣ ಅಪರಾಧ.</div><div class="sub">ಎರಡರ ಬಿಲ್ಲೂ ನಿಮಗೇ.</div>',
      card_en='<div class="h">Free schemes are a legal policy choice. Cash for votes is a crime.</div><div class="sub">Both cost you.</div>',
      lines=[('m', 'ಸಹಾಯ ಬೇಕು. ಆದರೆ ಸಾಲದ ಮೇಲೆ ಕೊಟ್ರೆ, ಬಿಲ್ ನಮ್ಮ ಮಕ್ಕಳ ಹೆಸರಿಗೆ.', "Help is needed. But paid on loans, the bill goes in our children's name.")], src=BNS),

 dict(kicker=('ಅದೇ ಸಮಯದಲ್ಲಿ', 'Meanwhile'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಶಾಸಕರ ಮೂಲ ವೇತನ</small>₹25,000 → <b>₹80,000</b></div><div class="row"><small>ಮರು ಆಯ್ಕೆಯಾದ 81 ಶಾಸಕರ ಸರಾಸರಿ ಆಸ್ತಿ</small>₹39.7 → <b>₹69.4 ಕೋಟಿ</b></div>',
      card_en='<div class="row"><small>MLAs\' basic pay</small>Rs 25,000 → <b>Rs 80,000</b></div><div class="row"><small>Average assets of 81 re-elected MLAs</small>Rs 39.7 → <b>Rs 69.4 cr</b></div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಅದೇ ಸಮಯದಲ್ಲಿ ಶಾಸಕರ ಸಂಬಳ, ಆಸ್ತಿ ಎರಡೂ ಏರಿದೆ!', "Dad, meanwhile the MLAs' pay and assets both went up!")], src=PAY),

 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='smile',
      card_kn='<div class="h">ನಿಮ್ಮ ಶಾಸಕ ಏನು ಕೆಲಸ ತೋರಿಸಿದ್ದಾರೆ? ಕಾಮೆಂಟ್ ಮಾಡಿ.</div><div class="sub">ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಇಲ್ಲಿ ನೋಡಿ:</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">What work has your MLA shown you? Tell us in the comments.</div><div class="sub">Look them up:</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಕೆಲಸ ತೋರಿಸಿ. ಆಮೇಲೆ ಮತ.', 'Show me the work. Then you get my vote.')], src=ASK),

 # chorus: the series theme, chanted on the beat
 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]

# The owner's recorded chorus on every Kannada episode.
REC = {'kn': {'chorus': 'voice/ep11/chorus.wav'}}
