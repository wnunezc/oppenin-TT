# Informe documental — DEMO-003

## 1. Identificación

Revisión de análisis: 1, independiente, sin revisión anterior aportada. Expediente ficticio DEMO-003, «FICTICIO — SOLO PRUEBA TÉCNICA». Etapa: importación, antes del pedido al proveedor. Ruta L1: importación. Perfil aplicado: PEO-01 v1.1; skill 1.1. Las fechas documentales se conservan como declaradas, separadas del sello real de análisis de inicio.txt.

## 2. Fuentes

- Reglas leídas íntegramente: SKILL.md y PERFIL-EXPEDIENTE.md, ambos en la raíz autorizada.
- Documento recibido: pruebas/entradas/E2E-03-proforma.pdf, una página, PROFORMA DEMO-PF-003, R1, fecha 2026-11-17, vinculada al expediente DEMO-003 y L1. Vigencia: «hasta 2026-12-01 inclusive».
- Sin correos ni fichas adicionales recibidos. No se identifican adjuntos referenciados ausentes. No hay archivos esenciales ilegibles.
- Método propio: pypdf.PdfReader y extract_text() en la totalidad de páginas (1). La extracción presenta caracteres de sustitución en acentos. Por ello se renderizó la totalidad con pdftoppm a 150 dpi y se leyó visualmente pagina-1.png. El contenido principal es legible; los datos siguientes proceden de esa lectura visual cotejada con la extracción. Las advertencias de fuentes de Poppler se conservan en el registro y no impidieron la lectura. Sin OCR ni comprobaciones externas.

## 3. Estado global

**PENDIENTE DE INFORMACIÓN**. El documento permite evaluar etapa y ruta sin contradicciones comprobadas, pero faltan unidad dimensional, acabado definido, condición de pago y evidencias atribuidas de aprobación y aceptación.

## 4. Datos normalizados

Todos los valores de esta sección proceden de E2E-03-proforma.pdf, página 1, campos expresamente indicados. «Aportado» significa declarado por la fuente, sin verificación externa.

| Campo | Valor original y procedencia | Estado del dato |
|---|---|---|
| Expediente / etapa | «Expediente: DEMO-003. Etapa solicitada: importación.» | aportado |
| Cliente / contacto | «Residencia Beta Demo»; «beta@cliente.example», campo Cliente | aportado |
| Proyecto / uso | «mobiliario residencial, sillas de comedor», campo Proyecto | aportado |
| Destino | «Casa Demo B, Ciudad de Panamá, Panamá», campo Destino | aportado |
| Proveedor / contacto | «Demo Furniture Export»; «ventas@exportador.example», campo Proveedor | aportado |
| Línea / producto | «L1: silla modelo S-20; 20 unidades; ruta importación.» | aportado |
| Dimensiones | «Dimensiones L x A x H: 500 x 550 x 850.»; ejes L/A/H declarados; unidad: NO APORTADO. No se normalizan a mm, cm ni m. | faltante |
| Material | «estructura de acero y asiento de polipropileno», campo Material | aportado |
| Acabado | «por confirmar», campo Acabado; definición: NO APORTADO | faltante |
| Moneda / unitario / subtotal | «Precio unitario: USD 80.00. Subtotal: USD 1600.00.» | aportado |
| Cargos / total | «Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00.»; «Total proforma: USD 1600.00. El total es de mercancía, no costo final puesto en destino.» | aportado |
| Alcance de costos | «Embalaje: incluido. Transporte internacional: excluido.»; «Transporte local: excluido. Tributos de importación: excluidos.» | aportado |
| Pago | Condición de pago: NO APORTADO. El campo Preparación menciona «recepción del anticipo», sin definir el anticipo ni las condiciones completas de pago. | faltante |
| Despacho / entrega | «País de despacho: China. País de entrega: Panamá.»; no se atribuye origen de fabricación | aportado |
| Preparación | «30 días calendario desde recepción del anticipo» | aportado |
| Transporte / instalación | «estimado 35 días calendario desde despacho; no hay fecha firme de llegada. No incluye instalación.» | aportado |
| Incoterm | «Las partes no han usado Incoterm en esta proforma.» | aportado |
| Aprobación de versión | «Especificación y condiciones aprobadas: DEMO-PF-003 R1.»; identidad y fecha de aprobación: NO APORTADO | faltante |
| Aceptación | «Aceptación del cliente: pendiente.»; evidencia con identidad, fecha y alcance/revisión: NO APORTADO | faltante |

Comprobación decimal a centavos: 20 × USD 80.00 = USD 1600.00; USD 1600.00 + USD 0.00 (impuestos de esta proforma) + USD 0.00 (otros cargos) = USD 1600.00. Coincide con subtotal y total declarados. Los costos excluidos no se interpretan como cero. El costo final puesto en destino no está cuantificado; no se exige calcularlo para revisar el total de mercancía.

## 5. Checklist

