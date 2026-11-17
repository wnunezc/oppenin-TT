# Revisión documental

## 1. Identificación

Expediente **DEMO-003**. Revisión de análisis **1**, independiente, sin revisión anterior aportada. Etapa: **importación**, antes del pedido al proveedor. Única línea L1, ruta importación. Perfil aplicado: **PEO-01 v1.1**; skill 1.1. La fuente declara «FICTICIO — SOLO PRUEBA TÉCNICA». Las fechas documentales se conservan como declaradas y se distinguen del horario real de ejecución registrado en registro.json.

## 2. Fuentes

- Recibido: `D:\OpsZone\DevWorkspace\Projects\Tech-Test\Oppenin\pruebas\entradas\E2E-03-proforma.pdf`, una página, proforma **DEMO-PF-003, R1, 2026-11-17**, vinculada a DEMO-003 y L1. Vigencia declarada: «hasta 2026-12-01 inclusive».
- Reglas leídas íntegramente: SKILL.md y PERFIL-EXPEDIENTE.md de la raíz autorizada.
- Método: apertura directa del PDF con pypdf.PdfReader y extract_text() sobre su única página; extracción propia conservada en extraccion-pypdf.json. Renderizado local con pdftoppm y lectura visual directa de pagina-1.png, comprobando toda la página. Los acentos de la extracción se conservaron correctamente en UTF-8; su apariencia inicial en consola correspondía a la visualización de caracteres, comprobada mediante representación escapada y visión.
- No se recibieron correos ni otros adjuntos del caso. No se menciona un adjunto ausente. No hay archivos ilegibles. No se aportó constancia atribuida de aprobación ni aceptación del cliente; son faltantes documentales, no archivos recibidos ilegibles.

## 3. Estado global

**PENDIENTE DE INFORMACIÓN**. El expediente es evaluable y no se comprobaron contradicciones, pero faltan datos obligatorios aplicables: unidad dimensional, acabado, condiciones de pago, evidencia atribuida de aprobación de R1 y aceptación del cliente. La frase genérica de aprobación no acredita esos controles.

## 4. Datos normalizados

Toda la información del caso procede de la página 1 de la proforma. «Aportado» indica declaración documental, sin comprobación externa.

| Campo / ubicación en página 1 | Original y valor conservado | Estado |
|---|---|---|
| Encabezado | PROFORMA DEMO-PF-003; R1; Fecha: 2026-11-17; vigencia hasta 2026-12-01 inclusive | aportado |
| Expediente / etapa | DEMO-003; importación | aportado |
| Cliente / contacto | Residencia Beta Demo; beta@cliente.example | aportado |
| Proyecto / uso | «mobiliario residencial, sillas de comedor» | aportado |
| Destino | «Casa Demo B, Ciudad de Panamá, Panamá» | aportado |
| Proveedor / contacto | Demo Furniture Export; ventas@exportador.example | aportado |
| Línea / producto / cantidad / unidad / ruta | «L1: silla modelo S-20; 20 unidades; ruta importación» | aportado |
| Dimensiones L1 | «Dimensiones L x A x H: 500 x 550 x 850». Ejes declarados L, A, H; largo 500, ancho 550, alto 850. Unidad: **NO APORTADO**. No se convierten ni se asume unidad | faltante |
| Material L1 | «estructura de acero y asiento de polipropileno» | aportado |
| Acabado L1 | «por confirmar»; acabado definido: **NO APORTADO** | faltante |
| Precio / subtotal | «Precio unitario: USD 80.00. Subtotal: USD 1600.00» | aportado |
| Alcance de costos | «Embalaje: incluido. Transporte internacional: excluido. Transporte local: excluido. Tributos de importación: excluidos» | aportado |
| Impuestos / otros cargos / total | «Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00. Total proforma: USD 1600.00. El total es de mercancía, no costo final puesto en destino» | aportado |
| Pago | Condición completa de pago: **NO APORTADO**. Solo se menciona «recepción del anticipo» como hito de preparación; no define importe o proporción ni condiciones de saldo | faltante |
| Despacho / entrega | «País de despacho: China. País de entrega: Panamá»; no se infiere origen de fabricación | aportado |
| Preparación | «30 días calendario desde recepción del anticipo» | aportado |
| Transporte / llegada | «estimado 35 días calendario desde despacho; no hay fecha firme de llegada» | aportado |
| Instalación | «No incluye instalación» | aportado |
| Incoterm | «Las partes no han usado Incoterm en esta proforma» | aportado |
| Aprobación de versión | «Especificación y condiciones aprobadas: DEMO-PF-003 R1». Identidad y fecha de aprobación: **NO APORTADO** | faltante |
| Aceptación del cliente | «Aceptación del cliente: pendiente»; evidencia explícita con alcance/revisión, identidad y fecha: **NO APORTADO** | faltante |

