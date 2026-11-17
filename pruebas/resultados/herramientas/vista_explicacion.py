"""Vista de impresión A4 del contenido Markdown simple; PDF solo en memoria."""
from pathlib import Path
from io import BytesIO
from datetime import datetime, timezone, timedelta
import json, subprocess, hashlib
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[3]
source=ROOT/'EXPLICACION.md'
text=source.read_text(encoding='utf-8')
style=ParagraphStyle('Texto',fontName='Helvetica',fontSize=11,leading=15,spaceAfter=10)
heading=ParagraphStyle('Titulo',fontName='Helvetica-Bold',fontSize=16,leading=20,spaceAfter=16)
parts=text.strip().split('\n\n')
story=[]
for part in parts:
    title=part.startswith('# ')
    content=part[2:] if title else part
    story.append(Paragraph(escape(' '.join(content.splitlines())),heading if title else style))
buf=BytesIO()
SimpleDocTemplate(buf,pagesize=A4,leftMargin=2*cm,rightMargin=2*cm,topMargin=2*cm,bottomMargin=2*cm).build(story)
payload=buf.getvalue()
reader=PdfReader(BytesIO(payload))
assert len(reader.pages)==1, f'La explicación ocupa {len(reader.pages)} páginas'
target=ROOT/'pruebas/resultados/validacion-fixtures/EXPLICACION-A4'
result=subprocess.run(['pdftoppm','-png','-singlefile','-scale-to','1300','-',str(target)],input=payload,capture_output=True)
assert result.returncode==0,result.stderr.decode(errors='replace')
evidence={'fecha':datetime.now(timezone(timedelta(hours=-5))).isoformat(),'zona':'America/Panama','fuente':'EXPLICACION.md','sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'paginas':len(reader.pages),'formato':'A4 210 x 297 mm','margenes_cm':2,'texto_pt':11,'interlineado_pt':15,'titulo_pt':16,'metodo':'ReportLab: composición completa del texto a A4; PDF transitorio en memoria, pypdf cuenta páginas, Poppler stdin genera vista PNG. No se guarda PDF adicional.','vista':'pruebas/resultados/validacion-fixtures/EXPLICACION-A4.png','stderr_poppler':result.stderr.decode(errors='replace')}
target.with_suffix('.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(evidence,ensure_ascii=False))
