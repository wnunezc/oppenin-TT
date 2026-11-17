# Informe documental

## 1. Identificación

Expediente **DEMO-004**, ficticio, solo prueba técnica. Revisión de análisis 1 de este informe; no se aportó revisión de análisis anterior. Etapa: **importación**, antes del pedido al proveedor. Ruta de L1: importación, declarada en proforma. Perfil aplicado: **PEO-01 v1.0**, skill revisor-expedientes-mobiliario, versión de instrucciones 1.0.

## 2. Fuentes

- `E2E-04-correo.md`: asunto «Datos para expediente DEMO-004»; fecha declarada 2026-11-18 10:00 UTC-05:00; remitente beta@cliente.example; firma Luis Demo. Sin identificador de revisión. Párrafos de cuerpo: 1 solicita etapa importación; 2 solicita 24 sillas y blanco mate; 3 no confirma proforma a sustituir ni nuevo total; 4 firma. La fecha es transcripción de la fuente, no comprobación externa.
- `E2E-04-proforma.pdf`: abierto y leído en su única página mediante extracción de texto con pypdf, sin OCR ni comprobación visual de apariencia. Documento DEMO-PF-004, R1, fecha 2026-11-17, vinculado a DEMO-004 y L1; vigencia hasta 2026-12-01 inclusive. Texto extraído conservado en `extraccion-pdf.txt`.
- No hay archivos recibidos ilegibles ni otros adjuntos declarados existentes. No se aportó documento que resuelva la sustitución, el total actualizado y la aceptación del alcance solicitado en el correo. Esto es evidencia faltante; no se presume la existencia de otra proforma o revisión.

## 3. Estado global

**CONFLICTO DOCUMENTAL.** L1 figura con 20 unidades y negro mate en DEMO-PF-004 R1, mientras el correo pide 24 sillas y blanco mate. El correo deja expresamente sin confirmar qué proforma se sustituye y el nuevo total. La fecha más reciente no determina por sí sola una versión aplicable aceptada.

## 4. Datos normalizados

Los estados corresponden al dato documental, sin comprobar autenticidad, autoridad o realidad externa.

| Campo | Valor original / normalizado | Estado y procedencia |
|---|---|---|
| Expediente / etapa | DEMO-004 / importación | Aportado: correo, asunto y cuerpo ¶1; PDF p.1, expediente/etapa |
| Cliente / contacto | Residencia Beta Demo / beta@cliente.example; firma Luis Demo | Aportado: PDF p.1, cliente/contacto; correo encabezado y ¶4 |
| Proyecto / uso | Mobiliario residencial, sillas de comedor | Aportado: PDF p.1, proyecto |
| Destino | Casa Demo B, Ciudad de Panamá, Panamá | Aportado: PDF p.1, destino |
| Línea / producto | L1, silla modelo S-20 | Aportado: PDF p.1, L1; correo ¶2 identifica L1 como sillas |
| Cantidad / unidad | PDF: «20 unidades»; correo: «24 sillas» | Contradictorio: PDF p.1 L1 frente a correo ¶2. Se conservan ambos valores |
| Largo / ancho / alto | «Dimensiones L x A x H: 500 x 550 x 850 mm»; largo 500 mm, ancho 550 mm, alto 850 mm | Aportado: PDF p.1, dimensiones. Sin conversiones necesarias |
| Material | «estructura de acero y asiento de polipropileno» | Aportado: PDF p.1, material. El correo no aporta modificación del material |
| Acabado | PDF: «negro mate»; correo: «blanco mate» | Contradictorio: PDF p.1, acabado, frente a correo ¶2 |
| Ruta | Importación | Aportado: PDF p.1, L1 |
| Proveedor | Demo Furniture Export / ventas@exportador.example | Aportado: PDF p.1, proveedor |
| Proforma | DEMO-PF-004, R1, 2026-11-17; vigente hasta 2026-12-01 inclusive | Aportado: PDF p.1, cabecera/vigencia. Aplicabilidad al cambio pendiente |
| Moneda / precio unitario | USD / USD 80.00 | Aportado para R1: PDF p.1, precio. Precio aceptado para 24 sillas blanco mate: NO APORTADO |
| Subtotal / impuestos / otros cargos / total | R1: USD 1600.00 / USD 0.00 / USD 0.00 / USD 1600.00 | Aportado para R1: PDF p.1, importes. Nuevo total: NO APORTADO, correo ¶3 |
| Costos incluidos / excluidos | Embalaje incluido; transporte internacional, transporte local y tributos de importación excluidos | Aportado: PDF p.1, costos. No equivalen a costos cero. Costo final puesto en destino: NO APORTADO; R1 declara que su total es solo mercancía |
| Pago | «30 % al confirmar pedido y 70 % antes del despacho» | Aportado para R1: PDF p.1, pago |
| Despacho / entrega | China / Panamá | Aportado: PDF p.1, países. No se identifica país de fabricación ni se deduce del despacho |
| Preparación | «30 días calendario desde recepción del anticipo» | Aportado: PDF p.1, preparación |
| Transporte | «estimado 35 días calendario desde despacho»; «no hay fecha firme de llegada» | Aportado como estimación: PDF p.1, transporte. No se suma para prometer fecha de llegada |
| Instalación | «No incluye instalación» | Aportado: PDF p.1, alcance |
| Incoterm | «Las partes no han usado Incoterm en esta proforma» | Aportado: PDF p.1, Incoterm |
| Aceptación | «Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-004 R1» | Aportado para R1: PDF p.1, constancia ficticia. Aceptación de revisión que incorpore 24 sillas blanco mate: NO APORTADA |

