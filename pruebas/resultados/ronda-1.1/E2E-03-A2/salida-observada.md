# Informe documental

## 1. Identificación

Expediente **DEMO-003**, revisión de análisis **1**, etapa declarada **importación**, antes del pedido al proveedor. Ruta de L1: importación. Perfil aplicado: **PEO-01 v1.1**, skill 1.1. Caso expresamente **FICTICIO — SOLO PRUEBA TÉCNICA**. Las fechas del expediente se conservan como datos declarados. No se aportó una revisión anterior del informe.

## 2. Fuentes

Se recibió y abrió `D:\OpsZone\DevWorkspace\Projects\Tech-Test\Oppenin\pruebas\entradas\E2E-03-proforma.pdf`: una página, PROFORMA DEMO-PF-003, R1, fecha 2026-11-17, vigencia hasta 2026-12-01 inclusive. La revisión se rige por SKILL.md y PERFIL-EXPEDIENTE.md leídos íntegramente.

Lectura propia mediante pypdf, iterando su única página. La extracción presentó caracteres de reemplazo en palabras acentuadas; se renderizó localmente la página con `pdftoppm -png -r 120` y se leyó íntegramente mediante visión directa. El renderizado mostró todo el contenido legible. Se conservaron extracción y PNG propios. Poppler emitió advertencias de fuentes Symbol y ArialUnicode; no impidieron la lectura de la página. Las transcripciones siguientes proceden de la lectura visual cuando difieren los acentos de la extracción; no son comprobaciones externas.

No se recibieron correos, fichas adicionales ni constancia atribuida de aprobación o aceptación del cliente. No hay otros adjuntos expresamente referenciados por nombre. Ningún archivo recibido quedó ilegible.

## 3. Estado global

**PENDIENTE DE INFORMACIÓN**. El expediente puede evaluarse y no se comprobó una contradicción, pero faltan la unidad de dimensiones, el acabado definitivo, la condición de pago suficientemente declarada, la evidencia atribuida de aprobación de la proforma R1 y la aceptación del cliente. La frase genérica de aprobación no acredita P09.

## 4. Datos normalizados

Todos los datos siguientes proceden de la página 1 de DEMO-PF-003 R1; se conserva la redacción original entre comillas.

| Campo o línea | Valor original y procedencia, página 1 | Estado documental |
|---|---|---|
| Expediente y etapa | “Expediente: DEMO-003. Etapa solicitada: importación.” | aportado |
| Cliente/contacto | “Cliente: Residencia Beta Demo. Contacto: beta@cliente.example.” | aportado |
| Proyecto/uso | “Proyecto: mobiliario residencial, sillas de comedor.” | aportado |
| Destino | “Destino: Casa Demo B, Ciudad de Panamá, Panamá.” | aportado |
| Proveedor/contacto | “Proveedor: Demo Furniture Export. Contacto: ventas@exportador.example.” | aportado |
| L1 producto/cantidad/ruta | “L1: silla modelo S-20; 20 unidades; ruta importación.” | aportado |
| L1 dimensiones | “Dimensiones L x A x H: 500 x 550 x 850.” Ejes rotulados L, A y H; unidad: **NO APORTADO**. Se conservan 500, 550 y 850 sin conversión. | faltante: unidad |
| L1 material | “Material: estructura de acero y asiento de polipropileno.” | aportado |
| L1 acabado | “Acabado: por confirmar.” Acabado definido: **NO APORTADO**. | faltante |
| Moneda/unitario/subtotal | “Precio unitario: USD 80.00. Subtotal: USD 1600.00.” | aportado |
| Embalaje y transporte | “Embalaje: incluido. Transporte internacional: excluido.” “Transporte local: excluido. Tributos de importación: excluidos.” | aportado como alcance de costos |
| Impuestos/otros cargos | “Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00.” | aportado |
| Total | “Total proforma: USD 1600.00. El total es de mercancía, no costo final puesto en destino.” | aportado; costo final en destino no cuantificado |
| Pago | Solo se menciona “recepción del anticipo” como hito. Condición de pago: **NO APORTADO**; no se indica importe/porcentaje del anticipo ni condiciones del saldo. | faltante |
| Países | “País de despacho: China. País de entrega: Panamá.” No se atribuye origen de fabricación. | aportado |
| Preparación | “Preparación: 30 días calendario desde recepción del anticipo.” | aportado |
| Transporte | “Transporte: estimado 35 días calendario desde despacho; no hay fecha firme de llegada.” | aportado; estimación, no compromiso de llegada |
| Instalación | “No incluye instalación.” | aportado |
| Incoterm | “Las partes no han usado Incoterm en esta proforma.” | aportado; control condicional no activado |
| Documento | “PROFORMA DEMO-PF-003 \| R1 \| Fecha: 2026-11-17”. “Vigencia: hasta 2026-12-01 inclusive.” | aportado |
| Aprobación | “Especificación y condiciones aprobadas: DEMO-PF-003 R1.” Identidad y fecha de quien aprueba: **NO APORTADO**. | faltante: evidencia atribuida |
| Aceptación cliente | “Aceptación del cliente: pendiente.” | faltante |

