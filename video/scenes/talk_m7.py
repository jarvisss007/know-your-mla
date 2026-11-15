# Mallanna Asks, Episode 7: "Raju's road" (ರಾಜುವಿನ ರಸ್ತೆ), talking-character format.
# Converted from scenes/ep7.py; every figure, qualifier and source carried over unchanged from that file and its
# published description. Raju cannot appear on stage, so Mallanna tells his story.
# Legal: these are ALLEGATIONS. Keep "alleged", "not proven", the Nagamohan Das finding, "SIT ordered, no result
# published", and END as the src of the last fact scene.
BPM = 96

BILLS = 'Sources: Karnataka Finance Department note, 17 September 2026; contractors association, 30 September 2026 (ThePrint)'
A21 = 'Source: Karnataka State Contractors Association letter to the PMO, 6 July 2021 (ThePrint)'
ND = 'Source: Justice H.N. Nagamohan Das inquiry report, March 2025 (The South First); cabinet decision, 11 April 2025'
A26 = "Sources: The Hans India, 13 February 2026; ThePrint, 30 September 2026"
END = 'Fictional characters. These are allegations; no court or Lokayukta has found that any commission rate was paid under either government.'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-2 s hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 7 · ರಾಜುವಿನ ರಸ್ತೆ', "Mallanna Asks · Episode 7 · Raju's road"), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="big r">36,136<small> ಕೋಟಿ</small></div><div class="h">ಗುತ್ತಿಗೆದಾರರಿಗೆ ಬಾಕಿ (₹)</div><div class="sub">Finance Department, September 2026. The contractors association says Rs 38,000 crore.</div>',
      card_en='<div class="big r">36,136<small> cr</small></div><div class="h">rupees owed to contractors</div><div class="sub">Finance Department, September 2026. The contractors association says Rs 38,000 crore.</div>',
      lines=[('m', 'ರಾಜು ರಸ್ತೆ ಮುಗಿಸಿ ಎರಡು ವರ್ಷ. ಬಿಲ್ ಇನ್ನೂ ಬಂದಿಲ್ಲ!', 'Raju finished the road two years ago. Still not paid!')], src=BILLS),

 dict(kicker=('ಜುಲೈ 2021 · ಬಿಜೆಪಿ ಸರ್ಕಾರ', 'July 2021 · BJP government'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="big r">40%</div><div class="h">ಗುತ್ತಿಗೆದಾರರ ಸಂಘದ ಆರೋಪ</div><div class="sub">An allegation, in a letter to the Prime Minister\'s Office.</div>',
      card_en='<div class="big r">40%</div><div class="h">the contractors association\'s allegation</div><div class="sub">In a letter to the Prime Minister\'s Office. ಇದು ಆರೋಪ.</div>',
      lines=[('m', 'ಕಮಿಷನ್ ಕಥೆ ಸಾಕು. ದಾಖಲೆ ಏನು ಹೇಳುತ್ತೆ?', 'Enough commission stories. What does the record say?'),
             ('k', '2021ರಲ್ಲಿ ಸಂಘದ ಆರೋಪ: ನಲವತ್ತು ಪರ್ಸೆಂಟ್ ಕಮಿಷನ್.', 'In 2021, contractors alleged commissions of up to 40 percent.')], src=A21),

 dict(kicker=('ಮಾರ್ಚ್ 2025 · ನ್ಯಾಯಾಂಗ ವಿಚಾರಣೆ', 'March 2025 · judicial inquiry'), m_expr='neutral', k_expr='ask',
      card_kn='<div class="h">ನ್ಯಾ. ನಾಗಮೋಹನ್ ದಾಸ್: 40% ಸಾಬೀತಾಗಿಲ್ಲ. ಟೆಂಡರ್‌ನಲ್ಲಿ ಲೋಪಗಳು ಕಂಡುಬಂದಿವೆ.</div><div class="sub">"The allegation of 40 percent commissions is not 100 percent true." SIT ordered April 2025. No result published.</div>',
      card_en='<div class="h">"The allegation of 40 percent commissions is not 100 percent true"</div><div class="sub">Justice Nagamohan Das: 40% not proven, but lapses in tendering found. SIT ordered April 2025. No result published.</div>',
      lines=[('k', 'ವಿಚಾರಣೆ: ನಲವತ್ತು ಪರ್ಸೆಂಟ್ ಸಾಬೀತಾಗಿಲ್ಲ, ಟೆಂಡರ್ ಲೋಪ ಇದೆ.', 'Inquiry: 40 percent not proven, but tendering lapses found.'),
             ('m', 'ಎಸ್‌ಐಟಿ ಆಯ್ತು. ಫಲಿತಾಂಶ ಇನ್ನೂ ಪ್ರಕಟ ಆಗಿಲ್ಲ.', 'An SIT was ordered. No result has been published.')], src=ND),

 dict(kicker=('2026 · ಕಾಂಗ್ರೆಸ್ ಸರ್ಕಾರ', '2026 · Congress government'), m_expr='skeptic', k_expr='ask',
      card_kn='<div class="h">ಅದೇ ಸಂಘದ ಆರೋಪ: "ಈಗ ಕಮಿಷನ್ ಹಿಂದಿಗಿಂತ ಹೆಚ್ಚು."</div><div class="sub">The Chief Minister replied: file an affidavit naming who has to be paid, and he will have it investigated.</div>',
      card_en='<div class="h">The same association alleges: "commission is now higher than before."</div><div class="sub">The Chief Minister replied: file an affidavit naming who has to be paid, and he will have it investigated.</div>',
      lines=[('m', 'ಈಗ ಅದೇ ಸಂಘದ ಆರೋಪ: ಕಮಿಷನ್ ಹಿಂದಿಗಿಂತ ಹೆಚ್ಚು.', 'Now the same group alleges commission is higher than before.'),
             ('k', 'ಸಿಎಂ: ಹೆಸರು ಹಾಕಿ ಅಫಿಡವಿಟ್ ಕೊಡಿ, ತನಿಖೆ ಮಾಡಿಸ್ತೀನಿ.', 'CM: name names in an affidavit, he will have it investigated.')], src=A26),

 # fairness / contrast beat: last fact scene, carries the END disclaimer
 dict(kicker=('ಎರಡೂ ಸರ್ಕಾರ, ಒಂದೇ ಆರೋಪ', 'Both governments, the same charge'), m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>2021 · ಬಿಜೆಪಿ ಸರ್ಕಾರ</small>ಆರೋಪ</div><div class="row"><small>2026 · ಕಾಂಗ್ರೆಸ್ ಸರ್ಕಾರ</small>ಆರೋಪ</div><div class="sub">No court or Lokayukta has found that any commission rate was paid under either government.</div>',
      card_en='<div class="row"><small>2021 · BJP government</small>Allegation</div><div class="row"><small>2026 · Congress government</small>Allegation</div><div class="sub">No court or Lokayukta has found that any commission rate was paid under either government.</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಎರಡೂ ಪಕ್ಷದ ಮೇಲೂ ಒಂದೇ ಆರೋಪ?', 'Dad, the same charge against both parties?'),
             ('m', 'ಪಕ್ಷ ಬದಲಾಯ್ತು, ವ್ಯವಸ್ಥೆ ಬದಲಾಗಿಲ್ಲ ಅಂತ ಆರೋಪ.', 'The charge is: the party changed, the system did not.')], src=END),

 dict(kicker=('ನೀವು ಏನು ಮಾಡಬಹುದು', 'What you can do'), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ಕೇಳಿ: ಪ್ರತಿ ಕಾಮಗಾರಿಯ ಬಿಲ್, ಪಾವತಿ ದಿನಾಂಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಯಾಕೆ ಇಲ್ಲ?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">Ask: why isn\'t every work\'s bill and payment date published online?</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ಕೇಳಿ: ಪ್ರತಿ ಕಾಮಗಾರಿ ಬಿಲ್ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಯಾಕಿಲ್ಲ?', 'Ask: why isn\'t every work\'s bill published online?')], src=END),

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
