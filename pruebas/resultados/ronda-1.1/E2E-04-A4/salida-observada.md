# Informe documental — DEMO-004

## 1. Identificación

Expediente DEMO-004. Revisión de análisis: revisión independiente 1 de esta sesión E2E-04-A4; no es una revisión de la proforma. Etapa: importación, antes del pedido al proveedor. Ruta de L1: importación. Perfil aplicado: PEO-01 v1.1; skill v1.1. Expediente expresamente ficticio, solo prueba técnica. Las fechas declaradas se conservan como datos del expediente, separadas de los sellos reales de esta sesión.

## 2. Fuentes

- **C:** `E2E-04-correo.md`, remitente beta@cliente.example, fecha 2026-11-18 10:00 UTC-05:00, asunto «Datos para expediente DEMO-004», firmado «Luis Demo.». Sin identificador ni revisión propios declarados; no se inventan. Párrafo 1: etapa y expediente; párrafo 2: cantidad y acabado; párrafo 3: sustitución y total no confirmados; párrafo 4: firma.
- **P:** `E2E-04-proforma.pdf`, abierta directamente con pypdf e iteradas todas sus páginas (1 página). DEMO-PF-004, R1, fecha 2026-11-17, vigencia hasta 2026-12-01 inclusive; vinculada a DEMO-004 y L1. Extracción propia conservada en `extraccion-proforma.txt`. El texto extraído es legible y contiene los campos y la constancia de aceptación; no se utilizó visión ni OCR.
- Reglas leídas íntegramente: `SKILL.md` y `PERFIL-EXPEDIENTE.md`.
- Documentos referenciados ausentes: no se menciona por nombre o identificador otro adjunto; no se ha recibido una proforma que documente los cambios solicitados. Archivos recibidos no legibles: ninguno identificado. Informe anterior aportado: ninguno.

En las tablas, C remite al correo identificado arriba y P a la página 1 de la proforma; se indica además el campo o párrafo. Todos los hechos son aportaciones documentales, sin comprobación externa.

## 3. Estado global

**CONFLICTO DOCUMENTAL.** C solicita 24 sillas en blanco mate; P documenta 20 unidades en negro mate. C declara expresamente que todavía no confirma cuál proforma debe sustituirse ni el nuevo total. No hay evidencia de sustitución y aceptación de los cambios; la fecha posterior del correo no hace prevalecer automáticamente su contenido.

## 4. Datos normalizados

