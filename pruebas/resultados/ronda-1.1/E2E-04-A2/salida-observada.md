# Informe documental — DEMO-004

## 1. Identificación

Expediente ficticio DEMO-004, solo prueba técnica. Revisión de análisis: primera revisión de esta sesión independiente. Etapa solicitada: importación, antes del pedido al proveedor. Ruta de L1: importación. Perfil aplicado: PEO-01 v1.1; skill revisor-expedientes-mobiliario v1.1. Las fechas declaradas de los documentos se conservan, separadas de la hora real de análisis registrada en inicio.txt.

## 2. Fuentes

- Correo recibido: E2E-04-correo.md, de beta@cliente.example, fecha 2026-11-18 10:00 UTC-05:00, asunto «Datos para expediente DEMO-004». Sin identificador o revisión propios declarados. Párrafo 1: etapa y expediente; párrafo 2: cantidad y acabado; párrafo 3: falta de confirmación de sustitución y nuevo total; firma: Luis Demo.
- PDF recibido y abierto: E2E-04-proforma.pdf, una página. PROFORMA DEMO-PF-004, R1, fecha 2026-11-17, vigencia hasta 2026-12-01 inclusive, vinculada a DEMO-004/L1.
- No hay otros documentos enumerados para este análisis ni un informe anterior aportado. El correo alude a una sustitución sin identificar una versión sustituta; no se recibió una proforma actualizada.
- Método: lectura íntegra del correo, skill y perfil mediante Get-Content; apertura del PDF real con pypdf/PdfReader e iteración de todas sus páginas. La extracción presenta caracteres de sustitución en acentos: se conservó sin corregir en extraccion-proforma.txt. Se renderizó la página con pdftoppm -png -r 120 y se leyó visualmente completa en proforma-1.png. El contenido esencial es legible en el renderizado. No se declara archivo esencial ilegible. Poppler avisó ausencia de fuentes Symbol y ArialUnicode; el renderizado permitió leer los campos.

Las transcripciones siguientes proceden de la visión del PDF cuando la extracción dañó caracteres. Son datos del expediente, sin comprobación externa.

## 3. Estado global

**CONFLICTO DOCUMENTAL**. La proforma R1 declara 20 unidades y negro mate; el correo requiere 24 sillas y blanco mate. El remitente no confirma qué proforma debe sustituirse ni el nuevo total. La fecha posterior del correo no acredita sustitución ni aceptación de una revisión actualizada.

## 4. Datos normalizados

Referencias: «PDF» significa E2E-04-proforma.pdf, página 1; «correo» significa la fuente identificada en la sección 2.

