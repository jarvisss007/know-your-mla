import sys, io, json, re
p, distf = sys.argv[1], sys.argv[2]
s = io.open(p, encoding='utf-8').read()

NAME = {'Ballary': 'Ballari', 'Bangalore Rural': 'Bengaluru Rural', 'Bangalore Urban': 'Bengaluru Urban', 'Devangere': 'Davanagere',
        'Mysore': 'Mysuru', 'Shimoga': 'Shivamogga', 'Chikmagalur': 'Chikkamagaluru'}
dist = {}
for r in json.load(io.open(distf, encoding='utf-8')):
    dist[r['c']] = NAME.get(r['dist'], r['dist'])
D = json.loads(re.search(r'const D = (\[.*?\]);', s, re.S).group(1))
missing = [d['c'] for d in D if d['c'] not in dist]
if missing:
    print('MISSING', missing)
    # Sarvagnanagar is a Bengaluru Urban seat
    for c in missing:
        if c.lower().startswith('sarvagn'): dist[c] = 'Bengaluru Urban'
    missing = [d['c'] for d in D if d['c'] not in dist]
    assert not missing, missing
ALL = sorted(set(dist[d['c']] for d in D))
assert len(ALL) == 31, ALL

# tag table rows in the districts section by the districts named in their first cell
SMART = ['Bengaluru Urban', 'Tumakuru', 'Dharwad', 'Belagavi', 'Dakshina Kannada', 'Shivamogga', 'Davanagere']
a, b = s.index('<section class="block" id="districts">'), s.index('</section>', s.index('<section class="block" id="districts">'))
sec = s[a:b]
def tag(m):
    first = m.group(1)
    if first == 'All districts': ds = ALL
    elif first == 'Seven cities': ds = SMART
    else: ds = [x.strip() for x in first.split(',')]
    for x in ds: assert x in ALL, x
    return f'<tr data-d="{"|".join(ds)}"><td>{first}</td>'
sec2, n = re.subn(r'<tr><td>([^<]+)</td>', tag, sec)
picker = '''<div class="dpick"><label for="dsel" id="dlab">Choose your district</label><select id="dsel"></select></div>
    <div id="dsum" class="dsum" hidden></div>
    <h3>Where the money went</h3>'''
sec2 = sec2.replace('<h3>Where the money went</h3>', picker, 1)
sec2 = sec2.replace('<tbody>', '<tbody class="dt">')
sec2 = sec2.replace('<h3>Children and women</h3>', '<p id="dnone1" class="dnone" hidden></p>\n    <h3>Children and women</h3>', 1)
sec2 = sec2.replace('    <p>Kalaburagi: income', '    <p id="dnone2" class="dnone" hidden></p>\n    <p data-d="Kalaburagi" class="dline">Kalaburagi: income', 1)
s = s[:a] + sec2 + s[b:]
print('tagged rows', n)

css = '''
.dpick{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:14px 0 6px}
.dpick label{font-weight:600}
.dpick select{font:inherit;font-size:17px;padding:10px 12px;border-radius:10px;background:var(--card,#161b22);color:inherit;border:1px solid #3a4250;min-width:240px;max-width:100%}
.dsum{background:var(--card,#161b22);border:1px solid #2b3240;border-left:4px solid #f2b705;border-radius:12px;padding:14px 16px;margin:8px 0 14px}
.dsum .big3{display:flex;flex-wrap:wrap;gap:18px;margin:6px 0 10px}
.dsum .big3 div b{display:block;font-size:24px}
.dsum .big3 div span{font-size:13px;opacity:.75}
.dsum ul{list-style:none;padding:0;margin:6px 0 0;display:flex;flex-wrap:wrap;gap:6px}
.dsum li button{font:inherit;font-size:14px;background:transparent;color:inherit;border:1px solid #3a4250;border-radius:999px;padding:4px 10px;cursor:pointer}
.dsum li button:hover,.dsum li button:focus-visible{border-color:#f2b705}
.dsum li small{opacity:.7}
.dnone{opacity:.8;font-style:italic}
'''
last = s.rindex('</style>')
s = s[:last] + css + s[last:]

