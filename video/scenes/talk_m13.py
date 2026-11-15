# Mallanna Asks, Season 2, Episode 13: "1,452 lakes to 194" (1,452 ಕೆರೆ → 194)
# Figures re-checked 2026-11-14 against CAG Report No. 2 of 2021, Performance Audit of Storm Water Management in
# Bengaluru (2013-14 to 2017-18), Executive Summary: 1,452 water bodies / 35 TMC in the early 1800s (IISc study cited);
# 194 / 5 TMC by 2016; 1.2 TMC after siltation; sewage 780 MLD mixed with storm water; no action on 714 of 2,626 identified
# encroachments; Rs 83.59 crore JNNURM assistance lost.
BPM = 96

CAG = 'Source: CAG Report No. 2 of 2021, Storm Water Management in Bengaluru (2013-14 to 2017-18), citing an IISc study'
FAIR = ('Source: CAG Report No. 2 of 2021. The audit years were under the Congress government (2013-18); '
        'the report was tabled in 2021 under the BJP government.')
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 13', 'Mallanna Asks · Episode 13'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">1,452 → 194</div><div class="h">ಬೆಂಗಳೂರಿನ ಕೆರೆಗಳು (1800ರ ದಶಕ → 2016)</div>',
      card_en='<div class="big r">1,452 → 194</div><div class="h">Bengaluru\'s lakes (early 1800s → 2016)</div>',
      lines=[('m', 'ಕೆರೆ ಇದ್ದ ಜಾಗದಲ್ಲಿ ಈಗ ಮಳೆ ನೀರು ಮನೆಗೆ ನುಗ್ಗುತ್ತೆ!', 'Where the lakes were, the rain now pours into our homes!')], src=CAG),

 dict(kicker=('ಸಿಎಜಿ ವರದಿ', 'The national auditor'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>1800ರ ದಶಕ · ಸಂಗ್ರಹ ಸಾಮರ್ಥ್ಯ</small>35 TMC</div><div class="row"><small>2016 · ಹೂಳಿನ ನಂತರ ಉಳಿದದ್ದು</small><b class="r">1.2 TMC</b></div>',
      card_en='<div class="row"><small>Early 1800s · storage</small>35 TMC</div><div class="row"><small>2016 · left after silting</small><b class="r">1.2 TMC</b></div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಮೂವತ್ತೈದು ಟಿಎಂಸಿ ನೀರು ಹಿಡಿಯುತ್ತಿದ್ದ ಕೆರೆಗಳಲ್ಲಿ ಈಗ ಒಂದೂವರೆ ಕೂಡ ಇಲ್ಲ.', 'Dad, lakes that held 35 TMC now hold barely 1.2.')], src=CAG),

 dict(kicker=('ಮಳೆ ನೀರು ಚರಂಡಿ', 'The stormwater drains'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">780<small> MLD</small></div><div class="h">ಕೊಳಚೆ ನೀರು ಮಳೆ ನೀರಿನ ಚರಂಡಿಗಳಿಗೆ, ಪ್ರತಿದಿನ</div>',
      card_en='<div class="big r">780<small> MLD</small></div><div class="h">of sewage flows into the stormwater drains, every day</div>',
      lines=[('m', 'ಮಳೆ ನೀರಿನ ಚರಂಡಿಯಲ್ಲಿ ಕೊಳಚೆ ನೀರು! ಮಳೆ ಬಂದರೆ ಎಲ್ಲಿ ಹೋಗಬೇಕು?', 'Sewage in the rain drains! When it rains, where does the water go?')], src=CAG),

 dict(kicker=('ಒತ್ತುವರಿ', 'Encroachments'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಗುರುತಿಸಿದ ಚರಂಡಿ ಒತ್ತುವರಿಗಳು</small>2,626</div><div class="row"><small>ಕ್ರಮವೇ ಆಗದವು</small><b class="r">714</b></div><div class="row"><small>ಕೈ ತಪ್ಪಿದ ಕೇಂದ್ರ ನೆರವು</small><b class="r">₹83.59 ಕೋಟಿ</b></div>',
      card_en='<div class="row"><small>Drain encroachments identified</small>2,626</div><div class="row"><small>No action taken</small><b class="r">714</b></div><div class="row"><small>Central aid lost</small><b class="r">Rs 83.59 cr</b></div>',
      lines=[('k', 'ಏಳುನೂರ ಹದಿನಾಲ್ಕು ಒತ್ತುವರಿಗಳ ಮೇಲೆ ಕ್ರಮವೇ ಇಲ್ಲ.', 'No action at all on 714 encroachments.'),
             ('m', 'ಎಂಬತ್ಮೂರು ಕೋಟಿ ಕೇಂದ್ರದ ಹಣವೂ ಕೈ ತಪ್ಪಿತು!', 'And Rs 83 crore of central money was lost too!')], src=FAIR),

 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ನಿಮ್ಮ ಬಡಾವಣೆಯ ಕೆರೆ ಮತ್ತು ಚರಂಡಿಯ ಒತ್ತುವರಿ ಪಟ್ಟಿ ಕೇಳಿ: ಎಷ್ಟು ತೆರವು, ಎಷ್ಟು ಬಾಕಿ?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Ask for your area\'s lake and drain encroachment list: how many cleared, how many pending?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಕೇಳಿ: ನಮ್ಮ ಕೆರೆ ಒತ್ತುವರಿ ಎಷ್ಟು ತೆರವಾಯ್ತು?', 'Ask: how much of our lake\'s encroachment has been cleared?')], src=ASK),

 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]