| Dato | Valor original y procedencia | Estado documental |
|---|---|---|
| Expediente y etapa | C, párrafo 1: «etapa importación de DEMO-004»; P, campo Expediente: DEMO-004, importación | aportado |
| Cliente y contacto | P, Cliente: «Residencia Beta Demo»; «beta@cliente.example»; C, encabezado y firma: beta@cliente.example, Luis Demo | aportado |
| Proyecto, uso y destino | P: «mobiliario residencial, sillas de comedor»; «Casa Demo B, Ciudad de Panamá, Panamá» | aportado |
| Línea y producto | P, L1: «silla modelo S-20»; C, párrafo 2: «línea L1» y «sillas» | aportado |
| Cantidad y unidad L1 | P, L1: «20 unidades»; C, párrafo 2: «24 sillas» | contradictorio |
| Dimensiones L1 | P, Dimensiones: «L x A x H: 500 x 550 x 850 mm»; largo 500 mm, ancho 550 mm, alto 850 mm | aportado |
| Material L1 | P, Material: «estructura de acero y asiento de polipropileno» | aportado |
| Acabado L1 | P, Acabado: «negro mate»; C, párrafo 2: «blanco mate» | contradictorio |
| Ruta L1 y proveedor | P: «ruta importación»; «Demo Furniture Export», «ventas@exportador.example» | aportado |
| Precio y subtotal R1 | P: «Precio unitario: USD 80.00. Subtotal: USD 1600.00» | aportado para R1; no confirmado para el cambio |
| Cargos e impuestos R1 | P: embalaje incluido; impuestos de esta proforma USD 0.00; otros cargos USD 0.00 | aportado |
| Exclusiones R1 | P: transporte internacional, transporte local y tributos de importación excluidos; total de mercancía, no costo final puesto en destino | aportado; no se consideran costos finales cero |
| Total | P: «Total proforma: USD 1600.00»; C, párrafo 3: «No confirmo todavía [...] el nuevo total»; total para el alcance modificado: NO APORTADO | faltante para el cambio |
| Pago | P: «30 % al confirmar pedido y 70 % antes del despacho» | aportado |
| Países | P: despacho China; entrega Panamá; no se declara país de fabricación | aportado para despacho y entrega |
| Plazos | P: preparación 30 días calendario desde recepción del anticipo; transporte estimado 35 días calendario desde despacho; sin fecha firme de llegada | aportado; no se suma para prometer llegada |
| Instalación | P: «No incluye instalación» | aportado |
| Incoterm | P: «Las partes no han usado Incoterm en esta proforma» | aportado; control I06 NA |
| Documento y vigencia | P: DEMO-PF-004, R1, fecha 2026-11-17, vigencia hasta 2026-12-01 inclusive, expediente DEMO-004, L1 | aportado |
| Aprobación/aceptación R1 | P, constancia: «Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-004 R1» | aportado para R1 |
| Sustitución y aceptación de cambios | C, párrafo 3: «No confirmo todavía cuál proforma debe sustituirse ni el nuevo total»; documento/revisión sustituto y aceptación del alcance modificado: NO APORTADO | faltante |

Comprobación aritmética decimal de R1: 20 × USD 80.00 = USD 1600.00; USD 1600.00 + USD 0.00 (impuestos de proforma) + USD 0.00 (otros cargos) = USD 1600.00. Coincide con el total de mercancía de R1. Esta comprobación no fija el total del alcance cambiado. Los costos expresamente excluidos no están cuantificados ni se requieren para validar ese total de mercancía.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de pedido | satisfecho | C párrafo 1 y P campo Expediente: DEMO-004, importación; identificador ficticio, no atribuido a ERP real. |
| P02 | Sí | satisfecho | P Cliente/contacto: Residencia Beta Demo y beta@cliente.example. |
| P03 | Sí | satisfecho | P Proyecto/destino: mobiliario residencial; Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí | contradictorio | L1 identificada; P 20 unidades frente a C párrafo 2, 24 sillas. Ambas cantidades positivas, pero incompatibles para el mismo alcance. |
| P05 | Sí | contradictorio | P aporta ejes, mm y material; acabado negro mate frente a blanco mate en C párrafo 2. |
| P06 | Sí | satisfecho | P L1 y C etapa: importación explícita. |
| P07 | Sí | faltante | P contiene condiciones comerciales y aritmética coherentes para R1; C párrafo 3 no confirma nuevo total. Condiciones/total del alcance modificado no documentados. |
| P08 | Sí | satisfecho | P preparación desde anticipo y transporte desde despacho; instalación excluida. No se exige fecha de llegada firme. |
| P09 | Sí | faltante | C identificado por remitente, fecha y asunto. P tiene número, fecha, R1 y aceptación atribuida con identidad y fecha. Falta documentar qué versión sustituye a cuál y la versión aplicable/aprobada para los cambios; la aprobación histórica de R1 se conserva. |
| P10 | Sí | faltante | P contiene aceptación expresa de R1 por Luis Demo el 2026-11-17; no se aporta aceptación explícita del alcance y revisión modificados. C no confirma sustitución ni total. |
| F01 | No | NA | L1 solo tiene ruta importación; no hay línea declarada de fabricación. |
| F02 | No | NA | No hay ruta de fabricación declarada. |
| F03 | No | NA | No hay ruta de fabricación declarada. |
| F04 | No | NA | No hay fabricación ni ajuste a espacio existente declarado. |
| F05 | No | NA | No hay ruta de fabricación declarada. |
| I01 | Sí, importación | satisfecho | P identifica Demo Furniture Export y proforma DEMO-PF-004 R1, 2026-11-17, vigente hasta 2026-12-01 inclusive. |
| I02 | Sí | contradictorio | P L1 modelo S-20, dimensiones/material y 20 unidades negro mate; C L1 pide 24 sillas blanco mate. No existe correspondencia resuelta de cantidad y acabado. |
| I03 | Sí | satisfecho | P países: despacho China, entrega Panamá; no se confunde despacho con origen de fabricación. |
| I04 | Sí | faltante | P declara USD, pago, precios, total y alcance de costos; C no confirma el nuevo total. Falta documentación comercial del alcance cambiado, no importes de transporte/tributos excluidos. |
| I05 | Sí | satisfecho | P preparación 30 días calendario desde anticipo y transporte estimado 35 días calendario desde despacho; hitos explícitos. |
| I06 | No, condición no activada | NA | P declara expresamente que no se ha usado Incoterm. El alcance de costos se revisa con I04. |

