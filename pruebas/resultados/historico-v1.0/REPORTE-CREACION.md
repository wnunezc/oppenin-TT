# Reporte de creación con IA

## Alcance y registro inicial

Inicio observado: **2026-11-17 12:18:28 America/Panama (UTC-05:00)**, obtenido de `clock.curr_time` (17:18:28 UTC). La primera persistencia del registro se realizó después de leer completamente, en orden, `PRUEBA TECNICA IT.pdf`, `TASK.MD` y `PROMPTD-CREACION-SKILL.md`, conforme a la prohibición de crear archivos antes de esas lecturas. Los eventos persistidos están en `pruebas/resultados/eventos.jsonl`. Las fechas de los fixtures son ficticias y no son marcas de ejecución.

Se desarrolla la skill propuesta y sus entregables, sin atribuir problemas internos comprobados a Oppenin. El contexto empresarial es únicamente el declarado por el usuario. No se crea el esquema habitual del workspace. El AGENTS.md del directorio ancestro se inspeccionó; la instrucción expresa del usuario excluye sus documentos de onboarding y vault en este proyecto.

## Herramientas y modelos

- Autoría: Codex en la aplicación de escritorio, con IA. La identidad exacta del modelo servido y la versión de la aplicación no están expuestas en esta sesión; no se deducen del nombre del producto.
- Pruebas: Codex CLI **0.136.0**, autenticación existente de ChatGPT; no se copiaron credenciales. Configuración existente observada: `model = "gpt-6.1-sol"`, `model_reasoning_effort = "medium"`. Esto identifica la selección configurada; si los eventos no exponen el modelo efectivamente servido, se registra como no expuesto. No se cambió esa configuración.
- Runtime incluido: bundle **26.1112.11217**, Python **3.12.14**, ReportLab **4.4.9**, pypdf **6.21.4** y Poppler disponible. Python del sistema dispone de PyYAML **6.0.3**, usado para el validador estructural de skills. No hubo instalaciones.
- Se leyeron las skills locales `skill-creator` y `pdf`; se aplican a creación, validación estructural y revisión de PDF. No se instaló la skill creada globalmente.

## Instrucciones principales y decisiones autorizadas

1. El usuario ordenó leer las tres fuentes en secuencia, implementar y validar sin limitarse a un plan, conservar el trabajo anterior, no enviar correo ni publicar ni crear commits, y mantener ignorados TASK.MD y el PDF fuente.
2. El prompt de desarrollo original se conserva íntegro en `PROMPTD-CREACION-SKILL.md`. De él proceden PEO-01, el formato de informe, los siete escenarios y las trece ejecuciones mínimas; no se atribuyen esos requisitos complementarios al PDF original.
3. Se consultó al usuario por la limitación del adjunto nativo de CLI: «¿autorizas presentar el archivo PDF real mediante su ruta local y que cada sesión independiente de la IA lo abra y lea con sus herramientas, conservando el registro de lectura y la respuesta?». Respuesta: «Sí, autorizar lectura del PDF real por ruta local».
4. Ampliación posterior literal del usuario: «agrega soporte para imagenes tambien... no solo seran pdf.». Se incorpora lectura por visión/OCR disponible, procedencia por archivo/región e ilegibilidad explícita. No se agregan controles documentales al perfil ni inferencias de dimensiones desde fotografías. Se añade una prueba con imagen derivada del fixture autorizado E2E-02.
5. En los intentos CLI se incorporó el texto completo de skill y perfil en el prompt. Tras el impedimento de modelo, la activación real de las sesiones completas utiliza subagentes Codex con `fork_turns=none`: leen íntegramente SKILL.md y PERFIL-EXPEDIENTE.md y únicamente los archivos enumerados de su caso, sin escenarios ni criterios esperados. El PDF real se proporciona por ruta autorizada y la imagen se abre con visión local. Se solicita revisión con las reglas de la skill, sin completar faltantes ni realizar acciones externas. Los prompts exactos se conservan en cada directorio de ejecución, separados de los resultados esperados.
6. La evaluación independiente con subagentes se aplica por la sección «Independent Forward-Testing» de la skill `skill-creator`; el alcance de pruebas completas ya estaba autorizado por el usuario. No se elige un modelo alternativo ni se modifica configuración: todos los subagentes heredan la misma selección de la sesión, cuya identidad exacta no es expuesta. No puede certificarse independientemente la identidad del modelo servido.

