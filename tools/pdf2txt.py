import sys
try:
    import pypdf
    r = pypdf.PdfReader(sys.argv[1])
    t = "\n".join((p.extract_text() or "") for p in r.pages)
except ImportError:
    import fitz
    d = fitz.open(sys.argv[1]); t = "\n".join(p.get_text() for p in d)
open(sys.argv[2], "w", encoding="utf-8").write(t)
print(len(t))
