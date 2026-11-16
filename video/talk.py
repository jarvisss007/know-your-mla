# Talking-character Shorts renderer (macOS).
# Usage: python talk.py SCENEFILE.py kn|en OUT.mp4 [BUILD_DIR]
# Characters speak with the Mac's built-in voices (Soumya kn_IN; Rishi/Tara en_IN), mouths move with the voice,
# eyes blink, the camera pushes in, number reveals land on a hit, and the episode ends on a chanted chorus over an
# original, generated beat (no third-party music, so no copyright claims).
import importlib.util, io, json, math, os, re, subprocess, sys, wave
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chars import mallanna, kaveri, stage2, STYLE

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
FFMPEG = '/opt/anaconda3/bin/ffmpeg'
W, H, FPS, SR = 1080, 1920, 25, 44100
KN_FONT = '"Kannada Sangam MN","Kannada MN","Noto Sans Kannada","Nirmala UI"'
LAT_FONT = '"Helvetica Neue","Segoe UI",Arial'

VOICES = {  # (say voice, pitch factor, rate wpm)
    'kn': {'m': ('Soumya', 0.80, 165), 'k': ('Soumya', 1.12, 175), 'c': ('Soumya', 0.92, 150)},
    'en': {'m': ('Rishi', 0.90, 175), 'k': ('Tara', 1.08, 180), 'c': ('Rishi', 0.95, 160)},
}

CSS = '''*{box-sizing:border-box;margin:0}
body{width:1080px;height:1920px;background:radial-gradient(ellipse at 50% 30%,#1c2230 0%,#0d1016 70%);color:#eceef2;font-family:KN,LAT,sans-serif;overflow:hidden}
.flag{position:absolute;left:0;right:0;top:0;height:16px;display:flex}.flag i{flex:1}.flag i:first-child{background:#f2b705}.flag i:last-child{background:#c21f30}
.brand{position:absolute;left:80px;top:90px;color:#9aa3b2;font:600 34px LAT,sans-serif}
.k{position:absolute;left:80px;right:80px;top:170px;color:#f2b705;font:700 40px/1.3 KN,LAT,sans-serif}
.card{position:absolute;left:80px;right:80px;top:270px;height:640px;display:flex;flex-direction:column;justify-content:center}
.big{font:900 200px/1 LAT,sans-serif;color:#f2b705}.big.r{color:#ef5261}
.big small{font-size:90px;color:#9aa3b2}
.h{font:800 66px/1.25 KN,LAT,sans-serif;margin-top:20px}
.sub{font:400 40px/1.4 LAT,KN,sans-serif;color:#9aa3b2;margin-top:22px}
.row{margin-top:26px;font:800 74px/1.15 LAT,KN,sans-serif;white-space:nowrap}.row small{display:block;font:600 36px KN,LAT,sans-serif;color:#9aa3b2;margin-bottom:6px}.row b{color:#f2b705}.row b.r{color:#ef5261}
.bub{position:absolute;left:60px;right:60px;top:930px;min-height:250px;background:#f2b705;color:#11141a;border-radius:40px;padding:28px 36px;font:800 58px/1.28 KN,LAT,sans-serif}
.bub.k2{background:#8fd3ff}.bub small{display:block;font:500 32px/1.35 LAT,KN,sans-serif;color:#2b3038;margin-top:10px}
.bub:after{content:"";position:absolute;bottom:-34px;border:20px solid transparent;border-top:24px solid #f2b705}
.bub.lm:after{left:200px}.bub.lk{background:#8fd3ff}.bub.lk:after{right:230px;border-top-color:#8fd3ff}
.stage{position:absolute;left:60px;top:1215px;transform:scale(1.13);transform-origin:top left}
.src{position:absolute;left:80px;right:80px;top:1760px;font:400 26px/1.4 LAT,sans-serif;color:#6f7888}
.url{font:800 46px LAT,sans-serif;color:#f2b705;margin-top:24px}
.chorus{position:absolute;left:60px;right:60px;top:300px;text-align:center;font:900 84px/1.3 KN,LAT,sans-serif;color:#f2b705;text-shadow:0 6px 30px rgba(242,183,5,.35)}
.chorus small{display:block;font:600 40px/1.4 LAT,sans-serif;color:#eceef2;margin-top:24px}
.bub .w{color:rgba(17,20,26,.42);border-radius:10px}
.bub.lit .w{color:#11141a}
.bub.hot .w{color:#fff;background:#11141a;box-shadow:0 0 0 5px #11141a}
'''.replace('KN,', KN_FONT + ',').replace('LAT,', LAT_FONT + ',')


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kw)


