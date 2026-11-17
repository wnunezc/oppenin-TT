# Reporte de creación con IA - versión inicial

Actualización de la preparación: **2026-11-17T13:26:18.929651-05:00, America/Panama (UTC-05:00)**. Identificación de la entrega: **versión inicial**.

## Corrección de identificación

Registro de esta precisión nominal: **2026-11-17T13:31:36.059167-05:00, America/Panama (UTC-05:00)**.

Por instrucción posterior del usuario, todos los cambios, revisiones y pruebas de este desarrollo pertenecen a una única versión inicial. Las etiquetas numéricas usadas durante el trabajo se conservan solo en evidencias, rutas y scripts históricos para no alterar lo ocurrido; no acreditan versiones liberadas ni versionado en Git. Se corrigió la identificación de la documentación activa y del texto portable, sin cambiar controles, fixtures, resultados o aprobaciones. No se repitieron pruebas funcionales. Las instrucciones probadas se conservan por sus bytes y hashes originales en `pruebas/resultados/correccion-identificacion/entradas-conservadas/`.

## Objetivo y fuentes

Se creó el Revisor de expedientes de mobiliario como instrucciones reutilizables para revisar integridad y coherencia documental antes de compra, fabricación o importación. La propuesta no afirma problemas internos comprobados de Oppenin ni inventa sus sistemas, responsables o aprobaciones.

Se leyeron completamente y en el orden solicitado el PDF original, TASK.MD y PROMPTD-CREACION-SKILL.md antes de crear archivos. El enunciado exige skill compartible, explicación de una página y reporte generado con IA. El perfil, los escenarios y sus repeticiones son alcance complementario autorizado, no requisitos atribuidos al PDF original. La recepción de imágenes fue autorizada después por el usuario.

TASK.MD y el PDF original estuvieron ignorados por Git durante la preparación inicial. Posteriormente el usuario autorizó incluir todos los archivos, también los excluidos, sin crear todavía el commit: se retiraron esas exclusiones y se prepararon los archivos en el índice. El prompt original se conserva sin alterarlo: la precisión posterior de P09 se documenta como decisión del usuario en el perfil de la versión inicial. No se crea AGENTS.md, MAESTRO-DESARROLLO.md ni documentación del vault.

## Fechas, herramientas y modelo

- Inicio real observado: **2026-11-17 12:18:28 America/Panama**, obtenido de clock.curr_time (17:18:28 UTC). La primera persistencia fue posterior a las lecturas exigidas; se distingue del inicio observado.
- Creación inicial de skill, perfil y fixtures: evento de finalización **2026-11-17T12:21:43.142309-05:00**. No se confunde con las fechas ficticias de los documentos.
- Inicio registrado de corrección y conservación previa: **2026-11-17T12:57:52.009537-05:00**. La ronda nueva conserva preparación, primer sello antes de lecturas y fin por cada sesión en sus registros; no se reconstruyen horas históricas faltantes.
- Autoría y evaluaciones: Codex con IA, aplicación de escritorio y sesiones independientes de subagentes. El identificador exacto del modelo servido y la versión de la aplicación no están expuestos por la herramienta. No se eligió otro modelo ni se alteró configuración durante las pruebas.
- Intentos iniciales: Codex CLI **0.136.0**, configuración existente observada gpt-6.1-sol/medium, rechazada por el servicio con la autenticación existente de ChatGPT. Esa selección no se presenta como modelo servido de las pruebas completas.
- Herramientas existentes: bundle **26.1112.11217**, Python **3.12.14**, ReportLab **4.4.9**, pypdf **6.21.4**, Poppler; Python del sistema con Pillow **12.3.0** y PyYAML **6.0.3**. No se instalaron herramientas.
- Se aplicaron las skills locales skill-creator y pdf. La skill creada no se instaló globalmente.

## Decisiones y prompts conservados

El prompt de desarrollo completo permanece en [PROMPTD-CREACION-SKILL.md](PROMPTD-CREACION-SKILL.md). La autorización inicial ordenó implementar y validar sin publicar, enviar correo o crear commits. El usuario autorizó después que cada IA abriera el PDF real por ruta local, dado que la CLI no admitía adjunto PDF nativo, y pidió soporte para imágenes.

Tras la evaluación se identificó la tensión de P09: exigía revisión de cada documento, pero los correos de fabricación no declaran revisión propia. Se consultó al usuario si autorizaba identificar correos por remitente, fecha y asunto y exigir revisión a documentos controlados, con evidencia atribuida de aprobación. Respuesta literal: **«Sí, precisar P09 y conservar los fixtures originales»**. PEO-01 (versión inicial) registra esa precisión; no se inventaron revisiones de correo ni se alteraron los fixtures para obtener suficiencia.

Otra aclaración del usuario fue que los casos con información faltante o contradictoria deben demostrar la detección y que las respuestas no tienen que ser idénticas. Por eso se separa el estado del expediente del veredicto de la prueba.

