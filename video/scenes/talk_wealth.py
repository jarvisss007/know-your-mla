# Mallanna Asks (topic Short): MLA wealth. Talking-character version of scenes_wealth.py / scenes_wealth_en.py.
# Facts, figures and sources carried over unchanged from the old scene files (sworn affidavits, ADR / myneta.info).
BPM = 96

AFF = "Source: MLAs' own sworn election affidavits, 2018 and 2023 (ADR / myneta.info)"
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಶಾಸಕರ ಆಸ್ತಿ', 'Mallanna Asks · MLA wealth'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">97%</div><div class="h">ಶಾಸಕರು ಕೋಟ್ಯಾಧಿಪತಿಗಳು</div><div class="sub">204 / 210 · affidavits in the archive</div>',
      card_en='<div class="big r">97%</div><div class="h">of MLAs are crorepatis</div><div class="sub">204 of the 210 whose affidavits are in the archive</div>',
      lines=[('m', 'ತೊಂಬತ್ತೇಳು ಪರ್ಸೆಂಟ್ ಶಾಸಕರು ಕೋಟ್ಯಾಧಿಪತಿಗಳು!', '97 percent of our MLAs are crorepatis!')], src=AFF),

 dict(kicker=('ಘೋಷಿತ ಆಸ್ತಿ · 2023', 'Declared assets · 2023'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಮಧ್ಯದ ಶಾಸಕ</small><b>₹18 ಕೋಟಿ</b></div><div class="row"><small>₹100 ಕೋಟಿಗೂ ಹೆಚ್ಚು</small><b class="r">29 ಶಾಸಕರು</b></div>',
      card_en='<div class="row"><small>The middle MLA</small><b>Rs 18 crore</b></div><div class="row"><small>Over Rs 100 crore</small><b class="r">29 MLAs</b></div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಮಧ್ಯದ ಶಾಸಕನ ಆಸ್ತಿ ಹದಿನೆಂಟು ಕೋಟಿ!', 'Dad, the middle MLA declares 18 crore!'),
             ('m', 'ಇಪ್ಪತ್ತೊಂಬತ್ತು ಜನರದ್ದು ನೂರು ಕೋಟಿಗೂ ಹೆಚ್ಚು.', '29 of them declare over 100 crore.')], src=AFF),

 dict(kicker=('2018, 2023 ಎರಡರಲ್ಲೂ ಗೆದ್ದ 81 ಶಾಸಕರು', '81 MLAs who won in both 2018 and 2023'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>2018 · ಸರಾಸರಿ ಆಸ್ತಿ</small>₹39.7 ಕೋಟಿ</div><div class="row"><small>2023 · ಸರಾಸರಿ ಆಸ್ತಿ</small><b class="r">₹69.4 ಕೋಟಿ</b></div>',
      card_en='<div class="row"><small>2018 · average assets</small>Rs 39.7 cr</div><div class="row"><small>2023 · average assets</small><b class="r">Rs 69.4 cr</b></div>',
      lines=[('k', 'ಎರಡು ಸಲ ಗೆದ್ದವರ ಸರಾಸರಿ ಆಸ್ತಿ ಸುಮಾರು ನಲವತ್ತರಿಂದ ಎಪ್ಪತ್ತು ಕೋಟಿ!', 'Those who won twice: average assets from about 40 to 70 crore!')], src=AFF),

 dict(kicker=('ಒಂದೇ ಅವಧಿಯಲ್ಲಿ', 'In one term'), hit=True, m_expr='skeptic', k_expr='sad',
      card_kn='<div class="big r">36<small> / 81</small></div><div class="h">ಶಾಸಕರ ಆಸ್ತಿ ಕನಿಷ್ಠ ದುಪ್ಪಟ್ಟಾಯಿತು</div>',
      card_en='<div class="big r">36<small> / 81</small></div><div class="h">at least doubled their declared wealth</div>',
      lines=[('m', 'ಐದು ವರ್ಷದಲ್ಲಿ ಮೂವತ್ತಾರು ಜನರ ಆಸ್ತಿ ಕನಿಷ್ಠ ದುಪ್ಪಟ್ಟು!', 'In five years, 36 of them at least doubled it!')], src=AFF),

 # fairness
 dict(kicker=('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair'), m_expr='neutral', k_expr='ask',
      card_kn='<div class="h">ಏರಿಕೆಯ ಬಹುಪಾಲು ಹಳೆಯ ಜಮೀನಿನ ಹೆಚ್ಚಿದ ಮೌಲ್ಯ. ಅದು ಕಾನೂನುಬಾಹಿರವಲ್ಲ.</div><div class="sub">ಎಲ್ಲ ಪಕ್ಷಗಳಲ್ಲೂ ಇದೇ ಕಥೆ.</div>',
      card_en='<div class="h">Much of the rise is land they already owned, now valued higher. That is legal.</div><div class="sub">And it is the same in every party.</div>',
      lines=[('k', 'ಆದರೆ ಅಪ್ಪಾ, ಏರಿಕೆಯ ಬಹುಪಾಲು ಹಳೆಯ ಜಮೀನಿನ ಹೆಚ್ಚಿದ ಬೆಲೆ.', 'But Dad, much of the rise is land they already owned, now valued higher.'),
             ('m', 'ಹೌದು, ಅದು ಕಾನೂನುಬಾಹಿರವಲ್ಲ. ಎಲ್ಲ ಪಕ್ಷದಲ್ಲೂ ಇದೇ ಕಥೆ.', 'True, that is legal. And it is the same in every party.')], src=''),

 # ask
 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ನಿಮ್ಮ ಶಾಸಕರ ಆಸ್ತಿ ಎಷ್ಟು ಏರಿತು? ಅವರದೇ ಪ್ರಮಾಣಪತ್ರದಲ್ಲಿ ನೋಡಿ.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">How much did your MLA\'s wealth grow? Check their own sworn affidavit.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ನಿಮ್ಮ ಆಸ್ತಿ ಐದು ವರ್ಷದಲ್ಲಿ ದುಪ್ಪಟ್ಟಾಯಿತಾ?', 'Did your assets double in five years?'),
             ('k', 'ನಿಮ್ಮ ಶಾಸಕರದ್ದು ನೋಡಿ, ಅವರದೇ ಪ್ರಮಾಣಪತ್ರದಲ್ಲಿ.', "Check your MLA's, in their own sworn affidavit.")], src=ASK),

 # chorus: the series theme, chanted on the beat
 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]

