# Mallanna Asks, Season 2, Episode 10: "The garbage account" (ಕಸದ ಲೆಕ್ಕ)
# Figures re-checked 2026-11-14:
#  - CAG Report No. 4 of 2018, Performance Audit of Solid Waste Management in ULBs, Karnataka (2012-13 to 2016-17),
#    Executive Summary: "process only 26 per cent of waste collected"; 6,935 (83%) of 8,324 km not swept daily;
#    Rs 93.19 crore balances at end of March 2017; dumping near River Kabini, CMC Nanjangud; staff shortage 32/70/65%.
#  - NGT, Oct 2022: Rs 2,900 crore environmental compensation for solid and liquid waste (PTI via Outlook, 15 Oct 2022).
#  - Swachh Survekshan 2024-25: Indore cleanest for the 8th year; Mysuru in the Super Swachh League (3-10 lakh category).
BPM = 96

CAG = 'Source: CAG Report No. 4 of 2018, Solid Waste Management in Urban Local Bodies, Karnataka (2012-13 to 2016-17)'
NGT = 'Source: National Green Tribunal order, October 2022 (PTI)'
SS = 'Source: Swachh Survekshan 2024-25 results, July 2025'
FAIR = ('The audit years were mostly under the Congress government (2013-18); the NGT penalty came under the BJP government (2022). '
        'Every figure comes from a public record.')
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 10', 'Mallanna Asks · Episode 10'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">26<small>%</small></div><div class="h">ಸಂಗ್ರಹಿಸಿದ ಕಸದಲ್ಲಿ ಸಂಸ್ಕರಣೆ ಆಗಿದ್ದು ಇಷ್ಟೇ</div>',
      card_en='<div class="big r">26<small>%</small></div><div class="h">of the garbage collected was processed</div>',
      lines=[('m', 'ಕಸ ಎತ್ತಿಕೊಂಡು ಹೋಗ್ತಾರೆ. ಆಮೇಲೆ ಎಲ್ಲಿ ಹಾಕ್ತಾರೆ?', 'They pick up the garbage. Then where do they dump it?')], src=CAG),

 dict(kicker=('ಸಿಎಜಿ · 35 ನಗರ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು', 'The national auditor · 35 towns'), m_expr='skeptic', k_expr='ask',
      card_kn='<div class="h">ನೂರು ಕೆಜಿ ಕಸದಲ್ಲಿ 26 ಕೆಜಿ ಮಾತ್ರ ಸಂಸ್ಕರಣೆ. ಉಳಿದದ್ದು ಊರ ಹೊರಗೆ.</div><div class="sub">Test-checked towns, 2012-13 to 2016-17</div>',
      card_en='<div class="h">Of every 100 kg collected, only 26 kg was processed.</div><div class="sub">The rest was dumped. ಉಳಿದದ್ದು ಊರ ಹೊರಗೆ.</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ನೂರು ಕೆಜಿ ಕಸದಲ್ಲಿ ಇಪ್ಪತ್ತಾರು ಕೆಜಿ ಮಾತ್ರ ಸಂಸ್ಕರಣೆ ಆಯ್ತು.', 'Dad, of every 100 kilos, only 26 were processed.'),
             ('m', 'ಉಳಿದ ಎಪ್ಪತ್ನಾಲ್ಕು ಕೆಜಿ ನಮ್ಮ ಊರ ಹೊರಗೆ!', 'And the other 74 lands at the edge of our town!')], src=CAG),

 dict(kicker=('ನಂಜನಗೂಡು · ಮೈಸೂರು ಜಿಲ್ಲೆ', 'Nanjangud · Mysuru district'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="h">ಜಿಪಿಎಸ್ ಇಲ್ಲದ ವಾಹನಗಳು. ಕಸ ಕಬಿನಿ ನದಿ ದಡದಲ್ಲಿ.</div><div class="sub">"Unauthorised dumping of waste near the bank of River Kabini"</div>',
      card_en='<div class="h">No working GPS on the trucks. Garbage dumped on the bank of the Kabini.</div><div class="sub">"Unauthorised dumping of waste near the bank of River Kabini" (CAG)</div>',
      lines=[('k', 'ನಂಜನಗೂಡಿನಲ್ಲಿ ಕಸ ಕಬಿನಿ ನದಿಯ ದಡಕ್ಕೆ ಹೋಯ್ತು.', 'In Nanjangud, the garbage went to the bank of the Kabini river.')], src=CAG),

 dict(kicker=('ಹಣ ಇತ್ತು', 'The money was there'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಮಾರ್ಚ್ 2017ಕ್ಕೆ ಖರ್ಚಾಗದೆ ಉಳಿದ ಕಸ ನಿರ್ವಹಣೆ ಹಣ</small><b class="r">₹93.19 ಕೋಟಿ</b></div><div class="row"><small>ಪ್ರತಿದಿನ ಗುಡಿಸದ ರಸ್ತೆಗಳು</small><b>83%</b></div>',
      card_en='<div class="row"><small>Waste-management money unspent, March 2017</small><b class="r">Rs 93.19 cr</b></div><div class="row"><small>Roads not swept daily</small><b>83%</b></div>',
      lines=[('m', 'ತೊಂಬತ್ಮೂರು ಕೋಟಿ ಹಣ ಇತ್ತು. ಖರ್ಚೇ ಮಾಡಿಲ್ಲ!', 'Rs 93 crore was sitting there. Never spent!'),
             ('k', 'ಪೌರಕಾರ್ಮಿಕರ ಹುದ್ದೆಗಳಲ್ಲಿ ಅರವತ್ತೈದು ಪರ್ಸೆಂಟ್ ಕೊರತೆ.', 'And 65 percent of sanitation-worker posts were short.')], src=CAG),

 dict(kicker=('ದಂಡ', 'The fine'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">₹2,900<small> ಕೋಟಿ</small></div><div class="h">ಕಸ ಮತ್ತು ಕೊಳಚೆ ನೀರಿನ ಅವ್ಯವಸ್ಥೆಗೆ ಹಸಿರು ನ್ಯಾಯಮಂಡಳಿ ದಂಡ (2022)</div>',
      card_en='<div class="big r">Rs 2,900<small> cr</small></div><div class="h">Green Tribunal compensation for solid and liquid waste (2022)</div>',
      lines=[('m', 'ಕೊನೆಗೆ ದಂಡ ಎರಡು ಸಾವಿರದ ಒಂಬೈನೂರು ಕೋಟಿ. ಕಟ್ಟೋದು ಯಾರು? ನಾವೇ!', 'In the end, a Rs 2,900 crore penalty. Who pays? We do!')], src=NGT),

 dict(kicker=('ಮಾಡಲು ಸಾಧ್ಯ', 'It can be done'), m_expr='smile', k_expr='smile',
      card_kn='<div class="row"><small>ಇಂದೋರ್ · ದೇಶದ ಅತಿ ಸ್ವಚ್ಛ ನಗರ</small><b>8 ವರ್ಷ ಸತತ</b></div><div class="row"><small>ಮೈಸೂರು · ಸೂಪರ್ ಸ್ವಚ್ಛ ಲೀಗ್</small><b>2024-25</b></div>',
      card_en='<div class="row"><small>Indore · India\'s cleanest city</small><b>8 years running</b></div><div class="row"><small>Mysuru · Super Swachh League</small><b>2024-25</b></div>',
      lines=[('k', 'ಮೈಸೂರು ಮಾಡಿ ತೋರಿಸಿದೆ. ಉಳಿದ ಊರುಗಳಿಗೆ ಯಾಕೆ ಆಗಲ್ಲ?', 'Mysuru has done it. Why can\'t the other towns?')], src=SS + '. ' + FAIR),

 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ಸ್ವಚ್ಛತಾ ಆ್ಯಪ್‌ನಲ್ಲಿ ದೂರು ಕೊಡಿ. ಆರ್‌ಟಿಐ: ನಮ್ಮ ವಾರ್ಡ್‌ನ ಕಸ ಎಷ್ಟು ಸಂಗ್ರಹ, ಎಷ್ಟು ಸಂಸ್ಕರಣೆ?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Complain on the Swachhata app. File an RTI: how much of our ward\'s garbage is collected, and how much processed?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಆರ್‌ಟಿಐ ಹಾಕಿ: ನಮ್ಮ ವಾರ್ಡ್ ಕಸ ಎಲ್ಲಿಗೆ ಹೋಗುತ್ತೆ?', 'File an RTI: where does our ward\'s garbage go?')], src=ASK),

 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]

