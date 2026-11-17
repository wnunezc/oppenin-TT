@'
from pathlib import Path
from pypdf import PdfReader
r=PdfReader(str(Path.cwd()/'pruebas/entradas/E2E-02-proforma.pdf'))
s='\n\n'.join(f'=== PÁGINA {n} ===\n'+p.extract_text() for n,p in enumerate(r.pages,1))
(Path.cwd()/'pruebas/resultados/E2E-02-S3/extraccion-propia.txt').write_text(s,encoding='utf-8')
print(s)
'@ | & 'C:\Program Files\WindowsApps\OpenAI.CodexPrimaryRuntime.v26-1112-737-0_26.1112.737.0_x64__3k8sg7r9htsxt\dependencies\python\python.exe' -X utf8 -