# Bring the site's MLA list up to date: 2024 and 2026 by-elections, and the missing Sarvagnanagar seat.
import io, json, re, csv, sys
site = sys.argv[1]
p = site + '/index.html'
s = io.open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:80])
    s = s.replace(old, new)

m = re.search(r'const D = (\[.*?\]);\n', s)
D = json.loads(m.group(1))
before = len(D)

GEORGE_SCAN = 'https://data.opencity.in/dataset/karnataka-assembly-elections-2023-affidavits/resource/0d78c24d-edbd-4737-983a-5eec40833b9e'
NEW = {  # constituency -> current MLA (myneta transcription of the by-election affidavit)
 'Channapatna':      dict(n='C P Yogeeshwara', p='Congress', k=10, a=67.55, l=29.28, id='9526', by='Nov 2024'),
 'Shiggaon':         dict(n='Pathan Yasirahmedkhan', p='Congress', k=0, a=3.05, l=0, id='9563', by='Nov 2024'),
 'Sandur (ST)':      dict(n='E Annapoorna', p='Congress', k=0, a=3.37, l=1.47, id='9556', by='Nov 2024'),
 'Bagalkot':         dict(n='Umesh Hullappa Meti', p='Congress', k=0, a=11.38, l=0.03, id='9595', by='Apr 2026'),
 'Davanagere South': dict(n='Samarth Shamanur Mallikarjuna', p='Congress', k=None, a=None, l=None, id='', by='Apr 2026'),
}
out, seen = [], set()
for d in D:
    c = d['c']
    if c in NEW:
        if c in seen: continue          # drops the second Bagalkot row (the late H.Y. Meti)
        seen.add(c)
        d = dict(c=c, a18=None, a23=None, **NEW[c])
        d['a23'] = d['a']
    out.append(d)
assert seen == set(NEW), seen
assert not any(d['c'] == 'Sarvagnanagar' for d in out)
out.append(dict(n='K. J. George', c='Sarvagnanagar', p='Congress', k=None, a=214.85, l=37.70, a18=None, a23=214.85, id='', url=GEORGE_SCAN))
assert len(out) == 224, len(out)
cons = [d['c'] for d in out]; assert len(set(cons)) == 224, [c for c in cons if cons.count(c) > 1]
missing = sum(1 for d in out if d['a'] is None)
s = s[:m.start(1)] + json.dumps(out, ensure_ascii=False, separators=(',', ':')) + s[m.end(1):]

# rendering: link override, unknown cases, by-election label
rep("const link = d.id ? `https://www.myneta.info/Karnataka2023/candidate.php?candidate_id=${d.id}` :",
    "const link = d.url ? d.url : d.id ? `https://www.myneta.info/Karnataka2023/candidate.php?candidate_id=${d.id}` :")
rep("${d.id ? t.read : t.find}", "${d.id || d.url ? t.read : t.find}")
rep("+ metric(t.cases, d.k)", "+ metric(t.cases, d.k == null ? t.notshown : d.k, d.k == null ? 'na' : '')")
rep('<span class="party ${pclass(d.p)}">${esc(t.party[d.p] || d.p)}</span></p>',
    '<span class="party ${pclass(d.p)}">${esc(t.party[d.p] || d.p)}</span>${d.by ? `<span class="by">${t.by} ${esc(d.by)}</span>` : \'\'}</p>')
rep("na: 'Not in archive',", "by: 'By-election', na: 'Not in archive',")
rep("na: 'ದಾಖಲೆಯಲ್ಲಿ ಲಭ್ಯವಿಲ್ಲ',", "by: 'ಉಪಚುನಾವಣೆ', na: 'ದಾಖಲೆಯಲ್ಲಿ ಲಭ್ಯವಿಲ್ಲ',")
rep('.party.Congress::before', '.by { font-size: 11px; padding: 1px 7px; border: 1px solid var(--line); border-radius: 999px; color: var(--muted) }\n.party.Congress::before')

