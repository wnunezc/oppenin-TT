# Informe documental — DEMO-002

## 1. Identificación

Expediente declarado: DEMO-002. Revisión de análisis: 1 de esta sesión independiente; no se recibió informe anterior. Etapa solicitada: importación, antes del pedido al proveedor. Ruta de L1: importación. Perfil aplicado: PEO-01 v1.1; skill 1.1. Documento expresamente ficticio: «FICTICIO — SOLO PRUEBA TÉCNICA». Sus fechas se conservan como datos declarados, separadas de la hora real del análisis.

## 2. Fuentes

- Recibido y abierto: `D:\OpsZone\DevWorkspace\Projects\Tech-Test\Oppenin\pruebas\entradas\E2E-02-proforma.pdf`, una página, proforma DEMO-PF-002, R1, fecha 2026-11-17, vigencia hasta 2026-12-01 inclusive. Relaciona expresamente DEMO-002 y L1.
- Reglas leídas íntegramente: `SKILL.md` y `PERFIL-EXPEDIENTE.md` de la raíz autorizada.
- Método: apertura propia con pypdf e iteración de todas las páginas (1 de 1); extracción textual conservada en `extraccion-propia.txt`. La extracción contiene los campos y la constancia de aceptación legibles; no fue necesario renderizado ni OCR. La consola inicial mostró caracteres dañados por codificación; se releyó la extracción UTF-8 correctamente, sin alterar el documento ni reconstruir texto.
- No se recibieron correos, informes anteriores ni otras fichas. No hay adjuntos referenciados ausentes ni archivos esenciales ilegibles identificados en lo recibido.
- Todas las evidencias documentales indicadas a continuación proceden de la página 1 de esta proforma. Los hashes de bytes originales se conservan en `fuentes-sha256.json`.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA**.

Los requisitos obligatorios aplicables están documentados y no se identificaron contradicciones. La constancia de Luis Demo, con identidad, fecha y referencia a DEMO-PF-002 R1, aporta evidencia documental de aceptación de las líneas y condiciones y de aprobación de esa versión. Este estado no autoriza la operación.

## 4. Datos normalizados

Se mantienen los valores originales; no se convirtieron unidades ni monedas.

| Campo | Valor original / normalizado | Procedencia |
|---|---|---|
| Expediente y etapa | «DEMO-002. Etapa solicitada: importación.» | p. 1, expediente |
| Cliente y contacto | «Residencia Beta Demo»; «beta@cliente.example» | p. 1, cliente |
| Proyecto y uso | «mobiliario residencial, sillas de comedor» | p. 1, proyecto |
| Destino | «Casa Demo B, Ciudad de Panamá, Panamá» | p. 1, destino |
| Proveedor y contacto | «Demo Furniture Export»; «ventas@exportador.example» | p. 1, proveedor |
| Línea, producto, cantidad y ruta | «L1: silla modelo S-20; 20 unidades; ruta importación.» | p. 1, L1 |
| Dimensiones y ejes | «Dimensiones L x A x H: 500 x 550 x 850 mm.»; largo 500 mm, ancho 550 mm, alto 850 mm | p. 1, dimensiones |
| Material | «estructura de acero y asiento de polipropileno» | p. 1, material |
| Acabado | «negro mate» | p. 1, acabado |
| Moneda y precio unitario | «USD 80.00» | p. 1, precio unitario |
| Subtotal | «USD 1600.00» | p. 1, subtotal |
| Alcance de costos | «Embalaje: incluido. Transporte internacional: excluido. Transporte local: excluido. Tributos de importación: excluidos.» | p. 1, costos |
| Impuestos de proforma y otros cargos | «USD 0.00» y «USD 0.00» | p. 1, impuestos / otros cargos |
| Total y alcance | «Total proforma: USD 1600.00. El total es de mercancía, no costo final puesto en destino.» | p. 1, total |
| Pago | «30 % al confirmar pedido y 70 % antes del despacho» | p. 1, pago |
| Países | «País de despacho: China. País de entrega: Panamá.» | p. 1, países |
| Preparación | «30 días calendario desde recepción del anticipo» | p. 1, preparación |
| Transporte | «estimado 35 días calendario desde despacho; no hay fecha firme de llegada» | p. 1, transporte |
| Instalación | «No incluye instalación.» | p. 1, servicio |
| Incoterm | «Las partes no han usado Incoterm en esta proforma.» | p. 1, Incoterm |
| Documento controlado | «PROFORMA DEMO-PF-002», «R1», «Fecha: 2026-11-17»; «Vigencia: hasta 2026-12-01 inclusive.» | p. 1, encabezado y vigencia |
| Aprobación y aceptación | «Especificación y condiciones aprobadas: DEMO-PF-002 R1.» y «Constancia ficticia de aceptación del cliente: Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente las líneas y condiciones de DEMO-PF-002 R1.» | p. 1, constancia final |
| Costo final puesto en destino | NO APORTADO; la fuente lo distingue expresamente del total de mercancía y excluye transporte y tributos | p. 1, costos y total |