Comprobación decimal de R1 a centavos: **20 × USD 80.00 = USD 1600.00**; **USD 1600.00 + USD 0.00 (impuestos de proforma) + USD 0.00 (otros cargos) = USD 1600.00**. Coincide internamente con el total de R1. No se incluyen importes desconocidos de transporte y tributos excluidos; no se calcula un total para el cambio solicitado.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base | satisfecho | DEMO-004 e importación explícitos en correo ¶1 y PDF p.1; identificador ficticio, sin atribución a ERP |
| P02 | Sí, base | satisfecho | PDF p.1, Residencia Beta Demo y contacto beta@cliente.example |
| P03 | Sí, base | satisfecho | PDF p.1, proyecto residencial y Casa Demo B, Ciudad de Panamá, Panamá |
| P04 | Sí, L1 | contradictorio | L1 identificada; 20 unidades en PDF p.1 y 24 sillas en correo ¶2, ambas positivas pero incompatibles |
| P05 | Sí, L1 | contradictorio | PDF p.1 contiene ejes, mm y material; acabado negro mate frente a blanco mate del correo ¶2 |
| P06 | Sí, L1 | satisfecho | PDF p.1 declara ruta importación |
| P07 | Sí, base | faltante | R1 aporta moneda, precio, subtotal, impuestos, cargos, total y pago; aritmética interna correcta. Correo ¶3 deja sin confirmar nuevo total para alcance modificado |
| P08 | Sí, base | satisfecho | PDF p.1 declara preparación desde anticipo, transporte estimado desde despacho y exclusión de instalación. No hay compromiso firme de llegada |
| P09 | Sí, base | contradictorio | R1 identificada, fechada y aceptada; correo posterior cambia cantidad/acabado y no confirma sustitución. No hay versión aplicable resuelta para el alcance modificado |
| P10 | Sí, base | faltante | Constancia ficticia con Luis Demo y fecha para R1 en PDF p.1; falta aceptación explícita de alcance/revisión que resuelva los cambios del correo |
| F01 | No | NA | L1 declarada solo importación; no hay línea de fabricación |
| F02 | No | NA | No se revisa fabricación ni existe línea con esa ruta declarada |
| F03 | No | NA | No se revisa fabricación ni existe línea con esa ruta declarada |
| F04 | No | NA | No hay ruta de fabricación; tampoco se declara fabricación ajustada a espacio existente |
| F05 | No | NA | L1 declarada solo importación |
| I01 | Sí, importación | satisfecho | PDF p.1: proveedor Demo Furniture Export, proforma disponible DEMO-PF-004 R1, fecha y vigencia explícitas; conflicto de aplicabilidad tratado en P09 |
| I02 | Sí, L1 | contradictorio | PDF p.1 identifica modelo S-20, cantidad, dimensiones/material/acabado; cantidad y acabado incompatibles con correo ¶2 |
| I03 | Sí, importación | satisfecho | PDF p.1: despacho China y entrega Panamá, con destino Casa Demo B |
| I04 | Sí, importación | faltante | R1 explicita moneda, pago, importes y costos incluidos/excluidos. Correo ¶3 no confirma nuevo total; falta condición comercial documentada para resolver el alcance cambiado |
| I05 | Sí, importación | satisfecho | PDF p.1: preparación 30 días desde anticipo y transporte estimado 35 días desde despacho; hitos explícitos, sin fecha firme de llegada |
| I06 | No, condición no activada | NA | PDF p.1 declara expresamente que no se usó Incoterm; alcance de costos evaluado en I04 |

