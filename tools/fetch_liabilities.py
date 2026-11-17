"""Fetch myneta.info's two liability figures for every MLA with a candidate id.

    py tools/fetch_liabilities.py
writes data/liabilities_myneta.csv: constituency, name, candidate_id, affidavit_total_cr (the affidavit's own
"Grand Total of Liabilities"), myneta_total_cr (myneta's headline "Liabilities", the calculated sum that also
counts dues to government departments and liabilities listed as in dispute), fetched_utc.
One request a second; myneta is a volunteer-run archive.
"""
import csv, html, json, pathlib, re, time, urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / "index.html").read_text(encoding="utf-8")
k = src.index("const D = [")
D = json.loads(src[k + 10: src.index("];", k) + 1])


def rupees_cr(s):
    return round(int(s.replace(",", "")) / 1e7, 2)


rows = []
for d in D:
    if not d.get("id"):
        continue
    url = f"https://www.myneta.info/Karnataka2023/candidate.php?candidate_id={d['id']}"
    for attempt in range(3):
        try:
            raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research; Gandaberunda)"}), timeout=40).read().decode("utf-8", "ignore")
            break
        except Exception as e:
            raw = ""; time.sleep(3)
    txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw)))
    head = re.search(r"Liabilities: Rs ([\d,]+)", txt)
    nil = re.search(r"Liabilities: Nil", txt)
    aff = re.search(r"Grand Total of Liabilities \(as per affidavit\)(.*?)Rs ([\d,]+)", txt)
    rows.append({"constituency": d["c"], "name": d["n"], "candidate_id": d["id"],
                 "affidavit_total_cr": rupees_cr(aff.group(2)) if aff else ("0" if nil else ""),
                 "myneta_total_cr": rupees_cr(head.group(1)) if head else ("0" if nil else ""),
                 "fetched_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
    time.sleep(1)

out = ROOT / "data" / "liabilities_myneta.csv"
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print("ok", len(rows), "rows;", sum(1 for r in rows if r["myneta_total_cr"] == ""), "without a headline figure")
