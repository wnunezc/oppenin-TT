# 1. Identificación

Expediente ficticio **DEMO-002**, revisión de análisis **1**. Etapa solicitada: **importación**, antes del pedido al proveedor. Línea L1, ruta explícita de importación. Perfil aplicado: **PEO-01 v1.0**, skill `revisor-expedientes-mobiliario`, instrucciones v1.0. El encabezado declara «FICTICIO — SOLO PRUEBA TÉCNICA»; el identificador no se atribuye a un ERP real.

# 2. Fuentes

Única fuente del expediente recibida y abierta: `pruebas/entradas/E2E-08-proforma.png`, página 1, proforma **DEMO-PF-002**, **R1**, fecha **2026-11-17**, vigencia «hasta 2026-12-01 inclusive» (región superior). Se leyó directamente mediante visión con `tools.view_image` y presentación de su imagen mediante `image`; no se utilizó OCR ni extracción textual ni PDF.

Regiones de procedencia utilizadas: superior (encabezado, identificación y datos de cliente/proyecto/proveedor); centro (línea, especificaciones, importes y condiciones); inferior del bloque de texto (plazos, Incoterm y aceptación), y pie de página (página 1). No se observaron campos no legibles. No se mencionan adjuntos ausentes ni revisiones anteriores. Las afirmaciones se transcriben de esta imagen; no constituyen comprobaciones externas.

# 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA.** Los requisitos obligatorios aplicables a la importación de L1 están documentados; no se identifican contradicciones. El total de mercancía está expresamente separado del costo final en destino, con costos excluidos identificados. Este estado no aprueba operación alguna.

# 4. Datos normalizados y texto original

Todos los datos siguientes tienen estado **aportado**, salvo los campos expresamente indicados. Fuente común: `pruebas/entradas/E2E-08-proforma.png`, página 1.

| Campo | Texto original visible | Valor / procedencia |
|---|---|---|
| Documento | «PROFORMA DEMO-PF-002 \| R1 \| Fecha: 2026-11-17»; «Vigencia: hasta 2026-12-01 inclusive.» | DEMO-PF-002 R1, 2026-11-17, vigente hasta 2026-12-01 inclusive; superior |
| Expediente y etapa | «Expediente: DEMO-002. Etapa solicitada: importación.» | DEMO-002; importación; superior |
| Cliente/contacto | «Cliente: Residencia Beta Demo. Contacto: beta@cliente.example.» | Residencia Beta Demo; beta@cliente.example; superior |
| Proyecto/uso | «Proyecto: mobiliario residencial, sillas de comedor.» | Mobiliario residencial; sillas de comedor; superior |
| Destino | «Destino: Casa Demo B, Ciudad de Panamá, Panamá.» | Casa Demo B, Ciudad de Panamá, Panamá; superior |
| Proveedor | «Proveedor: Demo Furniture Export. Contacto: ventas@exportador.example.» | Demo Furniture Export; ventas@exportador.example; superior |
| Línea/ruta | «L1: silla modelo S-20; 20 unidades; ruta importación.» | L1, silla S-20, cantidad 20, unidad de conteo unidades, importación; centro |
| Dimensiones | «Dimensiones L x A x H: 500 x 550 x 850 mm.» | Ejes rotulados L/A/H: 500/550/850 mm; se conservan las etiquetas originales; centro |
| Material | «Material: estructura de acero y asiento de polipropileno.» | Estructura de acero; asiento de polipropileno; centro |
| Acabado | «Acabado: negro mate.» | Negro mate; centro |
| Precio/subtotal | «Precio unitario: USD 80.00. Subtotal: USD 1600.00.» | USD 80.00/unidad; subtotal USD 1600.00; centro |
| Embalaje y transporte internacional | «Embalaje: incluido. Transporte internacional: excluido.» | Embalaje incluido; transporte internacional excluido; centro |
| Otros costos excluidos | «Transporte local: excluido. Tributos de importación: excluidos.» | Transporte local y tributos de importación excluidos; centro |
| Impuestos/cargos de proforma | «Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00.» | USD 0.00 / USD 0.00; centro |
| Total y alcance | «Total proforma: USD 1600.00. El total es de mercancía, no costo final puesto en destino.» | Total mercancía USD 1600.00; costo final puesto en destino: **NO APORTADO**, no es el total declarado ni se considera cero; centro |
| Pago | «Pago: 30 % al confirmar pedido y 70 % antes del despacho.» | Condición de pago declarada; centro |
| Países | «País de despacho: China. País de entrega: Panamá.» | Despacho China; entrega Panamá; país de fabricación: **NO APORTADO**, no se infiere del despacho; centro |
| Preparación | «Preparación: 30 días calendario desde recepción del anticipo.» | 30 días calendario; hito: recepción del anticipo; inferior del bloque |
| Transporte/llegada | «Transporte: estimado 35 días calendario desde despacho; no hay fecha firme de llegada. No incluye instalación.» | Transporte estimado 35 días calendario desde despacho; llegada firme no aportada, expresamente no confirmada; instalación excluida; inferior del bloque |
| Incoterm | «Las partes no han usado Incoterm en esta proforma.» | No utilizado; inferior del bloque |
| Revisión aprobada | «Especificación y condiciones aprobadas: DEMO-PF-002 R1.» | DEMO-PF-002 R1; inferior del bloque |
| Aceptación | «Constancia ficticia de aceptación del cliente: Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-002 R1.» | Luis Demo; beta@cliente.example; 2026-11-17; alcance: líneas y condiciones de DEMO-PF-002 R1; inferior del bloque |
| Página/caracterización | «FICTICIO - SOLO PRUEBA TÉCNICA \| Página 1» | Página 1; ficticio; pie |

