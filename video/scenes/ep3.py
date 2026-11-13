import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chars import stage, stage2, mallanna, kaveri, STYLE, bi

VAC = "Source: School Education Minister's reply in the Legislative Assembly, 18 December 2025"
PC = 'Source: UDISE+ 2025-26, reported by ThePrint'
ENR = 'Source: School Education Minister in the Assembly, December 2025 (The Week/PTI)'
NEF = "Source: National Education Foundation's own website (gat.ac.in, About NEF), November 2026"
QUO = 'Source: Daily Pioneer, 7 November 2026 (remarks at a government CSR event on school adoption)'
OLD = 'Sources: CAG (2021-22); Assembly reply, December 2025'
END = 'Fictional characters; real records. Aishwarya DKS Hegde has not been charged with anything; this video responds only to her public statement.'

def scenes(L):
    S = STYLE
    t = lambda kn, en: kn if L == 'kn' else en
    sub = lambda kn, en: '<div class="en">%s</div>' % (en if L == 'kn' else kn)
    return [
     (5.0, S + '<div class="k">%s</div>' % t('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 3 · ಕಾವೇರಿಯ ಶಾಲೆ', "Mallanna Asks · Episode 3 · Kaveri's school")
      + bi('ನಿಮ್ಮ ಶಾಲೆಗೆ ಸ್ಮಾರ್ಟ್ ಕ್ಲಾಸ್ ಕೊಡ್ತೀನಿ!', 'I will give your school a smart class!', L, 'b n')
      + bi('ಮೊದಲು ಗಣಿತ ಮೇಷ್ಟ್ರು ಕೊಡಿ ಸ್ವಾಮಿ.', 'First give us a maths teacher, sir.', L)
      + stage('skeptic', 'namaste'), ''),

     (6.0, S + bi('ಅಪ್ಪಾ, ನಮ್ಮ ಕ್ಲಾಸಿಗೆ ಗಣಿತ ಮೇಷ್ಟ್ರೇ ಇಲ್ಲ.', 'Dad, our class has no maths teacher.', L, 'b', 'background:#8fd3ff')
      + stage2([(mallanna('neutral'), 10, -40, 0.9), (kaveri('sad'), 520, 80, 1.0)])
      + '<div class="fact"><b>45,590 / 1,78,935</b><span>%s</span><i>%s</i></div>' % (
          t('ಪ್ರಾಥಮಿಕ ಶಿಕ್ಷಕರ ಹುದ್ದೆಗಳು ಖಾಲಿ (25.5%)', 'Primary teacher posts vacant (25.5%)'),
          t('Primary teacher posts vacant in Karnataka, December 2025.', 'ಡಿಸೆಂಬರ್ 2025, ಕರ್ನಾಟಕ.')), VAC),

     (5.5, S + '<div class="k">%s</div>' % t('ಬೋಧನೆಗೆ ಕಂಪ್ಯೂಟರ್ ಇರುವ ಶಾಲೆಗಳು', 'Schools with computers for teaching')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">37.8%%</b></div>' % t('ಸರ್ಕಾರಿ ಶಾಲೆಗಳು', 'Government schools')
      + '<div class="row"><small>%s</small>84.3%%</div>' % t('ಖಾಸಗಿ ಶಾಲೆಗಳು', 'Private schools')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">−17 %s</b></div>' % (t('ಸರ್ಕಾರಿ ಶಾಲೆ ದಾಖಲಾತಿ, 15 ವರ್ಷದಲ್ಲಿ', 'Government school enrolment, last 15 years'), t('ಲಕ್ಷ', 'lakh')),
      PC + '; ' + ENR),

     (6.5, S + '<div class="k">%s</div>' % t('ದಾಖಲೆಯಲ್ಲಿ', 'On the record')
      + '<h2>%s</h2>' % t('ಮುಖ್ಯಮಂತ್ರಿ ಕುಟುಂಬದ ಟ್ರಸ್ಟ್ ಖಾಸಗಿ ಶಾಲೆ ಮತ್ತು ಕಾಲೇಜುಗಳನ್ನು ನಡೆಸುತ್ತದೆ.', "The Chief Minister's family trust runs a private school and colleges.")
      + sub('ನ್ಯಾಷನಲ್ ಎಜುಕೇಶನ್ ಫೌಂಡೇಶನ್ ಟ್ರಸ್ಟಿಗಳು: ಉಷಾ ಶಿವಕುಮಾರ್ (ಅಧ್ಯಕ್ಷೆ), ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್, ಡಿ.ಕೆ. ಸುರೇಶ್, ಐಶ್ವರ್ಯ ಡಿಕೆಎಸ್ ಹೆಗ್ಡೆ (ಕಾರ್ಯದರ್ಶಿ ಟ್ರಸ್ಟಿ).',
            'National Education Foundation trustees: Usha Shivakumar (chair), D.K. Shivakumar, D.K. Suresh and Aishwarya DKS Hegde (secretary trustee). It runs Global Academy of Technology and National Hill View Public School.'), NEF),

     (6.5, S + '<div class="k">%s</div>' % t('ನವೆಂಬರ್ 2026, ಸರ್ಕಾರಿ ಕಾರ್ಯಕ್ರಮದಲ್ಲಿ, ವರದಿಯಾದಂತೆ', 'November 2026, at a government event, as reported')
      + '<h2>&ldquo;More than teacher shortage, low efficiency is the problem.&rdquo;</h2>'
      + sub('ಐಶ್ವರ್ಯ ಡಿಕೆಎಸ್ ಹೆಗ್ಡೆ, ಸರ್ಕಾರಿ ಶಿಕ್ಷಕರ ಬಗ್ಗೆ. ವಿರೋಧ ಪಕ್ಷ ಕ್ಷಮೆ ಕೇಳಲು ಒತ್ತಾಯಿಸಿತು.',
            'Aishwarya DKS Hegde, on government teachers. An opposition MLC asked her to apologise.'), QUO),

     (5.5, S + bi('ಖಾಲಿ ಹುದ್ದೆಯಲ್ಲಿ ದಕ್ಷತೆ ಹೇಗೆ ಬರುತ್ತೆ ಮೇಡಂ? ಮೊದಲು ಹುದ್ದೆ ತುಂಬಿಸಿ.', 'How does an empty post become efficient, madam? Fill the posts first.', L)
      + stage('firm', 'smug', 'point', show_neta=False), ''),

     (5.0, S + '<div class="k">%s</div>' % t('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair')
      + '<h2>%s</h2>' % t('2021-22ರಲ್ಲಿ, ಬಿಜೆಪಿ ಸರ್ಕಾರದಲ್ಲೂ, 26% ಹುದ್ದೆ ಖಾಲಿ ಇತ್ತು.', 'In 2021-22, under the BJP, 26% of these posts were also empty.')
      + sub('ಎರಡು ಸರ್ಕಾರ. ನಾಲ್ಕು ವರ್ಷ. ಬದಲಾವಣೆ ಬಹುತೇಕ ಇಲ್ಲ.', 'Two governments, four years, almost no change.'), OLD),

     (6.5, S + '<h1 style="font-size:%dpx">%s<br><span style="color:#f2b705">%s</span></h1>' % ((92, 'ಕೆಲಸ ತೋರಿಸಿ.', 'ಆಮೇಲೆ ಮತ.') if L == 'kn' else (88, 'Show me the work.', 'Then my vote.'))
      + stage2([(mallanna('firm'), 10, -40, 0.9), (kaveri('ask'), 520, 80, 1.0)], label=False)
      + '<div class="mid" style="font-size:40px;margin:14px 0 0">%s</div>' % t('ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ #3: ನಮ್ಮ ಶಾಲೆಗೆ ಶಿಕ್ಷಕರು ಯಾವಾಗ?', "Kaveri's question: when does our school get its teachers?")
      + '<div class="url" style="margin-top:12px">jarvisss007.github.io/know-your-mla</div>', END),
    ]

L = os.environ.get('LANG_OUT', 'kn')
SCENES = scenes(L)
OUT = 'mallanna3-%s.mp4' % L
FPS = 10