# The owner's recorded chorus is reused on every Kannada episode.
REC = {'kn': {'chorus': 'voice/ep11/chorus.wav'}}

META = {
 'kn': {'title': 'ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #10: ಕಸದ ಲೆಕ್ಕ | Only 26% of garbage processed #Shorts',
        'description': ('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ, ಸಂಚಿಕೆ 10: ಕಸದ ಲೆಕ್ಕ. ಸಿಎಜಿ ಪರಿಶೀಲಿಸಿದ ನಗರಗಳು ಸಂಗ್ರಹಿಸಿದ ಕಸದಲ್ಲಿ ಕೇವಲ 26% ಸಂಸ್ಕರಿಸಿದವು.\n\n'
                        'Mallanna Asks, episode 10: the garbage account. (Fictional characters; every figure is real.)\n'
                        '- The national auditor (CAG) found test-checked towns processed only 26% of the waste they collected (2012-13 to 2016-17).\n'
                        '- 6,935 of 8,324 km of roads (83%) were not swept daily.\n'
                        '- Rs 93.19 crore of waste-management money sat unspent at the end of March 2017.\n'
                        '- In Nanjangud, trucks without working GPS dumped waste near the bank of the River Kabini.\n'
                        '- Posts short: Environment Engineers 32%, Health Inspectors 70%, sanitation workers (pourakarmikas) 65%.\n'
                        '- In October 2022 the National Green Tribunal set Rs 2,900 crore as environmental compensation for solid and liquid waste.\n'
                        '- Indore has been India\'s cleanest city for 8 years; Mysuru is in the 2024-25 Super Swachh League.\n'
                        'The audit years were mostly under the Congress government; the NGT penalty came under the BJP government.\n\n'
                        'What you can do: complain on the Swachhata app; file an RTI for your ward\'s garbage collected vs processed. Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
                        'Sources: CAG Report No. 4 of 2018 (Solid Waste Management in ULBs, Karnataka); National Green Tribunal order, Oct 2022 (PTI); Swachh Survekshan 2024-25 results.\n'
                        'Every figure comes from a public record. If one is wrong, tell us and we will correct it. Music: original.\n\n'
                        '#MallannaAsks #Karnataka #ಕನ್ನಡ #SwachhBharat #KnowYourMLA')},
 'en': {'title': 'Mallanna Asks #10: The garbage account | Only 26% of waste processed #Shorts',
        'description': ('Mallanna Asks, episode 10. Your town collects the garbage. Then what? (Fictional characters; every figure is real.)\n'
                        '- The national auditor (CAG) found test-checked Karnataka towns processed only 26% of the waste they collected (2012-13 to 2016-17).\n'
                        '- 83% of roads (6,935 of 8,324 km) were not swept daily.\n'
                        '- Rs 93.19 crore of waste-management money sat unspent in March 2017.\n'
                        '- In Nanjangud, garbage was dumped near the bank of the River Kabini.\n'
                        '- 65% of sanitation-worker posts were short.\n'
                        '- The National Green Tribunal set Rs 2,900 crore as environmental compensation (Oct 2022).\n'
                        '- Indore: India\'s cleanest city 8 years running. Mysuru: in the 2024-25 Super Swachh League.\n'
                        'The audit years were mostly under Congress; the NGT penalty came under the BJP.\n\n'
                        'What you can do: complain on the Swachhata app; file an RTI for your ward\'s garbage collected vs processed. Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
                        'Sources: CAG Report No. 4 of 2018; National Green Tribunal, Oct 2022 (PTI); Swachh Survekshan 2024-25.\n'
                        'Every figure comes from a public record. If one is wrong, tell us and we will correct it. Music: original.\n\n'
                        '#MallannaAsks #Karnataka #India #SwachhBharat #CleanCities')},
}
