import io, sys
p = sys.argv[1]
s = io.open(p, encoding='utf-8').read()
assert 'id="rc"' not in s

# 1. a "Report card" button on every MLA row
old = "+ `</dl><a href=\"${link}\" target=\"_blank\" rel=\"noopener\">${d.id || d.url ? t.read : t.find}</a></li>`;"
new = "+ `</dl><div class=\"acts\"><button type=\"button\" class=\"rcb\" data-n=\"${esc(d.n)}\">${RCUI[lang].btn}</button><a href=\"${link}\" target=\"_blank\" rel=\"noopener\">${d.id || d.url ? t.read : t.find}</a></div></li>`;"
assert old in s
s = s.replace(old, new, 1)

# 2. the card overlay markup, before </body>
markup = '<div id="rc" class="rc" hidden role="dialog" aria-modal="true" aria-labelledby="rcname"><div class="rcin"><button type="button" class="rcx" id="rcx" aria-label="Close">×</button><div id="rcbody"></div></div></div>\n'
i = s.rindex('<script>')
s = s[:i] + markup + s[i:]

# 3. styles
css = '''
.acts{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.rcb{font:inherit;font-size:14px;font-weight:600;background:#f2b705;color:#11141a;border:0;border-radius:999px;padding:6px 14px;cursor:pointer}
.rc{position:fixed;inset:0;background:rgba(5,7,10,.78);z-index:50;display:flex;align-items:flex-start;justify-content:center;padding:16px;overflow:auto}
.rc[hidden]{display:none}
.rcin{position:relative;background:#161b22;border:1px solid #2b3240;border-top:6px solid #f2b705;border-radius:14px;max-width:560px;width:100%;padding:20px 18px 18px;margin-top:4vh}
.rcx{position:absolute;right:10px;top:8px;font-size:28px;line-height:1;background:none;border:0;color:#9aa3b2;cursor:pointer}
.rcin h2{margin:0 0 2px;font-size:24px}
.rcin .sub{opacity:.75;margin:0 0 14px}
.rcg{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin:0 0 14px}
.rcg div{background:#11141a;border-radius:10px;padding:10px 12px}
.rcg b{display:block;font-size:20px}
.rcg span{font-size:13px;opacity:.75}
.rcin h3{font-size:16px;margin:14px 0 6px;color:#f2b705}
.rcin ul{margin:0;padding-left:18px}
.rcin li{margin:6px 0;font-size:14px;line-height:1.45}
.rcq{background:#11141a;border-left:4px solid #ef5261;padding:10px 12px;border-radius:8px;margin-top:12px}
.rcsh{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
.rcsh a,.rcsh button{font:inherit;font-weight:700;font-size:15px;border-radius:999px;padding:10px 16px;text-decoration:none;cursor:pointer;border:0}
.rcsh .wa{background:#25d366;color:#0b1f12}
.rcsh .cp{background:#2b3240;color:#eceef2}
.rcin .fine{font-size:12px;opacity:.65;margin-top:12px}
'''
last = s.rindex('</style>')
s = s[:last] + css + s[last:]

