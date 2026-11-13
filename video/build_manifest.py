import json, io
SITE = 'https://jarvisss007.github.io/know-your-mla'
TAIL = '\n\nEvery figure comes from a public record. If one is wrong, tell us and we will correct it.\nFictional characters; real records.'
eps = {
 2: ('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #2: ಕಟ್ಟುತ್ತಲೇ ಇದ್ದಾನೆ', 'Mallanna Asks #2: He keeps paying',
     "Milk Rs 39 to Rs 54 (Nov 2022 to Nov 2026; Rs 7 of the latest Rs 8 goes to farmers). Bus fares +15% (Jan 2025) and +23-35% (Nov 2026). State tax on petrol raised by the BJP (2020) and the Congress (2024). Guidance values +25-30% (2023), registration fee 1% to 2% (2025), power +36 paise/unit (KERC, 2025). The state's own tax take: Rs 9,043 crore (2000-01) to Rs 2,20,000 crore (2026-27), in rupees. What came back: govt school enrolment -17 lakh in 15 years, 32,870 health posts vacant, Rs 36,136 crore owed to contractors.",
     'Sources: KMF price orders (DT Next, Outlook, The Week/PTI, The South First); bus fare orders (The Week/PTI, The South First); Business Today; Free Press Journal; The News Minute; Outlook; India TV; KERC order (The Week/PTI); RBI Handbook of State Finances; PRS Karnataka Budget Analysis 2026-27; Assembly replies.'),
 3: ('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #3: ಕಾವೇರಿಯ ಶಾಲೆ', "Mallanna Asks #3: Kaveri's school",
     "45,590 of 1,78,935 primary teacher posts vacant (25.5%, Dec 2025). Computers for teaching: 37.8% of government schools vs 84.3% of private (UDISE+ 2025-26). Government school enrolment down 17 lakh in 15 years. The CM's family trust (National Education Foundation; trustees include D.K. Shivakumar, D.K. Suresh and Aishwarya DKS Hegde) runs private institutions. In Nov 2026 she was reported saying: \"More than teacher shortage, low efficiency is the problem.\" To be fair: 26% of these posts were vacant under the BJP in 2021-22 too. Aishwarya DKS Hegde has not been charged with anything; this video responds only to her public statement.",
     "Sources: School Education Minister's Assembly reply, 18 Dec 2025; UDISE+ via ThePrint; The Week/PTI; gat.ac.in (About NEF); Daily Pioneer, 7 Nov 2026; CAG."),
 4: ('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #4: ಅಮ್ಮನ ಆಸ್ಪತ್ರೆ', "Mallanna Asks #4: Amma's hospital",
     '32,870 of 69,915 Health Department posts vacant (Dec 2024). Health is 4.3% of the 2026-27 budget vs a 6.2% state average. Child anaemia rose in Yadgir (74 to 76%), Kalaburagi (72.4 to 75.1%), Tumakuru (53.8 to 67.6%) between NFHS-4 and NFHS-5. To be fair: infant deaths fell from 23 to 14 per 1,000 (2018-2023).',
     'Sources: Health Department figures (Medical Dialogues); PRS Karnataka Budget Analysis 2026-27; CAG Report No. 10 of 2022; NFHS-5 factsheet; Sample Registration System.'),
 5: ('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #5: ಬಾರದ ನೀರು', 'Mallanna Asks #5: The water that never came',
     'Yettinahole: approved Rs 8,323 crore (2012), now Rs 23,252 crore; Rs 15,297 crore spent by March 2024; CAG: "could not be made operational even after 12 years"; new target end-2027. Mysuru 24x7 water: Rs 271.56 crore spent, no 24x7 water (CAG 2017). Upper Bhadra: Rs 2,813 crore (2003, stage I) to Rs 21,474 crore (2020); Rs 5,300 crore announced in the 2023-24 Union Budget, the Centre says no central scheme covers it, the state says it never came. Every government since 2012 ran Yettinahole.',
     'Sources: CAG Report No. 10 (2026); CAG Report No. 2 of 2017; Lok Sabha reply, Aug 2024; Chief Minister statements, 2026.'),
 6: ('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #6: ಗ್ಯಾರಂಟಿ ಲೆಕ್ಕ', 'Mallanna Asks #6: The guarantee math',
     'Of every Rs 100 the state earns in 2026-27: about Rs 59 goes to salaries, pensions and interest, about Rs 16 to the five guarantees (Rs 51,286 crore), Rs 25 to everything else (our calculation from PRS figures). Gruha Lakshmi alone is Rs 28,608 crore and is real help for many families. Meanwhile fuel tax and the registration fee went up, and the state still plans a revenue deficit of Rs 22,957 crore and borrowing (fiscal deficit) of Rs 97,448 crore.',
     'Sources: PRS Legislative Research, Karnataka Budget Analysis 2026-27; ThePrint; Business Today; Free Press Journal; The South First.'),
 7: ('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #7: ರಾಜುವಿನ ರಸ್ತೆ', "Mallanna Asks #7: Raju's road",
     'Rs 36,136 crore owed to contractors (Finance Department, Sept 2026; the contractors association says Rs 38,000 crore). July 2021, BJP government: the contractors association alleged commissions of up to 40% in a letter to the PMO. March 2025: Justice Nagamohan Das found the 40% claim "not 100 percent true" but found tendering lapses; an SIT was ordered, no result published. 2026, Congress government: the same association alleges commission is now higher; the CM asked them to file an affidavit naming who must be paid. These are allegations: no court or Lokayukta has found any commission rate was paid under either government.',
     'Sources: Finance Department note; ThePrint; The South First; Deccan Chronicle; The Hans India.'),
 8: ('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ #8: ಯಾರೂ ಜೈಲಿಗೆ ಯಾಕೆ ಹೋಗಲ್ಲ?', 'Mallanna Asks #8: Why does nobody go to jail?',
     "195 Lokayukta cases (Sept 2022-Feb 2026), 0 verdicts. The old ACB: 19 convictions from 2,000+ cases. Janardhan Reddy (BJP) convicted May 2025 after about 15 years, conviction suspended in 5 weeks; Satish Sail (Congress) sentenced Oct 2024, suspended within 3 weeks; both still MLAs, appeals pending. But exposure works: in 2011 a sitting CM resigned days after the Lokayukta report (B.S. Yediyurappa, later acquitted or cases quashed). 30% of MLAs skipped the annual asset statement (Nov 2025); the only penalty is publication of names. What you can do: RTI (Rs 10), a Lokayukta complaint (anyone), read your MLA's affidavit (free).",
     'Sources: Assembly records; CBI court and Telangana High Court; Karnataka High Court; Lokayukta; Karnataka Lokayukta Act 1984; Karnataka RTI Rules.'),
}
TAGS = '#MallannaAsks #Karnataka #KnowYourMLA #ಕನ್ನಡ'

