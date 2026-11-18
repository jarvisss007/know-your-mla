"""Render one square (1080x1080) share card per sitting MLA, in Kannada and English, for WhatsApp and X.

Every figure comes from the MLA list already published on the site (const D in index.html), which is taken from the
MLAs' own sworn 2023 election affidavits as transcribed by ADR (myneta.info). No allegation, grade or analysis is shown.

    py tools/make_mla_cards.py            # all MLAs
    py tools/make_mla_cards.py Hebbal     # one constituency (for a check)
writes cards/mla/<slug>-kn.png and <slug>-en.png using headless Chrome. Posting them is the owner's call.
"""
import html, io, json, pathlib, re, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "cards" / "mla"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SITE = "jarvisss007.github.io/know-your-mla/"
SKIP = {"Hiriyur"}  # seat vacant: D. Sudhakar died on 10 May 2026

PARTY_KN = {'Congress': 'ಕಾಂಗ್ರೆಸ್', 'BJP': 'ಬಿಜೆಪಿ', 'JD(S)': 'ಜೆಡಿ(ಎಸ್)', 'Independent': 'ಪಕ್ಷೇತರ', 'KRPP': 'ಕೆಆರ್‌ಪಿಪಿ', 'SKP': 'ಎಸ್‌ಕೆಪಿ'}