# ---------- characters with moving mouths and blinking eyes ----------
def m_svg(expr, mouth_open, blink):
    s = mallanna(expr)
    s = re.sub(r'<path d="M19[68] 2[56]\d[^>]*/>', ('<ellipse cx="220" cy="268" rx="22" ry="17" fill="#3a1a10"/>' if mouth_open
               else '<path d="M200 264 q20 6 40 0" stroke="#3a1a10" stroke-width="7" fill="none" stroke-linecap="round"/>'), s, count=1)
    if blink:
        s = s.replace('rx="10" ry="12"', 'rx="11" ry="2"')
    return s


def k_svg(expr, mouth_open, blink):
    s = kaveri('sad' if expr == 'sad' else 'smile')
    mouth_re = r'<path d="M1(38|40) (192|204)[^>]*/>'
    s = re.sub(mouth_re, ('<ellipse cx="160" cy="198" rx="13" ry="15" fill="#5b1f16"/>' if mouth_open
               else '<path d="M146 198 q14 6 28 0" stroke="#5b1f16" stroke-width="6" fill="none" stroke-linecap="round"/>'), s, count=1)
    if blink:
        s = s.replace('rx="9" ry="11"', 'rx="10" ry="2"')
    return s


def stage_svg(sc, speaker, mouth_open, blink):
    me, ke = sc.get('m_expr', 'neutral'), sc.get('k_expr', 'ask')
    m = m_svg(me, mouth_open and speaker in ('m', 'c'), blink)
    k = k_svg(ke, mouth_open and speaker in ('k', 'c'), blink)
    svg = stage2([(m, 10, -40, 0.9), (k, 520, 80, 1.0)])
    return svg.replace('width="850" height="470"', 'width="850" height="470"')


RECT_JS = ('<script>document.body.setAttribute("data-r",[...document.querySelectorAll(".bub .w")].map(e=>{const r=e.getBoundingClientRect();'
           'return [r.left,r.top,r.right,r.bottom].map(Math.round)}).flat().join(","))</script>')


def page(sc, lang, line, mouth_open, blink, wmode='', empty=False, card=None, probe=False):
    """wmode: '' = words dim (not yet spoken), 'lit' = all spoken, 'hot' = all in the current-word style.
    empty: no card and no bubble (the plate that entrances animate over). card: override the card HTML (count-up frames)."""
    kick = sc['kicker'][0 if lang == 'kn' else 1]
    body = '' if empty else (card if card is not None else sc['card_' + lang])
    bub = ''
    if line and line[0] in ('m', 'k') and not empty:
        big, small = (line[1], line[2]) if lang == 'kn' else (line[2], line[1])
        words = ' '.join('<span class="w">%s</span>' % w for w in big.split(' ') if w)
        bub = '<div class="bub %s %s">%s<small>%s</small></div>' % ('lm' if line[0] == 'm' else 'lk', wmode, words, small)
    chorus = ''
    if sc.get('chorus'):
        c = sc['chorus'][lang]
        chorus = '<div class="chorus">%s<small>%s</small></div>' % (c[0], c[1])
        body = ''
    src = '<div class="src">%s</div>' % sc['src'] if sc.get('src') else ''
    return ('<!doctype html><html><head><meta charset="utf-8"><style>' + CSS + '</style>' + STYLE + '</head><body>'
            '<div class="flag"><i></i><i></i></div><div class="brand">Gandaberunda · ಗಂಡಭೇರುಂಡ</div>'
            '<div class="k">' + kick + '</div><div class="card">' + body + '</div>' + chorus + bub +
            '<div class="stage">' + stage_svg(sc, line[0] if line else '', mouth_open, blink) + '</div>' + src +
            (RECT_JS if probe else '') + '</body></html>')


def word_rects(html, path, prof):
    """Pixel boxes of each word in the bubble, measured by Chrome itself (so Kannada shaping and wrapping are exact)."""
    io.open(path, 'w', encoding='utf-8').write(html)
    for attempt in range(5):
        try:
            dom = run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                       '--window-size=%d,%d' % (W, H), '--user-data-dir=' + prof, '--dump-dom', 'file://' + path]).stdout.decode('utf-8', 'ignore')
            break
        except subprocess.CalledProcessError:
            if attempt == 4: raise
            import time; time.sleep(2 + attempt * 2)
    m = re.search(r'data-r="([\d,\-]*)"', dom)
    v = [int(x) for x in m.group(1).split(',')] if m and m.group(1) else []
    return [tuple(v[i:i + 4]) for i in range(0, len(v), 4)]


