import sys
from pypdf import PdfReader
r=PdfReader(sys.argv[1])
out=open(sys.argv[2],'w',encoding='utf-8')
for i,p in enumerate(r.pages):
    out.write(f"\n=== PAGE {i+1} ===\n"+(p.extract_text() or ""))
print(len(r.pages))
