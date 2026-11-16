# Builds the pilot's voice + score mix and the timing file the 3D page animates to.
# Usage: python audio.py OUTDIR
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import talk
from talk import SR, tts, load_rec, add, score, write_wav
FPS = 25
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
VID = os.path.dirname(talk.HERE + '/')

SHOTS = [
 dict(name='open', lead=2.6, tail=0.7, hit=2.2, kicker='ಬೆಂಗಳೂರು · 2024',
      src='Source: NCRB 2024 data, reported by ThePrint, 13 Aug 2026',
      lines=[('m', 'ರಸ್ತೆ ಗುಂಡಿಗೆ ಜೀವ ಹೋಯ್ತು. ಉತ್ತರ ಕೊಡೋರು ಯಾರು?', 'A pothole took a life. Who answers for it?')]),
 dict(name='bars', lead=0.5, tail=0.5, hit=0.3, kicker='ನಗರ ಸಂಸ್ಥೆಗಳ ನಿರ್ಲಕ್ಷ್ಯದಿಂದ ಸಾವು · 2024',
      src='Source: NCRB 2024 data, reported by ThePrint, 13 Aug 2026',
      lines=[('k', 'ಮುಂಬೈ, ಚೆನ್ನೈ, ಹೈದರಾಬಾದ್‌ನಲ್ಲಿ ಒಂದೂ ಇಲ್ಲ. ನಮ್ಮಲ್ಲಿ ಹದಿನೇಳು.', 'Mumbai, Chennai, Hyderabad: zero. Ours: seventeen.')]),
 dict(name='court', lead=0.4, tail=0.4, kicker='ಹೈಕೋರ್ಟ್ · 2019',
      src='Source: Karnataka High Court interim order, 31 Jul 2019 (The News Minute)',
      lines=[('k', 'ಹೈಕೋರ್ಟ್ ಹೇಳಿತು: ಗುಂಡಿಗೆ ಬಲಿಯಾದವರಿಗೆ ಪರಿಹಾರ ಕೊಡಬೇಕು.', 'The High Court said: pothole victims must be compensated.')]),
 dict(name='houses', lead=2.3, tail=0.8, hit=2.0, kicker='ಪರಿಹಾರ ಸಿಕ್ಕಿತಾ? · 2017-22',
      src='Source: The News Minute investigation, Nov 2022 (13 pothole deaths, 2017-22)',
      lines=[('m', 'ಹದಿಮೂರು ಕುಟುಂಬ. ಒಬ್ಬರಿಗೂ ಪರಿಹಾರ ಇಲ್ಲ!', 'Thirteen families. Not one was compensated!')]),
 dict(name='chorus', lead=0.4, tail=1.4, hit=0.3, kicker='ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ',
      src='Fictional characters; every figure is from a public record. 2019 order: BJP govt · 2024 data: Congress govt.',
      chorus=('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ! ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!')),
]
t = 0.0; voice = []; hits = []; shots = []; chorus_start = None
for i, sh in enumerate(SHOTS):
    t0 = t
    if 'hit' in sh: hits.append(t0 + sh['hit'])
    t += sh['lead']; lines = []
    if sh.get('chorus'):
        chorus_start = t0
        a = load_rec(os.path.join(talk.HERE, 'voice/ep11/chorus.wav'))
        crowd = np.zeros(len(a) + 2000)
        for k_, (p, d) in enumerate(((1.0, 0), (0.95, 700), (1.05, 1400))):
            idx = np.clip((np.arange(len(a)) * p).astype(int), 0, len(a) - 1)
            crowd[d:d + len(a)] += a[idx] * (1.0 if k_ == 0 else 0.3)
        voice.append((t, crowd * 0.9))
        lines.append(dict(who='c', t0=t, t1=t + len(a) / SR, kn=sh['chorus'][0], en=sh['chorus'][1])); t += len(a) / SR
    for li, (who, kn, en) in enumerate(sh.get('lines', [])):
        a = tts(kn, 'kn', who, os.path.join(out, 's%d_%d.wav' % (i, li)))
        voice.append((t, a)); lines.append(dict(who=who, t0=t, t1=t + len(a) / SR, kn=kn, en=en)); t += len(a) / SR + 0.25
    t += sh['tail']
    shots.append(dict(name=sh['name'], t0=t0, t1=t, kicker=sh['kicker'], src=sh['src'], lines=lines, hit=(t0 + sh['hit']) if 'hit' in sh else None))
total = t + 0.2
vbuf = np.zeros(int(total * SR) + SR)
for at, a in voice: add(vbuf, a, at)
music = score(total + 1, 96, hits, chorus_start)
# rain bed: filtered noise, quiet
rs = np.random.RandomState(7).randn(len(vbuf)); rain = np.convolve(rs, np.ones(6) / 6, 'same') - np.convolve(rs, np.ones(60) / 60, 'same')
music = np.pad(music, (0, max(0, len(vbuf) - len(music))))[:len(vbuf)]
venv = np.convolve(np.abs(vbuf), np.ones(4410) / 4410, 'same')
duck = 1 - 0.55 * np.clip(venv / 0.05, 0, 1)
mix = vbuf + music * duck * 0.9 + rain * 0.035
mix = mix / max(1e-6, np.max(np.abs(mix))) * 0.95
write_wav(os.path.join(out, 'mix.wav'), mix[:int(total * SR)])
rms = np.sqrt(np.convolve(vbuf ** 2, np.ones(1764) / 1764, 'same'))
n = int(total * FPS)
json.dump(dict(fps=FPS, total=total, frames=n, shots=shots, hits=hits, bpm=96,
               rms=[round(float(rms[min(len(rms) - 1, int(i / FPS * SR))]), 3) for i in range(n)]),
          open(os.path.join(out, 'timeline.json'), 'w'), ensure_ascii=False)
print('total %.1fs' % total, [(s['name'], round(s['t0'], 1), round(s['t1'], 1)) for s in shots])
