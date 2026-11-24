"""Serve satellite maps as WebP (about 65% smaller) with the PNG kept as a fallback.

    from webp_images import webpify; webpify(html_path)
For every <img src="X.png"> in the page whose PNG sits next to it, writes X.webp (quality 80) and wraps the
<img> in <picture><source srcset="X.webp" type="image/webp">...</picture>. Adds loading="lazy" and the image's
width/height so the page doesn't jump while images load. Safe to run twice.
"""
import pathlib, re
from PIL import Image


def webpify(html_path):
    page = pathlib.Path(html_path)
    t = page.read_text(encoding="utf-8")
    t = re.sub(r"<picture><source srcset=\"[^\"]+\.webp\" type=\"image/webp\">(<img [^>]*>)</picture>", r"\1", t)  # undo a previous run

    def wrap(m):
        tag, src = m.group(0), m.group(1)
        png = page.parent / src
        if not png.exists():
            return tag
        webp = png.with_suffix(".webp")
        im = Image.open(png)
        if not webp.exists() or webp.stat().st_mtime < png.stat().st_mtime:
            im.save(webp, "WEBP", quality=80, method=6)
        if "loading=" not in tag:
            tag = tag.replace("<img ", f'<img loading="lazy" width="{im.width}" height="{im.height}" ', 1)
        return f'<picture><source srcset="{src[:-4]}.webp" type="image/webp">{tag}</picture>'

    t = re.sub(r'<img [^>]*src="([^"/:]+\.png)"[^>]*>', wrap, t)
    page.write_text(t, encoding="utf-8", newline="\n")
