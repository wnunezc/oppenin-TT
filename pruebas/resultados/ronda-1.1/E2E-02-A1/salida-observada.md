# Informe documental

## 1. Identificación

Expediente **DEMO-002**. Revisión de análisis: 1, independiente. Etapa solicitada: **importación**, antes del pedido al proveedor. Ruta L1: importación. Perfil aplicado: **PEO-01 v1.1**, skill revisor-expedientes-mobiliario v1.1. La fuente declara «FICTICIO — SOLO PRUEBA TÉCNICA»; no se atribuye el identificador a un ERP real. La fecha documental se conserva separada de la hora real registrada en inicio.txt.

## 2. Fuentes

- SKILL.md y PERFIL-EXPEDIENTE.md leídos íntegramente como reglas autorizadas.
- E2E-02-proforma.pdf: una página, abierta directamente mediante pypdf, extraída y leída íntegramente. Proforma **DEMO-PF-002, R1, 2026-11-17**; vigencia hasta **2026-12-01 inclusive**. Extracción propia: extraccion-pypdf.txt. El texto se obtuvo completo y legible; no fue necesario renderizado ni OCR. La primera visualización de consola mostró caracteres de acento sustituidos; una nueva lectura de la extracción con salida UTF-8 resolvió la visualización sin cambiar el texto de la fuente.
- No se recibieron correos ni revisiones anteriores. No se mencionan adjuntos pendientes de entrega. No hay archivos recibidos ilegibles.

Toda procedencia indicada como «p. 1» corresponde a E2E-02-proforma.pdf. Las huellas de los tres archivos originales se conservan en fuentes-sha256.json y registro.json. No se consultaron fuentes externas.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA**.

Los controles obligatorios de pedido e importación están satisfechos documentalmente, sin contradicciones verificadas. La constancia atribuida a Luis Demo con fecha y referencia exacta a R1 acredita documentalmente aprobación y aceptación para P09/P10; la frase genérica de aprobación no se utiliza por sí sola como evidencia. Este estado no autoriza la operación.

## 4. Datos normalizados

Todos los siguientes datos tienen estado **aportado** y proceden de p. 1, en los campos transcritos. No se dedujeron datos de apariencia ni se comprobaron externamente.

| Campo | Valor original y valor de revisión | Procedencia |
|---|---|---|
| Expediente y etapa | «Expediente: DEMO-002. Etapa solicitada: importación.» | p. 1, Expediente |
| Cliente y contacto | «Residencia Beta Demo»; «beta@cliente.example» | p. 1, Cliente/Contacto |
| Proyecto y uso | «mobiliario residencial, sillas de comedor» | p. 1, Proyecto |
| Destino | «Casa Demo B, Ciudad de Panamá, Panamá» | p. 1, Destino |
| Proveedor | «Demo Furniture Export»; «ventas@exportador.example» | p. 1, Proveedor/Contacto |
| Línea, modelo, cantidad y ruta | «L1: silla modelo S-20; 20 unidades; ruta importación.» | p. 1, L1 |
| Dimensiones | «Dimensiones L x A x H: 500 x 550 x 850 mm.»; largo 500 mm, ancho 550 mm, alto 850 mm | p. 1, Dimensiones |
| Material | «estructura de acero y asiento de polipropileno» | p. 1, Material |
| Acabado | «negro mate» | p. 1, Acabado |
| Moneda y precio unitario | «USD 80.00» | p. 1, Precio unitario |
| Subtotal | «USD 1600.00» | p. 1, Subtotal |
| Alcance de costos | «Embalaje: incluido. Transporte internacional: excluido.»; «Transporte local: excluido. Tributos de importación: excluidos.» | p. 1, Embalaje/Transportes/Tributos |
| Impuestos y otros cargos de proforma | «Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00.» | p. 1, Impuestos/Otros cargos |
| Total | «Total proforma: USD 1600.00. El total es de mercancía, no costo final puesto en destino.» | p. 1, Total proforma |
| Pago | «30 % al confirmar pedido y 70 % antes del despacho» | p. 1, Pago |
| Países | «País de despacho: China. País de entrega: Panamá.»; origen de fabricación: **NO APORTADO**, no exigido por I03 | p. 1, Países |
| Preparación | «30 días calendario desde recepción del anticipo» | p. 1, Preparación |
| Transporte | «estimado 35 días calendario desde despacho; no hay fecha firme de llegada» | p. 1, Transporte |
| Instalación | «No incluye instalación.» | p. 1, alcance de entrega |
| Incoterm | «Las partes no han usado Incoterm en esta proforma.» | p. 1, declaración sobre Incoterm |
| Documento controlado | «PROFORMA DEMO-PF-002»; «R1»; «Fecha: 2026-11-17»; «Vigencia: hasta 2026-12-01 inclusive.» | p. 1, encabezado/Vigencia |
| Aprobación y aceptación | «Especificación y condiciones aprobadas: DEMO-PF-002 R1.» y «Constancia ficticia de aceptación del cliente: Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-002 R1.» | p. 1, constancia inferior |

