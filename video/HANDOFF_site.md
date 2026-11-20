# Handoff from the video session to the research and site session (19 Nov 2026)

The owner asked for the videos, the site and X to be connected, and to know how many people visit the site.
These are the changes that sit in your files. Nothing in `research/`, `index.html`, `reports/` or `tools/` was touched.

## What exists now (video session's files)

- Films page: `video/index.html` -> https://jarvisss007.github.io/know-your-mla/video/ (three embedded films, share buttons, share card `video/films-card.jpg`).
- Three real-photo films, public on YouTube, built only from the Bhuvan completion photos and your published comparison images:
  - Kampli, 152 works, one tank: https://youtube.com/shorts/h2FJqPJlPis
  - Jeerala, six check dams, one bush (94 works): https://youtube.com/shorts/zAYbBqIlVFk
  - Kushtagi, three works, one cement tank, and the Kesur pit: https://youtube.com/shorts/Vmj1X3vx5-Y
- All cartoon Shorts (Mallanna Asks, Katha Studio) were set to Private on the owner's instruction. Public now: the three films above, the MLA pay rise (1,194 views) and Ranebennur (630 views).
- Figures used in the films are the ones on `reports/tank_findings.html`. If the review changes any of them, say so here and the film and description are corrected the same day.

## Asked of the site session

1. **Count visitors: DONE 20 Nov 2026 by the video session, on the owner's go-ahead.** The owner created `gandaberunda.goatcounter.com`. The counter line is now before `</body>` on all 245 served pages (root pages, `mla/`, `reports/`, `video/`) and in three generators (`tools/make_mla_pages.py`, `tools/publish_reports.py`, `tools/make_rti_page.py`) so a rebuild keeps it. If you add a new page or generator, add the same line. Original note follows.
   **Count visitors.** The site has no analytics, so nobody can say how many people visit. GitHub's traffic numbers cover the repository page only (2 visitors in 14 days), not the site. Suggested: GoatCounter (free, no cookies, no consent banner). The owner has to create the account; then one line goes before `</body>` on every page:
   `<script data-goatcounter="https://CODE.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>`
2. **Share previews: DONE 20 Nov 2026 by the video session.** `og:` tags and `twitter:card` are on the 15 report pages, `money.html`, `farmers.html` and `rti.html`, and in `tools/publish_reports.py` (rural jobs pages use `video/films-card.jpg`, the rest the brand banner). `money.html`, `farmers.html` and `rti.html` were patched in place: if a generator rebuilds them, add the same tags there. Original note follows.
   **Share previews on report pages.** `reports/*.html` have no `og:` or `twitter:` tags, so a link pasted into WhatsApp or X shows no picture. In `tools/publish_reports.py`, add to the head: `og:title`, `og:description` (the existing description), `og:image`, `twitter:card=summary_large_image`. For the rural jobs pages `video/films-card.jpg` can serve as the image.
3. **Put the film on the findings page.** Under the headline tiles of `tank_findings.html`:
   `<div style="max-width:340px;aspect-ratio:9/16"><iframe src="https://www.youtube-nocookie.com/embed/h2FJqPJlPis" style="width:100%;height:100%;border:0" loading="lazy" allowfullscreen title="152 works, one tank"></iframe></div>`
4. **Links.** Add "Films" (`video/`) to the header menu, and the YouTube channel (https://www.youtube.com/@GandaberundaKA) and X (https://x.com/anupam00720) to the site-wide footer. Add `video/` to `sitemap.xml`.
5. **Home page.** The six tiles do not include the rural jobs investigation, which is the strongest visual story on the site. Suggested tile: "152 works · One tank".

## Notes on the photos

- Some phone caption strips on the Bhuvan photos carry a person's name ("vivo V20 · MD Basha"). The films crop the bottom of every photo for that reason. Worth checking the compilations on the findings page for the same strip.

## Correction for the findings page (20 Nov 2026)

`reports/tank_findings.html` says 66 Kampli works were "completed" in one 4-hour photo session on 9 Nov 2024, and that the photos were taken between 10:27 and 14:13. In `kampli_tank_152_works.csv`, 66 photos carry that date, but they run from 10:27:32 to 16:17:39:

- 60 between 10:27 and 14:13
- 65 between 10:27 and 14:21 (3 hours 54 minutes)
- the 66th at 16:17 (Ramasagara)

So "66 in a 4-hour session" is one too many. Either "65 in under four hours" or "66 on one day" is correct. The first upload of the Kampli film repeated the 66 figure; it was replaced on 20 Nov with a corrected film (h2FJqPJlPis) that says 65, with a correction note in its description and under the X post. The tile and the caption on the findings page still need the same fix, and an entry in the site's corrections log.
