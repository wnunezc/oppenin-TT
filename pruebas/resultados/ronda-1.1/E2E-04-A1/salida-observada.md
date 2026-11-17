# Informe documental — DEMO-004

## 1. Identificación

Revisión de análisis: 1, independiente. Etapa: importación, antes del pedido al proveedor. Ruta declarada para L1: importación. Perfil aplicado: PEO-01 v1.1; skill revisor-expedientes-mobiliario v1.1. Expediente expresamente ficticio, solo prueba técnica. Las fechas de los documentos se conservan como datos del expediente, separadas de la hora real del análisis.

## 2. Fuentes

- **C1:** `pruebas/entradas/E2E-04-correo.md`, leído íntegramente. Remitente: beta@cliente.example; fecha: 2026-11-18 10:00 UTC-05:00; asunto: «Datos para expediente DEMO-004»; firma: Luis Demo. Sin identificador o revisión propios declarados. Párrafo 1: solicita revisar importación de DEMO-004; párrafo 2: solicita 24 sillas, blanco mate; párrafo 3: «No confirmo todavía cuál proforma debe sustituirse ni el nuevo total».
- **D1:** `pruebas/entradas/E2E-04-proforma.pdf`, abierto directamente con pypdf, una página; se iteró y extrajo el texto de esa página. DEMO-PF-004 R1, fecha 2026-11-17, vigencia hasta 2026-12-01 inclusive. La extracción contiene sus campos y la constancia de aceptación. No se necesitó renderizado ni OCR. Evidencia propia: `extraccion-pdf.txt`; procedimiento: `extraer_pdf.py`.
- Se leyeron íntegramente `SKILL.md` y `PERFIL-EXPEDIENTE.md` como reglas autorizadas. No se consultaron fuentes externas.
- No se aportó informe de revisión anterior ni documento que formalice el alcance comercial modificado por C1. No hay adjuntos adicionales expresamente referenciados ni archivos recibidos ilegibles.

## 3. Estado global

**CONFLICTO DOCUMENTAL**. C1 solicita 24 sillas blanco mate, mientras D1 R1 documenta y contiene aceptación de 20 sillas negro mate. No existe sustitución explícita ni aceptación del alcance modificado. La fecha posterior del correo no resuelve la discrepancia.

## 4. Datos normalizados

Todos los valores siguientes son aportados documentalmente; no se verificaron externamente. D1 corresponde en todos los casos a página 1.

