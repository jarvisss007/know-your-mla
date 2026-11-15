# Mallanna Asks (topic Short): Lokayukta cases. Talking-character version of scenes_lokayukta.py / scenes_lokayukta_en.py.
# Facts, figures and sources carried over unchanged from the old scene files.
BPM = 96

SRC = "Source: Chief Minister's reply in the Legislative Assembly (Lokayukta cases, September 2022 to February 2026)"
SANC = 'Source: Government sanction data, August 2023'
ACB = 'Source: Assembly records on the Anti-Corruption Bureau, March 2016 to March 2022'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಲೋಕಾಯುಕ್ತ', 'Mallanna Asks · Lokayukta'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">195</div><div class="h">ಭ್ರಷ್ಟಾಚಾರ ಪ್ರಕರಣ. ಒಂದೂ ತೀರ್ಪಿಲ್ಲ.</div>',
      card_en='<div class="big r">195</div><div class="h">corruption cases. Zero verdicts.</div>',
      lines=[('m', 'ನೂರಾ ತೊಂಬತ್ತೈದು ಭ್ರಷ್ಟಾಚಾರ ಪ್ರಕರಣ. ಒಂದಕ್ಕೂ ತೀರ್ಪಿಲ್ಲ!', '195 corruption cases. Not one verdict!')], src=SRC),

 dict(kicker=('ಸೆಪ್ಟೆಂಬರ್ 2022 ರಿಂದ ಫೆಬ್ರವರಿ 2026', 'September 2022 to February 2026'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಅಧಿಕಾರಿಗಳ ಮೇಲೆ ದಾಳಿ, ಟ್ರ್ಯಾಪ್ ಪ್ರಕರಣಗಳು</small>195</div><div class="row"><small>ಶಿಕ್ಷೆ ಅಥವಾ ಖುಲಾಸೆ</small><b class="r">0</b></div><div class="row"><small>ಹೈಕೋರ್ಟ್ ತಡೆ</small>62</div>',
      card_en='<div class="row"><small>Raid and trap cases against officials</small>195</div><div class="row"><small>Convictions or acquittals</small><b class="r">0</b></div><div class="row"><small>Stayed by the High Court</small>62</div>',
      lines=[('k', 'ಅಧಿಕಾರಿಗಳ ಮೇಲೆ ದಾಳಿ, ಟ್ರ್ಯಾಪ್. ಶಿಕ್ಷೆಯೂ ಇಲ್ಲ, ಖುಲಾಸೆಯೂ ಇಲ್ಲ.', 'Raids and traps on officials. No conviction, no acquittal.'),
             ('m', 'ಅರವತ್ತೆರಡು ಪ್ರಕರಣಕ್ಕೆ ಹೈಕೋರ್ಟ್ ತಡೆ ಇದೆ.', 'The High Court stayed 62 of them.')], src=SRC),

 dict(kicker=('ಅನುಮತಿಗಾಗಿ ಕಾಯುತ್ತಿವೆ', 'Waiting for permission'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="big r">156</div><div class="h">ಪ್ರಕರಣಗಳು ಸರ್ಕಾರದ ಅಭಿಯೋಜನಾ ಅನುಮತಿಗೆ ಕಾದಿದ್ದವು</div><div class="sub">August 2023</div>',
      card_en='<div class="big r">156</div><div class="h">cases waiting for the government\'s sanction to prosecute</div><div class="sub">August 2023</div>',
      lines=[('k', 'ನೂರೈವತ್ತಾರು ಪ್ರಕರಣ ಸರ್ಕಾರದ ಅನುಮತಿಗೆ ಕಾದಿದ್ದವು.', '156 cases were waiting for permission to prosecute.')], src=SANC),

 # fairness: it was worse before, under three governments
 dict(kicker=('ಹಿಂದೆ ಇನ್ನೂ ಕೆಟ್ಟದಿತ್ತು', 'It was worse before'), hit=True, m_expr='skeptic', k_expr='sad',
      card_kn='<div class="big">19</div><div class="h">ಶಿಕ್ಷೆಗಳು, 2,000ಕ್ಕೂ ಹೆಚ್ಚು ಪ್ರಕರಣಗಳಲ್ಲಿ</div><div class="sub">ಹಳೆಯ ಭ್ರಷ್ಟಾಚಾರ ನಿಗ್ರಹ ದಳ (ACB), 2016-2022 · ಮೂರು ಸರ್ಕಾರಗಳು</div>',
      card_en='<div class="big">19</div><div class="h">convictions from more than 2,000 cases</div><div class="sub">The old Anti-Corruption Bureau, 2016 to 2022, under three governments.</div>',
      lines=[('m', 'ಹಳೆಯ ಎಸಿಬಿ: ಎರಡು ಸಾವಿರಕ್ಕೂ ಹೆಚ್ಚು ಪ್ರಕರಣ, ಹತ್ತೊಂಬತ್ತೇ ಶಿಕ್ಷೆ.', 'The old ACB: over 2,000 cases, just 19 convictions.'),
             ('k', 'ಅದೂ ಮೂರು ಸರ್ಕಾರಗಳ ಕಾಲದಲ್ಲಿ.', 'And that was under three governments.')], src=ACB),

 # ask
 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ದಾಳಿ ಸುದ್ದಿಯಾಗುತ್ತದೆ. ತೀರ್ಪು ಭ್ರಷ್ಟಾಚಾರ ನಿಲ್ಲಿಸುತ್ತದೆ.</div><div class="sub">ತೀರ್ಪುಗಳು ಯಾಕೆ ಬರುತ್ತಿಲ್ಲ? ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Raids make headlines. Verdicts stop corruption.</div><div class="sub">Why do no verdicts arrive? Ask your MLA.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('k', 'ದಾಳಿ ಸುದ್ದಿಯಾಗುತ್ತೆ. ತೀರ್ಪು ಭ್ರಷ್ಟಾಚಾರ ನಿಲ್ಲಿಸುತ್ತೆ.', 'Raids make headlines. Verdicts stop corruption.'),
             ('m', 'ತೀರ್ಪು ಯಾಕೆ ಬರ್ತಿಲ್ಲ? ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ.', 'Why do no verdicts arrive? Ask your MLA.')], src=ASK),

 # chorus: the series theme, chanted on the beat
 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]

