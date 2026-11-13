import sys, io
p = sys.argv[1]
s = io.open(p, encoding='utf-8').read()

def a(url, label):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, label)

def mn(y23, y18):
    out = []
    if y18: out.append(a('https://www.myneta.info/karnataka2018/candidate.php?candidate_id=%d' % y18, '2018'))
    if y23: out.append(a('https://www.myneta.info/Karnataka2023/candidate.php?candidate_id=%d' % y23, '2023'))
    return out

CARDS = [
 ('B.Z. Zameer Ahmed Khan', 'Housing · Chamrajpet', [
   'A disproportionate-assets case registered in May 2022 is pending. The High Court declined to quash it in 2023, and in July 2026 Lokayukta police were reported to have sought sanction to prosecute. No court has ruled.',
   'His 2023 affidavit declares Rs 31.39 crore owed to 35 individuals and firms, against Rs 3.92 crore in bank loans. No link between any lender and his department was found.'],
  mn(7812, 5995) + [a('https://www.livelaw.in/high-court/karnataka-high-court/karnataka-high-court-dismisses-congress-mla-zameer-ahmed-khan-plea-disproportionate-a', 'LiveLaw')]),
 ('K.J. George', 'Energy, Tourism · Sarvagnanagar', [
   'He and his wife declared about Rs 80 crore in 2018 and about Rs 215 crore in 2023. ADR could not analyse his 2023 affidavit because no clear copy was on the Election Commission site.',
   'His affidavit lists a Rs 4 crore loan to Siddaramaiah, whose own affidavit lists the same debt. Both disclosed it; neither gives a date or purpose.',
   'The High Court quashed two cases against him, in 2020 and 2025.'],
  [a('https://myneta.info/karnataka2018/candidate.php?candidate_id=6647', '2018'),
   a('https://data.opencity.in/dataset/karnataka-assembly-elections-2023-affidavits/resource/0d78c24d-edbd-4737-983a-5eec40833b9e', '2023 scan'),
   a('https://adrindia.org/sites/default/files/Karnataka_Minister_Report_Post_Cabinet_Expansion_on_03_August_2026_English.pdf', 'ADR report')]),
 ('Byrathi Suresh', 'Transport · Hebbal', [
   'Six properties dated 30 March 2023, two weeks before he filed, are listed at zero purchase cost and about Rs 59.4 crore in value. The affidavit does not say how they were acquired; a family partition or gift would fit.',
   'Declared family assets rose from about Rs 417 crore to Rs 648 crore, and bank loans from about Rs 20 crore to Rs 83 crore.'],
  mn(7994, 7040)),
 ('N. Chaluvaraya Swamy', 'Major and Medium Irrigation · Nagamangala', [
   'About Rs 23.2 crore of his property increase comes from four entries dated 2018 to 2021 with no purchase cost. The affidavit describes two as gifts from siblings.',
   'His wife declared about Rs 5.72 crore of income for 2018-19, against Rs 28 to 47 lakh in each of the other four years. The affidavit does not ask for the source.'],
  mn(7590, 6358)),
 ('K.M. Shivalinge Gowda', 'Excise · Arsikere', [
   'Family assets rose from about Rs 1.68 crore to Rs 9.43 crore, but debts rose from Rs 5 lakh to about Rs 7.36 crore, so declared net worth is about Rs 2.07 crore.',
   'About Rs 3.47 crore of the debt is described only as business-related, without naming who is owed.'],
  mn(7824, 6610)),
 ('Ramalinga Reddy', 'Forest, Ecology and Environment · B.T.M. Layout', [
   'Declared assets rose from about Rs 66.6 crore to Rs 110.7 crore. Land bought between filings cost less than the income he declared.',
   'His 2023 filing lists commercial buildings as two lump sums, about Rs 45.1 crore and Rs 12.9 crore, with no address, date or cost.'],
  mn(7832, 6029)),
 ('Ajay Singh', 'Minor Irrigation, Science and Technology · Jevargi', [
   'Property bought between filings cost about Rs 3.41 crore, against about Rs 8.31 crore of declared income.',
   'Land in Tamil Nadu declared in 2013 and 2018 is not in his 2023 affidavit. Affidavits are not required to record sales.'],
  mn(7410, 6869)),
 ('Priyank Kharge', 'Home, IT and BT · Chittapur', [
   'Clean on the money tests: no property bought since 2018, and his debts fell.',
   'He declares stakes in three technology or services firms while serving as IT minister. He declares no government contracts, and no state benefit to those firms was found.'],
  mn(7211, 6143)),
 ('K.S. Basavanthappa', 'Muzrai, Fisheries and Ports · Mayakonda', [
   'Declared assets fell from Rs 1.73 crore to Rs 1.01 crore.',
   'Land declared at about Rs 1.43 crore in 2018 is not in his 2023 affidavit. The archive copy of the 2018 filing is misaligned, so this needs checking against the original.'],
  mn(7555, 6622)),
]

