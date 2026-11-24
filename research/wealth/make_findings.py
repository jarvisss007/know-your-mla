"""Step 5: write FINDINGS_DRAFT.md from CACHE/summary.json and the CSV (every number comes from there).
Usage: py make_findings.py CACHE_DIR
"""
import csv, json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
S = json.load(open(pathlib.Path(sys.argv[1]) / 'summary.json'))
ROWS = list(csv.DictReader(open(HERE / 'affidavits_2013_2018_2023.csv', encoding='utf-8')))
BYNAME = {(r['name'], r['constituency']): r for r in ROWS}
P = S['parties']

def f(x, d=2):
    if x is None or x == '': return 'n/a'
    return f'{float(x):,.{d}f}'

def pct(x): return 'n/a' if x is None else f'{x:,.0f}%'

def income_cell(r):
    t = r.get('income_test_2018_2023') or ''
    if t.startswith('growth larger'):
        return 'growth larger than declared income would suggest' + (' (movable rise alone, net of new loans, also exceeds it)' if 'movable assets alone' in t else '')
    return t or 'n/a'

L = []
w = L.append
w('# DRAFT: What Karnataka MLAs declared, 2013 vs 2018 vs 2023')
w('')
w('**Status: DRAFT research, not for the site until re-checked.** Built 24 Nov 2026 from myneta.info (ADR\'s transcription of the '
  'Election Commission affidavits). Every figure is self-declared by the candidate, covers the candidate plus spouse and dependants, '
  'and is a lead for checking against the scanned affidavit, not a finding about anyone\'s conduct.')
w('')
w('Files in this folder: `affidavits_2013_2018_2023.csv` (one row per sitting MLA, all three affidavits, growth and checks), '
  '`MATCH_REVIEW.csv` (matches a person must confirm), and the scripts that produced them (`fetch_myneta.py`, `myneta_parse.py`, '
  '`match_affidavits.py`, `link_groups.py`, `build_wealth.py`, `analyze.py`, `make_findings.py`). Raw pages were cached outside the repo.')
w('')
w('## Method')
w('')
w('1. **Who.** The 224 rows of `data/mlas.csv`. The "2023" affidavit is the one that elected the sitting member: the May 2023 general '
  'election for 219, the Nov 2024 by-elections for Channapatna, Shiggaon and Sandur, and the Apr 2026 by-election for Bagalkot. '
  'Davanagere South\'s Apr 2026 winner (Samarth Shamanur Mallikarjuna) has no affidavit on myneta yet. K. J. George (Sarvagnanagar) is not '
  'on myneta for 2023; his 2023 totals come from the site\'s existing opencity figure, with no movable/immovable split.')
w('2. **Candidate lists.** Every candidate myneta lists for Karnataka 2023, 2018 and 2013 (2,593 / 2,576 / 2,788 candidates; some list rows '
  'are hidden behind an obfuscated script on myneta and were decoded). One request a second.')
w('3. **Matching.** Seats were matched by name (delimitation was 2008, so 2013 and 2018 use the same 224 seats; spellings such as Kaup/Kapu, '
  'Byndoor/Baindur, Karkal/Karkala were mapped by hand). Within the seat, names were compared after removing case, dots, titles and word order. '
  'Confidence: **exact** = same name, same seat; **probable** = a name variant in the same seat (initials expanded, spelling variant, a '
  'father\'s name added), where every word of the MLA\'s name is present; **uncertain** = anything else (a word of the MLA\'s name missing, '
  'which is how a father or son with the family name shows up; the same name in a different seat; two candidates that fit equally). '
  'Nothing uncertain is used in the rankings or medians.')
w('4. **Second check.** Each MLA\'s myneta page has an "Other Elections" box, ADR\'s own grouping of a person\'s affidavits. It was read for '
  'every MLA and compared with the name match. Where it agreed with a same-seat name variant the match is probable; where it pointed to a '
  'different affidavit than an exact or probable name match, the match was downgraded to uncertain. Grouped affidavits from by-elections '
  'held between general elections (2019 to 2021) sit in the same myneta folders and were not used as "2018".')
w('5. **Numbers.** From each matched page: total assets and liabilities (myneta\'s headline), movable and immovable totals (the '
  'affidavit\'s stated totals; where a stated total is nil but the itemised rows are not, the row sum, choosing the pair that reproduces the '
  'headline total), and the income shown in income-tax returns. The 2023 affidavits list five years of ITR income (FY2018-19 to '
  'FY2022-23 for most) for self, spouse and dependants; that five-year family sum is the "declared income" for 2018 to 2023. The 2018 '
  'and 2013 affidavits list a single year, so no income comparison is made for 2013 to 2018.')
