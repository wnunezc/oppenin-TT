# Informe documental — DEMO-001

## 1. Identificación

Expediente declarado DEMO-001, ficticio, solo prueba técnica; no se atribuye a un ERP real. Revisión de análisis: 1 de esta ejecución. Etapa solicitada: pedido, antes de pedido al proveedor o fabricación. Ruta declarada para L1: fabricación. Skill revisor-expedientes-mobiliario, instrucciones versión 1.0; perfil PEO-01 v1.0.

## 2. Fuentes

Se leyó íntegramente `pruebas/entradas/E2E-01-correo.md`, correo textual con asunto «Aceptación pedido DEMO-001 — revisión R1», fecha 2026-11-17 09:00 UTC-05:00, remitente compras@oficina-alfa.example. El propio cuerpo identifica el documento DEMO-001-R1, revisión R1, fecha 2026-11-17. Las referencias a campos del cuerpo que siguen pertenecen siempre a este asunto y fecha. Se conserva su texto original en las citas de datos; son declaraciones de la fuente, no comprobaciones externas.

Fuentes normativas de esta revisión documental: `SKILL.md` y `PERFIL-EXPEDIENTE.md`, leídos íntegramente. No se consultaron fuentes externas. El correo dice «No se referencian adjuntos»; no se recibieron adjuntos ni hay documentos referenciados ausentes o medios ilegibles. No se aportó revisión anterior del análisis.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA.** Los controles base P01-P10 de la etapa pedido están satisfechos documentalmente y no se identifican contradicciones pendientes. Los controles adicionales de fabricación corresponden a la revisión de esa etapa y no se exigen simultáneamente en pedido. Este estado no aprueba ninguna operación.

## 4. Datos normalizados

Todos los siguientes datos tienen estado **aportado**. Procedencia: cuerpo del correo identificado en Fuentes, campos citados.

| Campo | Valor original y procedencia | Valor registrado/normalizado |
|---|---|---|
| Expediente y etapa | «Expediente DEMO-001. Solicito revisar etapa pedido.» | DEMO-001; pedido |
| Cliente y contacto | «Cliente: Oficina Alfa Demo. Contacto: compras@oficina-alfa.example.» | Oficina Alfa Demo; correo explícito |
| Proyecto y uso | «Proyecto: puestos administrativos, uso corporativo.» | Puestos administrativos; corporativo |
| Destino | «Entrega: Edificio Demo A, piso 2, Ciudad de Panamá, Panamá.» | Mismo destino declarado |
| Línea, descripción y cantidad | «Línea L1: escritorio independiente, 12 unidades.» | L1; escritorio independiente; 12 unidades |
| Dimensiones | «Dimensiones L x A x H: 1200 x 600 x 750 mm.» | Largo 1200 mm, ancho 600 mm, alto 750 mm; no se realiza conversión |
| Material y acabado | «Material: tablero melamínico de 18 mm. Acabado: blanco mate.» | Tablero melamínico, espesor declarado 18 mm; blanco mate |
| Ruta y ajuste | «Ruta L1: fabricación. No se ajusta a un espacio existente.» | Fabricación; sin ajuste declarado a espacio existente |
| Precio unitario y subtotal | «USD 150.00 por unidad; subtotal USD 1800.00.» | USD 150.00/unidad; USD 1800.00 |
| Cargos e impuestos | «Transporte USD 100.00; impuestos declarados USD 0.00; otros cargos USD 0.00; total USD 1900.00.» | Transporte USD 100.00; impuestos declarados USD 0.00; otros USD 0.00; total USD 1900.00 |
| Pago | «Pago: 50 % al aceptar y 50 % contra entrega.» | Mismos porcentajes e hitos declarados |
| Fecha y servicio | «Entrega: 2026-12-15. No incluye instalación.» | Fecha expresa 2026-12-15; instalación excluida |
| Documento y revisión | «Documento de alcance: este correo DEMO-001-R1, revisión R1, fecha 2026-11-17. No se referencian adjuntos.» | Correo DEMO-001-R1; R1; 2026-11-17; alcance L1 |
| Aceptación | «Acepto expresamente las cantidades, especificaciones, condiciones comerciales y alcance de esta revisión R1.» y «Nombre de aceptación: Elena Demo, 2026-11-17.» | Aceptación explícita de R1; Elena Demo; 2026-11-17 |

