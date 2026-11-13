# Original flat-style characters for the "Mallanna asks" series (Gandaberunda).
# Mallanna: an ordinary voter. Neta: a FICTIONAL, party-less politician who appears once every five years.
# No party colours, symbols, caps or likenesses of real people.

SKIN_M, SKIN_N = '#a8714a', '#c28d62'

def _brows(expr):
    if expr == 'skeptic':
        return ('<path d="M168 168 q18 -10 34 -2" stroke="#1b1b1b" stroke-width="7" fill="none" stroke-linecap="round"/>'
                '<path d="M236 158 q18 -14 36 0" stroke="#1b1b1b" stroke-width="7" fill="none" stroke-linecap="round"/>')
    if expr == 'firm':
        return ('<path d="M166 160 l36 10" stroke="#1b1b1b" stroke-width="8" stroke-linecap="round"/>'
                '<path d="M274 160 l-36 10" stroke="#1b1b1b" stroke-width="8" stroke-linecap="round"/>')
    return ('<path d="M168 164 q17 -8 34 0" stroke="#1b1b1b" stroke-width="7" fill="none" stroke-linecap="round"/>'
            '<path d="M238 164 q17 -8 34 0" stroke="#1b1b1b" stroke-width="7" fill="none" stroke-linecap="round"/>')

def _mouth_m(expr):
    if expr == 'firm':
        return '<path d="M196 262 h48" stroke="#3a1a10" stroke-width="7" stroke-linecap="round"/>'
    if expr == 'skeptic':
        return '<path d="M198 266 q22 -8 44 4" stroke="#3a1a10" stroke-width="7" fill="none" stroke-linecap="round"/>'
    if expr == 'smile':
        return '<path d="M196 258 q24 18 48 0" stroke="#3a1a10" stroke-width="7" fill="none" stroke-linecap="round"/>'
    return '<path d="M198 262 q22 6 44 0" stroke="#3a1a10" stroke-width="7" fill="none" stroke-linecap="round"/>'

def mallanna(expr='neutral', hand=None):
    """Voter, drawn in a 440x560 box. expr: neutral|skeptic|firm|smile. hand: None|'stop'|'point'"""
    arm = ''
    if hand == 'stop':
        arm = ('<path d="M330 400 L400 300" stroke="#8fb8de" stroke-width="44" stroke-linecap="round"/>'
               '<rect x="372" y="236" width="56" height="70" rx="22" fill="%s"/>' % SKIN_M)
    elif hand == 'point':
        arm = ('<path d="M330 410 L404 370" stroke="#8fb8de" stroke-width="44" stroke-linecap="round"/>'
               '<circle cx="414" cy="364" r="24" fill="%s"/><rect x="420" y="356" width="40" height="14" rx="7" fill="%s"/>' % (SKIN_M, SKIN_M))
    return ('<g>'
            '<rect x="90" y="330" width="260" height="240" rx="70" fill="#8fb8de"/>'                      # shirt
            '<path d="M220 330 v240" stroke="#7aa4ca" stroke-width="6"/>'
            '<path d="M120 352 q60 -40 120 -10 l-20 220 h-60 z" fill="#2f8f5b"/>'                         # towel over shoulder
            '<path d="M140 372 h70 M134 410 h70 M130 448 h70" stroke="#e8e2c8" stroke-width="7"/>'
            + arm +
            '<rect x="194" y="290" width="52" height="56" fill="%s"/>' % SKIN_M +                          # neck
            '<ellipse cx="220" cy="200" rx="92" ry="104" fill="%s"/>' % SKIN_M +                           # head
            '<ellipse cx="128" cy="210" rx="16" ry="26" fill="%s"/><ellipse cx="312" cy="210" rx="16" ry="26" fill="%s"/>' % (SKIN_M, SKIN_M) +
            '<path d="M128 170 q-6 -96 92 -100 q98 4 92 100 q-26 -52 -92 -54 q-66 2 -92 54z" fill="#1f1a17"/>'  # hair
            + _brows(expr) +
            '<ellipse cx="186" cy="196" rx="10" ry="12" fill="#1b1b1b"/><ellipse cx="254" cy="196" rx="10" ry="12" fill="#1b1b1b"/>'
            '<path d="M220 206 q-8 22 0 30" stroke="#7a4a2c" stroke-width="6" fill="none" stroke-linecap="round"/>'
            '<path d="M168 246 q26 -22 52 -6 q26 -16 52 6 q-26 8 -52 -2 q-26 10 -52 2z" fill="#1f1a17"/>'   # moustache
            + _mouth_m(expr) +
            '</g>')