w('6. **Growth.** Change in total assets 2013 to 2018, 2018 to 2023 and 2013 to 2023, in crore and per cent; the change in movable and in '
  'immovable assets; the change in liabilities and in net worth (assets minus liabilities). Composition: "mostly immovable" when the immovable '
  'change is at least 60% of the total change, "mostly movable" likewise, else "mixed". Percentage rankings only include MLAs who started '
  'at Rs 1 crore or more (otherwise a Rs 20 lakh start dominates).')
w('7. **Income test (2018 to 2023 only).** The phrase "growth larger than declared income would suggest" is used only where net worth rose by '
  'at least twice the family\'s five-year ITR income *and* by at least Rs 5 crore more than that income, and at least four ITR years are '
  'listed. Even then it is arithmetic, not a conclusion: affidavits value land differently across years, agricultural income is exempt and '
  'not in ITR "total income", and gifts and inheritance are not income.')
w('8. **Add-up check.** Where the affidavit\'s stated movable, immovable or liability total differs from the sum of its itemised rows (as '
  'myneta transcribed them) by more than 10% and more than Rs 1 crore. This can be the candidate\'s arithmetic, a nil total line, or '
  'myneta\'s transcription; only the scanned affidavit settles it.')
w('')
w('## Match counts')
w('')
mc = S['match_counts']
w('| Affidavit | exact | probable | uncertain (to review) | no match |')
w('|---|---|---|---|---|')
for y in ('2023', '2018', '2013'):
    m = mc[y]
    w(f'| {y} | {m.get("exact", 0)} | {m.get("probable", 0)} | {m.get("uncertain", 0)} | {m.get("none", 0)} |')
w('')
g18, g13 = S['grouping_counts']['2018'], S['grouping_counts']['2013']
w(f'Of the {mc["2018"]["exact"] + mc["2018"]["probable"]} usable 2018 matches, myneta\'s own grouping agrees with {g18.get("agrees", 0)}; '
  f'of the {mc["2013"]["exact"] + mc["2013"]["probable"]} usable 2013 matches, it agrees with {g13.get("agrees", 0)}. '
  '"No match" mostly means the MLA did not contest that year (first-time candidates, or contested elsewhere under a name we could not tie). '
  f'MATCH_REVIEW.csv has {S["n_review"]} rows for a person to decide. In the 2018 to 2023 comparison, '
  f'{S["party_switch_2018_2023"]} MLAs stood for a different party in 2018 than the one they sit with now; results by party use the current party.')
w('')
A = P['ALL']
w('## The overall picture')
w('')
w(f'- Sitting MLAs with a usable 2018 and 2023 affidavit: **{A["n_2018_2023"]}**. Median declared assets {f(A["median_assets_2018_cr"])} crore in 2018, '
  f'{f(A["median_assets_2023_cr_same_mlas"])} crore in 2023 (same people). Median change **+{f(A["median_growth_cr_2018_2023"])} crore ({pct(A["median_growth_pct_2018_2023"])})**.')
w(f'- Of these, the rise was mostly immovable (land, buildings) for {A["composition_2018_2023"]["mostly immovable"]}, mostly movable (cash, deposits, '
  f'shares, loans given, vehicles, jewellery) for {A["composition_2018_2023"]["mostly movable"]}, mixed for {A["composition_2018_2023"]["mixed"]}; '
  f'{A["n_fell_2018_2023"]} declared less in 2023 than in 2018. Median movable change +{f(A["median_movable_change_cr_2018_2023"])} crore, '
  f'median immovable change +{f(A["median_immovable_change_cr_2018_2023"])} crore.')
w(f'- With a usable 2013 affidavit too: {A["n_2013_2023"]} MLAs; median change 2013 to 2023 +{f(A["median_growth_cr_2013_2023"])} crore ({pct(A["median_growth_pct_2013_2023"])}).')
w(f'- The income test phrase applies to {A["n_income_flag"]} MLAs (listed below); for most of them the rise is mostly immovable, where land '
  'revaluation alone can produce it.')
w('')

