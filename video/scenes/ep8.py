import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chars import stage, stage2, mallanna, kaveri, STYLE, bi

LOK = "Sources: Chief Minister's reply in the Assembly (Sept 2022 to Feb 2026); Assembly records on the ACB, 2016-2022"
CONV = 'Sources: CBI special court, 6 May 2025, and Telangana High Court, 11 June 2025 (Reddy); special court, 26 October 2024, and Karnataka High Court, 13 November 2024 (Sail)'
BSY = 'Sources: Lokayukta report, July 2011; resignation, 31 July 2011; CBI court, 2016; Supreme Court, December 2018'
ASSET = 'Source: Karnataka Lokayukta, November 2025 (asset-statement defaulters among legislators)'
DO = 'Sources: Karnataka Lokayukta Act, 1984; Karnataka RTI Rules (Rs 10 application fee)'
END = 'Fictional characters. Convictions named here are suspended pending appeal; cases closed in favour of the accused are shown as such.'

def scenes(L):
    S = STYLE
    t = lambda kn, en: kn if L == 'kn' else en
    sub = lambda kn, en: '<div class="en">%s</div>' % (en if L == 'kn' else kn)
    return [
     (5.0, S + '<div class="k">%s</div>' % t('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 8 · ಯಾರೂ ಜೈಲಿಗೆ ಯಾಕೆ ಹೋಗಲ್ಲ?', 'Mallanna Asks · Episode 8 · Why does nobody go to jail?')
      + bi('ಅಪ್ಪಾ, ಇಷ್ಟು ಆರೋಪ ಇದ್ರೂ ಯಾರೂ ಜೈಲಿಗೆ ಯಾಕೆ ಹೋಗಲ್ಲ?', 'Dad, with so many charges, why does nobody go to jail?', L, 'b', 'background:#8fd3ff')
      + stage2([(mallanna('skeptic'), 10, -40, 0.9), (kaveri('ask'), 520, 80, 1.0)]), ''),

     (6.0, S + '<div class="k">%s</div>' % t('ಲೋಕಾಯುಕ್ತ · ಸೆಪ್ಟೆಂಬರ್ 2022 ರಿಂದ ಫೆಬ್ರವರಿ 2026', 'Lokayukta · Sept 2022 to Feb 2026')
      + '<div class="row"><small>%s</small>195</div>' % t('ದಾಳಿ, ಟ್ರ್ಯಾಪ್ ಪ್ರಕರಣಗಳು', 'Raid and trap cases')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">0</b></div>' % t('ತೀರ್ಪುಗಳು', 'Verdicts')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">19</b></div>' % t('ಹಳೆಯ ಎಸಿಬಿ: 2,000ಕ್ಕೂ ಹೆಚ್ಚು ಪ್ರಕರಣಗಳಲ್ಲಿ ಶಿಕ್ಷೆ', 'Old ACB: convictions from 2,000+ cases'), LOK),

     (6.5, S + '<div class="k">%s</div>' % t('ಶಿಕ್ಷೆ ಆದರೂ...', 'Even after a conviction')
      + '<div class="row"><small>%s</small>%s</div>' % (t('ಜನಾರ್ದನ ರೆಡ್ಡಿ (ಬಿಜೆಪಿ) · ಶಿಕ್ಷೆ ಮೇ 2025', 'Janardhan Reddy (BJP) · convicted May 2025'), t('5 ವಾರದಲ್ಲಿ ತಡೆ', 'Paused in 5 weeks'))
      + '<div class="row"><small>%s</small>%s</div>' % (t('ಸತೀಶ್ ಸೈಲ್ (ಕಾಂಗ್ರೆಸ್) · ಶಿಕ್ಷೆ ಅಕ್ಟೋಬರ್ 2024', 'Satish Sail (Congress) · sentenced Oct 2024'), t('3 ವಾರದಲ್ಲಿ ತಡೆ', 'Paused in 3 weeks'))
      + sub('ರೆಡ್ಡಿ ಪ್ರಕರಣ ತೀರ್ಪಿಗೆ ಸುಮಾರು 15 ವರ್ಷ ಹಿಡಿಯಿತು. ಇಬ್ಬರೂ ಇನ್ನೂ ಶಾಸಕರು; ಮೇಲ್ಮನವಿ ಬಾಕಿ ಇದೆ.',
            "Reddy's case took about 15 years to reach a verdict. Both are still MLAs; their appeals are pending."), CONV),

     (6.0, S + '<div class="k">%s</div>' % t('ಆದರೆ ಬಯಲು ಮಾಡುವುದು ಕೆಲಸ ಮಾಡುತ್ತದೆ', 'But exposure works')
      + '<h2>%s</h2>' % t('2011: ಲೋಕಾಯುಕ್ತ ವರದಿ ಬಂದ ಕೆಲವೇ ದಿನಗಳಲ್ಲಿ ಮುಖ್ಯಮಂತ್ರಿ ರಾಜೀನಾಮೆ.', "2011: within days of the Lokayukta's mining report, a sitting Chief Minister resigned.")
      + sub('ಯಡಿಯೂರಪ್ಪ ನಂತರ ಆ ಪ್ರಕರಣಗಳಲ್ಲಿ ಖುಲಾಸೆಯಾದರು ಅಥವಾ ಪ್ರಕರಣ ರದ್ದಾಯಿತು. ಆದರೆ ಕುರ್ಚಿ ಹೋಯಿತು.',
            'B.S. Yediyurappa was later acquitted or had those cases quashed. But he lost the chair.'), BSY),

     (5.5, S + '<div class="k">%s</div>' % t('ಪ್ರತಿ ವರ್ಷ ಆಸ್ತಿ ಘೋಷಣೆ ಕಡ್ಡಾಯ', 'Annual asset statements are compulsory')
      + '<div class="big r">30%%</div><h2 style="margin-top:20px">%s</h2>' % t('ಶಾಸಕರು ಸಲ್ಲಿಸಲಿಲ್ಲ (ನವೆಂಬರ್ 2025)', 'of MLAs did not file (November 2025)')
      + sub('ಶಿಕ್ಷೆ? ಪತ್ರಿಕೆಯಲ್ಲಿ ಹೆಸರು ಪ್ರಕಟ. ಅಷ್ಟೇ.', 'The penalty? Their names are published in the newspaper. That is all.'), ASSET),

     (6.5, S + bi('ಕೋರ್ಟ್ ತಡ ಮಾಡಬಹುದು. ಮತ ತಡ ಮಾಡಲ್ಲ.', 'The court can be slow. The vote is not.', L)
      + '<div class="row" style="margin-top:20px"><small>%s</small>₹10</div>' % t('ಆರ್‌ಟಿಐ ಅರ್ಜಿ', 'An RTI application')
      + '<div class="row"><small>%s</small>%s</div>' % (t('ಲೋಕಾಯುಕ್ತಕ್ಕೆ ದೂರು', 'A Lokayukta complaint'), t('ಯಾರಾದರೂ', 'Anyone can file'))
      + '<div class="row"><small>%s</small>%s</div>' % (t('ನಿಮ್ಮ ಶಾಸಕರ ಪ್ರಮಾಣಪತ್ರ', "Your MLA's affidavit"), t('ಉಚಿತ', 'Free to read')), DO),

     (6.5, S + '<h1 style="font-size:%dpx">%s<br><span style="color:#f2b705">%s</span></h1>' % ((92, 'ಕೆಲಸ ತೋರಿಸಿ.', 'ಆಮೇಲೆ ಮತ.') if L == 'kn' else (88, 'Show me the work.', 'Then my vote.'))
      + stage2([(mallanna('firm'), 10, -40, 0.9), (kaveri('smile'), 520, 80, 1.0)], label=False)
      + '<div class="mid" style="font-size:40px;margin:14px 0 0">%s</div>' % t('ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ #8: ನಮ್ಮ ಶಾಸಕರು ಈ ವರ್ಷ ಆಸ್ತಿ ಘೋಷಣೆ ಸಲ್ಲಿಸಿದ್ದಾರಾ?',
                                                                              "Kaveri's question: did our MLA file this year's asset statement?")
      + '<div class="url" style="margin-top:12px">jarvisss007.github.io/know-your-mla</div>', END),
    ]

L = os.environ.get('LANG_OUT', 'kn')
SCENES = scenes(L)
OUT = 'mallanna8-%s.mp4' % L
FPS = 10