Comprobación decimal a centavos, conservada en calculos.json: **20 × USD 80.00 = USD 1600.00**; **USD 1600.00 + USD 0.00 de impuestos + USD 0.00 de otros cargos = USD 1600.00**. Coinciden con subtotal y total declarados. El embalaje se declara incluido. No se asigna cero a transporte o tributos excluidos: el costo final puesto en destino no está cuantificado y no se exige aquí cuantificarlo. No se suman plazos para prometer una llegada.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de pedido | satisfecho | P. 1, expediente DEMO-003 y etapa importación declarados; identificador ficticio, sin atribución a ERP |
| P02 | Sí | satisfecho | P. 1, cliente Residencia Beta Demo y beta@cliente.example |
| P03 | Sí | satisfecho | P. 1, mobiliario residencial, sillas de comedor; Casa Demo B, Ciudad de Panamá, Panamá |
| P04 | Sí | satisfecho | P. 1, L1 única, silla modelo S-20, 20 unidades |
| P05 | Sí | faltante | P. 1, L x A x H 500 x 550 x 850 sin unidad; material declarado, acabado «por confirmar» |
| P06 | Sí | satisfecho | P. 1, ruta de L1 expresamente importación |
| P07 | Sí | faltante | P. 1, moneda/importes/alcance de cargos completos y aritmética coincidente; falta condición de pago, la mención de anticipo como hito no la define |
| P08 | Sí | satisfecho | P. 1, preparación 30 días desde anticipo, transporte estimado 35 días desde despacho; instalación excluida. No se exige fecha firme adicional |
| P09 | Sí | faltante | P. 1, proforma identificada, fechada, R1 y relacionada con DEMO-003/L1; frase «Especificación y condiciones aprobadas: DEMO-PF-003 R1» sin identidad ni fecha de aprobación |
| P10 | Sí | faltante | P. 1, «Aceptación del cliente: pendiente»; no hay evidencia atribuida del alcance y revisión aceptados |
| F01 | No | NA | L1 se declara exclusivamente de importación; no hay ruta de fabricación |
| F02 | No | NA | L1 se declara exclusivamente de importación; no aplica ficha/plano de fabricación |
| F03 | No | NA | L1 se declara exclusivamente de importación; no aplica aprobación técnica de fabricación |
| F04 | No | NA | Sin ruta de fabricación ni condición declarada de ajuste a espacio existente |
| F05 | No | NA | L1 exclusivamente de importación; sus plazos se evalúan en P08/I05 |
| I01 | Sí, importación L1 | satisfecho | P. 1, Demo Furniture Export; proforma DEMO-PF-003, fecha 2026-11-17, R1, vigencia hasta 2026-12-01 inclusive |
| I02 | Sí | faltante | P. 1, código/modelo S-20, 20 unidades y material identificados; falta unidad dimensional y acabado definitivo para completar especificación de L1 |
| I03 | Sí | satisfecho | P. 1, despacho China; entrega Panamá, Casa Demo B. No se confunde despacho con origen |
| I04 | Sí | faltante | P. 1, USD, importes y alcance de costos declarados; condición de pago no definida. Exclusiones expresas satisfacen declaración del alcance de costos |
| I05 | Sí | satisfecho | P. 1, preparación 30 días calendario desde recepción del anticipo; transporte estimado 35 días calendario desde despacho. Hitos explícitos y naturaleza estimada conservados |
| I06 | No, condición no activada | NA | P. 1, «Las partes no han usado Incoterm en esta proforma»; alcance de costos evaluado en I04 |

## 6. Hallazgos

| Hallazgo | Requisitos | Valores / documento involucrado | Consecuencia documental y acción requerida |
|---|---|---|---|
| H01 | P05, I02 | DEMO-PF-003 R1, p. 1, «Dimensiones L x A x H: 500 x 550 x 850» | Especificación incompleta por unidad ausente. Aportar unidad explícita de los tres valores, conservando ejes y referencia a L1 |
| H02 | P05, I02 | Misma fuente, p. 1, «Acabado: por confirmar» | Acabado no definido. Aportar acabado identificado para L1 en documentación aplicable |
| H03 | P07, I04 | Misma fuente, p. 1, hito «recepción del anticipo» sin condición comercial de pago | No se puede registrar la condición de pago completa. Aportar importe/proporción y condición del anticipo, así como condiciones del saldo aplicables |
| H04 | P09 | Misma fuente, p. 1, frase genérica «Especificación y condiciones aprobadas: DEMO-PF-003 R1» | La frase no acredita aprobación atribuida. Aportar evidencia explícita vinculada a documento/revisión, identidad y fecha; no basta la fecha de emisión |
| H05 | P10 | Misma fuente, p. 1, «Aceptación del cliente: pendiente» | Falta aceptación documental del cliente. Aportar evidencia explícita del alcance y revisión aceptados con identidad y fecha |

No se encontró contradicción documental comprobable. Los valores pendientes no se completan por contexto. Ninguna persona real ni responsable empresarial se asigna por inferencia.

## 7. Preguntas y siguiente acción humana

1. H01: ¿Cuál es la unidad explícita de 500 × 550 × 850 para los ejes L × A × H de L1?
2. H02: ¿Qué acabado definitivo corresponde a L1?
3. H03: ¿Cuáles son las condiciones de pago, incluido el anticipo mencionado y el saldo aplicable?
4. H04: ¿Qué constancia identifica quién aprobó DEMO-PF-003 R1 y en qué fecha? Si se emite otra revisión al completar datos, aportar su aprobación explícita vinculada.
5. H05: ¿Qué evidencia documenta la aceptación del cliente del alcance y revisión aplicables, con identidad y fecha?

La siguiente acción humana es completar estos faltantes y aportar la documentación aplicable para una nueva revisión, preservando esta revisión y cualquier versión anterior. Si una constancia de aceptación también acredita la aprobación de versión, puede atender H04 y H05 si satisface ambos controles. No se aprueba compra, importación, fabricación ni instalación. No se solicita cuantificación de costos expresamente excluidos ni fecha firme de llegada adicional.

## 8. Límites

Revisión exclusivamente documental sobre el PDF efectivamente recibido. No se verificaron externamente identidad, autoridad, autenticidad, datos comerciales, dimensiones, materiales, capacidad técnica, plazos, cumplimiento aduanero o legal. La aritmética de importes no valida precios ni costos finales. PEO-01 es un perfil de demostración; no se afirma certificación ni conformidad ISO. No se consultó red ni se contrastaron las referencias externas citadas por el perfil, pues no forman parte de las fuentes autorizadas de esta ejecución. Este informe no emite veredicto de prueba.