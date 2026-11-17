# Informe documental — DEMO-002

## 1. Identificación

Expediente DEMO-002; revisión de análisis 1, independiente. Etapa solicitada: importación, antes del pedido al proveedor. Ruta L1: importación. Perfil aplicado: PEO-01 v1.1; skill 1.1. Expediente expresamente ficticio: «FICTICIO — SOLO PRUEBA TÉCNICA». Las fechas documentales se conservan según la fuente.

## 2. Fuentes

Recibido y leído: `pruebas/entradas/E2E-09-escaneado.pdf`, una página, proforma DEMO-PF-002 R1, fecha 2026-11-17, vigencia hasta 2026-12-01 inclusive. No se recibió revisión anterior de informe ni se mencionan adjuntos ausentes.

Se abrió el PDF original con pypdf y se iteró su única página. La extracción fue vacía; se renderizó completa con pdftoppm a PNG a 150 dpi y se leyó mediante visión directa. Se conservaron `extraccion-pypdf.txt`, `pagina-1.png` y `transcripcion-visual.txt`. El contenido esencial resultó legible por visión; la extracción vacía no se considera ausencia de datos. Las ubicaciones siguientes se refieren siempre a esa página del PDF.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA**. Todos los controles obligatorios aplicables están satisfechos documentalmente y no se observan contradicciones pendientes. Este estado no aprueba la operación.

## 4. Datos normalizados

Los datos siguientes están `aportado`; su procedencia es la página 1 de DEMO-PF-002 R1. Se preserva la transcripción visual completa como evidencia.

| Campo y ubicación | Valor original / dato normalizado |
|---|---|
| Encabezado, identificador y etapa | «Expediente: DEMO-002. Etapa solicitada: importación.» |
| Encabezado documental | «PROFORMA DEMO-PF-002 \| R1 \| Fecha: 2026-11-17»; vigencia «hasta 2026-12-01 inclusive» |
| Superior, cliente/contacto | Residencia Beta Demo; beta@cliente.example |
| Superior, proyecto/destino | «mobiliario residencial, sillas de comedor»; «Casa Demo B, Ciudad de Panamá, Panamá» |
| Superior, proveedor | Demo Furniture Export; ventas@exportador.example |
| Línea L1 | «silla modelo S-20; 20 unidades; ruta importación» |
| Especificación L1 | «Dimensiones L x A x H: 500 x 550 x 850 mm»; largo (L) 500 mm, ancho (A) 550 mm, alto (H) 850 mm; no se hizo conversión |
| Material/acabado L1 | «estructura de acero y asiento de polipropileno»; «negro mate» |
| Centro, importes | «Precio unitario: USD 80.00. Subtotal: USD 1600.00»; «Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00»; «Total proforma: USD 1600.00» |
| Alcance de costos | Embalaje incluido; transporte internacional y local excluidos; tributos de importación excluidos. «El total es de mercancía, no costo final puesto en destino» |
| Pago | «30 % al confirmar pedido y 70 % antes del despacho» |
| Países | Despacho: China; entrega: Panamá. País de fabricación: NO APORTADO, no exigido por I03 |
| Plazos | «Preparación: 30 días calendario desde recepción del anticipo»; «Transporte: estimado 35 días calendario desde despacho; no hay fecha firme de llegada» |
| Servicio/Incoterm | «No incluye instalación»; «Las partes no han usado Incoterm en esta proforma» |
| Inferior, aprobación/aceptación | «Especificación y condiciones aprobadas: DEMO-PF-002 R1». Constancia ficticia: «Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-002 R1» |

