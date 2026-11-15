import io, sys
p = sys.argv[1]
s = io.open(p, encoding='utf-8').read()
def a(url, label): return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'
C = 'https://d1jmc0u14z2tmp.cloudfront.net/uploads/download_audit_report/'
rows = [
 ('Ramanagara', 'Disaster-management funds', 'Rs 19.26 crore sat unspent with the Deputy Commissioner at the end of March 2023. The auditor said such balances let the state book money as spent when it was not.', a(C + '2025/Chapter---III-Financial-resources-and-Utilisation-0694513dd546d02.17872728.pdf', 'CAG Report No. 8 of 2025')),
 ('Haveri', 'Disaster-management funds', 'Rs 27.58 crore sat unspent with the Deputy Commissioner in March 2023. Flood losses in the district were put at Rs 2,720.64 crore in 2019 alone.', a(C + '2025/Chapter---III-Financial-resources-and-Utilisation-0694513dd546d02.17872728.pdf', 'CAG Report No. 8 of 2025')),
 ('Mandya', 'MySugar (state-owned sugar company)', 'Rs 124.08 crore spent on a co-generation plant and mill upgrade became "unfruitful": the plant, due in 2003, had its trial run in 2007 and was not run after that. The state paid Rs 59.04 crore more in interest. Accumulated losses: Rs 416.67 crore (2012-13 accounts).', a(C + '2016/Karnataka_PSUs_Report_No_3_2016.pdf', 'CAG Report No. 3 of 2016')),
 ('Hassan', 'Hassan airport', 'First proposed in 1967; foundation stone laid in 2007; Rs 193.65 crore cleared in June 2021. In December 2025 the minister said it would be finished in 2025-26, after the 2024-25 target was missed.', a('https://www.thenewsminute.com/article/karnataka-clears-rs-193-crores-funding-hassan-greenfield-airport-project-150406', 'The News Minute')),
 ('Chamarajanagar, Mysuru', 'Mysuru-Chamarajanagar rail electrification', 'Rs 81.05 crore spent electrifying the line without the Airports Authority\'s clearance, leaving it "unproductive" and costing Rs 80.20 lakh a month to keep running diesel engines.', a('https://cag.gov.in/uploads/PressRelease/PR-Press-Brief-English-Approved-06a80895d292804-53454298.pdf', 'CAG Report No. 14 of 2026 (Railways)')),
 ('Udupi', 'Varahi irrigation weir', 'Awarded in 2005 at Rs 13.47 crore; cost rose to Rs 72.33 crore. Rates revised without the tender discount gave the contractor an undue benefit of Rs 20.53 crore. In 2017 a legislator said Rs 689 crore had been spent on the project and its canal served only 3,375 hectares.', a(C.replace('d1jmc0u14z2tmp.cloudfront.net', 'cag.gov.in') + '2009/Karnataka_Commercial_2009_chap2.pdf', 'CAG, 2009') + ' · ' + a('https://daijiworld.com/news/newsDisplay?newsID=441413', 'Daijiworld, 2017')),
 ('Dakshina Kannada', 'Pumpwell flyover, Mangaluru', 'Due to open on 31 March 2013; opened on 31 January 2020, almost seven years late.', a('https://www.thenewsminute.com/karnataka/after-delay-over-10-years-pumpwell-flyover-inaugurated-mangaluru-117237', 'The News Minute')),
 ('Chikkamagaluru', 'Kadur-Chikkamagaluru-Belur rail line', 'Sanctioned in 1996-97. In January 2026, 30 years on, 56 of 68 km were in service and the Belur-Sakleshpur part was not yet built.', a('https://www.thehansindia.com/news/cities/bengaluru/chikkamagaluru-finally-connected-by-rail-1038917', 'The Hans India')),
 ('Gadag', 'Mother and child hospital, Gadag', 'Due in November 2015; finished in January 2019, 1,166 days late. Officials charged the contractor Rs 1,000 a day instead of the contractual Rs 25,950, a short levy of Rs 57.39 lakh.', a(C + '2021/9.%20Full%20Report-0614b01d87f87e6.86', 'CAG Report No. 3 of 2021')),
 ('Kodagu, Mysuru', 'Mysuru-Kushalnagar rail line', 'Sanctioned in February 2019 at Rs 1,854.62 crore; shelved in January 2026 for "low traffic potential and poor financial returns".', a('https://starofmysore.com/mysuru-kushalnagar-railway-project-scrapped/amp', 'Star of Mysore')),
 ('Koppal', 'PWD Koppal division bills', 'In four months of spending checked, Rs 3.09 crore was paid through 28 fake or duplicate work bills; the auditor said collusion "could not be ruled out". The state says Rs 2.80 crore was recovered.', a(C + '2022/Report-No.-3-of-the-Year-2022-(Karnataka)', 'CAG Report No. 3 of 2022')),
 ('Bidar', 'Mother and child hospital, Bidar', 'Engineers certified a lift, a generator and an operation theatre as done before they were supplied, leading to an "irregular payment" of Rs 97.59 lakh. The state disputed this; the auditor rejected its reply.', a(C + '2021/9.%20Full%20Report-0614b01d87f87e6.86', 'CAG Report No. 3 of 2021')),
 ('Bidar', 'Karanja irrigation project', 'Rs 635 crore spent to irrigate 29,722 hectares; in 2017 the Water Resources Minister said the canals fell short of water.', a('https://daijiworld.com/news/newsDisplay?newsID=433018', 'Daijiworld, 2017')),
]
# Hassan joins the Yettinahole row (its weirs are in Hassan district)
s = s.replace('<tr data-d="Kolar|Chikkaballapura"><td>Kolar, Chikkaballapura</td><td>Yettinahole drinking water</td>',
              '<tr data-d="Kolar|Chikkaballapura|Hassan"><td>Kolar, Chikkaballapura, Hassan</td><td>Yettinahole drinking water</td>', 1)
html = '\n'.join('        <tr data-d="%s"><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % ('|'.join(x.strip() for x in d.split(',')), d, w, t, src) for d, w, t, src in rows)
a0 = s.index('<section class="block" id="districts">')
b0 = s.index('</tbody>', a0)
s = s[:b0] + html + '\n      ' + s[b0:]
io.open(p, 'w', encoding='utf-8').write(s)
print('added', len(rows))
