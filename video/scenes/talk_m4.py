# Mallanna Asks, Episode 4: "Amma's hospital" (ಅಮ್ಮನ ಆಸ್ಪತ್ರೆ)
# Talking-character version of scenes_mallanna4.py (+ en_wrap4.py). Every figure and source is carried over
# unchanged from that file and the published description in upload_all.json. Nothing new added.
# Amma does not appear on stage; Mallanna speaks about her.
BPM = 96

VAC = "Source: Karnataka Health Department figures, December 2024 (reported by Medical Dialogues)"
PRS = 'Source: PRS Legislative Research, Karnataka Budget Analysis 2026-27'
NFHS = 'Sources: CAG Report No. 10 of 2022 (NFHS figures); NFHS-5 district factsheet, Tumakuru'
SRS = 'Source: Sample Registration System bulletins, 2018 and 2023'
ASK = 'Fictional characters. Every figure comes from a public record. If one is wrong, tell us and we will correct it.'

SCENES = [
 # 0-3 s hook
 dict(kicker=('ಮಲ್ಲಣ್ಣ ಕೇಳ್ತಾನೆ · ಸಂಚಿಕೆ 4 · ಅಮ್ಮನ ಆಸ್ಪತ್ರೆ', "Mallanna Asks · Episode 4 · Amma's hospital"),
      hit=True, m_expr='skeptic', k_expr='sad',
      card_kn='<div class="big r">47%</div><div class="h">ಆರೋಗ್ಯ ಇಲಾಖೆ ಹುದ್ದೆಗಳು ಖಾಲಿ</div><div class="sub">69,915ರಲ್ಲಿ 32,870 · ಡಿಸೆಂಬರ್ 2024</div>',
      card_en='<div class="big r">47%</div><div class="h">of Health Department posts are vacant</div><div class="sub">32,870 of 69,915 · December 2024</div>',
      lines=[('m', 'ಆಸ್ಪತ್ರೆ ಕಟ್ಟಡ ಇದೆ ಸ್ವಾಮಿ. ಡಾಕ್ಟರ್ ಇಲ್ಲ.', 'The hospital building is there, sir. The doctor is not.')], src=VAC),

 dict(kicker=('ಅಮ್ಮನ ಶುಗರ್ ಚೆಕ್‌ಅಪ್', "Amma's sugar check-up"), m_expr='neutral', k_expr='ask',
      card_kn='<div class="row"><small>ಖಾಲಿ ಹುದ್ದೆಗಳು</small><b class="r">32,870</b></div><div class="row"><small>ಒಟ್ಟು ಹುದ್ದೆಗಳು</small>69,915</div>',
      card_en='<div class="row"><small>Posts vacant</small><b class="r">32,870</b></div><div class="row"><small>Total posts</small>69,915</div>',
      lines=[('m', 'ಅಮ್ಮನ ಶುಗರ್ ಚೆಕ್‌ಅಪ್‌ಗೆ ಇದು ಮೂರನೇ ಸಲ.', "This is our third trip for Amma's sugar check-up."),
             ('k', 'ನೂರು ಜನ ಬೇಕಾದಲ್ಲಿ 47 ಜನ ಇಲ್ಲ. ಕೆಲಸ ಯಾರು ಮಾಡ್ತಾರೆ?', 'If 47 of every 100 are missing, who does the work?')], src=VAC),

 dict(kicker=('ಬಜೆಟ್‌ನಲ್ಲಿ ಆರೋಗ್ಯದ ಪಾಲು · 2026-27', "Health's share of the budget · 2026-27"), hit=True, m_expr='skeptic', k_expr='ask',
      card_kn='<div class="row"><small>ಕರ್ನಾಟಕ</small><b class="r">4.3%</b></div><div class="row"><small>ಎಲ್ಲ ರಾಜ್ಯಗಳ ಸರಾಸರಿ</small>6.2%</div>',
      card_en='<div class="row"><small>Karnataka</small><b class="r">4.3%</b></div><div class="row"><small>Average of all states</small>6.2%</div>',
      lines=[('m', 'ಬೇರೆ ರಾಜ್ಯಗಳಿಗಿಂತ ನಾವು ಆರೋಗ್ಯಕ್ಕೆ ಕಡಿಮೆ ಖರ್ಚು ಮಾಡ್ತೀವಿ.', 'We spend less of our budget on health than the average state.')], src=PRS),

 dict(kicker=('ಮಕ್ಕಳ ರಕ್ತಹೀನತೆ (6-59 ತಿಂಗಳು) · 2015-16 → 2019-21', 'Children with anaemia (6-59 months) · 2015-16 → 2019-21'), hit=True, m_expr='firm', k_expr='sad',
      card_kn='<div class="row"><small>ಯಾದಗಿರಿ</small>74% → <b class="r">76%</b></div><div class="row"><small>ಕಲಬುರಗಿ</small>72.4% → <b class="r">75.1%</b></div><div class="row"><small>ತುಮಕೂರು</small>53.8% → <b class="r">67.6%</b></div>',
      card_en='<div class="row"><small>Yadgir</small>74% → <b class="r">76%</b></div><div class="row"><small>Kalaburagi</small>72.4% → <b class="r">75.1%</b></div><div class="row"><small>Tumakuru</small>53.8% → <b class="r">67.6%</b></div>',
      lines=[('k', 'ಈ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ರಕ್ತಹೀನತೆ ಇರುವ ಮಕ್ಕಳು ಹೆಚ್ಚಾಗಿದ್ದಾರೆ.', 'In these districts, more children have anaemia now.')], src=NFHS),

 # fairness
 dict(kicker=('ನ್ಯಾಯವಾಗಿ ಹೇಳಬೇಕೆಂದರೆ', 'To be fair'), hit=True, m_expr='smile', k_expr='smile',
      card_kn='<div class="row"><small>ಶಿಶು ಮರಣ ದರ, 1,000 ಜನನಕ್ಕೆ · 2018 → 2023</small>23 → <b>14</b></div><div class="sub">ರಾಷ್ಟ್ರೀಯ ದರ 25ಕ್ಕಿಂತ ಕಡಿಮೆ.</div>',
      card_en='<div class="row"><small>Infant deaths per 1,000 births · 2018 → 2023</small>23 → <b>14</b></div><div class="sub">Below the national 25.</div>',
      lines=[('m', 'ಶಿಶು ಮರಣ ಇಳಿದಿದೆ. ಎಲ್ಲಾ ಹುದ್ದೆ ತುಂಬಿದ್ರೆ ಹೇಗಿರುತ್ತೆ ಯೋಚಿಸಿ.', 'Infant deaths fell. Imagine it with every post filled.')], src=SRS),

 dict(kicker=('ಕಾವೇರಿಯ ಪ್ರಶ್ನೆ', "Kaveri's question"), m_expr='firm', k_expr='ask',
      card_kn='<div class="h">ನಮ್ಮ ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ಎಷ್ಟು ಹುದ್ದೆ ಖಾಲಿ?</div><div class="sub">ನಿಮ್ಮ ಶಾಸಕರನ್ನು ಕೇಳಿ. ಅವರನ್ನು ಇಲ್ಲಿ ನೋಡಿ:</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      card_en='<div class="h">How many posts are empty at our hospital?</div><div class="sub">Ask your MLA. Look them up:</div><div class="url">jarvisss007.github.io/know-your-mla</div>',
      lines=[('m', 'ರಿಬ್ಬನ್ ಕತ್ತರಿಸೋಕೆ ಬರ್ತೀರಾ. ಡಾಕ್ಟರ್ ನೇಮಕಕ್ಕೆ?', 'You come to cut the ribbon. And to appoint the doctors?'),
             ('k', 'ನಮ್ಮ ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ಎಷ್ಟು ಹುದ್ದೆ ಖಾಲಿ?', 'How many posts are empty at our hospital?')], src=ASK),

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