def item(e, L, date, time):
    kn, en, body, src = eps[e]
    title = (kn + ' | ' + en.split(': ', 1)[1] + ' #Shorts') if L == 'kn' else (en + ' | Karnataka #Shorts')
    if len(title) > 100:
        title = (kn + ' #Shorts') if L == 'kn' else (en + ' #Shorts')
    assert len(title) <= 100, title
    desc = (('%s\n\n' % kn) if L == 'kn' else '') + body + '\n\nWhat work has your MLA shown you? Tell us in the comments. Look them up: ' + SITE + '\n\n' + src + TAIL + '\n\n' + TAGS
    assert len(desc) <= 4900, (e, L, len(desc))
    return {'file': 'mallanna%d-%s.mp4' % (e, L), 'title': title, 'description': desc, 'date': date, 'time': time}

batch1 = [item(2, 'kn', '16 Nov 2026', '06:30'), item(2, 'en', '16 Nov 2026', '07:30'), item(3, 'kn', '17 Nov 2026', '06:30'),
          item(3, 'en', '17 Nov 2026', '07:30'), item(4, 'kn', '18 Nov 2026', '06:30'), item(5, 'kn', '19 Nov 2026', '06:30')]
batch2 = [item(6, 'kn', '20 Nov 2026', '06:30'), item(6, 'en', '20 Nov 2026', '07:30'), item(7, 'kn', '21 Nov 2026', '06:30'),
          item(7, 'en', '21 Nov 2026', '07:30'), item(8, 'kn', '22 Nov 2026', '06:30'), item(8, 'en', '22 Nov 2026', '07:30')]
json.dump({'batch1': batch1, 'batch2': batch2}, io.open('upload_manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for b in batch1 + batch2:
    print(len(b['title']), len(b['description']), b['file'], b['date'], b['time'])
