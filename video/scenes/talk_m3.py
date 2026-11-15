# Mallanna Asks, Episode 3: "Kaveri's school" (ಕಾವೇರಿಯ ಶಾಲೆ)
# Talking-character version of ep3.py. Every figure, quote and source is carried over unchanged from that file
# and the published description in upload_all.json. Nothing new added. The quote is attributed as reported;
# the not-charged line stays on screen with it.
BPM = 96

VAC = "Source: School Education Minister's reply in the Legislative Assembly, 18 December 2025"
PC = 'Source: UDISE+ 2025-26, reported by ThePrint'
ENR = 'Source: School Education Minister in the Assembly, December 2025 (The Week/PTI)'
NEF = "Source: National Education Foundation's own website (gat.ac.in, About NEF), November 2026"
QUO = 'Source: Daily Pioneer, 7 November 2026 (remarks at a government CSR event on school adoption)'
OLD = 'Sources: CAG (2021-22); Assembly reply, December 2025'
CLEAR = 'Aishwarya DKS Hegde has not been charged with anything; this video responds only to her public statement.'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-3 s hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 3 · ಕಾವೇರಿಯ ಶಾಲೆ', "Mallanna Asks · Episode 3 · Kaveri's school"),
      hit=True, m_expr='skeptic', k_expr='sad',
      card_kn='<div class="big r">45,590</div><div class="h">ಪ್ರಾಥಮಿಕ ಶಿಕ್ಷಕರ ಹುದ್ದೆ ಖಾಲಿ</div><div class="sub">1,78,935 ಹುದ್ದೆಗಳಲ್ಲಿ (25.5%) · ಡಿಸೆಂಬರ್ 2025</div>',
      card_en='<div class="big r">45,590</div><div class="h">primary teacher posts vacant</div><div class="sub">of 1,78,935 posts (25.5%) · December 2025</div>',
      lines=[('m', 'ಸ್ಮಾರ್ಟ್ ಕ್ಲಾಸ್ ಆಮೇಲೆ ಸ್ವಾಮಿ. ಮೊದಲು ಗಣಿತ ಮೇಷ್ಟ್ರು ಕೊಡಿ.', 'Smart class later, sir. First give us a maths teacher.')], src=VAC),

 dict(kicker=('ಬೋಧನೆಗೆ ಕಂಪ್ಯೂಟರ್ ಇರುವ ಶಾಲೆಗಳು', 'Schools with computers for teaching'), hit=True, m_expr='neutral', k_expr='sad',
      card_kn='<div class="row"><small>ಸರ್ಕಾರಿ ಶಾಲೆಗಳು</small><b class="r">37.8%</b></div><div class="row"><small>ಖಾಸಗಿ ಶಾಲೆಗಳು</small>84.3%</div><div class="row"><small>ಸರ್ಕಾರಿ ಶಾಲೆ ದಾಖಲಾತಿ, 15 ವರ್ಷದಲ್ಲಿ</small><b class="r">−17 ಲಕ್ಷ</b></div>',
      card_en='<div class="row"><small>Government schools</small><b class="r">37.8%</b></div><div class="row"><small>Private schools</small>84.3%</div><div class="row"><small>Govt school enrolment, last 15 years</small><b class="r">−17 lakh</b></div>',
      lines=[('k', 'ಅಪ್ಪಾ, ನಮ್ಮ ಕ್ಲಾಸಿಗೆ ಗಣಿತ ಮೇಷ್ಟ್ರೇ ಇಲ್ಲ.', 'Dad, our class has no maths teacher.')], src=PC + '; ' + ENR),

 dict(kicker=('ದಾಖಲೆಯಲ್ಲಿ', 'On the record'), m_expr='skeptic', k_expr='ask',
      card_kn='<div class="h">ಮುಖ್ಯಮಂತ್ರಿ ಕುಟುಂಬದ ಟ್ರಸ್ಟ್ ಖಾಸಗಿ ಶಾಲೆ ಮತ್ತು ಕಾಲೇಜುಗಳನ್ನು ನಡೆಸುತ್ತದೆ.</div><div class="sub">ನ್ಯಾಷನಲ್ ಎಜುಕೇಶನ್ ಫೌಂಡೇಶನ್ ಟ್ರಸ್ಟಿಗಳು: ಉಷಾ ಶಿವಕುಮಾರ್ (ಅಧ್ಯಕ್ಷೆ), ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್, ಡಿ.ಕೆ. ಸುರೇಶ್, ಐಶ್ವರ್ಯ ಡಿಕೆಎಸ್ ಹೆಗ್ಡೆ (ಕಾರ್ಯದರ್ಶಿ ಟ್ರಸ್ಟಿ).</div>',
      card_en='<div class="h">The Chief Minister\'s family trust runs a private school and colleges.</div><div class="sub">National Education Foundation trustees: Usha Shivakumar (chair), D.K. Shivakumar, D.K. Suresh, Aishwarya DKS Hegde (secretary trustee).</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಮುಖ್ಯಮಂತ್ರಿ ಕುಟುಂಬದ ಟ್ರಸ್ಟ್ ಖಾಸಗಿ ಶಾಲೆ ನಡೆಸುತ್ತಂತೆ.', "Dad, the Chief Minister's family trust runs a private school.")], src=NEF),

 dict(kicker=('ನವೆಂಬರ್ 2026, ಸರ್ಕಾರಿ ಕಾರ್ಯಕ್ರಮದಲ್ಲಿ, ವರದಿಯಾದಂತೆ', 'November 2026, at a government event, as reported'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">&ldquo;More than teacher shortage, low efficiency is the problem.&rdquo;</div><div class="sub">ಐಶ್ವರ್ಯ ಡಿಕೆಎಸ್ ಹೆಗ್ಡೆ, ಸರ್ಕಾರಿ ಶಿಕ್ಷಕರ ಬಗ್ಗೆ. ವಿರೋಧ ಪಕ್ಷ ಕ್ಷಮೆ ಕೇಳಲು ಒತ್ತಾಯಿಸಿತು.</div>',
      card_en='<div class="h">&ldquo;More than teacher shortage, low efficiency is the problem.&rdquo;</div><div class="sub">Aishwarya DKS Hegde, on government teachers. An opposition MLC asked her to apologise.</div>',
      lines=[('m', 'ಖಾಲಿ ಹುದ್ದೆಯಲ್ಲಿ ದಕ್ಷತೆ ಹೇಗೆ ಬರುತ್ತೆ ಮೇಡಂ? ಮೊದಲು ಹುದ್ದೆ ತುಂಬಿಸಿ.', 'How does an empty post become efficient, madam? Fill the posts first.')],
      src=QUO + '. ' + CLEAR),

 # fairness: the other government too
 dict(kicker=('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="big">26%</div><div class="h">2021-22ರಲ್ಲಿ, ಬಿಜೆಪಿ ಸರ್ಕಾರದಲ್ಲೂ, ಈ ಹುದ್ದೆಗಳು ಖಾಲಿ ಇದ್ದವು.</div>',
      card_en='<div class="big">26%</div><div class="h">of these posts were also empty in 2021-22, under the BJP.</div>',
      lines=[('m', 'ಎರಡು ಸರ್ಕಾರ. ನಾಲ್ಕು ವರ್ಷ. ಬದಲಾವಣೆ ಬಹುತೇಕ ಇಲ್ಲ.', 'Two governments, four years, almost no change.')], src=OLD),

 dict(kicker=('ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ', "Kaveri's question"), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ನಮ್ಮ ಶಾಲೆಗೆ ಶಿಕ್ಷಕರು ಯಾವಾಗ?</div><div class="sub">ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ. ಅವರನ್ನು ಇಲ್ಲಿ ನೋಡಿ:</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">When does our school get its teachers?</div><div class="sub">Ask your MLA. Look them up:</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('k', 'ನಮ್ಮ ಶಾಲೆಗೆ ಶಿಕ್ಷಕರು ಯಾವಾಗ ಬರ್ತಾರೆ?', 'When does our school get its teachers?')], src=ASK + ' ' + CLEAR),

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
