import sys, io
p = sys.argv[1]
s = io.open(p, encoding='utf-8').read()

def a(url, label):
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'

CAG10_26 = 'https://cag.gov.in/uploads/download_audit_report/2025/6.-Chapter-II---Planning-and-Financial-Management-069c3d2da1892f3.81971865.pdf'
CAG11_25 = 'https://cag.gov.in/uploads/download_audit_report/2025/Chapter-4---Implemention-of-Projects-and-Monitoring-06981df9e14b034.71900044.pdf'
CAG10_22 = 'https://cag.gov.in/uploads/download_audit_report/2022/Executive-summary-063f74dd849f3e5.57928385.pdf'
CAG7_25 = 'https://cag.gov.in/uploads/download_audit_report/2025/Chapter---III-Collection-of-DMFT-Funds-06943928230ce21.71895304.pdf'
CAG2_17 = 'https://cag.gov.in/uploads/download_audit_report/2017/Chapter_2_Performance_Audit_Karnataka_Report_No_2_of_2017_on_General_and_Social_Sector.pdf'
CAG8_25 = 'https://cag.gov.in/uploads/download_audit_report/2025/Chapter---III-Financial-resources-and-Utilisation-0694513dd546d02.17872728.pdf'

rows = [
 ('Kolar, Chikkaballapura', 'Yettinahole drinking water', 'Approved in 2012 at Rs 8,323.50 crore; now Rs 23,251.66 crore. Rs 15,297 crore spent by March 2024. No project report set a completion date, and the auditor found it "could not be made operational even after 12 years". The government now promises water by the end of 2027.', a(CAG10_26, 'CAG Report No. 10, 2026')),
 ('Bengaluru Urban', 'Namma Metro Phase 2', 'Approved in January 2014 at Rs 26,405 crore, due in 2020. Cost raised to Rs 40,425 crore in May 2025. The last section is now due March to May 2027.', a('https://www.theweek.in/wire-updates/national/2025/05/22/mds21-ka-cabinet-decisions.html', 'The Week (PTI)')),
 ('Bengaluru Urban, Bengaluru Rural', 'Suburban rail', 'Approved in October 2020 at Rs 15,767 crore. In June 2022 the Prime Minister promised it in 40 months (about October 2025); no corridor was built by then. Cost raised to Rs 16,876 crore in January 2026; the airport line is now due March 2030.', a('https://www.deccanherald.com/india/karnataka/bengaluru-suburban-rail-revival-new-k-ride-chief-lays-out-timelines-3873802', 'Deccan Herald')),
 ('Bagalkot, Vijayapura', 'Upper Krishna Project, Stage III', 'Approved in January 2012 at Rs 17,207 crore; revised to Rs 51,148.94 crore in October 2017; put at Rs 87,818 crore by the Chief Minister in September 2025, with 59,354 acres of land still to be acquired.', a('https://assets.thehansindia.com/karnataka/cabinet-approves-enhanced-compensation-of-rs-40-lakh-per-acre-1007165', 'The Hans India')),
 ('Chitradurga, Davanagere, Chikkamagaluru, Tumakuru', 'Upper Bhadra irrigation', 'Stage I approved in 2003 at Rs 2,813 crore; the whole project re-revised to Rs 21,473.67 crore in 2020, due March 2026. Rs 5,300 crore was put in the 2023-24 Union Budget, but the Centre told the Lok Sabha in August 2024 the project is under no central scheme. In August 2026 the Chief Minister said the money had not come.', a('https://sansad.in/getFile/loksabhaquestions/annex/182/AS257_FaOdjD.pdf?source=pqals', 'Lok Sabha reply')),
 ('Uttara Kannada, Dharwad', 'Hubballi-Ankola rail line', 'Sanctioned in the mid-1990s and inaugurated in 1999. By August 2024 only earthwork and bridges on the 47-km Hubballi-Kiravatti section were done; the rest awaits forest and wildlife clearance for 569.64 hectares.', a('https://sansad.in/getFile/loksabhaquestions/annex/182/AU2628_ddlChP.pdf?source=pqals', 'Lok Sabha reply')),
 ('Seven cities', 'Smart City Mission', 'Hubballi-Dharwad awarded 6 of 62 projects on time and Belagavi 3 of 107. Mangaluru dropped works and cannot use Rs 51.85 crore; Rs 9.44 crore of its drainage spending was "unfruitful". Davanagere\'s command centre opened 3 years 4 months late. Shivamogga had no full-time CEO for five years.', a(CAG11_25, 'CAG Report No. 11 of 2025')),
 ('Kalaburagi, Bidar, Yadgir, Raichur, Koppal, Ballari, Vijayanagara', 'Kalyana Karnataka development board', 'Spent 74% of released funds with physical progress of up to 70%. Rs 387.52 crore of assistance was lost because funds went unused (the government disputes this). 3,731 works worth Rs 738.65 crore were cancelled in 2013-21. In Kalaburagi, Rs 5.60 crore on five abandoned park works was "rendered wasteful".', a(CAG10_22, 'CAG Report No. 10 of 2022')),
 ('Ballari', 'Mining-area development fund', 'Of Rs 1,912.55 crore collected from 2015-16 to 2022-23, Rs 629.62 crore (39.5%) was used: the lowest of the five districts audited.', a(CAG7_25, 'CAG Report No. 7 of 2025')),
 ('Mysuru', '24x7 water supply', 'Rs 271.56 crore spent, and the city still did not get round-the-clock water. Coverage was cut from 69 zones to 47, and 25.69% to 37.01% of water was lost or unbilled, against a 15% condition.', a(CAG2_17, 'CAG Report No. 2 of 2017')),
 ('Kodagu', 'Flood and disaster funds', 'Rs 57.04 crore sat unspent with the Deputy Commissioner in March 2023, the largest such balance of nine districts audited. The DC told the auditor that structural flood-protection works were not taken up. After the 2018 floods, 845 houses were promised in six months; in April 2021 the minister said 786 of 836 families had houses.', a(CAG8_25, 'CAG Report No. 8 of 2025') + ' · ' + a('https://www.deccanherald.com/india/karnataka/162-houses-handed-over-to-kodagu-flood-victims-of-2018-977803.html', 'Deccan Herald')),
 ('Shivamogga', 'Airport', 'Foundation stone laid in 2008; the private contract was cancelled in 2015 with nothing built. Relaunched in 2020 at Rs 220 crore and opened in February 2023 at around Rs 450 crore.', a('https://www.deccanherald.com/india/karnataka/karnataka-cm-b-s-yediyurappa-relaunches-his-pet-shivamogga-airport-project-849767.html', 'Deccan Herald')),
 ('All districts', 'MLA and MLC local area funds', 'In December 2017 the Planning Minister said Rs 406 crore of these funds from 2002-2013 had lapsed unused, and about Rs 1,000 crore released from 2013 to September 2017 was still unspent.', a('https://www.deccanherald.com/content/648202/just-elections-govt-unearths-rs.html', 'Deccan Herald')),
]

