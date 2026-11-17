# Informe documental — DEMO-002

## 1. Identificación

- Expediente: DEMO-002, ficticio, solo prueba técnica; no se atribuye a un ERP real.
- Revisión de análisis: S1, primera revisión aportada a este análisis.
- Etapa solicitada: importación, antes del pedido al proveedor.
- Ruta: importación para L1; no se declara fabricación.
- Skill aplicada: revisor-expedientes-mobiliario, versión de instrucciones 1.0. Perfil: PEO-01 v1.0.

## 2. Fuentes

Documento recibido y leído íntegramente mediante extracción local propia con pypdf: `pruebas/entradas/E2E-02-proforma.pdf`, una página. Todas las referencias de este informe corresponden a su página 1. Documento identificado como DEMO-PF-002, R1, fecha 2026-11-17, vinculado expresamente a DEMO-002 y L1; vigencia hasta 2026-12-01 inclusive.

La lectura comprendió la única página del PDF mediante `PdfReader` y `page.extract_text()`. No se utilizó OCR, renderizado visual ni extracción de terceros. El texto original extraído se conserva en `texto-extraido.txt` y el método en `metodo-lectura.txt`. No se observaron campos textuales ilegibles en la extracción. La aceptación se aporta como constancia dentro de la proforma; no como correo independiente ni como comprobación de autenticidad.

Fuentes normativas internas recibidas y leídas completas: `SKILL.md` y `PERFIL-EXPEDIENTE.md`. No se recibieron revisiones anteriores del expediente, archivos adicionales ni documentos referenciados ausentes. No se identificaron archivos recibidos imposibles de leer.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA.** Los requisitos obligatorios aplicables están satisfechos documentalmente y no se identificaron contradicciones pendientes. La exclusión expresa de transportes y tributos delimita el total de la proforma y no equivale a declarar que esos costos sean cero. El estado no autoriza la importación ni la compra.

## 4. Datos normalizados

Todos los datos siguientes están **aportados**, excepto las ausencias expresamente indicadas. La procedencia es DEMO-PF-002 R1, página 1, campo señalado.

| Campo / alcance | Valor original y dato registrado | Procedencia |
|---|---|---|
| Identificación y etapa | «Expediente: DEMO-002. Etapa solicitada: importación.» | Expediente / etapa |
| Cliente y contacto | «Residencia Beta Demo»; «beta@cliente.example» | Cliente / contacto |
| Proyecto y uso | «mobiliario residencial, sillas de comedor» | Proyecto |
| Destino | «Casa Demo B, Ciudad de Panamá, Panamá» | Destino |
| Proveedor y contacto | «Demo Furniture Export»; «ventas@exportador.example» | Proveedor / contacto |
| Línea y producto | «L1: silla modelo S-20» | L1 |
| Cantidad y unidad | «20 unidades» | L1 |
| Ruta | «ruta importación» | L1 |
| Dimensiones | «Dimensiones L x A x H: 500 x 550 x 850 mm.» Largo 500 mm, ancho 550 mm, alto 850 mm, conservando la notación de ejes L × A × H de la fuente. No se convirtió la unidad. | Dimensiones |
| Material | «estructura de acero y asiento de polipropileno» | Material |
| Acabado | «negro mate» | Acabado |
| Moneda / precio / subtotal | «USD 80.00» unitario; «USD 1600.00» subtotal | Precio unitario / subtotal |
| Embalaje | «incluido» | Embalaje |
| Transporte internacional / local | «excluido» / «excluido»; importes: NO APORTADOS, no se tratan como cero | Alcance de costos |
| Tributos de importación | «excluidos»; importe: NO APORTADO, no se trata como cero | Alcance de costos |
| Impuestos de esta proforma / otros cargos | «USD 0.00» / «USD 0.00» | Impuestos / otros cargos |
| Total proforma | «USD 1600.00. El total es de mercancía, no costo final puesto en destino.» | Total |
| Pago | «30 % al confirmar pedido y 70 % antes del despacho» | Pago |
| País de despacho / entrega | «China» / «Panamá»; país de fabricación: NO APORTADO, no se deduce del despacho | Países |
| Preparación | «30 días calendario desde recepción del anticipo» | Preparación |
| Transporte | «estimado 35 días calendario desde despacho» | Transporte |
| Llegada | «no hay fecha firme de llegada»; fecha firme: NO APORTADA | Transporte / llegada |
| Instalación | «No incluye instalación.» | Alcance del servicio |
| Incoterm | «Las partes no han usado Incoterm en esta proforma.» | Incoterm |
| Documento / revisión / fecha / vigencia | «PROFORMA DEMO-PF-002 | R1 | Fecha: 2026-11-17»; «hasta 2026-12-01 inclusive» | Cabecera / vigencia |
| Versión aprobada | «Especificación y condiciones aprobadas: DEMO-PF-002 R1.» | Aprobación |
| Aceptación del cliente | «Constancia ficticia de aceptación del cliente: Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-002 R1.» | Constancia de aceptación |

