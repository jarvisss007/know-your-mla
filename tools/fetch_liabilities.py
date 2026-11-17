"""Fetch the liability figures from every MLA's affidavit page on myneta.info.

    py tools/fetch_liabilities.py
writes data/liabilities_myneta.csv, one row per MLA with a candidate id:
  affidavit_total_cr  loans: the affidavit's "Grand Total of Liabilities" (part i); Nil = 0
  govt_dues_cr        "Grand Total of all Govt Dues" (part ii: income tax, property tax, utility dues); Nil = 0
  disputed_cr         liabilities the candidate lists as in dispute (part iv), total column; Nil = 0
  myneta_total_cr     myneta's headline "Liabilities" (its calculated sum of i + ii + iv). Unreliable: for some
                      MLAs it prints Nil although part i is not nil (e.g. Gauribidanur), so it is kept for reference only.
The site's own figure `l` in index.html is part i + part ii (checked 16-17 Nov 2026, research/DEBTS_CHECK_2026-11-16.md).
Each row's total column is the last "Rs <amount>" in that row; a row whose total cell is Nil has none.
One request a second; myneta is a volunteer-run archive.

    py tools/fetch_liabilities.py Mandya Humnabad
fetches only the named constituencies and updates their rows in the existing CSV.
"""
import csv, html, json, pathlib, re, sys, time, urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / "index.html").read_text(encoding="utf-8")
k = src.index("const D = [")
D = json.loads(src[k + 10: src.index("];", k) + 1])


def rupees_cr(s):
    return round(int(s.replace(",", "")) / 1e7, 2)


ONLY = set(sys.argv[1:])
rows = []
for d in D:
    if not d.get("id") or (ONLY and d["c"] not in ONLY):
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

    def row_total(start, end):
        """Total column of one affidavit row: the last 'Rs <amount>' between two labels; None if the row is missing."""
        a = txt.find(start)
        if a < 0:
            return None
        b = txt.find(end, a + len(start))
        seg = txt[a + len(start): b if b > 0 else a + 3000]
        amts = re.findall(r"Rs ([\d,]+)", seg)
        return rupees_cr(amts[-1]) if amts else 0

    loans = row_total("Grand Total of Liabilities (as per affidavit)", "Dues to")
    if loans == 0:
        # myneta sometimes prints the part i grand total as Nil or 0 although the rows above it are filled in
        # (Hadagali, Muddebihal, Jagalur, Doddaballapur, checked 17 Nov 2026): add up the three rows instead.
        parts = [row_total("Loans from Banks / FIs", "Loans due to Individual"),
                 row_total("Loans due to Individual / Entity", "Any other Liability"),
                 row_total("Any other Liability", "Grand Total of Liabilities")]
        loans = round(sum(x or 0 for x in parts), 2)
    dues = row_total("Grand Total of all Govt Dues (as per affidavit)", "Whether any other liabilities are in dispute")
    disp = row_total("authority before which it is pending", "Totals (Calculated")
    rows.append({"constituency": d["c"], "name": d["n"], "candidate_id": d["id"],
                 "affidavit_total_cr": "" if loans is None else loans,
                 "govt_dues_cr": "" if dues is None else dues,
                 "disputed_cr": "" if disp is None else disp,
                 "myneta_total_cr": rupees_cr(head.group(1)) if head else ("0" if nil else ""),
                 "fetched_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
    time.sleep(1)

out = ROOT / "data" / "liabilities_myneta.csv"
if ONLY and out.exists():
    keep = [r for r in csv.DictReader(open(out, encoding="utf-8")) if r["constituency"] not in ONLY]
    order = [d["c"] for d in D]
    rows = sorted(keep + rows, key=lambda r: order.index(r["constituency"]) if r["constituency"] in order else 999)
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print("ok", len(rows), "rows;", sum(1 for r in rows if r["affidavit_total_cr"] == ""), "without an affidavit liabilities row")