Comprobación aritmética de apoyo con importes decimales declarados: **20 × USD 80.00 = USD 1600.00**; **USD 1600.00 + USD 0.00 + USD 0.00 = USD 1600.00**. Coincide a centavos con el subtotal y total de proforma. No se suman costos excluidos como cero, no se convierten monedas ni se calculan tributos. No se transforma el plazo de transporte en compromiso de llegada ni se suman estimaciones para prometer una fecha.

# 5. Checklist

Evidencia común: imagen citada, página 1. Los datos se evalúan como afirmaciones documentales del expediente ficticio.

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de importación | satisfecho | Superior: DEMO-002 y etapa importación declarados. |
| P02 | Sí | satisfecho | Superior: Residencia Beta Demo y beta@cliente.example. |
| P03 | Sí | satisfecho | Superior: proyecto residencial de sillas de comedor; Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí | satisfecho | Centro: L1 única, silla S-20, 20 unidades positivas. |
| P05 | Sí | satisfecho | Centro: L x A x H 500 x 550 x 850 mm; acero/polipropileno y negro mate. Se conserva nomenclatura de ejes de la fuente. |
| P06 | Sí | satisfecho | Centro: L1 declara ruta importación. |
| P07 | Sí | satisfecho | Centro: USD, unitario, subtotal, impuestos/cargos y total, pago 30 %/70 %. Total exclusivamente de mercancía y exclusiones expresas. Aritmética coincidente. |
| P08 | Sí | satisfecho | Inferior del bloque: preparación desde recepción del anticipo, transporte estimado desde despacho; instalación excluida. La fuente no confirma llegada firme. |
| P09 | Sí | satisfecho | Superior e inferior: DEMO-PF-002, fecha 2026-11-17, R1, relación con L1 y aceptación expresa de esa revisión. |
| P10 | Sí | satisfecho | Inferior: constancia ficticia de Luis Demo, contacto, 2026-11-17, acepta líneas y condiciones de DEMO-PF-002 R1. No acredita autoridad o firma legal. |
| F01 | No | NA | L1 declara exclusivamente importación; no hay línea de fabricación. |
| F02 | No | NA | Misma ruta declarada: no se revisa fabricación. |
| F03 | No | NA | No hay fabricación declarada que active aprobación técnica de fabricación. |
| F04 | No | NA | Ruta importación; no se declara fabricación ajustada a un espacio existente. |
| F05 | No | NA | L1 solo importación; sus plazos se revisan en P08/I05. |
| I01 | Sí | satisfecho | Superior: proveedor Demo Furniture Export; proforma disponible DEMO-PF-002 R1, fecha y vigencia explícitas. |
| I02 | Sí | satisfecho | Centro: L1 S-20, 20 unidades, dimensiones con mm, material y acabado, integrados en la misma proforma aceptada. |
| I03 | Sí | satisfecho | Centro/superior: despacho China; país de entrega Panamá y destino Casa Demo B. No se confunde despacho con origen de fabricación. |
| I04 | Sí | satisfecho | Centro: moneda, importes y pago; embalaje incluido, transporte internacional/local y tributos excluidos. El total no representa costo final en destino. |
| I05 | Sí | satisfecho | Inferior del bloque: preparación 30 días calendario desde anticipo y transporte estimado 35 días calendario desde despacho; sin fecha firme de llegada. |
| I06 | No, condición no activada | NA | Inferior: «Las partes no han usado Incoterm en esta proforma.» No se inventa término, lugar ni edición. |

# 6. Hallazgos

No se identificaron faltantes obligatorios ni contradicciones documentales aplicables en la fuente recibida.

| ID | Requisito | Valores/documento | Consecuencia documental y acción humana |
|---|---|---|---|
| OBS-01 | P07 / I04 | DEMO-PF-002 R1: USD 1600.00 es total de mercancía; transporte internacional, local y tributos excluidos | El costo final en destino no está cuantificado. El alcance de costos está explícito y satisface el control documental. Para una decisión económica integral, la revisión humana debe considerar separadamente los costos excluidos; no tratarlos como cero. |
| OBS-02 | P08 / I05 | Preparación 30 días desde recepción de anticipo; transporte estimado 35 días desde despacho; no hay llegada firme | Son condiciones con hitos declarados, no promesa de fecha de llegada. Conservar esta distinción en la revisión humana. |

Estas observaciones no se presentan como contradicciones ni requisitos adicionales del perfil.

# 7. Preguntas y siguiente acción humana

No hay preguntas bloqueantes para completar esta revisión documental según PEO-01. Siguiente acción: someter DEMO-PF-002 R1 y su aceptación ficticia a revisión humana, teniendo presentes los costos excluidos y el carácter estimado del transporte. Este informe no aprueba ni ordena compra, importación, fabricación o instalación.

# 8. Límites

Revisión exclusivamente documental de una imagen de prueba ficticia. Visión directa del texto visible; sin comprobación externa de autenticidad, proveedor, identidad/autoridad de quien acepta, calidad de materiales, factibilidad, fabricación, condiciones comerciales reales o cumplimiento técnico, legal o aduanero. No se deducen propiedades de apariencia fotográfica. No se exige documentación aduanera o logística definitiva de una operación aún no iniciada.

PEO-01 es un perfil de demostración; sus campos no se atribuyen a una norma ISO ni esta revisión acredita conformidad o certificación. Las referencias ISO incluidas en el perfil no fueron consultadas externamente en esta revisión. No se aportó revisión anterior del análisis; no se reconstruyen antecedentes.