_TAIL = ('Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
         'Sources: ' + AFF[len('Source: '):] + '\n\n'
         'Every figure comes from a public record. If one is wrong, tell us and we will correct it. Music: original.\n\n')
META = {
 'kn': {'title': '97% ಶಾಸಕರು ಕೋಟ್ಯಾಧಿಪತಿಗಳು: ಐದು ವರ್ಷದಲ್ಲಿ ಆಸ್ತಿ ದುಪ್ಪಟ್ಟು? | ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #Shorts',
        'description': ('ಮಲ್ಲಣ್ಣ ಮತ್ತು ಕಾವೇರಿ ಕರ್ನಾಟಕದ ಶಾಸಕರ ಘೋಷಿತ ಆಸ್ತಿಯನ್ನು ನೋಡುತ್ತಾರೆ.\n'
                         'ಎಲ್ಲ ಅಂಕಿಗಳೂ ಶಾಸಕರ ಸ್ವಂತ ಚುನಾವಣಾ ಪ್ರಮಾಣಪತ್ರಗಳಿಂದ.\n\n'
                         '• 97% ಶಾಸಕರು ಕೋಟ್ಯಾಧಿಪತಿಗಳು (ದಾಖಲೆಯಲ್ಲಿರುವ 210ರಲ್ಲಿ 204)\n'
                         '• 2023: ಮಧ್ಯದ ಶಾಸಕನ ಆಸ್ತಿ ಸುಮಾರು ₹18 ಕೋಟಿ; 29 ಶಾಸಕರ ಆಸ್ತಿ ₹100 ಕೋಟಿಗೂ ಹೆಚ್ಚು\n'
                         '• 2018 ಮತ್ತು 2023 ಎರಡರಲ್ಲೂ ಗೆದ್ದ 81 ಶಾಸಕರ ಸರಾಸರಿ ಆಸ್ತಿ: ₹39.7 ಕೋಟಿ → ₹69.4 ಕೋಟಿ\n'
                         '• ಆ 81ರಲ್ಲಿ 36 ಶಾಸಕರ ಆಸ್ತಿ ಒಂದೇ ಅವಧಿಯಲ್ಲಿ ಕನಿಷ್ಠ ದುಪ್ಪಟ್ಟಾಯಿತು\n\n'
                         'ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ: ಏರಿಕೆಯ ಬಹುಪಾಲು ಹಳೆಯ ಜಮೀನಿನ ಹೆಚ್ಚಿದ ಮೌಲ್ಯ. ಅದು ಕಾನೂನುಬಾಹಿರವಲ್ಲ. ಎಲ್ಲ ಪಕ್ಷಗಳಲ್ಲೂ ಇದೇ ಕಥೆ.\n\n'
                         + _TAIL + '#MallannaAsks #Karnataka #ಕನ್ನಡ')},
 'en': {'title': "97% of Karnataka's MLAs are crorepatis. Did yours double? | Mallanna Asks #Shorts",
        'description': ("Mallanna and Kaveri look at what Karnataka's MLAs declared they own.\n"
                         'Every figure is from the MLAs\' own sworn election affidavits.\n\n'
                         '• 97% of MLAs are crorepatis (204 of the 210 whose affidavits are in the archive)\n'
                         '• 2023: the middle MLA declares about Rs 18 crore; 29 MLAs declare more than Rs 100 crore\n'
                         '• 81 MLAs who won in both 2018 and 2023: average declared assets Rs 39.7 crore → Rs 69.4 crore\n'
                         '• 36 of those 81 at least doubled their declared wealth in one term\n\n'
                         'To be fair: much of the rise is land they already owned, now valued higher. That is legal. And it is the same in every party.\n\n'
                         + _TAIL + '#MallannaAsks #Karnataka')},
}

# The owner's recorded chorus on every Kannada episode.
REC = {'kn': {'chorus': 'voice/ep11/chorus.wav'}}
