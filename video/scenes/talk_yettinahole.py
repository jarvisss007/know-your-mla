# Yettinahole drinking water project, talking-character format (no episode number).
# Converted from scenes/scenes_yettinahole.py + scenes_yettinahole_en.py; every figure and source carried over unchanged
# from those files and the published description.
# Legal: follow the CAG wording, "could not be made operational even after 12 years". Never "no water" / "not one drop".
BPM = 96

SRC2 = 'Sources: CAG audit of the Yettinahole project; Chief Minister statement setting an end-2027 target for Kolar and Chikkaballapura, 2026'
CAG = 'Source: CAG performance audit of the Yettinahole project (cost to January 2023, spending to March 2024)'
STATE = 'Source: State government statement, 20 August 2026'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-2 s hook
 dict(kicker=('ಎತ್ತಿನಹೊಳೆ ಯೋಜನೆ', 'Yettinahole project'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">15,297<small> ಕೋಟಿ</small></div><div class="h">ಖರ್ಚು (ಮಾರ್ಚ್ 2024). ಕೋಲಾರ ಇನ್ನೂ ನೀರಿಗಾಗಿ ಕಾಯುತ್ತಿದೆ.</div>',
      card_en='<div class="big r">15,297<small> cr</small></div><div class="h">rupees spent by March 2024. Kolar is still waiting for the water.</div>',
      lines=[('m', 'ಹದಿನೈದು ಸಾವಿರ ಕೋಟಿ ಖರ್ಚು. ಕೋಲಾರ ಇನ್ನೂ ಕಾಯ್ತಾ ಇದೆ!', '15,297 crore spent. Kolar is still waiting!')], src=SRC2),

 dict(kicker=('ರಾಷ್ಟ್ರೀಯ ಲೆಕ್ಕಪರಿಶೋಧಕರ ವರದಿ', 'What the national auditor found'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="big r">12<small> ವರ್ಷ</small></div><div class="h">ಆದರೂ ಯೋಜನೆ ಕಾರ್ಯಾರಂಭ ಮಾಡಿಲ್ಲ.</div><div class="sub">"Could not be made operational even after 12 years." CAG</div>',
      card_en='<div class="big r">12<small> years</small></div><div class="h">"Could not be made operational even after 12 years."</div><div class="sub">CAG</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಹನ್ನೆರಡು ವರ್ಷವಾದರೂ ಯೋಜನೆ ಕಾರ್ಯಾರಂಭ ಮಾಡಿಲ್ಲ ಅಂತ ಸಿಎಜಿ.', 'Auditor: "could not be made operational even after 12 years."')], src=CAG),

 dict(kicker=('ವೆಚ್ಚ ಎಷ್ಟು ಏರಿತು', 'How the bill grew'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>2012 · ಅನುಮೋದಿತ ವೆಚ್ಚ</small>₹8,324 ಕೋಟಿ</div><div class="row"><small>2023 · ಪರಿಷ್ಕೃತ ವೆಚ್ಚ</small><b class="r">₹23,252 ಕೋಟಿ</b></div><div class="sub">Almost three times. No project report ever fixed a completion date.</div>',
      card_en='<div class="row"><small>2012 · approved cost</small>Rs 8,324 cr</div><div class="row"><small>2023 · revised cost</small><b class="r">Rs 23,252 cr</b></div><div class="sub">Almost three times. No project report ever fixed a completion date.</div>',
      lines=[('m', 'ಎಂಟು ಸಾವಿರ ಕೋಟಿ ಯೋಜನೆ, ಈಗ ಇಪ್ಪತ್ತಮೂರು ಸಾವಿರ ಕೋಟಿ!', 'An 8,324 crore project is now 23,252 crore!'),
             ('k', 'ಮುಗಿಯೋದು ಯಾವಾಗ?', 'When will it finish?'),
             ('m', 'ಗಡುವೇ ಇರಲಿಲ್ಲ ಮಗಳೇ!', 'There was never a deadline!')], src=CAG),

 dict(kicker=('ಕಾಮಗಾರಿ ಯಾರಿಗೆ ಹೋಯಿತು', 'Who got the work'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಸಾಮರ್ಥ್ಯ ಪರಿಶೀಲಿಸದೆ ನೀಡಿದ ಕಾಮಗಾರಿ</small><b class="r">80%</b></div><div class="row"><small>ಮೌಲ್ಯದ ಕೆಲಸ ಕೇವಲ 7 ಗುತ್ತಿಗೆದಾರರಿಗೆ</small><b>67%</b></div>',
      card_en='<div class="row"><small>Works awarded without checking bidders</small><b class="r">80%</b></div><div class="row"><small>Work by value to just 7 contractors</small><b>67%</b></div>',
      lines=[('k', 'ಎಂಬತ್ತು ಪರ್ಸೆಂಟ್ ಕಾಮಗಾರಿ ಸಾಮರ್ಥ್ಯ ನೋಡದೆ ಕೊಟ್ಟರು!', '80 percent of works were awarded without checking the bidders!'),
             ('m', 'ಅರವತ್ತೇಳು ಪರ್ಸೆಂಟ್ ಕೆಲಸ ಕೇವಲ ಏಳು ಗುತ್ತಿಗೆದಾರರಿಗೆ.', '67 percent of the work went to just seven contractors.')], src=CAG),

 dict(kicker=('ಆಗಸ್ಟ್ 2026', 'August 2026'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big">20<small> / 54</small></div><div class="h">ಕಾಮಗಾರಿ ಪ್ಯಾಕೇಜ್‌ಗಳು ಮಾತ್ರ ಪೂರ್ಣ</div>',
      card_en='<div class="big">20<small> / 54</small></div><div class="h">work packages complete</div>',
      lines=[('k', 'ಐವತ್ತನಾಲ್ಕರಲ್ಲಿ ಇಪ್ಪತ್ತೇ ಪ್ಯಾಕೇಜ್ ಮುಗಿದಿವೆ.', 'Only 20 of 54 work packages are complete.')], src=STATE),

 # fairness beat
 dict(kicker=('2012ರಿಂದ', 'Since 2012'), m_expr='neutral', k_expr='ask',
      card_kn='<div class="h">2012ರಿಂದ ಪ್ರತಿ ಸರ್ಕಾರವೂ ಇದನ್ನು ನಡೆಸಿದೆ.</div><div class="h" style="color:#f2b705">ಬಿಜೆಪಿ · ಕಾಂಗ್ರೆಸ್ · ಸಮ್ಮಿಶ್ರ</div>',
      card_en='<div class="h">Every government since 2012 has run it.</div><div class="h" style="color:#f2b705">BJP · Congress · Coalition</div>',
      lines=[('m', 'ಬಿಜೆಪಿ, ಕಾಂಗ್ರೆಸ್, ಸಮ್ಮಿಶ್ರ. ಎಲ್ಲರೂ ನಡೆಸಿದರು.', 'BJP, Congress, coalition. Every one of them ran it.')], src=''),

 dict(kicker=('ಹೊಸ ಭರವಸೆ: 2027ರ ಕೊನೆ', 'The new promise: end of 2027'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ಮತ್ತೆ ತಪ್ಪಿದರೆ, ಕೋಲಾರ ಮತ್ತು ಚಿಕ್ಕಬಳ್ಳಾಪುರಕ್ಕೆ ಯಾರು ಉತ್ತರಿಸುತ್ತಾರೆ?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">If it slips again, who answers to Kolar and Chikkaballapura?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಹೊಸ ಗಡುವು 2027. ಮತ್ತೆ ತಪ್ಪಿದರೆ ಯಾರು ಉತ್ತರ ಕೊಡ್ತಾರೆ?', 'The new target is 2027. If it slips again, who answers?')], src=SRC2),

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