Comprobación decimal a centavos: 20 × USD 80.00 = USD 1600.00; USD 1600.00 + USD 0.00 (impuestos de la proforma) + USD 0.00 (otros cargos) = USD 1600.00. Los costos excluidos no se interpretan como cero ni se suman al total de mercancía. No se convierten los plazos en fecha de llegada.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de importación | satisfecho | P. 1, superior: DEMO-002 y etapa importación explícitos. Identificador ficticio, no atribuido a ERP. |
| P02 | Sí | satisfecho | P. 1, cliente: Residencia Beta Demo y beta@cliente.example. |
| P03 | Sí | satisfecho | P. 1, proyecto/destino: mobiliario residencial; Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí | satisfecho | P. 1, L1: identificador único, silla S-20, cantidad positiva 20 unidades. |
| P05 | Sí | satisfecho | P. 1, dimensiones/material/acabado: L x A x H 500 x 550 x 850 mm; acero y polipropileno; negro mate. |
| P06 | Sí | satisfecho | P. 1, L1: ruta importación expresamente declarada. |
| P07 | Sí | satisfecho | P. 1, bloque comercial: USD, unitario 80.00, subtotal y total 1600.00, impuestos/otros 0.00, exclusiones expresas y pago 30 %/70 %. Aritmética coherente. |
| P08 | Sí | satisfecho | P. 1, plazos/servicio: preparación 30 días desde anticipo y transporte estimado 35 días desde despacho; instalación excluida. Sin compromiso de llegada firme. |
| P09 | Sí | satisfecho | P. 1, encabezado y constancia inferior: DEMO-PF-002 R1, fecha, relación con DEMO-002/L1 y aceptación expresa de líneas y condiciones de esa revisión por Luis Demo, correo y fecha 2026-11-17. La evidencia atribuida complementa la frase genérica de aprobación. No hay correos recibidos que identificar. |
| P10 | Sí | satisfecho | P. 1, inferior: Luis Demo, beta@cliente.example, fecha 2026-11-17, aceptación expresa de líneas y condiciones de DEMO-PF-002 R1. |
| F01 | No | NA | P. 1, L1: ruta únicamente importación; no se solicita fabricación. |
| F02 | No | NA | P. 1, L1: no hay línea de fabricación. |
| F03 | No | NA | P. 1, L1: no hay ruta de fabricación que active aprobación técnica de fabricación. |
| F04 | No | NA | P. 1, alcance de sillas importadas; no se declara fabricación ajustada a espacio existente. |
| F05 | No | NA | P. 1, L1: ruta importación; plazo de fabricación no aplicable. |
| I01 | Sí, importación | satisfecho | P. 1: Demo Furniture Export; proforma disponible DEMO-PF-002, fecha 2026-11-17, R1 y vigencia hasta 2026-12-01 inclusive. |
| I02 | Sí | satisfecho | P. 1: L1 incluida en la propia proforma con S-20, 20 unidades, dimensiones con unidad, material y acabado; no hay otra especificación recibida incompatible. |
| I03 | Sí | satisfecho | P. 1: despacho China, entrega Panamá y destino Casa Demo B. No se confunde despacho con fabricación. |
| I04 | Sí | satisfecho | P. 1: USD, pago, importes y alcance de costos explícitos; embalaje incluido, transportes y tributos excluidos. |
| I05 | Sí | satisfecho | P. 1: preparación 30 días calendario desde anticipo; transporte estimado 35 días desde despacho. La fuente dice que no hay fecha firme; ambos plazos y sus hitos están aportados. |
| I06 | No, condición no activada | NA | P. 1: las partes expresan que no han usado Incoterm; el alcance se evalúa por I04. |

## 6. Hallazgos

No se identifican faltantes obligatorios, contradicciones o campos esenciales no legibles. No hay bloqueantes documentales del perfil.

Observación H01, P07/I04/I05: el total USD 1600.00 corresponde a mercancía y excluye transporte internacional/local y tributos de importación; el costo final puesto en destino no está cuantificado. El transporte es estimado y no hay fecha firme de llegada. Son alcances expresamente declarados, no incumplimientos ni razones para exigir importes excluidos o una llegada firme en esta revisión. Acción: conservar estas condiciones visibles en la revisión humana.

## 7. Preguntas y siguiente acción humana

No se requieren aclaraciones para completar los controles documentales aplicables. Siguiente acción: revisión humana de DEMO-PF-002 R1 considerando sus exclusiones y plazos estimados, sin que este informe autorice pedido, importación o instalación.

## 8. Límites

Revisión exclusivamente documental del único PDF recibido y sus datos visibles. No se comprueban externamente identidad, autenticidad, autoridad de quien acepta, calidad de materiales, factibilidad técnica, condiciones legales/aduaneras ni cumplimiento normativo. La aceptación se registra como constancia ficticia aportada. PEO-01 es un perfil de demostración y este informe no certifica conformidad ISO. No se usaron red ni acciones externas.