# ---------- motion helpers ----------
CARD_BOX, BUB_BOX = (0, 262, W, 918), (0, 918, W, 1212)


def ease_out(u):
    u = min(1.0, max(0.0, u)); return 1 - (1 - u) ** 3


def ease_back(u):
    u = min(1.0, max(0.0, u)); c = 1.70158; return 1 + (c + 1) * (u - 1) ** 3 + c * (u - 1) ** 2


def fx(frame, plate, box, s=1.0, alpha=1.0, dy=0, anchor=(0.1, 0.5)):
    """Re-draw one region of the frame scaled / shifted / faded over the empty plate."""
    x0, y0, x1, y1 = box; w, h = x1 - x0, y1 - y0
    src = frame.crop(box)
    if abs(s - 1) > 1e-3: src = src.resize((max(1, int(w * s)), max(1, int(h * s))), Image.BILINEAR)
    base = plate.crop(box)
    layer = base.copy()
    layer.paste(src, (int(anchor[0] * w * (1 - s)), int(anchor[1] * h * (1 - s)) + int(dy)))
    frame.paste(Image.blend(base, layer, min(1.0, max(0.0, alpha))), (x0, y0))


def fmt_like(orig, val):
    """Format val the way the original number token is written (Indian or western commas, same decimals)."""
    dec = len(orig.split('.')[1]) if '.' in orig else 0
    txt = ('%.*f' % (dec, val)); ip, fp = (txt.split('.') + [''])[:2]
    if ',' in orig:
        if re.match(r'^\d{1,2}(,\d{2})+,\d{3}', orig):
            head, tail = ip[:-3], ip[-3:]
            parts = []
            while len(head) > 2: parts.insert(0, head[-2:]); head = head[:-2]
            if head: parts.insert(0, head)
            ip = ','.join(parts + [tail]) if parts else tail
        else:
            ip = '{:,}'.format(int(ip))
    return ip + ('.' + fp if dec else '')


def countup_cards(card_html, steps=7):
    """If the card's big figure is a single number, return card variants counting up to it (else None)."""
    m = re.search(r'<div class="big[^"]*">(.*?)</div>', card_html, re.S)
    if not m: return None
    toks = re.findall(r'\d[\d,]*(?:\.\d+)?', re.sub(r'<small>.*?</small>', '', m.group(1), flags=re.S))
    if len(toks) != 1: return None
    tok = toks[0]; val = float(tok.replace(',', ''))
    if val < 10: return None
    out = []
    for i in range(steps):
        f = ease_out((i + 1) / (steps + 1))
        inner = m.group(1).replace(tok, fmt_like(tok, val * f), 1)
        out.append(card_html[:m.start(1)] + inner + card_html[m.end(1):])
    return out


def shoot(html, png, prof):
    hp = png[:-4] + '.html'
    io.open(hp, 'w', encoding='utf-8').write(html)
    for attempt in range(5):  # headless Chrome sometimes fails when another render is running; retry
        try:
            run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                 '--window-size=%d,%d' % (W, H), '--user-data-dir=' + prof, '--screenshot=' + png, 'file://' + hp])
            break
        except subprocess.CalledProcessError:
            if attempt == 4: raise
            import time; time.sleep(2 + attempt * 2)
    im = Image.open(png).convert('RGB')
    assert im.size == (W, H), im.size
    return im


# ---------- audio ----------
def tts(text, lang, who, path):
    voice, pitch, rate = VOICES[lang][who]
    aiff = path[:-4] + '.aiff'
    run(['say', '-v', voice, '-r', str(rate), '-o', aiff, text])
    sr0 = int(float(run([FFMPEG.replace('ffmpeg', 'ffprobe'), '-v', 'error', '-select_streams', 'a:0', '-show_entries',
                         'stream=sample_rate', '-of', 'csv=p=0', aiff]).stdout.decode().strip()))
    af = 'asetrate=%d,aresample=%d,atempo=%.4f' % (int(sr0 * pitch), SR, 1 / pitch)
    run([FFMPEG, '-y', '-v', 'error', '-i', aiff, '-af', af, '-ac', '1', '-ar', str(SR), path])
    with wave.open(path) as w:
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    # trim silence at the ends
    nz = np.where(np.abs(a) > 0.01)[0]
    return a[max(0, nz[0] - 400): nz[-1] + 800] if len(nz) else a