js = '''
const DIST = ''' + json.dumps({d['c']: dist[d['c']] for d in D}, ensure_ascii=False) + ''';
const DUI = {
  en: { lab: 'Choose your district', all: 'All 31 districts', mlas: 'MLAs', assets: 'combined declared assets', cases: 'with declared cases', tap: 'Tap a name to open their record.', none1: 'No project in this district has been through the second check yet. Research continues.', none2: 'No district health figure has been checked for this district yet.', cr: v => 'Rs ' + v + ' cr' },
  kn: { lab: 'ನಿಮ್ಮ ಜಿಲ್ಲೆ ಆಯ್ಕೆಮಾಡಿ', all: 'ಎಲ್ಲ 31 ಜಿಲ್ಲೆಗಳು', mlas: 'ಶಾಸಕರು', assets: 'ಒಟ್ಟು ಘೋಷಿತ ಆಸ್ತಿ', cases: 'ಪ್ರಕರಣ ಘೋಷಿಸಿದವರು', tap: 'ದಾಖಲೆ ನೋಡಲು ಹೆಸರಿನ ಮೇಲೆ ಒತ್ತಿ.', none1: 'ಈ ಜಿಲ್ಲೆಯ ಯಾವ ಯೋಜನೆಯೂ ಇನ್ನೂ ಎರಡನೇ ಪರಿಶೀಲನೆ ಮುಗಿಸಿಲ್ಲ. ಸಂಶೋಧನೆ ಮುಂದುವರಿದಿದೆ.', none2: 'ಈ ಜಿಲ್ಲೆಯ ಆರೋಗ್ಯ ಅಂಕಿಗಳನ್ನು ಇನ್ನೂ ಪರಿಶೀಲಿಸಿಲ್ಲ.', cr: v => '₹' + v + ' ಕೋಟಿ' }
};
let dsel = '';
try { dsel = localStorage.getItem('kym-dist') || '' } catch (e) {}
function districts() {
  const t = DUI[lang], sel = $('dsel'), names = [...new Set(Object.values(DIST))].sort();
  if (dsel && !names.includes(dsel)) dsel = '';
  $('dlab').textContent = t.lab; $('dlab').classList.toggle('kn', lang === 'kn');
  sel.innerHTML = `<option value="">${t.all}</option>` + names.map(n => `<option${n === dsel ? ' selected' : ''}>${n}</option>`).join('');
  const tabs = document.querySelectorAll('#districts tbody.dt');
  tabs.forEach((tb, i) => {
    let shown = 0;
    tb.querySelectorAll('tr').forEach(tr => { const on = !dsel || tr.dataset.d.split('|').includes(dsel); tr.hidden = !on; if (on) shown++ });
    const msg = $('dnone' + (i + 1)); msg.hidden = shown > 0; msg.textContent = i ? t.none2 : t.none1;
    tb.closest('.tw').hidden = shown === 0;
  });
  document.querySelectorAll('#districts .dline').forEach(p => { p.hidden = !!dsel && p.dataset.d !== dsel });
  const box = $('dsum');
  if (!dsel) { box.hidden = true; return }
  const ms = D.filter(d => DIST[d.c] === dsel).sort((x, y) => (y.a ?? -1) - (x.a ?? -1));
  const tot = ms.reduce((z, d) => z + (d.a || 0), 0), withK = ms.filter(d => d.k > 0).length;
  const byP = {}; ms.forEach(d => { byP[d.p] = (byP[d.p] || 0) + 1 });
  const pp = Object.entries(byP).sort((x, y) => y[1] - x[1]).map(([p, n]) => `<span class="party ${pclass(p)}">${esc(u().party[p] || p)} ${n}</span>`).join(' ');
  box.hidden = false;
  box.innerHTML = `<h3 style="margin:0">${esc(dsel)}</h3><div class="big3"><div><b>${ms.length}</b><span>${t.mlas}</span></div><div><b>${t.cr(Math.round(tot).toLocaleString('en-IN'))}</b><span>${t.assets}</span></div><div><b>${withK}</b><span>${t.cases}</span></div></div><p style="margin:0 0 6px">${pp}</p><p style="margin:0;font-size:14px;opacity:.8">${t.tap}</p><ul>`
    + ms.map(d => `<li><button type="button" data-n="${esc(d.n)}">${esc(d.n)} <small>· ${esc(d.c)}${d.a != null ? ' · ' + t.cr(num(d.a).lakh ? (d.a).toFixed(2) : num(d.a)) : ''}</small></button></li>`).join('') + '</ul>';
}
$('dsel').addEventListener('change', e => { dsel = e.target.value; try { localStorage.setItem('kym-dist', dsel) } catch (x) {} districts() });
$('dsum').addEventListener('click', e => { const b = e.target.closest('button[data-n]'); if (!b) return;
  $('q').value = b.dataset.n; party = 'All'; showAll = false;
  document.querySelectorAll('.chip[data-p]').forEach(c => c.setAttribute('aria-pressed', c.dataset.p === 'All'));
  render(); document.getElementById('find').scrollIntoView({ behavior: 'smooth' }) });
$('lang').addEventListener('click', districts);
districts();
'''
end = s.rindex('</script>')
s = s[:end] + js + s[end:]
s = s.replace("const FIXED = '.lead, .updated, .nav a, section.block h2,", "const FIXED = '.lead, .updated, .nav a, section.block h2, #districts > h3,", 1)
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