| Dato | Valor original y procedencia | Estado documental |
|---|---|---|
| Expediente/etapa | PDF: «Expediente: DEMO-004. Etapa solicitada: importación.» Correo, párr. 1: «Solicito revisar la etapa importación de DEMO-004.» | aportado |
| Cliente/contacto | PDF, Cliente: «Residencia Beta Demo. Contacto: beta@cliente.example.» Correo: mismo remitente, firma «Luis Demo.» | aportado |
| Proyecto/destino | PDF: «mobiliario residencial, sillas de comedor»; «Casa Demo B, Ciudad de Panamá, Panamá.» | aportado |
| Línea/descripción/ruta | PDF: «L1: silla modelo S-20; 20 unidades; ruta importación.» Correo, párr. 2: «Para la línea L1 necesitamos 24 sillas y acabado blanco mate.» | contradictorio en cantidad; descripción/modelo y ruta aportados por PDF |
| Cantidad/unidad | PDF: «20 unidades»; correo: «24 sillas» | contradictorio; se conservan ambos valores |
| Dimensiones | PDF, Dimensiones: «L x A x H: 500 x 550 x 850 mm.» Normalización literal: largo 500 mm, ancho 550 mm, alto 850 mm | aportado para R1; no se infieren cambios por correo |
| Material | PDF: «estructura de acero y asiento de polipropileno.» | aportado para R1 |
| Acabado | PDF: «negro mate»; correo, párr. 2: «blanco mate» | contradictorio |
| Proveedor | PDF: «Demo Furniture Export. Contacto: ventas@exportador.example.» | aportado |
| Precio y subtotal | PDF: «Precio unitario: USD 80.00. Subtotal: USD 1600.00.» | aportado para R1; precio aplicable al cambio NO APORTADO |
| Costos y total | PDF: «Embalaje: incluido. Transporte internacional: excluido.» «Transporte local: excluido. Tributos de importación: excluidos.» «Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00.» «Total proforma: USD 1600.00. El total es de mercancía, no costo final puesto en destino.» | aportado para R1; nuevo total faltante, no confirmado en correo párr. 3 |
| Pago | PDF: «30 % al confirmar pedido y 70 % antes del despacho.» | aportado para R1 |
| Despacho/entrega | PDF: «País de despacho: China. País de entrega: Panamá.» | aportado; no se interpreta país de fabricación |
| Plazos/instalación | PDF: «Preparación: 30 días calendario desde recepción del anticipo.» «Transporte: estimado 35 días calendario desde despacho; no hay fecha firme de llegada. No incluye instalación.» | aportado para R1; no se calcula fecha de llegada |
| Incoterm | PDF: «Las partes no han usado Incoterm en esta proforma.» | aportado, condición I06 no activada |
| Aprobación/aceptación | PDF: «Especificación y condiciones aprobadas: DEMO-PF-004 R1.» Más abajo: «Constancia ficticia de aceptación del cliente: Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-004 R1.» | aportado para R1 con identidad y fecha; no cubre automáticamente las modificaciones del correo |
| Sustitución | Correo, párr. 3: «No confirmo todavía cuál proforma debe sustituirse ni el nuevo total.» | faltante: sustitución expresa y versión aplicable al cambio |

Comprobación decimal de R1: 20 × USD 80.00 = USD 1600.00; USD 1600.00 + USD 0.00 (impuestos) + USD 0.00 (otros cargos) = USD 1600.00. Es coherente para sus 20 unidades. No se calcula ni se atribuye un total aprobado a 24 sillas. Los costos excluidos no equivalen a cero del costo final; este no está cuantificado y no se exige su importe como bloqueante.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base | satisfecho | PDF encabezado y correo párr. 1: DEMO-004, importación. |
| P02 | Sí, base | satisfecho | PDF Cliente/contacto; remitente y firma del correo. |
| P03 | Sí, base | satisfecho | PDF Proyecto/Destino: residencial, Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí, L1 | contradictorio | PDF L1: 20 unidades; correo párr. 2: 24 sillas. Identificador, descripción y unidad disponibles. |
| P05 | Sí, L1 | contradictorio | PDF Dimensiones/Material aportados; Acabado negro mate frente a blanco mate del correo párr. 2. |
| P06 | Sí, L1 | satisfecho | PDF L1 declara ruta importación y correo solicita esa etapa. |
| P07 | Sí, base | faltante | R1 declara USD, precio, subtotal, cargos, total y pago coherentes para 20 unidades; correo párr. 3 no confirma nuevo total y no aporta condiciones comerciales actualizadas. No hay dos importes incompatibles declarados. |
| P08 | Sí, base | satisfecho | PDF Preparación/Transporte e instalación: hitos explícitos, plazos y exclusión de instalación. |
| P09 | Sí, base | contradictorio | Correo identificado por remitente/fecha/asunto. PDF DEMO-PF-004 R1 con fecha, vínculo y aceptación atribuida; no está resuelta la versión aplicable al alcance discrepante. Correo párr. 3 no confirma sustitución. |
| P10 | Sí, base | faltante | PDF contiene aceptación explícita de R1 por Luis Demo el 2026-11-17. No hay aceptación del alcance modificado vinculada a una revisión actualizada; el correo pide cambios sin confirmarla. |
| F01 | No | NA | L1 tiene ruta explícita importación; no se declara fabricación. |
| F02 | No | NA | No hay línea de fabricación en las fuentes recibidas. |
| F03 | No | NA | No hay línea de fabricación que active aprobación técnica de plano/ficha. |
| F04 | No | NA | Ruta importación; tampoco se declara fabricación ajustada a espacio existente. |
| F05 | No | NA | No se solicita etapa ni ruta de fabricación. |
| I01 | Sí, importación | satisfecho | PDF Proveedor/encabezado/vigencia: Demo Furniture Export, DEMO-PF-004 R1, 2026-11-17, hasta 2026-12-01 inclusive. |
| I02 | Sí, L1 importada | contradictorio | L1/S-20 tiene dimensiones, material y acabado en PDF; 20/negro mate discrepan de 24/blanco mate del correo. |
| I03 | Sí, importación | satisfecho | PDF País de despacho China; país de entrega Panamá y destino identificado. |
| I04 | Sí, importación | faltante | R1 declara moneda, pago, precio/total y alcance de costos. Falta versión comercial aplicable a 24/blanco mate y nuevo total que el correo deja sin confirmar. Las exclusiones expresas satisfacen el alcance de costos. |
| I05 | Sí, importación | satisfecho | PDF: preparación 30 días calendario desde anticipo; transporte estimado 35 días calendario desde despacho. No es exigible llegada firme adicional. |
| I06 | No, condición ausente | NA | PDF declara expresamente que no se ha usado Incoterm; costos evaluados con I04. |