def load_rec(path):
    """A recorded voice clip (already trimmed and levelled), as mono float samples at SR."""
    raw = run([FFMPEG, '-v', 'error', '-i', path, '-f', 's16le', '-ac', '1', '-ar', str(SR), '-']).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768


def stretch(a, target_sec, path):
    """Time-stretch a voice clip to target length (for chanting on the beat)."""
    cur = len(a) / SR
    tmp_in, tmp_out = path + '.in.wav', path + '.out.wav'
    write_wav(tmp_in, a)
    f = cur / target_sec
    chain = []
    while f > 2.0: chain.append('atempo=2.0'); f /= 2.0
    while f < 0.5: chain.append('atempo=0.5'); f /= 0.5
    chain.append('atempo=%.4f' % f)
    run([FFMPEG, '-y', '-v', 'error', '-i', tmp_in, '-af', ','.join(chain), tmp_out])
    with wave.open(tmp_out) as w:
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768


def write_wav(path, a, ch=1):
    a = np.clip(a, -1, 1)
    with wave.open(path, 'wb') as w:
        w.setnchannels(ch); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((a * 32767).astype(np.int16).tobytes())


def env(n, a, d, r, total):
    e = np.ones(total)
    a_, d_ = int(a * SR), int(d * SR)
    if a_: e[:a_] = np.linspace(0, 1, a_)
    e[a_:] = np.exp(-np.arange(total - a_) / max(1, r * SR))
    return e


def note(freq, dur, kind='pad', vol=0.2):
    n = int(dur * SR); t = np.arange(n) / SR
    if kind == 'pad':
        s = sum(np.sin(2 * np.pi * freq * h * t + h) / h for h in (1, 2, 3, 4)) * 0.5
        s *= np.minimum(1, t / 0.4) * np.minimum(1, (dur - t) / 0.4)
    elif kind == 'bass':
        s = np.sign(np.sin(2 * np.pi * freq * t)) * 0.4 + np.sin(2 * np.pi * freq * t) * 0.6
        s *= np.exp(-t / 0.35)
    elif kind == 'bell':
        s = (np.sin(2 * np.pi * freq * t) + 0.4 * np.sin(2 * np.pi * freq * 2.76 * t)) * np.exp(-t / 0.5)
    return s * vol


def kick(vol=0.9):
    n = int(0.35 * SR); t = np.arange(n) / SR
    f = 110 * np.exp(-t / 0.05) + 42
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12) * vol


def snare(vol=0.35):
    n = int(0.2 * SR); t = np.arange(n) / SR
    return (np.random.RandomState(1).randn(n) * 0.7 + np.sin(2 * np.pi * 190 * t) * 0.5) * np.exp(-t / 0.06) * vol


def hat(vol=0.08):
    n = int(0.05 * SR); t = np.arange(n) / SR
    x = np.random.RandomState(2).randn(n); x = np.diff(np.concatenate([[0], x]))
    return x * np.exp(-t / 0.015) * vol


def boom(vol=0.9):
    n = int(1.6 * SR); t = np.arange(n) / SR
    low = np.sin(2 * np.pi * (60 * np.exp(-t / 0.4) + 30) * t) * np.exp(-t / 0.6)
    noise = np.random.RandomState(3).randn(n) * np.exp(-t / 0.08) * 0.5
    return (low + noise) * vol


def riser(dur, vol=0.25):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.random.RandomState(4).randn(n)
    k = 30; x = np.convolve(x, np.ones(k) / k, 'same')
    sweep = np.sin(2 * np.pi * np.cumsum(200 + 1400 * (t / dur) ** 2) / SR) * 0.3
    return (x * 3 + sweep) * (t / dur) ** 2 * vol


def add(buf, clip, at):
    i = int(at * SR)
    if i >= len(buf): return
    j = min(len(buf), i + len(clip)); buf[i:j] += clip[:j - i]


