SRC_ECI = 'Source: Election Commission results, 2013, 2018, 2019 by-election, 2023'
ROW = '<div class="row"><small>{y}</small>{n} <span style="color:#9aa3b2;font-size:48px">· {p}</span></div>'
SCENES = [
 (4.0, '<div class="k">ರಾಣೆಬೆನ್ನೂರು · ಹಾವೇರಿ ಜಿಲ್ಲೆ</div><h1>4 ಚುನಾವಣೆ.<br>4 ಶಾಸಕರು.</h1><div class="en">Ranebennur: four elections since 2013, four different MLAs.</div>', ''),
 (7.0, '<div class="k">ಯಾರು ಗೆದ್ದರು</div>'
       + ROW.format(y='2013', n='K.B. Koliwad', p='ಕಾಂಗ್ರೆಸ್')
       + ROW.format(y='2018', n='R. Shankar', p='ಕೆಪಿಜೆಪಿ')
       + ROW.format(y='2019 · ಉಪಚುನಾವಣೆ', n='Arunkumar Guttur', p='ಬಿಜೆಪಿ')
       + ROW.format(y='2023', n='Prakash Koliwad', p='ಕಾಂಗ್ರೆಸ್'), SRC_ECI),
 (5.0, '<div class="k">2018</div><h2>ಆರ್. ಶಂಕರ್ ಗೆದ್ದರು.<br>ಸಚಿವರಾದರು.</h2><div class="en">2018: R. Shankar wins as his party\'s only MLA and becomes a minister in the coalition government.</div>', ''),
 (6.0, '<div class="k">ಜುಲೈ 2019</div><h1>ಪಕ್ಷಾಂತರ.<br>ಅನರ್ಹತೆ.</h1><div class="mid">ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ಎತ್ತಿಹಿಡಿಯಿತು · ನವೆಂಬರ್ 2019</div><div class="en">He switched his support to the BJP. The Speaker disqualified him under the anti-defection law, and the Supreme Court upheld it.</div>',
       'Source: Supreme Court of India, Shrimanth Balasaheb Patil v. Speaker, 13 November 2019'),
 (5.5, '<div class="k">2018 ರಿಂದ 2023</div><div class="big r">4</div><h2 style="margin-top:20px">ಒಬ್ಬ ನಾಯಕ, ಐದು ವರ್ಷ, ನಾಲ್ಕು ಪಕ್ಷಗಳು.</h2><div class="en">One leader, five years, four parties: KPJP, Congress, BJP, NCP.</div>',
       'Sources: Supreme Court judgment, Nov 2019; news reports, 2019 and 2023'),
 (4.5, '<div class="k">ಡಿಸೆಂಬರ್ 2019</div><h1>ರಾಣೆಬೆನ್ನೂರು ಮತ್ತೆ ಮತ ಹಾಕಬೇಕಾಯಿತು.</h1><div class="en">December 2019: Ranebennur had to vote all over again in a by-election.</div>', SRC_ECI),
 (6.0, '<div class="k">ಈಗಿನ ಶಾಸಕ · 2023</div><h2>Prakash Koliwad · ಕಾಂಗ್ರೆಸ್</h2><div class="row"><small>ವಿಧಾನಸಭೆ ಹಾಜರಾತಿ</small><b>98.2%</b></div><div class="row"><small>ರಾಜ್ಯ ಸರಾಸರಿ</small>79.3%</div><div class="en">Today: Prakash Koliwad (Congress). Assembly attendance 98.2%, against a state average of 79.3%.</div>',
       'Source: PRS Legislative Research, MLA Track, May 2023 to December 2024'),
 (6.5, '<h1>ನಿಮ್ಮ ಮತ ಒಮ್ಮೆ ವ್ಯರ್ಥವಾಯಿತು.</h1><h2 style="margin-top:40px;color:#f2b705">ಮುಂದಿನ ಬಾರಿ, ಮತ ಕೊಡುವ ಮೊದಲು ಪ್ರಶ್ನೆ ಕೇಳಿ.</h2><div class="url">jarvisss007.github.io/know-your-mla</div><div class="en">Your vote was wasted once. Next time, ask your questions before you give it.</div>',
       'Every figure in this video comes from a public record. If one is wrong, tell us and we will correct it.'),
]
OUT = 'ranebennur-kn.mp4'
