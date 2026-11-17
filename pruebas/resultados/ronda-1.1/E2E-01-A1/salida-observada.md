# Informe documental — DEMO-001

## 1. Identificación

Expediente ficticio DEMO-001, solo prueba técnica. Revisión de análisis: 1, independiente. Etapa solicitada: pedido, antes de fabricación. Ruta declarada de L1: fabricación. Perfil aplicado: PEO-01 v1.1, skill 1.1. Las fechas del expediente son datos declarados y se distinguen del sello real de análisis conservado en inicio.txt.

## 2. Fuentes

- Recibido y leído íntegramente: `pruebas/entradas/E2E-01-correo.md`. Remitente: compras@oficina-alfa.example; destinatario: pedidos@demo-mobiliario.example; fecha: 2026-11-17 09:00 UTC-05:00; asunto: «Aceptación pedido DEMO-001 — revisión R1». El propio correo declara identificador DEMO-001-R1, revisión R1, fecha 2026-11-17.
- Instrucciones aplicadas: `SKILL.md` versión 1.1 y `PERFIL-EXPEDIENTE.md` PEO-01 v1.1, leídos íntegramente.
- Adjuntos recibidos: ninguno. El correo declara «No se referencian adjuntos»; no se identifican documentos referenciados ausentes ni archivos ilegibles.
- No se recibió una revisión anterior de informe. No hay PDF ni PNG en las fuentes autorizadas de este caso; no se empleó extracción PDF, renderizado ni visión.

Las referencias C1 siguientes identifican el correo por remitente, fecha y asunto anteriores. Las ubicaciones se expresan mediante el párrafo/campo literal que inicia cada dato; no son comprobaciones externas.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA**.

Los requisitos obligatorios aplicables a la etapa pedido están documentados y no se identifican contradicciones pendientes. La ruta de fabricación está declarada, pero no convierte esta revisión de pedido en una revisión de la etapa fabricación. Este estado no autoriza la operación.

## 4. Datos normalizados

Todos los valores de esta sección tienen estado de dato `aportado`; son declaraciones de C1.

| Campo | Valor original / normalizado | Procedencia |
|---|---|---|
| Expediente y etapa | «Expediente DEMO-001. Solicito revisar etapa pedido.» | C1, párrafo Expediente |
| Cliente y contacto | «Oficina Alfa Demo»; «compras@oficina-alfa.example» | C1, campo Cliente / Contacto |
| Proyecto y uso | «puestos administrativos, uso corporativo» | C1, campo Proyecto |
| Destino | «Edificio Demo A, piso 2, Ciudad de Panamá, Panamá» | C1, primer campo Entrega |
| Línea / descripción | L1; «escritorio independiente» | C1, campo Línea L1 |
| Cantidad / unidad | «12 unidades» | C1, campo Línea L1 |
| Dimensiones y ejes | «L x A x H: 1200 x 600 x 750 mm»; largo 1200 mm, ancho 600 mm, alto 750 mm | C1, campo Dimensiones |
| Material | «tablero melamínico de 18 mm» | C1, campo Material |
| Acabado | «blanco mate» | C1, campo Acabado |
| Ruta / ajuste a sitio | «fabricación. No se ajusta a un espacio existente.» | C1, campo Ruta L1 |
| Moneda / precio / subtotal | «USD 150.00 por unidad; subtotal USD 1800.00» | C1, párrafo USD |
| Cargos y total | «Transporte USD 100.00; impuestos declarados USD 0.00; otros cargos USD 0.00; total USD 1900.00» | C1, párrafo Transporte y continuación |
| Pago | «50 % al aceptar y 50 % contra entrega» | C1, campo Pago |
| Entrega / instalación | «2026-12-15. No incluye instalación.» | C1, segundo campo Entrega |
| Documento de alcance | «este correo DEMO-001-R1, revisión R1, fecha 2026-11-17» | C1, campo Documento de alcance |
| Aceptación | «Acepto expresamente las cantidades, especificaciones, condiciones comerciales y alcance de esta revisión R1.»; «Elena Demo, 2026-11-17» | C1, párrafo Acepto y campo Nombre de aceptación |