def neta(pose='namaste'):
    """Fictional politician, drawn in a 460x560 box. pose: namaste|gift|smug"""
    hands = ''
    if pose == 'namaste':
        hands = ('<path d="M140 480 L212 400 M320 480 L248 400" stroke="#d9d4c8" stroke-width="54" stroke-linecap="round"/>'
                 '<path d="M140 480 L212 400 M320 480 L248 400" stroke="#f4f1ea" stroke-width="44" stroke-linecap="round"/>'
                 '<path d="M206 410 q-4 -96 24 -112 q28 16 24 112 z" fill="%s" stroke="#8a5a3a" stroke-width="3"/>'
                 '<path d="M230 300 v108" stroke="#8a5a3a" stroke-width="3"/>' % SKIN_N)
    elif pose == 'gift':
        hands = ('<path d="M120 470 L60 420" stroke="#f4f1ea" stroke-width="46" stroke-linecap="round"/>'
                 '<rect x="-30" y="360" width="120" height="130" rx="12" fill="#7d4bb3"/>'
                 '<path d="M0 360 q30 -50 60 0" stroke="#5c3388" stroke-width="10" fill="none"/>'
                 '<rect x="-14" y="380" width="88" height="22" fill="#e9b949"/>'                           # sari folds
                 '<circle cx="62" cy="438" r="20" fill="#cfd5dd"/><rect x="50" y="410" width="24" height="14" rx="4" fill="#9aa3b2"/>'  # cooker lid
                 '<circle cx="30" cy="356" r="26" fill="%s"/>' % SKIN_N)
    else:
        hands = ('<path d="M150 470 L230 430 M310 470 L230 430" stroke="#f4f1ea" stroke-width="46" stroke-linecap="round"/>')
    mouth = ('<path d="M196 262 q34 32 68 0 z" fill="#5b1f16"/><path d="M204 264 h52" stroke="#fff" stroke-width="8"/>'
             if pose != 'smug' else '<path d="M200 262 q34 14 64 -8" stroke="#5b1f16" stroke-width="8" fill="none" stroke-linecap="round"/>')
    brows = ('<path d="M172 156 q18 -12 36 -2" stroke="#2a2a2a" stroke-width="7" fill="none"/><path d="M252 154 q18 -10 36 2" stroke="#2a2a2a" stroke-width="7" fill="none"/>')
    eyes = ('<path d="M178 196 q12 -12 24 0" stroke="#1b1b1b" stroke-width="7" fill="none" stroke-linecap="round"/>'
            '<path d="M258 196 q12 -12 24 0" stroke="#1b1b1b" stroke-width="7" fill="none" stroke-linecap="round"/>') if pose != 'smug' else (
            '<path d="M176 198 h28 M256 198 h28" stroke="#1b1b1b" stroke-width="8" stroke-linecap="round"/>')
    garland = ''.join('<circle cx="%d" cy="%d" r="15" fill="%s"/>' % (230 + 120 * __import__('math').cos(a / 10), 300 + 150 * __import__('math').sin(a / 10), '#f39c12' if i % 2 else '#e67e22')
                      for i, a in enumerate(range(5, 27, 2)))
    return ('<g>'
            '<rect x="60" y="320" width="340" height="260" rx="110" fill="#f4f1ea"/>'                     # kurta (portly)
            '<path d="M80 360 q150 120 300 -10 l10 60 q-160 110 -320 0z" fill="#8a8f98"/>'                # grey shawl
            '<rect x="204" y="284" width="52" height="50" fill="%s"/>' % SKIN_N +
            '<ellipse cx="230" cy="196" rx="100" ry="106" fill="%s"/>' % SKIN_N +
            '<ellipse cx="130" cy="206" rx="16" ry="26" fill="%s"/><ellipse cx="330" cy="206" rx="16" ry="26" fill="%s"/>' % (SKIN_N, SKIN_N) +
            '<path d="M134 160 q4 -80 96 -84 q94 4 96 84 q-40 -40 -120 -36 q-50 4 -72 36z" fill="#2b2b2b"/>'
            + brows + eyes +
            '<path d="M230 206 q-10 24 0 34" stroke="#8a5a3a" stroke-width="6" fill="none"/>'
            + mouth + garland + hands +
            '<rect x="296" y="476" width="36" height="16" rx="4" fill="#d4af37"/>'                         # gold watch
            '</g>')