INTRO = 'Nine members of the cabinet were put through six public-record tests, and every finding was re-derived by an independent check. No test produced proof of wrongdoing. These are the open questions and the clean results. The Deputy Chief Minister and nineteen other ministers have not been tested yet.'
INTRO_KN = 'ಸಚಿವ ಸಂಪುಟದ ಒಂಬತ್ತು ಸದಸ್ಯರ ಪ್ರಮಾಣಪತ್ರಗಳು ಮತ್ತು ಸಾರ್ವಜನಿಕ ದಾಖಲೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ, ಪ್ರತಿ ಅಂಶವನ್ನೂ ಸ್ವತಂತ್ರವಾಗಿ ಮರುಪರಿಶೀಲಿಸಲಾಗಿದೆ. ಯಾವ ಪರೀಕ್ಷೆಯೂ ತಪ್ಪಿನ ಪುರಾವೆ ನೀಡಿಲ್ಲ. ಉಪಮುಖ್ಯಮಂತ್ರಿ ಮತ್ತು ಇತರ ಹತ್ತೊಂಬತ್ತು ಸಚಿವರನ್ನು ಇನ್ನೂ ಪರಿಶೀಲಿಸಿಲ್ಲ. ವಿವರಗಳು ಸದ್ಯ ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿವೆ.'

cards = ''
for name, meta, lis, src in CARDS:
    cards += '      <div class="card"><h3>%s</h3><p class="meta">Congress · %s</p><ul>\n' % (name, meta)
    cards += '\n'.join('        <li>%s</li>' % l for l in lis)
    cards += '</ul><p class="src">Sources: %s</p></div>\n' % ' · '.join(src)

section = ('  <section class="block" id="cabinet">\n    <h2>Nine ministers tested</h2>\n    <p>%s</p>\n    <div class="cards">\n%s    </div>\n  </section>\n\n' % (INTRO, cards))

def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60])
    s = s.replace(old, new)

assert 'id="cabinet"' not in s
rep('  <section class="block" id="state">', section + '  <section class="block" id="state">')
rep('<a href="#tested">Five MLAs tested</a>', '<a href="#tested">Five MLAs tested</a><a href="#cabinet">Nine ministers tested</a>')
rep('<p class="updated">Last updated 12 November 2026</p>', '<p class="updated">Last updated 13 November 2026</p>')
rep("'Last updated 12 November 2026': 'ಕೊನೆಯ ನವೀಕರಣ: 12 ನವೆಂಬರ್ 2026',",
    "'Last updated 13 November 2026': 'ಕೊನೆಯ ನವೀಕರಣ: 13 ನವೆಂಬರ್ 2026',\n  'Nine ministers tested': 'ಪರಿಶೀಲಿಸಿದ ಒಂಬತ್ತು ಸಚಿವರು',\n  '%s': '%s'," % (INTRO, INTRO_KN))
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('ok', len(s))
