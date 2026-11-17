# Informe documental

## 1. Identificación

Expediente **DEMO-002**, revisión de análisis **1**, etapa solicitada **importación**, antes del pedido al proveedor. Ruta declarada: **importación**, únicamente para L1. Perfil aplicado: **PEO-01 v1.0**, skill revisor-expedientes-mobiliario, instrucciones v1.0. El documento declara «FICTICIO — SOLO PRUEBA TÉCNICA»; sus personas, entidades y aceptación se tratan como datos ficticios.

## 2. Fuentes

- Recibido y leído íntegramente: `pruebas/entradas/E2E-02-proforma.pdf`, una página. Documento **DEMO-PF-002, R1**, fecha **2026-11-17**, vigencia **hasta 2026-12-01 inclusive**; vincula expresamente DEMO-002 y L1.
- Método: apertura del PDF real con `pypdf.PdfReader` y extracción de texto de **todas sus páginas (1/1)**, sin OCR ni comprobación externa. Texto original conservado en `extraccion-propia.txt`. Todos los campos citados a continuación proceden de la página 1.
- Referenciados ausentes: ninguno identificado. Archivos recibidos ilegibles: ninguno identificado en la extracción. Revisiones anteriores de análisis o documentos: no aportadas.
- Bases de revisión leídas íntegramente: `SKILL.md` y `PERFIL-EXPEDIENTE.md`. No son hechos del expediente.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA.** Los controles obligatorios aplicables están satisfechos documentalmente; no se identifican contradicciones pendientes. La exclusión expresa del transporte y tributos no equivale a costo cero puesto en destino. Este estado no aprueba ninguna operación.

## 4. Datos normalizados

Todos los datos siguientes están **aportados** como declaraciones documentales, sin comprobación externa.

| Campo | Valor original / normalizado | Procedencia |
|---|---|---|
| Expediente y etapa | «Expediente: DEMO-002. Etapa solicitada: importación.» | PDF p. 1, expediente |
| Documento | «PROFORMA DEMO-PF-002 | R1 | Fecha: 2026-11-17»; vigencia hasta 2026-12-01 inclusive | PDF p. 1, encabezado/vigencia |
| Solicitante/contacto | Residencia Beta Demo; beta@cliente.example | PDF p. 1, Cliente |
| Proyecto/uso | «mobiliario residencial, sillas de comedor» | PDF p. 1, Proyecto |
| Entrega | «Casa Demo B, Ciudad de Panamá, Panamá» | PDF p. 1, Destino |
| Proveedor/contacto | Demo Furniture Export; ventas@exportador.example | PDF p. 1, Proveedor |
| L1 | «silla modelo S-20; 20 unidades; ruta importación» | PDF p. 1, L1 |
| Dimensiones L1 | «Dimensiones L x A x H: 500 x 550 x 850 mm»; largo 500 mm, ancho 550 mm, alto 850 mm | PDF p. 1, Dimensiones |
| Material L1 | «estructura de acero y asiento de polipropileno» | PDF p. 1, Material |
| Acabado L1 | «negro mate» | PDF p. 1, Acabado |
| Moneda/precio/subtotal L1 | USD; unitario 80.00; subtotal 1600.00 | PDF p. 1, Precio unitario/Subtotal |
| Costos declarados | «Embalaje: incluido»; transporte internacional y local excluidos; tributos de importación excluidos | PDF p. 1, Embalaje/Transporte/Tributos |
| Importes de proforma | Impuestos USD 0.00; otros cargos USD 0.00; total USD 1600.00 | PDF p. 1, Impuestos/Otros cargos/Total |
| Alcance del total | «El total es de mercancía, no costo final puesto en destino» | PDF p. 1, Total proforma |
| Pago | «30 % al confirmar pedido y 70 % antes del despacho» | PDF p. 1, Pago |
| Países | Despacho China; entrega Panamá. País de origen de fabricación: NO APORTADO, sin exigencia adicional en este perfil | PDF p. 1, País de despacho/entrega |
| Preparación | «30 días calendario desde recepción del anticipo» | PDF p. 1, Preparación |
| Transporte | «estimado 35 días calendario desde despacho» | PDF p. 1, Transporte |
| Llegada | «no hay fecha firme de llegada»; fecha confirmada: NO APORTADO, no requerida al existir plazos con hitos | PDF p. 1, Transporte |
| Instalación | «No incluye instalación» | PDF p. 1, alcance |
| Incoterm | «Las partes no han usado Incoterm en esta proforma» | PDF p. 1, Incoterm |
| Versión aprobada | «Especificación y condiciones aprobadas: DEMO-PF-002 R1» | PDF p. 1, aprobación |
| Aceptación | «Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-002 R1» | PDF p. 1, Constancia ficticia de aceptación del cliente |