La evidencia documental de cada fila corresponde a la página 1 del PDF recibido, salvo los motivos de no aplicabilidad.

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base | satisfecho | Campos Expediente y Etapa: DEMO-003, importación; identificador ficticio, sin atribución a ERP. |
| P02 | Sí, base | satisfecho | Cliente Residencia Beta Demo y beta@cliente.example. |
| P03 | Sí, base | satisfecho | Proyecto residencial de sillas; Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí, L1 | satisfecho | L1, silla S-20, 20 unidades, cantidad positiva. |
| P05 | Sí, L1 | faltante | L x A x H: 500 x 550 x 850 sin unidad; acero/polipropileno declarados; acabado «por confirmar». |
| P06 | Sí, L1 | satisfecho | La línea declara ruta importación. |
| P07 | Sí, base | faltante | USD, precios, subtotal, cargos y total declarados y coherentes; condición de pago ausente. La referencia al anticipo no la define. |
| P08 | Sí, base | satisfecho | Preparación desde recepción del anticipo y transporte desde despacho, con plazos explícitos; instalación excluida. No se transforma la estimación en fecha firme. |
| P09 | Sí, proforma | faltante | DEMO-PF-003, R1, fecha y vínculo a DEMO-003/L1 presentes. La frase genérica de aprobación carece de identidad y fecha atribuibles a esta versión. |
| P10 | Sí, base | faltante | «Aceptación del cliente: pendiente»; no hay evidencia de alcance/revisión aceptados, identidad y fecha. |
| F01 | No | NA | L1 declara exclusivamente importación; no hay línea de fabricación. |
| F02 | No | NA | Ruta documentada de L1: importación. |
| F03 | No | NA | Ruta documentada de L1: importación. |
| F04 | No | NA | No hay ruta de fabricación ni fabricación declarada ajustada a espacio existente. |
| F05 | No | NA | Ruta documentada de L1: importación. |
| I01 | Sí, L1 | satisfecho | Proveedor Demo Furniture Export; proforma disponible DEMO-PF-003, 2026-11-17, R1, vigente hasta 2026-12-01 inclusive. |
| I02 | Sí, L1 | faltante | Modelo S-20, 20 unidades, dimensiones y material en proforma; falta unidad dimensional y acabado definido. No se aportó otra línea para comparar versiones. |
| I03 | Sí, L1 | satisfecho | Despacho China y entrega Panamá explícitos; destino Casa Demo B. |
| I04 | Sí, L1 | faltante | Moneda, precios/total y costos incluidos/excluidos expresos; falta condición de pago. No faltan importes de los conceptos expresamente excluidos para declarar el alcance de costos. |
| I05 | Sí, L1 | satisfecho | Preparación 30 días calendario desde recepción del anticipo; transporte estimado 35 días calendario desde despacho. No se exige llegada firme ni se suman como compromiso. |
| I06 | No, condición no activada | NA | La proforma declara que las partes no han usado Incoterm. No se inventa término, lugar ni edición. |

## 6. Hallazgos

| ID | Requisito | Valores/documentos involucrados | Consecuencia documental | Acción requerida |
|---|---|---|---|---|
| H01 | P05, I02 | DEMO-PF-003 R1 p. 1, «L x A x H: 500 x 550 x 850» | No puede establecerse dimensión física ni normalizarse sin unidad. | Aportar unidad explícita para los tres ejes en la especificación controlada de L1. |
| H02 | P05, I02 | Misma fuente, Acabado «por confirmar» | La especificación de L1 está incompleta. | Definir y documentar acabado de L1 en la revisión aplicable. |
| H03 | P07, I04 | Misma fuente, Preparación menciona anticipo; no hay condición de pago | No pueden revisarse íntegramente las condiciones comerciales. | Aportar condición de pago, con definición del anticipo y pago restante cuando corresponda. |
| H04 | P09 | Misma fuente, «Especificación y condiciones aprobadas: DEMO-PF-003 R1.» | La frase no acredita aprobación atribuida de la versión; la fecha de emisión no demuestra fecha de aprobación. | Aportar constancia explícita vinculada a documento y revisión con identidad y fecha. |
| H05 | P10 | Misma fuente, «Aceptación del cliente: pendiente.» | No hay aceptación documental del alcance y revisión por el cliente. | Aportar aceptación explícita con alcance/revisión aceptados, identidad y fecha. |

## 7. Preguntas y siguiente acción humana

1. H01: ¿Qué unidad corresponde a 500 × 550 × 850, en los ejes L/A/H de L1?
2. H02: ¿Cuál es el acabado definido de L1 y en qué revisión quedará registrado?
3. H03: ¿Cuál es la condición de pago, incluido el anticipo mencionado y el saldo si corresponde?
4. H04: ¿Qué evidencia documenta quién aprobó la versión aplicable y en qué fecha, con referencia explícita a la proforma/revisión?
5. H05: ¿Qué evidencia aporta el cliente de aceptación del alcance y revisión aplicables, con identidad y fecha?

La siguiente acción humana es reunir las precisiones y evidencias vinculadas a los cinco hallazgos y someterlas a una nueva revisión documental, conservando este informe. Si se emite una revisión nueva, documentar expresamente su relación de sustitución y la aprobación/aceptación del alcance correspondiente. Esta revisión no aprueba la operación.

## 8. Límites

Revisión exclusivamente documental del material recibido y legible. No se comprobó externamente identidad, autoridad, autenticidad, calidad, factibilidad técnica ni cumplimiento legal/aduanero. No se conectaron sistemas ni se ejecutaron acciones externas. No se exigen documentos definitivos de embarque o aduana de una operación aún no iniciada. Los controles son del perfil de demostración PEO-01 v1.1; no constituyen certificación ni dictamen de cumplimiento ISO. No se consultaron fuentes web ni se validaron las referencias externas mencionadas en el perfil. No existe revisión anterior aportada para comparar cambios.
