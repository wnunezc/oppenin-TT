# Informe documental — DEMO-003

## 1. Identificación

Expediente DEMO-003. Revisión de análisis: 1, de 17 de noviembre de 2026. Etapa: importación, antes del pedido al proveedor. Ruta declarada para L1: importación. Perfil aplicado: PEO-01 v1.0; skill revisor-expedientes-mobiliario, instrucciones 1.0. El documento declara «FICTICIO — SOLO PRUEBA TÉCNICA»; el identificador no se atribuye a un ERP real.

## 2. Fuentes

Recibido y abierto localmente: `pruebas/entradas/E2E-03-proforma.pdf`, una página, proforma DEMO-PF-003 R1, fecha 2026-11-17, vigencia hasta 2026-12-01 inclusive. Se abrió y extrajo íntegramente la página 1 con Python/pypdf, sin extracción ajena, OCR, red o comprobación externa. La transcripción original está conservada en `texto-extraido.txt`. No hay páginas adicionales ni texto extraído marcado como no legible. El método es extracción de texto PDF, sin inspección visual de la maquetación.

Fuentes de reglas leídas íntegramente: SKILL.md y PERFIL-EXPEDIENTE.md. No se recibieron otras revisiones ni documentos de aceptación. La proforma no menciona adjuntos ausentes. La aceptación es expresamente pendiente; no se considera recibida por la frase genérica de aprobación.

## 3. Estado global

**PENDIENTE DE INFORMACIÓN.** La fuente esencial es legible y permite determinar etapa y ruta. Faltan la unidad de las dimensiones, el acabado definido, la condición de pago y evidencia explícita de aceptación y de versión aprobada por el cliente. No se identifica una contradicción documental comprobada. «Especificación y condiciones aprobadas: DEMO-PF-003 R1» no identifica quién aprobó ni cuándo; no equivale a aceptación del cliente, expresamente pendiente.

## 4. Datos normalizados

Todos los valores proceden de la página 1 de DEMO-PF-003 R1; se indican los campos para localizar cada dato. Son afirmaciones documentales, no comprobaciones externas.

| Campo | Original y valor conservado | Estado |
|---|---|---|
| Expediente / etapa | «Expediente: DEMO-003. Etapa solicitada: importación.» | aportado |
| Cliente / contacto | «Residencia Beta Demo»; beta@cliente.example | aportado |
| Proyecto / uso | «mobiliario residencial, sillas de comedor» | aportado |
| Destino | «Casa Demo B, Ciudad de Panamá, Panamá» | aportado |
| Proveedor / contacto | «Demo Furniture Export»; ventas@exportador.example | aportado |
| Línea / producto | «L1: silla modelo S-20» | aportado |
| Cantidad / unidad de conteo | «20 unidades» | aportado |
| Ruta L1 | «ruta importación» | aportado |
| Dimensiones L1 | «Dimensiones L x A x H: 500 x 550 x 850.» Se conserva L=500, A=550, H=850; unidad: NO APORTADO. No se convierten ni se presuponen mm. | faltante: unidad |
| Material L1 | «estructura de acero y asiento de polipropileno» | aportado |
| Acabado L1 | «por confirmar»; acabado definido: NO APORTADO | faltante |
| Moneda / precio unitario | «USD 80.00» | aportado |
| Subtotal | «USD 1600.00» | aportado |
| Embalaje | «incluido» | aportado |
| Transporte internacional / local | «excluido» en ambos campos; importes: NO APORTADO | aportado: exclusiones |
| Tributos de importación | «excluidos»; importe: NO APORTADO | aportado: exclusión |
| Impuestos de la proforma / otros cargos | «USD 0.00» / «USD 0.00» | aportado |
| Total proforma | «USD 1600.00»; «El total es de mercancía, no costo final puesto en destino.» | aportado |
| Condición de pago | NO APORTADO. «Desde recepción del anticipo» es un hito de preparación; no determina importe, porcentaje ni condición de pago. | faltante |
| Despacho / entrega | «China» / «Panamá»; no se declara país de fabricación | aportado |
| Preparación | «30 días calendario desde recepción del anticipo» | aportado |
| Transporte | «estimado 35 días calendario desde despacho» | aportado, estimado |
| Llegada | «no hay fecha firme de llegada» | aportado: ausencia declarada |
| Instalación | «No incluye instalación.» | aportado |
| Incoterm | «Las partes no han usado Incoterm en esta proforma.» | aportado |
| Documento / fecha / revisión / vigencia | DEMO-PF-003 / 2026-11-17 / R1 / hasta 2026-12-01 inclusive | aportado |
| Aprobación anunciada | «Especificación y condiciones aprobadas: DEMO-PF-003 R1.» Identidad, fecha y evidencia de aceptación: NO APORTADO. | faltante: evidencia |
| Aceptación del cliente | «pendiente»; identidad y fecha de aceptación: NO APORTADO | faltante |