Comprobación aritmética decimal de importes declarados: **20 × USD 80.00 = USD 1600.00**; **USD 1600.00 + USD 0.00 (impuestos de esta proforma) + USD 0.00 (otros cargos) = USD 1600.00**, coincidente a centavos con el total de proforma. No se asigna importe cero a transportes ni tributos excluidos. Costo final puesto en destino: **NO APORTADO**, expresamente fuera del total indicado. No se suman plazos para prometer llegada ni se convierten monedas.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de pedido | satisfecho | P. 1: DEMO-002 y etapa importación explícitos; identificador ficticio, sin atribución a ERP real. |
| P02 | Sí | satisfecho | P. 1: Residencia Beta Demo y beta@cliente.example. |
| P03 | Sí | satisfecho | P. 1: mobiliario residencial/sillas de comedor y Casa Demo B, Ciudad de Panamá, Panamá; destino suficiente para la demostración. |
| P04 | Sí | satisfecho | P. 1: L1 única, silla S-20, 20 unidades, cantidad positiva. |
| P05 | Sí | satisfecho | P. 1: L x A x H 500 x 550 x 850 mm, estructura de acero, asiento de polipropileno y negro mate. |
| P06 | Sí | satisfecho | P. 1: ruta importación explícita para L1. |
| P07 | Sí | satisfecho | P. 1: USD 80.00/unitario, subtotal y total USD 1600.00, impuestos y otros cargos USD 0.00; embalaje incluido, transportes y tributos excluidos; pago 30 %/70 % con hitos. Total declarado limitado a mercancía; aritmética coincidente. |
| P08 | Sí | satisfecho | P. 1: preparación 30 días desde recepción de anticipo y transporte estimado 35 días desde despacho; destino declarado, instalación excluida. No hay fecha firme de llegada y no se inventa. |
| P09 | Sí | satisfecho | P. 1: DEMO-PF-002, fecha 2026-11-17, R1, vinculación DEMO-002/L1 y aceptación explícita de R1. |
| P10 | Sí | satisfecho | P. 1: constancia ficticia de Luis Demo con contacto y fecha 2026-11-17; acepta líneas y condiciones de DEMO-PF-002 R1. Evidencia documental, sin acreditar autoridad o autenticidad. |
| F01 | No | NA | P. 1: única línea L1 con ruta importación; no se declara fabricación. |
| F02 | No | NA | Misma ruta explícita: no corresponde ficha de fabricación. |
| F03 | No | NA | Misma ruta explícita: no corresponde aprobación técnica de fabricación. |
| F04 | No | NA | No hay línea de fabricación ni declaración de fabricación ajustada a espacio existente. |
| F05 | No | NA | No hay línea de fabricación; preparación importadora examinada con I05. |
| I01 | Sí, L1 importación | satisfecho | P. 1: proveedor Demo Furniture Export y proforma disponible DEMO-PF-002 R1, fecha 2026-11-17 y vigencia hasta 2026-12-01 inclusive. |
| I02 | Sí | satisfecho | P. 1: la propia proforma identifica L1/S-20, 20 unidades, dimensiones con ejes/mm, material y acabado; aceptación refiere la misma revisión. No hay otra fuente que contradiga la correspondencia. |
| I03 | Sí | satisfecho | P. 1: despacho China; entrega Panamá y Casa Demo B. Despacho no se interpreta como origen de fabricación. |
| I04 | Sí | satisfecho | P. 1: moneda, pago, precios y total explícitos; embalaje incluido y transportes/tributos excluidos. Costo final en destino no definido, sin ocultar la exclusión. |
| I05 | Sí | satisfecho | P. 1: preparación 30 días calendario desde recepción del anticipo y transporte estimado 35 días calendario desde despacho; hitos explícitos. No hay fecha firme de llegada. |
| I06 | Condición no activada | NA | P. 1: las partes declaran que no han usado Incoterm. No se exige término, lugar o edición; alcance revisado en I04. |

## 6. Hallazgos

No se identifican faltantes obligatorios ni contradicciones aplicables con la fuente aportada. Se registran estas precisiones documentales para conservar su alcance:

| ID | Requisito | Valores/documentos | Consecuencia documental | Acción requerida |
|---|---|---|---|---|
| H01 | P07/I04 | DEMO-PF-002 R1 p. 1: USD 1600.00 de mercancía; transportes internacional/local y tributos de importación excluidos | El total no representa costo final puesto en destino; las exclusiones no son costos cero ni contradicen el total expresamente limitado | Mantener el alcance al revisar humanamente. Si se requiere conocer el costo final, aportar importes de los conceptos excluidos; no constituye faltante obligatorio de esta revisión. |
| H02 | P08/I05 | DEMO-PF-002 R1 p. 1: 30 días desde anticipo; transporte estimado 35 días desde despacho; sin fecha firme de llegada | Los plazos están documentados con hitos, pero no hay compromiso de llegada a fecha cierta | Conservar el carácter estimado y no prometer una fecha sumando plazos; una llegada firme necesitaría confirmación expresa si se solicita. |

## 7. Preguntas y siguiente acción humana

No hay preguntas bloqueantes con los documentos recibidos. La siguiente acción es la **revisión humana** de DEMO-PF-002 R1 con su alcance de costos y plazos declarados y la constancia ficticia de aceptación. Este informe no autoriza confirmar el pedido, pagar, importar ni instalar. No se requieren documentos de una operación todavía no iniciada, como declaración aduanera, conocimiento de embarque, packing list definitivo o comprobante de recepción.

## 8. Límites

Revisión exclusivamente documental de una fuente ficticia, basada en texto extraído del PDF real. No se verificaron externamente identidad, autoridad, autenticidad, calidad, factibilidad, origen de fabricación ni cumplimiento técnico o legal. No se realizaron ingeniería, dictámenes aduaneros ni acciones externas. PEO-01 es un perfil de demostración: sus campos no se atribuyen a ISO; este informe no constituye certificación ni conformidad ISO. No se consultaron las referencias externas citadas en el perfil.
