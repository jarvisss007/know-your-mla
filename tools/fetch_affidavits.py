"""Download each sitting MLA's 2023 myneta affidavit page (polite: 1 request/second, cached)."""
import csv, pathlib, time, urllib.request, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build' / 'raw'
RAW.mkdir(parents=True, exist_ok=True)
URL = 'https://www.myneta.info/Karnataka2023/candidate.php?candidate_id={}'
ids = [r['myneta_candidate_id'] for r in csv.DictReader(open(ROOT / 'data' / 'mlas.csv')) if r['myneta_candidate_id']]
for i, cid in enumerate(ids):
    out = RAW / f'{cid}.html'
    if out.exists() and out.stat().st_size > 20000: continue
    req = urllib.request.Request(URL.format(cid), headers={'User-Agent': 'Mozilla/5.0 (civic research; Gandaberunda)'})
    for attempt in range(3):
        try:
            out.write_bytes(urllib.request.urlopen(req, timeout=30).read()); break
        except Exception as e:
            print('retry', cid, e); time.sleep(5)
    time.sleep(1)
print('pages', len(list(RAW.glob('*.html'))), 'of', len(ids))