NITI = 'https://www.niti.gov.in/sites/default/files/2022-07/'
health = [
 ('Tumakuru', 'Children under 5 who are stunted', '28.6%', '40.3%', a('http://web.archive.org/web/20221210034257id_/http://rchiips.org/nfhs/NFHS-5_FCTS/KA/Tumkur.pdf', 'NFHS-5 factsheet')),
 ('Tumakuru', 'Children 6-59 months with anaemia', '53.8%', '67.6%', a('http://web.archive.org/web/20221210034257id_/http://rchiips.org/nfhs/NFHS-5_FCTS/KA/Tumkur.pdf', 'NFHS-5 factsheet')),
 ('Bengaluru Rural', 'Children under 5 who are stunted', '28.7%', '36.6%', a('http://web.archive.org/web/20231017165448id_/http://rchiips.org/nfhs/NFHS-5_FCTS/KA/Bangalore%20Rural.pdf', 'NFHS-5 factsheet')),
 ('Dharwad', 'Children under 5 who are stunted', '37%', '45%', a(NITI + 'Dharwad-Karnataka.pdf', 'NITI district profile')),
 ('Gadag', 'Children under 5 who are stunted', '35%', '45%', a(NITI + 'Gadag-Karnataka.pdf', 'NITI district profile')),
 ('Chitradurga', 'Children under 5 who are stunted', '29%', '36%', a(NITI + 'Chitradurga-Karnataka.pdf', 'NITI district profile')),
 ('Uttara Kannada', 'Children 6-59 months with anaemia', '48%', '69%', a(NITI + 'Uttara%20Kannada-Karnataka.pdf', 'NITI district profile')),
 ('Shivamogga', 'Children 6-59 months with anaemia', '54%', '69%', a(NITI + 'Shimoga-Karnataka.pdf', 'NITI district profile')),
 ('Belagavi', 'Non-pregnant women 15-49 with anaemia', '41%', '53%', a(NITI + 'Belgaum-Karnataka.pdf', 'NITI district profile')),
 ('Yadgir', 'Children 6-59 months with anaemia', '74%', '76%', a(CAG10_22, 'CAG Report No. 10 of 2022')),
 ('Kalaburagi', 'Children 6-59 months with anaemia', '72.4%', '75.1%', a(CAG10_22, 'CAG Report No. 10 of 2022')),
 ('Raichur', 'Children 6-59 months with anaemia', '70.6%', '73.6%', a(CAG10_22, 'CAG Report No. 10 of 2022')),
 ('Haveri', 'Children under 5 who are stunted (improved)', '44%', '30%', a(NITI + 'Haveri-Karnataka.pdf', 'NITI district profile')),
 ('Chikkaballapura', 'Children under 5 who are stunted (improved)', '38%', '31%', a(NITI + 'Chikkaballapura-Karnataka.pdf', 'NITI district profile')),
]

R = '\n'.join(f'        <tr><td>{d}</td><td>{w}</td><td>{t}</td><td>{src}</td></tr>' for d, w, t, src in rows)
H = '\n'.join(f'        <tr><td>{d}</td><td>{m}</td><td>{x}</td><td>{y}</td><td>{src}</td></tr>' for d, m, x, y, src in health)