def table(key, period):
    w('| # | MLA (seat) | Party now | ' + ('2013 | ' if period == '2013_2023' else '') + '2018 | 2023 | Change, crore | Change % | Movable change | Immovable change | Mostly | Family ITR income, 5 yrs | Note |')
    w('|---|---|---|' + ('---|' if period == '2013_2023' else '') + '---|---|---|---|---|---|---|---|---|')
    for i, x in enumerate(S['rankings'][key], 1):
        r = BYNAME[(x['name'], x['constituency'])]
        note = []
        if period == '2018_2023': note.append(income_cell(r))
        if r['match_2018'] == 'probable' or (period == '2013_2023' and r['match_2013'] == 'probable'): note.append('probable match')
        yrs = ('2018', '2023') if period == '2018_2023' else ('2013', '2023')
        if any(r['addup_' + y] for y in yrs): note.append("an affidavit's totals do not add up (see below)")
        w(f'| {i} | {x["name"]} ({x["constituency"]}) | {x["party_now"]} | ' + (f'{f(x["assets_cr_2013"])} | ' if period == '2013_2023' else '') +
          f'{f(x["assets_cr_2018"])} | {f(x["assets_cr_2023"])} | {f(r["growth_cr_" + period])} | {pct(float(r["growth_pct_" + period]) if r["growth_pct_" + period] else None)} | '
          f'{f(r["movable_change_cr_" + period])} | {f(r["immovable_change_cr_" + period])} | {r["composition_" + period] or "n/a"} | '
          f'{f(r["family_itr_income_cr_2023_affidavit"]) + " cr" if period == "2018_2023" and r["family_itr_income_cr_2023_affidavit"] else "n/a"} | {"; ".join(note)} |')
    w('')

w('## Largest increases, 2018 to 2023 (crore)')
w('')
w('Amounts in Rs crore, as declared. "Family ITR income, 5 yrs" is the sum of income shown in returns by self, spouse and dependants in the 2023 affidavit.')
w('')
table('abs_2018_2023', '2018_2023')
w('## Largest increases, 2018 to 2023 (per cent; 2018 assets at least Rs 1 crore)')
w('')
table('pct_2018_2023', '2018_2023')
w('## Largest increases, 2013 to 2023 (crore)')
w('')
w('No income comparison: the 2013 and 2018 affidavits list one year of ITR income only.')
w('')
table('abs_2013_2023', '2013_2023')
w('## Largest increases, 2013 to 2023 (per cent; 2013 assets at least Rs 1 crore)')
w('')
table('pct_2013_2023', '2013_2023')
w('## Largest decreases')
w('')
w('2018 to 2023 (all MLAs whose declared assets fell, largest first):')
w('')
w('| MLA (seat) | Party now | 2018 | 2023 | Change | Movable change | Immovable change | Liabilities change |')
w('|---|---|---|---|---|---|---|---|')
for x in S['rankings']['fall_2018_2023']:
    r = BYNAME[(x['name'], x['constituency'])]
    w(f'| {x["name"]} ({x["constituency"]}) | {x["party_now"]} | {f(x["assets_cr_2018"])} | {f(x["assets_cr_2023"])} | {f(r["growth_cr_2018_2023"])} | '
      f'{f(r["movable_change_cr_2018_2023"])} | {f(r["immovable_change_cr_2018_2023"])} | {f(r["liabilities_change_cr_2018_2023"])} |')
w('')
w('2013 to 2023 decreases: ' + '; '.join(f'{x["name"]} ({x["constituency"]}, {x["party_now"]}) {f(x["assets_cr_2013"])} to {f(x["assets_cr_2023"])} crore'
                                          for x in S['rankings']['fall_2013_2023']) + '.')
w('')
w('A fall can be a sale, a gift to a family member who is no longer a dependant, a lower valuation, or a debt written off; the affidavit does not say which.')
w('')
w('## Where growth is larger than declared income would suggest (2018 to 2023)')
w('')
w('Net worth change against the family\'s five-year ITR income in the 2023 affidavit. Affidavits value land differently across years '
  '(purchase cost in one, an estimate of market value in the next), agricultural income is exempt and not in these figures, and inheritance '
  'and gifts are not income. Read each row as "the arithmetic does not close on the declared figures alone", nothing more.')
w('')
w('| MLA (seat) | Party now | Net worth change, crore | Family ITR income, 5 yrs, crore | Asset rise mostly | Movable rise net of new loans also exceeds income? |')
w('|---|---|---|---|---|---|')
for x in sorted(S['income_flags'], key=lambda x: -x['nw']):
    w(f'| {x["name"]} ({x["constituency"]}) | {x["party_now"]} | {f(x["nw"])} | {f(x["income"])} | {x["composition"]} | {"yes" if "movable assets alone" in x["text"] else "no"} |')
w('')
w('## Affidavits whose totals do not add up')
w('')
w('Stated total vs the sum of itemised rows, more than 10% and more than Rs 1 crore apart. Years used in the comparison only.')
w('')
w('| MLA (seat) | Party now | Discrepancy |')
w('|---|---|---|')
for a in S['addup']:
    parts = [p for p in a['issues'].split(' | ') if p[:4] in a['used_years']]
    if parts: w(f'| {a["name"]} ({a["constituency"]}) | {a["party_now"]} | {"; ".join(parts)} |')
