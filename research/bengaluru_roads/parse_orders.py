"""Parse OpenCity's BBMP work-order/payment CSVs (public view of accounts.bbmp.gov.in).
Writes data/payments.csv (one row per payment line) and prints:
  - white-topping construction works grouped by work code
  - bill lines that appear more than once (same bill id) with different payment refs
Read-only; no network."""
import csv, glob, re, collections, json
FILES = {"2024-25": ["data/bbmp_2024-25_work_orders_payments.csv", "data/opencity_bbmp_05_*.csv", "data/opencity_bbmp_06_*.csv"],
         "2025-26": ["data/bbmp_2025-26_198wards.csv", "data/bbmp_2025-26_225wards.csv", "data/bbmp_2025-26_243wards.csv", "data/bbmp_2025-26_common_wards.csv"]}
BR = re.compile(r"BR\s*-\s*(\d+)\s*/\s*([\d]{2}-\w{3}-\d{4}).*?Rtgs\s*-\s*(\d+)\s*/\s*([\d]{2}-\w{3}-\d{4})", re.S)
rows = []
for fy, pats in FILES.items():
    for p in pats:
        for f in glob.glob(p):
            for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="ignore")):
                r = {k.strip().lower(): (v or "").strip() for k, v in r.items() if k}
                wo = re.sub(r"<[^>]*>", " ", r.get("wodetails", ""))
                m = re.match(r"\s*(\d{3}-\d{2}-\d{6})\s*(.*)", wo, re.S)
                b = BR.search(r.get("brnumber", ""))
                rows.append({"fy_file": fy, "file": f.split("/")[-1].split("\\")[-1], "bill_id": r.get("id"), "ward": r.get("ward"),
                             "work_code": m.group(1) if m else "", "work": re.sub(r"\s+", " ", (m.group(2) if m else wo)).strip(),
                             "contractor": r.get("contractor"), "br_no": b.group(1) if b else "", "br_date": b.group(2) if b else "",
                             "rtgs_no": b.group(3) if b else "", "rtgs_date": b.group(4) if b else "",
                             "gross": int(r.get("amount") or 0), "nett": int(r.get("nett") or 0)})
with open("data/payments.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), "payment lines")

# repeated bill ids
by = collections.defaultdict(list)
for r in rows: by[r["bill_id"]].append(r)
rep = {k: v for k, v in by.items() if len({(x["rtgs_no"], x["rtgs_date"]) for x in v}) > 1}
extra = sum(sum(x["gross"] for x in v) - v[0]["gross"] for v in rep.values())
print(len(rep), "bill ids listed with 2+ different payment refs; extra gross if each were a real payment: Rs %.2f cr" % (extra / 1e7))
pat = collections.Counter()
for v in rep.values():
    v = sorted(v, key=lambda x: x["rtgs_date"])
    pat[tuple(sorted(x["fy_file"] for x in v))] += 1
print("by file-year pattern:", dict(pat))
json.dump({k: v for k, v in list(rep.items())}, open("data/repeated_bills.json", "w"), indent=1)

# white-topping construction works
WT = re.compile(r"white.?top", re.I); NOT = re.compile(r"consultan|detailed project report|\bDPR\b|survey|restoration of road cut|RCC line", re.I)
seen = set(); g = collections.defaultdict(lambda: {"gross": 0, "lines": 0, "dates": [], "work": "", "wards": set()})
for r in rows:
    if WT.search(r["work"]) and not NOT.search(r["work"]):
        key = (r["bill_id"], r["br_no"], r["gross"])  # count each bill once
        if key in seen: continue
        seen.add(key); x = g[r["work_code"]]
        x["gross"] += r["gross"]; x["lines"] += 1; x["dates"].append(r["br_date"]); x["work"] = r["work"]; x["wards"].add(r["ward"])
print("\nWhite-topping construction works (each bill counted once):")
for k, x in sorted(g.items(), key=lambda kv: -kv[1]["gross"]):
    print(f"{k} | Rs {x['gross']/1e7:6.2f} cr | {x['lines']} bills | bills {min(x['dates'])}..{max(x['dates'])} | {x['work'][:150]}")
