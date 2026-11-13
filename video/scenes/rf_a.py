# The Ruling Family · Episode A · "Their own numbers"   (record-only, no characters)
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chars import STYLE

DKS = "Source: D.K. Shivakumar's sworn election affidavits, 2008, 2013, 2018, 2023 (ADR / myneta.info). Total declared assets of the candidate and family."
DKSU = "Source: D.K. Suresh's sworn Lok Sabha affidavits, 2013 by-election, 2014, 2019, 2024 (ADR / myneta.info)."
ADR = 'Source: Association for Democratic Reforms, analysis of 31 sitting Chief Ministers, July 2026'
CASE = 'Sources: CBI FIR, 3 October 2020; Karnataka cabinet decision, 23 November 2023; Supreme Court, 15 July 2024; Karnataka High Court, 29 August 2024 (reported by ThePrint and The Tribune)'
END = 'Declared wealth includes land and business holdings revalued over time. It is not proof of wrongdoing, and neither brother has been convicted in any case. We sent these questions to the Chief Minister\'s office before publishing.'

def bars(rows, mx, color):
    out = ''
    for label, v in rows:
        w = max(4, int(700 * v / mx))
        out += ('<div style="display:flex;align-items:center;gap:18px;margin:16px 0">'
                '<div style="width:110px;font:700 40px Segoe UI;color:#9aa3b2">%s</div>'
                '<div style="height:64px;width:%dpx;background:%s;border-radius:8px"></div>'
                '<div style="font:800 46px Segoe UI;white-space:nowrap">₹%s</div></div>') % (label, w, color, f'{v:,.1f}'.replace('.0', ''))
    return out