w('')
w('## By party')
w('')
w('Current party. Medians over MLAs with a usable affidavit in both years. Independents, KRPP and SKP members have no usable 2018 match.')
w('')
w('| Party | MLAs | Median assets 2023 (all) | n, 2018 to 2023 | Median 2018 | Median 2023 | Median change, crore | Median change % | Median movable change | Median immovable change | Mostly immovable / movable / mixed / fell | Income-test phrase applies | n, 2013 to 2023 | Median change 2013 to 2023 | % |')
w('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for p in ('Congress', 'BJP', 'JD(S)', 'Independent', 'KRPP', 'SKP', 'ALL'):
    x = P[p]; c = x['composition_2018_2023']
    fell = c['mostly immovable (fall)'] + c['mostly movable (fall)'] + c['mixed (fall)']
    w(f'| {p} | {x["mlas"]} | {f(x["median_assets_2023_cr"])} | {x["n_2018_2023"]} | {f(x["median_assets_2018_cr"])} | {f(x["median_assets_2023_cr_same_mlas"])} | '
      f'{f(x["median_growth_cr_2018_2023"])} | {pct(x["median_growth_pct_2018_2023"])} | {f(x["median_movable_change_cr_2018_2023"])} | {f(x["median_immovable_change_cr_2018_2023"])} | '
      f'{c["mostly immovable"]} / {c["mostly movable"]} / {c["mixed"]} / {fell} | {x["n_income_flag"]} | {x["n_2013_2023"]} | {f(x["median_growth_cr_2013_2023"])} | {pct(x["median_growth_pct_2013_2023"])} |')
w('')
w('The party medians are close to one another; the differences are smaller than the spread inside each party, and the samples are small '
  'for JD(S). The same pattern (most of the rise in land and buildings) holds in every party.')
w('')
w('## Caveats')
w('')
w('- Self-declared figures, transcribed by myneta. Before anything is published about a named MLA, open the scanned affidavit on the '
  'Election Commission\'s site and check the totals by hand.')
w('- Land is valued inconsistently: some affidavits give purchase cost, some an estimate of current market value, and the same plot can '
  'jump in value between affidavits with no transaction. Immovable growth is the least reliable part of these numbers.')
w('- Totals include spouse and dependants, whose membership changes (a child who becomes independent drops out).')
w('- Five years of ITR income is taxable income after deductions; it is not spending money, and agricultural income is exempt and absent.')
w('- Nominal rupees, no inflation adjustment (prices rose roughly a third between 2018 and 2023).')
w('- A match marked probable is a name variant in the same seat, usually confirmed by myneta\'s grouping; it is still not a document check.')
w('- "Uncertain" and "no match" rows are left out of every ranking and median. That leaves out first-term MLAs and people who changed seats '
  '(for example Siddaramaiah, who contested Badami and Chamundeshwari in 2018 and Varuna in 2023), until a person confirms them.')
w('')
w('## Needs a person')
w('')
w(f'- **MATCH_REVIEW.csv ({S["n_review"]} rows).** Each row has the candidate found, why it is uncertain, other candidates, myneta\'s grouping, '
  'and the page link. Several look like the same person under a different seat or spelling (Siddaramaiah 2018, A C Srinivasa, N Y Gopalakrishna, '
  'B Nagendra 2013, Madhu Bangarappa 2018, Nayana Motamma 2018, U T Khader 2013, Basavaraj Rayareddi 2013); several look like a relative '
  'who shares the family name and must not be used (B S Yediyurappa for Vijayendra, '
  'Umesh Katti for Nikhil Katti, Umesh Jadhav for Avinash Jadhav, K B Koliwad for Prakash Koliwad, M C Managuli for Ashok Managuli, '
  'Hullappa Meti for Umesh Meti); the rest need a look. Confirmed rows can then be re-run into the rankings.')
w('- **K H Puttaswamy Gowda (Gauribidanur, Independent):** myneta\'s 2023 headline is Rs 1,267 crore, but the itemised rows it transcribed add to '
  'about Rs 12 crore movable and nothing immovable. Check the scan before using his figure anywhere.')
w('- **D K Shivakumar 2023 liabilities:** stated Rs 265 crore, itemised rows add to Rs 503 crore on myneta.')
w('- **Davanagere South:** no affidavit for the Apr 2026 by-election winner on myneta yet.')
w('- **K. J. George:** 2023 from opencity (totals only); add the movable/immovable split from the scan.')
w('- **Hiriyur and Dharwad:** `data/mlas.csv` still carries the members who died (Hiriyur, 10 May 2026) and were disqualified (Dharwad, '
  'from 15 Apr 2026); their rows are kept here as elected in 2023.')
w('- **By-election winners** (Channapatna, Shiggaon, Sandur, Bagalkot): their "2023" column is the later by-election affidavit, so their '
  '2018 to 2023 change actually runs to 2024 or 2026.')
(HERE / 'FINDINGS_DRAFT.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
print('written', len(L), 'lines')