## 6. Hallazgos

| Hallazgo | Requisito | Evidencia y consecuencia documental | Acción requerida |
|---|---|---|---|
| H01 | P04, I02 | PDF R1: 20 unidades; correo párr. 2: 24 sillas L1. Cantidad aplicable no conciliada. | Confirmar cantidad definitiva de L1 e incorporarla a la proforma/revisión aplicable. |
| H02 | P05, I02 | PDF R1: negro mate; correo párr. 2: blanco mate. Acabado aplicable no conciliado. | Confirmar acabado definitivo e incorporarlo a la revisión aplicable. |
| H03 | P07, I04 | USD 1600.00 corresponde a 20 unidades R1; correo párr. 3 no confirma nuevo total. No existe importe nuevo declarado para comparar. | Aportar proforma actualizada con precio, subtotal, cargos declarados, total y condición de pago aplicables al alcance confirmado. Mantener explícito el alcance de costos. |
| H04 | P09, P10 | R1 tiene aceptación identificada y fechada; el correo posterior no confirma sustitución ni acepta una nueva revisión identificada. No puede elegirse una fuente por su fecha. | Aportar evidencia explícita de qué documento/revisión sustituye a cuál, y aprobación/aceptación del alcance y revisión finales con identidad y fecha. Conservar el antecedente R1. |

## 7. Preguntas y siguiente acción humana

Resolver conjuntamente:

1. H01–H02: ¿La cantidad y acabado definitivos de L1 son 24 sillas/blanco mate, 20 unidades/negro mate u otros valores expresamente confirmados?
2. H03: ¿Cuál es la proforma revisada que declara las condiciones comerciales y el total para esos valores confirmados?
3. H04: ¿Qué documento/revisión sustituye expresamente a DEMO-PF-004 R1 y dónde consta su aprobación y aceptación por el cliente, con identidad, fecha y referencia exacta a la revisión y alcance?

Siguiente acción humana: conciliar esos puntos y aportar la revisión y constancias correspondientes para una nueva revisión documental. Este informe no aprueba ni ejecuta el pedido.

## 8. Límites

Revisión exclusivamente documental de las fuentes autorizadas recibidas. No se comprobaron externamente identidad, autenticidad, autoridad, precios, factibilidad, calidad de materiales ni cumplimiento técnico o legal. No se ejecutaron compra, fabricación, importación, instalación ni comunicaciones externas. PEO-01 es un perfil de demostración, no una lista universal impuesta por ISO. Este informe no acredita certificación ni conformidad ISO y no emite veredicto de prueba.