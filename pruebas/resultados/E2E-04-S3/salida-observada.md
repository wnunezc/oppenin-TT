# Informe documental — DEMO-004

## 1. Identificación

Expediente **DEMO-004**. Revisión de análisis **1**, realizada el 17 de noviembre de 2026 (America/Panama). Etapa solicitada: **importación**, antes del pedido al proveedor. Única línea L1, ruta explícita importación. Perfil aplicado: **PEO-01 v1.0**, skill **revisor-expedientes-mobiliario**, instrucciones v1.0. Expediente **FICTICIO — SOLO PRUEBA TÉCNICA**; no se atribuye este identificador a un ERP real.

## 2. Fuentes

- **E2E-04-correo.md**: leído íntegramente. Asunto «Datos para expediente DEMO-004», fecha declarada **2026-11-18 10:00 UTC-05:00**, remitente beta@cliente.example, firmado «Luis Demo». Sin identificador de revisión declarado. Se vincula expresamente a DEMO-004 y L1. Para trazabilidad: párrafo 1 «Solicito revisar…»; párrafo 2 «Para la línea L1 necesitamos…»; párrafo 3 «No confirmo todavía…»; firma final «Luis Demo». La fecha declarada es posterior a la fecha de este análisis: se conserva sin corregir ni acreditar su autenticidad.
- **E2E-04-proforma.pdf**: archivo PDF real abierto con pypdf; **1 página de 1 leída**, por extracción textual directa, sin OCR ni comprobación externa. Documento **DEMO-PF-004 R1**, fecha **2026-11-17**, vigencia «hasta 2026-12-01 inclusive», vinculado a DEMO-004/L1. El texto original extraído se conserva en `extraccion-propia.txt`.
- No se recibieron otras revisiones de proforma ni una aceptación del cambio a 24 sillas blancas. El correo no identifica una proforma sustituta. No hay adjuntos adicionales mencionados como entregados. No se detectaron campos ilegibles en la extracción recibida.

## 3. Estado global

**CONFLICTO DOCUMENTAL**. La proforma R1 documenta 20 sillas negro mate aceptadas; el correo solicita 24 sillas blanco mate y declara expresamente que no confirma la sustitución de proforma ni el nuevo total. La fecha posterior del correo no resuelve ni sustituye automáticamente el alcance aceptado. También hay información pendiente, pero prevalece el conflicto documental.

## 4. Datos normalizados

| Campo | Original aportado y procedencia | Estado documental |
|---|---|---|
| Cliente/contacto | «Residencia Beta Demo», «beta@cliente.example»; PDF p. 1, Cliente. Correo: mismo remitente y firma Luis Demo | Aportado, sin verificación externa de identidad/autoridad |
| Proyecto/uso/destino | «mobiliario residencial, sillas de comedor»; «Casa Demo B, Ciudad de Panamá, Panamá»; PDF p. 1 | Aportado |
| Línea/producto/unidad/ruta | «L1: silla modelo S-20; 20 unidades; ruta importación»; PDF p. 1. Correo párr. 2: «Para la línea L1 necesitamos 24 sillas» | Cantidad contradictoria: **20 unidades / 24 sillas**. Descripción y ruta aportadas |
| Dimensiones L1 | «Dimensiones L x A x H: 500 x 550 x 850 mm»; PDF p. 1 | Aportado: largo 500 mm, ancho 550 mm, alto 850 mm; no se convierte ni altera la fuente |
| Material L1 | «estructura de acero y asiento de polipropileno»; PDF p. 1 | Aportado |
| Acabado L1 | «negro mate»; PDF p. 1. Correo párr. 2: «acabado blanco mate» | Contradictorio: **negro mate / blanco mate** |
| Proveedor | «Demo Furniture Export», ventas@exportador.example; PDF p. 1 | Aportado |
| Documento/vigencia | DEMO-PF-004, R1, 2026-11-17, «hasta 2026-12-01 inclusive»; PDF p. 1 | Aportado; sustitución aplicable al nuevo alcance: **NO APORTADO** |
| Precio/moneda | «Precio unitario: USD 80.00. Subtotal: USD 1600.00»; PDF p. 1 | Aportado para R1 de 20 unidades. Precio aceptado para el alcance modificado: **NO APORTADO** |
| Cargos/total R1 | «Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00»; «Total proforma: USD 1600.00»; PDF p. 1 | Aportado para R1. Correo párr. 3: «No confirmo todavía … el nuevo total»: total del cambio **NO APORTADO** |
| Alcance de costos | «Embalaje: incluido»; transportes internacional y local excluidos; tributos de importación excluidos; «El total es de mercancía, no costo final puesto en destino»; PDF p. 1 | Aportado como alcance comercial; importes excluidos/costo final: **NO APORTADO**, sin convertirlos en cero |
| Pago | «30 % al confirmar pedido y 70 % antes del despacho»; PDF p. 1 | Aportado para R1 |
| Países | «País de despacho: China. País de entrega: Panamá»; PDF p. 1 | Aportado; país de fabricación no declarado ni inferido |
| Plazos/instalación | «Preparación: 30 días calendario desde recepción del anticipo»; «Transporte: estimado 35 días calendario desde despacho; no hay fecha firme de llegada»; «No incluye instalación»; PDF p. 1 | Aportado con hitos y carácter estimado; fecha firme de llegada no aportada ni exigida por existir plazos documentados |
| Incoterm | «Las partes no han usado Incoterm en esta proforma»; PDF p. 1 | Aportado: I06 NA |
| Aceptación | PDF p. 1: «Especificación y condiciones aprobadas: DEMO-PF-004 R1» y «Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-004 R1» | Aceptación documental de R1 aportada. Aceptación del cambio a 24/blanco mate: **NO APORTADO** |