_TAIL = ('Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
         "Sources: Chief Minister's reply in the Legislative Assembly (Lokayukta cases, September 2022 to February 2026); "
         'Government sanction data, August 2023; Assembly records on the Anti-Corruption Bureau, March 2016 to March 2022\n\n'
         'Every figure comes from a public record. If one is wrong, tell us and we will correct it. Music: original.\n\n')
META = {
 'kn': {'title': 'ಲೋಕಾಯುಕ್ತ: 195 ಭ್ರಷ್ಟಾಚಾರ ಪ್ರಕರಣ, ಒಂದೂ ತೀರ್ಪಿಲ್ಲ | ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #Shorts',
        'description': ('ಮಲ್ಲಣ್ಣ ಮತ್ತು ಕಾವೇರಿ ಲೋಕಾಯುಕ್ತ ಪ್ರಕರಣಗಳ ಸ್ಥಿತಿ ನೋಡುತ್ತಾರೆ.\n'
                         'ದಾಳಿ ಸುದ್ದಿಯಾಗುತ್ತದೆ. ತೀರ್ಪು ಭ್ರಷ್ಟಾಚಾರ ನಿಲ್ಲಿಸುತ್ತದೆ.\n\n'
                         '• ಸೆಪ್ಟೆಂಬರ್ 2022 – ಫೆಬ್ರವರಿ 2026: ಅಧಿಕಾರಿಗಳ ಮೇಲೆ 195 ದಾಳಿ, ಟ್ರ್ಯಾಪ್ ಪ್ರಕರಣಗಳು\n'
                         '• ಶಿಕ್ಷೆ ಅಥವಾ ಖುಲಾಸೆ: 0 · ಹೈಕೋರ್ಟ್ ತಡೆ: 62\n'
                         '• ಆಗಸ್ಟ್ 2023: 156 ಪ್ರಕರಣಗಳು ಸರ್ಕಾರದ ಅಭಿಯೋಜನಾ ಅನುಮತಿಗೆ ಕಾದಿದ್ದವು\n'
                         '• ಹಳೆಯ ಭ್ರಷ್ಟಾಚಾರ ನಿಗ್ರಹ ದಳ (2016-2022): 2,000ಕ್ಕೂ ಹೆಚ್ಚು ಪ್ರಕರಣಗಳಲ್ಲಿ 19 ಶಿಕ್ಷೆಗಳು\n\n'
                         'ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ: ಹಿಂದೆ ಇನ್ನೂ ಕೆಟ್ಟದಿತ್ತು, ಮೂರು ಸರ್ಕಾರಗಳ ಕಾಲದಲ್ಲಿ.\n\n'
                         + _TAIL + '#MallannaAsks #Karnataka #ಕನ್ನಡ')},
 'en': {'title': 'Karnataka Lokayukta: 195 corruption cases, zero verdicts | Mallanna Asks #Shorts',
        'description': ('Mallanna and Kaveri look at where the Lokayukta cases stand.\n'
                         'Raids make headlines. Verdicts stop corruption.\n\n'
                         '• September 2022 to February 2026: 195 raid and trap cases against officials\n'
                         '• Convictions or acquittals: 0 · Stayed by the High Court: 62\n'
                         "• August 2023: 156 cases were waiting for the government's sanction to prosecute\n"
                         '• The old Anti-Corruption Bureau (2016 to 2022): 19 convictions from more than 2,000 cases\n\n'
                         'To be fair: it was worse before, under three governments.\n\n'
                         + _TAIL + '#MallannaAsks #Karnataka')},
}

# The owner's recorded chorus on every Kannada episode.
REC = {'kn': {'chorus': 'voice/ep11/chorus.wav'}}