Comprobación aritmética de apoyo con importes decimales: **20 × USD 80.00 = USD 1600.00**; **USD 1600.00 + USD 0.00 de impuestos declarados + USD 0.00 de otros cargos = USD 1600.00**. Coincide con el total de mercancía. Las exclusiones de transporte y tributos no equivalen a costo cero puesto en destino; no se requiere cuantificarlas para evaluar el total de mercancía declarado.

## 5. Checklist

En esta tabla, “p. 1” remite al único PDF recibido, DEMO-PF-003 R1.

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de pedido | satisfecho | p. 1, expediente DEMO-003 y etapa importación explícitos; identificador ficticio. |
| P02 | Sí | satisfecho | p. 1, Residencia Beta Demo y beta@cliente.example. |
| P03 | Sí | satisfecho | p. 1, mobiliario residencial/sillas de comedor; Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí | satisfecho | p. 1, L1, silla S-20, 20 unidades; identificador único y cantidad positiva. |
| P05 | Sí | faltante | p. 1, L x A x H 500 x 550 x 850 sin unidad; material aportado; acabado “por confirmar”. |
| P06 | Sí | satisfecho | p. 1, L1 declara ruta importación. |
| P07 | Sí | faltante | p. 1, moneda, unitario, subtotal, cargos y total coherentes; no se declara condición de pago. La referencia al anticipo como hito no determina esa condición. |
| P08 | Sí | satisfecho | p. 1, preparación 30 días desde anticipo y transporte estimado 35 días desde despacho; instalación expresamente excluida. No se transforma en llegada firme. |
| P09 | Sí | faltante | p. 1, identificador DEMO-PF-003, R1, fecha y relación con DEMO-003/L1 disponibles; frase genérica “Especificación y condiciones aprobadas” sin identidad ni fecha de aprobación. |
| P10 | Sí | faltante | p. 1, “Aceptación del cliente: pendiente.” No hay alcance/revisión aceptados con identidad y fecha. |
| F01 | No | NA | p. 1, única línea L1 con ruta exclusivamente importación; no fabricación declarada. |
| F02 | No | NA | p. 1, única línea de importación; no ruta de fabricación que active plano/ficha de fabricación. |
| F03 | No | NA | p. 1, L1 importación; no se activa aprobación técnica de fabricación. |
| F04 | No | NA | p. 1, L1 importación; tampoco se declara fabricación ajustada a espacio existente. |
| F05 | No | NA | p. 1, L1 importación; no plazo de fabricación exigible en esta ruta. |
| I01 | Sí, importación L1 | satisfecho | p. 1, Demo Furniture Export; proforma disponible DEMO-PF-003, 2026-11-17, R1, vigencia hasta 2026-12-01 inclusive. |
| I02 | Sí | faltante | p. 1, L1/S-20 y 20 unidades identificados; unidad de dimensiones ausente y acabado por confirmar impiden correspondencia completa de especificación. |
| I03 | Sí | satisfecho | p. 1, China como despacho y Panamá como entrega; destino identificado. |
| I04 | Sí | faltante | p. 1, USD, precio/total y alcance de costos explícitos; falta condición de pago, aunque se menciona anticipo. Exclusiones de transporte y tributos declaradas. |
| I05 | Sí | satisfecho | p. 1, 30 días calendario desde recepción de anticipo y estimado 35 días desde despacho. No se exige llegada firme adicional. |
| I06 | No, condición no activada | NA | p. 1 declara expresamente que las partes no han usado Incoterm; alcance de costos evaluado en I04. |