Verificación decimal de importes declarados: 20 × USD 80.00 = USD 1600.00; USD 1600.00 + USD 0.00 de impuestos de esta proforma + USD 0.00 de otros cargos = USD 1600.00. Coincide a centavos con subtotal y total. Los costos excluidos no se consideran cero. No se calcula costo final en destino, tributos ni conversión monetaria. No se suman los plazos para prometer una fecha de llegada.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí: base | satisfecho | P. 1, expediente DEMO-003 y etapa importación explícitos. |
| P02 | Sí: base | satisfecho | P. 1, cliente Residencia Beta Demo y correo. |
| P03 | Sí: base | satisfecho | P. 1, proyecto residencial y Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí: base | satisfecho | P. 1, L1, silla S-20, 20 unidades; cantidad positiva. |
| P05 | Sí: base | faltante | P. 1, ejes L x A x H y valores presentes, unidad ausente; material presente; acabado «por confirmar». |
| P06 | Sí: base | satisfecho | P. 1, L1 ruta importación explícita. |
| P07 | Sí: base | faltante | P. 1, moneda, importes y exclusiones explícitos, coherentes aritméticamente; no declara condición de pago. |
| P08 | Sí: base | satisfecho | P. 1, preparación desde anticipo y transporte estimado desde despacho; destino declarado; instalación excluida. Se registra la naturaleza estimada, sin afirmar fecha firme. |
| P09 | Sí: base | faltante | P. 1, número, fecha, revisión y relación con DEMO-003/L1 presentes. La frase «aprobadas» carece de evidencia identificada de aprobación; aceptación del cliente pendiente. |
| P10 | Sí: base | faltante | P. 1, aceptación pendiente; faltan alcance y revisión aceptados con identidad y fecha. |
| F01 | No | NA | L1 declara únicamente importación; no hay ruta de fabricación. |
| F02 | No | NA | L1 declara únicamente importación; no hay ruta de fabricación. |
| F03 | No | NA | L1 declara únicamente importación; no hay ruta de fabricación. |
| F04 | No | NA | L1 declara únicamente importación; no se declara fabricación ajustada a espacio existente. |
| F05 | No | NA | L1 declara únicamente importación; no hay ruta de fabricación. |
| I01 | Sí: importación | satisfecho | P. 1, Demo Furniture Export; DEMO-PF-003, fecha 2026-11-17, R1, vigencia explícita hasta 2026-12-01 inclusive. |
| I02 | Sí: importación | faltante | P. 1, L1/S-20, cantidad y material presentes; dimensiones sin unidad y acabado pendiente. La única fuente no permite completar esos campos. |
| I03 | Sí: importación | satisfecho | P. 1, despacho China y entrega Panamá explícitos; no se infiere origen de fabricación. |
| I04 | Sí: importación | faltante | P. 1, precios y alcance de costos declarados; pago sin definir. Transporte y tributos excluidos, sin interpretarlos como costo cero. |
| I05 | Sí: importación | satisfecho | P. 1, preparación 30 días calendario desde recepción del anticipo y transporte estimado 35 días calendario desde despacho, ambos con hitos. No se exige llegada firme adicional ni se transforma la estimación en compromiso. |
| I06 | No: condición no activada | NA | P. 1, las partes declaran no haber usado Incoterm; no se inventa término, lugar o edición. Costos se evalúan en I04. |

## 6. Hallazgos

| ID | Requisitos | Valores/documentos involucrados | Consecuencia documental | Acción requerida |
|---|---|---|---|---|
| H01 | P05, I02 | DEMO-PF-003 R1, p. 1: «500 x 550 x 850», ejes L x A x H, sin unidad | Especificación dimensional incompleta; no puede normalizarse a una unidad ni comprobarse plenamente la correspondencia técnica. | Aportar unidad explícita para las tres dimensiones de L1 en documentación identificada. |
| H02 | P05, I02 | DEMO-PF-003 R1, p. 1: acabado «por confirmar» | No hay acabado definido para la línea. | Aportar acabado identificado e incorporarlo a la revisión sometida a aceptación. |
| H03 | P07, I04 | DEMO-PF-003 R1, p. 1: hito «recepción del anticipo», sin condición de pago | Los importes comerciales están presentes pero falta la condición de pago; el hito no permite reconstruirla. | Aportar condición de pago, incluido el anticipo mencionado y condiciones del saldo si corresponde, sin completarlas por suposición. |
| H04 | P09, P10 | DEMO-PF-003 R1, p. 1: frase genérica «aprobadas» y aceptación del cliente «pendiente» | La frase genérica no acredita aceptación del cliente ni identifica evidencia de aprobación de la revisión. No se trata como contradicción comprobada ni como autorización. | Aportar evidencia explícita de aceptación del cliente con identidad, fecha, alcance y revisión exacta, una vez definidos los campos pendientes. Si hay una revisión nueva, documentar su relación con R1 y la aceptación de los cambios. |

El transporte internacional, el transporte local y los tributos de importación están expresamente excluidos. Se conserva esa limitación del total como información aportada, sin exigir importes no previstos por el perfil ni presentar USD 1600.00 como costo final puesto en destino.

## 7. Preguntas y siguiente acción humana

1. ¿Qué unidad corresponde a L=500, A=550 y H=850 de L1?
2. ¿Cuál es el acabado definido de la silla S-20?
3. ¿Cuál es la condición de pago acordada, incluido el anticipo que inicia la preparación?
4. ¿Qué evidencia identifica a quien aceptó, la fecha, el alcance y la revisión aceptada por el cliente? La fuente actualmente declara esa aceptación pendiente.

La siguiente acción humana es reunir las respuestas en documentación identificada y aportar la aceptación explícita de la revisión resultante. Después corresponde una nueva revisión documental que conserve este informe y registre qué evidencia resuelve cada hallazgo. Este informe no aprueba el pedido al proveedor ni la importación. No se exigen declaración aduanera, conocimiento de embarque, packing list definitivo ni recepción de una operación aún no iniciada.

## 8. Límites

Revisión exclusivamente documental conforme a PEO-01 v1.0. Las afirmaciones proceden de la proforma ficticia y no fueron comprobadas externamente. La extracción de texto no acredita autenticidad, autoridad de firmantes, calidad del material, factibilidad, conformidad técnica o legal ni cumplimiento aduanero. No se realizaron acciones externas, envíos, instalaciones ni consultas de red. No se afirma certificación ni conformidad ISO; los controles aplicados son los del perfil de demostración.

No se aporta revisión de análisis anterior; no hay comparación de cambios que documentar.
