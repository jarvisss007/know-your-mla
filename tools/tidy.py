import sys, io
p = sys.argv[1]
s = io.open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:70])
    s = s.replace(old, new)

CSS = '''
/* Tidy pass: one-line sticky section bar, clearer search, phone-friendly tables */
html { scroll-behavior: smooth }
section.block, #find { scroll-margin-top: 60px }
.nav { position: sticky; top: 0; z-index: 5; flex-wrap: nowrap; overflow-x: auto; gap: 8px; margin: 0 -16px 22px; padding: 10px 16px; background: var(--bg); border-bottom: 1px solid var(--line); scrollbar-width: none; -webkit-overflow-scrolling: touch }
.nav::-webkit-scrollbar { display: none }
.nav a { flex: none; white-space: nowrap; font-size: 13px; padding: 6px 12px; border: 1px solid var(--line); border-radius: 999px; background: var(--surface); color: var(--fg) }
.nav a:hover { border-color: var(--accent); color: var(--accent) }
.facts { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px 20px }
.controls input[type=search] { font-size: 16px; padding: 14px 16px; border-width: 2px; border-color: var(--fg) }
.controls input[type=search]:focus { outline: 3px solid var(--yellow); outline-offset: 1px }
.controls select { padding: 13px 12px }
.more { display: block; width: 100%; padding: 13px 16px; font-weight: 600 }
@media (max-width: 640px) {
  .facts { grid-template-columns: repeat(2, minmax(0, 1fr)) }
  .controls select { flex: 1 1 100% }
  .tw { overflow: visible; border: 0; background: none }
  table.t, table.t tbody { display: block; min-width: 0 }
  table.t thead { display: none }
  table.t tr { display: block; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; margin-bottom: 8px }
  table.t td, table.t tr:last-child td { display: block; padding: 0; border: 0; margin-bottom: 6px; white-space: normal }
  table.t td:first-child { font-family: var(--display); font-weight: 500; font-size: 17px; white-space: normal; margin-bottom: 2px }
  table.t td:last-child { margin-bottom: 0; font-size: 13px }
  table.t:not(.lab) td:nth-child(2) { color: var(--muted); font-size: 13px }
  table.t.lab td[data-label]:not(:first-child)::before { content: attr(data-label); display: block; color: var(--muted); font-size: 11px; letter-spacing: .06em; text-transform: uppercase; margin-top: 6px }
}
</style>'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i+len('</style>'):]

# second table (State of the state) gets labelled cells on phones
i = s.index('<table class="t">', s.index('id="state"'))
s = s[:i] + '<table class="t lab">' + s[i + len('<table class="t">'):]

# keep phone labels in step with the current language
rep('''    if (lang === 'kn' && kn) { el.textContent = kn; el.classList.add('kn') } else { el.innerHTML = el.dataset.enHtml; el.classList.remove('kn') }
  });
}''', '''    if (lang === 'kn' && kn) { el.textContent = kn; el.classList.add('kn') } else { el.innerHTML = el.dataset.enHtml; el.classList.remove('kn') }
  });
  document.querySelectorAll('table.t.lab').forEach(tb => {
    const heads = [...tb.querySelectorAll('thead th')].map(th => th.textContent.trim());
    tb.querySelectorAll('tbody tr').forEach(tr => [...tr.children].forEach((td, i) => { td.dataset.label = heads[i] || '' }));
  });
}''')

rep("nomatch: 'No match'", "nomatch: 'No 2018 figure'")
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('ok')
