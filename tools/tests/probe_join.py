"""Drives the Have your say page of index.html in headless Chrome and prints one JSON line.
    py tools/tests/probe_join.py
Expect: disabled0=true, two Google Form links with prefilled fields, "Hassan is not done yet", "Kanakapura is done", err=none, SW below 500."""
import pathlib, subprocess, html, re, tempfile
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
src = (pathlib.Path(__file__).resolve().parents[2] / "index.html").read_text(encoding="utf-8")
probe = """<script>addEventListener("error",e=>window.__e=e.message);setTimeout(()=>{let out=[];window.open=u=>out.push(decodeURIComponent(u).slice(0,300));const q=s=>document.querySelector(s);
out.push("disabled0="+q("[data-send=next]").disabled);
q("#jtopics .chip").click();q("#jdist").value="Hassan";q("#jdist").dispatchEvent(new Event("change"));q("[data-send=next]").click();
q("#jfseat").value="Holenarasipur";q("#jfseat").dispatchEvent(new Event("change"));q("#jfwhat .chip:nth-child(2)").click();q("[data-send=field]").click();
q("#jac").value="Hassan";q("#jac").dispatchEvent(new Event("change"));out.push(q("#jacres").textContent);
q("#jac").value="Kanakapura";q("#jac").dispatchEvent(new Event("change"));out.push(q("#jacres").textContent);
out.push("opts="+q("#jac").options.length+"/"+q("#jdist").options.length+" map="+q("#jfmap").textContent.slice(0,70)+" err="+(window.__e||"none")+" on="+q(".page.on").id+" SW="+document.documentElement.scrollWidth);
document.body.setAttribute("data-out",JSON.stringify(out))},3000)</script></body>"""
p = pathlib.Path(tempfile.gettempdir()) / "gb_probe_join.html"
p.write_text(src.replace("</body>", probe), encoding="utf-8")
dom = subprocess.run([CHROME, "--headless=new", "--dump-dom", "--window-size=500,1400", "--virtual-time-budget=8000", p.as_uri() + "#join"],
                     capture_output=True, text=True, encoding="utf-8").stdout
m = re.search(r'data-out="([^"]*)"', dom)
print(html.unescape(m.group(1)) if m else "NO OUTPUT")
p.unlink()