Comprobación decimal de importes declarados: 20 × USD 80.00 = USD 1600.00; USD 1600.00 + USD 0.00 (impuestos de esta proforma) + USD 0.00 (otros cargos) = USD 1600.00. Coinciden a centavos con subtotal y total declarados. Las exclusiones de transporte y tributos no se interpretan como costos finales de cero. No se calculó un costo final ni una llegada sumando estimaciones.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base | satisfecho | p. 1: DEMO-002 y etapa importación explícitos; identificador de demostración, sin atribución a ERP. |
| P02 | Sí, base | satisfecho | p. 1, cliente: Residencia Beta Demo y beta@cliente.example. |
| P03 | Sí, base | satisfecho | p. 1, proyecto / destino: mobiliario residencial, sillas de comedor; Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí, L1 | satisfecho | p. 1, L1: identificador único, silla modelo S-20, 20 unidades. |
| P05 | Sí, L1 | satisfecho | p. 1: L x A x H 500 x 550 x 850 mm; estructura de acero y asiento de polipropileno; negro mate. |
| P06 | Sí, L1 | satisfecho | p. 1, L1: «ruta importación». |
| P07 | Sí, base | satisfecho | p. 1: USD 80.00 unitario; subtotal/total USD 1600.00; impuestos y otros cargos USD 0.00; embalaje incluido; exclusiones expresas; pago 30 % / 70 % con hitos. Aritmética concordante. |
| P08 | Sí, base | satisfecho | p. 1: preparación 30 días desde anticipo; transporte estimado 35 días desde despacho; destino identificado; instalación excluida. No se exige llegada firme adicional con estos hitos. |
| P09 | Sí, documento controlado | satisfecho | p. 1: DEMO-PF-002 R1, 2026-11-17, vinculado a DEMO-002 y L1. La constancia de Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente líneas y condiciones de esa versión. La conclusión no se basa únicamente en la frase genérica de aprobación. |
| P10 | Sí, base | satisfecho | p. 1, constancia ficticia del cliente: Luis Demo, contacto y fecha 2026-11-17; acepta expresamente líneas y condiciones de DEMO-PF-002 R1. Autenticidad y autoridad no comprobadas. |
| F01 | No | NA | p. 1, L1: solo ruta importación, sin fabricación declarada. |
| F02 | No | NA | p. 1, L1: solo ruta importación; no corresponde exigir plano/ficha de fabricación. |
| F03 | No | NA | p. 1, L1: solo ruta importación; no se activa revisión técnica de fabricación. |
| F04 | No | NA | p. 1: L1 tiene ruta importación y no declara fabricación ajustada a espacio existente. |
| F05 | No | NA | p. 1, L1: solo ruta importación; no corresponde plazo de fabricación. |
| I01 | Sí, importación | satisfecho | p. 1: Demo Furniture Export; proforma DEMO-PF-002, fecha 2026-11-17, R1, vigencia hasta 2026-12-01 inclusive. |
| I02 | Sí, L1 | satisfecho | p. 1: la propia proforma vincula L1/S-20, 20 unidades, dimensiones con mm, material y negro mate; la aceptación refiere sus líneas. No hay fuente incompatible aportada. |
| I03 | Sí, importación | satisfecho | p. 1: despacho China; entrega Panamá, Casa Demo B, Ciudad de Panamá. No se deduce país de fabricación. |
| I04 | Sí, importación | satisfecho | p. 1: moneda, pago, precio/total y alcance expreso; embalaje incluido, transportes y tributos excluidos. Total de mercancía identificado; costo final no cuantificado. |
| I05 | Sí, importación | satisfecho | p. 1: preparación 30 días calendario desde anticipo; transporte estimado 35 días calendario desde despacho. No hay llegada firme, sin que se requiera con los plazos e hitos aportados. |
| I06 | No, condición no activada | NA | p. 1: declara expresamente que las partes no han usado Incoterm. Alcance de costos revisado en I04. |

## 6. Hallazgos

No se identifican faltantes obligatorios ni contradicciones documentales aplicables en la fuente recibida. No hay hallazgos bloqueantes abiertos.

Observación de alcance vinculada a P07/I04: los transportes internacional y local y los tributos de importación están excluidos; el total USD 1600.00 corresponde a mercancía y el costo final puesto en destino no está cuantificado. Las exclusiones satisfacen la declaración de alcance del perfil y no generan una exigencia adicional de importes en esta revisión.

## 7. Preguntas y siguiente acción humana

No se requieren aclaraciones para cerrar los controles documentales aplicables de este expediente. Siguiente acción: someter DEMO-PF-002 R1 y este informe a revisión humana antes del pedido al proveedor, considerando la vigencia declarada y el alcance de costos y plazos documentado. No se aprueba compra ni importación.

## 8. Límites

Revisión exclusivamente documental de la proforma ficticia recibida. No se verificaron externamente datos, identidad, autenticidad, autoridad, factibilidad técnica, calidad de materiales, capacidad del proveedor ni cumplimiento legal o aduanero. No constituye certificación, evaluación de conformidad ISO ni autorización operativa. PEO-01 es un perfil de demostración; no se atribuyen sus campos a una norma ISO. No se consultó red ni fuentes distintas de las autorizadas. No se emite veredicto de prueba.
