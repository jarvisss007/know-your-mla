import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chars import stage, stage2, mallanna, kaveri, raju, STYLE, bi

BILLS = 'Sources: Karnataka Finance Department note, 17 September 2026; contractors association, 30 September 2026 (ThePrint)'
A21 = 'Source: Karnataka State Contractors Association letter to the PMO, 6 July 2021 (ThePrint)'
ND = 'Source: Justice H.N. Nagamohan Das inquiry report, March 2025 (The South First); cabinet decision, 11 April 2025'
A26 = "Sources: The Hans India, 13 February 2026; ThePrint, 30 September 2026"
END = 'Fictional characters. These are allegations; no court or Lokayukta has found that any commission rate was paid under either government.'

def scenes(L):
    S = STYLE
    t = lambda kn, en: kn if L == 'kn' else en
    sub = lambda kn, en: '<div class="en">%s</div>' % (en if L == 'kn' else kn)
    return [
     (5.0, S + '<div class="k">%s</div>' % t('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 7 · ರಾಜುವಿನ ರಸ್ತೆ', "Mallanna Asks · Episode 7 · Raju's road")
      + bi('ರಸ್ತೆ ಮುಗಿಸಿ ಎರಡು ವರ್ಷ ಆಯ್ತು. ಬಿಲ್ ಇನ್ನೂ ಬಂದಿಲ್ಲ.', 'I finished the road two years ago. Still not paid.', L, 'b n')
      + stage2([(mallanna('neutral'), 10, -40, 0.9), (raju('firm'), 450, -40, 0.9)]), ''),

     (5.5, S + '<div class="k">%s</div>' % t('ಗುತ್ತಿಗೆದಾರರಿಗೆ ಬಾಕಿ', 'Owed to contractors')
      + '<div class="big r">₹36,136 %s</div>' % t('ಕೋಟಿ', 'cr')
      + sub('ಹಣಕಾಸು ಇಲಾಖೆ, ಸೆಪ್ಟೆಂಬರ್ 2026. ಗುತ್ತಿಗೆದಾರರ ಸಂಘದ ಪ್ರಕಾರ ₹38,000 ಕೋಟಿ.', 'Finance Department, September 2026. The contractors association says Rs 38,000 crore.'), BILLS),

     (5.0, S + bi('ಕಮಿಷನ್ ಕಥೆ ಕೇಳಿದ್ದೀನಿ. ದಾಖಲೆ ಏನು ಹೇಳುತ್ತೆ?', 'I have heard the commission stories. What does the record say?', L)
      + stage2([(mallanna('skeptic'), 10, -40, 0.9), (raju('neutral'), 450, -40, 0.9)]), ''),

     (6.0, S + '<div class="k">%s</div>' % t('ಜುಲೈ 2021 · ಬಿಜೆಪಿ ಸರ್ಕಾರ', 'July 2021 · BJP government')
      + '<div class="big r">40%</div>'
      + '<h2 style="margin-top:20px">%s</h2>' % t('ಗುತ್ತಿಗೆದಾರರ ಸಂಘ ಪ್ರಧಾನಿ ಕಚೇರಿಗೆ ಬರೆದ ಪತ್ರದಲ್ಲಿ ಮಾಡಿದ ಆರೋಪ', "the contractors association's allegation, in a letter to the Prime Minister's Office"), A21),

     (6.5, S + '<div class="k">%s</div>' % t('ಮಾರ್ಚ್ 2025 · ನ್ಯಾಯಾಂಗ ವಿಚಾರಣೆ', 'March 2025 · judicial inquiry')
      + '<h2>&ldquo;%s&rdquo;</h2>' % 'The allegation of 40 percent commissions is not 100 percent true'
      + sub('ನ್ಯಾ. ನಾಗಮೋಹನ್ ದಾಸ್ ವರದಿ: 40% ಸಾಬೀತಾಗಿಲ್ಲ, ಆದರೆ ಟೆಂಡರ್‌ನಲ್ಲಿ ಲೋಪಗಳು ಕಂಡುಬಂದಿವೆ. ಏಪ್ರಿಲ್ 2025ರಲ್ಲಿ ಎಸ್‌ಐಟಿ ರಚನೆ. ಫಲಿತಾಂಶ ಇನ್ನೂ ಪ್ರಕಟವಾಗಿಲ್ಲ.',
            'Justice Nagamohan Das: 40% not proven, but lapses in tendering found. A special investigation team was ordered in April 2025. No result has been published.'), ND),

     (6.5, S + '<div class="k">%s</div>' % t('2026 · ಕಾಂಗ್ರೆಸ್ ಸರ್ಕಾರ', '2026 · Congress government')
      + '<h2>%s</h2>' % t('ಅದೇ ಸಂಘದ ಆರೋಪ: "ಈಗ ಕಮಿಷನ್ ಹಿಂದಿಗಿಂತ ಹೆಚ್ಚು."', 'The same association alleges: "commission is now higher than before."')
      + sub('ಮುಖ್ಯಮಂತ್ರಿಯ ಉತ್ತರ: ಯಾರಿಗೆ ಕೊಡಬೇಕಾಯಿತು ಎಂದು ಹೆಸರಿಸಿ ಅಫಿಡವಿಟ್ ಕೊಡಿ, ತನಿಖೆ ಮಾಡಿಸುತ್ತೇನೆ.',
            'The Chief Minister replied: file an affidavit naming who has to be paid, and he will have it investigated.'), A26),

     (5.5, S + bi('ಅಪ್ಪಾ, ಎರಡೂ ಪಕ್ಷದ ಮೇಲೂ ಒಂದೇ ಆರೋಪ ಅಂದ್ರೆ?', 'Dad, the same charge against both parties. What does that mean?', L, 'b', 'background:#8fd3ff')
      + bi('ಪಕ್ಷ ಬದಲಾಯ್ತು, ವ್ಯವಸ್ಥೆ ಬದಲಾಗಿಲ್ಲ ಅಂತ ಆರೋಪ.', 'The charge is: the party changed, the system did not.', L)
      + stage2([(mallanna('firm'), 10, -40, 0.9), (kaveri('ask'), 520, 80, 1.0)]), ''),

     (6.5, S + '<h1 style="font-size:%dpx">%s<br><span style="color:#f2b705">%s</span></h1>' % ((92, 'ಕೆಲಸ ತೋರಿಸಿ.', 'ಆಮೇಲೆ ಮತ.') if L == 'kn' else (88, 'Show me the work.', 'Then my vote.'))
      + stage2([(mallanna('firm'), 10, -40, 0.9), (raju('smile'), 450, -40, 0.9)], label=False)
      + '<div class="mid" style="font-size:40px;margin:14px 0 0">%s</div>' % t('ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ #7: ಪ್ರತಿ ಕಾಮಗಾರಿಯ ಬಿಲ್, ಪಾವತಿ ದಿನಾಂಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಯಾಕೆ ಇಲ್ಲ?',
                                                                              "Kaveri's question: why isn't every work's bill and payment date published online?")
      + '<div class="url" style="margin-top:12px">jarvisss007.github.io/know-your-mla</div>', END),
    ]

L = os.environ.get('LANG_OUT', 'kn')
SCENES = scenes(L)
OUT = 'mallanna7-%s.mp4' % L
FPS = 10
