import io, sys
p = sys.argv[1]
s = io.open(p, encoding='utf-8').read()
assert 'id="eyes"' not in s
ISSUE = 'https://github.com/jarvisss007/know-your-mla/issues/new'
rti = [
 ('A project in your district',
  'Under the RTI Act 2005, please provide for [project name] in [district]: (1) the administrative approval with date and sanctioned cost; (2) every revised estimate with date and amount; (3) total expenditure to date; (4) the original and current completion dates; (5) copies of the last three progress reports; (6) names of contractors and amounts paid to each.'),
 ('Your MLA\'s local area fund',
  'Under the RTI Act 2005, please provide for the Legislators\' Local Area Development fund of [MLA name], [constituency], for 2023-24 to date: (1) amounts released each year; (2) the list of works sanctioned, with location, cost and date; (3) works completed and amounts paid; (4) any unspent or lapsed balance.'),
 ('Vacant posts in your hospital or school',
  'Under the RTI Act 2005, please provide for [hospital/school name], [taluk]: (1) the sanctioned posts by category; (2) posts filled and vacant as on today; (3) the date since which each post has been vacant; (4) steps taken to fill them.'),
]
cards = ''.join(
 '<div class="card"><h3>%s</h3><p class="rtitxt">%s</p><p><button type="button" class="rcb rticp">Copy</button></p></div>' % (t, x) for t, x in rti)
sec = f'''  <section class="block" id="eyes">
    <h2>Be our eyes</h2>
    <p>Investigators who uncover hidden money work on the ground. You can be that, in your own town. Pick a project from the District by district list, go and see it, and send us dated photos, or file a Right to Information request and send us the reply. Every reply is an official record nobody can dismiss.</p>
    <ul class="plain">
      <li><b>Photos:</b> take them yourself, in a public place, with the date and location visible. Never photograph people or private property.</li>
      <li><b>RTI:</b> an application costs Rs 10 and must be answered within 30 days. Address it to the Public Information Officer of the department.</li>
      <li><b>Send it:</b> <a href="{ISSUE}" target="_blank" rel="noopener">open an issue on GitHub</a> with your district, the project and your evidence. We check everything before using it, and never publish your name without asking.</li>
    </ul>
    <h3>Ready-to-use RTI requests</h3>
    <div class="cards">{cards}</div>
  </section>

'''
anchor = '  <section class="block" id="press">'
assert anchor in s
s = s.replace(anchor, sec + anchor, 1)
s = s.replace('<a href="#districts">District by district</a>', '<a href="#districts">District by district</a><a href="#eyes">Be our eyes</a>', 1)
kn = '''  "Be our eyes": "ನಮ್ಮ ಕಣ್ಣಾಗಿ",
  "Ready-to-use RTI requests": "ತಕ್ಷಣ ಬಳಸಬಹುದಾದ ಆರ್‌ಟಿಐ ಅರ್ಜಿಗಳು",
'''
k_anchor = "  'State of the state': 'ರಾಜ್ಯದ ಸ್ಥಿತಿ',"
s = s.replace(k_anchor, kn + k_anchor, 1)
js = '''
document.querySelectorAll('.rticp').forEach(b => b.addEventListener('click', () => {
  const t = b.closest('.card').querySelector('.rtitxt').textContent;
  try { navigator.clipboard.writeText(t); b.textContent = lang === 'kn' ? 'ನಕಲಾಯಿತು' : 'Copied' } catch (e) {}
}));
'''
end = s.rindex('</script>')
s = s[:end] + js + s[end:]
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