def stage(m_expr='neutral', n_pose='namaste', m_hand=None, show_neta=True, extra=''):
    """850x470 stage: Mallanna left, Neta right."""
    n = '<g transform="translate(450 0) scale(0.84)">%s</g>' % neta(n_pose) if show_neta else ''
    return ('<svg viewBox="0 0 900 500" width="850" height="470" style="display:block;margin:10px 0 0">'
            '<rect x="0" y="470" width="900" height="30" rx="8" fill="#232935"/>'
            '<g transform="translate(10 -40) scale(0.9)">%s</g>' % mallanna(m_expr, m_hand) + n + extra +
            '<text x="890" y="26" text-anchor="end" font-family="Segoe UI" font-size="22" fill="#6f7888">Fictional characters · ಕಾಲ್ಪನಿಕ ಪಾತ್ರಗಳು</text>'
            '</svg>')

STYLE = '''<style>
.b{display:inline-block;background:#eceef2;color:#11141a;border-radius:34px;padding:22px 30px;font:700 46px/1.3 "Nirmala UI","Segoe UI",sans-serif;position:relative;max-width:820px;margin:8px 0}
.b small{display:block;font:500 30px/1.35 "Segoe UI",sans-serif;color:#454c58;margin-top:6px}
.b.m{background:#f2b705}.b.n{background:#eceef2;margin-left:120px}
.fact{border-left:8px solid #ef5261;padding:6px 0 6px 26px;margin-top:22px}
.fact b{display:block;font:800 76px/1.1 "Segoe UI","Nirmala UI",sans-serif;color:#ef5261}
.fact span{display:block;font:600 40px/1.3 "Nirmala UI","Segoe UI",sans-serif;color:#eceef2;margin-top:6px}
.fact i{display:block;font:400 32px/1.35 "Segoe UI",sans-serif;color:#9aa3b2;font-style:normal;margin-top:6px}
</style>'''

SKIN_K, SKIN_A = '#b37a52', '#a06a45'