## Construcción y comprobaciones iniciales

Se inspeccionó Git: repositorio sin commits y sin archivos rastreados. Existían `.gitignore`, las tres fuentes y ningún desarrollo previo. `.gitignore` ya excluía `/TASK.MD` y `/PRUEBA TECNICA IT.pdf`; se comprobó con `git check-ignore -v` y no se modificó.

Se creó SKILL.md v1.0 y el perfil compañero PEO-01 v1.0. El perfil conserva literalmente los campos y reglas autorizados, separando ISO, datos del expediente y decisiones de demostración. El soporte de imágenes no cambia sus requisitos. La guía documenta activación portable y límites. Los fixtures provienen de los bloques autorizados; se generan cuatro PDF con marca visible de prueba y correos `.example`, sin logos ni firmas reales.

Se consultaron los catálogos oficiales de [ISO 10013:2021](https://www.iso.org/standard/75736.html) y [ISO 9001:2026](https://www.iso.org/standard/9001) el 17 de noviembre de 2026. Coinciden con las ediciones indicadas en el prompt. No se consultó el texto normativo completo ni se realizó mapeo por cláusulas o evaluación de conformidad.

La preparación reproducible está conservada en `pruebas/resultados/herramientas/preparar.py`. Reabrió los cuatro PDF con pypdf y contrastó cada línea con el fixture. Poppler renderizó los cuatro; se inspeccionaron visualmente completos, legibles y sin texto recortado. Las vistas y extracciones están en `pruebas/resultados/validacion-fixtures/`. Se conserva el manifiesto inicial con SHA-256 para skill, perfil y entradas iniciales.

## Problemas observados y tratamiento

- La primera extracción del PDF fuente falló porque stdout utilizaba cp1252 y no admitía una viñeta. Se repitió con stdout UTF-8, se obtuvo su página completa y se leyó antes de TASK.MD.
- `fitz`/PyMuPDF no está disponible en el runtime. Se utilizó Poppler existente para renderizar; no se instaló nada.
- El validador de skills falló inicialmente por ausencia de `yaml` en el Python del bundle. Se ejecutó con Python del sistema, que ya dispone de PyYAML, y devolvió `Skill is valid!`. Esta comprobación no demuestra comportamiento E2E.
- Poppler emitió avisos sobre fuentes de sustitución Symbol/ArialUnicode; las páginas generadas utilizan Helvetica y se inspeccionó el resultado visual, sin recortes observados.
- Codex CLI emite avisos de metadatos de plugins existentes al inicializar. Se conservan en stderr; no se modifica la configuración ni se instala o utiliza un plugin para revisar expedientes.
- Tres intentos CLI (E2E-01/02/03-R1) se interrumpieron por HTTP 400/model_not_found: «The 'gpt-6.1-sol' model is not supported when using Codex with a ChatGPT account». No produjeron informes y no se cuentan como pruebas completas. La lista local de modelos anunciaba precisamente ese modelo, por lo que no se asumió que otra selección funcionaría. Se continuó con sesiones de evaluación nativas independientes, manteniendo los intentos originales.
- En algunas primeras sesiones, el inicio registrado corresponde a la captura de evidencia después de la lectura inicial de instrucciones, que se repitió; sus registros lo aclaran. No se atribuye ese timestamp a un momento anterior no capturado.
- Las sesiones nativas no ofrecen una exportación automática íntegra de todas las llamadas internas. Se conservan prompts, entradas con hashes, métodos/comandos de lectura, extracción propia e informes observados; los intentos CLI sí conservan eventos JSONL y stderr completos. No se inventan enlaces de conversación.

## Validaciones y cierre

Se completaron **14 ejecuciones reales de la skill** en sesiones independientes: los siete escenarios originales, dos repeticiones adicionales de E2E-02/03/04 (13 ejecuciones previstas en total) y una prueba adicional de imagen documental legible. Las catorce tienen respuesta observada completa y resultaron **APROBADAS contra los criterios locales de sus escenarios**, con las observaciones de calidad conservadas en la tabla. No se declara aceptación del evaluador ni funcionamiento universal.

Resultados observados: E2E-01 y E2E-02, documentación suficiente; E2E-03, pendiente de información por unidad/acabado/pago/aceptación; E2E-04, conflicto de cantidad y acabado; E2E-05, pendiente por F04; E2E-06, documentación suficiente con cierre de H01/F04 y nueva revisión 2, manteniendo el informe anterior intacto; E2E-07, pendiente y con rechazo de la instrucción incrustada. E2E-08 leyó directamente una imagen PNG ficticia mediante visión, citó archivo/regiones y obtuvo documentación suficiente, sin consultar el PDF o sus extracciones.

Las repeticiones conservaron los estados y hallazgos obligatorios. Todos los registros de fuentes tienen los mismos hashes de SKILL.md v1.0, PEO-01 v1.0 y fixtures correspondientes. No se modificaron reglas compartidas ni se corrigieron respuestas observadas. Los tres intentos CLI interrumpidos no se cuentan entre las ejecuciones completas. El modelo nativo servido no está expuesto: se mantuvo la misma configuración heredada sin seleccionar otro modelo; no se certifica su identidad exacta.

La comparación está en `pruebas/RESULTADOS.md` y en `pruebas/resultados/comparacion-esperado-observado.json`. Cada sesión conserva su prompt, fuentes con SHA256, timestamps reales, método de lectura y respuesta completa. Las extracciones propias de PDF se conservaron en archivos separados o incorporadas al informe observado (E2E-04-S1 y E2E-03-S2). El código de comparación combina la revisión semántica de la IA coordinadora con corroboraciones de estructura/hashes; no deduce aprobación únicamente por encontrar una etiqueta.

Observaciones de calidad: algunas celdas reproducen separadores `|` de la fuente sin escape Markdown; una ejecución pregunta por una fecha futura del fixture y otras añaden preguntas condicionales sobre costo final. Esas preguntas no se adoptan como requisitos nuevos de PEO-01 ni cambian los estados comprobados. La transcripción visual presenta una variación de acento en el pie, sin modificar campos comerciales. Las salidas originales se mantienen sin ocultar estas diferencias.

Se ejecutaron **47 comprobaciones deterministas complementarias** de sintaxis Python, hashes iniciales, contenido de los PDF, fidelidad de los 21 controles del perfil, aritmética, imagen PNG, explicación A4 y estado de Git. Evidencia: `pruebas/resultados/validacion-artefactos.json`. El validador de skills volvió a devolver `Skill is valid!`. Estas comprobaciones no sustituyen las ejecuciones con IA.

La explicación se compuso realmente a A4 con márgenes de 2 cm y texto Helvetica de 11 pt (título 16 pt), se contó una página y se inspeccionó su vista PNG completa, legible y sin recortes. El PDF de impresión se mantuvo solo en memoria y se pasó a Poppler por stdin: no existe un PDF final adicional. Se conservan la vista `pruebas/resultados/validacion-fixtures/EXPLICACION-A4.png`, su configuración, hash y timestamp en el JSON compañero, y el método reproducible en `vista_explicacion.py`.

Se entrega también `pruebas/resultados/instrucciones-completas.txt`, con el texto íntegro de skill y perfil reunido para herramientas sin archivos auxiliares. No contiene resultados esperados. La skill y sus instrucciones son portables; los scripts de evidencia documentan las rutas locales utilizadas durante esta validación y no son una dependencia de uso.

No hay escenarios obligatorios pendientes de ejecución. No se probaron OCR de PDF escaneado, imágenes borrosas, texto manuscrito o fotografías de muebles; el soporte de imagen comprobado corresponde a un documento nítido. La validación empresarial, una operación comercial real y la evaluación formal de conformidad ISO no forman parte de esta demostración ni se afirman realizadas. Los cuatro entregables del enunciado están preparados localmente: skill compartible, guía, explicación de una página con ejemplo ejecutado y reporte con evidencia. El evaluador conserva su decisión de aceptación.

No se dispone de un enlace público verificable de esta conversación; no se inventa. Se conserva el historial local de eventos, prompts exactos, llamadas de herramientas y respuestas de prueba. Estos datos son ficticios; los resultados no representan operaciones comerciales reales ni aceptación del evaluador. La entrega prevista en el enunciado es responder al correo a más tardar el 20 de noviembre de 2026, sin hora límite declarada. No se enviará ese correo desde esta ejecución.

Cierre de preparación y auditoría local: **2026-11-17T12:40:24.434652-05:00 America/Panama (UTC-05:00)**. Se verificaron las 14 salidas completas, sus hashes, las tres repeticiones por caso seleccionado, la conservación de la revisión anterior y los enlaces de evidencia. Véase `pruebas/resultados/auditoria-final.json`. No se creó commit, no se publicaron archivos ni se envió correo.
