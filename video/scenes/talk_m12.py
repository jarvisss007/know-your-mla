# Mallanna Asks, Season 2, Episode 12: "Pothole roads, zero compensation" (ಗುಂಡಿ ರಸ್ತೆ, ಶೂನ್ಯ ಪರಿಹಾರ)
# Figures re-checked 2026-11-14:
#  - NCRB 2024 via ThePrint (13 Aug 2026): Bengaluru 17 deaths from civic-agency negligence; Delhi 4; Mumbai, Ahmedabad,
#    Chennai, Hyderabad, Kolkata none. Bengaluru: 49 (2019), 18, 31, 22, 20 (2023). 41,150 potholes identified to March,
#    39,000+ claimed repaired.
#  - Karnataka High Court interim order, 31 Jul 2019 (CJ A.S. Oka, J. P.M. Nawaz): BBMP liable to compensate pothole
#    victims; "Ensuring pothole-free roads is a legal and constitutional obligation of the BBMP" (TNM, 1 Aug 2019).
#  - TNM investigation (Nov 2022): of 13 pothole deaths in Bengaluru 2017-22, no family compensated (TNM's own reporting).
#  - CM's one-month pothole deadline, 20 Sep 2025; missed (Deccan Herald, 1 Nov 2025).
BPM = 96

