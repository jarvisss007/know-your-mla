import io, json, re
sk = io.open(r'C:\Users\binap\.claude\scheduled-tasks\gandaberunda-upload-retry\SKILL.md', encoding='utf-8').read()
def grab(key, nxt):
    title = re.search(r'^%s title: (.*)$' % key, sk, re.M).group(1).strip()
    d = sk.split('%s description:\n' % key, 1)[1]
    d = d.split('\n\n%s title:' % nxt, 1)[0] if nxt else d
    return title, d.strip()
tD, dD = grab('D', 'A')
tA, dA = grab('A', 'B')
tB, dB = grab('B', 'C')
tC = re.search(r'^C title: (.*)$', sk, re.M).group(1).strip()
en = dA.split('\n\n', 1)[1]  # drop the Kannada paragraph
en = en.rsplit('\n\n', 1)[0] + '\n\n#Karnataka #Yettinahole #Kolar #Chikkaballapur #CAG #Bengaluru'
dC = en
first = [
 {'file': 'mallanna1-kn.mp4', 'title': tD, 'description': dD, 'date': '15 Nov 2026', 'time': '06:30'},
 {'file': 'yettinahole-kn.mp4', 'title': tA, 'description': dA, 'date': '20 Nov 2026', 'time': '05:30'},
 {'file': 'wealth-en.mp4', 'title': tB, 'description': dB, 'date': '22 Nov 2026', 'time': '05:30'},
 {'file': 'yettinahole-en.mp4', 'title': tC, 'description': dC, 'date': '23 Nov 2026', 'time': '05:30'},
]
m = json.load(io.open('upload_manifest.json', encoding='utf-8'))
allv = first + m['batch1'] + m['batch2'] + m['batch3']
for v in allv:
    assert len(v['title']) <= 100, v['title']
    v['status'] = 'pending'
json.dump(allv, io.open('upload_all.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for i, v in enumerate(allv): print(i, v['file'], v['date'], v['time'], len(v['title']))
print(dC[-200:])
