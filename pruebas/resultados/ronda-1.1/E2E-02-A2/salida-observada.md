# Informe documental — DEMO-002

## 1. Identificación

Expediente **DEMO-002**, revisión de análisis **1** de esta sesión independiente. Etapa solicitada: **importación**, antes del pedido al proveedor. Ruta de L1: **importación**. Perfil aplicado: **PEO-01 v1.1**, skill v1.1. La fuente declara «FICTICIO — SOLO PRUEBA TÉCNICA». Fechas del documento conservadas como datos ficticios; la hora real del análisis consta por separado en inicio.txt y registro.json.

## 2. Fuentes

- Reglas leídas íntegramente: SKILL.md y PERFIL-EXPEDIENTE.md, versiones 1.1.
- Único documento del expediente recibido: `pruebas/entradas/E2E-02-proforma.pdf`, una página, **PROFORMA DEMO-PF-002, R1, fecha 2026-11-17**, vinculada expresamente a DEMO-002 y L1. Vigencia: «hasta 2026-12-01 inclusive».
- No se recibieron correos ni una revisión de análisis anterior. No hay adjuntos referenciados ausentes ni archivos esenciales ilegibles.
- Método: apertura del PDF real con pypdf e iteración de su única página. La extracción propia se conserva sin corregir en extraccion-pypdf.txt. Por caracteres dañados en acentos, renderizado local de la página completa con pdftoppm y lectura visual directa de pagina-1.png. Todos los datos de este informe proceden de la página 1; el texto legible visualmente se transcribe aquí sin atribuirlo a comprobación externa. Poppler emitió avisos de fuentes Symbol y ArialUnicode, pero generó la página y su contenido esencial fue legible.
- Los hashes SHA-256 sobre bytes originales y rutas absolutas están en fuentes-sha256.json y registro.json.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA**.

Los controles obligatorios aplicables están satisfechos y no se identificaron contradicciones pendientes. La constancia de aceptación de la propia proforma aporta identidad, fecha y referencia explícita a la revisión aceptada. Este estado no aprueba la operación.

## 4. Datos normalizados

En esta sección, toda procedencia corresponde a **E2E-02-proforma.pdf, página 1**, campo indicado. No se efectuaron conversiones de unidades ni de moneda.

| Campo | Valor original aportado / valor de revisión | Procedencia y estado |
|---|---|---|
| Expediente y etapa | «Expediente: DEMO-002. Etapa solicitada: importación.» | Expediente/etapa; aportado |
| Documento | «PROFORMA DEMO-PF-002 \| R1 \| Fecha: 2026-11-17»; «Vigencia: hasta 2026-12-01 inclusive.» | Encabezado/vigencia; aportado |
| Cliente y contacto | «Residencia Beta Demo»; «beta@cliente.example» | Cliente/contacto; aportado |
| Proyecto y destino | «mobiliario residencial, sillas de comedor»; «Casa Demo B, Ciudad de Panamá, Panamá» | Proyecto/destino; aportado |
| Proveedor y contacto | «Demo Furniture Export»; «ventas@exportador.example» | Proveedor/contacto; aportado |
| Línea, descripción, cantidad y ruta | «L1: silla modelo S-20; 20 unidades; ruta importación.» | L1; aportado |
| Dimensiones | «Dimensiones L x A x H: 500 x 550 x 850 mm.»; largo 500 mm, ancho 550 mm, alto 850 mm, conservando orden y unidad de la fuente | Dimensiones; aportado |
| Material | «estructura de acero y asiento de polipropileno» | Material; aportado |
| Acabado | «negro mate» | Acabado; aportado |
| Precio y subtotal | «Precio unitario: USD 80.00. Subtotal: USD 1600.00.» | Precio; aportado |
| Costos | «Embalaje: incluido. Transporte internacional: excluido.»; «Transporte local: excluido. Tributos de importación: excluidos.» | Alcance de costos; aportado |
| Impuestos y otros cargos de la proforma | «Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00.» | Cargos; aportado |
| Total y alcance | «Total proforma: USD 1600.00. El total es de mercancía, no costo final puesto en destino.» | Total; aportado. Costo final en destino: NO APORTADO, expresamente fuera del total declarado |
| Pago | «30 % al confirmar pedido y 70 % antes del despacho» | Pago; aportado |
| Países | «País de despacho: China. País de entrega: Panamá.» | Países; aportado. No se interpreta China como origen de fabricación |
| Preparación | «30 días calendario desde recepción del anticipo» | Preparación; aportado |
| Transporte y llegada | «estimado 35 días calendario desde despacho»; «no hay fecha firme de llegada» | Transporte; aportado. Fecha firme: NO APORTADO; no requerida al estar declarados los plazos y sus hitos |
| Instalación | «No incluye instalación.» | Alcance del servicio; aportado |
| Incoterm | «Las partes no han usado Incoterm en esta proforma.» | Incoterm; aportado |
| Aprobación y aceptación | «Especificación y condiciones aprobadas: DEMO-PF-002 R1.»; «Constancia ficticia de aceptación del cliente: Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-002 R1.» | Constancia final; aportado. La constancia atribuida acredita documentalmente P09/P10; la frase genérica aislada no bastaría |

