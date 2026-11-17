# Informe documental

## 1. Identificación

Expediente **DEMO-002**. Revisión de análisis: **1**, sin antecedentes aportados. Etapa: **importación**, antes del pedido al proveedor. Ruta de L1: importación. Perfil aplicado: **PEO-01 v1.0**, con la skill `revisor-expedientes-mobiliario`, versión de instrucciones 1.0. Expediente **ficticio, solo prueba técnica**, según la página 1 de la fuente.

## 2. Fuentes

- `pruebas/entradas/E2E-02-proforma.pdf`: una página, abierta y extraída íntegramente mediante Python/pypdf; documento **DEMO-PF-002, R1, fecha 2026-11-17**, vigente hasta 2026-12-01 inclusive. Relaciona expresamente DEMO-002 y L1. Contiene especificaciones, condiciones y constancia ficticia de aceptación.
- No se recibieron otros documentos del expediente. No hay adjuntos referenciados ausentes ni archivos recibidos ilegibles.
- Instrucciones leídas íntegramente: `SKILL.md` y `PERFIL-EXPEDIENTE.md`.
- Texto original extraído conservado en `texto-extraido.txt`. La extracción es una lectura documental, sin comprobación externa ni verificación de autenticidad. Toda la evidencia del expediente citada a continuación corresponde a la página 1.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA**.

Los controles obligatorios aplicables están documentados y no se identificaron contradicciones pendientes. El transporte se declara estimado, sin llegada firme, y se excluyen expresamente costos que no constituyen cero de costo final. Este estado no aprueba ni autoriza una operación.

## 4. Datos normalizados

Todos los datos siguientes tienen estado **aportado** y proceden de la página 1 de DEMO-PF-002 R1. No se han comprobado externamente.

| Campo | Valor original y lectura normalizada |
|---|---|
| Expediente y etapa | «Expediente: DEMO-002. Etapa solicitada: importación.» |
| Cliente y contacto | «Residencia Beta Demo»; `beta@cliente.example`. |
| Proyecto y uso | «mobiliario residencial, sillas de comedor». |
| Destino | «Casa Demo B, Ciudad de Panamá, Panamá». |
| Proveedor y contacto | «Demo Furniture Export»; `ventas@exportador.example`. |
| Línea y producto | «L1: silla modelo S-20; 20 unidades; ruta importación.» Identificador L1 único dentro del documento; cantidad positiva 20, unidad de conteo unidades. |
| Dimensiones | «Dimensiones L x A x H: 500 x 550 x 850 mm.» Largo 500 mm, ancho 550 mm, alto 850 mm; no se realizó conversión. |
| Material | «estructura de acero y asiento de polipropileno». |
| Acabado | «negro mate». |
| Moneda, precio y subtotal | «Precio unitario: USD 80.00. Subtotal: USD 1600.00.» |
| Costos incluidos | «Embalaje: incluido.» No se declara importe separado para el embalaje. |
| Costos excluidos | «Transporte internacional: excluido. Transporte local: excluido. Tributos de importación: excluidos.» Importes de esos costos: **NO APORTADO**; no se tratan como cero. |
| Impuestos y otros cargos de la proforma | «Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00.» |
| Total y alcance | «Total proforma: USD 1600.00. El total es de mercancía, no costo final puesto en destino.» Costo final puesto en destino: **NO APORTADO**; no se presenta el total de mercancía como ese costo. |
| Pago | «30 % al confirmar pedido y 70 % antes del despacho.» |
| Países | «País de despacho: China. País de entrega: Panamá.» País de origen de fabricación: **NO APORTADO**, no inferido del despacho. |
| Preparación | «30 días calendario desde recepción del anticipo.» |
| Transporte y llegada | «estimado 35 días calendario desde despacho; no hay fecha firme de llegada.» No se sumaron estimaciones ni se prometió una fecha de llegada. |
| Instalación | «No incluye instalación.» |
| Incoterm | «Las partes no han usado Incoterm en esta proforma.» |
| Documento y vigencia | «PROFORMA DEMO-PF-002 \| R1 \| Fecha: 2026-11-17»; «Vigencia: hasta 2026-12-01 inclusive.» |
| Revisión aprobada | «Especificación y condiciones aprobadas: DEMO-PF-002 R1.» |
| Aceptación | «Constancia ficticia de aceptación del cliente: Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-002 R1.» Es una constancia contenida en la fuente, sin acreditación externa de identidad, autoridad o firma. |

Comprobación aritmética decimal a centavos de los importes declarados:

- 20 × USD 80.00 = **USD 1600.00**, coincidente con el subtotal.
- USD 1600.00 + USD 0.00 (impuestos de la proforma) + USD 0.00 (otros cargos) = **USD 1600.00**, coincidente con el total de mercancía declarado.

La suma no incluye importes excluidos no aportados. No hubo conversión monetaria ni cálculo de tributos.

## 5. Checklist