def score(total, bpm, hits, chorus_start):
    """Original backing track: Am - F - C - G progression, kick/snare/hat, bass, bell motif; louder in the chorus."""
    beat = 60 / bpm; bar = beat * 4
    out = np.zeros(int(total * SR) + SR)
    roots = [(220.0, [220.0, 261.63, 329.63]), (174.61, [174.61, 220.0, 261.63]),
             (261.63, [261.63, 329.63, 392.0]), (196.0, [196.0, 246.94, 293.66])]
    motif = [659.25, 587.33, 523.25, 440.0, 523.25, 587.33, 659.25, 783.99]
    b = 0; t = 0.0
    while t < total:
        root, chord = roots[b % 4]
        loud = 1.6 if t >= chorus_start else 1.0
        for f in chord: add(out, note(f / 2, bar, 'pad', 0.05 * loud), t)
        for q in range(4):
            bt = t + q * beat
            add(out, note(root / 4, beat * 0.9, 'bass', 0.18 * loud), bt)
            add(out, kick(0.55 * loud), bt) if q in (0, 2) or t >= chorus_start else None
            if q in (1, 3): add(out, snare(0.22 * loud), bt)
            add(out, hat(0.06 * loud), bt + beat / 2)
        if t >= chorus_start or b % 2 == 1:
            for i, f in enumerate(motif[(b % 2) * 4:(b % 2) * 4 + 4]):
                add(out, note(f, beat, 'bell', 0.06 * loud), t + i * beat)
        t += bar; b += 1
    for h in hits:
        add(out, riser(0.9), max(0, h - 0.9)); add(out, boom(0.8), h)
    return out[:int(total * SR)]