# wording: the list is no longer purely the 2023 result
OLD_LEAD = "What each of Karnataka's 224 MLAs swore to the Election Commission in 2023: their wealth, their debts and the criminal cases against them. Search for your constituency."
NEW_LEAD = "What each of Karnataka's 224 MLAs swore to the Election Commission when they were elected: their wealth, their debts and the criminal cases against them. Search for your constituency."
i = s.index(OLD_LEAD); j = s.index("'", s.index(':', s.index(OLD_LEAD, i + 1) + len(OLD_LEAD)) + 1)
rep(OLD_LEAD, NEW_LEAD, 2)
kn_lead_start = s.index(NEW_LEAD, s.index(NEW_LEAD) + 1) + len(NEW_LEAD)
q1 = s.index("'", s.index(':', kn_lead_start)); q2 = s.index("'", q1 + 1)
s = s[:q1 + 1] + 'ಕರ್ನಾಟಕದ 224 ಶಾಸಕರು ಆಯ್ಕೆಯಾದಾಗ ಚುನಾವಣಾ ಆಯೋಗಕ್ಕೆ ಪ್ರಮಾಣಪತ್ರದಲ್ಲಿ ಘೋಷಿಸಿದ ಆಸ್ತಿ, ಸಾಲ ಮತ್ತು ಕ್ರಿಮಿನಲ್ ಪ್ರಕರಣಗಳು. ನಿಮ್ಮ ಕ್ಷೇತ್ರವನ್ನು ಹುಡುಕಿ.' + s[q2:]
rep("in 2023.\">", "when they were elected.\">")

old_note = re.search(r"Figures are from the 2023 election\. Some seats have changed hands since\. Asset figures were not available for \d+ MLAs\.", s).group(0)
new_note = ("Figures are from the 2023 election, except five seats won in by-elections since (Channapatna, Shiggaon and Sandur in November 2024; "
            "Bagalkot and Davanagere South in April 2026), which show the new MLA's by-election affidavit. "
            "Asset figures are not available for %d MLAs." % missing)
rep(old_note, new_note, 2)
nk = s.index(new_note, s.index(new_note) + 1) + len(new_note)
q1 = s.index("'", s.index(':', nk)); q2 = s.index("'", q1 + 1)
s = s[:q1 + 1] + ('ಅಂಕಿಗಳು 2023ರ ಚುನಾವಣೆಯವು. ನಂತರ ಉಪಚುನಾವಣೆ ನಡೆದ ಐದು ಕ್ಷೇತ್ರಗಳಲ್ಲಿ (ಚನ್ನಪಟ್ಟಣ, ಶಿಗ್ಗಾಂವಿ, ಸಂಡೂರು: ನವೆಂಬರ್ 2024; '
                  'ಬಾಗಲಕೋಟೆ, ದಾವಣಗೆರೆ ದಕ್ಷಿಣ: ಏಪ್ರಿಲ್ 2026) ಹೊಸ ಶಾಸಕರ ಪ್ರಮಾಣಪತ್ರವನ್ನು ತೋರಿಸಲಾಗಿದೆ. %d ಶಾಸಕರ ಆಸ್ತಿ ವಿವರ ಲಭ್ಯವಿಲ್ಲ.' % missing) + s[q2:]

# corrections log
anchor = '<li>12 Nov 2026: An earlier post implied'
rep(anchor, ('<li>13 Nov 2026: The MLA list still showed the 2023 winners in five seats that have since had by-elections '
             '(Channapatna, Shiggaon, Sandur, Bagalkot, Davanagere South), listed Bagalkot twice, and left out Sarvagnanagar '
             '(K.J. George, whose affidavit is not in the ADR archive). The current MLAs are now shown, and George\'s figures come '
             'from a scan of his 2023 affidavit.</li>\n      ') + anchor)
io.open(p, 'w', encoding='utf-8', newline='').write(s)

with io.open(site + '/data/mlas.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['name', 'constituency', 'party', 'declared_cases', 'assets_crore', 'liabilities_crore', 'assets_crore_2018', 'myneta_candidate_id', 'election', 'source_url'])
    for d in out:
        w.writerow([d['n'], d['c'], d['p'], '' if d['k'] is None else d['k'], '' if d['a'] is None else d['a'], '' if d['l'] is None else d['l'],
                    '' if d.get('a18') is None else d['a18'], d['id'], ('By-election ' + d['by']) if d.get('by') else '2023', d.get('url', '')])
print('rows', before, '->', len(out), '| no asset figure:', missing)
