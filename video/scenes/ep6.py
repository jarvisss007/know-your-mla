import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chars import stage, stage2, mallanna, kaveri, STYLE, bi

PRS = 'Source: PRS Legislative Research, Karnataka Budget Analysis 2026-27 (share of guarantees: our calculation from PRS figures)'
GL = 'Sources: PRS Legislative Research; ThePrint on the 2026-27 budget'
RAISE = 'Sources: Business Today, June 2024; Free Press Journal, April 2025; The South First, August 2025'
END = 'Fictional characters. Every figure in this video comes from a public record. If one is wrong, tell us and we will correct it.'

def scenes(L):
    S = STYLE
    t = lambda kn, en: kn if L == 'kn' else en
    sub = lambda kn, en: '<div class="en">%s</div>' % (en if L == 'kn' else kn)
    return [
     (5.0, S + '<div class="k">%s</div>' % t('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 6 · ಗ್ಯಾರಂಟಿ ಲೆಕ್ಕ', 'Mallanna Asks · Episode 6 · The guarantee math')
      + bi('ಐದು ಗ್ಯಾರಂಟಿ ಕೊಟ್ಟಿದೀವಿ. ಇನ್ನೇನು ಬೇಕು?', 'We gave you five guarantees. What more do you want?', L, 'b n')
      + bi('ಲೆಕ್ಕ ಬೇಕು ಸ್ವಾಮಿ.', 'The accounts, sir.', L)
      + stage('skeptic', 'smug'), ''),

     (6.0, S + '<div class="k">%s</div>' % t('ರಾಜ್ಯದ ಆದಾಯದ ₹100ರಲ್ಲಿ, 2026-27', "Of every Rs 100 the state earns, 2026-27")
      + '<div class="row"><small>%s</small><b style="color:#ef5261">₹59</b></div>' % t('ಸಂಬಳ, ಪಿಂಚಣಿ, ಬಡ್ಡಿ', 'Salaries, pensions, interest')
      + '<div class="row"><small>%s</small><b style="color:#f2b705">₹16</b></div>' % t('ಐದು ಗ್ಯಾರಂಟಿಗಳು (₹51,286 ಕೋಟಿ)', 'Five guarantees (Rs 51,286 crore)')
      + '<div class="row"><small>%s</small>₹25</div>' % t('ಉಳಿದ ಎಲ್ಲದಕ್ಕೂ', 'Everything else')
      + sub('ರಸ್ತೆ, ಆಸ್ಪತ್ರೆ, ಶಾಲೆ, ನೀರು, ಎಲ್ಲವೂ ಈ ₹25ರಲ್ಲೇ.', 'Roads, hospitals, schools, water: all of it from the last Rs 25.'), PRS),

     (5.5, S + '<div class="k">%s</div>' % t('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair')
      + '<h2>%s</h2>' % t('ಗೃಹಲಕ್ಷ್ಮಿ ಒಂದೇ ₹28,608 ಕೋಟಿ: ಮನೆಯೊಡತಿಯರಿಗೆ ತಿಂಗಳಿಗೆ ₹2,000.', 'Gruha Lakshmi alone is Rs 28,608 crore: Rs 2,000 a month to women heads of households.')
      + sub('ಅನೇಕ ಕುಟುಂಬಗಳಿಗೆ ಇದು ನಿಜವಾದ ಸಹಾಯ. ಪ್ರಶ್ನೆ ಸಹಾಯದ ಬಗ್ಗೆ ಅಲ್ಲ. ಅದಕ್ಕೆ ದುಡ್ಡು ಎಲ್ಲಿಂದ ಎಂಬುದು.',
            'For many families it is real help. The question is not the help. It is where the money comes from.'), GL),

     (6.0, S + bi('ಅದಕ್ಕೇನಾ ಪೆಟ್ರೋಲ್, ನೋಂದಣಿ ಎಲ್ಲಾ ಏರಿದ್ದು?', 'Is that why petrol and registration went up?', L)
      + '<div class="row" style="margin-top:24px"><small>%s</small>25.92%% → <b style="color:#ef5261">29.84%%</b></div>' % t('ಪೆಟ್ರೋಲ್ ಮೇಲಿನ ರಾಜ್ಯ ತೆರಿಗೆ · 2024', 'State tax on petrol · 2024')
      + '<div class="row"><small>%s</small>14.3%% → <b style="color:#ef5261">21.17%%</b></div>' % t('ಡೀಸೆಲ್ · 2024-25', 'Diesel · 2024-25')
      + '<div class="row"><small>%s</small>1%% → <b style="color:#ef5261">2%%</b></div>' % t('ನೋಂದಣಿ ಶುಲ್ಕ · 2025', 'Property registration fee · 2025')
      + sub('ಇವೆಲ್ಲ ನೇರವಾಗಿ ರಾಜ್ಯದ ಖಜಾನೆಗೆ ಹೋಗುವ ಏರಿಕೆಗಳು.', 'Each of these rises goes straight to the state treasury.'), RAISE),

     (6.0, S + '<div class="k">%s</div>' % t('ಆದರೂ ಸಾಲ', 'And still, borrowing')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">₹22,957 %s</b></div>' % (t('ಆದಾಯ ಕೊರತೆ, 2026-27', 'Revenue deficit, 2026-27'), t('ಕೋಟಿ', 'cr'))
      + '<div class="row"><small>%s</small><b style="color:#ef5261">₹97,448 %s</b></div>' % (t('ವಿತ್ತೀಯ ಕೊರತೆ (ಸಾಲ), 2026-27', 'Fiscal deficit (borrowing), 2026-27'), t('ಕೋಟಿ', 'cr'))
      + sub('ದೈನಂದಿನ ಖರ್ಚಿಗೂ ಸಾಲ. ಆ ಸಾಲದ ಬಡ್ಡಿ ಮುಂದಿನ ವರ್ಷದ ₹59ರಲ್ಲಿ ಸೇರುತ್ತದೆ.',
            "Borrowing even for day-to-day spending. The interest on it joins next year's Rs 59."), PRS),

     (5.5, S + bi('ಅಪ್ಪಾ, ಆ ಸಾಲ ಯಾರು ತೀರಿಸ್ತಾರೆ?', 'Dad, who pays back that loan?', L, 'b', 'background:#8fd3ff')
      + bi('ನೀನು, ಕಾವೇರಿ.', 'You do, Kaveri.', L)
      + stage2([(mallanna('firm'), 10, -40, 0.9), (kaveri('sad'), 520, 80, 1.0)]), ''),

     (6.5, S + '<h1 style="font-size:%dpx">%s<br><span style="color:#f2b705">%s</span></h1>' % ((92, 'ಕೆಲಸ ತೋರಿಸಿ.', 'ಆಮೇಲೆ ಮತ.') if L == 'kn' else (88, 'Show me the work.', 'Then my vote.'))
      + stage('firm', 'namaste', 'point', show_neta=False)
      + '<div class="mid" style="font-size:40px;margin:14px 0 0">%s</div>' % t('ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ #6: ಗ್ಯಾರಂಟಿಗೆ ದುಡ್ಡು ಎಲ್ಲಿಂದ, ಮತ್ತು ಕೆಲಸಕ್ಕೆ ಎಷ್ಟು ಉಳಿಯಿತು?',
                                                                              "Kaveri's question: where does the guarantee money come from, and what is left for the work?")
      + '<div class="url" style="margin-top:12px">jarvisss007.github.io/know-your-mla</div>', END),
    ]

L = os.environ.get('LANG_OUT', 'kn')
SCENES = scenes(L)
OUT = 'mallanna6-%s.mp4' % L
FPS = 10
