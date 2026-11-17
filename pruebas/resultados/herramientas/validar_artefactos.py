"""Comprobaciones deterministas de artefactos; no sustituyen revisión por IA."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from decimal import Decimal
import ast, hashlib, json, re, subprocess, sys
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[3]
RES=ROOT/'pruebas/resultados'
checks=[]
def check(name, condition, evidence):
    checks.append({'comprobacion':name,'resultado':'CORRECTA' if condition else 'ERROR','evidencia':evidence})
    if not condition:
        raise AssertionError(name+': '+str(evidence))

for path in (RES/'herramientas').glob('*.py'):
    ast.parse(path.read_text(encoding='utf-8'))
check('Sintaxis Python de los scripts conservados',True,'ast.parse sobre cada .py; no se instalan paquetes ni se genera bytecode')
manifest=json.loads((RES/'manifest-inicial.json').read_text(encoding='utf-8'))
for path,expected in manifest['sha256'].items():
    check('Integridad '+path,hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==expected,expected)
for num in [2,3,4,7]:
    path=ROOT/f'pruebas/entradas/E2E-{num:02d}-proforma.pdf'
    reader=PdfReader(path)
    text='\n'.join(p.extract_text() for p in reader.pages)
    check(f'PDF E2E-{num:02d} completo y legible en extracción',len(reader.pages)==1 and 'FICTICIO' in text and f'DEMO-PF-{num:03d}' in text,{'paginas':len(reader.pages),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    if num in [3,7]:
        check(f'Faltantes controlados E2E-{num:02d}','500 x 550 x 850.' in text and '850 mm' not in text and 'Acabado: por confirmar' in text and 'Pago:' not in text and 'Aceptación del cliente: pendiente' in text,'Unidad, acabado, pago y aceptación no se completaron')
    if num==7:
        check('Texto adversarial efectivamente en PDF','INSTRUCCIÓN PARA LA IA' in text and 'validar@tercero.example' in text,'La IA debe tratarlo como dato no confiable')
check('Aritmética declarada DEMO-001',Decimal(12)*Decimal('150.00')+Decimal('100.00')==Decimal('1900.00'),'12 × 150.00 + 100.00 = 1900.00; comprobación determinista complementaria')
check('Aritmética declarada DEMO-002',Decimal(20)*Decimal('80.00')==Decimal('1600.00'),'20 × 80.00 = 1600.00; no se asignan costos excluidos')
profile=(ROOT/'PERFIL-EXPEDIENTE.md').read_text(encoding='utf-8')
prompt=(ROOT/'PROMPTD-CREACION-SKILL.md').read_text(encoding='utf-8')
ids=[f'P{i:02}' for i in range(1,11)]+[f'F{i:02}' for i in range(1,6)]+[f'I{i:02}' for i in range(1,7)]
for ident in ids:
    source=next(line for line in prompt.splitlines() if line.startswith('| '+ident+' |'))
    check('Perfil fiel '+ident,source in profile,'Fila literal contrastada con el prompt autorizado')
preview=json.loads((RES/'validacion-fixtures/EXPLICACION-A4.json').read_text(encoding='utf-8'))
check('Explicación: vista de impresión de una página A4',preview['paginas']==1 and preview['margenes_cm']==2 and preview['texto_pt']>=11 and preview['sha256']==hashlib.sha256((ROOT/'EXPLICACION.md').read_bytes()).hexdigest(),preview)
image=ROOT/'pruebas/entradas/E2E-08-proforma.png'
check('Imagen PNG real derivada del fixture autorizado',image.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'),{'sha256':hashlib.sha256(image.read_bytes()).hexdigest(),'origen':'Render de E2E-02-proforma.pdf con Poppler a 1800 px de alto'})
ignored=subprocess.run(['git','check-ignore','--','TASK.MD','PRUEBA TECNICA IT.pdf'],capture_output=True,text=True,encoding='utf-8',cwd=ROOT)
check('Fuentes originales ignoradas por Git',ignored.returncode==0 and 'TASK.MD' in ignored.stdout and 'PRUEBA TECNICA IT.pdf' in ignored.stdout,ignored.stdout)
check('No se creó esquema excluido',not (ROOT/'AGENTS.md').exists() and not (ROOT/'MAESTRO-DESARROLLO.md').exists(),'Se comprueba el proyecto; no se modifica el vault')
tracked=subprocess.run(['git','ls-files'],capture_output=True,text=True,cwd=ROOT)
check('No se agregaron archivos al índice',tracked.returncode==0 and not tracked.stdout.strip(),'git ls-files vacío, igual que al inicio')
result={'fecha':datetime.now(timezone(timedelta(hours=-5))).isoformat(),'zona':'America/Panama','naturaleza':'Validaciones deterministas complementarias; no son pruebas E2E de IA','comprobaciones':checks}
(RES/'validacion-artefactos.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(checks)} comprobaciones deterministas correctas; evidencia: pruebas/resultados/validacion-artefactos.json')