Comprobación aritmética decimal de apoyo, a centavos: 20 × USD 80.00 = USD 1600.00; USD 1600.00 + USD 0.00 (impuestos de esta proforma) + USD 0.00 (otros cargos) = USD 1600.00. Coincide con subtotal y total declarados. No se agregaron valores a los costos excluidos ni se calculó un costo final puesto en destino. No se sumaron plazos para prometer una fecha de llegada.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de pedido | satisfecho | Pág. 1, expediente DEMO-002 y etapa importación explícitos. |
| P02 | Sí | satisfecho | Pág. 1, Residencia Beta Demo y beta@cliente.example. |
| P03 | Sí | satisfecho | Pág. 1, mobiliario residencial; Casa Demo B, Ciudad de Panamá, Panamá. Destino identificado para la demostración. |
| P04 | Sí | satisfecho | Pág. 1, identificador único L1, silla S-20, 20 unidades positivas. |
| P05 | Sí | satisfecho | Pág. 1, L × A × H 500 × 550 × 850 mm, estructura de acero y asiento de polipropileno, negro mate. |
| P06 | Sí | satisfecho | Pág. 1, ruta importación explícita en L1. |
| P07 | Sí | satisfecho | Pág. 1, USD, unitario, subtotal, impuestos y otros cargos, total y pago definidos; cálculo coherente. Costos de transporte y tributos de importación expresamente excluidos del total de mercancía. |
| P08 | Sí | satisfecho | Pág. 1, preparación desde recepción del anticipo y transporte estimado desde despacho; destino identificado y exclusión de instalación explícita. Se conserva el carácter estimado, sin prometer llegada. |
| P09 | Sí | satisfecho | Pág. 1, DEMO-PF-002 R1, fecha 2026-11-17; relación con DEMO-002 y L1; especificaciones y condiciones aprobadas para esa revisión y constancia de aceptación exacta. |
| P10 | Sí | satisfecho | Pág. 1, constancia ficticia de Luis Demo, contacto y fecha 2026-11-17, aceptación expresa de líneas y condiciones de DEMO-PF-002 R1. Se registra la evidencia documental, sin acreditar autoridad o autenticidad. |
| F01 | No | NA | L1 declara solo importación; no hay línea con ruta fabricación a revisar. |
| F02 | No | NA | Etapa/ruta de importación; no se activa la ficha de fabricación. |
| F03 | No | NA | No se declara fabricación; no se activa aprobación técnica de fabricación. |
| F04 | No | NA | No hay ruta fabricación ni declaración de fabricación ajustada a espacio existente. |
| F05 | No | NA | L1 corresponde a importación; sus plazos se evalúan en P08 e I05. |
| I01 | Sí | satisfecho | Pág. 1, proveedor Demo Furniture Export; proforma disponible DEMO-PF-002, fecha 2026-11-17, R1, vigencia explícita hasta 2026-12-01 inclusive. |
| I02 | Sí | satisfecho | Pág. 1, L1/S-20, 20 unidades, dimensiones con unidad, material y acabado están en la proforma y quedan incluidos en su aceptación expresa. |
| I03 | Sí | satisfecho | Pág. 1, despacho China, entrega Panamá y destino Casa Demo B. No se identifica China como origen de fabricación. |
| I04 | Sí | satisfecho | Pág. 1, moneda, pago, precios y total; embalaje incluido; transportes internacional y local y tributos de importación excluidos; total expresamente limitado a mercancía. |
| I05 | Sí | satisfecho | Pág. 1, preparación 30 días calendario desde recepción del anticipo; transporte estimado 35 días calendario desde despacho. Hitos explícitos; la ausencia de fecha firme se declara y no invalida la alternativa de plazos con hitos prevista por el perfil. |
| I06 | No, condición no activada | NA | Pág. 1 declara expresamente que las partes no han usado Incoterm. No se inventa término, lugar o edición; costos evaluados en I04. |

## 6. Hallazgos

No se identificaron faltantes obligatorios, contradicciones ni datos no legibles que bloqueen la revisión humana.

**H01 — Alcance comercial y temporal delimitado, informativo.** Requisitos P07, P08, I04 e I05. DEMO-PF-002 R1, pág. 1, declara total de mercancía USD 1600.00 y excluye transporte internacional, transporte local y tributos de importación; declara transporte estimado y ausencia de fecha firme de llegada. Consecuencia documental: ni costo final puesto en destino ni llegada firme pueden afirmarse con esta fuente. Acción requerida en la revisión humana: conservar estas exclusiones y el carácter estimado del transporte al valorar el alcance aceptado. No constituye un faltante obligatorio según el perfil aplicado.

## 7. Preguntas y siguiente acción humana

No hay preguntas bloqueantes para completar los requisitos documentales aplicables. Corresponde a la revisión humana examinar DEMO-PF-002 R1 y su constancia ficticia de aceptación, manteniendo las exclusiones de costos, el transporte estimado y la vigencia declarada. Este informe no aprueba ni ejecuta pedidos, compras, importaciones o instalaciones.

## 8. Límites

Revisión exclusivamente documental, basada en la única proforma recibida y en PEO-01 v1.0. Los datos y la constancia ficticia son afirmaciones de la fuente, sin comprobación externa. No se verificaron autenticidad, autoridad del aceptante, factibilidad técnica, calidad de materiales ni cumplimiento legal o aduanero. No se efectuaron acciones externas. No se atribuyen los campos del perfil a una norma ISO ni se afirma certificación o conformidad ISO. No se recibió revisión anterior de análisis para comparar cambios.
