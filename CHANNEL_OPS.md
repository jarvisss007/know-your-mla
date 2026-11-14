# Gandaberunda channel operations

The channel owner has asked Claude to run the YouTube channel (@GandaberundaKA) and the Know Your MLA site day to day: gather live information, verify it, build videos, upload them, and keep the record current, with the goal of reaching all of Karnataka and then all of India. This file is the standing routine. Every session, scheduled or interactive, follows it.

## Daily routine

1. **Sync.** `git pull` this repo. Read `video/SERIES.md`, `video/upload_manifest.json`, and `research/` for open threads.
2. **News sweep (last 24-48 h).** Karnataka: Assembly and Council replies, CAG reports tabled, Lokayukta/ED/CBI actions, court orders involving MLAs or ministers, budget and price changes (milk, bus, fuel, power, property), project deadlines (Yettinahole, metro, suburban rail, Upper Bhadra, Upper Krishna), ADR reports. Prefer primary documents; credible outlets (PTI copy, The Hindu, Deccan Herald, Indian Express, ThePrint, The News Minute, The South First) when they cite official figures.
3. **Verify.** Every new figure is opened at its source and re-checked by a second, independent pass before it is used. Record each in `research/` with URL, quote, date and confidence.
4. **Correct first.** If anything already published is now wrong or outdated (a deadline passed, a case moved, a figure revised), fix the site and the video description the same day, and note it in the site's corrections log.
5. **Build.** Turn the best verified item into an episode (Mallanna Asks, The Ruling Family, district stories), in Kannada and English, with the source on every screen and a fairness beat.
6. **Upload.** Work through `video/upload_manifest.json` in order until YouTube's daily cap stops it. Schedule Kannada at 06:30 Pacific (8 PM India) and English at 07:30 Pacific (9 PM India). Add the channel music track. Mark each entry done in the manifest with its link.
7. **Save.** Commit and push everything (scenes, videos, manifest, research) to this repo. Nothing lives only on one machine.
8. **Report.** A short log entry in `ops/log/YYYY-MM-DD.md`: what was checked, built, uploaded, corrected, and what needs the owner.

## Weekly

- Review views/retention in Studio; double down on formats that hold viewers; retire ones that don't.
- One longer district "report card" when enough districts are verified.
- Check the right-of-reply inbox status with the owner; publish replies in full.

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