# 4. behaviour
js = r'''
const RCUI = {
  en: { btn: 'Report card', assets: 'Declared assets, 2023', growth: 'Since 2018', debts: 'Declared debts', cases: 'Declared criminal cases', dist: 'district', found: 'What the record shows in this district', none: 'No district finding has passed our second check yet.', ask: 'Questions to ask', q1: 'What work have you done in this constituency since 2023? Show me.', q2: 'Did you file this year\'s asset statement with the Lokayukta?', q3: 'When will the pending project in our district be finished, in writing?', wa: 'Share on WhatsApp', cp: 'Copy link', copied: 'Link copied', fine: 'Figures are self-declared in sworn affidavits (ADR / myneta.info) and not proof of wrongdoing. A declared case is not a conviction.', na: 'Not in archive' },
  kn: { btn: 'ವರದಿ ಕಾರ್ಡ್', assets: 'ಘೋಷಿತ ಆಸ್ತಿ, 2023', growth: '2018ರಿಂದ', debts: 'ಘೋಷಿತ ಸಾಲ', cases: 'ಘೋಷಿತ ಕ್ರಿಮಿನಲ್ ಪ್ರಕರಣಗಳು', dist: 'ಜಿಲ್ಲೆ', found: 'ಈ ಜಿಲ್ಲೆಯಲ್ಲಿ ದಾಖಲೆ ಏನು ಹೇಳುತ್ತದೆ', none: 'ಈ ಜಿಲ್ಲೆಯ ಯಾವ ಅಂಶವೂ ಇನ್ನೂ ಎರಡನೇ ಪರಿಶೀಲನೆ ಮುಗಿಸಿಲ್ಲ.', ask: 'ಕೇಳಬೇಕಾದ ಪ್ರಶ್ನೆಗಳು', q1: '2023ರಿಂದ ಈ ಕ್ಷೇತ್ರದಲ್ಲಿ ನೀವು ಮಾಡಿದ ಕೆಲಸ ಏನು? ತೋರಿಸಿ.', q2: 'ಈ ವರ್ಷದ ಆಸ್ತಿ ಘೋಷಣೆಯನ್ನು ಲೋಕಾಯುಕ್ತಕ್ಕೆ ಸಲ್ಲಿಸಿದ್ದೀರಾ?', q3: 'ನಮ್ಮ ಜಿಲ್ಲೆಯ ಬಾಕಿ ಯೋಜನೆ ಯಾವಾಗ ಮುಗಿಯುತ್ತದೆ? ಬರೆದು ಕೊಡಿ.', wa: 'ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಹಂಚಿ', cp: 'ಲಿಂಕ್ ನಕಲಿಸಿ', copied: 'ಲಿಂಕ್ ನಕಲಾಯಿತು', fine: 'ಅಂಕಿಗಳು ಶಾಸಕರೇ ಪ್ರಮಾಣಪತ್ರದಲ್ಲಿ ಘೋಷಿಸಿದವು (ಎಡಿಆರ್ / myneta.info); ತಪ್ಪಿನ ಪುರಾವೆಯಲ್ಲ. ಘೋಷಿತ ಪ್ರಕರಣ ಎಂದರೆ ಶಿಕ್ಷೆಯಲ್ಲ.', na: 'ಲಭ್ಯವಿಲ್ಲ' }
};
const SITE = 'https://jarvisss007.github.io/know-your-mla/';
function cardHTML(d) {
  const t = RCUI[lang], u0 = u(), dist = DIST[d.c] || '';
  const cr = v => v == null ? t.na : (lang === 'kn' ? '₹' : 'Rs ') + (v < 1 ? (v * 100).toFixed(0) + (lang === 'kn' ? ' ಲಕ್ಷ' : ' lakh') : num(v) + (lang === 'kn' ? ' ಕೋಟಿ' : ' crore'));
  const g = d.a18 ? Math.round(100 * (d.a23 - d.a18) / d.a18) : null;
  const rows = [...document.querySelectorAll('#districts tbody.dt:first-of-type tr, #districts .tw:first-of-type tbody tr')]
    .filter(tr => tr.dataset.d && tr.dataset.d.split('|').includes(dist))
    .map(tr => '<li><b>' + esc(tr.cells[1].textContent) + ':</b> ' + esc(tr.cells[2].textContent) + '</li>');
  const uniq = [...new Set(rows)];
  return `<h2 id="rcname">${esc(d.n)}</h2><p class="sub">${esc(d.c)} · ${esc(u0.party[d.p] || d.p)} · ${esc(dist)} ${t.dist}</p>`
    + `<div class="rcg"><div><b>${cr(d.a)}</b><span>${t.assets}</span></div><div><b>${g == null ? '—' : (g >= 0 ? '+' : '') + g + '%'}</b><span>${t.growth}</span></div>`
    + `<div><b>${d.l == null ? t.na : d.l > 0 ? cr(d.l) : '0'}</b><span>${t.debts}</span></div><div><b>${d.k == null ? t.na : d.k}</b><span>${t.cases}</span></div></div>`
    + `<h3>${t.found}</h3>` + (uniq.length ? '<ul>' + uniq.join('') + '</ul>' : `<p>${t.none}</p>`)
    + `<div class="rcq"><h3 style="margin-top:0">${t.ask}</h3><ul><li>${t.q1}</li><li>${t.q2}</li><li>${t.q3}</li></ul></div>`
    + `<div class="rcsh"><a class="wa" target="_blank" rel="noopener" id="rcwa">${t.wa}</a><button type="button" class="cp" id="rccp">${t.cp}</button></div>`
    + `<p class="fine">${t.fine}</p>`;
}
function openCard(name, push) {
  const d = D.find(x => x.n === name); if (!d) return;
  $('rcbody').innerHTML = cardHTML(d);
  $('rcbody').querySelectorAll('h2,h3,p,li,span').forEach(el => { if (lang === 'kn') el.classList.add('kn') });
  const link = SITE + '#mla=' + encodeURIComponent(d.n);
  const g = d.a18 ? Math.round(100 * (d.a23 - d.a18) / d.a18) : null;
  const msg = (lang === 'kn'
    ? `${d.n} (${d.c}) ವರದಿ ಕಾರ್ಡ್: ಘೋಷಿತ ಆಸ್ತಿ ₹${d.a != null ? num(d.a) : '?'} ಕೋಟಿ` + (g != null ? `, 2018ರಿಂದ ${g >= 0 ? '+' : ''}${g}%` : '') + `. ಕೆಲಸ ತೋರಿಸಿ, ಆಮೇಲೆ ಮತ. `
    : `Report card for ${d.n} (${d.c}): declared assets Rs ${d.a != null ? num(d.a) : '?'} crore` + (g != null ? `, ${g >= 0 ? '+' : ''}${g}% since 2018` : '') + `. Show me the work, then my vote. `) + link;
  $('rcwa').href = 'https://wa.me/?text=' + encodeURIComponent(msg);
  $('rccp').onclick = () => { try { navigator.clipboard.writeText(link); $('rccp').textContent = RCUI[lang].copied } catch (e) {} };
  $('rc').hidden = false; document.body.style.overflow = 'hidden';
  if (push) { try { history.replaceState(null, '', '#mla=' + encodeURIComponent(d.n)) } catch (e) {} }
  $('rcx').focus();
}
function closeCard() { $('rc').hidden = true; document.body.style.overflow = ''; if (location.hash.startsWith('#mla=')) { try { history.replaceState(null, '', location.pathname + location.search) } catch (e) {} } }
$('list').addEventListener('click', e => { const b = e.target.closest('.rcb'); if (b) openCard(b.dataset.n, true) });
$('rcx').addEventListener('click', closeCard);
$('rc').addEventListener('click', e => { if (e.target === $('rc')) closeCard() });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && !$('rc').hidden) closeCard() });
$('lang').addEventListener('click', () => { render(); const m = location.hash.match(/^#mla=(.+)$/); if (m && !$('rc').hidden) openCard(decodeURIComponent(m[1]), false) });
render();
{ const m = location.hash.match(/^#mla=(.+)$/); if (m) openCard(decodeURIComponent(m[1]), false); }
'''
end = s.rindex('</script>')
s = s[:end] + js + s[end:]
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
