"""Shared inline-SVG chart: green-cover share on every clean Jan-Mar date, one line per year.
Used by make_rural_page.py and make_page.py. Styling comes from the page's CSS classes
(.grid .ax .ln .pt .pick .lab .s19 .s25 .s26)."""
from datetime import date


def green_chart(rob, pick_dates, label):
    W, H, L, T, Rm, B = 640, 300, 44, 16, 64, 34
    by = {}
    for x in rob:
        if "veg_pct" not in x:
            continue
        d = date.fromisoformat(x["date"])
        by.setdefault(d.year, []).append(((d - date(d.year, 1, 1)).days, x["veg_pct"], x["date"]))
    ymax = max(10, (int(max(v for s in by.values() for _, v, _ in s)) // 10 + 1) * 10)
    sx = lambda doy: L + doy / 89 * (W - L - Rm)
    sy = lambda v: T + (1 - v / ymax) * (H - T - B)
    parts = []
    for g in range(0, ymax + 1, 20 if ymax > 50 else 10):
        parts.append(f'<line x1="{L}" x2="{W-Rm}" y1="{sy(g):.1f}" y2="{sy(g):.1f}" class="grid"/>'
                     f'<text x="{L-6}" y="{sy(g)+4:.1f}" text-anchor="end" class="ax">{g}%</text>')
    for doy, lab in ((0, "1 Jan"), (31, "1 Feb"), (59, "1 Mar"), (89, "31 Mar")):
        parts.append(f'<text x="{sx(doy):.1f}" y="{H-12}" text-anchor="middle" class="ax">{lab}</text>')
    cls = {2019: "s19", 2025: "s25", 2026: "s26"}
    picked = set(pick_dates)
    for yr in sorted(by):
        s = sorted(by[yr])
        pts = " ".join(f"{sx(a):.1f},{sy(v):.1f}" for a, v, _ in s)
        parts.append(f'<polyline points="{pts}" class="ln {cls.get(yr, "")}"/>')
        for a, v, ds in s:
            big = ds in picked
            parts.append(f'<circle cx="{sx(a):.1f}" cy="{sy(v):.1f}" r="{5 if big else 3}" class="pt {cls.get(yr, "")}{" pick" if big else ""}"><title>{ds}: {v:.1f}% green</title></circle>')
    ends = sorted((sy(sorted(by[yr])[-1][1]) + 4, yr) for yr in by)
    for i in range(1, len(ends)):
        if ends[i][0] - ends[i - 1][0] < 16:
            ends[i] = (ends[i - 1][0] + 16, ends[i][1])
    for y, yr in ends:
        parts.append(f'<text x="{W - Rm + 8}" y="{y:.1f}" class="lab {cls.get(yr, "")}">{yr}</text>')
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{label}">' + "".join(parts) + "</svg>"


CHART_CSS = """.chart { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 12px; }
.chart svg { width: 100%; height: auto; display: block; }
.grid { stroke: var(--grid); stroke-width: 1; }
.ax { fill: var(--muted); font: 12px var(--body); }
.ln { fill: none; stroke-width: 2; }
.lab { font: 600 13px var(--body); }
.s19 { stroke: var(--s19); fill: var(--s19); } .s25 { stroke: var(--s25); fill: var(--s25); } .s26 { stroke: var(--s26); fill: var(--s26); }
.ln.s19, .ln.s25, .ln.s26 { fill: none; }
.pt { stroke: var(--surface); stroke-width: 1.5; } .pt.pick { stroke: var(--fg); stroke-width: 2; }"""
