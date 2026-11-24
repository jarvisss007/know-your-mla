# DRAFT: did the party-tiered grants win votes? (25 Nov 2026)

Companion to BJP_ERA_GRANTS_DRAFT.md and CM_GRANTS_BY_SEAT_DRAFT.md. Analysis, not a record: our arithmetic on official results.

## Data
- Grants: Assembly USQ 114 (15 Feb 2022): Rs 52 crore special grant to 63 BJP-held seats (and one government-backing independent). Party on 15 Feb 2022 rebuilt from the 2018 results and every change (seats_party_15feb2022.csv).
- Results: 2018 and 2023 Assembly results per constituency (Wikipedia election tables citing ECI; seat totals match official counts). Independent re-check of 2023 winners against our MLA list (data/mlas.csv, by-election seats reset to their 2023 winner): same result.

## Result: the Rs 52 crore seats did worse, not better
Among the 121 seats the BJP held on 15 Feb 2022:

| | Got Rs 52 crore (63) | Did not (58) |
|---|---|---|
| BJP won again in 2023 | 17 (27%) | 34 (59%) |
| BJP vote share, 2023 minus 2018 | -6.1 points | +1.0 points |
| BJP's 2018 winning margin (median) | 8.5 points | 8.9 points |

- The two groups were equally safe in 2018, yet the funded seats lost far more often. The gap holds within every 2018-margin band (e.g. margin under 5 points: 0 of 12 funded seats held, 3 of 6 unfunded).
- Holding 2018 margin and region constant, being on the list goes with about 25 points lower chance of the BJP winning in 2023 (95% range 7 to 44 points; p = 0.005), and 4.2 points lower vote share (p = 0.013).
- It survives dropping Bengaluru city (no seat there was listed), flagging seats won by defection or by-election, and keeping only seats where the sitting MLA stood again (11 of 41 funded seats held vs 23 of 39 unfunded).
- Independent re-check with our MLA list: 15 of 53 funded vs 30 of 51 unfunded (17 seats not matched by name).

## The 2024 by-elections (Congress government; CM special grant)
- Channapatna (Rs 150 crore): JD(S) had won in 2023 by 15,915 votes; Congress won in Nov 2024 by 25,413, with C.P. Yogeeshwara, the BJP's 2023 candidate.
- Sandur (Rs 125 crore): Congress held it, but its margin fell from 35,522 to 9,649.
- Shiggaon (Rs 100 crore): BJP won in 2023 by 35,978; Congress took it in 2024 by 13,448.
- No sanction date was found for any of the three, so whether the money came before the vote is unknown; three seats are too few to test.

## What this does and does not show
- It shows the BJP's 2022 special grant was not followed by better results in the funded seats; they did markedly worse.
- It does not show the grant hurt. The government chose the seats: it may have funded seats where its MLA was already in trouble, or MLAs who lobbied hardest. Correlation, not cause; 63 vs 58 seats.
- The fair reading for readers: money steered to ruling-party seats did not buy those seats back in 2023.

## Files
- grants_vs_2023_result_by_seat.csv: seat-level 2018 and 2023 results with the grant flag.
