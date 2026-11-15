# Mallanna Asks (topic Short): Bengaluru without an elected council. Talking-character version of scenes_bengaluru.py.
# Facts, figures and sources carried over unchanged from the old scene file. The English lines translate its Kannada.
BPM = 96

TERM = 'Source: BBMP council term ended 10 September 2020'
SC = 'Source: Supreme Court orders on the Greater Bengaluru corporation elections, 2026'
GRANT = 'Source: State government figures on Bengaluru development grants'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಬೆಂಗಳೂರು', 'Mallanna Asks · Bengaluru'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">6<small> ವರ್ಷ</small></div><div class="h">ಚುನಾಯಿತ ಪಾಲಿಕೆ ಇಲ್ಲ</div><div class="sub">ಸೆಪ್ಟೆಂಬರ್ 2020 ರಿಂದ</div>',
      card_en='<div class="big r">6<small> years</small></div><div class="h">with no elected city council</div><div class="sub">since September 2020</div>',
      lines=[('m', 'ಬೆಂಗಳೂರಿಗೆ ಆರು ವರ್ಷದಿಂದ ಚುನಾಯಿತ ಪಾಲಿಕೆಯೇ ಇಲ್ಲ!', 'Bengaluru has had no elected council for six years!')], src=TERM),

 dict(kicker=('ಸೆಪ್ಟೆಂಬರ್ 2020 ರಿಂದ', 'Since September 2020'), m_expr='skeptic', k_expr='ask',
      card_kn='<div class="h">ಭಾರತದ ಟೆಕ್ ರಾಜಧಾನಿ.</div><div class="h">ವಾರ್ಡ್‌ಗೆ ಕಾರ್ಪೊರೇಟರ್ ಇಲ್ಲ.</div>',
      card_en='<div class="h">India\'s tech capital.</div><div class="h">No corporator for any ward.</div>',
      lines=[('k', 'ಭಾರತದ ಟೆಕ್ ರಾಜಧಾನಿ. ಆದ್ರೆ ಯಾವ ವಾರ್ಡ್‌ಗೂ ಕಾರ್ಪೊರೇಟರ್ ಇಲ್ಲ.', "India's tech capital, and no ward has a corporator.")], src=TERM),

 dict(kicker=('ಹಣ ಮಾತ್ರ ಹರಿಯುತ್ತಲೇ ಇದೆ', 'The money keeps flowing'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>ವಾರ್ಷಿಕ ಅಭಿವೃದ್ಧಿ ಅನುದಾನ · ಮೊದಲು</small>₹3,000 ಕೋಟಿ</div><div class="row"><small>ಈಗ</small><b class="r">₹7,000 ಕೋಟಿ</b></div>',
      card_en='<div class="row"><small>Annual development grant · before</small>Rs 3,000 cr</div><div class="row"><small>Now</small><b class="r">Rs 7,000 cr</b></div>',
      lines=[('m', 'ಆದ್ರೆ ನಗರದ ಅನುದಾನ ಮೂರು ಸಾವಿರದಿಂದ ಏಳು ಸಾವಿರ ಕೋಟಿಗೆ ಏರಿದೆ.', "But the city's yearly grant rose from 3,000 to 7,000 crore."),
             ('k', 'ಉತ್ತರ ಕೊಡೋಕೆ ಒಬ್ಬ ಕಾರ್ಪೊರೇಟರೂ ಇಲ್ಲ.', 'And no elected councillor to answer for it.')], src=GRANT),

 # fairness: both governments
 dict(kicker=('ಎರಡೂ ಸರ್ಕಾರಗಳು', 'Both governments'), m_expr='skeptic', k_expr='ask',
      card_kn='<div class="h">2020-23 ಬಿಜೆಪಿ ಸರ್ಕಾರ ಚುನಾವಣೆ ನಡೆಸಲಿಲ್ಲ. 2023ರಿಂದ ಕಾಂಗ್ರೆಸ್ ಸರ್ಕಾರವೂ ನಡೆಸಲಿಲ್ಲ.</div>',
      card_en='<div class="h">The BJP government did not hold it, 2020-23. The Congress government has not, since 2023.</div>',
      lines=[('m', 'ಬಿಜೆಪಿ ಸರ್ಕಾರ ಚುನಾವಣೆ ನಡೆಸಲಿಲ್ಲ.', 'The BJP government did not hold the election.'),
             ('k', 'ಕಾಂಗ್ರೆಸ್ ಸರ್ಕಾರವೂ ನಡೆಸಿಲ್ಲ!', 'The Congress government has not held it either!')], src=''),

 dict(kicker=('2026ರಲ್ಲಿ ಸುಪ್ರೀಂ ಕೋರ್ಟ್', 'The Supreme Court in 2026'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big">3</div><div class="h">ಬಾರಿ ಚುನಾವಣಾ ಗಡುವು ಮುಂದೂಡಿಕೆ</div><div class="sub">ಹೊಸ ಗಡುವು: 31 ಡಿಸೆಂಬರ್ 2026</div>',
      card_en='<div class="big">3</div><div class="h">times the election deadline moved</div><div class="sub">New deadline: 31 December 2026</div>',
      lines=[('k', 'ಈ ವರ್ಷ ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ಗಡುವು ಮೂರು ಸಲ ಮುಂದೆ ಹೋಯ್ತು.', "This year the Supreme Court's deadline moved three times."),
             ('m', 'ಹೊಸ ಗಡುವು ಡಿಸೆಂಬರ್ ಮೂವತ್ತೊಂದು.', 'The new deadline is 31 December.')], src=SC),

 # ask
 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗೆ ಚುನಾವಣೆ ಉಂಟು. ಬೆಂಗಳೂರಿಗೆ ಇಲ್ಲ.</div><div class="sub">31 ಡಿಸೆಂಬರ್. ಮತ್ತೆ ಮುಂದೂಡುತ್ತಾರೆಯೇ? ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Your village panchayat gets elections. Bengaluru does not.</div><div class="sub">31 December. Will it be pushed back again? Ask your MLA.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಮತ್ತೆ ಮುಂದೂಡ್ತಾರಾ? ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ.', 'Will it be pushed back again? Ask your MLA.')], src=ASK),

 # chorus: the series theme, chanted on the beat
 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]

_TAIL = ('Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
         'Sources: BBMP council term ended 10 September 2020; State government figures on Bengaluru development grants; '
         'Supreme Court orders on the Greater Bengaluru corporation elections, 2026\n\n'
         'Every figure comes from a public record. If one is wrong, tell us and we will correct it. Music: original.\n\n')
META = {
 'kn': {'title': 'ಬೆಂಗಳೂರು: 6 ವರ್ಷದಿಂದ ಚುನಾಯಿತ ಪಾಲಿಕೆ ಇಲ್ಲ | ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #Shorts',
        'description': ('ಮಲ್ಲಣ್ಣ ಮತ್ತು ಕಾವೇರಿ ಕೇಳುತ್ತಾರೆ: ಬೆಂಗಳೂರಿಗೆ ಚುನಾಯಿತ ಪಾಲಿಕೆ ಯಾವಾಗ?\n'
                         'ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗೆ ಚುನಾವಣೆ ಉಂಟು. ಬೆಂಗಳೂರಿಗೆ ಇಲ್ಲ.\n\n'
                         '• ಸೆಪ್ಟೆಂಬರ್ 2020 ರಿಂದ ಚುನಾಯಿತ ಪಾಲಿಕೆ ಇಲ್ಲ: ಆರು ವರ್ಷ, ಯಾವ ವಾರ್ಡ್‌ಗೂ ಕಾರ್ಪೊರೇಟರ್ ಇಲ್ಲ\n'
                         '• ನಗರಕ್ಕೆ ವಾರ್ಷಿಕ ಅಭಿವೃದ್ಧಿ ಅನುದಾನ ₹3,000 ಕೋಟಿಯಿಂದ ₹7,000 ಕೋಟಿಗೆ ಏರಿದೆ\n'
                         '• 2026ರಲ್ಲಿ ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ಚುನಾವಣಾ ಗಡುವು 3 ಬಾರಿ ಮುಂದೂಡಿಕೆ; ಹೊಸ ಗಡುವು 31 ಡಿಸೆಂಬರ್ 2026\n\n'
                         'ಎರಡೂ ಸರ್ಕಾರಗಳು: 2020-23 ಬಿಜೆಪಿ ಸರ್ಕಾರ ಚುನಾವಣೆ ನಡೆಸಲಿಲ್ಲ. 2023ರಿಂದ ಕಾಂಗ್ರೆಸ್ ಸರ್ಕಾರವೂ ನಡೆಸಲಿಲ್ಲ.\n\n'
                         + _TAIL + '#MallannaAsks #Karnataka #ಕನ್ನಡ')},
 'en': {'title': 'Bengaluru: six years with no elected city council | Mallanna Asks #Shorts',
        'description': ('Mallanna and Kaveri ask: when does Bengaluru get an elected council?\n'
                         'Your village panchayat gets elections. Bengaluru does not.\n\n'
                         '• No elected city council since September 2020: six years with no corporator for any ward\n'
                         "• The city's annual development grant rose from Rs 3,000 crore to Rs 7,000 crore\n"
                         "• In 2026 the Supreme Court's election deadline moved three times; the new deadline is 31 December 2026\n\n"
                         'Both governments: the BJP government did not hold the election from 2020 to 2023. The Congress government has not held it since 2023.\n\n'
                         + _TAIL + '#MallannaAsks #Karnataka')},
}

# The owner's recorded chorus on every Kannada episode.
REC = {'kn': {'chorus': 'voice/ep11/chorus.wav'}}
