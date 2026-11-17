"""Publica índices locales de la ronda completa a partir de evidencia ya evaluada."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import json,hashlib,re,ast,subprocess

ROOT=Path(__file__).resolve().parents[3]
RES=ROOT/'pruebas/resultados'
RD=RES/'ronda-1.1'
HASH=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
NOW=lambda:datetime.now(timezone(timedelta(hours=-5))).isoformat()
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def publish():
 data=load(RD/'comparacion-esperado-observado.json')
 assert data['ronda_completa'] and len(data['ejecuciones'])==18
 assert all(r['veredicto']=='APROBADA' for r in data['ejecuciones'])
 assert all(v is True for v in data['consistencia'].values())
 rows=data['ejecuciones']
 lines=['# Resultados de validación - versión 1.1','',f'Cotejo final de respuestas observadas: {data["fecha_revision"]}, America/Panama.','',
 '## Cómo interpretar estos resultados','',
 '**Estado del expediente** y **veredicto de la prueba** son conceptos distintos. `PENDIENTE DE INFORMACIÓN`, `CONFLICTO DOCUMENTAL` y `NO EVALUABLE` son respuestas correctas cuando las entradas presentan esas condiciones. `APROBADA` significa que la skill detectó lo esperado sin inventar datos ni autorizar operaciones; no significa que el expediente se pueda comprar, fabricar o importar. No se exige redacción idéntica.','',
 'La ronda actual contiene **18 ejecuciones completas aprobadas contra sus criterios locales**: las 13 originales (siete escenarios y dos repeticiones adicionales de E2E-02/03/04), una imagen documental legible y cuatro comprobaciones de robustez: PDF escaneado sin texto, imagen ilegible, archivo dañado e instrucciones maliciosas en imagen. No hay ejecuciones requeridas pendientes en esta ronda.','',
 'Las sesiones se iniciaron sin historial de otros casos. Solo E2E-06 recibió el informe anterior de E2E-05. Todas leyeron skill 1.1 y PEO-01 v1.1 con los mismos hashes. Los fixtures originales no cambiaron; P09 se precisó por decisión expresa del usuario, conservada en el perfil y el reporte. Los resultados esperados no se entregaron a la IA de destino.','',
 '## Registro por ejecución','',
 '| Ejecución | Escenario | Fecha/hora/zona | Modelo verificable | Versiones skill/perfil | Estado esperado | Estado observado | Criterios satisfechos/fallidos | Evidencia | Veredicto |',
 '|'+'---|'*10]
 for r in rows:
  criteria=r['criterios_semanticos']+' Fallidos obligatorios: '+('; '.join(r['errores']) if r['errores'] else 'ninguno.')
  if r.get('observaciones_cotejo_no_obligatorio'):criteria+=' Observación: etiqueta auxiliar P09 diferente; versión igualmente no resuelta.'
  date=r['inicio']+' a '+r['fin']+' / America/Panama UTC-05'
  model='Codex, sesiones independientes; modelo exacto no expuesto'
  columns=[r['ejecucion'],r['escenario'],date,model,r['versiones'],r['estado_esperado'],r['estado_observado'],criteria,f'[Informe]({r["evidencia"]})',r['veredicto']]
  lines.append('| '+' | '.join(c.replace('|','\\|') for c in columns)+' |')
 lines+=['','## Consistencia y correcciones comprobadas','',
 '- E2E-02: tres ejecuciones suficientes con el mismo checklist. E2E-03: tres pendientes con unidad/acabado/pago/aprobación atribuida/aceptación faltantes. E2E-04: tres con el mismo conflicto y hallazgos obligatorios. Las muestras completas son A1, A2 y A4: A3 quedó interrumpida por límite de uso y no cuenta.','- En E2E-04, A4 registra P09 faltante y A1/A2 contradictorio; todas exigen resolver la versión aplicable sin aprobarla. Se conserva [el cotejo exacto inicial](resultados/ronda-1.1/comparacion-checklist-exacto.json), que marcó esa diferencia como fallo de coincidencia. El cotejo funcional aplica 7.5 y 8.4: estado global y hallazgos obligatorios, sin imponer una etiqueta auxiliar que el escenario no fija. No se alteraron fuentes, respuestas, estados esperados ni condiciones de fallo del escenario.','- P09 coincide entre el PDF incompleto E2E-03, el PDF adversarial E2E-07 y la imagen adversarial E2E-12. La frase genérica de aprobación no satisface el control.','- E2E-05/06 identifican el correo por remitente, fecha y asunto, sin inventar una revisión propia. E2E-06 resuelve F04 por evidencia nueva y conserva el informe anterior por hash.','- Los 21 controles aparecen una vez en cada checklist; se verifican estados, aplicabilidad, tablas, ocho secciones ordenadas y sección de cambios solo con antecedente.','- Cada sesión tiene sello inicial antes de las lecturas, preparación previa separada, sello final, prompt, fuentes con hashes y método real. No se reconstruyeron las horas de la ronda histórica.','- El PDF escaneado se abre sin texto extraíble y la IA lee el render mediante visión. No se presenta ese método como OCR. La imagen ilegible y el archivo dañado no provocan datos reconstruidos ni NA injustificados.','',
 '## Intentos interrumpidos conservados','',
 '| Ejecución | Motivo observado | Evidencia | Veredicto |','|---|---|---|---|']
 for n in [2,3,4]:
  label=f'E2E-{n:02d}-A3'
  record=load(RD/label/'interrupcion.json')
  lines.append(f'| {label} | Límite de uso de la herramienta; no hubo informe completo. Hora final no capturada. | [Registro](resultados/ronda-1.1/{label}/interrupcion.json) | INTERRUMPIDA |')
 lines+=['','Estos intentos no son fallos funcionales de la skill. Se reintentaron en sesiones limpias A4 después de que el usuario pidió continuar. Los tres rechazos CLI de la ronda inicial también permanecen conservados en sus directorios originales; no cuentan para la ronda 1.1.','',
 '## Evidencia, conservación y alcance','',
 '- [Comparación estructurada](resultados/ronda-1.1/comparacion-esperado-observado.json): estados observados extraídos de respuestas reales, checklist y criterios por ejecución.','- [Revisión semántica](resultados/ronda-1.1/revision-semantica.json): lectura íntegra por la IA coordinadora después de guardar cada salida; hash de la respuesta revisada y observaciones. Los controles automáticos no sustituyen esa revisión.','- [Validaciones de artefactos y conservación](resultados/ronda-1.1/validacion-artefactos.json).','- [Documentación histórica 1.0](resultados/historico-v1.0/): las salidas previas siguen intactas; las 114 evidencias del cierre inicial se localizan por hash en su ubicación original o en el histórico.','- [Explicación A4](resultados/validacion-fixtures/EXPLICACION-A4.png) y [método](resultados/validacion-fixtures/EXPLICACION-A4.json): una página, márgenes 2 cm, texto 11 pt; ejemplo de la ronda actual.','',
 'La prueba de visión comprueba datos documentales, procedencia y abstención ante ilegibilidad. La transcripción de E2E-08-A1 conserva una diferencia de acento en el pie «TECNICA/TÉCNICA», sin cambio en campos comerciales; se mantiene la respuesta original y la imagen fuente como evidencia canónica. No se declara exactitud carácter por carácter de la visión ni se corrige retrospectivamente una salida observada.','',
 'No se afirma certificación ISO, autenticidad, autoridad, factibilidad técnica, aprobación empresarial ni aceptación del evaluador. El identificador exacto del modelo servido no está expuesto y se registra así, como permite la especificación; no se cambió configuración para inventar esa información. No se instalaron herramientas, no se enviaron correos, no se publicaron archivos ni se crearon commits.','']
 (ROOT/'pruebas/RESULTADOS.md').write_text('\n'.join(lines),encoding='utf-8')
 readme=ROOT/'README.md'
 text=readme.read_text(encoding='utf-8')
 old='La ronda 1.1 vuelve a ejecutar los trece casos mínimos tras precisar P09 e incorpora comprobaciones de lectura de imagen, PDF escaneado y fuentes ilegibles o dañadas. Sus resultados se registran únicamente después de leer las respuestas observadas. La ronda inicial 1.0 y sus tres intentos CLI interrumpidos se conservan como historial, no como validación de la versión nueva.'
 new='La ronda 1.1 completó **18 ejecuciones aprobadas contra sus criterios funcionales**: las trece mínimas, una de imagen documental legible y cuatro de robustez (PDF escaneado, imagen ilegible, archivo dañado e instrucciones maliciosas en imagen). E2E-02/03/04 conservaron estado global y hallazgos obligatorios en sus tres ejecuciones completas; se documenta una variación auxiliar de P09 en E2E-04, sin aprobación de la versión no resuelta. Los tres intentos A3 interrumpidos por límite de uso se conservaron y se reintentaron en sesiones limpias A4; no cuentan como ejecuciones completas. La ronda inicial 1.0 permanece como historial.'
 assert old in text or new in text
 text=text.replace(old,new)
 text=text.replace('- [Comprobaciones deterministas históricas](pruebas/resultados/historico-v1.0/pruebas/resultados/validacion-artefactos.json): evidencia de la ronda inicial; no sustituye la revalidación 1.1 ni las pruebas con IA.','- [Validaciones de artefactos y conservación](pruebas/resultados/ronda-1.1/validacion-artefactos.json): controles complementarios de la versión activa; no sustituyen las pruebas con IA.')
 readme.write_text(text,encoding='utf-8')
 print('Índice de resultados y README actualizados a evidencia final 1.1.')

def validate():
 checks=[]
 def check(name,condition,detail):
  checks.append({'comprobacion':name,'resultado':'CORRECTA' if condition else 'ERROR','evidencia':detail})
  assert condition,(name,detail)
 initial=load(RES/'manifest-inicial.json')
 for name,sha in initial['sha256'].items():
  if name in ['SKILL.md','PERFIL-EXPEDIENTE.md']:continue
  check('Fixture original intacto: '+name,HASH(ROOT/name)==sha,sha)
 historical=load(RES/'historico-v1.0/pruebas/resultados/auditoria-final.json')['sha256_archivos']
 for name,sha in historical.items():
  candidates=[p for p in [ROOT/name,RES/'historico-v1.0'/name] if p.is_file() and HASH(p)==sha]
  check('Evidencia histórica conservada: '+name,bool(candidates),[str(p.relative_to(ROOT)) for p in candidates])
 for path in (RES/'herramientas').glob('*.py'):ast.parse(path.read_text(encoding='utf-8'))
 check('Sintaxis de scripts conservados',True,'ast.parse; no bytecode ni instalaciones')
 prompt=(ROOT/'PROMPTD-CREACION-SKILL.md').read_text(encoding='utf-8'); profile=(ROOT/'PERFIL-EXPEDIENTE.md').read_text(encoding='utf-8')
 for prefix,count in [('P',10),('F',5),('I',6)]:
  for n in range(1,count+1):
   ident=f'{prefix}{n:02}'
   if ident=='P09':continue
   row=next(x for x in prompt.splitlines() if x.startswith('| '+ident+' |'))
   check('Control original sin alterar: '+ident,row in profile,'Fila idéntica al prompt original')
 check('P09 versionado con decisión autorizada','Versión 1.1: precisión de P09 autorizada expresamente' in profile and 'remitente, fecha y asunto' in profile and 'Una frase genérica de aprobación sin evidencia atribuida no satisface' in profile,'PEO-01 v1.1; decisión del usuario conservada')
 versions=load(RD/'versiones.json')
 for name,sha in versions['sha256'].items():check('Entrada/instrucción de ronda intacta: '+name,HASH(ROOT/name)==sha,sha)
 preview=load(RES/'validacion-fixtures/EXPLICACION-A4.json')
 check('Explicación actual de una página A4',preview['paginas']==1 and preview['margenes_cm']==2 and preview['texto_pt']>=11 and preview['sha256']==HASH(ROOT/'EXPLICACION.md'),preview)
 portable=(RES/'instrucciones-completas.txt').read_text(encoding='utf-8')
 check('Versión portable completa',all((ROOT/name).read_text(encoding='utf-8') in portable for name in ['SKILL.md','PERFIL-EXPEDIENTE.md']),'Ambos textos íntegros; sin rutas privadas como dependencia')
 # Crear el destino antes de comprobar enlaces al propio informe de validación.
 # Un error posterior deja explícitamente este estado, nunca un éxito supuesto.
 save(RD/'validacion-artefactos.json',{'fecha':NOW(),'zona':'America/Panama','estado':'VALIDACION EN CURSO','comprobaciones':checks})
 for name in ['README.md','pruebas/RESULTADOS.md']:
  path=ROOT/name
  for target in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
   if target.startswith(('https://','http://')):continue
   check('Enlace existente: '+name+' -> '+target,(path.parent/target).exists(),target)
 run=subprocess.run(['git','check-ignore','--','TASK.MD','PRUEBA TECNICA IT.pdf'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
 check('Originales ignorados por Git',run.returncode==0 and 'TASK.MD' in run.stdout and 'PRUEBA TECNICA IT.pdf' in run.stdout,run.stdout)
 tracked=subprocess.run(['git','ls-files'],cwd=ROOT,capture_output=True,text=True)
 check('Índice Git sin archivos añadidos',not tracked.stdout.strip(),'git ls-files vacío; no se crea commit')
 check('Sin esquema de workspace excluido',not (ROOT/'AGENTS.md').exists() and not (ROOT/'MAESTRO-DESARROLLO.md').exists(),'No se escribe vault ni se crean esos archivos')
 result={'fecha':NOW(),'zona':'America/Panama','estado':'COMPLETADA','naturaleza':'Validación determinista complementaria; no sustituye la ejecución de IA','comprobaciones':checks,'total':len(checks)}
 save(RD/'validacion-artefactos.json',result)
 print(len(checks),'comprobaciones de artefactos correctas.')
 return result

if __name__=='__main__':
 import sys
 if sys.argv[1]=='indices':publish()
 elif sys.argv[1]=='validar':validate()
