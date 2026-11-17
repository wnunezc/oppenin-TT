from pathlib import Path
import json,re
from datetime import datetime,timezone,timedelta
out=Path(r'D:\OpsZone\DevWorkspace\Projects\Tech-Test\Oppenin\pruebas\resultados\ronda-1.1\E2E-03-A2')
report=(out/'salida-observada.md').read_text(encoding='utf-8')
ids=re.findall(r'^\| ((?:P|F|I)\d{2}) \|',report,re.M)
expected=[f'P{i:02}' for i in range(1,11)]+[f'F{i:02}' for i in range(1,6)]+[f'I{i:02}' for i in range(1,7)]
assert sorted(ids)==sorted(expected) and len(ids)==21
(out/'validacion.txt').write_text('Verificado automáticamente: 21 controles, cada ID P01-P10, F01-F05 e I01-I06 aparece exactamente una vez en el checklist.\nRevisión manual: estados admitidos, evidencias/motivos, hallazgos y preguntas vinculados al perfil; sin veredicto de prueba.\n',encoding='utf-8')
fin=datetime.now(timezone(timedelta(hours=-5))).isoformat(timespec='milliseconds')
record={
'inicio':(out/'inicio.txt').read_text(encoding='utf-8').strip(),
'fin':fin,
'zona':'America/Panama UTC-05:00',
'fuentes':json.loads((out/'fuentes-sha256.json').read_text(encoding='utf-8')),
'skill':'1.1','perfil':'PEO-01 v1.1',
'modelo':'No expuesto por la herramienta; no se modificó modelo ni configuración.',
'metodo':[
'Primera operación: captura con DateTimeOffset.UtcNow.ToOffset(-05:00) y escritura de inicio.txt antes de leer fuentes.',
'Conservación exacta del mensaje recibido en prompt-recibido.txt. Lectura de solicitud-ia.txt mediante Get-Content -Raw.',
'Lectura íntegra de SKILL.md y PERFIL-EXPEDIENTE.md mediante Get-Content -Raw.',
'Ejecución de extraer.py mediante C:\\Program Files\\WindowsApps\\OpenAI.CodexPrimaryRuntime.v26-1112-737-0_26.1112.737.0_x64__3k8sg7r9htsxt\\dependencies\\python\\python.exe; PdfReader y extract_text() en todas las páginas (1). SHA256 calculado sobre bytes originales con hashlib.sha256.',
'pdftoppm -png -r 120 D:\\OpsZone\\DevWorkspace\\Projects\\Tech-Test\\Oppenin\\pruebas\\entradas\\E2E-03-proforma.pdf D:\\OpsZone\\DevWorkspace\\Projects\\Tech-Test\\Oppenin\\pruebas\\resultados\\ronda-1.1\\E2E-03-A2\\pagina',
'Lectura visual directa de pagina-1.png mediante view_image: única página íntegra, legible. Se contrastó con la extracción; informe conserva transcripción visible de los campos.',
'Informe guardado en salida-observada.md. Validación automática de 21 ID únicos y revisión manual del contenido; después captura de fin con datetime.now en UTC-05:00.'
],
'incidencias':['La extracción pypdf presentó caracteres de reemplazo en palabras acentuadas; se resolvió mediante renderizado local y lectura visual íntegra de la página.','pdftoppm emitió: No display font for Symbol; No display font for ArialUnicode. La imagen se generó y todo el texto esencial resultó legible.'],
'salidas':[str(out/x) for x in ['inicio.txt','prompt-recibido.txt','extraer.py','fuentes-sha256.json','extraccion-propia.txt','pagina-1.png','salida-observada.md','validacion.txt','registro.json']]
}
(out/'registro.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
print('Informe y registro guardados. Checklist validado: 21 controles únicos.')