| Campo | Valor original y normalización | Procedencia y estado |
|---|---|---|
| Expediente y etapa | «DEMO-004»; «importación» | C1 párrafo 1 y D1 encabezado; aportado |
| Cliente y contacto | Residencia Beta Demo; beta@cliente.example | D1 Cliente; aportado. C1 remitente y firma Luis Demo |
| Proyecto, uso y destino | «mobiliario residencial, sillas de comedor»; «Casa Demo B, Ciudad de Panamá, Panamá» | D1 Proyecto/Destino; aportado |
| Línea y producto | L1; «silla modelo S-20»; unidad de conteo: unidades/sillas | D1 L1; C1 párrafo 2 se refiere a L1; aportado |
| Cantidad L1 | D1: «20 unidades»; C1: «24 sillas» | D1 L1 y C1 párrafo 2; contradictorio |
| Dimensiones L1 | «L x A x H: 500 x 550 x 850 mm»; largo 500 mm, ancho 550 mm, alto 850 mm | D1 Dimensiones; aportado; sin conversión ni deducción por escala |
| Material L1 | «estructura de acero y asiento de polipropileno» | D1 Material; aportado |
| Acabado L1 | D1: «negro mate»; C1: «blanco mate» | D1 Acabado y C1 párrafo 2; contradictorio |
| Ruta L1 | «importación» | D1 L1 y C1 etapa; aportado |
| Proveedor | Demo Furniture Export; ventas@exportador.example | D1 Proveedor; aportado |
| Moneda y precio unitario | USD 80.00 | D1 Precio unitario; aportado para R1; precio del alcance modificado: NO APORTADO expresamente |
| Subtotal y total R1 | USD 1600.00 y USD 1600.00; «total de mercancía, no costo final puesto en destino» | D1 Subtotal/Total; aportado para 20 unidades. Nuevo total para el alcance de C1: NO APORTADO |
| Cargos e impuestos | Embalaje incluido; transporte internacional y local excluidos; tributos de importación excluidos; impuestos de esta proforma USD 0.00; otros cargos USD 0.00 | D1 costos; aportado. El costo final puesto en destino no está cuantificado; las exclusiones no equivalen a cero |
| Pago | «30 % al confirmar pedido y 70 % antes del despacho» | D1 Pago; aportado para R1 |
| Entrega y servicio | Preparación: 30 días calendario desde recepción del anticipo; transporte estimado: 35 días calendario desde despacho; sin fecha firme de llegada; no incluye instalación | D1 Preparación/Transporte; aportado; no se suman estimaciones como compromiso de llegada |
| Países | Despacho: China; entrega: Panamá | D1 países; aportado. Origen de fabricación: NO APORTADO; no se exige ni se infiere |
| Incoterm | «Las partes no han usado Incoterm en esta proforma» | D1 Incoterm; aportado |
| Control documental | DEMO-PF-004, R1, 2026-11-17, vinculada a DEMO-004/L1, vigente hasta 2026-12-01 inclusive | D1 encabezado/vigencia; aportado. Versión que sustituye R1: NO APORTADO; C1 párrafo 3 no la confirma |
| Aprobación y aceptación | «Especificación y condiciones aprobadas: DEMO-PF-004 R1». Además: «Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-004 R1» | D1 bloque final; evidencia atribuida para R1, no solo frase genérica. Aceptación del alcance de C1: NO APORTADO |

Comprobación decimal de R1: 20 × USD 80.00 = USD 1600.00; USD 1600.00 + USD 0.00 de impuestos de la proforma + USD 0.00 de otros cargos = USD 1600.00. Coincide a centavos. No se calcula ni atribuye un nuevo total para 24 unidades sin condiciones comerciales confirmadas.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de importación | satisfecho | C1 párrafo 1 y D1 encabezado declaran DEMO-004 e importación; identificador ficticio, no atribuido a ERP |
| P02 | Sí | satisfecho | D1 Cliente: Residencia Beta Demo y beta@cliente.example |
| P03 | Sí | satisfecho | D1 Proyecto/Destino: mobiliario residencial y Casa Demo B, Ciudad de Panamá, Panamá |
| P04 | Sí | contradictorio | D1 L1: S-20, 20 unidades; C1 párrafo 2: L1, 24 sillas; ambas cantidades positivas y con unidad, discrepancia sin resolver |
| P05 | Sí | contradictorio | D1 Dimensiones/Material completos; acabado negro mate frente a blanco mate en C1 párrafo 2 |
| P06 | Sí | satisfecho | D1 L1 declara ruta importación; coincide con etapa de C1 |
| P07 | Sí | faltante | D1 comerciales completos y aritméticamente coherentes para R1; C1 párrafo 3 no confirma nuevo total ni condiciones comerciales del alcance modificado |
| P08 | Sí | satisfecho | D1 Preparación/Transporte: plazos con hitos explícitos, destino identificado y exclusión de instalación |
| P09 | Sí | contradictorio | C1 identificado por remitente/fecha/asunto; D1 con identificador/fecha/R1 y constancia atribuida de aprobación mediante aceptación. Falta determinar la versión aplicable que resuelva C1 frente a R1; C1 no confirma sustitución |
| P10 | Sí | faltante | D1 constancia de Luis Demo, 2026-11-17, acepta expresamente R1; no se aporta aceptación de una revisión que integre y resuelva los cambios de cantidad/acabado de C1 |
| F01 | No | NA | L1 declara solo importación; no hay ruta fabricación |
| F02 | No | NA | No se revisa fabricación para L1 |
| F03 | No | NA | No se revisa fabricación para L1 |
| F04 | No | NA | No hay ruta fabricación ni declaración de fabricación ajustada a espacio existente |
| F05 | No | NA | L1 tiene ruta importación; preparación/despacho se evalúan con I05 |
| I01 | Sí | satisfecho | D1: Demo Furniture Export, DEMO-PF-004, 2026-11-17, R1 y vigencia explícita hasta 2026-12-01 inclusive |
| I02 | Sí | contradictorio | C1 L1: 24 sillas blanco mate frente a D1 L1 S-20: 20 unidades negro mate; dimensiones y material aportados en D1 |
| I03 | Sí | satisfecho | D1 países y destino: despacho China, entrega Panamá/Casa Demo B; no se confunde despacho con fabricación |
| I04 | Sí | faltante | D1 declara moneda, pago, precios y alcance de costos; queda sin confirmar total/condiciones para el alcance modificado de C1. No se exigen importes de transportes/tributos expresamente excluidos |
| I05 | Sí | satisfecho | D1: preparación 30 días calendario desde anticipo; transporte estimado 35 días calendario desde despacho; no es necesaria llegada firme adicional |
| I06 | No, condición ausente | NA | D1 declara expresamente que no se ha usado Incoterm; alcance de costos revisado en I04 |

