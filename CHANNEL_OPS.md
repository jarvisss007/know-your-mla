# Gandaberunda channel operations

The channel owner has asked Claude to run the YouTube channel (@GandaberundaKA) and the Know Your MLA site day to day: gather live information, verify it, build videos, upload them, and keep the record current, with the goal of reaching all of Karnataka and then all of India. This file is the standing routine. Every session, scheduled or interactive, follows it.

## Who does what (owner's decision, 15 Nov 2026)

Two Claude sessions work on this project, never on the same files:

- **Video session** (built the talking-format Shorts): owns `video/` (renderers, scenes, voice, songs, `upload_sched.json`), all YouTube uploads, scheduling, music and descriptions.
- **Research and site session**: owns `research/`, `index.html` and `data/`, the right-of-reply process, district and minister research, and constituency report cards. It hands verified facts to the video session as files in `research/` (each with source URL, quote, date) and never uploads to YouTube.

`video/upload_all.json` and `video/upload_manifest.json` are superseded; everything in them is on the channel.

## Daily routine

1. **Sync.** `git pull` this repo. Read `video/SERIES.md`, `video/upload_manifest.json`, and `research/` for open threads.
2. **News sweep (last 24-48 h).** Karnataka: Assembly and Council replies, CAG reports tabled, Lokayukta/ED/CBI actions, court orders involving MLAs or ministers, budget and price changes (milk, bus, fuel, power, property), project deadlines (Yettinahole, metro, suburban rail, Upper Bhadra, Upper Krishna), ADR reports. Prefer primary documents; credible outlets (PTI copy, The Hindu, Deccan Herald, Indian Express, ThePrint, The News Minute, The South First) when they cite official figures.
3. **Verify.** Every new figure is opened at its source and re-checked by a second, independent pass before it is used. Record each in `research/` with URL, quote, date and confidence.
4. **Correct first.** If anything already published is now wrong or outdated (a deadline passed, a case moved, a figure revised), fix the site and the video description the same day, and note it in the site's corrections log.
5. **Build.** Turn the best verified item into an episode (Mallanna Asks, The Ruling Family, district stories), in Kannada and English, with the source on every screen and a fairness beat.
6. **Upload (video session only).** Work through `video/upload_sched.json` in order until YouTube's daily cap stops it. Schedule Kannada at 06:30 Pacific (8 PM India) and English at 07:30 Pacific (9 PM India). Add the channel music track. Mark each entry done in the manifest with its link.
7. **Save.** Commit and push everything (scenes, videos, manifest, research) to this repo. Nothing lives only on one machine.
8. **Report.** A short log entry in `ops/log/YYYY-MM-DD.md`: what was checked, built, uploaded, corrected, and what needs the owner.

## Weekly

- Review views/retention in Studio; double down on formats that hold viewers; retire ones that don't.
- One longer district "report card" when enough districts are verified.
- Check the right-of-reply inbox status with the owner; publish replies in full.

## X (@anupam00720): what the first week showed (checked 18 Nov 2026)

The account has 7 followers. 35 posts from 12 to 18 Nov drew 0 likes, 0 reposts and no replies from anyone else; most got 1 to 3 views (`ops/x_metrics.csv`). The content is not the bottleneck: almost nobody sees it. What did best, on tiny numbers: the CM's own 2013 affidavit debts (10 views), the Know Your MLA launch (9), the post addressed to news agencies (6), two MLAs convicted (5). Abstract budget and audit figures got 1 to 2. The 13 posts sent in 4 minutes on 18 Nov got 1 view each.

Rules from now on:
- **No bursts.** At most 2 posts a day, at least 4 hours apart; a thread counts as one. Never empty a queue at once again; use X's free "Schedule post".
- **A picture with every post.** Attach the matching card from `cards/money/` or `cards/farmers/` (made by `tools/make_money_cards.py`, `tools/make_farmer_cards.py`). The card carries the number, the source and the site address, so it still works if the post is screenshotted.
- **Link in the first reply, not the post.** X shows posts with outside links to fewer people. Post the text and card; reply to it with the link.
- **Lead with a person or a place.** A named public office-holder's own record, or a district people live in, before a state-wide total. Budget totals go in the card's lines, not the opening words.
- **Reach comes from people, not the timeline.** The owner shares each card in WhatsApp groups (Kannada first) and, if the owner chooses, replies with a card under big accounts' posts on the same subject. Claude does not reply, tag or message anyone on X without the owner's say.
- **Measure.** Each week add rows to `ops/x_metrics.csv` (views, likes, reposts, replies from others, 24 hours or more after posting) and keep what works.

## Always ask the owner first

- Any new allegation about a named person, or anything about a private individual or a politician's family member beyond their own public words and roles.
- Right-of-reply letters and any message to an official, journalist or politician (the owner sends them).
- Anything that costs money (ads, promotions, paid tools), account settings, deletions.
- Replying to viewer comments as the channel.

## Never

- State a crime, "black money", or corruption as fact without a court, CAG or Lokayukta finding. Attribute every allegation by name and date.
- Use party colours, symbols or real people's likeness for the fictional characters.
- Use copyrighted music or film clips. Music comes from the YouTube Audio Library only.
- Commit browser profiles, credentials or tokens.

## Reach plan

- Every episode in Kannada and English; Hindi for national stories (e.g. "India's richest Chief Minister").
- Titles: number first, question or contrast, under 100 characters.
- The owner cross-posts each Short to X, Instagram Reels and WhatsApp groups, tagging the responsible minister and both parties.
- A recorded theme song (`video/theme-song.md`) and the owner's own voice-over when available: both raise retention more than anything else.