REC = {'kn': {'chorus': 'voice/ep11/chorus.wav'}}

_FACTS = ('- The national auditor (CAG), citing an IISc study: Bengaluru had 1,452 water bodies holding 35 TMC in the early 1800s; by 2016, 194, with only 1.2 TMC usable after silting.\n'
          '- 780 MLD of sewage flows into the stormwater drains.\n'
          '- BBMP had taken no action on 714 of 2,626 identified drain encroachments.\n'
          '- Rs 83.59 crore of central (JNNURM) assistance was lost because works were left incomplete.\n'
          'The audit years were under the Congress government (2013-18); the report was tabled in 2021 under the BJP government.\n\n')
_SRC = ('Source: CAG Report No. 2 of 2021, Performance Audit of Storm Water Management in Bengaluru (2013-14 to 2017-18).\n'
        'Every figure comes from a public record. If one is wrong, tell us and we will correct it. Music: original.')
META = {
 'kn': {'title': 'ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #13: 1,452 ಕೆರೆ → 194 | Where Bengaluru\'s lakes went #Shorts',
        'description': ('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ, ಸಂಚಿಕೆ 13: ಬೆಂಗಳೂರಿನಲ್ಲಿ 1,452 ಕೆರೆಗಳಿದ್ದವು; 2016ಕ್ಕೆ 194.\n\n'
                        'Mallanna Asks, episode 13. (Fictional characters; every figure is real.)\n' + _FACTS +
                        'What you can do: ask for your area\'s lake and drain encroachment list. Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
                        + _SRC + '\n\n#MallannaAsks #Karnataka #ಕನ್ನಡ #Bengaluru #Lakes')},
 'en': {'title': 'Mallanna Asks #13: Bengaluru had 1,452 lakes. Now 194 #Shorts',
        'description': ('Mallanna Asks, episode 13. Where the lakes were, the rain now goes into homes. (Fictional characters; every figure is real.)\n' + _FACTS +
                        'What you can do: ask for your area\'s lake and drain encroachment list. Look up your MLA: https://jarvisss007.github.io/know-your-mla\n\n'
                        + _SRC + '\n\n#MallannaAsks #Bengaluru #Lakes #UrbanFlooding #India')},
}
