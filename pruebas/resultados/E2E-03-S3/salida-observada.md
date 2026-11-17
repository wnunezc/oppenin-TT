# Informe documental

## 1. Identificación

Expediente DEMO-003. Revisión de análisis 1, realizada el 17 de noviembre de 2026. Etapa solicitada: importación, antes del pedido al proveedor. Ruta L1: importación. Perfil aplicado: PEO-01 v1.0, skill revisor-expedientes-mobiliario, instrucciones v1.0. Caso expresamente ficticio, solo prueba técnica.

## 2. Fuentes

Recibido y abierto: `pruebas/entradas/E2E-03-proforma.pdf`, una página. Documento DEMO-PF-003, R1, fecha 2026-11-17, vigente hasta 2026-12-01 inclusive. Se accedió a la única página con pypdf.PdfReader y se extrajo íntegramente su texto mediante extract_text(); no se realizó OCR ni comprobación visual de un render. Transcripción propia conservada en `extraccion-propia.txt`. Las referencias «p. 1» de este informe corresponden a ese PDF. El texto extraído es legible; no se identificaron documentos adjuntos mencionados como disponibles ni revisiones anteriores aportadas. La aceptación se declara pendiente, no es un adjunto recibido.

## 3. Estado global

**PENDIENTE DE INFORMACIÓN.** Faltan unidad dimensional, acabado definitivo, condición de pago y evidencia identificada y fechada de la revisión aceptada por el cliente. No se comprobó contradicción entre valores aportados. Las exclusiones de costos no equivalen a costos finales de cero.

## 4. Datos normalizados

Todos los datos siguientes proceden de p. 1; son declaraciones documentales, no comprobaciones externas.

| Campo | Original y valor registrado | Estado |
|---|---|---|
| Expediente y etapa | «DEMO-003. Etapa solicitada: importación» | aportado |
| Cliente y contacto | «Residencia Beta Demo»; beta@cliente.example | aportado |
| Proyecto y uso | «mobiliario residencial, sillas de comedor» | aportado |
| Entrega | «Casa Demo B, Ciudad de Panamá, Panamá» | aportado |
| Proveedor | «Demo Furniture Export»; ventas@exportador.example | aportado |
| Línea | «L1: silla modelo S-20; 20 unidades; ruta importación» | aportado |
| Dimensiones L1 | «Dimensiones L x A x H: 500 x 550 x 850»; largo 500, ancho 550, alto 850; unidad: NO APORTADO. No se convierten medidas sin unidad. | faltante parcial |
| Material L1 | «estructura de acero y asiento de polipropileno» | aportado |
| Acabado L1 | «por confirmar»; acabado definitivo: NO APORTADO | faltante |
| Moneda, precio y subtotal | USD; unitario USD 80.00; subtotal USD 1600.00 | aportado |
| Cargos de proforma | «Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00» | aportado |
| Total | «USD 1600.00. El total es de mercancía, no costo final puesto en destino» | aportado; costo final NO APORTADO |
| Alcance de costos | Embalaje incluido; transporte internacional, transporte local y tributos de importación excluidos. Sus importes: NO APORTADO | aportado como exclusión; importes finales faltantes |
| Condición de pago | NO APORTADO. Se menciona «recepción del anticipo» solo como hito; no consta condición de pago completa ni importe/porcentaje del anticipo | faltante |
| Países | Despacho China; entrega Panamá. Origen de fabricación: NO APORTADO, no inferido ni exigido por I03 | aportado |
| Preparación | «30 días calendario desde recepción del anticipo» | aportado |
| Transporte | «estimado 35 días calendario desde despacho; no hay fecha firme de llegada» | aportado como estimación |
| Instalación | «No incluye instalación» | aportado |
| Incoterm | «Las partes no han usado Incoterm en esta proforma» | aportado; I06 NA |
| Revisión aplicable | DEMO-PF-003 R1, 2026-11-17, vinculada a DEMO-003 y L1 | aportado |
| Aprobación y aceptación | «Especificación y condiciones aprobadas: DEMO-PF-003 R1». «Aceptación del cliente: pendiente». Identidad y fecha de aceptación: NO APORTADO | faltante de evidencia explícita de aceptación del cliente |

