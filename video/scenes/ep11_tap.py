# Mallanna Asks, Season 2, Episode 11: "The tap came. The water?" (ನಲ್ಲಿ ಬಂತು, ನೀರು?)
# Every figure re-checked 2026-11-14 against the CAG performance audit of the Jal Jeevan Mission, Government of
# Karnataka (audit period 2019-20 to 2023-24), Executive Summary pp. v-vii.
BPM = 96

# Mallanna's Kannada lines and the chorus in the channel owner's own voice (recorded 2026-11-14).
REC = {'kn': {'0.0': 'voice/ep11/m1.wav', '2.0': 'voice/ep11/m2.wav', '4.0': 'voice/ep11/m3.wav',
              '6.0': 'voice/ep11/m4.wav', 'chorus': 'voice/ep11/chorus.wav'}}

CAG = 'Source: CAG performance audit, Jal Jeevan Mission, Government of Karnataka (2019-20 to 2023-24)'
COV = 'Sources: PTI, 1 May 2026 (Karnataka about 87%); Union Minister of State, 19 Nov 2025 (states at 100%)'
FUNDS = ('Sources: CAG JJM audit; Union Jal Shakti Minister, Lok Sabha, 11 Dec 2025; Karnataka CM\'s memorandum, Nov 2025. '
         'The mission years ran under BJP and Congress state governments.')
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-3 s hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 11', 'Mallanna Asks · Episode 11'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">2<small> / 28</small></div><div class="h">ಹಳ್ಳಿಗಳಲ್ಲಿ ಮಾತ್ರ ಸುರಕ್ಷಿತ ನೀರು</div>',
      card_en='<div class="big r">2<small> / 28</small></div><div class="h">villages had water that met the standard</div>',
      lines=[('m', 'ನಲ್ಲಿ ಬಂತು. ನೀರು ಎಲ್ಲಿ?', 'The tap came. Where is the water?')], src=CAG),

 dict(kicker=('ಜಲ ಜೀವನ್ ಮಿಷನ್ · ಸಿಎಜಿ ವರದಿ', 'Jal Jeevan Mission · the national auditor'), m_expr='skeptic', k_expr='ask',
      card_kn='<div class="h">ಲೆಕ್ಕಪರಿಶೋಧಕರು 28 ಹಳ್ಳಿಗಳ ನೀರನ್ನು ಸ್ವತಂತ್ರವಾಗಿ ಪರೀಕ್ಷಿಸಿದರು.</div><div class="sub">With the State Pollution Control Board labs.</div>',
      card_en='<div class="h">The auditor had water from 28 villages tested independently.</div><div class="sub">ಸ್ವತಂತ್ರ ಪರೀಕ್ಷೆ · State Pollution Control Board labs</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಸಿಎಜಿ ಇಪ್ಪತ್ತೆಂಟು ಹಳ್ಳಿಗಳ ನೀರನ್ನು ಪರೀಕ್ಷೆ ಮಾಡಿಸಿತು.', 'Dad, the national auditor tested the water in 28 villages.'),
             ('k', 'ಮಾನದಂಡಕ್ಕೆ ತಕ್ಕಂತೆ ಇದ್ದದ್ದು ಕೇವಲ ಎರಡು ಹಳ್ಳಿಗಳ ನೀರು.', 'Only two of them met the drinking-water standard.')], src=CAG),

 dict(kicker=('ನವೆಂಬರ್ 2024ರ ಸ್ಥಿತಿ', 'As of November 2024'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">24.52<small> ಲಕ್ಷ</small></div><div class="h">ಮನೆಗಳಿಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ನಲ್ಲಿ ಸಂಪರ್ಕವಿಲ್ಲ (34%)</div>',
      card_en='<div class="big r">24.52<small> lakh</small></div><div class="h">homes still had no working tap (34%)</div>',
      lines=[('m', 'ಮೂರು ಮನೆಯಲ್ಲಿ ಒಂದು ಮನೆಗೆ ಇನ್ನೂ ನಲ್ಲಿ ಸಂಪರ್ಕವೇ ಇಲ್ಲ!', 'One home in three still has no working tap!')], src=CAG),

 dict(kicker=('ನೀರು ಪರೀಕ್ಷಾ ಪ್ರಯೋಗಾಲಯಗಳು', 'Water-testing labs'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಜಿಲ್ಲಾ + ತಾಲ್ಲೂಕು ಲ್ಯಾಬ್‌ಗಳು</small>31 + 48 = <b>79</b></div><div class="row"><small>ಆರ್ಸೆನಿಕ್ ಪರೀಕ್ಷೆ ಮಾಡಬಲ್ಲವು</small><b class="r">0</b></div>',
      card_en='<div class="row"><small>District + taluk labs</small>31 + 48 = <b>79</b></div><div class="row"><small>Could test for arsenic</small><b class="r">0</b></div>',
      lines=[('k', 'ಎಪ್ಪತ್ತೊಂಬತ್ತು ಲ್ಯಾಬ್‌ಗಳಲ್ಲಿ ಒಂದರಲ್ಲೂ ಆರ್ಸೆನಿಕ್ ಪರೀಕ್ಷೆ ಮಾಡುವ ವ್ಯವಸ್ಥೆ ಇಲ್ಲ.', 'Not one of 79 labs could even test for arsenic.')], src=CAG),

 dict(kicker=('ಹಣ ಎಲ್ಲಿ?', 'Where did the money go?'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>ಕೇಂದ್ರದ ಹಂಚಿಕೆ</small>₹24,819 ಕೋಟಿ</div><div class="row"><small>ರಾಜ್ಯಕ್ಕೆ ಬಂದದ್ದು</small><b class="r">₹11,189 ಕೋಟಿ (45%)</b></div>',
      card_en='<div class="row"><small>Central allocation</small>Rs 24,819 cr</div><div class="row"><small>What the state received</small><b class="r">Rs 11,189 cr (45%)</b></div>',
      lines=[('m', 'ಹಣ ಇತ್ತು. ಅರ್ಧಕ್ಕಿಂತ ಕಡಿಮೆ ಬಂತು. ಯಾಕೆ?', 'The money was there. Less than half arrived. Why?'),
             ('k', 'ಕೇಂದ್ರ ರಾಜ್ಯವನ್ನು ದೂರುತ್ತೆ. ರಾಜ್ಯ ಕೇಂದ್ರವನ್ನು ದೂರುತ್ತೆ.', 'The Centre blames the state. The state blames the Centre.')], src=FUNDS),

 dict(kicker=('ಬೇರೆ ರಾಜ್ಯಗಳು ಮುಗಿಸಿವೆ', 'Other states finished'), m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ತೆಲಂಗಾಣ · ಗೋವಾ · ಗುಜರಾತ್ · ಪಂಜಾಬ್</small><b>100%</b></div><div class="row"><small>ಕರ್ನಾಟಕ (ಮೇ 2026)</small><b class="r">ಸುಮಾರು 87%</b></div>',
      card_en='<div class="row"><small>Telangana · Goa · Gujarat · Punjab</small><b>100%</b></div><div class="row"><small>Karnataka (May 2026)</small><b class="r">about 87%</b></div>',
      lines=[('k', 'ತೆಲಂಗಾಣ, ಗೋವಾ, ಗುಜರಾತ್ ನೂರಕ್ಕೆ ನೂರು ಮುಗಿಸಿವೆ. ನಾವು?', 'Telangana, Goa and Gujarat reached one hundred percent. And us?')], src=COV),

 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ಗ್ರಾಮ ಸಭೆಯಲ್ಲಿ ಕೇಳಿ: ನಮ್ಮ ಊರಿನ ನೀರಿನ ಪರೀಕ್ಷಾ ವರದಿ ಎಲ್ಲಿ?</div><div class="sub">Or file an RTI with your Rural Drinking Water division for your village\'s lab reports.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Ask at your gram sabha: where is our village\'s water test report?</div><div class="sub">Or file an RTI with your Rural Drinking Water division for the lab reports.</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಗ್ರಾಮ ಸಭೆಯಲ್ಲಿ ಕೇಳಿ: ನಮ್ಮ ನೀರಿನ ಪರೀಕ್ಷಾ ವರದಿ ಎಲ್ಲಿ?', 'Ask at your gram sabha: where is our water test report?')], src=ASK),

 # chorus: the series theme, chanted on the beat
 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]
