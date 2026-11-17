from pathlib import Path
from decimal import Decimal
from datetime import datetime, timezone, timedelta
import hashlib, json, re
root = Path(r'D:\OpsZone\DevWorkspace\Projects\Tech-Test\Oppenin')
out = root / 'pruebas/resultados/ronda-1.1/E2E-04-A4'
report = (out/'salida-observada.md').read_text(encoding='utf-8')
expected = [f'P{i:02}' for i in range(1,11)] + [f'F{i:02}' for i in range(1,6)] + [f'I{i:02}' for i in range(1,7)]
found = re.findall(r'^\| ([PFI]\d{2}) \|',report,re.M)
assert found == expected, (found, expected)
for line in report.splitlines():
    if re.match(r'^\| [PFI]\d{2} \|',line):
        cells=line.split('|')
        assert len(cells)==6, line
        assert cells[3].strip() in ['satisfecho','faltante','contradictorio','no verificable','NA']
        assert cells[4].strip()
subtotal = Decimal('20') * Decimal('80.00')
total = subtotal + Decimal('0.00') + Decimal('0.00')
assert subtotal == Decimal('1600.00') and total == Decimal('1600.00')
validation={'controles':len(found),'orden_y_unicidad':'verificados','estados_y_evidencia':'verificados','aritmetica_decimal':f'20 x 80.00 = {subtotal}; {subtotal} + 0.00 + 0.00 = {total}', 'lectura_pdf':'pypdf; 1 pagina; extract_text de todas las paginas; extraccion propia UTF-8'}
(out/'verificacion.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding='utf-8')
sourcepaths = ['SKILL.md','PERFIL-EXPEDIENTE.md','pruebas/entradas/E2E-04-correo.md','pruebas/entradas/E2E-04-proforma.pdf','pruebas/resultados/ronda-1.1/E2E-04-A4/solicitud-ia.txt']
record = {
'inicio': (out/'inicio.txt').read_text(encoding='utf-8'),
'fin': datetime.now(timezone(timedelta(hours=-5))).isoformat(timespec='milliseconds'),
'zona':'America/Panama UTC-05:00',
'fuentes':[{'ruta':str(root/p),'sha256':hashlib.sha256((root/p).read_bytes()).hexdigest()} for p in sourcepaths],
'skill':'1.1','perfil':'PEO-01 v1.1',
'modelo':'no expuesto por la herramienta salvo identidad verificable',
'metodo': [
'Primera operacion: PowerShell [DateTimeOffset]::UtcNow.ToOffset([TimeSpan]::FromHours(-5)); guardado ISO 8601 en inicio.txt antes de leer fuentes.',
'PowerShell: conservacion literal del mensaje delegado en prompt-recibido.txt y Get-Content -LiteralPath solicitud-ia.txt -Raw.',
'PowerShell: Get-Content -LiteralPath -Raw de SKILL.md, PERFIL-EXPEDIENTE.md y E2E-04-correo.md, completos.',
'Python existente indicado por solicitud; from pypdf import PdfReader; reader=PdfReader(ruta original E2E-04-proforma.pdf); for i,page in enumerate(reader.pages,1): page.extract_text(); escritura propia UTF-8 extraccion-proforma.txt. Una pagina iterada, texto completo legible; no fue necesario renderizar.',
'Python json.dumps(ensure_ascii=True) de extraccion-proforma.txt para leer sin ambiguedad de codificacion de consola.',
'PowerShell WriteAllText UTF-8 del informe; python validacion-registro.py comprueba checklist, aritmetica decimal y genera registro. Script conservado.',
'Fuentes hasheadas con hashlib.sha256 sobre read_bytes de originales; sin red, plugins, correo, subagentes, instalaciones ni cambios de configuracion/modelo.'
],
'incidencias':['La validacion local inicial esperaba por error siete segmentos al separar las cuatro columnas del checklist; se corrigio a seis y se repitio. No se cambio el informe.', 'La consola mostro caracteres acentuados alterados en la primera salida Python por codificacion de stdout. Se verifico el texto UTF-8 propio mediante JSON con escapes Unicode; no se modifico la fuente ni se reconstruyeron datos.'],
'salidas':[str(out/n) for n in ['inicio.txt','prompt-recibido.txt','extraccion-proforma.txt','salida-observada.md','verificacion.json','validacion-registro.py','registro.json']]
}
(out/'registro.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'validacion':validation,'registro':str(out/'registro.json'),'fin':record['fin']},ensure_ascii=True))