La evidencia de expediente indicada en la tabla procede de DEMO-PF-002 R1, página 1.

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de pedido | satisfecho | DEMO-002 y etapa importación explícitos; identificador ficticio, no atribuido a ERP real. |
| P02 | Sí | satisfecho | Residencia Beta Demo y beta@cliente.example. |
| P03 | Sí | satisfecho | Proyecto residencial de sillas de comedor; Casa Demo B, Ciudad de Panamá, Panamá. Destino identificado para la demostración. |
| P04 | Sí | satisfecho | L1, silla S-20, 20 unidades; identificador único y cantidad positiva. |
| P05 | Sí | satisfecho | L x A x H, 500 x 550 x 850 mm; estructura de acero y asiento de polipropileno; negro mate. |
| P06 | Sí | satisfecho | L1 declara ruta importación. |
| P07 | Sí | satisfecho | USD, precio 80.00, subtotal 1600.00, impuestos y otros cargos de proforma 0.00, total mercancía 1600.00, pago 30/70 con hitos. Exclusiones explícitas; el total declarado no depende de valorar costos excluidos. No hay costo final puesto en destino declarado. |
| P08 | Sí | satisfecho | Preparación 30 días desde recepción del anticipo; transporte estimado 35 días desde despacho; no hay llegada firme; instalación excluida. Los hitos están expresos y la incertidumbre se conserva. |
| P09 | Sí | satisfecho | Proforma DEMO-PF-002 R1 de 2026-11-17, vinculada a DEMO-002/L1; R1 identificada como aprobada y aceptada expresamente en la constancia ficticia. |
| P10 | Sí | satisfecho | Luis Demo, contacto y fecha 2026-11-17; aceptación expresa de líneas y condiciones de DEMO-PF-002 R1. Se registra evidencia documental, sin verificar autoridad real. |
| F01 | No | NA | L1 declara exclusivamente importación; no hay línea de fabricación en el alcance. |
| F02 | No | NA | Misma condición: no se revisa fabricación. |
| F03 | No | NA | Misma condición: no se revisa fabricación. |
| F04 | No | NA | No hay ruta de fabricación ni declaración de fabricación ajustada a espacio existente. |
| F05 | No | NA | No hay fabricación en el alcance; preparación y transporte se evalúan bajo importación. |
| I01 | Sí, importación L1 | satisfecho | Demo Furniture Export; proforma disponible con número, fecha, R1 y vigencia explícita hasta 2026-12-01 inclusive. |
| I02 | Sí | satisfecho | L1/S-20, 20 unidades, dimensiones con ejes y mm, material y acabado en la proforma; no existe otra fuente recibida con valores incompatibles. |
| I03 | Sí | satisfecho | Despacho China; entrega Panamá y destino Casa Demo B. No se equipara despacho con origen de fabricación. |
| I04 | Sí | satisfecho | USD, pago, precios y total; embalaje incluido; transporte internacional/local y tributos excluidos; impuestos y otros cargos de esta proforma declarados. Alcance del total claramente limitado a mercancía. |
| I05 | Sí | satisfecho | Preparación 30 días calendario desde recepción del anticipo; transporte estimado 35 días calendario desde despacho. No se exige una llegada firme como sustituto obligatorio de plazos e hitos ya declarados. |
| I06 | No, condición desactivada | NA | La fuente declara expresamente que las partes no han usado Incoterm. Alcance de costos evaluado por I04; no se inventa término, lugar o edición. |

## 6. Hallazgos

No se identifican faltantes obligatorios ni contradicciones aplicables pendientes. Se registran dos observaciones de alcance que deben conservarse en la revisión humana; no son incumplimientos del perfil:

| ID | Requisito | Valores/documentos | Consecuencia documental | Acción requerida |
|---|---|---|---|---|
| OBS-01 | P07, I04 | Página 1: USD 1600.00 corresponde a mercancía; transporte internacional/local y tributos excluidos, sin importes. | El expediente no permite afirmar un costo final puesto en destino ni tratar exclusiones como costo cero. | Mantener explícita esta delimitación al evaluar comercialmente el expediente. Si se pretende decidir sobre costo final, obtener esos importes en un alcance posterior. |
| OBS-02 | P08, I05 | Página 1: 30 días desde anticipo; transporte estimado 35 días desde despacho; sin llegada firme. | No existe fecha de llegada comprometida documentada. | Conservar los hitos y el carácter estimado; no convertir la suma de plazos en compromiso de llegada. |

## 7. Preguntas y siguiente acción humana

No hay preguntas bloqueantes para completar esta revisión bajo PEO-01 v1.0. La siguiente acción corresponde a una persona: revisar el expediente y sus condiciones, teniendo presentes el alcance de costos, la vigencia y el carácter estimado del transporte. Este informe no acepta el pedido ni aprueba compra, importación o instalación.

No se requieren como emitidos documentos de una operación aún no iniciada, tales como declaración aduanera, conocimiento de embarque, packing list definitivo o comprobante de recepción.

## 8. Límites

Revisión exclusivamente documental de un expediente ficticio, basada en los tres archivos autorizados. No se usaron red, servicios externos, correo ni comprobaciones externas. Se leyó la única página real del PDF mediante extracción de su texto con pypdf; no se realizó inspección visual, OCR ni verificación de autenticidad. No se infirieron propiedades desde imágenes ni se hicieron cálculos técnicos.

Las afirmaciones de proveedor y cliente se registran como datos aportados. No se verificaron identidad, autoridad de firmante, calidad de material, factibilidad, obligaciones aduaneras o cumplimiento técnico/legal. PEO-01 v1.0 es un perfil documental de demostración; este resultado no constituye certificación ni afirmación de conformidad ISO. No se consultaron ni verificaron externamente las referencias normativas mencionadas en el perfil.
