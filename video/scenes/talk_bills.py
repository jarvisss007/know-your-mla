# Mallanna Asks (topic Short): unpaid contractor bills. Talking-character version of scenes_bills.py.
# Facts, figures and sources carried over unchanged from the old scene file. The English lines translate its Kannada.
BPM = 96

FIN = 'Source: Finance Department note, 17 September 2026'
CAG = 'Source: CAG State Finances Audit Report'
PRS = 'Source: PRS Legislative Research, Karnataka Budget Analysis 2026-27'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಗುತ್ತಿಗೆದಾರರ ಬಾಕಿ', 'Mallanna Asks · Unpaid bills'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r" style="font-size:150px">₹36,136<small> ಕೋಟಿ</small></div><div class="h">ಗುತ್ತಿಗೆದಾರರಿಗೆ ಸರ್ಕಾರದ ಬಾಕಿ</div>',
      card_en='<div class="big r" style="font-size:150px">Rs 36,136<small> cr</small></div><div class="h">the state owes contractors in unpaid bills</div>',
      lines=[('m', 'ಗುತ್ತಿಗೆದಾರರಿಗೆ ಸರ್ಕಾರದ ಬಾಕಿ ಮೂವತ್ತಾರು ಸಾವಿರ ಕೋಟಿಗೂ ಹೆಚ್ಚು!', 'The state owes contractors over 36,000 crore!')], src=FIN),

 dict(kicker=('ಸರ್ಕಾರದ ಸ್ವಂತ ಮಾತು', "The government's own words"), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="h">ಹೊಸ ಯೋಜನೆ ಆರಂಭಿಸಬೇಡಿ ಎಂದು ಹಣಕಾಸು ಇಲಾಖೆ ಎಚ್ಚರಿಸಿದೆ.</div><div class="row"><small>ಆರಂಭಿಸಿದ ಕಾಮಗಾರಿ ಮುಗಿಸಲು</small><b class="r">₹2 ಲಕ್ಷ ಕೋಟಿ+</b></div>',
      card_en='<div class="h">The Finance Department warned against starting new projects.</div><div class="row"><small>To finish works already started</small><b class="r">Rs 2 lakh cr+</b></div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಹೊಸ ಯೋಜನೆ ಶುರು ಮಾಡಬೇಡಿ ಅಂತ ಹಣಕಾಸು ಇಲಾಖೆಯೇ ಹೇಳಿದೆ.', 'Dad, the Finance Department itself warned: start no new projects.'),
             ('m', 'ಶುರುವಾದ ಕೆಲಸ ಮುಗಿಸೋಕೆ ಎರಡು ಲಕ್ಷ ಕೋಟಿಗೂ ಹೆಚ್ಚು ಬೇಕು.', 'Finishing works already started costs over 2 lakh crore.')], src=FIN),

 dict(kicker=('ಅಪೂರ್ಣ · ಮಾರ್ಚ್ 2024', 'Incomplete · March 2024'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">3,140</div><div class="h">ಯೋಜನೆಗಳು ಅಪೂರ್ಣ, ಮಾರ್ಚ್ 2024</div>',
      card_en='<div class="big r">3,140</div><div class="h">projects incomplete, March 2024</div>',
      lines=[('k', 'ಸಿಎಜಿ ಲೆಕ್ಕದಲ್ಲಿ ಮೂರು ಸಾವಿರದ ನೂರ ನಲವತ್ತು ಯೋಜನೆ ಅಪೂರ್ಣ.', 'The national auditor counted 3,140 projects incomplete.')], src=CAG),

 dict(kicker=('ಆದಾಯ ಖಾತೆ', 'Revenue account'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>2022-23 · ಹೆಚ್ಚುವರಿ</small><b>+₹13,496 ಕೋಟಿ</b></div><div class="row"><small>2025-26 · ಕೊರತೆ</small><b class="r">−₹25,449 ಕೋಟಿ</b></div>',
      card_en='<div class="row"><small>2022-23 · surplus</small><b>+Rs 13,496 cr</b></div><div class="row"><small>2025-26 · deficit</small><b class="r">−Rs 25,449 cr</b></div>',
      lines=[('m', 'ಆದಾಯ ಖಾತೆ ಹೆಚ್ಚುವರಿಯಲ್ಲಿತ್ತು. ಈಗ ಇಪ್ಪತ್ತೈದು ಸಾವಿರ ಕೋಟಿ ಕೊರತೆ!', 'The revenue account had a surplus. Now a deficit of over 25,000 crore!')], src=PRS),

 # fairness: whose dues are these?
 dict(kicker=('ಬಾಕಿ ಯಾರದ್ದು?', 'Whose dues are these?'), m_expr='neutral', k_expr='ask',
      card_kn='<div class="h">₹20,000 ಕೋಟಿ ಹಿಂದಿನ ಬಿಜೆಪಿ ಸರ್ಕಾರದ್ದು ಎಂದು ಮಾಜಿ ಮುಖ್ಯಮಂತ್ರಿ ಹೇಳುತ್ತಾರೆ.</div><div class="sub">ಅಧಿಕೃತ ಪಟ್ಟಿ ಪ್ರಕಟವಾಗಿಲ್ಲ. ಯಾರೂ ಪರಿಶೀಲಿಸಲು ಆಗುವುದಿಲ್ಲ.</div>',
      card_en='<div class="h">The former Chief Minister says Rs 20,000 crore of it dates from the BJP government.</div><div class="sub">No official list has been published, so nobody can check.</div>',
      lines=[('k', 'ಇಪ್ಪತ್ತು ಸಾವಿರ ಕೋಟಿ ಹಿಂದಿನ ಬಿಜೆಪಿ ಸರ್ಕಾರದ್ದು ಅಂತ ಮಾಜಿ ಸಿಎಂ ಹೇಳ್ತಾರೆ.', 'The former Chief Minister says 20,000 crore is from the BJP government.'),
             ('m', 'ಅಧಿಕೃತ ಪಟ್ಟಿ ಪ್ರಕಟವಾಗಿಲ್ಲ. ಯಾರೂ ಪರಿಶೀಲಿಸೋಕೆ ಆಗಲ್ಲ.', 'No official list is published, so nobody can check.')], src=''),

 # ask
 dict(kicker=('ನೀವು ಏನು ಕೇಳಬಹುದು', 'What you can ask'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ಯಾರಿಗೆ ಎಷ್ಟು ಬಾಕಿ, ಯಾವ ಕ್ರಮದಲ್ಲಿ ಪಾವತಿ: ಸರ್ಕಾರ ಪ್ರಕಟಿಸುತ್ತದೆಯೇ?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Will the government publish who is owed, and in what order they will be paid?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಯಾರಿಗೆ ಎಷ್ಟು ಬಾಕಿ, ಯಾವ ಕ್ರಮದಲ್ಲಿ ಪಾವತಿ? ಸರ್ಕಾರ ಪ್ರಕಟಿಸುತ್ತಾ?', 'Who is owed, and in what order will they be paid? Will they publish it?')], src=ASK),

 # chorus: the series theme, chanted on the beat
 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]

_TAIL = ('Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
         'Sources: Finance Department note, 17 September 2026; CAG State Finances Audit Report; '
         'PRS Legislative Research, Karnataka Budget Analysis 2026-27\n\n'
         'Every figure comes from a public record. If one is wrong, tell us and we will correct it. Music: original.\n\n')
META = {
 'kn': {'title': 'ಗುತ್ತಿಗೆದಾರರಿಗೆ ₹36,136 ಕೋಟಿ ಬಾಕಿ: ಯಾರಿಗೆ, ಯಾವಾಗ? | ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #Shorts',
        'description': ('ಮಲ್ಲಣ್ಣ ಮತ್ತು ಕಾವೇರಿ ಸರ್ಕಾರದ ಬಾಕಿ ಬಿಲ್‌ಗಳನ್ನು ನೋಡುತ್ತಾರೆ.\n'
                         'ಯಾರಿಗೆ ಎಷ್ಟು ಬಾಕಿ, ಯಾವ ಕ್ರಮದಲ್ಲಿ ಪಾವತಿ: ಸರ್ಕಾರ ಪ್ರಕಟಿಸುತ್ತದೆಯೇ?\n\n'
                         '• ಗುತ್ತಿಗೆದಾರರಿಗೆ ಸರ್ಕಾರದ ಬಾಕಿ: ₹36,136 ಕೋಟಿ\n'
                         '• ಹೊಸ ಯೋಜನೆ ಆರಂಭಿಸಬೇಡಿ ಎಂದು ಹಣಕಾಸು ಇಲಾಖೆ ಎಚ್ಚರಿಸಿದೆ; ಆರಂಭಿಸಿದ ಕಾಮಗಾರಿ ಮುಗಿಸಲು ₹2 ಲಕ್ಷ ಕೋಟಿಗೂ ಹೆಚ್ಚು\n'
                         '• ಮಾರ್ಚ್ 2024: 3,140 ಯೋಜನೆಗಳು ಅಪೂರ್ಣ (ಸಿಎಜಿ)\n'
                         '• ಆದಾಯ ಖಾತೆ: 2022-23ರಲ್ಲಿ +₹13,496 ಕೋಟಿ ಹೆಚ್ಚುವರಿ → 2025-26ರಲ್ಲಿ −₹25,449 ಕೋಟಿ ಕೊರತೆ\n\n'
                         'ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ: ₹20,000 ಕೋಟಿ ಹಿಂದಿನ ಬಿಜೆಪಿ ಸರ್ಕಾರದ್ದು ಎಂದು ಮಾಜಿ ಮುಖ್ಯಮಂತ್ರಿ ಹೇಳುತ್ತಾರೆ. ಅಧಿಕೃತ ಪಟ್ಟಿ ಪ್ರಕಟವಾಗಿಲ್ಲ, ಯಾರೂ ಪರಿಶೀಲಿಸಲು ಆಗುವುದಿಲ್ಲ.\n\n'
                         + _TAIL + '#MallannaAsks #Karnataka #ಕನ್ನಡ')},
 'en': {'title': 'Karnataka owes contractors Rs 36,136 crore. Who gets paid first? | Mallanna Asks #Shorts',
        'description': ("Mallanna and Kaveri look at the state's unpaid bills.\n"
                         'Will the government publish who is owed, and in what order they will be paid?\n\n'
                         '• The state owes contractors Rs 36,136 crore in unpaid bills\n'
                         '• The Finance Department warned against starting new projects; finishing works already started costs over Rs 2 lakh crore\n'
                         '• March 2024: 3,140 projects incomplete (CAG)\n'
                         '• Revenue account: surplus of Rs 13,496 crore in 2022-23 → deficit of Rs 25,449 crore in 2025-26\n\n'
                         'To be fair: the former Chief Minister says Rs 20,000 crore of it dates from the BJP government. No official list has been published, so nobody can check.\n\n'
                         + _TAIL + '#MallannaAsks #Karnataka')},
}

# The owner's recorded chorus on every Kannada episode.
REC = {'kn': {'chorus': 'voice/ep11/chorus.wav'}}
