# Informe documental

## 1. Identificación

Expediente **DEMO-005**. Revisión de análisis: **1**, emitida el 17 de noviembre de 2026. Etapa declarada: **fabricación**, antes de iniciar la operación. Ruta de L1: fabricación. Perfil aplicado: **PEO-01 v1.0**; skill `revisor-expedientes-mobiliario`, instrucciones v1.0. Expediente **FICTICIO — SOLO PRUEBA TÉCNICA**.

## 2. Fuentes

Se recibieron y leyeron íntegramente dos archivos de texto:

- **C**: `pruebas/entradas/E2E-05-correo.md`. Asunto «Expediente DEMO-005 — fabricación de closet»; fecha `2026-11-17 11:00 UTC-05:00`; remitente `cliente@residencia-gamma.example`. No declara revisión propia. Se identifica por asunto y fecha y remite a FT-DEMO-005 R2. Las referencias siguientes usan sus párrafos o campos identificables.
- **F**: `pruebas/entradas/E2E-05-ficha.md`. Ficha **FT-DEMO-005**, fecha **2026-11-17**, revisión **R2**; vinculada explícitamente a DEMO-005, L1.

Documento mencionado pero no recibido: registro de medición del nicho. C indica «Se menciona un registro de medición del nicho, pero no se adjunta»; F, campo «Registro de medición en sitio», indica «no disponible». No hay archivos recibidos ilegibles. No se aportó revisión anterior del análisis.

## 3. Estado global

**PENDIENTE DE INFORMACIÓN**.

El requisito condicional F04 está activado porque L1 es un closet ajustado a un nicho existente. Falta el registro de medición con fecha y responsable y la confirmación de incorporación a R2 aprobada. Las fuentes disponibles son legibles y coherentes; no se identifica una contradicción documental aplicable.

## 4. Datos normalizados

Los estados de esta sección describen lo aportado, sin comprobación externa.

| Campo | Valor original / normalizado | Estado y procedencia |
|---|---|---|
| Expediente y etapa | «DEMO-005»; «fabricación» | aportado — C, asunto y campo «Etapa a revisar»; F, campo expediente |
| Cliente y contacto | «Residencia Gamma Demo»; `cliente@residencia-gamma.example` | aportado — C, campo cliente/contacto y remitente |
| Proyecto y uso | «Proyecto residencial» | aportado — C, párrafo de proyecto |
| Destino | «Casa Demo C, Ciudad de Panamá, Panamá» | aportado — C, destino; campo entrega confirma Casa Demo C |
| Línea, producto, cantidad y unidad | «L1: closet a medida ajustado a nicho existente, 1 unidad» | aportado — C, L1; F, expediente/línea/producto, «1 closet ajustado a nicho existente» |
| Dimensiones de L1 | «Dimensiones L x A x H: 2400 x 600 x 2400 mm»; largo 2400 mm, ancho 600 mm, alto 2400 mm | aportado — C y F, dimensiones; valores idénticos, sin conversión |
| Material | «tablero melamínico de 18 mm» | aportado — C, material; F, material |
| Acabado | «roble claro» | aportado — C y F, acabado |
| Ruta y fabricante | «fabricación»; «Taller Demo Local» | aportado — C, ruta/taller; F, taller |
| Moneda y precio unitario | «USD 1200.00 por unidad» | aportado — C, condiciones comerciales |
| Subtotal | «USD 1200.00» | aportado — C, condiciones comerciales |
| Transporte e instalación | «Instalación incluida; transporte incluido» | aportado — C, alcance/cargos; no se asigna importe separado |
| Impuestos y otros cargos | «impuestos USD 0.00; otros cargos USD 0.00» | aportado — C, cargos |
| Total | «USD 1200.00» | aportado — C, total |
| Pago | «50 % al aceptar y 50 % al terminar instalación» | aportado — C, pago |
| Entrega | «Casa Demo C, 2026-12-15» | aportado — C, entrega |
| Fabricación | «15 días calendario desde aprobación técnica» | aportado — C, plazo; hito inicial explícito, sin derivar fecha de terminación |
| Ficha aplicable | «FT-DEMO-005, fecha 2026-11-17, revisión R2» | aportado — C, ficha adjunta; F, encabezado |
| Aceptación del cliente | «Acepto alcance, cantidades, especificaciones y condiciones de R2»; «Sara Demo, 2026-11-17» | aportado — C, aceptación; evidencia documental ficticia, sin validar identidad o autoridad |
| Aprobación técnica | «Mateo Demo, 2026-11-17, aprueba esta ficha R2 según constancia ficticia de prueba» | aportado — F, revisión técnica, referida a FT-DEMO-005 R2 |
| Registro de medición, fecha y responsable | **NO APORTADO** | faltante — C, último párrafo; F, registro de medición |
| Confirmación de incorporación de medición a R2 aprobada | **NO APORTADO** | faltante — no consta en C ni F |

Comprobaciones aritméticas de apoyo, con importes declarados y comparación a centavos:

- 1 unidad × USD 1200.00/unidad = **USD 1200.00**, coincide con el subtotal declarado.
- USD 1200.00 + USD 0.00 de impuestos + USD 0.00 de otros cargos = **USD 1200.00**, coincide con el total declarado. Instalación y transporte se declaran incluidos; no se inventan sus importes separados.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Obligatorio, base de fabricación | satisfecho | C, asunto y etapa: DEMO-005 y fabricación. Identificador ficticio, sin atribución a ERP. |
| P02 | Obligatorio | satisfecho | C, cliente y contacto: Residencia Gamma Demo y correo explícito. |
| P03 | Obligatorio | satisfecho | C, proyecto residencial y destino Casa Demo C, Ciudad de Panamá, Panamá. Suficientemente identificado para esta demostración. |
| P04 | Obligatorio | satisfecho | C, L1: descripción, identificador único y 1 unidad; F corresponde a L1 y 1 closet. |
| P05 | Obligatorio | satisfecho | C y F: L x A x H 2400 x 600 x 2400 mm, tablero melamínico de 18 mm y roble claro. |
| P06 | Obligatorio | satisfecho | C, ruta: fabricación para la única línea L1. |
| P07 | Obligatorio | satisfecho | C, USD, precio unitario/subtotal/total 1200.00, impuestos/otros cargos 0.00, transporte e instalación incluidos y pago 50 %/50 %. Operaciones mostradas arriba sin discrepancia. |
| P08 | Obligatorio | satisfecho | C, entrega 2026-12-15 en Casa Demo C e instalación incluida. |
| P09 | Obligatorio | satisfecho | C identifica y acepta FT-DEMO-005 de 2026-11-17 R2; F disponible con esos datos y vínculo a DEMO-005/L1. El correo se identifica por asunto y fecha, sin revisión propia declarada. El registro ausente se conserva como faltante F04. |
| P10 | Obligatorio | satisfecho | C, aceptación explícita de alcance, cantidades, especificaciones y condiciones de R2 por Sara Demo, 2026-11-17. No acredita autoridad legal. |
| F01 | Obligatorio para L1 | satisfecho | C y F, Taller Demo Local identificado para L1. |
| F02 | Obligatorio para L1 | satisfecho | F disponible, FT-DEMO-005 R2, L1 y 1 closet; especificaciones coinciden con C y con la aceptación R2. |
| F03 | Obligatorio para L1 | satisfecho | F, revisión técnica: Mateo Demo, 2026-11-17, aprueba esta ficha R2; identificador en encabezado. Se registra la constancia ficticia, sin sustituir revisión técnica. |
| F04 | Condicional activado para L1 | faltante | C y F declaran closet ajustado a nicho existente. Registro de medición ausente; no constan fecha, responsable ni confirmación de incorporación a R2 aprobada. |
| F05 | Obligatorio para L1 | satisfecho | C, 15 días calendario desde aprobación técnica; destino Casa Demo C y entrega declarada. No se calcula ni promete fecha derivada del plazo. |
| I01 | No aplicable | NA | C declara exclusivamente fabricación en L1; no hay ruta de importación. |
| I02 | No aplicable | NA | L1 tiene ruta de fabricación explícita. |
| I03 | No aplicable | NA | L1 tiene ruta de fabricación explícita; no se exige despacho internacional. |
| I04 | No aplicable | NA | L1 tiene ruta de fabricación explícita; condiciones base revisadas bajo P07. |
| I05 | No aplicable | NA | L1 tiene ruta de fabricación explícita; plazo revisado bajo F05. |
| I06 | No aplicable | NA | No hay ruta de importación ni Incoterm utilizado en las fuentes. |

## 6. Hallazgos

### H01 — Medición del nicho y vínculo con la ficha aprobada no documentados

**Requisito afectado:** F04, L1.

**Valores y documentos:** C describe «closet a medida ajustado a nicho existente» y menciona un registro no adjunto. F confirma el ajuste al nicho y declara «Registro de medición en sitio: no disponible». La ficha FT-DEMO-005 R2 está aprobada documentalmente, pero no existe confirmación de incorporación de una medición registrada.

**Consecuencia documental:** no se satisface el control condicional de medición del espacio existente. Las dimensiones declaradas y la aprobación de la ficha no sustituyen ese registro. La ausencia no implica ilegibilidad ni conflicto entre fuentes y mantiene el expediente pendiente de información.

**Acción requerida:** aportar el registro de medición del nicho, con fecha e identificación del responsable, y evidencia explícita de su incorporación a FT-DEMO-005 R2 aprobada. Si la medición exige otra revisión, aportar esa revisión y las aprobaciones técnica y del cliente correspondientes, con evidencia de sustitución de R2; no se presume que exista tal cambio.

## 7. Preguntas y siguiente acción humana

Para resolver H01/F04 en una sola devolución documental:

1. ¿Cuál es el registro de medición del nicho de L1 y qué fecha y responsable documenta? Aportar el registro disponible completo y vinculado a DEMO-005/L1.
2. ¿Qué evidencia confirma que esa medición fue incorporada a FT-DEMO-005 R2 aprobada? Aportarla con referencia exacta a la ficha; si hubo cambios, aportar revisión resultante y evidencia explícita de sustitución y aceptación pertinente.

Siguiente acción humana: completar esa evidencia y someter el expediente a una nueva revisión documental que conserve este informe y registre qué documentos resuelven H01. Este informe no aprueba fabricación, compra, instalación ni otra operación.

## 8. Límites

Revisión exclusivamente documental de los dos archivos de texto recibidos, leídos directamente; no se empleó OCR, visión, red ni verificación externa. Los nombres, dimensiones, materiales, importes, aceptaciones y aprobaciones son afirmaciones del expediente ficticio. No se comprobó identidad, autoridad, autenticidad, medición física, calidad, factibilidad técnica o capacidad del taller. No se realizaron planos, ingeniería ni validaciones legales.

Los requisitos aplicados pertenecen al perfil de demostración PEO-01 v1.0. No constituyen una lista universal impuesta por ISO ni acreditan conformidad o certificación. No se verificó externamente el contenido normativo citado por el perfil.