Comprobación decimal a centavos: 20 × USD 80.00 = USD 1600.00; USD 1600.00 + USD 0.00 (impuestos de proforma) + USD 0.00 (otros cargos) = USD 1600.00. Coincide con subtotal y total declarados. No se asigna cero a los transportes o tributos excluidos ni se calcula costo puesto en destino. No se suman plazos para prometer una llegada.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base | satisfecho | p. 1, expediente DEMO-003 y etapa importación explícitos; identificador ficticio, sin atribución a ERP. |
| P02 | Sí, base | satisfecho | p. 1, cliente y correo explícitos. |
| P03 | Sí, base | satisfecho | p. 1, mobiliario residencial y Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí, L1 | satisfecho | p. 1, L1 única, silla S-20, 20 unidades positivas. |
| P05 | Sí, L1 | faltante | p. 1, ejes y valores presentes, unidad ausente; material presente; acabado «por confirmar». |
| P06 | Sí, L1 | satisfecho | p. 1, ruta importación explícita. |
| P07 | Sí, base | faltante | p. 1, importes y exclusiones explícitos, aritmética coherente; falta condición de pago. Total declarado limitado a mercancía, no total final. |
| P08 | Sí, base | satisfecho | p. 1, preparación desde anticipo y transporte estimado desde despacho; instalación expresamente excluida. No hay fecha firme de llegada, ni se inventa. |
| P09 | Sí, base | faltante | p. 1, número, fecha, R1 y vinculación presentes; afirmación genérica de aprobación sin evidencia identificada y fechada que establezca la versión aceptada por el cliente. |
| P10 | Sí, base | faltante | p. 1, aceptación del cliente «pendiente»; no hay identidad, fecha ni alcance aceptado documentados. |
| F01 | No | NA | L1 declarada exclusivamente de importación; no se declara fabricación en este expediente. |
| F02 | No | NA | Misma ruta explícita; no aplica exigir plano de fabricación. |
| F03 | No | NA | Misma ruta explícita; no aplica aprobación técnica de fabricación. |
| F04 | No | NA | Ruta importación, sin declaración de fabricación ajustada a espacio existente. |
| F05 | No | NA | Ruta importación; no se exige plazo de fabricación. |
| I01 | Sí, importación | satisfecho | p. 1, proveedor, proforma DEMO-PF-003 R1, fecha y vigencia explícitas, vigente en fecha de revisión. |
| I02 | Sí, L1 importada | faltante | p. 1, código, cantidad, valores dimensionales y material presentes; faltan unidad dimensional y acabado definitivo. Solo hay una fuente, sin cotejo independiente. |
| I03 | Sí, importación | satisfecho | p. 1, China como despacho y Panamá como entrega. No se deduce origen. |
| I04 | Sí, importación | faltante | p. 1, moneda, precio/total y alcance de costos declarados; condición de pago ausente. Exclusiones no son cero de costo final. |
| I05 | Sí, importación | satisfecho | p. 1, preparación 30 días desde anticipo y transporte estimado 35 días desde despacho, con hitos explícitos. La estimación no confirma llegada. |
| I06 | No, condición no activada | NA | p. 1 declara expresamente que no se usa Incoterm. El alcance de costos se revisa en I04. |

## 6. Hallazgos

| Hallazgo | Requisito | Evidencia y consecuencia documental | Acción requerida |
|---|---|---|---|
| H01 | P05, I02 | p. 1, «500 x 550 x 850» sin unidad; la especificación dimensional no está completa y no puede normalizarse. | Aportar unidad explícita para largo, ancho y alto de L1, en documento identificado y revisado. |
| H02 | P05, I02 | p. 1, acabado «por confirmar»; no hay acabado definitivo que revisar o aceptar. | Definir acabado de L1 y documentarlo en la revisión correspondiente. |
| H03 | P07, I04 | p. 1, hito «recepción del anticipo» sin condición de pago; no permite establecer lo que debe pagarse y cuándo. | Aportar condición de pago, incluido anticipo y saldo cuando correspondan. |
| H04 | P09, P10 | p. 1, revisión R1 llamada «aprobada», pero aceptación del cliente pendiente, sin identidad y fecha. No se equipara una afirmación sin atribución a aceptación; no se considera contradicción demostrada porque no se identifica quién aprobó. | Aportar aceptación explícita del cliente, con identidad, fecha, alcance y revisión exacta, una vez definidos los campos pendientes. Documentar sustitución y aceptación si se emite revisión nueva. |
| H05 | P07, I04 (alcance declarado) | p. 1, USD 1600.00 corresponde a mercancía; transportes y tributos excluidos, sin importes. No se puede determinar costo final puesto en destino. No es contradicción aritmética ni falta de declaración del alcance de costos. | Mantener visible la exclusión y obtener los costos pendientes si se necesita revisar un presupuesto final puesto en destino. No imputarlos a cero. |

## 7. Preguntas y siguiente acción humana

En una sola respuesta documental, precisar:

1. ¿Qué unidad corresponde a largo 500, ancho 550 y alto 850 de L1?
2. ¿Cuál es el acabado definitivo de las 20 sillas S-20?
3. ¿Cuál es la condición de pago, incluido el importe o porcentaje y el hito del anticipo y del saldo, si corresponden?
4. ¿Qué evidencia identifica al cliente que acepta, la fecha y el alcance/revisión exactos aceptados? ¿Quién emitió la afirmación de aprobación de R1?
5. Si se requiere costo final en destino, ¿cuáles son los importes y fuentes de transporte internacional, transporte local y tributos actualmente excluidos?

Siguiente acción humana: reunir una revisión identificada que resuelva H01-H03 y la aceptación de H04; aportar evidencia explícita de sustitución y aceptación de cambios pertinentes si cambia R1. Someter el conjunto a nueva revisión documental conservando este informe. La estimación de transporte no constituye fecha firme de llegada. No se exige documentación aduanera o de embarque definitiva para esta etapa previa al pedido. Este informe no aprueba ninguna operación.

## 8. Límites

Revisión exclusivamente documental basada en el texto extraído de una página del archivo recibido; sin comprobación externa de autenticidad, autoridad, materiales, factibilidad, calidad ni cumplimiento técnico o legal. No se hicieron cálculos de tributos, conversiones monetarias ni interpretaciones de obligaciones legales de comercio. Los controles son del perfil demostrativo PEO-01 v1.0; no constituyen certificación ni acreditan conformidad ISO. No se consultaron referencias externas ni el texto normativo completo. No se recibió revisión anterior para comparar cambios.
