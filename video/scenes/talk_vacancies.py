# Mallanna Asks (topic Short): vacant health posts. Talking-character version of scenes_vacancies.py.
# Facts, figures and sources carried over unchanged from the old scene file. The English lines translate its Kannada.
BPM = 96

HEALTH = 'Source: Karnataka Health Department vacancy figures, December 2024'
PRS = 'Source: PRS Legislative Research, Karnataka Budget Analysis 2026-27'
TEACH = 'Sources: CAG; Assembly reply, December 2025'
SRS = 'Source: Sample Registration System'
PAY = "Source: Karnataka Legislators' Salaries amendments, 2022 and 2025"
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಖಾಲಿ ಹುದ್ದೆಗಳು', 'Mallanna Asks · Vacant posts'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">32,870</div><div class="h">ಆರೋಗ್ಯ ಇಲಾಖೆಯ ಹುದ್ದೆಗಳು ಖಾಲಿ</div>',
      card_en='<div class="big r">32,870</div><div class="h">Health Department posts vacant</div>',
      lines=[('m', 'ಆರೋಗ್ಯ ಇಲಾಖೆಯಲ್ಲಿ ಮೂವತ್ತೆರಡು ಸಾವಿರಕ್ಕೂ ಹೆಚ್ಚು ಹುದ್ದೆ ಖಾಲಿ!', 'Over 32,000 Health Department posts are vacant!')], src=HEALTH),

 dict(kicker=('69,915 ಮಂಜೂರಾದ ಹುದ್ದೆಗಳಲ್ಲಿ', 'Of 69,915 sanctioned posts'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="big r">47%</div><div class="h">ಖಾಲಿ. ಸುಮಾರು ಅರ್ಧ.</div>',
      card_en='<div class="big r">47%</div><div class="h">vacant. Almost half.</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಅಂದ್ರೆ ಸುಮಾರು ಅರ್ಧ ಹುದ್ದೆ ಖಾಲಿ!', 'Dad, that is almost half the posts empty!')], src=HEALTH),

 dict(kicker=('ಬಜೆಟ್‌ನಲ್ಲಿ ಆರೋಗ್ಯದ ಪಾಲು', "Health's share of the budget"), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>ಕರ್ನಾಟಕ</small><b class="r">4.3%</b></div><div class="row"><small>ರಾಜ್ಯಗಳ ಸರಾಸರಿ</small>6.2%</div>',
      card_en='<div class="row"><small>Karnataka</small><b class="r">4.3%</b></div><div class="row"><small>Average of states</small>6.2%</div>',
      lines=[('m', 'ಬಜೆಟ್‌ನಲ್ಲಿ ಆರೋಗ್ಯಕ್ಕೆ ನಾಲ್ಕು ಪಾಯಿಂಟ್ ಮೂರು ಪರ್ಸೆಂಟ್. ಸರಾಸರಿ ಆರು ಪಾಯಿಂಟ್ ಎರಡು.', 'Health gets 4.3% of the budget. The states average 6.2%.')], src=PRS),

 # fairness: two governments
 dict(kicker=('ಪ್ರಾಥಮಿಕ ಶಾಲಾ ಶಿಕ್ಷಕರು', 'Primary school teachers'), m_expr='skeptic', k_expr='sad',
      card_kn='<div class="row"><small>2021-22 · ಖಾಲಿ</small>26%</div><div class="row"><small>ಡಿಸೆಂಬರ್ 2025 · ಖಾಲಿ</small><b class="r">25.5%</b></div><div class="sub">ಎರಡು ಸರ್ಕಾರ, ಬದಲಾವಣೆ ಬಹುತೇಕ ಇಲ್ಲ.</div>',
      card_en='<div class="row"><small>2021-22 · vacant</small>26%</div><div class="row"><small>December 2025 · vacant</small><b class="r">25.5%</b></div><div class="sub">Two governments, almost no change.</div>',
      lines=[('k', 'ಶಿಕ್ಷಕರ ಹುದ್ದೆಯೂ ಕಾಲು ಭಾಗ ಖಾಲಿ.', 'A quarter of teacher posts are vacant too.'),
             ('m', 'ಎರಡು ಸರ್ಕಾರ ಬಂತು. ಬದಲಾವಣೆ ಬಹುತೇಕ ಇಲ್ಲ.', 'Two governments, almost no change.')], src=TEACH),

 # fairness: what improved
 dict(kicker=('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair'), m_expr='neutral', k_expr='smile',
      card_kn='<div class="h">ಶಿಶು ಮರಣ ದರ ಇಳಿದಿದೆ: 1,000 ಜನನಕ್ಕೆ 23 ರಿಂದ 14.</div><div class="sub">2018 → 2023 · ರಾಷ್ಟ್ರೀಯ ದರ 25</div>',
      card_en='<div class="h">Infant deaths fell from 23 to 14 per 1,000 births.</div><div class="sub">2018 to 2023 · below the national 25</div>',
      lines=[('k', 'ಆದ್ರೆ ಶಿಶು ಮರಣ ಸಾವಿರಕ್ಕೆ ಇಪ್ಪತ್ಮೂರರಿಂದ ಹದಿನಾಲ್ಕಕ್ಕೆ ಇಳಿದಿದೆ.', 'But infant deaths fell from 23 to 14 per 1,000 births.')], src=SRS),

 dict(kicker=('ಒಂದು ಹುದ್ದೆ ಮಾತ್ರ ಎಂದೂ ಖಾಲಿ ಇರುವುದಿಲ್ಲ', 'One post is never left vacant'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಶಾಸಕರ ಮೂಲ ವೇತನ</small>₹25,000 → <b class="r">₹80,000</b></div><div class="sub">2022 ಮತ್ತು 2025ರಲ್ಲಿ, ಚರ್ಚೆಯೇ ಇಲ್ಲದೆ</div>',
      card_en='<div class="row"><small>MLAs\' basic pay</small>Rs 25,000 → <b class="r">Rs 80,000</b></div><div class="sub">In 2022 and 2025, both times without debate</div>',
      lines=[('m', 'ಶಾಸಕರ ಮೂಲ ವೇತನ ಇಪ್ಪತ್ತೈದು ಸಾವಿರದಿಂದ ಎಂಬತ್ತು ಸಾವಿರ!', "MLAs' basic pay: from 25,000 to 80,000!")], src=PAY),

 # ask
 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ನಿಮ್ಮ ಊರಿನ ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ವೈದ್ಯರಿದ್ದಾರೆಯೇ? ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Is there a doctor at your local hospital? Ask your MLA.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('k', 'ನಿಮ್ಮ ಊರ ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ಡಾಕ್ಟರ್ ಇದ್ದಾರಾ? ಶಾಸಕರನ್ನು ಕೇಳಿ.', 'Is there a doctor at your local hospital? Ask your MLA.')], src=ASK),

 # chorus: the series theme, chanted on the beat
 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]