INTRO = 'Big projects and public funds across the 31 districts, as recorded by the national auditor, Parliament and the state government. Every figure here was checked a second time against the original document; where a later report changed the picture, the newer fact is shown.'
NOTE = 'Most of these projects ran under several governments of different parties. A late or over-cost project is a finding about the government of the day, not proof of personal wrongdoing by any MLA.'
HEALTHP = 'Two national health surveys, 2015-16 and 2019-21, measured the same things in every district. In these districts, things got worse; two improved.'

section = f'''  <section class="block" id="districts">
    <h2>District by district</h2>
    <p>{INTRO}</p>
    <h3>Where the money went</h3>
    <div class="tw"><table class="t lab">
      <thead><tr><th>District</th><th>Project or fund</th><th>What the record shows</th><th>Source</th></tr></thead>
      <tbody>
{R}
      </tbody>
    </table></div>
    <h3>Children and women</h3>
    <p>{HEALTHP}</p>
    <div class="tw"><table class="t lab">
      <thead><tr><th>District</th><th>Measure</th><th>2015-16</th><th>2019-21</th><th>Source</th></tr></thead>
      <tbody>
{H}
      </tbody>
    </table></div>
    <p>Kalaburagi: income per person grew 47.96% from 2013-14 to 2019-20, against 74.84% for the state ({a(CAG10_22, 'CAG')}).</p>
    <p>{NOTE}</p>
  </section>

'''
anchor = '  <section class="block" id="press">'
assert anchor in s and 'id="districts"' not in s
s = s.replace(anchor, section + anchor, 1)
s = s.replace('<a href="#state">State of the state</a>', '<a href="#state">State of the state</a><a href="#districts">District by district</a>', 1)

kn = f'''  "District by district": "ಜಿಲ್ಲಾವಾರು",
  "Where the money went": "ಹಣ ಎಲ್ಲಿ ಹೋಯಿತು",
  "Children and women": "ಮಕ್ಕಳು ಮತ್ತು ಮಹಿಳೆಯರು",
  "{INTRO}": "31 ಜಿಲ್ಲೆಗಳ ದೊಡ್ಡ ಯೋಜನೆಗಳು ಮತ್ತು ಸಾರ್ವಜನಿಕ ನಿಧಿಗಳು, ರಾಷ್ಟ್ರೀಯ ಲೆಕ್ಕಪರಿಶೋಧಕರು, ಸಂಸತ್ತು ಮತ್ತು ರಾಜ್ಯ ಸರ್ಕಾರದ ದಾಖಲೆಗಳಂತೆ. ಪ್ರತಿ ಅಂಕಿಯನ್ನೂ ಮೂಲ ದಾಖಲೆಯೊಂದಿಗೆ ಮತ್ತೊಮ್ಮೆ ಪರಿಶೀಲಿಸಲಾಗಿದೆ. ವಿವರಗಳು ಸದ್ಯ ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿವೆ.",
  "{NOTE}": "ಈ ಯೋಜನೆಗಳಲ್ಲಿ ಹೆಚ್ಚಿನವು ಬೇರೆ ಬೇರೆ ಪಕ್ಷಗಳ ಹಲವು ಸರ್ಕಾರಗಳ ಅವಧಿಯಲ್ಲಿ ನಡೆದಿವೆ. ತಡವಾದ ಅಥವಾ ವೆಚ್ಚ ಮೀರಿದ ಯೋಜನೆ ಆಗಿನ ಸರ್ಕಾರದ ಬಗ್ಗೆ ಸಂಶೋಧನೆ; ಯಾವುದೇ ಶಾಸಕರ ವೈಯಕ್ತಿಕ ತಪ್ಪಿನ ಪುರಾವೆ ಅಲ್ಲ.",
  "{HEALTHP}": "2015-16 ಮತ್ತು 2019-21ರ ಎರಡು ರಾಷ್ಟ್ರೀಯ ಆರೋಗ್ಯ ಸಮೀಕ್ಷೆಗಳು ಪ್ರತಿ ಜಿಲ್ಲೆಯಲ್ಲೂ ಒಂದೇ ಅಂಶಗಳನ್ನು ಅಳೆದಿವೆ. ಈ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಪರಿಸ್ಥಿತಿ ಹದಗೆಟ್ಟಿದೆ; ಎರಡರಲ್ಲಿ ಸುಧಾರಿಸಿದೆ.",
  "District": "ಜಿಲ್ಲೆ", "Project or fund": "ಯೋಜನೆ ಅಥವಾ ನಿಧಿ", "What the record shows": "ದಾಖಲೆ ಏನು ಹೇಳುತ್ತದೆ",
'''
k_anchor = "  'State of the state': 'ರಾಜ್ಯದ ಸ್ಥಿತಿ',"
assert k_anchor in s
s = s.replace(k_anchor, kn + k_anchor, 1)
io.open(p, 'w', encoding='utf-8').write(s)
print('ok', len(rows), len(health))
