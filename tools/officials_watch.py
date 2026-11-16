"""Officials watch: a daily sweep of public news for Lokayukta / ED action in Karnataka.

What it does
  1. Reads Google News search feeds (English and Kannada) for raids, traps, suspensions,
     chargesheets, court orders and ED action involving Karnataka officials.
  2. Sorts each new headline into a type (new raid, trap, suspension, court, ...).
  3. Matches headlines against the officials already in the tracker, using a PRIVATE
     names file, so a later development on a tracked case is flagged for checking.
  4. Writes a dated review queue. Nothing is published: every item is a lead to be opened,
     read and verified by a person before it goes into research/officials_tracker.

Headlines carry names, so the names file and the queue live in the private leads repo,
never in this public repo.

Run:  py tools/officials_watch.py [--days 3] [--private ../MLA-ARE-BADDDDD]

The feeds are Google News search RSS, read for personal review only; headlines are not
republished. Kannada-script names are not matched yet (aliases are in Latin script).
"""
import argparse
import csv
import datetime as dt
import email.utils
import json
import pathlib
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
TRACKER = ROOT / "research" / "officials_tracker" / "tracker.csv"

QUERIES_EN = [
    "Karnataka Lokayukta raid", "Karnataka Lokayukta disproportionate assets",
    "Karnataka Lokayukta trap bribe", "Karnataka official suspended Lokayukta",
    "Lokayukta chargesheet Karnataka", "Karnataka High Court Lokayukta case quash OR stay OR bail",
    "sanction to prosecute Karnataka Lokayukta", "Enforcement Directorate Karnataka searches official",
]
QUERIES_KN = ["ಲೋಕಾಯುಕ್ತ ದಾಳಿ", "ಲೋಕಾಯುಕ್ತ ಬಲೆಗೆ", "ಆದಾಯ ಮೀರಿದ ಆಸ್ತಿ", "ಅಧಿಕಾರಿ ಅಮಾನತು ಲೋಕಾಯುಕ್ತ", "ಲೋಕಾಯುಕ್ತ ಆರೋಪಪಟ್ಟಿ"]

# Order matters: first match wins.
KINDS = [
    ("Verdict", r"convict|acquit|sentenced|ಶಿಕ್ಷೆ|ಖುಲಾಸೆ"),
    ("Chargesheet", r"charge ?sheet|ಆರೋಪಪಟ್ಟಿ|ದೋಷಾರೋಪ"),
    ("Sanction", r"sanction|prosecution|ಅಭಿಯೋಜನ"),
    ("Court", r"high court|\bhc\b|supreme court|quash|stay|bail|ಹೈಕೋರ್ಟ್|ಜಾಮೀನು|ತಡೆ"),
    ("Suspension", r"suspend|reinstat|ಅಮಾನತು"),
    ("ED / money laundering", r"\bed\b|enforcement directorate|pmla|money laundering|ಇಡಿ|ಜಾರಿ ನಿರ್ದೇಶನಾಲಯ"),
    ("Trap (bribe)", r"trap|bribe|red-handed|caught|nab|ಲಂಚ|ಬಲೆ"),
    ("Raid / assets", r"raid|search|disproportionate|assets|ದಾಳಿ|ಆಸ್ತಿ"),
]
KARNATAKA = r"karnataka|bengaluru|bangalore|mysuru|mangaluru|belagavi|kalaburagi|hubballi|dharwad|davanagere|shivamogga|tumakuru|ballari|vijayapura|bidar|raichur|hassan|mandya|udupi|kodagu|madikeri|chitradurga|koppal|gadag|haveri|yadgir|chikkamagaluru|chikkaballapur|kolar|ramanagara|bagalkot|uttara kannada|karwar|lokayukta|ಲೋಕಾಯುಕ್ತ"


def feed(query, lang, days):
    q = urllib.parse.quote(f"{query} when:{days}d")
    if lang == "kn":
        url = f"https://news.google.com/rss/search?q={q}&hl=kn&gl=IN&ceid=IN:kn"
    else:
        url = f"https://news.google.com/rss/search?q={q}&hl=en-IN&gl=IN&ceid=IN:en"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (personal news reader)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        root = ET.fromstring(r.read())
    for it in root.iter("item"):
        src = it.find("source")
        yield {
            "title": (it.findtext("title") or "").strip(),
            "link": it.findtext("link") or "",
            "guid": it.findtext("guid") or it.findtext("link") or "",
            "date": it.findtext("pubDate") or "",
            "outlet": src.text if src is not None else "",
        }


def norm(s):
    return re.sub(r"[^a-z0-9ಀ-೿ ]+", " ", s.lower())


