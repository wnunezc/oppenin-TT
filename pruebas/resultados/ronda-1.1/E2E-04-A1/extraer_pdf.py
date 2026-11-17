from pathlib import Path
from pypdf import PdfReader
root = Path(r'D:\OpsZone\DevWorkspace\Projects\Tech-Test\Oppenin')
out = root / 'pruebas/resultados/ronda-1.1/E2E-04-A1'
pdf = root / 'pruebas/entradas/E2E-04-proforma.pdf'
r = PdfReader(str(pdf))
parts = [f'Archivo: {pdf}\nMétodo: pypdf PdfReader; extract_text() por todas las páginas.\nPáginas: {len(r.pages)}\n']
for n, page in enumerate(r.pages, 1):
    parts.append(f'\n--- PÁGINA {n} ---\n{page.extract_text() or "[SIN TEXTO EXTRAÍDO]"}\n')
text = ''.join(parts)
(out / 'extraccion-pdf.txt').write_text(text, encoding='utf-8')
print(text)