**Comprobación aritmética decimal de R1, a centavos:** 20 × USD 80.00 = USD 1,600.00; USD 1,600.00 + USD 0.00 (impuestos de esta proforma) + USD 0.00 (otros cargos) = USD 1,600.00. Coincide con el total de mercancía declarado para R1. No se calcula un nuevo total para 24 unidades ni el costo puesto en destino: faltan condiciones confirmadas del cambio e importes de costos excluidos. No se suman plazos para prometer una llegada.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base | satisfecho | Correo párr. 1 y PDF p. 1: DEMO-004, importación |
| P02 | Sí | satisfecho | PDF p. 1: entidad solicitante y correo; constancia de Luis Demo |
| P03 | Sí | satisfecho | PDF p. 1: proyecto residencial y Casa Demo B, Ciudad de Panamá, Panamá |
| P04 | Sí | contradictorio | L1 identificada, descripción y unidad disponibles; PDF p. 1: 20 unidades; correo párr. 2: 24 sillas |
| P05 | Sí | contradictorio | PDF p. 1 aporta ejes, mm y material; acabado negro mate frente a blanco mate del correo párr. 2 |
| P06 | Sí | satisfecho | PDF p. 1 y etapa del correo: importación, sin fabricación declarada |
| P07 | Sí | faltante | R1 tiene moneda, precio, subtotal, cargos, total y pago coherentes; correo párr. 3 no confirma nuevo total. Falta condición comercial documentada aplicable al cambio |
| P08 | Sí | satisfecho | PDF p. 1: preparación desde anticipo, transporte estimado desde despacho y exclusión de instalación. No constituye fecha firme de llegada |
| P09 | Sí | contradictorio | R1, fecha y vigencia identificadas y aprobadas en PDF; el correo cambia cantidad/acabado pero no identifica ni confirma sustitución. Versión vigente para ese alcance sin resolver |
| P10 | Sí | faltante | Aceptación explícita de R1 por Luis Demo el 2026-11-17, PDF p. 1; no hay aceptación explícita del alcance cambiado con revisión y condiciones comerciales exactas |
| F01 | No | NA | L1 declara exclusivamente ruta importación; no hay líneas de fabricación |
| F02 | No | NA | Misma condición: no se revisa fabricación |
| F03 | No | NA | Misma condición: no se revisa fabricación |
| F04 | No | NA | Ruta importación; no se declara fabricación ajustada a espacio existente |
| F05 | No | NA | No hay ruta de fabricación declarada |
| I01 | Sí, L1 | satisfecho | PDF p. 1: proveedor, proforma disponible, número, R1, fecha y vigencia explícita; su aplicabilidad al cambio se observa en P09 |
| I02 | Sí, L1 | contradictorio | Código S-20, dimensiones, material y acabado están en PDF p. 1; cantidad y acabado incompatibles con correo párr. 2 |
| I03 | Sí, L1 | satisfecho | PDF p. 1: China como despacho y Panamá como entrega; no se confunde con origen de fabricación |
| I04 | Sí, L1 | faltante | PDF p. 1 define precio, pago y costos incluidos/excluidos de R1; total y condiciones comerciales del alcance modificado sin confirmación, correo párr. 3. No se exige convertir exclusiones en cotización de costo final |
| I05 | Sí, L1 | satisfecho | PDF p. 1: preparación 30 días calendario desde anticipo y transporte estimado 35 desde despacho; ausencia explícita de fecha firme |
| I06 | Condición no activada | NA | PDF p. 1 declara expresamente que no se ha usado Incoterm; no se inventa término, edición ni lugar |