Comprobación aritmética decimal a centavos: 12 × USD 150.00 = USD 1800.00. USD 1800.00 + USD 100.00 + USD 0.00 + USD 0.00 = USD 1900.00. Ambos resultados coinciden con los importes declarados. No se calculan tributos ni se comprueba externamente su procedencia.

## 5. Checklist

La evidencia de P01-P10 corresponde a los campos originales del correo reproducidos en Datos normalizados.

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Obligatorio: pedido | satisfecho | DEMO-001 y etapa pedido explícitos; carácter ficticio declarado. |
| P02 | Obligatorio: pedido | satisfecho | Oficina Alfa Demo y compras@oficina-alfa.example. |
| P03 | Obligatorio: pedido | satisfecho | Puestos administrativos, uso corporativo y Edificio Demo A, piso 2, Ciudad de Panamá, Panamá. |
| P04 | Obligatorio: pedido | satisfecho | Única línea L1, escritorio independiente, cantidad positiva 12, unidad de conteo «unidades». |
| P05 | Obligatorio: pedido | satisfecho | L x A x H de 1200 x 600 x 750 mm; material y acabado explícitos. |
| P06 | Obligatorio: pedido | satisfecho | Ruta L1 expresamente fabricación. |
| P07 | Obligatorio: pedido | satisfecho | Moneda, precio, subtotal, transporte, impuestos, otros cargos, total y pago explícitos; aritmética coincidente. |
| P08 | Obligatorio: pedido | satisfecho | Fecha expresa 2026-12-15 e instalación excluida. No requiere convertir un plazo relativo. |
| P09 | Obligatorio: pedido | satisfecho | Documento DEMO-001-R1, fecha y R1 identificados; aceptación expresa de esta revisión y ninguna referencia a adjuntos. |
| P10 | Obligatorio: pedido | satisfecho | Aceptación explícita de cantidades, especificaciones, condiciones y alcance R1; Elena Demo, 2026-11-17. Se registra evidencia, sin acreditar autoridad real o firma legal. |
| F01 | No aplicable en etapa pedido | NA | La etapa declarada es pedido; la identificación de taller se exige al revisar fabricación. |
| F02 | No aplicable en etapa pedido | NA | La etapa declarada es pedido; la ficha/plano de fabricación se exige en esa etapa. |
| F03 | No aplicable en etapa pedido | NA | La aprobación técnica corresponde a la revisión de fabricación. |
| F04 | No aplicable | NA | Además de la etapa pedido, la fuente declara escritorio independiente que no se ajusta a un espacio existente; no activa la condición. |
| F05 | No aplicable en etapa pedido | NA | El plazo de fabricación es control adicional de fabricación; la entrega base está documentada en P08. |
| I01 | No aplicable | NA | Etapa pedido y única ruta declarada fabricación; no se declara importación. |
| I02 | No aplicable | NA | No hay línea de importación declarada; no se exige correspondencia con proforma. |
| I03 | No aplicable | NA | No hay ruta de importación declarada; no se exige país de despacho. |
| I04 | No aplicable | NA | No hay ruta de importación declarada; se evalúan condiciones de pedido en P07. |
| I05 | No aplicable | NA | No hay ruta de importación declarada; no se exigen plazos de despacho/transporte de importación. |
| I06 | No aplicable | NA | No hay ruta de importación declarada y las fuentes no utilizan Incoterm. |

## 6. Hallazgos

No se identifican faltantes obligatorios, datos no legibles ni contradicciones aplicables a la etapa pedido. No se generan hallazgos bloqueantes ni se añaden requisitos de etapas posteriores.

## 7. Preguntas y siguiente acción humana

No hay preguntas necesarias para resolver bloqueantes documentales en esta etapa. Siguiente acción: revisión humana del expediente DEMO-001-R1 y de la evidencia declarada. Este informe no acepta el pedido ni autoriza compra, fabricación, importación o instalación. Si se revisa posteriormente la etapa fabricación, deberá evaluarse con sus controles adicionales y la evidencia que entonces se aporte.

## 8. Límites

Revisión exclusivamente documental del texto recibido. No se verificaron externamente identidad, autoridad, autenticidad, direcciones, disponibilidad, precios, impuestos, viabilidad de entrega, calidad del material, capacidad de fabricación ni cumplimiento técnico o legal. El resultado registra la aceptación declarada y no sustituye revisión técnica ni legal. No hubo acciones externas ni envíos. Los campos son del perfil de demostración PEO-01 v1.0; no se afirma certificación ni conformidad ISO, ni se verificó el texto normativo completo. No existe revisión anterior aportada para comparación.