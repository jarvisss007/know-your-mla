"""Entity links: connect raided officials to registered businesses, and draft the complaint.

Input (PRIVATE repo, because it carries names):
  leads/officials/entities.csv with columns
    id            tracker row id (research/officials_tracker/tracker.csv)
    entity        registered name of the company, LLP, trust, society or school
    kind          company | LLP | trust | society | school | proprietorship | unknown
    reg_no        CIN / LLPIN / UDISE / society number, if shown
    register_url  the public page the details were read from
    official_role director | partner | trustee | proprietor | none listed | not checked
    note          what the register shows, in plain words (no inference)
    confidence    high | medium | low
    source_url    the raid report that first named the business

Output (PRIVATE repo):
  leads/officials/LINKS.md                 one board: every link, its evidence and confidence
  leads/officials/complaints/<id>.md       a draft letter for each high-confidence link, for the
                                           owner to read, sign and file. Nothing is sent from here.

Printed: aggregate counts only (no names), safe to quote in the public tracker.

Run:  py tools/entity_links.py [--private ../MLA-ARE-BADDDDD]
"""
import argparse
import csv
import datetime as dt
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TRACKER = ROOT / "research" / "officials_tracker" / "tracker.csv"

LETTER = """# DRAFT, not sent. For the owner to check, sign and file.

To: The Registrar, Karnataka Lokayukta, M.S. Building, Bengaluru 560001
(copy, if the business is a company or LLP: the Income Tax Benami Prohibition Unit, Bengaluru)

Date: {today}

Subject: Information from public records for the ongoing case against the {post}, {department}, {district} (searched on {action_date})

Sir/Madam,

Your office searched premises linked to the above official on {action_date}, as reported in {source_url}.

Public registers show the following, which may help the investigation:

- Entity: {entity} ({kind}{reg})
- What the register shows: {note}
- Official's listed role: {official_role}
- Where this was read: {register_url}

We make no allegation beyond what these public records show, and we have not contacted the official
or anyone named in the register. We request that this be placed before the investigating officer.

Name, address and phone of the complainant: ____________________
Signature: ____________________

Attachments: printouts of the register pages above, dated.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--private", default=str(ROOT.parent / "MLA-ARE-BADDDDD"))
    a = ap.parse_args()
    base = pathlib.Path(a.private) / "leads" / "officials"
    src = base / "entities.csv"
    rows = list(csv.DictReader(open(src, encoding="utf-8")))
    tracked = {r["id"]: r for r in csv.DictReader(open(TRACKER, encoding="utf-8"))}
    today = dt.date.today().isoformat()

    lines = [f"# Entity links, {today}", "",
             "Every line is a lead read from a public register. Confidence is about the match, not about wrongdoing.", ""]
    for conf in ("high", "medium", "low"):
        group = [r for r in rows if r["confidence"] == conf]
        if not group:
            continue
        lines += [f"## {conf.capitalize()} confidence ({len(group)})", ""]
        for r in group:
            t = tracked.get(r["id"], {})
            reg = f", {r['reg_no']}" if r["reg_no"] else ""
            lines.append(f"- **{r['id']}** {t.get('post', '?')}, {t.get('department', '?')}: {r['entity']} ({r['kind']}{reg}). "
                         f"Official's role: {r['official_role']}. {r['note']} [register]({r['register_url']}) · [raid report]({r['source_url']})")
        lines.append("")
    (base / "LINKS.md").write_text("\n".join(lines), encoding="utf-8")

    outdir = base / "complaints"
    outdir.mkdir(exist_ok=True)
    drafted = 0
    for r in rows:
        if r["confidence"] != "high" or r["official_role"] in ("not checked",):
            continue
        t = tracked.get(r["id"], {})
        (outdir / f"{r['id']}.md").write_text(LETTER.format(
            today=today, post=t.get("post", "?"), department=t.get("department", "?"), district=t.get("district", "?"),
            action_date=t.get("action_date", "?"), source_url=r["source_url"], entity=r["entity"], kind=r["kind"],
            reg=f", {r['reg_no']}" if r["reg_no"] else "", note=r["note"], official_role=r["official_role"],
            register_url=r["register_url"]), encoding="utf-8")
        drafted += 1

    officials = {r["id"] for r in rows}
    as_role = {r["id"] for r in rows if r["official_role"] in ("director", "partner", "trustee", "proprietor") and r["confidence"] == "high"}
    print(f"{len(rows)} entity links for {len(officials)} officials; "
          f"{len(as_role)} officials themselves listed in a register role (high confidence); {drafted} complaint drafts")


if __name__ == "__main__":
    main()
