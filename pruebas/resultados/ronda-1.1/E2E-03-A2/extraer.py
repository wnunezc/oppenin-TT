from pathlib import Path
from pypdf import PdfReader
import hashlib,json
root=Path(r'D:\OpsZone\DevWorkspace\Projects\Tech-Test\Oppenin')
out=root/'pruebas/resultados/ronda-1.1/E2E-03-A2'
paths=[root/'SKILL.md',root/'PERFIL-EXPEDIENTE.md',root/'pruebas/entradas/E2E-03-proforma.pdf']
hashes=[{'ruta':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]
(out/'fuentes-sha256.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2),encoding='utf-8')
r=PdfReader(str(paths[-1]))
pages=[]
for i,p in enumerate(r.pages,1):
    t=p.extract_text()
    pages.append(f'=== PAGINA {i} ===\n{t}')
text='\n\n'.join(pages)
(out/'extraccion-propia.txt').write_text(text,encoding='utf-8')
print('PAGINAS:',len(r.pages))
print(text)