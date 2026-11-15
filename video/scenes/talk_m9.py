# Mallanna Asks, Episode 9: "North and South" (ಉತ್ತರ ಮತ್ತು ದಕ್ಷಿಣ), talking-character format.
# Converted from scenes/ep9.py; every figure and source carried over unchanged from that file and its published description.
BPM = 96

METRO = 'Sources: Union Cabinet approval, January 2014; Karnataka cabinet, 22 May 2025 (The Week/PTI); BMRCL fare revision, 9 February 2025 (The Week)'
KK = 'Sources: State figures reported by The Week, 19 September 2024 (KKRDB 2013-14 to 2024-25); Karnataka cabinet, 22 May 2025'
CAG = 'Source: CAG Report No. 10 of 2022, Functioning of the Kalyana Karnataka Region Development Board'
END = 'Fictional characters. Metro costs are shared by the Centre, the state and loans. Every figure comes from a public record; if one is wrong, tell us.'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-2 s hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 9 · ಉತ್ತರ ಮತ್ತು ದಕ್ಷಿಣ', 'Mallanna Asks · Episode 9 · North and South'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="big r">2×</div><div class="h">ಒಂದು ಮೆಟ್ರೋ ಹಂತದ ವೆಚ್ಚ = ಏಳು ಜಿಲ್ಲೆಗಳ 12 ವರ್ಷದ ಹಂಚಿಕೆಯ ಎರಡು ಪಟ್ಟು</div>',
      card_en='<div class="big r">2×</div><div class="h">One metro phase costs twice what seven districts were allocated in 12 years</div>',
      lines=[('m', 'ಬೆಂಗಳೂರಿಗೆ ಮೆಟ್ರೋ ಸರಿ. ಕಲಬುರಗಿಯೂ ಕರ್ನಾಟಕನೇ ಸ್ವಾಮಿ!', 'A metro for Bengaluru, fine. Kalaburagi is Karnataka too, sir!')], src=KK),

 dict(kicker=('ನಮ್ಮ ಮೆಟ್ರೋ · ಹಂತ 2', 'Namma Metro · Phase 2'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>2014 · ಅನುಮೋದನೆ, ಗಡುವು 2020</small>₹26,405 ಕೋಟಿ</div><div class="row"><small>2025 · ಪರಿಷ್ಕೃತ, ಈಗ 2027</small><b class="r">₹40,425 ಕೋಟಿ</b></div><div class="row"><small>ಗರಿಷ್ಠ ಟಿಕೆಟ್ ದರ · ಫೆಬ್ರವರಿ 2025</small>₹60 → <b class="r">₹90</b></div>',
      card_en='<div class="row"><small>2014 · approved, due 2020</small>Rs 26,405 cr</div><div class="row"><small>2025 · revised, now due 2027</small><b class="r">Rs 40,425 cr</b></div><div class="row"><small>Top fare · February 2025</small>Rs 60 → <b class="r">Rs 90</b></div>',
      lines=[('k', 'ಮೆಟ್ರೋ ಎರಡನೇ ಹಂತ: ಗಡುವು 2020 ಇತ್ತು. ಈಗ 2027!', 'Metro Phase 2 was due in 2020. Now it is 2027!'),
             ('m', 'ವೆಚ್ಚ ನಲವತ್ತು ಸಾವಿರ ಕೋಟಿ ದಾಟಿತು. ಟಿಕೆಟ್ ತೊಂಬತ್ತು ರೂಪಾಯಿ!', 'The cost crossed 40,000 crore. The top fare is 90 rupees!')], src=METRO),

 dict(kicker=('ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ ಮಂಡಳಿ · 7 ಜಿಲ್ಲೆ · 12 ವರ್ಷ', 'Kalyana Karnataka board · 7 districts · 12 years'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="row"><small>ಹಂಚಿಕೆ, 2013-14 ರಿಂದ 2024-25</small>₹19,778 ಕೋಟಿ</div><div class="row"><small>ಬಿಡುಗಡೆ</small>₹13,229 ಕೋಟಿ</div><div class="row"><small>ಖರ್ಚು</small><b class="r">₹11,174 ಕೋಟಿ</b></div>',
      card_en='<div class="row"><small>Allocated, 2013-14 to 2024-25</small>Rs 19,778 cr</div><div class="row"><small>Released</small>Rs 13,229 cr</div><div class="row"><small>Spent</small><b class="r">Rs 11,174 cr</b></div>',
      lines=[('k', 'ಏಳು ಜಿಲ್ಲೆ, ಹನ್ನೆರಡು ವರ್ಷ. ಬಂದಿದ್ದು ಕಡಿಮೆ, ಖರ್ಚಾಗಿದ್ದು ಇನ್ನೂ ಕಡಿಮೆ!', 'Seven districts, twelve years. Less came, even less was spent!')], src=KK),

 dict(kicker=('ರಾಷ್ಟ್ರೀಯ ಲೆಕ್ಕಪರಿಶೋಧಕರು ಕಂಡದ್ದು', 'What the national auditor found'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಬಳಸದ ಕಾರಣ ಕಳೆದುಕೊಂಡ ನೆರವು</small><b class="r">₹387.52 ಕೋಟಿ</b></div><div class="row"><small>ರದ್ದಾದ ಕಾಮಗಾರಿಗಳು (₹738.65 ಕೋಟಿ)</small><b class="r">3,731</b></div><div class="sub">The government disputes the first figure.</div>',
      card_en='<div class="row"><small>Assistance lost because funds went unused</small><b class="r">Rs 387.52 cr</b></div><div class="row"><small>Works cancelled (Rs 738.65 cr)</small><b class="r">3,731</b></div><div class="sub">The government disputes the first figure.</div>',
      lines=[('m', 'ಸಿಎಜಿ ಪ್ರಕಾರ ಮೂರು ಸಾವಿರಕ್ಕೂ ಹೆಚ್ಚು ಕಾಮಗಾರಿ ರದ್ದು!', 'The auditor: over 3,000 works were cancelled!')], src=CAG),

 dict(kicker=('ಪ್ರತಿ ವ್ಯಕ್ತಿಯ ಆದಾಯ ಏರಿಕೆ · 2013-14 ರಿಂದ 2019-20', 'Growth in income per person · 2013-14 to 2019-20'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="row"><small>ಕರ್ನಾಟಕ</small>74.84%</div><div class="row"><small>ಕಲಬುರಗಿ</small><b class="r">47.96%</b></div><div class="row"><small>ಯಾದಗಿರಿ: ರಕ್ತಹೀನ ಮಕ್ಕಳು, ರಾಜ್ಯದಲ್ಲೇ ಅತಿ ಹೆಚ್ಚು</small><b class="r">76%</b></div>',
      card_en='<div class="row"><small>Karnataka</small>74.84%</div><div class="row"><small>Kalaburagi</small><b class="r">47.96%</b></div><div class="row"><small>Yadgir: children with anaemia, highest in the state</small><b class="r">76%</b></div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಬೆಂಗಳೂರಿನ ಮಕ್ಕಳಿಗೂ ನಮಗೂ ಬೇರೆ ಬೇರೆ ಕರ್ನಾಟಕನಾ?', 'Dad, is Bengaluru a different Karnataka from ours?')], src=CAG),

 # fairness beat
 dict(kicker=('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair'), m_expr='neutral', k_expr='ask',
      card_kn='<div class="h">2013ರ 371ಜೆ ಕಲಮು ಈ ಭಾಗಕ್ಕೆ ಮೀಸಲು ಉದ್ಯೋಗ, ಸೀಟು ಮತ್ತು ಸ್ವಂತ ಮಂಡಳಿ ಕೊಟ್ಟಿತು.</div><div class="sub">The rights came. The money did not fully come, and what came was not fully spent.</div>',
      card_en='<div class="h">Article 371J (2013) gave the region reserved jobs, college seats and its own board.</div><div class="sub">ಹಕ್ಕು ಸಿಕ್ಕಿತು. ಹಣ ಪೂರ್ತಿ ಬರಲಿಲ್ಲ, ಬಂದದ್ದೂ ಪೂರ್ತಿ ಖರ್ಚಾಗಲಿಲ್ಲ.</div>',
      lines=[('m', 'ಹಕ್ಕು ಸಿಕ್ಕಿತು. ಹಣ ಪೂರ್ತಿ ಬರಲಿಲ್ಲ, ಬಂದದ್ದೂ ಖರ್ಚಾಗಲಿಲ್ಲ.', 'Rights came. Money did not fully come, or get fully spent.')], src=END),

 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ಕೇಳಿ: ನಮ್ಮ ಜಿಲ್ಲೆಗೆ ಹಂಚಿದ ಹಣದಲ್ಲಿ ಎಷ್ಟು ಖರ್ಚಾಯಿತು? ಪಟ್ಟಿ ಕೊಡಿ.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Ask: how much of our district\'s allocation was actually spent? Publish the list.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಕೇಳಿ: ನಮ್ಮ ಜಿಲ್ಲೆಯ ಹಣದಲ್ಲಿ ಎಷ್ಟು ಖರ್ಚಾಯಿತು? ಪಟ್ಟಿ ಕೊಡಿ.', 'Ask: what did our district actually spend? Publish the list.')], src=END),

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