# ---------- build ----------
def build(scene_file, lang, out, bdir):
    os.makedirs(bdir, exist_ok=True); prof = os.path.join(bdir, 'prof')
    spec = importlib.util.spec_from_file_location('ep', scene_file); ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
    bpm = getattr(ep, 'BPM', 96); beat = 60 / bpm
    timeline = []   # (t0, t1, scene_idx, line_idx)
    voice = []      # (t, samples)
    hits, t = [], 0.0
    chorus_start = None
    # Recorded human voice lines, if the episode provides them: REC = {'kn': {'scene.line': 'path.wav', 'chorus': 'path.wav'}}
    rec = {k: (v if os.path.isabs(v) else os.path.join(HERE, v)) for k, v in getattr(ep, 'REC', {}).get(lang, {}).items()}
    for si, sc in enumerate(ep.SCENES):
        t0 = t
        if sc.get('hit'): hits.append(t + 0.05)
        t += sc.get('lead', 0.35)
        if sc.get('chorus'):
            chorus_start = t0
            bar = beat * 4
            rc = rec.get('chorus')
            if rc:  # a real recorded chorus: keep the human voice in front, add a light crowd behind it
                a = load_rec(rc)
                crowd = np.zeros(len(a) + 2000)
                for k_, (p, d) in enumerate(((1.0, 0), (0.95, 700), (1.05, 1400))):
                    idx = np.clip((np.arange(len(a)) * p).astype(int), 0, len(a) - 1)
                    crowd[d:d + len(a)] += a[idx] * (1.0 if k_ == 0 else 0.3)
                voice.append((t, crowd * 0.9))
                timeline.append((t, t + len(a) / SR, si, ('c', ' '.join(sc['chant'][lang]), '')))
                t += len(a) / SR + sc.get('tail', 1.0)
                continue
            for li, line in enumerate(sc['chant'][lang]):
                for rep in range(sc.get('reps', 2)):
                    a = tts(line, lang, 'c', os.path.join(bdir, 'ch%d_%d_%s.wav' % (li, rep, lang)))
                    a = stretch(a, bar * 2 * 0.92, os.path.join(bdir, 'chs%d_%d_%s' % (li, rep, lang)))
                    # crowd: three pitched copies, slightly offset
                    crowd = np.zeros(len(a) + 2000)
                    for k_, (p, d) in enumerate(((1.0, 0), (0.94, 600), (1.06, 1200))):
                        idx = np.clip((np.arange(len(a)) * p).astype(int), 0, len(a) - 1)
                        crowd[d:d + len(a)] += a[idx] * (0.7 if k_ == 0 else 0.45)
                    voice.append((t, crowd * 0.9))
                    timeline.append((t, t + bar * 2, si, ('c', line, line)))
                    t += bar * 2
            t += sc.get('tail', 1.0)
            continue
        for li, line in enumerate(sc['lines']):
            who, kn, en = line[0], line[1], line[2]
            rp = rec.get('%d.%d' % (si, li))
            a = load_rec(rp) if rp else tts(kn if lang == 'kn' else en, lang, who, os.path.join(bdir, 's%d_l%d_%s.wav' % (si, li, lang)))
            voice.append((t, a))
            timeline.append((t, t + len(a) / SR, si, line))
            t += len(a) / SR + 0.25
        t += sc.get('tail', 0.45)
        timeline.append((t0, t, si, None))  # scene span marker
    total = t + 0.3
    print('duration %.1fs' % total)

    # audio mix with ducking
    vbuf = np.zeros(int(total * SR) + SR)
    for at, a in voice: add(vbuf, a, at)
    music = score(total + 1, bpm, hits, chorus_start if chorus_start is not None else total + 99)
    music = np.pad(music, (0, max(0, len(vbuf) - len(music))))[:len(vbuf)]
    venv = np.convolve(np.abs(vbuf), np.ones(4410) / 4410, 'same')
    duck = 1 - 0.55 * np.clip(venv / 0.05, 0, 1)
    mix = vbuf * 1.0 + music * duck * 0.9
    mix = mix / max(1e-6, np.max(np.abs(mix))) * 0.95
    wav = os.path.join(bdir, 'mix_%s.wav' % lang); write_wav(wav, mix[:int(total * SR)])

    # frames: render the 4 mouth/blink states per line (and idle per scene)
    cache = {}
    def img(si, line, mo, bl):
        key = (si, line[1] if line else None, mo, bl)
        if key not in cache:
            p = os.path.join(bdir, 'f_%s_%d_%d_%d_%d.png' % (lang, si, len(cache), mo, bl))
            cache[key] = shoot(page(ep.SCENES[si], lang, line, mo, bl), p, prof)
        return cache[key]

    plates, kar, counts = {}, {}, {}
    def plate(si):
        if si not in plates:
            plates[si] = shoot(page(ep.SCENES[si], lang, None, 0, 0, empty=True), os.path.join(bdir, 'p_%s_%d.png' % (lang, si)), prof)
        return plates[si]
    def karaoke(si, line):
        key = (si, line[1])
        if key not in kar:
            n = len(kar); sc = ep.SCENES[si]
            rects = word_rects(page(sc, lang, line, 0, 0, probe=True), os.path.join(bdir, 'k_%s_%d.html' % (lang, n)), prof)
            lit = shoot(page(sc, lang, line, 0, 0, wmode='lit'), os.path.join(bdir, 'kl_%s_%d.png' % (lang, n)), prof)
            hot = shoot(page(sc, lang, line, 0, 0, wmode='hot'), os.path.join(bdir, 'kh_%s_%d.png' % (lang, n)), prof)
            words = [w for w in (line[1] if lang == 'kn' else line[2]).split(' ') if w]
            if len(rects) != len(words): rects = []
            wt = np.cumsum([len(w) + 1.5 for w in words]); wt = wt / wt[-1] if len(wt) else wt
            kar[key] = (rects, lit, hot, wt)
        return kar[key]
    def count_imgs(si):
        if si not in counts:
            sc = ep.SCENES[si]
            cards = countup_cards(sc['card_' + lang]) if sc.get('hit') and not sc.get('chorus') else None
            counts[si] = [shoot(page(sc, lang, None, 0, 0, card=c), os.path.join(bdir, 'c_%s_%d_%d.png' % (lang, si, i)), prof).crop(CARD_BOX)
                          for i, c in enumerate(cards)] if cards else []
        return counts[si]

    spans = {}
    for (a0, a1, si, ln) in timeline:
        if ln is None: spans[si] = (a0, a1)
    for (a0, a1, si, ln) in timeline:
        if ln is not None and ln[0] == 'c':
            s0, s1 = spans.get(si, (a0, a1)); spans[si] = (min(s0, a0), max(s1, a1 + 1.0))
    lines_by_t = [(a0, a1, si, ln) for (a0, a1, si, ln) in timeline if ln is not None]
    rms = np.sqrt(np.convolve(vbuf ** 2, np.ones(1764) / 1764, 'same'))

    ff = subprocess.Popen([FFMPEG, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '%dx%d' % (W, H), '-r', str(FPS),
                           '-i', '-', '-i', wav, '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p',
                           '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    nframes = int(total * FPS)
    last_line = {}
    for fi in range(nframes):
        tt = fi / FPS
        si = max([s for s, (a0, a1) in spans.items() if a0 <= tt] or [0])
        a0, a1 = spans[si]
        cur = None
        for (b0, b1, s2, ln) in lines_by_t:
            if s2 == si and b0 <= tt: cur = ln
        if cur is None:
            cur = next((ln for (b0, b1, s2, ln) in lines_by_t if s2 == si), None)
        speaking = any(b0 <= tt <= b1 and s2 == si for (b0, b1, s2, ln) in lines_by_t)
        r = rms[min(len(rms) - 1, int(tt * SR))]
        mo = 1 if (speaking and r > 0.02 and (fi // 2) % 3 != 2) else 0
        bl = 1 if (tt % 3.3) < 0.12 else 0
        if cur and cur[0] == 'c':
            mo = 1 if r > 0.03 else 0
        im = img(si, cur, mo, bl)
        sc = ep.SCENES[si]
        if not sc.get('chorus'):
            im = im.copy(); pl = plate(si)
            if cur and cur[0] in ('m', 'k'):
                cb0, cb1 = next((b0, b1) for (b0, b1, s2, ln) in lines_by_t if s2 == si and ln is cur)
                first = next(ln for (b0, b1, s2, ln) in lines_by_t if s2 == si) is cur
                # word-by-word captions: spoken words go solid, the word being said gets the dark pill
                rects, lit, hot, wt = karaoke(si, cur)
                if rects and tt >= cb0:
                    u = (tt - cb0) / max(0.05, cb1 - cb0)
                    wi = int(np.searchsorted(wt, u, side='right')) if u < 1 else len(rects)
                    for j, (rx0, ry0, rx1, ry1) in enumerate(rects[:wi + 1]):
                        bx = (max(0, rx0 - 6), max(0, ry0 - 6), min(W, rx1 + 6), min(H, ry1 + 6))
                        if j < wi: im.paste(lit.crop(bx), bx[:2])
                        elif j == wi: im.paste(hot.crop(bx), bx[:2])
                # bubble pops in on each new line
                pop0 = a0 + 0.12 if first else cb0
                anchor = (0.22, 1.0) if cur[0] == 'm' else (0.78, 1.0)
                if tt < pop0: fx(im, pl, BUB_BOX, alpha=0.0)
                elif tt - pop0 < 0.24:
                    u = (tt - pop0) / 0.24
                    fx(im, pl, BUB_BOX, s=0.86 + 0.14 * ease_back(u), alpha=u * 2.5, anchor=anchor)
            # card entrance: figures count up and land with a punch on hits; other cards slide up
            te = tt - a0
            if sc.get('hit'):
                ci = count_imgs(si)
                if ci and te < 0.56: im.paste(ci[min(len(ci) - 1, int(te / 0.08))], CARD_BOX[:2])
                if te < 0.4: fx(im, pl, CARD_BOX, s=1 + 0.2 * (1 - ease_out(te / 0.4)), alpha=te / 0.12)
            elif te < 0.4:
                e = ease_out(te / 0.4); fx(im, pl, CARD_BOX, alpha=e, dy=(1 - e) * 60)
        # camera push-in across the scene, shake + flash on hits
        p = (tt - a0) / max(0.1, a1 - a0)
        z = 1.0 + 0.06 * min(1, max(0, p))
        dx = dy = 0
        flash = 0.0
        for h in hits:
            if 0 <= tt - h < 0.35:
                k_ = 1 - (tt - h) / 0.35
                dx, dy = int(14 * k_ * math.sin(tt * 90)), int(10 * k_ * math.cos(tt * 77))
                flash = 0.3 * max(0.0, 1 - (tt - h) / 0.16)
        cw, ch = int(W / z), int(H / z)
        x0 = (W - cw) // 2 + dx; y0 = int((H - ch) * 0.35) + dy
        x0 = max(0, min(W - cw, x0)); y0 = max(0, min(H - ch, y0))
        fr = im.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.BILINEAR)
        arr = np.asarray(fr, dtype=np.float32)
        if flash: arr = arr * (1 - flash) + 255 * flash
        ff.stdin.write(arr.astype(np.uint8).tobytes())
    ff.stdin.close(); ff.wait()
    print('wrote', out, 'frames', nframes, 'renders', len(cache))


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else os.path.join(HERE, 'build_talk'))