Activación real de la ronda de revalidación: cada subagente se creó con contexto limpio, capturó hora antes de leer fuentes, leyó su solicitud, SKILL.md, PERFIL-EXPEDIENTE.md y solo las entradas enumeradas. La solicitud pide: «Revisa este expediente en la etapa indicada y entrega tu informe documental», prohíbe completar datos o ejecutar acciones externas y no contiene resultados esperados. Solo E2E-06 recibe el informe anterior de E2E-05 de la misma ronda. Se conservan el mensaje recibido, solicitud completa, fuentes con SHA256 y métodos/comandos de lectura en cada directorio de [ronda de revalidación](pruebas/resultados/ronda-1.1/).

## Trabajo realizado

1. Se inspeccionaron archivos y Git. El repositorio no tenía commits ni archivos rastreados; .gitignore ya excluía TASK.MD y el PDF fuente y no se modificó.
2. Se crearon las primeras instrucciones, perfil y los correos/fichas y cuatro proformas PDF autorizados, con marca visible ficticia y correos .example. Los PDF se reabrieron, cotejaron con los bloques originales y renderizaron para inspección visual.
3. La primera ronda completó trece ejecuciones originales más una de imagen. Sus respuestas, discrepancias y documentos se conservan; no se reutilizan como validación del estado corregido de las instrucciones.
4. Antes de corregir se copiaron los documentos previos a las precisiones al [histórico](pruebas/resultados/historico-v1.0/). Las 114 evidencias del cierre original se conservan por hash en su ruta original o en ese histórico. La vista A4 antigua se recuperó idéntica por hash antes de cerrar la conservación, separada de la vista actual.
5. Se incorporaron las precisiones: P09 explícito; lectura visual de PDF sin texto; abstención ante ilegibilidad; tablas sin columnas accidentales; sin bloqueantes por costos excluidos o fechas ficticias futuras. Las instrucciones precisan estados y procedencia sin imponer redacción idéntica.
6. Se mantuvieron los fixtures originales y se agregaron derivaciones controladas: un PDF de imagen de la proforma completa, una imagen deliberadamente ilegible, un archivo deliberadamente truncado y un PNG de la proforma con instrucciones maliciosas. No se agregaron datos comerciales. El truncado es un caso negativo, no se presenta como PDF válido.
7. Se ejecutó una ronda nueva completa con la misma skill/perfil. La coordinadora leyó cada respuesta antes de cotejarla, conservó su hash y registró la revisión semántica por separado. El cotejo automático extrae el estado observado y los controles; no rellena el observado con el esperado.
8. Se actualizaron guía, README, instrucciones completas portables, explicación y tabla de resultados. No se modificaron informes observados después de compararlos.

## Problemas reales y tratamiento

- La primera lectura del PDF fuente falló por cp1252; stdout UTF-8 permitió extraer y leer su página completa antes de continuar. Durante algunas pruebas reaparecieron problemas de representación de acentos en consola; se conservó la extracción y se usó relectura UTF-8 o visión del render, registrando el método real.
- PyMuPDF no estaba disponible: se utilizó Poppler existente. El Python del bundle carecía de yaml: el validador de skills se ejecutó con Python/PyYAML ya disponibles en el sistema. Poppler emitió advertencias de fuentes, pero las páginas generadas fueron legibles.
- La CLI rechazó el modelo configurado en tres intentos iniciales. Se conservaron como INTERRUMPIDA y se usaron sesiones nativas independientes, sin cambiar configuración ni simular informes.
- En la ronda inicial algunas horas se capturaron después de las lecturas; esa limitación permanece en sus registros. Se resolvió para la validación activa con nuevos sellos previos a lecturas en todas las sesiones, sin modificar las horas antiguas.
- P09 se aplicaba de forma distinta entre proformas incompletas y confundía revisión documental con revisión propia de correos. La decisión autorizada se incorporó a la versión inicial; las nuevas ejecuciones de E2E-03/07/12 registran uniformemente la aprobación genérica como insuficiente y E2E-05/06 identifican los correos sin inventar revisiones.
- Tres intentos A3 se interrumpieron por límite de uso antes de producir informe completo. Tras «Continua con lo que estavas haciendo», se reintentaron en conversaciones limpias A4. Los archivos parciales y el error se conservan; su hora final no capturada no se inventa. Las muestras completas de consistencia son A1/A2/A4.
- El cotejador inicialmente no admitía timestamps con espacio antes del desfase. Se corrigió el lector para aceptar los formatos registrados sin reescribir sus valores.
- Un cotejo adicional de checklist idéntico marcó una diferencia de P09 en E2E-04-A4: faltante frente a contradictorio en A1/A2. Se conservan [el cotejo inicial](pruebas/resultados/ronda-1.1/comparacion-checklist-exacto.json) y su código. El escenario exige conflicto global, cantidad/acabado y reconciliación de revisión/aceptación; no fija esa etiqueta auxiliar. El cotejo funcional aplica ese criterio original y la aclaración del usuario, manteniendo visible la diferencia, sin cambiar estados globales esperados, entradas, respuestas o condiciones de fallo.
- El validador de enlaces se detuvo inicialmente porque su propio archivo de resultados aún no existía. Se ordenó la escritura de un estado explícito EN CURSO antes del chequeo y la marca COMPLETADA solo al terminar todos los controles; la ejecución posterior completó los 213 controles.
- La transcripción visual de E2E-08-A1 conserva una variación de acento en el pie TECNICA/TÉCNICA, sin cambios comerciales. Se conserva la imagen original como evidencia canónica y no se presenta la visión como transcripción exacta garantizada carácter por carácter. No se corrigió silenciosamente la respuesta.

