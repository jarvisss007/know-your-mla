# Mallanna Asks, Episode 6: "The guarantee math" (ಗ್ಯಾರಂಟಿ ಲೆಕ್ಕ), talking-character format.
# Converted from scenes/ep6.py; every figure and source carried over unchanged from that file and its published description.
BPM = 96

PRS = 'Source: PRS Legislative Research, Karnataka Budget Analysis 2026-27 (share of guarantees: our calculation from PRS figures)'
GL = 'Sources: PRS Legislative Research; ThePrint on the 2026-27 budget'
RAISE = 'Sources: Business Today, June 2024; Free Press Journal, April 2025; The South First, August 2025'
END = 'Fictional characters. Every figure in this video comes from a public record. If one is wrong, tell us and we will correct it.'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-2 s hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 6 · ಗ್ಯಾರಂಟಿ ಲೆಕ್ಕ', 'Mallanna Asks · Episode 6 · The guarantee math'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="big r">₹25<small> / ₹100</small></div><div class="h">ರಸ್ತೆ, ಆಸ್ಪತ್ರೆ, ಶಾಲೆ, ನೀರು, ಎಲ್ಲಕ್ಕೂ ಉಳಿಯುವುದು ಇಷ್ಟೇ</div>',
      card_en='<div class="big r">Rs 25<small> / 100</small></div><div class="h">is all that is left for roads, hospitals, schools, water</div>',
      lines=[('m', 'ಐದು ಗ್ಯಾರಂಟಿ ಸರಿ. ಲೆಕ್ಕ ಎಲ್ಲಿ ಸ್ವಾಮಿ?', 'Five guarantees, fine. Where are the accounts, sir?')], src=PRS),

 dict(kicker=('ರಾಜ್ಯದ ಆದಾಯದ ₹100ರಲ್ಲಿ, 2026-27', 'Of every Rs 100 the state earns, 2026-27'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>ಸಂಬಳ, ಪಿಂಚಣಿ, ಬಡ್ಡಿ</small><b class="r">₹59</b></div><div class="row"><small>ಐದು ಗ್ಯಾರಂಟಿಗಳು (₹51,286 ಕೋಟಿ)</small><b>₹16</b></div><div class="row"><small>ಉಳಿದ ಎಲ್ಲದಕ್ಕೂ</small>₹25</div>',
      card_en='<div class="row"><small>Salaries, pensions, interest</small><b class="r">Rs 59</b></div><div class="row"><small>Five guarantees (Rs 51,286 crore)</small><b>Rs 16</b></div><div class="row"><small>Everything else</small>Rs 25</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ನೂರರಲ್ಲಿ ಐವತ್ತೊಂಬತ್ತು ಸಂಬಳ, ಪಿಂಚಣಿ, ಬಡ್ಡಿಗೇ!', 'Dad, 59 of every 100 rupees: salaries, pensions, interest!'),
             ('m', 'ಹದಿನಾರು ಗ್ಯಾರಂಟಿಗೆ. ಉಳಿದ ಎಲ್ಲಕ್ಕೂ ಇಪ್ಪತ್ತೈದೇ.', 'Sixteen to the guarantees. Just 25 for everything else.')], src=PRS),

 # fairness beat
 dict(kicker=('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair'), m_expr='neutral', k_expr='smile',
      card_kn='<div class="row"><small>ಗೃಹಲಕ್ಷ್ಮಿ ಒಂದೇ</small>₹28,608 ಕೋಟಿ</div><div class="h">ಮನೆಯೊಡತಿಯರಿಗೆ ತಿಂಗಳಿಗೆ ₹2,000</div><div class="sub">For many families it is real help.</div>',
      card_en='<div class="row"><small>Gruha Lakshmi alone</small>Rs 28,608 cr</div><div class="h">Rs 2,000 a month to women heads of households</div><div class="sub">ಅನೇಕ ಕುಟುಂಬಗಳಿಗೆ ಇದು ನಿಜವಾದ ಸಹಾಯ.</div>',
      lines=[('k', 'ಗೃಹಲಕ್ಷ್ಮಿ ಅನೇಕ ಮನೆಗಳಿಗೆ ನಿಜವಾದ ಸಹಾಯ ಅಲ್ವಾ?', 'Gruha Lakshmi is real help for many families, right?'),
             ('m', 'ಹೌದು. ಪ್ರಶ್ನೆ ಸಹಾಯದ್ದಲ್ಲ. ದುಡ್ಡು ಎಲ್ಲಿಂದ ಅನ್ನೋದು.', 'Yes. The question is where the money comes from.')], src=GL),

 dict(kicker=('ತೆರಿಗೆ, ಶುಲ್ಕ ಏರಿಕೆ', 'Taxes and fees went up'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಪೆಟ್ರೋಲ್ ಮೇಲಿನ ರಾಜ್ಯ ತೆರಿಗೆ · 2024</small>25.92% → <b class="r">29.84%</b></div><div class="row"><small>ಡೀಸೆಲ್ · 2024-25</small>14.3% → <b class="r">21.17%</b></div><div class="row"><small>ನೋಂದಣಿ ಶುಲ್ಕ · 2025</small>1% → <b class="r">2%</b></div>',
      card_en='<div class="row"><small>State tax on petrol · 2024</small>25.92% → <b class="r">29.84%</b></div><div class="row"><small>Diesel · 2024-25</small>14.3% → <b class="r">21.17%</b></div><div class="row"><small>Property registration fee · 2025</small>1% → <b class="r">2%</b></div>',
      lines=[('m', 'ಅದಕ್ಕೇನಾ ಪೆಟ್ರೋಲ್, ಡೀಸೆಲ್, ನೋಂದಣಿ ಎಲ್ಲಾ ಏರಿದ್ದು?', 'Is that why petrol, diesel and registration went up?')], src=RAISE),

 dict(kicker=('ಆದರೂ ಸಾಲ · 2026-27', 'And still, borrowing · 2026-27'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="row"><small>ಆದಾಯ ಕೊರತೆ</small><b class="r">₹22,957 ಕೋಟಿ</b></div><div class="row"><small>ವಿತ್ತೀಯ ಕೊರತೆ (ಸಾಲ)</small><b class="r">₹97,448 ಕೋಟಿ</b></div><div class="sub">Borrowing even for day-to-day spending.</div>',
      card_en='<div class="row"><small>Revenue deficit</small><b class="r">Rs 22,957 cr</b></div><div class="row"><small>Fiscal deficit (borrowing)</small><b class="r">Rs 97,448 cr</b></div><div class="sub">ದೈನಂದಿನ ಖರ್ಚಿಗೂ ಸಾಲ.</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಆ ಸಾಲ ಯಾರು ತೀರಿಸ್ತಾರೆ?', 'Dad, who pays back that loan?'),
             ('m', 'ನೀನು, ಕಾವೇರಿ.', 'You do, Kaveri.')], src=PRS),

 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ: ಗ್ಯಾರಂಟಿಗೆ ದುಡ್ಡು ಎಲ್ಲಿಂದ? ಕೆಲಸಕ್ಕೆ ಎಷ್ಟು ಉಳಿಯಿತು?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Ask your MLA: where does the guarantee money come from? What is left for the work?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಶಾಸಕರನ್ನು ಕೇಳಿ: ಕೆಲಸಕ್ಕೆ ಎಷ್ಟು ಉಳಿಯಿತು?', 'Ask your MLA: what is left for the work?')], src=END),

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