Comprobación aritmética decimal a centavos: **20 × USD 80.00 = USD 1600.00**; **USD 1600.00 + USD 0.00 (impuestos de la proforma) + USD 0.00 (otros cargos) = USD 1600.00**. Coincide con subtotal y total declarados. No se asigna valor cero a los costos excluidos ni se calcula un costo final en destino.

## 5. Checklist

Todas las referencias a campos corresponden a la página 1 del PDF recibido.

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Obligatorio | satisfecho | Campo expediente: DEMO-002; etapa importación. Identificador ficticio, sin atribución a ERP real. |
| P02 | Obligatorio | satisfecho | Cliente Residencia Beta Demo y contacto beta@cliente.example. |
| P03 | Obligatorio | satisfecho | Proyecto residencial de sillas de comedor; Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Obligatorio | satisfecho | L1 única, silla modelo S-20, 20 unidades; cantidad positiva. |
| P05 | Obligatorio | satisfecho | L x A x H 500 x 550 x 850 mm; estructura de acero/asiento de polipropileno; negro mate. |
| P06 | Obligatorio | satisfecho | L1 declara ruta importación. |
| P07 | Obligatorio | satisfecho | USD 80.00, subtotal y total USD 1600.00; impuestos/otros cargos USD 0.00; exclusiones expresas y pago 30 %/70 %. Aritmética coincidente. |
| P08 | Obligatorio | satisfecho | Preparación 30 días desde recepción del anticipo y transporte estimado 35 días desde despacho; instalación excluida. No se convierte la estimación en fecha firme. |
| P09 | Obligatorio | satisfecho | DEMO-PF-002 R1, fecha 2026-11-17; vínculo a DEMO-002/L1. Constancia de Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente líneas y condiciones de esa revisión. No hay correos recibidos que identificar. |
| P10 | Obligatorio | satisfecho | Constancia ficticia de aceptación del cliente con Luis Demo, correo, fecha y alcance/revisión DEMO-PF-002 R1 explícitos. Sin comprobación de autenticidad o autoridad. |
| F01 | No aplicable | NA | L1 declara exclusivamente importación; no hay línea de fabricación. |
| F02 | No aplicable | NA | Sin ruta de fabricación; no se exige plano/ficha de fabricación. |
| F03 | No aplicable | NA | Sin ruta de fabricación; no se exige aprobación técnica de fabricación. |
| F04 | No aplicable | NA | Sin ruta de fabricación ni condición declarada de ajuste a espacio existente. |
| F05 | No aplicable | NA | Sin ruta de fabricación; los plazos de importación se revisan en I05. |
| I01 | Obligatorio | satisfecho | Demo Furniture Export; proforma disponible DEMO-PF-002 R1, 2026-11-17, vigente hasta 2026-12-01 inclusive. |
| I02 | Obligatorio | satisfecho | La propia proforma identifica L1/S-20, 20 unidades, dimensiones en mm, material y acabado. No se recibió otra especificación incompatible. |
| I03 | Obligatorio | satisfecho | Despacho China; entrega Panamá, con destino Casa Demo B, Ciudad de Panamá. |
| I04 | Obligatorio | satisfecho | Moneda, pago y total declarados; embalaje incluido; transportes internacional/local y tributos de importación excluidos. El costo final no está cuantificado y no fue solicitado como total de esta proforma. |
| I05 | Obligatorio | satisfecho | Preparación 30 días calendario desde recepción del anticipo; transporte estimado 35 días calendario desde despacho. Ambos hitos están declarados; no se exige llegada firme adicional. |
| I06 | No aplicable | NA | La fuente declara expresamente que las partes no han usado Incoterm. Alcance de costos revisado en I04. |

## 6. Hallazgos

No se identificaron faltantes obligatorios ni contradicciones aplicables que requieran subsanación. No se crean hallazgos bloqueantes por los costos expresamente excluidos, la ausencia declarada de llegada firme o la inexistencia de Incoterm.

Observación documental de alcance, vinculada a P07/I04: USD 1600.00 corresponde a mercancía; transporte internacional, transporte local y tributos de importación están excluidos. El costo final puesto en destino permanece sin cuantificar. Esta observación no exige importes adicionales para satisfacer el alcance documental revisado.

## 7. Preguntas y siguiente acción humana

No hay preguntas bloqueantes derivadas de los controles aplicables. La siguiente acción corresponde a la revisión humana de DEMO-PF-002 R1 con el alcance y exclusiones declarados. Este informe no autoriza compra, importación, fabricación ni instalación; no se enviaron mensajes ni se ejecutó operación externa.

## 8. Límites

Revisión exclusivamente documental de la fuente recibida. La constancia se registra como evidencia ficticia aportada: no se verifican autenticidad, autoridad del aceptante, calidad de materiales, factibilidad técnica, cumplimiento legal/aduanero ni capacidades del proveedor. No se comprobaron datos externamente. PEO-01 es el perfil de demostración aplicado; no se afirma certificación ni conformidad ISO. No se consultaron normas ni fuentes externas. No se aportó una revisión anterior, por lo que no procede una comparación de cambios.