T = {
 'en': dict(kicker='{c} · {dist} district', head='{n} ({p}) declared these assets in 2023',
            growth='Since 2018: {sign}{g}% (from {a18})', nogrowth='No 2018 figure to compare',
            debts='Debts declared: {l}', cases='Declared criminal cases: {k} (a case is not a conviction)',
            ask='Ask your MLA: what work have you done here since 2023? Show me.',
            src='Source: the MLA\'s own sworn election affidavit, 2023 (ADR / myneta.info)',
            brand='Gandaberunda · official records, not allegations', q='Full report card:'),
 'kn': dict(kicker='{c} · {dist} ಜಿಲ್ಲೆ', head='{n} ({p}) 2023ರಲ್ಲಿ ಘೋಷಿಸಿದ ಆಸ್ತಿ',
            growth='2018ರಿಂದ: {sign}{g}% ({a18}ರಿಂದ)', nogrowth='ಹೋಲಿಸಲು 2018ರ ಅಂಕಿ ಇಲ್ಲ',
            debts='ಘೋಷಿತ ಸಾಲ: {l}', cases='ಘೋಷಿತ ಕ್ರಿಮಿನಲ್ ಪ್ರಕರಣಗಳು: {k} (ಪ್ರಕರಣ ಎಂದರೆ ಶಿಕ್ಷೆ ಅಲ್ಲ)',
            ask='ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ: 2023ರಿಂದ ಇಲ್ಲಿ ಏನು ಕೆಲಸ ಮಾಡಿದ್ದೀರಿ? ತೋರಿಸಿ.',
            src='ಮೂಲ: ಶಾಸಕರ ಸ್ವಂತ ಚುನಾವಣಾ ಪ್ರಮಾಣಪತ್ರ, 2023 (ADR / myneta.info)',
            brand='ಗಂಡಭೇರುಂಡ · ಅಧಿಕೃತ ದಾಖಲೆಗಳು, ಆರೋಪಗಳಲ್ಲ', q='ಪೂರ್ಣ ವರದಿ ಕಾರ್ಡ್:'),
}

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+Kannada:wght@400;600;800&display=swap">
<style>
html,body{{margin:0;width:1080px;height:1080px;background:#0e1014;color:#f2f2ee;font-family:"Noto Sans Kannada","Segoe UI",sans-serif}}
.c>*{{flex-shrink:0}} .c{{box-sizing:border-box;width:1080px;height:1080px;padding:68px 80px;display:flex;flex-direction:column;gap:20px}}
.bar{{width:90px;height:8px;background:#f5b51b}}
.gov{{color:#f5b51b;font-weight:800;font-size:32px}}
.head{{font-size:42px;font-weight:800;line-height:1.25}}
.big{{font-size:{bigpx}px;font-weight:800;line-height:1;color:#f5b51b}}
ul{{margin:6px 0 0;padding:0;list-style:none;display:flex;flex-direction:column;gap:12px;font-size:32px;line-height:1.35;color:#d8d8d2}}
li{{padding-left:30px;position:relative}} li:before{{content:"";position:absolute;left:0;top:.55em;width:12px;height:12px;background:#f5b51b}}
.ask{{font-size:34px;font-weight:800;line-height:1.3;color:#f2f2ee;border-left:6px solid #e0453a;padding-left:20px}}
.sp{{flex:1}}
.foot{{border-top:2px solid #2a2d33;padding-top:20px;display:flex;flex-direction:column;gap:6px}}
.q{{font-size:26px;color:#d8d8d2}} .l{{font-size:28px;font-weight:800;color:#f2f2ee}} .s{{font-size:21px;color:#8f939b}}
</style></head><body><div class="c">
<div class="bar"></div><div class="gov">{kicker}</div><div class="head">{head}</div><div class="big">{big}</div>
<ul>{lis}</ul><div class="ask">{ask}</div><div class="sp"></div>
<div class="foot"><div class="q">{q}</div><div class="l">{link}</div><div class="s">{src}</div><div class="s">{brand}</div></div>
</div></body></html>"""


def money(v, lang):
    if v is None:
        return '—'
    if v < 1:
        return f"₹{round(v * 100)} {'ಲಕ್ಷ' if lang == 'kn' else 'lakh'}"
    s = f"{v:,.0f}" if v >= 100 else (f"{v:.1f}" if v >= 10 else f"{v:.2f}")
    return f"₹{s} {'ಕೋಟಿ' if lang == 'kn' else 'crore'}"


def slug(c):
    return re.sub(r'[^a-z0-9]+', '-', c.lower()).strip('-')


def main():
    s = io.open(ROOT / 'index.html', encoding='utf-8').read()
    D = json.loads(re.search(r'const D = (\[.*?\]);', s).group(1))
    DIST = json.loads(re.search(r'const DIST = (\{.*?\});', s).group(1))
    only = set(sys.argv[1:])
    OUT.mkdir(parents=True, exist_ok=True)
    made = 0
    with tempfile.TemporaryDirectory() as tmp:
        for d in D:
            if d['c'] in SKIP or (only and d['c'] not in only) or d.get('a') is None:
                continue
            sl = slug(d['c'])
            if not (ROOT / 'mla' / f'{sl}.html').exists():
                print('no page for', d['c']); continue
            for lang in ('kn', 'en'):
                t = T[lang]; e = html.escape
                party = PARTY_KN.get(d['p'], d['p']) if lang == 'kn' else d['p']
                lines = []
                if d.get('a18'):
                    g = round(100 * (d['a23'] - d['a18']) / d['a18'])
                    lines.append(t['growth'].format(sign='+' if g >= 0 else '', g=g, a18=money(d['a18'], lang)))
                else:
                    lines.append(t['nogrowth'])
                lines.append(t['debts'].format(l=money(d.get('l'), lang) if d.get('l') else '0'))
                lines.append(t['cases'].format(k=d.get('k', 0)))
                big = money(d['a'], lang)
                page = PAGE.format(bigpx=150 if len(big) <= 11 else 120,
                                   kicker=e(t['kicker'].format(c=d['c'], dist=DIST.get(d['c'], ''))),
                                   head=e(t['head'].format(n=d['n'], p=party)), big=e(big),
                                   lis=''.join(f'<li>{e(x)}</li>' for x in lines), ask=e(t['ask']), q=e(t['q']),
                                   link=e(SITE + f'mla/{sl}.html'), src=e(t['src']), brand=e(t['brand']))
                f = pathlib.Path(tmp) / f'{sl}-{lang}.html'
                f.write_text(page, encoding='utf-8')
                png = OUT / f'{sl}-{lang}.png'
                subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1080,1080',
                                '--virtual-time-budget=6000', f'--screenshot={png}', f.as_uri()],
                               check=True, capture_output=True, timeout=90)
                made += 1
    print('cards made:', made)


if __name__ == '__main__':
    main()
