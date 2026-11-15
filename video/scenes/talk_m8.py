# Mallanna Asks, Episode 8: "Why does nobody go to jail?" (ಯಾರೂ ಜೈಲಿಗೆ ಯಾಕೆ ಹೋಗಲ್ಲ?), talking-character format.
# Converted from scenes/ep8.py; every figure and source carried over unchanged from that file and its published description.
# Legal: convictions are described as suspended pending appeal; Yediyurappa's acquittals/quashed cases shown as such.
BPM = 96

LOK = "Sources: Chief Minister's reply in the Assembly (Sept 2022 to Feb 2026); Assembly records on the ACB, 2016-2022"
CONV = 'Sources: CBI special court, 6 May 2025, and Telangana High Court, 11 June 2025 (Reddy); special court, 26 October 2024, and Karnataka High Court, 13 November 2024 (Sail)'
BSY = 'Sources: Lokayukta report, July 2011; resignation, 31 July 2011; CBI court, 2016; Supreme Court, December 2018'
ASSET = 'Source: Karnataka Lokayukta, November 2025 (asset-statement defaulters among legislators)'
DO = 'Sources: Karnataka Lokayukta Act, 1984; Karnataka RTI Rules (Rs 10 application fee)'
END = 'Fictional characters. Convictions named here are suspended pending appeal; cases closed in favour of the accused are shown as such.'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-2 s hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 8 · ಯಾರೂ ಜೈಲಿಗೆ ಯಾಕೆ ಹೋಗಲ್ಲ?', 'Mallanna Asks · Episode 8 · Why does nobody go to jail?'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="big r">0<small> / 195</small></div><div class="h">ಲೋಕಾಯುಕ್ತ ದಾಳಿ, ಟ್ರ್ಯಾಪ್ ಪ್ರಕರಣಗಳಲ್ಲಿ ತೀರ್ಪು</div><div class="sub">Sept 2022 to Feb 2026</div>',
      card_en='<div class="big r">0<small> / 195</small></div><div class="h">verdicts in Lokayukta raid and trap cases</div><div class="sub">Sept 2022 to Feb 2026</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಇಷ್ಟು ಆರೋಪ ಇದ್ರೂ ಯಾರೂ ಜೈಲಿಗೆ ಯಾಕೆ ಹೋಗಲ್ಲ?', 'Dad, with so many charges, why does nobody go to jail?')], src=LOK),

 dict(kicker=('ಲೋಕಾಯುಕ್ತ · ಸೆಪ್ಟೆಂಬರ್ 2022 ರಿಂದ ಫೆಬ್ರವರಿ 2026', 'Lokayukta · Sept 2022 to Feb 2026'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="row"><small>ದಾಳಿ, ಟ್ರ್ಯಾಪ್ ಪ್ರಕರಣಗಳು</small>195</div><div class="row"><small>ತೀರ್ಪುಗಳು</small><b class="r">0</b></div><div class="row"><small>ಹಳೆಯ ಎಸಿಬಿ: 2,000+ ಪ್ರಕರಣಗಳಲ್ಲಿ ಶಿಕ್ಷೆ</small><b class="r">19</b></div>',
      card_en='<div class="row"><small>Raid and trap cases</small>195</div><div class="row"><small>Verdicts</small><b class="r">0</b></div><div class="row"><small>Old ACB: convictions from 2,000+ cases</small><b class="r">19</b></div>',
      lines=[('m', 'ಹಳೆ ಎಸಿಬಿ: ಎರಡು ಸಾವಿರಕ್ಕೂ ಹೆಚ್ಚು ಪ್ರಕರಣ, ಹತ್ತೊಂಬತ್ತೇ ಶಿಕ್ಷೆ.', 'The old ACB: over 2,000 cases, just 19 convictions.')], src=LOK),

 # fairness: one from each party
 dict(kicker=('ಶಿಕ್ಷೆ ಆದರೂ...', 'Even after a conviction'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಜನಾರ್ದನ ರೆಡ್ಡಿ (ಬಿಜೆಪಿ) · ಶಿಕ್ಷೆ ಮೇ 2025</small>5 ವಾರದಲ್ಲಿ ತಡೆ</div><div class="row"><small>ಸತೀಶ್ ಸೈಲ್ (ಕಾಂಗ್ರೆಸ್) · ಶಿಕ್ಷೆ ಅಕ್ಟೋಬರ್ 2024</small>3 ವಾರದಲ್ಲಿ ತಡೆ</div><div class="sub">Both convictions suspended pending appeal. Both are still MLAs.</div>',
      card_en='<div class="row"><small>Janardhan Reddy (BJP) · convicted May 2025</small>Suspended, 5 wks</div><div class="row"><small>Satish Sail (Congress) · sentenced Oct 2024</small>Suspended, 3 wks</div><div class="sub">Both suspended pending appeal. Both are still MLAs.</div>',
      lines=[('k', 'ಶಿಕ್ಷೆ ಆದರೂ ವಾರಗಳಲ್ಲೇ ತಡೆ. ಇಬ್ಬರೂ ಇನ್ನೂ ಶಾಸಕರು!', 'Convicted, then suspended within weeks. Both are still MLAs!'),
             ('m', 'ಮೇಲ್ಮನವಿ ಬಾಕಿ ಇದೆ. ರೆಡ್ಡಿ ಕೇಸ್‌ಗೆ ಸುಮಾರು ಹದಿನೈದು ವರ್ಷ ಹಿಡೀತು.', "Their appeals are pending. Reddy's case took about 15 years.")], src=CONV),

 dict(kicker=('ಆದರೆ ಬಯಲು ಮಾಡುವುದು ಕೆಲಸ ಮಾಡುತ್ತದೆ', 'But exposure works'), m_expr='smile', k_expr='ask',
      card_kn='<div class="h">2011: ಲೋಕಾಯುಕ್ತ ವರದಿ ಬಂದ ಕೆಲವೇ ದಿನಗಳಲ್ಲಿ ಮುಖ್ಯಮಂತ್ರಿ ರಾಜೀನಾಮೆ.</div><div class="sub">B.S. Yediyurappa was later acquitted or had those cases quashed. But he lost the chair.</div>',
      card_en='<div class="h">2011: within days of the Lokayukta\'s mining report, a sitting Chief Minister resigned.</div><div class="sub">B.S. Yediyurappa was later acquitted or had those cases quashed. But he lost the chair.</div>',
      lines=[('m', 'ಆದರೆ ಬಯಲು ಮಾಡಿದ್ರೆ ಕೆಲಸ ಆಗುತ್ತೆ. 2011ರಲ್ಲಿ ಸಿಎಂ ರಾಜೀನಾಮೆ ಕೊಟ್ರು.', 'But exposure works. In 2011 a sitting CM resigned.'),
             ('k', 'ಆಮೇಲೆ ಖುಲಾಸೆ ಆದ್ರು, ಇಲ್ಲ ಕೇಸ್ ರದ್ದಾಯ್ತು. ಆದ್ರೆ ಕುರ್ಚಿ ಹೋಯ್ತು!', 'Later acquitted, or the cases quashed. But he lost the chair!')], src=BSY),

 dict(kicker=('ಪ್ರತಿ ವರ್ಷ ಆಸ್ತಿ ಘೋಷಣೆ ಕಡ್ಡಾಯ', 'Annual asset statements are compulsory'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">30%</div><div class="h">ಶಾಸಕರು ಸಲ್ಲಿಸಲಿಲ್ಲ (ನವೆಂಬರ್ 2025)</div><div class="sub">The penalty? Their names are published in the newspaper. That is all.</div>',
      card_en='<div class="big r">30%</div><div class="h">of MLAs did not file (November 2025)</div><div class="sub">ಶಿಕ್ಷೆ? ಪತ್ರಿಕೆಯಲ್ಲಿ ಹೆಸರು ಪ್ರಕಟ. ಅಷ್ಟೇ.</div>',
      lines=[('k', 'ಮೂವತ್ತು ಪರ್ಸೆಂಟ್ ಶಾಸಕರು ಆಸ್ತಿ ಘೋಷಣೆ ಸಲ್ಲಿಸಲಿಲ್ಲ!', '30 percent of MLAs did not file their asset statement!'),
             ('m', 'ಶಿಕ್ಷೆ? ಪತ್ರಿಕೆಯಲ್ಲಿ ಹೆಸರು. ಅಷ್ಟೇ.', 'The penalty? Their names in the paper. That is all.')], src=ASSET),

 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ಕೇಳಿ: ನಮ್ಮ ಶಾಸಕರು ಈ ವರ್ಷ ಆಸ್ತಿ ಘೋಷಣೆ ಸಲ್ಲಿಸಿದ್ದಾರಾ?</div><div class="sub">RTI: Rs 10 · Lokayukta complaint: anyone can file · Your MLA\'s affidavit: free to read</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Ask: did our MLA file this year\'s asset statement?</div><div class="sub">RTI: Rs 10 · Lokayukta complaint: anyone can file · Your MLA\'s affidavit: free to read</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಕೋರ್ಟ್ ತಡ ಮಾಡಬಹುದು. ಮತ ತಡ ಮಾಡಲ್ಲ.', 'The court can be slow. The vote is not.')], src=DO + '. ' + END),

 # chorus: the series theme, chanted on the beat
 dict(kicker=('ಮಲ್ಲಣ್ಣನ ಹಾಡು', "Mallanna's song"), chorus={
          'kn': ('ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!<br>ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!', 'Show us the work, sir! First the account, then our vote!'),
          'en': ('Show us the work, sir, show us the work!<br>First the account, then our vote!', 'ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!')},
      chant={'kn': ['ಕೆಲಸ ತೋರಿಸಿ ಸ್ವಾಮಿ, ಕೆಲಸ ತೋರಿಸಿ!', 'ಆಮೇಲೆ ಮತ, ಮೊದಲು ಲೆಕ್ಕ ಕೊಡಿ!'],
             'en': ['Show us the work, sir, show us the work!', 'First the account, then our vote!']},
      reps=1, m_expr='firm', k_expr='ask', hit=True, card_kn='', card_en='', lines=[], src=ASK, tail=1.2),
]

# The owner's recorded chorus on every Kannada episode.
REC = {'kn': {'chorus': 'voice/ep11/chorus.wav'}}