## 6. Hallazgos

| Hallazgo | Requisitos | Valores/documentos involucrados | Consecuencia documental | Acción requerida |
|---|---|---|---|---|
| H01 | P05, I02 | p. 1, “Dimensiones L x A x H: 500 x 550 x 850.” | No permite establecer dimensiones con unidad ni compararlas de forma exacta. | Aportar unidad explícita para las dimensiones L1, manteniendo los ejes y valores o documentando su corrección en una versión identificada. |
| H02 | P05, I02 | p. 1, “Acabado: por confirmar.” | La especificación de L1 no está cerrada. | Definir el acabado y aportar documento identificado con fecha y revisión que lo incorpore. |
| H03 | P07, I04 | p. 1, solo referencia a recepción del anticipo. | No se conoce la condición comercial de pago; el hito temporal no la completa. | Aportar condición de pago, incluidos anticipo y saldo aplicables, vinculada a la proforma correspondiente. |
| H04 | P09 | p. 1, aprobación genérica de DEMO-PF-003 R1 sin identidad ni fecha. | La versión identificada no cuenta con evidencia explícita atribuida de aprobación. | Aportar constancia de aprobación con identidad, fecha y referencia exacta al documento/revisión; si se modifica el alcance, identificar la versión finalmente aprobada. |
| H05 | P10 | p. 1, aceptación del cliente pendiente. | No consta aceptación explícita del alcance/revisión por el cliente. | Aportar aceptación vinculada al alcance y revisión finales, con identidad y fecha. |

No hay valores incompatibles comprobados entre fuentes; solo se recibió una proforma. El total de mercancía es coherente aritméticamente. El costo final en destino no está cuantificado y no se ha solicitado calcularlo.

## 7. Preguntas y siguiente acción humana

1. H01: ¿Cuál es la unidad explícita de los valores L x A x H de L1, 500 x 550 x 850?
2. H02: ¿Qué acabado definitivo corresponde a L1 y qué documento/revisión lo recoge?
3. H03: ¿Cuáles son las condiciones de pago de la proforma, incluidos el anticipo y el saldo aplicables?
4. H04: ¿Puede aportarse la evidencia de aprobación de la versión aplicable de la proforma, con identidad, fecha y referencia exacta al documento/revisión?
5. H05: ¿Puede aportarse la aceptación del cliente del alcance y revisión finales, con identidad y fecha?

La siguiente acción humana es aportar estas precisiones y evidencias para una nueva revisión documental, conservando este informe. Esta revisión no aprueba compra ni importación.

## 8. Límites

Revisión exclusivamente documental del PDF efectivamente recibido, bajo PEO-01 v1.1. No se verificaron externamente identidad, autoridad, autenticidad, datos empresariales, calidad de materiales, factibilidad, cumplimiento técnico, aduanero o legal. No se realizó cálculo de tributos, conversión de moneda, inferencia dimensional ni promesa de llegada. Los controles corresponden al perfil de demostración y no acreditan certificación o conformidad ISO. No se utilizaron red, correo, plugins, subagentes ni servicios externos para esta revisión.