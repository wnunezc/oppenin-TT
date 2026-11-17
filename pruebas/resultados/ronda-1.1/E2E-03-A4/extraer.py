from pathlib import Path
from pypdf import PdfReader
import json, hashlib
base=Path(r'D:\OpsZone\DevWorkspace\Projects\Tech-Test\Oppenin')
out=base/'pruebas/resultados/ronda-1.1/E2E-03-A4'
sources=[base/'SKILL.md',base/'PERFIL-EXPEDIENTE.md',base/'pruebas/entradas/E2E-03-proforma.pdf']
reader=PdfReader(sources[-1])
pages=[]
for n,p in enumerate(reader.pages,1):
    value=p.extract_text()
    pages.append({'pagina':n,'texto':value})
    print(f'=== PAGINA {n} ===\n{value}')
(out/'extraccion-pypdf.json').write_text(json.dumps({'metodo':'pypdf.PdfReader; extract_text() de todas las paginas','paginas':pages},ensure_ascii=False,indent=2),encoding='utf-8')
(out/'fuentes-sha256.json').write_text(json.dumps([{'ruta':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources],ensure_ascii=False,indent=2),encoding='utf-8')
print('TOTAL PAGINAS:',len(pages))
