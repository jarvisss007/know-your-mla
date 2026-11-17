"""Toggles the Kannada switch on index.html in headless Chrome and prints one JSON line.
    py tools/tests/probe_kn.py
Expect: Kannada tab names, chip, label and button; Research card linking a _kn report; English restored with links intact; err=none."""
import pathlib, subprocess, html, re, tempfile
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
src = (pathlib.Path(__file__).resolve().parents[2] / "index.html").read_text(encoding="utf-8")
probe = """<script>addEventListener("error",e=>window.__e=(window.__e||"")+e.message+";");setTimeout(()=>{let out=[];const q=s=>document.querySelector(s);
document.getElementById("lang").click();
out.push("nav="+[...document.querySelectorAll(".nav a")].slice(0,4).map(a=>a.textContent).join("|"));
out.push("chip="+q("#jtopics .chip").textContent+" lbl="+q("label[for=jdist]").textContent+" btn="+q("[data-send=next]").textContent);
out.push("research h3 link="+q("#research .rep h3 a").getAttribute("href")+" "+q("#research .rep h3 a").textContent);
out.push("pager="+q("#join nav.pager").textContent);
q("#jtopics .chip").click(); q("[data-send=next]").disabled||out.push("enabled");
let opened=""; window.open=u=>opened=decodeURIComponent(u); q("[data-send=next]").click(); out.push("msg="+opened.slice(-80));
document.getElementById("lang").click();
out.push("back nav="+q(".nav a").textContent+" lede link="+!!q("#research > p a")+" foot link="+!!q("#join p.fine a")+" chip="+q("#jtopics .chip").textContent+" pressed="+q("#jtopics .chip").getAttribute("aria-pressed"));
out.push("err="+(window.__e||"none")+" SW="+document.documentElement.scrollWidth);
document.body.setAttribute("data-out",JSON.stringify(out))},3000)</script></body>"""
p = pathlib.Path(tempfile.gettempdir()) / "gb_probe_kn.html"
p.write_text(src.replace("</body>", probe), encoding="utf-8")
dom = subprocess.run([CHROME, "--headless=new", "--dump-dom", "--window-size=500,1400", "--virtual-time-budget=8000", p.as_uri() + "#join"],
                     capture_output=True, text=True, encoding="utf-8").stdout
m = re.search(r'data-out="([^"]*)"', dom)
print(html.unescape(m.group(1)) if m else "NO OUTPUT")
p.unlink()