## 6. Hallazgos

| ID | Requisito | Valores y fuentes | Consecuencia documental | Acción requerida |
|---|---|---|---|---|
| H01 | P04, I02 | C1 párrafo 2: 24 sillas; D1 p. 1 L1: 20 unidades | Cantidad aplicable contradictoria | Confirmar cantidad final de L1 e incorporarla a la proforma/revisión aplicable |
| H02 | P05, I02 | C1 párrafo 2: blanco mate; D1 p. 1 Acabado: negro mate | Acabado aplicable contradictorio | Confirmar acabado final de L1 y documentarlo en la versión aplicable |
| H03 | P07, I04 | D1 p. 1 comerciales: USD 80.00/unidad, USD 1600.00 para 20 unidades; C1 párrafo 3: nuevo total no confirmado | Condiciones comerciales del alcance modificado incompletas; no se puede usar el total de R1 como total confirmado para 24 sillas | Aportar precio unitario, subtotal, cargos/impuestos declarados, total y condición de pago aplicables al alcance definitivo mediante documento actualizado o confirmación explícita |
| H04 | P09, P10 | D1 p. 1 R1 aceptada por Luis Demo el 2026-11-17; C1 de 2026-11-18 solicita cambios y no confirma qué proforma sustituir | La aceptación de R1 no acredita aceptación de los cambios; versión aplicable sin resolver | Identificar expresamente qué documento/revisión sustituye o mantiene R1, aportar la versión correspondiente con fecha e identificador y evidencia atribuida de aprobación/aceptación del alcance final con identidad y fecha |

## 7. Preguntas y siguiente acción humana

1. H01–H02: ¿La cantidad final de L1 es 20 o 24 sillas y el acabado final es negro mate o blanco mate? Aportar la confirmación documental de ambos campos.
2. H03: ¿Cuáles son las condiciones comerciales y el total de mercancía del alcance final? Aportar la proforma o confirmación explícita que los documente, incluyendo los campos comerciales indicados en H03.
3. H04: ¿Qué documento y revisión quedan aplicables y cuál sustituye a DEMO-PF-004 R1, si corresponde? Aportar evidencia explícita de aprobación y aceptación del cliente vinculada al alcance y revisión finales, con identidad y fecha.

Siguiente acción humana: resolver conjuntamente los hallazgos con evidencia documental; después efectuar una nueva revisión conservando este informe. Este informe no aprueba ni ejecuta el pedido al proveedor.

## 8. Límites

Revisión exclusivamente documental de las fuentes enumeradas y de su coherencia según PEO-01 v1.1. No verifica autenticidad, autoridad de firmantes, capacidad de fabricación, calidad, viabilidad técnica, cumplimiento legal/aduanero ni condiciones externas. No certifica conformidad ISO ni atribuye a ISO los campos de este perfil. No se realizaron consultas de red, envíos, compras ni acciones externas. No se verificaron referencias normativas externas. La constancia de aceptación se registra como evidencia ficticia aportada, sin validación de firma o autoridad.