## Validaciones realmente ejecutadas

La ronda activa completó **18 ejecuciones con IA** y **18 aprobaciones contra los criterios funcionales de los casos**: las trece mínimas previstas y cinco comprobaciones de medios/robustez. No hay ejecuciones obligatorias pendientes.

E2E-01/02 producen documentación suficiente; E2E-03 detecta los faltantes; E2E-04 conserva el conflicto de cantidad/acabado y exige conciliación; E2E-05 detecta F04 ausente; E2E-06 lo resuelve con la medición y conserva el antecedente; E2E-07 rechaza la instrucción maliciosa. E2E-08 lee imagen documental; E2E-09 lee el PDF escaneado mediante renderizado y visión, sin afirmar OCR; E2E-10/11 se abstienen ante imagen ilegible/archivo dañado; E2E-12 rechaza la instrucción maliciosa de la imagen.

Las tres ejecuciones completas de E2E-02/03/04 mantienen el estado global y los hallazgos obligatorios. E2E-02/03 coinciden además en los 21 estados del checklist. En E2E-04 la clasificación auxiliar de P09 varía, pero ninguna respuesta da por resuelta la versión ni autoriza el alcance; la diferencia queda registrada. Las 18 respuestas contienen los 21 controles, con evidencia/motivo y NA según aplique.

Se ejecutaron **213 comprobaciones deterministas de artefactos**, incluidas conservación histórica, fixtures e instrucciones intactos, controles del perfil no alterados salvo P09 autorizado, portabilidad, enlaces y Git. El validador estructural devolvió **Skill is valid!**. Estas comprobaciones complementan, no sustituyen, las pruebas con IA.

[RESULTADOS.md](pruebas/RESULTADOS.md) enlaza cada respuesta y distingue estados del expediente de veredictos. La [comparación estructurada](pruebas/resultados/ronda-1.1/comparacion-esperado-observado.json) conserva estados extraídos, criterios obligatorios y observaciones; la [revisión semántica](pruebas/resultados/ronda-1.1/revision-semantica.json) registra lectura, fecha y hash por respuesta.

EXPLICACION.md usa una ejecución nueva, E2E-01-A1, expresamente ficticia. Su [vista A4](pruebas/resultados/validacion-fixtures/EXPLICACION-A4.png) se compuso con márgenes de 2 cm, texto 11 pt y título 16 pt, se verificó como una página y se inspeccionó completa. El PDF transitorio estuvo solo en memoria; no se creó un PDF final adicional. El [JSON de impresión](pruebas/resultados/validacion-fixtures/EXPLICACION-A4.json) vincula la vista al hash del Markdown actual.

## Referencias, entrega y límites

Las referencias oficiales consultadas en la fase inicial fueron [ISO 10013:2021](https://www.iso.org/standard/75736.html) y [ISO 9001:2026](https://www.iso.org/standard/9001). No se leyó el texto normativo completo ni se hizo un mapeo de cláusulas; los controles son del perfil de demostración y no acreditan certificación ni conformidad.

La entrega local incluye skill, perfil, guía, texto portable completo, explicación, este reporte y pruebas/evidencias. No existe enlace público verificable de la conversación; se conserva la transcripción disponible de prompts, registros y respuestas. Las sesiones nativas no ofrecen exportación automática íntegra de todas sus llamadas internas; se registran los métodos y comandos disponibles, sin inventar enlaces o identidad de modelo.

La interpretación de documentos no acredita autenticidad, autoridad, factibilidad ni cumplimiento técnico/legal; la revisión humana sigue siendo parte expresa del objetivo. Los resultados no garantizan comportamiento universal en todo modelo o documento ni exactitud literal de toda transcripción visual. No se usa una limitación de acceso para simular lectura, completar datos o declarar aprobación.

El enunciado prevé entrega por respuesta al correo a más tardar el **20 de noviembre de 2026**, sin hora límite declarada y con posible llamada posterior. Al cerrar la preparación inicial no se había enviado correo, publicado archivos ni creado commits; no se instalaron herramientas ni se alteró configuración para ejecutar las pruebas. Posteriormente el usuario autorizó crear el primer commit y publicarlo en `https://github.com/wnunezc/oppenin-TT`, exclusivamente con su identidad y firma. Esa autorización no incluye el envío del correo ni representa aceptación del evaluador.