_TAIL = ('Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
         'Sources: Karnataka Health Department vacancy figures, December 2024; PRS Legislative Research, Karnataka Budget Analysis 2026-27; '
         "CAG; Assembly reply, December 2025; Sample Registration System; Karnataka Legislators' Salaries amendments, 2022 and 2025\n\n"
         'Every figure comes from a public record. If one is wrong, tell us and we will correct it. Music: original.\n\n')
META = {
 'kn': {'title': 'ಆರೋಗ್ಯ ಇಲಾಖೆಯಲ್ಲಿ 32,870 ಹುದ್ದೆ ಖಾಲಿ: ಸುಮಾರು ಅರ್ಧ | ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #Shorts',
        'description': ('ಮಲ್ಲಣ್ಣ ಮತ್ತು ಕಾವೇರಿ ಕರ್ನಾಟಕದ ಖಾಲಿ ಹುದ್ದೆಗಳನ್ನು ನೋಡುತ್ತಾರೆ.\n'
                         'ನಿಮ್ಮ ಊರಿನ ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ವೈದ್ಯರಿದ್ದಾರೆಯೇ?\n\n'
                         '• ಆರೋಗ್ಯ ಇಲಾಖೆ: 69,915 ಮಂಜೂರಾದ ಹುದ್ದೆಗಳಲ್ಲಿ 32,870 ಖಾಲಿ (47%), ಡಿಸೆಂಬರ್ 2024\n'
                         '• 2026-27 ಬಜೆಟ್‌ನಲ್ಲಿ ಆರೋಗ್ಯದ ಪಾಲು 4.3%; ರಾಜ್ಯಗಳ ಸರಾಸರಿ 6.2%\n'
                         '• ಪ್ರಾಥಮಿಕ ಶಾಲಾ ಶಿಕ್ಷಕರ ಹುದ್ದೆ: 2021-22ರಲ್ಲಿ 26% ಖಾಲಿ, ಡಿಸೆಂಬರ್ 2025ರಲ್ಲಿ 25.5%\n'
                         '• ಶಾಸಕರ ಮೂಲ ವೇತನ ₹25,000 → ₹80,000 (2022 ಮತ್ತು 2025ರಲ್ಲಿ, ಚರ್ಚೆಯೇ ಇಲ್ಲದೆ)\n\n'
                         'ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ: ಎರಡು ಸರ್ಕಾರ, ಬದಲಾವಣೆ ಬಹುತೇಕ ಇಲ್ಲ. ಶಿಶು ಮರಣ ದರ 1,000 ಜನನಕ್ಕೆ 23 ರಿಂದ 14ಕ್ಕೆ ಇಳಿದಿದೆ (2018-2023), ರಾಷ್ಟ್ರೀಯ 25ಕ್ಕಿಂತ ಕಡಿಮೆ.\n\n'
                         + _TAIL + '#MallannaAsks #Karnataka #ಕನ್ನಡ')},
 'en': {'title': "Karnataka's Health Department: 32,870 posts vacant, almost half | Mallanna Asks #Shorts",
        'description': ("Mallanna and Kaveri look at Karnataka's empty posts.\n"
                         'Is there a doctor at your local hospital?\n\n'
                         '• Health Department: 32,870 of 69,915 sanctioned posts vacant (47%), December 2024\n'
                         '• The 2026-27 budget gives health 4.3% of spending, against an average of 6.2% across states\n'
                         '• Primary teacher posts: 26% vacant in 2021-22, 25.5% in December 2025\n'
                         "• MLAs' basic pay rose from Rs 25,000 to Rs 80,000 (in 2022 and 2025, both times without debate)\n\n"
                         'To be fair: two governments, almost no change. Infant deaths fell from 23 to 14 per 1,000 births (2018 to 2023), below the national 25.\n\n'
                         + _TAIL + '#MallannaAsks #Karnataka')},
}

# The owner's recorded chorus on every Kannada episode.
REC = {'kn': {'chorus': 'voice/ep11/chorus.wav'}}
