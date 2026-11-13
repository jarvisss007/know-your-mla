import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chars import stage, stage2, mallanna, kaveri, STYLE, bi

METRO = 'Sources: Union Cabinet approval, January 2014; Karnataka cabinet, 22 May 2025 (The Week/PTI); BMRCL fare revision, 9 February 2025 (The Week)'
KK = 'Sources: State figures reported by The Week, 19 September 2024 (KKRDB 2013-14 to 2024-25); Karnataka cabinet, 22 May 2025'
CAG = 'Source: CAG Report No. 10 of 2022, Functioning of the Kalyana Karnataka Region Development Board'
END = 'Fictional characters. Metro costs are shared by the Centre, the state and loans. Every figure comes from a public record; if one is wrong, tell us.'

def scenes(L):
    S = STYLE
    t = lambda kn, en: kn if L == 'kn' else en
    sub = lambda kn, en: '<div class="en">%s</div>' % (en if L == 'kn' else kn)
    return [
     (5.0, S + '<div class="k">%s</div>' % t('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 9 · ಉತ್ತರ ಮತ್ತು ದಕ್ಷಿಣ', 'Mallanna Asks · Episode 9 · North and South')
      + bi('ಬೆಂಗಳೂರಿಗೆ ಮೆಟ್ರೋ! ಕರ್ನಾಟಕದ ಹೆಮ್ಮೆ!', 'A metro for Bengaluru! The pride of Karnataka!', L, 'b n')
      + bi('ಕಲಬುರಗಿಯೂ ಕರ್ನಾಟಕನೇ ಸ್ವಾಮಿ.', 'Kalaburagi is Karnataka too, sir.', L)
      + stage('skeptic', 'namaste'), ''),

     (6.0, S + '<div class="k">%s</div>' % t('ನಮ್ಮ ಮೆಟ್ರೋ · ಹಂತ 2', 'Namma Metro · Phase 2')
      + '<div class="row"><small>%s</small>₹26,405 %s</div>' % (t('2014 · ಅನುಮೋದನೆ, ಗಡುವು 2020', '2014 · approved, due 2020'), t('ಕೋಟಿ', 'cr'))
      + '<div class="row"><small>%s</small><b style="color:#ef5261">₹40,425 %s</b></div>' % (t('2025 · ಪರಿಷ್ಕೃತ, ಈಗ 2027', '2025 · revised, now due 2027'), t('ಕೋಟಿ', 'cr'))
      + '<div class="row"><small>%s</small>₹60 → <b style="color:#ef5261">₹90</b></div>' % t('ಗರಿಷ್ಠ ಟಿಕೆಟ್ ದರ · ಫೆಬ್ರವರಿ 2025', 'Top fare · February 2025'), METRO),

     (6.5, S + '<div class="k">%s</div>' % t('ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ ಮಂಡಳಿ · 7 ಜಿಲ್ಲೆ · 12 ವರ್ಷ', 'Kalyana Karnataka board · 7 districts · 12 years')
      + '<div class="row"><small>%s</small>₹19,778 %s</div>' % (t('ಹಂಚಿಕೆ, 2013-14 ರಿಂದ 2024-25', 'Allocated, 2013-14 to 2024-25'), t('ಕೋಟಿ', 'cr'))
      + '<div class="row"><small>%s</small>₹13,229 %s</div>' % (t('ಬಿಡುಗಡೆ', 'Released'), t('ಕೋಟಿ', 'cr'))
      + '<div class="row"><small>%s</small><b style="color:#ef5261">₹11,174 %s</b></div>' % (t('ಖರ್ಚು', 'Spent'), t('ಕೋಟಿ', 'cr'))
      + sub('ಒಂದು ಮೆಟ್ರೋ ಹಂತದ ವೆಚ್ಚ ಏಳು ಜಿಲ್ಲೆಗಳ 12 ವರ್ಷದ ಹಂಚಿಕೆಯ ಎರಡು ಪಟ್ಟು.',
            "One metro phase costs twice what seven districts were allocated in 12 years."), KK),

     (6.0, S + '<div class="k">%s</div>' % t('ರಾಷ್ಟ್ರೀಯ ಲೆಕ್ಕಪರಿಶೋಧಕರು ಕಂಡದ್ದು', 'What the national auditor found')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">₹387.52 %s</b></div>' % (t('ಬಳಸದ ಕಾರಣ ಕಳೆದುಕೊಂಡ ನೆರವು', 'Assistance lost because funds went unused'), t('ಕೋಟಿ', 'cr'))
      + '<div class="row"><small>%s</small><b style="color:#ef5261">3,731</b></div>' % t('ರದ್ದಾದ ಕಾಮಗಾರಿಗಳು (₹738.65 ಕೋಟಿ)', 'Works cancelled (Rs 738.65 cr)')
      + sub('ಸರ್ಕಾರ ಮೊದಲ ಅಂಶವನ್ನು ಒಪ್ಪುವುದಿಲ್ಲ. ಹಣ ಬಂದರೂ ಖರ್ಚಾಗಲಿಲ್ಲ.', 'The government disputes the first figure. Even the money that came was not spent.'), CAG),

     (6.0, S + '<div class="k">%s</div>' % t('ಪ್ರತಿ ವ್ಯಕ್ತಿಯ ಆದಾಯ ಏರಿಕೆ · 2013-14 ರಿಂದ 2019-20', 'Growth in income per person · 2013-14 to 2019-20')
      + '<div class="row"><small>%s</small>74.84%%</div>' % t('ಕರ್ನಾಟಕ', 'Karnataka')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">47.96%%</b></div>' % t('ಕಲಬುರಗಿ', 'Kalaburagi')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">76%%</b></div>' % t('ಯಾದಗಿರಿ: ರಕ್ತಹೀನ ಮಕ್ಕಳು, ರಾಜ್ಯದಲ್ಲೇ ಅತಿ ಹೆಚ್ಚು', 'Yadgir: children with anaemia, highest in the state'), CAG),

     (5.0, S + '<div class="k">%s</div>' % t('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair')
      + '<h2>%s</h2>' % t('2013ರ 371ಜೆ ಕಲಮು ಈ ಭಾಗಕ್ಕೆ ಮೀಸಲು ಉದ್ಯೋಗ, ಸೀಟು ಮತ್ತು ಸ್ವಂತ ಮಂಡಳಿ ಕೊಟ್ಟಿತು.', 'Article 371J (2013) gave the region reserved jobs, college seats and its own board.')
      + sub('ಹಕ್ಕು ಸಿಕ್ಕಿತು. ಹಣ ಪೂರ್ತಿ ಬರಲಿಲ್ಲ, ಬಂದದ್ದೂ ಪೂರ್ತಿ ಖರ್ಚಾಗಲಿಲ್ಲ.', 'The rights came. The money did not fully come, and what came was not fully spent.'), ''),

     (5.5, S + bi('ಅಪ್ಪಾ, ಬೆಂಗಳೂರಿನ ಮಕ್ಕಳಿಗೂ ನಮಗೂ ಬೇರೆ ಬೇರೆ ಕರ್ನಾಟಕನಾ?', 'Dad, do Bengaluru kids and we live in two different Karnatakas?', L, 'b', 'background:#8fd3ff')
      + stage2([(mallanna('firm'), 10, -40, 0.9), (kaveri('sad'), 520, 80, 1.0)]), ''),

     (6.5, S + '<h1 style="font-size:%dpx">%s<br><span style="color:#f2b705">%s</span></h1>' % ((92, 'ಕೆಲಸ ತೋರಿಸಿ.', 'ಆಮೇಲೆ ಮತ.') if L == 'kn' else (88, 'Show me the work.', 'Then my vote.'))
      + stage('firm', 'namaste', 'point', show_neta=False)
      + '<div class="mid" style="font-size:40px;margin:14px 0 0">%s</div>' % t('ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ #9: ನಮ್ಮ ಜಿಲ್ಲೆಗೆ ಹಂಚಿದ ಹಣದಲ್ಲಿ ಎಷ್ಟು ಖರ್ಚಾಯಿತು? ಪಟ್ಟಿ ಕೊಡಿ.',
                                                                              "Kaveri's question: how much of our district's allocation was actually spent? Publish the list.")
      + '<div class="url" style="margin-top:12px">jarvisss007.github.io/know-your-mla</div>', END),
    ]

L = os.environ.get('LANG_OUT', 'kn')
SCENES = scenes(L)
OUT = 'mallanna9-%s.mp4' % L
FPS = 10