def kaveri(expr='ask'):
    """Mallanna's daughter, 12, government-school uniform. Drawn in a 320x420 box. expr: ask|sad|smile"""
    mouth = {'ask': '<ellipse cx="160" cy="196" rx="12" ry="14" fill="#5b1f16"/>',
             'sad': '<path d="M140 204 q20 -14 40 0" stroke="#5b1f16" stroke-width="6" fill="none" stroke-linecap="round"/>',
             'smile': '<path d="M138 192 q22 18 44 0" stroke="#5b1f16" stroke-width="6" fill="none" stroke-linecap="round"/>'}[expr]
    brows = ('<path d="M118 128 q14 -10 28 -2 M174 126 q14 -8 28 2" stroke="#1b1b1b" stroke-width="5" fill="none" stroke-linecap="round"/>' if expr != 'sad'
             else '<path d="M118 124 q14 8 28 6 M174 130 q14 2 28 -6" stroke="#1b1b1b" stroke-width="5" fill="none" stroke-linecap="round"/>')
    return ('<g>'
            '<path d="M70 300 q90 -40 180 0 l20 120 h-220z" fill="#2c5aa0"/>'                    # pinafore
            '<path d="M110 262 h100 l10 60 h-120z" fill="#f4f1ea"/>'                               # shirt collar
            '<path d="M150 262 l10 26 l10 -26" fill="#c21f30"/>'                                  # tie
            '<rect x="140" y="230" width="40" height="40" fill="%s"/>' % SKIN_K +
            '<ellipse cx="160" cy="160" rx="72" ry="82" fill="%s"/>' % SKIN_K +
            '<path d="M88 150 q-2 -84 72 -86 q74 2 72 86 q-16 -44 -72 -48 q-56 4 -72 48z" fill="#1a1512"/>'
            '<path d="M92 160 q-30 60 -14 130" stroke="#1a1512" stroke-width="22" fill="none" stroke-linecap="round"/>'   # braids
            '<path d="M228 160 q30 60 14 130" stroke="#1a1512" stroke-width="22" fill="none" stroke-linecap="round"/>'
            '<circle cx="78" cy="292" r="14" fill="#c21f30"/><circle cx="242" cy="292" r="14" fill="#c21f30"/>'
            + brows +
            '<ellipse cx="134" cy="152" rx="9" ry="11" fill="#1b1b1b"/><ellipse cx="186" cy="152" rx="9" ry="11" fill="#1b1b1b"/>'
            + mouth +
            '<rect x="230" y="330" width="70" height="86" rx="6" fill="#f2b705"/><path d="M244 352 h42 M244 372 h42 M244 392 h30" stroke="#11141a" stroke-width="5"/>'  # notebook
            '</g>')

def amma():
    """Mallanna's mother, 70. Drawn in a 360x460 box."""
    return ('<g>'
            '<path d="M60 300 q120 -50 240 0 l20 160 h-280z" fill="#2f7d4f"/>'                     # sari
            '<path d="M70 300 q80 -20 120 40 l-30 120 h-90z" fill="#c9a227"/>'                      # pallu
            '<rect x="158" y="236" width="44" height="46" fill="%s"/>' % SKIN_A +
            '<ellipse cx="180" cy="160" rx="80" ry="88" fill="%s"/>' % SKIN_A +
            '<path d="M100 150 q2 -86 80 -88 q78 2 80 88 q-24 -50 -80 -52 q-56 2 -80 52z" fill="#bfbfbf"/>'
            '<circle cx="180" cy="66" r="26" fill="#bfbfbf"/>'                                      # bun
            '<circle cx="150" cy="158" r="22" fill="none" stroke="#333" stroke-width="5"/><circle cx="210" cy="158" r="22" fill="none" stroke="#333" stroke-width="5"/><path d="M172 158 h16" stroke="#333" stroke-width="5"/>'
            '<circle cx="150" cy="160" r="6" fill="#1b1b1b"/><circle cx="210" cy="160" r="6" fill="#1b1b1b"/>'
            '<path d="M158 214 q22 -10 44 0" stroke="#5b1f16" stroke-width="6" fill="none" stroke-linecap="round"/>'
            '<circle cx="180" cy="122" r="6" fill="#c21f30"/>'                                      # bindi
            '<path d="M290 300 l30 160" stroke="#6b4a2b" stroke-width="12" stroke-linecap="round"/>'  # walking stick
            '</g>')

def stage2(parts, label=True):
    """parts: list of (svg_group, x, y, scale). 900x500 viewBox."""
    g = ''.join('<g transform="translate(%d %d) scale(%s)">%s</g>' % (x, y, s, svg) for svg, x, y, s in parts)
    return ('<svg viewBox="0 0 900 500" width="850" height="470" style="display:block;margin:10px 0 0">'
            '<rect x="0" y="470" width="900" height="30" rx="8" fill="#232935"/>' + g +
            ('<text x="890" y="26" text-anchor="end" font-family="Segoe UI" font-size="22" fill="#6f7888">Fictional characters · ಕಾಲ್ಪನಿಕ ಪಾತ್ರಗಳು</text>' if label else '') +
            '</svg>')
