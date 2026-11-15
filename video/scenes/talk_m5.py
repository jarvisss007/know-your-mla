# Mallanna Asks, Episode 5: "The water that never came" (ಬಾರದ ನೀರು)
# Talking-character version of scenes_mallanna5.py (+ en_wrap5.py). Every figure and source is carried over
# unchanged from that file and the published description in upload_all.json. Nothing new added.
BPM = 96

CAG_Y = 'Source: CAG Report No. 10 (Yettinahole project), tabled 29 January 2026'
CM27 = "Sources: CAG Report No. 10, 2026; Chief Minister's statement on the end-2027 target, 2026"
CAG_M = 'Source: CAG Report No. 2 of 2017 (Mysuru 24x7 water supply)'
UB = "Sources: Lok Sabha reply, August 2024; Chief Minister's statement, August 2026"
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-3 s hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 5 · ಬಾರದ ನೀರು', 'Mallanna Asks · Episode 5 · The water that never came'),
      hit=True, m_expr='skeptic', k_expr='sad',
      card_kn='<div class="big r">₹15,297</div><div class="h">ಕೋಟಿ ಖರ್ಚು, ಮಾರ್ಚ್ 2024ರ ವರೆಗೆ. ಎತ್ತಿನಹೊಳೆ ನೀರು ಇನ್ನೂ ಬಂದಿಲ್ಲ.</div>',
      card_en='<div class="big r">₹15,297</div><div class="h">crore spent by March 2024. Yettinahole water still has not come.</div>',
      lines=[('m', 'ಹೊಸ ಮಾತು ಹೇಳಿ ಸ್ವಾಮಿ. ನೀರಿನ ಭರವಸೆ 2012ರದ್ದು.', 'Say something new, sir. The water promise is from 2012.')], src=CAG_Y),

 dict(kicker=('ಎತ್ತಿನಹೊಳೆ ಕುಡಿಯುವ ನೀರಿನ ಯೋಜನೆ', 'Yettinahole drinking water project'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>2012 · ಅನುಮೋದಿತ ವೆಚ್ಚ</small>₹8,323 ಕೋಟಿ</div><div class="row"><small>2023 · ಪರಿಷ್ಕೃತ ವೆಚ್ಚ</small><b class="r">₹23,252 ಕೋಟಿ</b></div><div class="sub">ಸಿಎಜಿ: &ldquo;could not be made operational even after 12 years&rdquo;. ಸರ್ಕಾರದ ಹೊಸ ಭರವಸೆ: 2027ರ ಕೊನೆಗೆ ನೀರು.</div>',
      card_en='<div class="row"><small>2012 · approved cost</small>Rs 8,323 cr</div><div class="row"><small>2023 · revised cost</small><b class="r">Rs 23,252 cr</b></div><div class="sub">The auditor: &ldquo;could not be made operational even after 12 years&rdquo;. The government\'s new promise: water by the end of 2027.</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಕೋಲಾರ, ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಇನ್ನೂ ಕಾಯ್ತಿದೆ.', 'Dad, Kolar and Chikkaballapura are still waiting.')], src=CM27),

 dict(kicker=('ಮೈಸೂರು · 24x7 ನೀರು ಯೋಜನೆ', 'Mysuru · 24x7 water scheme'), hit=True, m_expr='skeptic', k_expr='sad',
      card_kn='<div class="big r">₹271.56</div><div class="h">ಕೋಟಿ ಖರ್ಚು. 24x7 ನೀರು ಬರಲಿಲ್ಲ.</div><div class="sub">ಯೋಜನೆಯ ವ್ಯಾಪ್ತಿ 69 ವಲಯದಿಂದ 47ಕ್ಕೆ ಇಳಿಯಿತು.</div>',
      card_en='<div class="big r">₹271.56</div><div class="h">crore spent. No 24x7 water.</div><div class="sub">The coverage area was cut from 69 zones to 47.</div>',
      lines=[('m', 'ಮೈಸೂರಿಗೆ ದಿನದ ಇಪ್ಪತ್ನಾಲ್ಕು ಗಂಟೆ ನೀರು ಅಂದ್ರು. ಬರಲೇ ಇಲ್ಲ.', 'Mysuru was promised water round the clock. It never came.')], src=CAG_M),

 dict(kicker=('ಭದ್ರಾ ಮೇಲ್ದಂಡೆ · ಚಿತ್ರದುರ್ಗ, ದಾವಣಗೆರೆ', 'Upper Bhadra · Chitradurga, Davanagere'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>2003 · ಮೊದಲ ಹಂತ</small>₹2,813 ಕೋಟಿ</div><div class="row"><small>2020 · ಪರಿಷ್ಕೃತ</small><b class="r">₹21,474 ಕೋಟಿ</b></div><div class="sub">2023-24 ಕೇಂದ್ರ ಬಜೆಟ್‌ನಲ್ಲಿ ₹5,300 ಕೋಟಿ ಘೋಷಣೆ. ಯಾವ ಕೇಂದ್ರ ಯೋಜನೆಯಲ್ಲೂ ಇಲ್ಲ ಎಂದು ಕೇಂದ್ರ. ಹಣ ಬರಲೇ ಇಲ್ಲ ಎಂದು ರಾಜ್ಯ.</div>',
      card_en='<div class="row"><small>2003 · stage I</small>Rs 2,813 cr</div><div class="row"><small>2020 · revised</small><b class="r">Rs 21,474 cr</b></div><div class="sub">Rs 5,300 cr announced in the 2023-24 Union Budget. The Centre says no central scheme covers it. The state says the money never came.</div>',
      lines=[('k', 'ಕೇಂದ್ರ ಒಂದು ಹೇಳುತ್ತೆ. ರಾಜ್ಯ ಇನ್ನೊಂದು ಹೇಳುತ್ತೆ.', 'The Centre says one thing. The state says another.')], src=UB),

 # fairness
 dict(kicker=('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair'), m_expr='firm', k_expr='sad',
      card_kn='<div class="h">2012ರಿಂದ ಪ್ರತಿ ಸರ್ಕಾರವೂ ಎತ್ತಿನಹೊಳೆಯನ್ನು ನಡೆಸಿದೆ.</div><div class="sub">ಬಿಜೆಪಿ · ಕಾಂಗ್ರೆಸ್ · ಸಮ್ಮಿಶ್ರ</div>',
      card_en='<div class="h">Every government since 2012 has run Yettinahole.</div><div class="sub">BJP · Congress · Coalition</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ನೀರು ಬರಲ್ಲ. ಬಿಲ್ ಮಾತ್ರ ಬರುತ್ತೆ.', 'Dad, the water never comes. Only the bill does.')], src=CAG_Y),

 dict(kicker=('ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ', "Kaveri's question"), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ನೀರು ನಮ್ಮ ಊರಿಗೆ ಯಾವಾಗ? ಬರೆದು ಕೊಡಿ.</div><div class="sub">ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ. ಅವರನ್ನು ಇಲ್ಲಿ ನೋಡಿ:</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">When will the water reach our town? Put it in writing.</div><div class="sub">Ask your MLA. Look them up:</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ನೀರು ನಮ್ಮ ಊರಿಗೆ ಯಾವಾಗ? ಬರೆದು ಕೊಡಿ.', 'When will the water reach our town? Put it in writing.')], src=ASK),

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