NCRB = 'Source: NCRB 2024 data, reported by ThePrint, 13 Aug 2026'
HC = 'Source: Karnataka High Court interim order, 31 Jul 2019 (The News Minute)'
TNM = 'Source: The News Minute investigation, Nov 2022 (13 pothole deaths, 2017-22)'
DL = 'Sources: Deccan Herald, 20 Sep 2025 and 1 Nov 2025. Court orders and deadlines span the BJP (2019-22) and Congress (2025) governments.'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 12', 'Mallanna Asks · Episode 12'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">17</div><div class="h">ಬೆಂಗಳೂರು: 2024ರಲ್ಲಿ ನಗರ ಸಂಸ್ಥೆಗಳ ನಿರ್ಲಕ್ಷ್ಯದಿಂದ ಸಾವು</div>',
      card_en='<div class="big r">17</div><div class="h">Bengaluru deaths from civic-body negligence, 2024</div>',
      lines=[('m', 'ರಸ್ತೆ ಗುಂಡಿಗೆ ಜೀವ ಹೋಯ್ತು. ಉತ್ತರ ಕೊಡೋರು ಯಾರು?', 'A pothole took a life. Who answers for it?')], src=NCRB),

 dict(kicker=('ಎನ್‌ಸಿಆರ್‌ಬಿ 2024', 'National crime records, 2024'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಬೆಂಗಳೂರು</small><b class="r">17</b></div><div class="row"><small>ದೆಹಲಿ</small>4</div><div class="row"><small>ಮುಂಬೈ · ಚೆನ್ನೈ · ಹೈದರಾಬಾದ್ · ಕೋಲ್ಕತ್ತಾ</small><b>0</b></div>',
      card_en='<div class="row"><small>Bengaluru</small><b class="r">17</b></div><div class="row"><small>Delhi</small>4</div><div class="row"><small>Mumbai · Chennai · Hyderabad · Kolkata</small><b>0</b></div>',
      lines=[('k', 'ಮುಂಬೈ, ಚೆನ್ನೈ, ಹೈದರಾಬಾದ್‌ನಲ್ಲಿ ಒಂದೂ ಇಲ್ಲ. ನಮ್ಮಲ್ಲಿ ಹದಿನೇಳು.', 'Mumbai, Chennai, Hyderabad: zero. Ours: seventeen.'),
             ('m', 'ಆರು ವರ್ಷದಿಂದ ಬೆಂಗಳೂರೇ ನಂಬರ್ ಒನ್!', 'Six years running, Bengaluru tops this list!')], src=NCRB),

 dict(kicker=('ಹೈಕೋರ್ಟ್ · 2019', 'High Court · 2019'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="h">"ಗುಂಡಿ ಇಲ್ಲದ ರಸ್ತೆ ಬಿಬಿಎಂಪಿಯ ಕಾನೂನು ಮತ್ತು ಸಾಂವಿಧಾನಿಕ ಹೊಣೆ." ಸಂತ್ರಸ್ತರಿಗೆ ಪರಿಹಾರ ಕೊಡಬೇಕು.</div>',
      card_en='<div class="h">"Ensuring pothole-free roads is a legal and constitutional obligation of the BBMP." Victims must be compensated.</div>',
      lines=[('k', 'ಹೈಕೋರ್ಟ್ ಹೇಳಿತು: ಗುಂಡಿಗೆ ಬಲಿಯಾದವರಿಗೆ ಪರಿಹಾರ ಕೊಡಬೇಕು.', 'The High Court said: pothole victims must be compensated.')], src=HC),

 dict(kicker=('ಪರಿಹಾರ ಸಿಕ್ಕಿತಾ?', 'Was anyone paid?'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">0<small> / 13</small></div><div class="h">ಕುಟುಂಬಗಳಿಗೆ ಪರಿಹಾರ ಸಿಕ್ಕಿಲ್ಲ (2017-22)</div>',
      card_en='<div class="big r">0<small> / 13</small></div><div class="h">families had been compensated (2017-22)</div>',
      lines=[('m', 'ಹದಿಮೂರು ಕುಟುಂಬ. ಒಬ್ಬರಿಗೂ ಪರಿಹಾರ ಇಲ್ಲ!', 'Thirteen families. Not one was compensated!')], src=TNM),

 dict(kicker=('ಗಡುವು ಮುಗಿಯಿತು', 'Deadline missed'), m_expr='skeptic', k_expr='ask',
      card_kn='<div class="h">ಸೆಪ್ಟೆಂಬರ್ 2025: ಒಂದು ತಿಂಗಳಲ್ಲಿ ಗುಂಡಿ ಮುಚ್ಚಿ ಎಂದು ಮುಖ್ಯಮಂತ್ರಿ. ನವೆಂಬರ್: ರಸ್ತೆ ಹಾಗೇ.</div><div class="sub">2019 court order (BJP govt) · 2025 deadline (Congress govt)</div>',
      card_en='<div class="h">Sept 2025: the CM set a one-month pothole deadline. November: the roads were still riddled.</div><div class="sub">2019 court order under the BJP govt · 2025 deadline under the Congress govt</div>',
      lines=[('k', 'ಕೋರ್ಟ್ ಆದೇಶ ಬಂತು, ಗಡುವು ಬಂತು. ಗುಂಡಿ ಹಾಗೇ ಇದೆ.', 'Court orders came, deadlines came. The potholes stayed.')], src=DL),

 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ಗುಂಡಿಯ ಫೋಟೋ, ಜಾಗ, ದಿನಾಂಕದೊಂದಿಗೆ ದೂರು ಕೊಡಿ. ಆರ್‌ಟಿಐ: ನಮ್ಮ ರಸ್ತೆಯ ಗುಂಡಿ ಮುಚ್ಚುವ ಗುತ್ತಿಗೆ ಯಾರಿಗೆ?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Report each pothole with a photo, place and date. File an RTI: who holds the repair contract for our road?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಆರ್‌ಟಿಐ ಹಾಕಿ: ನಮ್ಮ ರಸ್ತೆ ರಿಪೇರಿ ಗುತ್ತಿಗೆ ಯಾರಿಗೆ?', 'File an RTI: who holds the repair contract for our road?')], src=ASK),

 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]

REC = {'kn': {'chorus': 'voice/ep11/chorus.wav'}}

_SRC = ('Sources: NCRB 2024 data (ThePrint, 13 Aug 2026); Karnataka High Court interim order, 31 Jul 2019 (The News Minute); '
        'The News Minute investigation, Nov 2022; Deccan Herald, 20 Sep and 1 Nov 2025.\n'
        'Every figure comes from a public record. If one is wrong, tell us and we will correct it. Music: original.')
META = {
 'kn': {'title': 'ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #12: ಗುಂಡಿ ರಸ್ತೆ, ಶೂನ್ಯ ಪರಿಹಾರ | Pothole deaths, zero compensation #Shorts',
        'description': ('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ, ಸಂಚಿಕೆ 12: ಗುಂಡಿ ರಸ್ತೆ, ಶೂನ್ಯ ಪರಿಹಾರ.\n\n'
                        'Mallanna Asks, episode 12. (Fictional characters; every figure is real.)\n'
                        '- NCRB 2024: Bengaluru recorded 17 deaths from civic-agency negligence. Delhi 4; Mumbai, Chennai, Hyderabad, Kolkata none. Bengaluru has topped this list six years running.\n'
                        '- 31 Jul 2019: the Karnataka High Court held BBMP liable to compensate pothole victims: "a legal and constitutional obligation".\n'
                        '- The News Minute traced 13 pothole deaths (2017-22): no family had been compensated.\n'
                        '- Sept 2025: the CM set a one-month pothole deadline; by November it was missed.\n'
                        'The court orders and deadlines span the BJP and Congress governments.\n\n'
                        'What you can do: report each pothole with a photo, place and date; file an RTI for your road\'s repair contract. Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
                        + _SRC + '\n\n#MallannaAsks #Karnataka #ಕನ್ನಡ #Bengaluru #Potholes')},
 'en': {'title': 'Mallanna Asks #12: A court said pay pothole victims. 0 of 13 families paid #Shorts',
        'description': ('Mallanna Asks, episode 12. A court said pothole victims must be compensated. Were they? (Fictional characters; every figure is real.)\n'
                        '- NCRB 2024: Bengaluru had 17 deaths from civic-agency negligence; Delhi 4; Mumbai, Chennai, Hyderabad, Kolkata none. Six years at the top.\n'
                        '- 31 Jul 2019: the Karnataka High Court held BBMP liable to compensate pothole victims.\n'
                        '- The News Minute traced 13 pothole deaths (2017-22): no family compensated.\n'
                        '- Sept 2025: a one-month pothole deadline from the CM; missed by November.\n'
                        'Orders and deadlines span both BJP and Congress governments.\n\n'
                        'What you can do: report each pothole with a photo, place and date; file an RTI for the repair contract. Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
                        + _SRC + '\n\n#MallannaAsks #Karnataka #Bengaluru #Potholes #RoadSafety')},
}