def scenes(L):
    S = STYLE
    t = lambda kn, en: kn if L == 'kn' else en
    cr = t('ಕೋಟಿ', 'crore')
    sub = lambda kn, en: '<div class="en">%s</div>' % (en if L == 'kn' else kn)
    return [
     (4.5, S + '<div class="k">%s</div>' % t('ಆಳುವ ಕುಟುಂಬ · ಭಾಗ 1', 'The Ruling Family · Part 1')
      + '<h1>%s</h1>' % t('ಭಾರತದ ಅತ್ಯಂತ ಶ್ರೀಮಂತ ಮುಖ್ಯಮಂತ್ರಿ.', "India's richest Chief Minister.")
      + '<div class="big" style="margin-top:30px">₹1,413 %s</div>' % cr
      + sub('ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್, ಕರ್ನಾಟಕ, ಘೋಷಿತ ಆಸ್ತಿ. ಆಂಧ್ರದ ಚಂದ್ರಬಾಬು ನಾಯ್ಡು ₹931 ಕೋಟಿಯೊಂದಿಗೆ ಎರಡನೇ ಸ್ಥಾನ.',
            "D.K. Shivakumar, Karnataka: declared assets. Second: Andhra Pradesh's N. Chandrababu Naidu at Rs 931 crore."), ADR),

     (6.5, S + '<div class="k">%s</div>' % t('ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ · ಅವರದೇ ಪ್ರಮಾಣಪತ್ರಗಳು', "D.K. Shivakumar · his own sworn affidavits")
      + bars([('2008', 75.6), ('2013', 251.5), ('2018', 840.0), ('2023', 1413.8)], 1413.8, '#f2b705')
      + sub('15 ವರ್ಷದಲ್ಲಿ 18 ಪಟ್ಟು. 2013 ರಿಂದ 2023ರ ನಡುವೆ 5.6 ಪಟ್ಟು; ಇದರಲ್ಲಿ ಐದು ವರ್ಷ (2014-2019) ಅವರು ಸಚಿವರಾಗಿದ್ದರು.',
            '18 times in 15 years. 5.6 times between 2013 and 2023, years that include five as a minister (2014 to 2019).'), DKS),

     (6.0, S + '<div class="k">%s</div>' % t('ಸಹೋದರ ಡಿ.ಕೆ. ಸುರೇಶ್ · ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ ಸಂಸದ 2013-2024', 'His brother D.K. Suresh · Bangalore Rural MP, 2013-2024')
      + bars([('2013', 47.3), ('2014', 85.9), ('2019', 338.9), ('2024', 593.1)], 1413.8, '#ef5261')
      + sub('11 ವರ್ಷದಲ್ಲಿ 12.5 ಪಟ್ಟು. 2024ರಲ್ಲಿ ಅವರು ಸೋತರು.', '12.5 times in 11 years. He lost the seat in 2024.'), DKSU),

     (6.0, S + '<div class="k">%s</div>' % t('ಈ ನಡುವೆ, ನೀವು ಕಟ್ಟುವುದು', 'Meanwhile, what you pay')
      + '<div class="row"><small>%s</small>₹39 → <b style="color:#ef5261">₹54</b></div>' % t('ಹಾಲು, ಲೀಟರ್‌ಗೆ (2022 → 2026)', 'Milk, per litre (2022 to 2026)')
      + '<div class="row"><small>%s</small>₹6 → <b style="color:#ef5261">₹10</b></div>' % t('ಬಿಎಂಟಿಸಿ ಕನಿಷ್ಠ ಟಿಕೆಟ್', 'BMTC minimum bus fare')
      + '<div class="row"><small>%s</small><b style="color:#ef5261">32,870</b></div>' % t('ಖಾಲಿ ಆರೋಗ್ಯ ಹುದ್ದೆಗಳು', 'Health posts vacant'),
      'Sources: KMF price orders; BMTC fare order, November 2026; Health Department, December 2024'),

     (7.0, S + '<div class="k">%s</div>' % t('ದಾಖಲೆಯಲ್ಲಿರುವ ಪ್ರಕರಣ', 'The case on record')
      + '<h2>%s</h2>' % t('ಸಿಬಿಐ ಆರೋಪ: 2013-18ರಲ್ಲಿ ಆದಾಯಕ್ಕಿಂತ ₹74.93 ಕೋಟಿ ಹೆಚ್ಚು ಆಸ್ತಿ.', 'CBI allegation: Rs 74.93 crore of assets beyond known income, 2013 to 2018.')
      + sub('2020ರಲ್ಲಿ ಎಫ್‌ಐಆರ್. 2023ರಲ್ಲಿ ಅವರೇ ಉಪಮುಖ್ಯಮಂತ್ರಿಯಾಗಿದ್ದ ಸರ್ಕಾರ ಸಿಬಿಐ ಅನುಮತಿ ಹಿಂಪಡೆದು ಪ್ರಕರಣವನ್ನು ಲೋಕಾಯುಕ್ತಕ್ಕೆ ಕಳಿಸಿತು. ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ಎಫ್‌ಐಆರ್ ರದ್ದುಪಡಿಸಲು ನಿರಾಕರಿಸಿತು. ಯಾವುದೇ ತೀರ್ಪು ಇಲ್ಲ.',
            'FIR in 2020. In 2023 the government in which he was Deputy Chief Minister withdrew consent for the CBI and sent the case to the Lokayukta. The Supreme Court refused to quash the FIR. No verdict yet.'), CASE),

     (6.5, S + '<h2>%s</h2>' % t('ನಮ್ಮ ಪ್ರಶ್ನೆ:', 'Our question:')
      + '<h1 style="color:#f2b705;margin-top:20px">%s</h1>' % t('ನೀವು ಸಚಿವರಾಗಿದ್ದ ವರ್ಷಗಳಲ್ಲಿ ಯಾವ ವ್ಯವಹಾರ ಇಷ್ಟು ವೇಗವಾಗಿ ಬೆಳೆಯಿತು?', 'Which business grew this fast in the years you were a minister?')
      + '<div class="url">jarvisss007.github.io/know-your-mla</div>', END),
    ]

L = os.environ.get('LANG_OUT', 'kn')
SCENES = scenes(L)
OUT = 'ruling-family-a-%s.mp4' % L
FPS = 10