Comprobación aritmética decimal a centavos: 12 × USD 150.00 = USD 1800.00. USD 1800.00 + USD 100.00 + USD 0.00 + USD 0.00 = USD 1900.00. Ambos resultados coinciden con los importes declarados; no se calculan tributos adicionales ni se convierten monedas. No fue necesaria conversión dimensional.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, pedido | satisfecho | C1, párrafo Expediente: DEMO-001 y etapa pedido explícitos. Identificador ficticio, sin atribución a ERP. |
| P02 | Sí, pedido | satisfecho | C1, Cliente / Contacto: Oficina Alfa Demo y compras@oficina-alfa.example. |
| P03 | Sí, pedido | satisfecho | C1, Proyecto y primer Entrega: uso corporativo y destino identificado en Panamá. |
| P04 | Sí, pedido | satisfecho | C1, Línea L1: identificador único, escritorio independiente, 12 unidades; cantidad positiva. |
| P05 | Sí, pedido | satisfecho | C1, Dimensiones, Material y Acabado: L x A x H 1200 x 600 x 750 mm; tablero melamínico de 18 mm; blanco mate. |
| P06 | Sí, pedido | satisfecho | C1, Ruta L1: fabricación explícita. |
| P07 | Sí, pedido | satisfecho | C1, párrafos USD y Transporte, campo Pago: moneda, precio, subtotal, cargos, impuestos, total y pago declarados; comprobación aritmética coincidente. |
| P08 | Sí, pedido | satisfecho | C1, segundo Entrega: fecha absoluta 2026-12-15 y exclusión expresa de instalación; no requiere hito de plazo relativo. |
| P09 | Sí, pedido | satisfecho | C1 identificado por remitente, fecha y asunto; conserva DEMO-001-R1 / R1 / 2026-11-17. El propio correo define el alcance y contiene aceptación explícita de R1 atribuida a Elena Demo y fechada 2026-11-17. No hay adjuntos referenciados. |
| P10 | Sí, pedido | satisfecho | C1, Acepto / Nombre de aceptación: cantidades, especificaciones, condiciones comerciales y alcance R1 aceptados expresamente, con identidad y fecha. No se verifica autoridad ni autenticidad. |
| F01 | No en etapa pedido | NA | C1 solicita revisar etapa pedido; el taller corresponde al control adicional de etapa fabricación. |
| F02 | No en etapa pedido | NA | C1 solicita pedido, sin revisión de fabricación solicitada; ficha/plano de fabricación no exigible todavía por este control. |
| F03 | No en etapa pedido | NA | C1 solicita pedido; aprobación técnica de plano/ficha corresponde a etapa fabricación. |
| F04 | No | NA | Etapa pedido; además C1, Ruta L1, declara «No se ajusta a un espacio existente», por lo que no activa la condición de medición de sitio. |
| F05 | No en etapa pedido | NA | C1 solicita pedido; plazo de fabricación es control adicional de etapa fabricación. La entrega de pedido se evalúa en P08. |
| I01 | No | NA | C1, Ruta L1: fabricación; no se declara importación. |
| I02 | No | NA | Única línea con ruta fabricación, sin ruta importación declarada en C1. |
| I03 | No | NA | Única línea con ruta fabricación, sin ruta importación declarada en C1. |
| I04 | No | NA | Única línea con ruta fabricación; los costos de pedido se evalúan en P07. |
| I05 | No | NA | No hay línea de importación declarada; C1 solicita etapa pedido. |
| I06 | No | NA | No hay ruta importación ni Incoterm utilizado en C1; no se inventa ninguno. |

## 6. Hallazgos

No se identifican faltantes obligatorios aplicables, contradicciones ni datos no legibles en las fuentes recibidas. No hay hallazgos abiertos que requieran corrección documental en esta etapa.

## 7. Preguntas y siguiente acción humana

No se requieren aclaraciones para completar la revisión documental de pedido bajo este perfil. Siguiente acción: someter el expediente y este informe a revisión humana. No se aprueba compra, fabricación, importación ni instalación.

## 8. Límites

Revisión exclusivamente documental de las fuentes enumeradas. No se comprobaron externamente identidades, autoridad de la persona que acepta, autenticidad, disponibilidad de materiales, factibilidad técnica ni cumplimiento legal. La aceptación se registra como evidencia declarada en el correo. El informe no sustituye revisión técnica ni certifica cumplimiento ISO; PEO-01 es el perfil de demostración aplicado. No se consultaron fuentes externas ni se ejecutaron acciones operativas.