## 6. Hallazgos

| ID | Requisito | Valores/documentos | Consecuencia documental | Acción requerida |
|---|---|---|---|---|
| H01 | P04, I02 | PDF p.1 L1: 20 unidades; correo ¶2: 24 sillas | Cantidad aplicable no resuelta | Confirmar cantidad y documentarla en la versión que resulte aplicable, con aceptación |
| H02 | P05, I02 | PDF p.1: negro mate; correo ¶2: blanco mate | Especificación de acabado incompatible | Confirmar acabado e incorporarlo a la versión aplicable aceptada |
| H03 | P09, P10 | PDF p.1: aceptación de R1 por Luis Demo el 2026-11-17; correo ¶2-3: cambios y sustitución sin confirmar | La aceptación documentada de R1 no acredita aceptación de los cambios; no puede elegirse una versión por su fecha | Aportar evidencia explícita de qué documento/revisión se mantiene o sustituye y aceptación del alcance resultante, con identidad y fecha |
| H04 | P07, I04 | R1: USD 80.00/unidad, total mercancía USD 1600.00; correo ¶3: nuevo total sin confirmar | La coherencia aritmética de R1 no resuelve los importes del alcance modificado | Aportar precio, subtotal, cargos/impuestos declarados, total y pago aplicables al alcance final; confirmar alcance de costos, conservando explícitas las exclusiones |

## 7. Preguntas y siguiente acción humana

1. ¿Se mantiene L1 con 20 unidades negro mate de DEMO-PF-004 R1, o se solicita sustituirla por 24 sillas blanco mate? Aportar confirmación explícita que resuelva ambos datos.
2. ¿Qué documento y revisión quedan aplicables y cuáles se sustituyen? Aportar esa evidencia y la aceptación expresa del alcance resultante con identidad y fecha.
3. Para el alcance final, ¿cuáles son precio unitario, subtotal, impuestos/cargos declarados, total de mercancía y condición de pago? Confirmar también qué costos permanecen incluidos, excluidos o pendientes. Si se necesita conocer el costo final en destino, documentar los costos pendientes; no tratarlos como cero.

La siguiente acción humana es conciliar estos puntos y aportar la documentación resultante para una nueva revisión, conservando este informe. No se aprueba ni ejecuta el pedido o la importación. No se exigen documentos aduaneros o de embarque ya emitidos para una operación todavía no iniciada.

## 8. Límites

Revisión exclusivamente documental de los dos archivos recibidos. La lectura del PDF se realizó por extracción de texto, no por inspección visual ni OCR; se leyó la única página y no se detectó ilegibilidad en el texto extraído. Datos, constancia de aceptación, identidad y fechas se registran tal como fueron aportados, sin comprobación externa de autenticidad, autoridad, factibilidad, material, calidad o cumplimiento técnico/legal. No hubo consultas de red ni acciones externas. PEO-01 es un perfil de demostración: este informe no certifica ISO ni acredita conformidad normativa. No existe revisión de análisis anterior aportada para comparar cambios.