## 6. Hallazgos

| Hallazgo | Requisito | Valores/documentos involucrados | Consecuencia documental | Acción requerida |
|---|---|---|---|---|
| H01 | P04, I02 | P L1: 20 unidades; C párrafo 2: 24 sillas | Cantidad de L1 contradictoria; no se puede fijar alcance único. | Confirmar cantidad aplicable y reflejarla en la documentación controlada que corresponda. |
| H02 | P05, I02 | P acabado negro mate; C párrafo 2 blanco mate | Acabado de L1 contradictorio. | Confirmar acabado aplicable y documentarlo en la versión correspondiente. |
| H03 | P07, I04 | P R1 USD 1600.00 para 20 unidades; C párrafo 3 no confirma nuevo total | El total de R1 está comprobado aritméticamente, pero no resuelve las condiciones comerciales de los cambios. | Aportar documento con cantidad/acabado acordados, precio unitario, subtotal, cargos/impuestos declarados, total, moneda y pago del alcance modificado, o aclarar expresamente la vigencia del alcance R1. |
| H04 | P09, P10 | P aceptación explícita de R1 por Luis Demo, 2026-11-17; C sin confirmación de sustitución | La evidencia de aceptación de R1 no acredita aceptación de una versión modificada ni resuelve qué documento será aplicable. | Aportar referencia explícita de sustitución o mantenimiento de versión y evidencia atribuida, con identidad y fecha, de aprobación/aceptación del alcance y revisión que resulten aplicables. |

## 7. Preguntas y siguiente acción humana

1. **H01–H02:** ¿Qué cantidad y acabado deben quedar aplicables a L1: los 20/negro mate de R1 o los 24/blanco mate solicitados en el correo? Documentar la resolución sin borrar ninguno de los antecedentes.
2. **H03:** ¿Cuáles son las condiciones comerciales y el total del alcance que se confirme? Aportar la proforma controlada correspondiente con sus importes declarados; no basta trasladar automáticamente el total de R1.
3. **H04:** ¿Qué documento y revisión se mantienen o sustituyen expresamente, y qué evidencia con identidad y fecha acredita su aprobación y la aceptación del cliente del alcance final?

Siguiente acción humana: reunir esas aclaraciones y documentos y someterlos a una revisión documental nueva conservando este informe y los antecedentes. Este informe no aprueba pedido ni importación.

## 8. Límites

Revisión exclusivamente documental de las fuentes recibidas. No se ha verificado externamente identidad, autoridad, autenticidad, calidad material, factibilidad técnica ni cumplimiento legal o aduanero. Las constancias se registran como evidencia ficticia aportada. No se emite certificación ni declaración de conformidad ISO; PEO-01 es un perfil de demostración. No se hicieron consultas de red ni acciones externas.