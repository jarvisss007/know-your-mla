# Handoff from the video session to the research and site session (19 Nov 2026)

The owner asked for the videos, the site and X to be connected, and to know how many people visit the site.
These are the changes that sit in your files. Nothing in `research/`, `index.html`, `reports/` or `tools/` was touched.

## What exists now (video session's files)

- Films page: `video/index.html` -> https://jarvisss007.github.io/know-your-mla/video/ (three embedded films, share buttons, share card `video/films-card.jpg`).
- Three real-photo films, public on YouTube, built only from the Bhuvan completion photos and your published comparison images:
  - Kampli, 152 works, one tank: https://youtube.com/shorts/a91dEUEKgO8
  - Jeerala, six check dams, one bush (94 works): https://youtube.com/shorts/zAYbBqIlVFk
  - Kushtagi, three works, one cement tank, and the Kesur pit: https://youtube.com/shorts/Vmj1X3vx5-Y
- All cartoon Shorts (Mallanna Asks, Katha Studio) were set to Private on the owner's instruction. Public now: the three films above, the MLA pay rise (1,194 views) and Ranebennur (630 views).
- Figures used in the films are the ones on `reports/tank_findings.html`. If the review changes any of them, say so here and the film and description are corrected the same day.

## Asked of the site session

1. **Count visitors.** The site has no analytics, so nobody can say how many people visit. GitHub's traffic numbers cover the repository page only (2 visitors in 14 days), not the site. Suggested: GoatCounter (free, no cookies, no consent banner). The owner has to create the account; then one line goes before `</body>` on every page:
   `<script data-goatcounter="https://CODE.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>`
2. **Share previews on report pages.** `reports/*.html` have no `og:` or `twitter:` tags, so a link pasted into WhatsApp or X shows no picture. In `tools/publish_reports.py`, add to the head: `og:title`, `og:description` (the existing description), `og:image`, `twitter:card=summary_large_image`. For the rural jobs pages `video/films-card.jpg` can serve as the image.
3. **Put the film on the findings page.** Under the headline tiles of `tank_findings.html`:
   `<div style="max-width:340px;aspect-ratio:9/16"><iframe src="https://www.youtube-nocookie.com/embed/a91dEUEKgO8" style="width:100%;height:100%;border:0" loading="lazy" allowfullscreen title="152 works, one tank"></iframe></div>`
4. **Links.** Add "Films" (`video/`) to the header menu, and the YouTube channel (https://www.youtube.com/@GandaberundaKA) and X (https://x.com/anupam00720) to the site-wide footer. Add `video/` to `sitemap.xml`.
5. **Home page.** The six tiles do not include the rural jobs investigation, which is the strongest visual story on the site. Suggested tile: "152 works · One tank".

## Notes on the photos

- Some phone caption strips on the Bhuvan photos carry a person's name ("vivo V20 · MD Basha"). The films crop the bottom of every photo for that reason. Worth checking the compilations on the findings page for the same strip.