Los estados satisfechos registran presencia y coherencia local de datos aportados; no subsanan la falta de una versión aceptada que consolide el cambio.

## 6. Hallazgos

| ID | Requisitos | Evidencia/valores | Consecuencia documental | Acción requerida |
|---|---|---|---|---|
| H01 | P04, I02 | PDF p. 1 R1: 20 unidades; correo párr. 2: 24 sillas | No hay cantidad única documentada para tramitar L1 | Confirmar cantidad aplicable y documentarla en una revisión vinculada al expediente, con sustitución y aceptación explícitas |
| H02 | P05, I02 | PDF p. 1 R1: negro mate; correo párr. 2: blanco mate | Especificación de acabado incompatible entre fuentes | Confirmar acabado aplicable e incorporarlo en la revisión identificada y aceptada |
| H03 | P07, I04 | R1: USD 80.00/unidad y USD 1600.00 para 20; correo párr. 3: nuevo total no confirmado | No se conoce el precio/total aceptado aplicable al cambio; no hay error aritmético demostrado en R1 | Aportar condiciones comerciales del alcance acordado: precio unitario, subtotal, cargos/impuestos declarados, total, pago y alcance de costos; indicar inclusiones/exclusiones o pendientes sin convertirlos en cero |
| H04 | P09, P10 | R1 aceptada por Luis Demo el 2026-11-17; correo de fecha declarada 2026-11-18 solicita cambios sin confirmar sustitución | La evidencia de aceptación existente cubre R1, no acredita la aceptación de una revisión que reúna los cambios. No puede elegirse fuente por fecha | Identificar documento/revisión que sustituye o conserva R1 y aportar evidencia explícita de aceptación de su alcance y condiciones, con identidad y fecha |

## 7. Preguntas y siguiente acción humana

1. **H01:** ¿L1 debe quedar en 20 o 24 sillas? Aportar la confirmación documental vinculada a DEMO-004.
2. **H02:** ¿El acabado definitivo es negro mate o blanco mate? Incorporar el valor acordado en la revisión aplicable.
3. **H03:** ¿Cuáles son las condiciones comerciales y el total confirmados para esa cantidad y acabado? Aportar el documento correspondiente, con moneda, precio unitario, subtotal, cargos/impuestos, total, pago y alcance de costos.
4. **H04:** ¿Qué documento/revisión queda vigente y cuál sustituye, si corresponde? Aportar aceptación explícita de esa revisión, con identidad, fecha y alcance.

La siguiente acción humana es reunir estas respuestas y la documentación coherente y aceptada para emitir una nueva revisión documental conservando esta. Este informe no aprueba el pedido ni autoriza compra o importación. No se exigen declaración aduanera, conocimiento de embarque, packing list definitivo ni recepción de una operación todavía no iniciada.

## 8. Límites

Revisión exclusivamente documental de las dos fuentes recibidas, sin comprobación externa de identidad, autoridad, autenticidad, disponibilidad, calidad, factibilidad ni cumplimiento técnico o legal. La extracción del PDF es textual; no se infieren dimensiones ni materiales de apariencia visual. No se realizaron acciones externas ni se consultó la red. Los controles son del perfil de demostración PEO-01; no se atribuyen a ISO ni se afirma certificación o conformidad normativa. No se aportó una revisión anterior del análisis, por lo que no se presenta un historial de cambios.