Comprobación decimal de importes declarados: **20 × USD 80.00 = USD 1600.00**; **USD 1600.00 + USD 0.00 de impuestos de proforma + USD 0.00 de otros cargos = USD 1600.00**, coincidente a centavos con el total. No se asigna valor cero a transportes o tributos excluidos. El costo final puesto en destino no está cuantificado y no se ha solicitado como alcance adicional. No se suman estimaciones de preparación y transporte para prometer llegada.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de pedido | satisfecho | p. 1, Expediente: DEMO-002 y etapa importación explícitos. |
| P02 | Sí | satisfecho | p. 1, Cliente/Contacto: Residencia Beta Demo y beta@cliente.example. |
| P03 | Sí | satisfecho | p. 1, Proyecto/Destino: mobiliario residencial, sillas de comedor, Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí | satisfecho | p. 1, L1: identificador único, silla S-20, 20 unidades; cantidad positiva y unidad de conteo. |
| P05 | Sí | satisfecho | p. 1, Dimensiones/Material/Acabado: L x A x H 500 x 550 x 850 mm, acero y polipropileno, negro mate. |
| P06 | Sí | satisfecho | p. 1, L1: ruta importación expresa. |
| P07 | Sí | satisfecho | p. 1, precios/cargos/total/pago: USD 80.00, subtotal y total USD 1600.00, impuestos y cargos USD 0.00, exclusiones expresas y pago 30 %/70 %. Operación decimal coincidente. |
| P08 | Sí | satisfecho | p. 1, Preparación/Transporte/Instalación: 30 días calendario desde anticipo, transporte estimado 35 días desde despacho; instalación excluida. No se exige fecha firme adicional. |
| P09 | Sí | satisfecho | p. 1, encabezado y expediente: DEMO-PF-002 R1 de 2026-11-17 vinculado a DEMO-002/L1. Constancia atribuida a Luis Demo, beta@cliente.example, 2026-11-17, acepta líneas y condiciones de DEMO-PF-002 R1. No depende de la frase genérica «aprobadas». No hay correos recibidos que identificar. |
| P10 | Sí | satisfecho | p. 1, constancia: aceptación expresa por Luis Demo, contacto y fecha 2026-11-17, alcance de líneas y condiciones de DEMO-PF-002 R1. |
| F01 | No | NA | p. 1, etapa y ruta L1 exclusivamente importación; no hay línea de fabricación declarada. |
| F02 | No | NA | p. 1, etapa y ruta L1 importación; no se activa ficha/plano de fabricación. |
| F03 | No | NA | p. 1, etapa y ruta L1 importación; no se activa aprobación técnica de fabricación. |
| F04 | No | NA | p. 1, etapa/ruta importación de sillas; no se declara fabricación ajustada a espacio existente. |
| F05 | No | NA | p. 1, etapa y ruta L1 importación; no se activa plazo de fabricación. |
| I01 | Sí, importación | satisfecho | p. 1, Proveedor/Encabezado/Vigencia: Demo Furniture Export; proforma DEMO-PF-002 R1, 2026-11-17, vigente hasta 2026-12-01 inclusive. |
| I02 | Sí | satisfecho | p. 1, L1 y especificaciones dentro de la propia proforma: S-20, 20 unidades, L x A x H 500 x 550 x 850 mm, acero/polipropileno y negro mate; sin fuentes incompatibles aportadas. |
| I03 | Sí | satisfecho | p. 1, Países/Destino: despacho China, entrega Panamá, Casa Demo B en Ciudad de Panamá. No se confunde despacho con origen de fabricación. |
| I04 | Sí | satisfecho | p. 1, comerciales: USD, pago 30 %/70 %, precios y total; embalaje incluido, ambos transportes y tributos de importación excluidos expresamente. |
| I05 | Sí | satisfecho | p. 1, plazos: preparación 30 días calendario desde recepción del anticipo; transporte estimado 35 días calendario desde despacho. La fuente declara ausencia de fecha firme de llegada. |
| I06 | No, condición no activada | NA | p. 1: «Las partes no han usado Incoterm en esta proforma.» El alcance de costos se evalúa en I04. |

## 6. Hallazgos

No se identifican faltantes obligatorios, contradicciones ni campos esenciales no legibles en el material recibido. No hay hallazgos bloqueantes que requieran corrección documental según PEO-01 v1.1.

Observaciones de alcance, sin agregar requisitos: los USD 1600.00 corresponden a mercancía, con transportes y tributos de importación excluidos y sin costo final puesto en destino cuantificado (P07/I04). Los 35 días de transporte son estimados y no constituyen llegada firme (P08/I05). Se conserva el carácter ficticio y documental de la aceptación (P09/P10).

## 7. Preguntas y siguiente acción humana

No se requieren preguntas para cerrar controles del perfil en este expediente. Siguiente acción: revisión humana de la proforma DEMO-PF-002 R1 y de su alcance comercial declarado antes de decidir sobre el pedido. Este informe no aprueba compra, importación ni instalación.

## 8. Límites

Revisión exclusivamente documental de las fuentes enumeradas, mediante extracción textual propia de la única página del PDF. No se verificaron autenticidad, autoridad del aceptante, identidad real, calidad, factibilidad técnica, origen de fabricación ni cumplimiento legal/aduanero. No hubo comprobación externa, acceso a red ni lectura de otras sesiones. Los controles pertenecen a PEO-01 v1.1; no se afirma conformidad ni certificación ISO. No se exige documentación de embarque de una operación todavía no iniciada. No se aportó informe anterior, por lo que no corresponde apartado de cambios.