# Build English-first versions of the Kannada-only episodes (1, 4, 5) from their scene files.
import importlib.util, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1]  # e.g. scenes_mallanna1.py
spec = importlib.util.spec_from_file_location('m', os.path.join(HERE, src)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
KN = re.compile('[ಀ-೿]')
D = {
 'ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 1': 'Mallanna Asks · Episode 1',
 'ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 4 · ಅಮ್ಮನ ಆಸ್ಪತ್ರೆ': "Mallanna Asks · Episode 4 · Amma's hospital",
 'ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 5 · ಬಾರದ ನೀರು': 'Mallanna Asks · Episode 5 · The water that never came',
 'ರಾಜ್ಯದ ಖಾತೆ': "The state's accounts",
 '2022-23 · ಆದಾಯ ಖಾತೆ ಹೆಚ್ಚುವರಿ': '2022-23 · revenue surplus', '2025-26 · ಆದಾಯ ಕೊರತೆ': '2025-26 · revenue deficit',
 'ಗುತ್ತಿಗೆದಾರರಿಗೆ ಬಾಕಿ': 'Owed to contractors', 'ಅದೇ ಸಮಯದಲ್ಲಿ': 'Meanwhile',
 'ಶಾಸಕರ ಮೂಲ ವೇತನ': "MLAs' basic pay", 'ಮರು ಆಯ್ಕೆಯಾದ 81 ಶಾಸಕರ ಸರಾಸರಿ ಆಸ್ತಿ': 'Average assets of 81 re-elected MLAs',
 'ಬಜೆಟ್‌ನಲ್ಲಿ ಆರೋಗ್ಯದ ಪಾಲು · 2026-27': "Health's share of the budget · 2026-27", 'ಕರ್ನಾಟಕ': 'Karnataka', 'ಎಲ್ಲ ರಾಜ್ಯಗಳ ಸರಾಸರಿ': 'Average of all states',
 'ಮಕ್ಕಳ ರಕ್ತಹೀನತೆ (6-59 ತಿಂಗಳು) · 2015-16 → 2019-21': 'Children with anaemia (6-59 months) · 2015-16 → 2019-21',
 'ಯಾದಗಿರಿ': 'Yadgir', 'ಕಲಬುರಗಿ': 'Kalaburagi', 'ತುಮಕೂರು': 'Tumakuru', 'ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ': 'To be fair',
 'ಎತ್ತಿನಹೊಳೆ ಕುಡಿಯುವ ನೀರಿನ ಯೋಜನೆ': 'Yettinahole drinking water project', '2012 · ಅನುಮೋದಿತ ವೆಚ್ಚ': '2012 · approved cost',
 '2023 · ಪರಿಷ್ಕೃತ ವೆಚ್ಚ': '2023 · revised cost', 'ಮಾರ್ಚ್ 2024ರ ವರೆಗೆ ಖರ್ಚು': 'Spent by March 2024',
 'ಮೈಸೂರು · 24x7 ನೀರು ಯೋಜನೆ': 'Mysuru · 24x7 water scheme', 'ಭದ್ರಾ ಮೇಲ್ದಂಡೆ · ಚಿತ್ರದುರ್ಗ, ದಾವಣಗೆರೆ': 'Upper Bhadra · Chitradurga, Davanagere',
 '2003 · ಮೊದಲ ಹಂತ': '2003 · stage I', '2020 · ಪರಿಷ್ಕೃತ': '2020 · revised', 'ಬಿಜೆಪಿ · ಕಾಂಗ್ರೆಸ್ · ಸಮ್ಮಿಶ್ರ': 'BJP · Congress · Coalition',
 'ಕೋಟಿ': 'crore', '1 ವರ್ಷ ಜೈಲು': 'Up to 1 year in jail', 'ಕೆಲಸ ತೋರಿಸಿ.': 'Show me the work.', 'ಆಮೇಲೆ ಮತ.': 'Then my vote.',
}
PRE = {'ಖರ್ಚು. 24x7 ನೀರು ಬರಲಿಲ್ಲ.': 'spent. No 24x7 water.'}
def conv(h):
    for k, v in PRE.items(): h = h.replace(k, v)
    h = re.sub(r'(<div class="b[^"]*"[^>]*>)(.*?)<small>(.*?)</small></div>', lambda x: x.group(1) + x.group(3) + '<small>' + x.group(2) + '</small></div>', h, flags=re.S)
    h = re.sub(r'<span>(.*?)</span><i>(.*?)</i>', lambda x: '<span>' + x.group(2) + '</span><i>' + x.group(1) + '</i>', h, flags=re.S)
    # a Kannada heading followed by an English .en line: put the English in the heading, Kannada becomes the small line
    mh = re.search(r'<(h1|h2)([^>]*)>(.*?)</\1>', h, re.S); me = re.search(r'<div class="en"([^>]*)>(.*?)</div>', h, re.S)
    if mh and me and KN.search(mh.group(3)) and 'ಕೆಲಸ ತೋರಿಸಿ' not in mh.group(3):
        kn_text = re.sub('<[^>]+>', ' ', mh.group(3)).strip()
        h = h.replace(mh.group(0), '<%s%s>%s</%s>' % (mh.group(1), mh.group(2), me.group(2), mh.group(1)), 1)
        h = h.replace(me.group(0), '<div class="en"%s>%s</div>' % (me.group(1), kn_text), 1)
    for k in sorted(D, key=len, reverse=True):
        h = h.replace(k, D[k])
    # the closing Kannada call-to-action line (.mid) duplicates the English .en line: drop it
    h = re.sub(r'<div class="mid"[^>]*>[^<]*[ಀ-೿][^<]*</div>', '', h)
    return h
SCENES = [(s, conv(h), src_) for s, h, src_ in m.SCENES]
OUT = m.OUT.replace('-kn.mp4', '-en.mp4')
FPS = getattr(m, 'FPS', 10)
left = [i for i, (_, h, _) in enumerate(SCENES) if KN.search(re.sub(r'<(small|i|div class="en"|text)[^>]*>.*?</(small|i|div|text)>', '', re.sub('<svg.*?</svg>', '', h, flags=re.S), flags=re.S))]
print('scenes with Kannada still in big text:', left, file=sys.stderr)
