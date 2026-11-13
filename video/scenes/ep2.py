import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chars import stage, stage2, mallanna, kaveri, STYLE, bi

MILK = 'Sources: KMF price orders reported by DT Next (Nov 2022), Outlook (Aug 2023), The Week/PTI (Jun 2024, Mar 2025), The South First (Nov 2026)'
BUS = 'Sources: The Week/PTI, 2 January 2025; The South First, November 2026'
FUEL = 'Sources: Business Today, 15 June 2024; Free Press Journal, April 2025; The News Minute, March 2020; Outlook, 4 November 2021'
HOME = 'Sources: India TV, September 2023; The South First, August 2025; The Week/PTI (KERC order), 20 March 2025'
TAX = "Sources: RBI Handbook of Statistics on State Government Finances (2000-01); PRS Karnataka Budget Analysis 2026-27"
BACK = 'Sources: School Education Minister in the Assembly, December 2025 (The Week/PTI); Health Department, December 2024; Finance Department note, September 2026'
END = 'Fictional characters. Every figure in this video comes from a public record. If one is wrong, tell us and we will correct it.'

def scenes(L):
    S = STYLE
    t = lambda kn, en: kn if L == 'kn' else en
    sub = lambda kn, en: '<div class="en">%s</div>' % (en if L == 'kn' else kn)
    return [
     (5.0, S + '<div class="k">%s</div>' % t('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 2 · ಕಟ್ಟುತ್ತಲೇ ಇದ್ದಾನೆ', 'Mallanna Asks · Episode 2 · He keeps paying')
      + bi('ಬೆಲೆ ಏರಿಕೆ? ಎಲ್ಲಿ? ಎಲ್ಲಾ ಫ್ರೀ ಕೊಟ್ಟಿದೀವಲ್ಲ!', 'Price rise? Where? We gave you everything free!', L, 'b n')
      + bi('ಫ್ರೀ ಮುಂದಿನ ಬಾಗಿಲಿಂದ ಬಂತು. ಬಿಲ್ ಹಿಂದಿನ ಬಾಗಿಲಿಂದ.', 'Free came through the front door. The bill came through the back.', L)
      + stage('skeptic', 'smug'), ''),

     (6.0, S + '<div class="k">%s</div>' % t('ನಂದಿನಿ ಹಾಲು · ಟೋನ್ಡ್, ಲೀಟರ್‌ಗೆ', 'Nandini toned milk, per litre')
      + '<div class="row"><small>%s</small>₹39</div>' % t('ನವೆಂಬರ್ 2022 · ಬಿಜೆಪಿ ಸರ್ಕಾರ', 'Nov 2022 · BJP government')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">₹54</b></div>' % t('ನವೆಂಬರ್ 2026 · ಕಾಂಗ್ರೆಸ್ ಸರ್ಕಾರ', 'Nov 2026 · Congress government')
      + sub('ನಾಲ್ಕು ಏರಿಕೆ: ₹3, ₹2 (50 ಮಿಲಿ ಹೆಚ್ಚು), ₹4, ₹8. ಕೊನೆಯ ₹8ರಲ್ಲಿ ₹7 ರೈತರಿಗೆ ಹೋಗುತ್ತದೆ.',
            'Four rises since: Rs 3, Rs 2 (with 50 ml more), Rs 4 and now Rs 8. To be fair, Rs 7 of the latest Rs 8 goes to dairy farmers.'), MILK),

     (5.5, S + bi('ಅಪ್ಪಾ, ಬಸ್ ಟಿಕೆಟ್ ಮತ್ತೆ ಏರಿತು!', 'Dad, the bus ticket went up again!', L, 'b', 'background:#8fd3ff')
      + stage2([(mallanna('neutral'), 10, -40, 0.9), (kaveri('ask'), 520, 80, 1.0)])
      + '<div class="fact"><b>+15%% · +23 to 35%%</b><span>%s</span><i>%s</i></div>' % (
          t('ಜನವರಿ 2025, ಮತ್ತೆ ನವೆಂಬರ್ 2026', 'January 2025, then again in November 2026'),
          t('Bus fares: +15% in Jan 2025, then +23% (KSRTC) to +35% (BMTC) in Nov 2026. BMTC minimum fare: Rs 6 to Rs 10.',
            'ಬಿಎಂಟಿಸಿ ಕನಿಷ್ಠ ದರ ₹6 ರಿಂದ ₹10.')), BUS),

     (6.0, S + '<div class="k">%s</div>' % t('ಪೆಟ್ರೋಲ್ ಮೇಲಿನ ರಾಜ್ಯ ತೆರಿಗೆ', 'State tax on petrol')
      + '<div class="row"><small>%s</small>25.92%% → <b style="color:#ef5261">29.84%%</b></div>' % t('ಜೂನ್ 2024 · ಕಾಂಗ್ರೆಸ್', 'June 2024 · Congress')
      + '<div class="row"><small>%s</small>32%% → <b style="color:#ef5261">35%%</b></div>' % t('ಏಪ್ರಿಲ್ 2020 · ಬಿಜೆಪಿ', 'April 2020 · BJP')
      + sub('ಎರಡೂ ಪಕ್ಷಗಳು ತೆರಿಗೆ ಏರಿಸಿವೆ. ನವೆಂಬರ್ 2021ರಲ್ಲಿ ಬಿಜೆಪಿ ಲೀಟರ್‌ಗೆ ₹7 ಇಳಿಸಿತ್ತು. 2025ರಲ್ಲಿ ಡೀಸೆಲ್ ತೆರಿಗೆ ಮತ್ತೆ ಏರಿತು.',
            'Both parties raised it. The BJP also cut fuel by Rs 7 a litre in November 2021. Diesel tax went up again in April 2025.'), FUEL),

     (6.0, S + '<div class="k">%s</div>' % t('ಮನೆ, ಜಮೀನು, ಕರೆಂಟ್', 'Your home, your land, your power bill')
      + '<div class="row"><small>%s</small><b>+25 to 30%%</b></div>' % t('ಮಾರ್ಗಸೂಚಿ ಮೌಲ್ಯ · ಅಕ್ಟೋಬರ್ 2023', 'Guidance values · Oct 2023')
      + '<div class="row"><small>%s</small>1%% → <b style="color:#ef5261">2%%</b></div>' % t('ನೋಂದಣಿ ಶುಲ್ಕ · ಆಗಸ್ಟ್ 2025', 'Registration fee · Aug 2025')
      + '<div class="row"><small>%s</small><b>+36 paise</b></div>' % t('ಪ್ರತಿ ಯೂನಿಟ್ ಕರೆಂಟ್ · ಏಪ್ರಿಲ್ 2025 (KERC)', 'Per unit of power · Apr 2025 (KERC order)'), HOME),

     (6.0, S + '<div class="k">%s</div>' % t('ರಾಜ್ಯ ಸಂಗ್ರಹಿಸುವ ಸ್ವಂತ ತೆರಿಗೆ, ವರ್ಷಕ್ಕೆ', "The state's own tax collection, per year")
      + '<div class="row"><small>2000-01</small>₹9,043 %s</div>' % t('ಕೋಟಿ', 'cr')
      + '<div class="row"><small>2026-27</small><b>₹2,20,000 %s</b></div>' % t('ಕೋಟಿ', 'cr')
      + sub('ರೂಪಾಯಿಯಲ್ಲಿ 24 ಪಟ್ಟು (ಹಣದುಬ್ಬರ ಸೇರಿಸಿಲ್ಲ). ನಾವೆಲ್ಲರೂ ಕೊಳ್ಳುವ, ಓಡಿಸುವ, ನೋಂದಾಯಿಸುವ ಎಲ್ಲದರಿಂದ ಸಂಗ್ರಹ.',
            '24 times more in rupees (not adjusted for inflation). Collected from what all of us buy, drive and register.'), TAX),

     (6.0, S + bi('ಕಟ್ಟೋದು ನಾವು. ವಾಪಸ್ ಏನು ಬಂತು?', 'We pay. What came back?', L)
      + '<div class="row" style="margin-top:24px"><small>%s</small><b style="color:#ef5261">−17 %s</b></div>' % (t('ಸರ್ಕಾರಿ ಶಾಲೆ ದಾಖಲಾತಿ, 15 ವರ್ಷದಲ್ಲಿ', 'Government school enrolment, last 15 years'), t('ಲಕ್ಷ', 'lakh'))
      + '<div class="row"><small>%s</small><b style="color:#ef5261">32,870</b></div>' % t('ಖಾಲಿ ಆರೋಗ್ಯ ಹುದ್ದೆಗಳು', 'Health posts vacant')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">₹36,136 %s</b></div>' % (t('ಗುತ್ತಿಗೆದಾರರಿಗೆ ಬಾಕಿ', 'Owed to contractors'), t('ಕೋಟಿ', 'cr')), BACK),

     (6.5, S + '<h1 style="font-size:%dpx">%s<br><span style="color:#f2b705">%s</span></h1>' % ((92, 'ಕೆಲಸ ತೋರಿಸಿ.', 'ಆಮೇಲೆ ಮತ.') if L == 'kn' else (88, 'Show me the work.', 'Then my vote.'))
      + stage2([(mallanna('firm'), 10, -40, 0.9), (kaveri('smile'), 520, 80, 1.0)], label=False)
      + '<div class="mid" style="font-size:40px;margin:14px 0 0">%s</div>' % t('ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ #2: ನಾವು ಕಟ್ಟಿದ ತೆರಿಗೆಯಲ್ಲಿ ನಮ್ಮ ಊರಿಗೆ ಎಷ್ಟು ಬಂತು?',
                                                                              "Kaveri's question: how much of our tax came back to our town?")
      + '<div class="url" style="margin-top:12px">jarvisss007.github.io/know-your-mla</div>', END),
    ]

L = os.environ.get('LANG_OUT', 'kn')
SCENES = scenes(L)
OUT = 'mallanna2-%s.mp4' % L
FPS = 10
