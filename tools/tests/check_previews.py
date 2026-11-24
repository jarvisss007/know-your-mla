"""Check that every published page has a share preview: <title>, meta description, og:title, og:description, og:image.

    py tools/tests/check_previews.py
Lists pages missing any of them (WhatsApp and X show a bare link without these), grouped by what is missing.
"""
import collections, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKIP_DIRS = {"research", "video", ".git", "content", "cards", "node_modules"}
NEED = {
    "title": r"<title>\s*\S",
    "description": r'<meta\s+name="description"\s+content="\s*\S',
    "og:title": r'<meta\s+property="og:title"\s+content="\s*\S',
    "og:description": r'<meta\s+property="og:description"\s+content="\s*\S',
    "og:image": r'<meta\s+property="og:image"\s+content="https?://\S',
}
missing = collections.defaultdict(list)
pages = [p for p in ROOT.rglob("*.html") if not (SKIP_DIRS & set(p.relative_to(ROOT).parts))]
for p in pages:
    head = p.read_text(encoding="utf-8", errors="ignore").split("</head>")[0]
    for k, rx in NEED.items():
        if not re.search(rx, head, re.I):
            missing[k].append(str(p.relative_to(ROOT)))
bad = sorted({x for v in missing.values() for x in v})
print(f"{len(pages)} pages, {len(bad)} with an incomplete share preview")
for k, v in missing.items():
    print(f"  missing {k}: {len(v)}")
    for x in sorted(v)[:40]:
        print("    ", x)
