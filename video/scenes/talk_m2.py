# Mallanna Asks, Episode 2: "He keeps paying" (ಕಟ್ಟುತ್ತಲೇ ಇದ್ದಾನೆ)
# Talking-character version of ep2.py. Every figure and source is carried over unchanged from that file and the
# published description in upload_all.json. Nothing new added.
BPM = 96

MILK = 'Sources: KMF price orders reported by DT Next (Nov 2022), Outlook (Aug 2023), The Week/PTI (Jun 2024, Mar 2025), The South First (Nov 2026)'
BUS = 'Sources: The Week/PTI, 2 January 2025; The South First, November 2026'
FUEL = 'Sources: Business Today, 15 June 2024; Free Press Journal, April 2025; The News Minute, March 2020; Outlook, 4 November 2021'
HOME = 'Sources: India TV, September 2023; The South First, August 2025; The Week/PTI (KERC order), 20 March 2025'
TAX = "Sources: RBI Handbook of Statistics on State Government Finances (2000-01); PRS Karnataka Budget Analysis 2026-27"
BACK = 'Sources: School Education Minister in the Assembly, December 2025 (The Week/PTI); Health Department, December 2024; Finance Department note, September 2026'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-3 s hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 2 · ಕಟ್ಟುತ್ತಲೇ ಇದ್ದಾನೆ', 'Mallanna Asks · Episode 2 · He keeps paying'),
      hit=True, m_expr='skeptic', k_expr='sad',
      card_kn='<div class="h">ನಂದಿನಿ ಟೋನ್ಡ್ ಹಾಲು, ಲೀಟರ್‌ಗೆ</div><div class="row"><small>ನವೆಂಬರ್ 2022 · ಬಿಜೆಪಿ ಸರ್ಕಾರ</small>₹39</div><div class="row"><small>ನವೆಂಬರ್ 2026 · ಕಾಂಗ್ರೆಸ್ ಸರ್ಕಾರ</small><b class="r">₹54</b></div><div class="sub">ನ್ಯಾಯವಾಗಿ: ಕೊನೆಯ ₹8 ಏರಿಕೆಯಲ್ಲಿ ₹7 ರೈತರಿಗೆ.</div>',
      card_en='<div class="h">Nandini toned milk, per litre</div><div class="row"><small>Nov 2022 · BJP government</small>Rs 39</div><div class="row"><small>Nov 2026 · Congress government</small><b class="r">Rs 54</b></div><div class="sub">To be fair: Rs 7 of the latest Rs 8 rise goes to dairy farmers.</div>',
      lines=[('m', 'ಫ್ರೀ ಮುಂದಿನ ಬಾಗಿಲಿಂದ ಬಂತು. ಬಿಲ್ ಹಿಂದಿನ ಬಾಗಿಲಿಂದ.', 'Free came through the front door. The bill came through the back.')], src=MILK),

 dict(kicker=('ಬಸ್ ದರ', 'Bus fares'), hit=True, m_expr='neutral', k_expr='ask',
      card_kn='<div class="row"><small>ಜನವರಿ 2025</small><b class="r">+15%</b></div><div class="row"><small>ನವೆಂಬರ್ 2026 · KSRTC / BMTC</small><b class="r">+23 to 35%</b></div><div class="sub">ಬಿಎಂಟಿಸಿ ಕನಿಷ್ಠ ದರ ₹6 ರಿಂದ ₹10.</div>',
      card_en='<div class="row"><small>January 2025</small><b class="r">+15%</b></div><div class="row"><small>November 2026 · KSRTC / BMTC</small><b class="r">+23 to 35%</b></div><div class="sub">BMTC minimum fare: Rs 6 to Rs 10.</div>',
      lines=[('k', 'ಅಪ್ಪಾ, ಬಸ್ ಟಿಕೆಟ್ ಮತ್ತೆ ಏರಿತು!', 'Dad, the bus ticket went up again!')], src=BUS),

 # fairness: both parties raised it
 dict(kicker=('ಪೆಟ್ರೋಲ್ ಮೇಲಿನ ರಾಜ್ಯ ತೆರಿಗೆ', 'State tax on petrol'), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>ಏಪ್ರಿಲ್ 2020 · ಬಿಜೆಪಿ</small>32% → <b class="r">35%</b></div><div class="row"><small>ಜೂನ್ 2024 · ಕಾಂಗ್ರೆಸ್</small>25.92% → <b class="r">29.84%</b></div><div class="sub">ನವೆಂಬರ್ 2021ರಲ್ಲಿ ಬಿಜೆಪಿ ಲೀಟರ್‌ಗೆ ₹7 ಇಳಿಸಿತ್ತು. ಏಪ್ರಿಲ್ 2025ರಲ್ಲಿ ಡೀಸೆಲ್ ತೆರಿಗೆ ಮತ್ತೆ ಏರಿತು.</div>',
      card_en='<div class="row"><small>April 2020 · BJP</small>32% → <b class="r">35%</b></div><div class="row"><small>June 2024 · Congress</small>25.92% → <b class="r">29.84%</b></div><div class="sub">The BJP also cut fuel by Rs 7 a litre in Nov 2021. Diesel tax went up again in April 2025.</div>',
      lines=[('m', 'ಪೆಟ್ರೋಲ್ ತೆರಿಗೆ ಎರಡೂ ಪಕ್ಷಗಳು ಏರಿಸಿವೆ.', 'Both parties raised the tax on petrol.')], src=FUEL),

 dict(kicker=('ಮನೆ, ಜಮೀನು, ಕರೆಂಟ್', 'Your home, your land, your power bill'), hit=True, m_expr='skeptic', k_expr='sad',
      card_kn='<div class="row"><small>ಮಾರ್ಗಸೂಚಿ ಮೌಲ್ಯ · ಅಕ್ಟೋಬರ್ 2023</small><b>+25 to 30%</b></div><div class="row"><small>ನೋಂದಣಿ ಶುಲ್ಕ · ಆಗಸ್ಟ್ 2025</small>1% → <b class="r">2%</b></div><div class="row"><small>ಪ್ರತಿ ಯೂನಿಟ್ ಕರೆಂಟ್ · ಏಪ್ರಿಲ್ 2025 (KERC)</small><b>+36 paise</b></div>',
      card_en='<div class="row"><small>Guidance values · Oct 2023</small><b>+25 to 30%</b></div><div class="row"><small>Registration fee · Aug 2025</small>1% → <b class="r">2%</b></div><div class="row"><small>Per unit of power · Apr 2025 (KERC order)</small><b>+36 paise</b></div>',
      lines=[('k', 'ಮನೆ, ಜಮೀನು, ಕರೆಂಟ್, ಎಲ್ಲದರ ಬಿಲ್ ಏರಿತು.', 'Home, land, power: every bill went up.')], src=HOME),

 dict(kicker=('ರಾಜ್ಯ ಸಂಗ್ರಹಿಸುವ ಸ್ವಂತ ತೆರಿಗೆ, ವರ್ಷಕ್ಕೆ', "The state's own tax collection, per year"), hit=True, m_expr='firm', k_expr='ask',
      card_kn='<div class="row"><small>2000-01</small>₹9,043 ಕೋಟಿ</div><div class="row"><small>2026-27</small><b>₹2,20,000 ಕೋಟಿ</b></div><div class="sub">ರೂಪಾಯಿಯಲ್ಲಿ 24 ಪಟ್ಟು (ಹಣದುಬ್ಬರ ಸೇರಿಸಿಲ್ಲ).</div>',
      card_en='<div class="row"><small>2000-01</small>Rs 9,043 cr</div><div class="row"><small>2026-27</small><b>Rs 2,20,000 cr</b></div><div class="sub">24 times more in rupees (not adjusted for inflation).</div>',
      lines=[('m', 'ನಾವು ಕೊಳ್ಳೋ, ಓಡಿಸೋ, ನೋಂದಾಯಿಸೋ ಎಲ್ಲದರಿಂದ ತೆರಿಗೆ.', 'Tax on everything we buy, drive and register.')], src=TAX),

 dict(kicker=('ವಾಪಸ್ ಏನು ಬಂತು?', 'What came back?'), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಸರ್ಕಾರಿ ಶಾಲೆ ದಾಖಲಾತಿ, 15 ವರ್ಷದಲ್ಲಿ</small><b class="r">−17 ಲಕ್ಷ</b></div><div class="row"><small>ಖಾಲಿ ಆರೋಗ್ಯ ಹುದ್ದೆಗಳು</small><b class="r">32,870</b></div><div class="row"><small>ಗುತ್ತಿಗೆದಾರರಿಗೆ ಬಾಕಿ</small><b class="r">₹36,136 ಕೋಟಿ</b></div>',
      card_en='<div class="row"><small>Government school enrolment, last 15 years</small><b class="r">−17 lakh</b></div><div class="row"><small>Health posts vacant</small><b class="r">32,870</b></div><div class="row"><small>Owed to contractors</small><b class="r">Rs 36,136 cr</b></div>',
      lines=[('k', 'ಕಟ್ಟೋದು ನಾವು. ವಾಪಸ್ ಏನು ಬಂತು?', 'We pay. What came back?')], src=BACK),

 dict(kicker=('ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ', "Kaveri's question"), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ನಾವು ಕಟ್ಟಿದ ತೆರಿಗೆಯಲ್ಲಿ ನಮ್ಮ ಊರಿಗೆ ಎಷ್ಟು ಬಂತು?</div><div class="sub">ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ. ಅವರನ್ನು ಇಲ್ಲಿ ನೋಡಿ:</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">How much of our tax came back to our town?</div><div class="sub">Ask your MLA. Look them up:</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('k', 'ನಾವು ಕಟ್ಟಿದ ತೆರಿಗೆಯಲ್ಲಿ ನಮ್ಮ ಊರಿಗೆ ಎಷ್ಟು ಬಂತು?', 'How much of our tax came back to our town?')], src=ASK),

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