def load_names(private):
    path = private / "leads" / "officials" / "names.csv"
    if not path.exists():
        return []
    out = []
    for r in csv.DictReader(open(path, encoding="utf-8")):
        for alias in r["aliases"].split("|"):
            toks = [t for t in norm(alias).split() if len(t) > 2]
            if toks:
                out.append((r["id"], alias.strip(), toks))
    return out


def match(text, names):
    t = " " + norm(text) + " "
    hits = []
    for rid, alias, toks in names:
        key = max(toks, key=len)  # the most distinctive part of the name
        if f" {key} " not in t:
            continue
        full = all(f" {k} " in t for k in toks)
        hits.append((rid, alias, "strong" if full and len(toks) > 1 else "weak"))
    seen, best = set(), []
    for h in sorted(hits, key=lambda h: h[2] != "strong"):
        if h[0] not in seen:
            seen.add(h[0])
            best.append(h)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=3)
    ap.add_argument("--private", default=str(ROOT.parent / "MLA-ARE-BADDDDD"))
    a = ap.parse_args()
    private = pathlib.Path(a.private)
    outdir = private / "leads" / "officials" / "watch"
    outdir.mkdir(parents=True, exist_ok=True)
    seen_path = outdir / "seen.json"
    seen = set(json.loads(seen_path.read_text(encoding="utf-8"))) if seen_path.exists() else set()
    names = load_names(private)
    tracked = {r["id"]: r for r in csv.DictReader(open(TRACKER, encoding="utf-8"))}

    items, errors = {}, []
    for lang, qs in (("en", QUERIES_EN), ("kn", QUERIES_KN)):
        for q in qs:
            for attempt in (1, 2):
                try:
                    for it in feed(q, lang, a.days):
                        items.setdefault(it["guid"], it)
                    break
                except Exception as e:  # one bad feed must not stop the sweep
                    if attempt == 1 and "429" in str(e):
                        time.sleep(60)  # rate-limited: wait once, then retry
                        continue
                    errors.append(f"{q}: {e}")
                    break
            time.sleep(6)  # be gentle with the feed

    new = [it for g, it in items.items() if g not in seen]
    rows = []
    for it in new:
        text = it["title"]
        if not re.search(KARNATAKA, text, re.I) and "ಲೋಕಾಯುಕ್ತ" not in text:
            continue
        kind = next((k for k, rx in KINDS if re.search(rx, text, re.I)), "Other")
        try:
            when = email.utils.parsedate_to_datetime(it["date"]).date().isoformat()
        except Exception:
            when = ""
        rows.append({**it, "kind": kind, "when": when, "hits": match(text, names)})

    today = dt.date.today().isoformat()
    lines = [f"# Officials watch, {today}", "",
             f"Sweep of the last {a.days} days: {len(items)} headlines read, {len(new)} not seen before, {len(rows)} about Karnataka.",
             "Every line is a LEAD from a headline. Open it, read the article, and only then update the tracker.", ""]
    flagged = [r for r in rows if r["hits"]]
    if flagged:
        lines += ["## Possible developments on tracked officials", ""]
        for r in sorted(flagged, key=lambda r: r["when"], reverse=True):
            for rid, alias, conf in r["hits"]:
                post = tracked.get(rid, {}).get("post", "?")
                lines.append(f"- **{rid}** ({post}) · name match {conf} on \"{alias}\" · {r['kind']} · {r['when']} · {r['outlet']}: [{r['title']}]({r['link']})")
        lines.append("")
    for kind, _ in KINDS + [("Other", "")]:
        group = [r for r in rows if r["kind"] == kind and not r["hits"]]
        if group:
            lines += [f"## {kind} ({len(group)})", ""]
            lines += [f"- {r['when']} · {r['outlet']}: [{r['title']}]({r['link']})" for r in sorted(group, key=lambda r: r["when"], reverse=True)]
            lines.append("")
    if errors:
        lines += ["## Feeds that failed", ""] + [f"- {e}" for e in errors] + [""]
    if not names:
        lines += ["Note: no names file found, so tracked officials were not matched.", ""]

    out = outdir / f"{today}.md"
    n = 2
    while out.exists():  # a second run the same day gets its own file
        out = outdir / f"{today}-{n}.md"
        n += 1
    out.write_text("\n".join(lines), encoding="utf-8")
    seen_path.write_text(json.dumps(sorted(seen | set(items))), encoding="utf-8")
    print(f"{out}: {len(rows)} Karnataka items, {len(flagged)} matched to tracked officials, {len(errors)} feed errors")


if __name__ == "__main__":
    main()
