# Informe documental

## 1. Identificación

Expediente DEMO-003. Revisión de análisis 1, 17 de noviembre de 2026. Etapa: importación, antes del pedido al proveedor. Ruta L1: importación. Caso expresamente ficticio, solo prueba técnica. Skill `revisor-expedientes-mobiliario`, versión de instrucciones 1.0; perfil PEO-01 v1.0.

## 2. Fuentes

Recibido y leído: `pruebas/entradas/E2E-03-proforma.pdf`, una página, PROFORMA DEMO-PF-003 R1, fecha 2026-11-17, vigencia hasta 2026-12-01 inclusive. Vinculado expresamente a DEMO-003 y L1. Se abrió el PDF real con pypdf y se extrajo el texto de todas sus páginas, sin OCR ni comprobación externa. Texto original conservado al final.

No hay otros adjuntos referenciados por nombre ni archivos recibidos ilegibles. No se aportó aceptación del cliente ni evidencia adicional de la aprobación declarada. No se recibió revisión anterior de análisis.

## 3. Estado global

**PENDIENTE DE INFORMACIÓN**. La fuente permite identificar expediente, etapa y ruta. Faltan unidad dimensional, acabado definitivo, condiciones de pago y aceptación documental del cliente. No se ha comprobado contradicción aplicable: la frase genérica de aprobación no identifica al cliente ni resuelve su aceptación expresamente pendiente.

## 4. Datos normalizados

Todos los valores siguientes proceden de la página 1 de DEMO-PF-003 R1. Son afirmaciones de la fuente, sin comprobación externa.

| Campo | Original y valor registrado | Estado |
|---|---|---|
| Expediente / etapa | `Expediente: DEMO-003. Etapa solicitada: importación.` | aportado |
| Cliente / contacto | `Residencia Beta Demo`; `beta@cliente.example` | aportado |
| Proyecto / uso | `mobiliario residencial, sillas de comedor` | aportado |
| Destino | `Casa Demo B, Ciudad de Panamá, Panamá` | aportado |
| Proveedor / contacto | `Demo Furniture Export`; `ventas@exportador.example` | aportado |
| L1 identificación / descripción | `L1: silla modelo S-20` | aportado |
| L1 cantidad / unidad de conteo / ruta | `20 unidades; ruta importación` | aportado |
| L1 dimensiones | `Dimensiones L x A x H: 500 x 550 x 850.` Largo 500, ancho 550, alto 850; unidad: **NO APORTADO**. Sin conversión ni asignación de mm por contexto. | faltante (unidad) |
| L1 material | `estructura de acero y asiento de polipropileno` | aportado |
| L1 acabado | `por confirmar`; acabado definitivo: **NO APORTADO** | faltante |
| L1 precio unitario / subtotal | `USD 80.00` / `USD 1600.00` | aportado |
| Embalaje | `incluido` | aportado |
| Transporte internacional / local | `excluido` / `excluido`; importes: **NO APORTADO** | aportado (exclusiones); faltante (importes) |
| Tributos de importación | `excluidos`; importe: **NO APORTADO** | aportado (exclusión); faltante (importe) |
| Impuestos de esta proforma / otros cargos | `USD 0.00` / `USD 0.00` | aportado |
| Total proforma | `USD 1600.00. El total es de mercancía, no costo final puesto en destino.` | aportado |
| Costo final puesto en destino | **NO APORTADO**; no equivale al total de mercancía | faltante |
| Condiciones de pago | **NO APORTADO**. Solo consta `recepción del anticipo` como hito, sin monto/porcentaje ni condiciones del saldo. | faltante |
| País de despacho / entrega | `China` / `Panamá`. No se declara origen de fabricación. | aportado |
| Preparación | `30 días calendario desde recepción del anticipo` | aportado |
| Transporte | `estimado 35 días calendario desde despacho; no hay fecha firme de llegada` | aportado como estimación |
| Instalación | `No incluye instalación` | aportado |
| Incoterm | `Las partes no han usado Incoterm en esta proforma` | aportado (no utilizado) |
| Documento / revisión / fecha / vigencia | `DEMO-PF-003`, `R1`, `2026-11-17`, `hasta 2026-12-01 inclusive` | aportado |
| Revisión declarada aprobada | `Especificación y condiciones aprobadas: DEMO-PF-003 R1.` Sin identidad, fecha ni evidencia de aceptación del cliente. | aportado (declaración); faltante (evidencia) |
| Aceptación del cliente | `pendiente`; identidad, fecha y alcance aceptados: **NO APORTADO** | faltante |

Comprobación decimal a centavos: 20 × USD 80.00 = USD 1600.00 de subtotal. USD 1600.00 + USD 0.00 de impuestos de esta proforma + USD 0.00 de otros cargos = USD 1600.00, coincidente con el total declarado de mercancía. Embalaje incluido. No se suman costos excluidos como cero ni se calcula el costo final de importación. No se suman plazos para prometer una llegada.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de pedido | satisfecho | p. 1: DEMO-003 y etapa importación; identificador ficticio, sin atribución a ERP. |
| P02 | Sí | satisfecho | p. 1: Residencia Beta Demo y correo explícito. |
| P03 | Sí | satisfecho | p. 1: uso residencial y destino Casa Demo B, Ciudad de Panamá, Panamá. |
| P04 | Sí | satisfecho | p. 1: L1 única, silla S-20, 20 unidades. |
| P05 | Sí | faltante | p. 1: ejes y valores presentes, unidad omitida; acabado por confirmar. Material declarado. |
| P06 | Sí | satisfecho | p. 1: L1 ruta importación expresa. |
| P07 | Sí | faltante | p. 1: moneda, importes y exclusiones declarados, aritmética coincidente; condición de pago no aportada. Costo final en destino indeterminado por exclusiones sin importe. |
| P08 | Sí | satisfecho | p. 1: preparación 30 días desde anticipo y transporte estimado 35 desde despacho; instalación excluida. Se conservan hitos y carácter estimado, sin afirmar fecha firme. |
| P09 | Sí | faltante | p. 1: número, fecha, revisión, vigencia y relación con expediente/L1 presentes. Declaración de aprobación sin evidencia identificada; aceptación del cliente pendiente. |
| P10 | Sí | faltante | p. 1: aceptación pendiente; sin identidad, fecha ni alcance/revisión aceptados por el cliente. |
| F01 | No | NA | L1 expresamente de importación; ninguna línea de fabricación. |
| F02 | No | NA | Misma ruta expresa; no se exige ficha de fabricación. |
| F03 | No | NA | No hay fabricación declarada. |
| F04 | No | NA | No hay fabricación ni condición de ajuste a espacio existente. |
| F05 | No | NA | No hay fabricación; preparación de importación evaluada en I05. |
| I01 | Sí | satisfecho | p. 1: proveedor y proforma disponibles con número, fecha, R1 y vigencia expresa. |
| I02 | Sí | faltante | p. 1: L1/S-20 y 20 unidades en la propia proforma; material presente, dimensiones sin unidad y acabado pendiente impiden completar especificaciones. |
| I03 | Sí | satisfecho | p. 1: despacho China y entrega Panamá. No equivale a origen de fabricación. |
| I04 | Sí | faltante | p. 1: moneda/precios/total y alcance de costos explícitos; condición de pago ausente, aunque se mencione anticipo como hito. |
| I05 | Sí | satisfecho | p. 1: preparación 30 días calendario desde anticipo y transporte estimado 35 desde despacho. No se transforma estimación en compromiso de llegada. |
| I06 | No, condición no activada | NA | p. 1 declara que no se usó Incoterm. Costos revisados con I04. |

## 6. Hallazgos

| ID | Requisito | Valores/documentos y consecuencia | Acción requerida |
|---|---|---|---|
| H01 | P05, I02 | DEMO-PF-003 R1 p. 1: `500 x 550 x 850` sin unidad. No es posible fijar ni normalizar dimensiones físicas. | Aportar unidad para largo, ancho y alto, conservando ejes y valores en especificación identificada. |
| H02 | P05, I02 | DEMO-PF-003 R1 p. 1: acabado `por confirmar`. Especificación incompleta. | Definir acabado de L1 e identificar revisión que lo incorpora. |
| H03 | P07, I04 | DEMO-PF-003 R1 p. 1: anticipo solo como hito, sin condiciones de pago. | Aportar condición de pago, monto/porcentaje de anticipo y condiciones del saldo si corresponde. |
| H04 | P09, P10 | DEMO-PF-003 R1 p. 1: declaración genérica de aprobación; aceptación del cliente pendiente. No acredita quién aprobó ni cuándo, ni aceptación del cliente. | Aportar evidencia con identidad, fecha y alcance/revisión aceptados; aclarar a qué aprobación corresponde la frase genérica. Una revisión posterior no sustituye automáticamente R1 sin evidencia pertinente. |
| H05 | P07, I04: alcance de costos | DEMO-PF-003 R1 p. 1: USD 1600.00 solo mercancía; transportes y tributos excluidos sin importe. Costo final desconocido; exclusiones documentadas, sin contradicción con total. | Conservar exclusiones en revisión humana. Para determinar total puesto en destino, aportar costos y alcance; no tratar exclusiones como cero. |

## 7. Preguntas y siguiente acción humana

Solicitar en una sola respuesta documental:

1. ¿Qué unidad corresponde a largo 500, ancho 550 y alto 850 de L1, y cuál es el acabado definitivo?
2. ¿Cuáles son las condiciones de pago, incluido anticipo que inicia la preparación y, si corresponde, saldo?
3. ¿Quién aprobó DEMO-PF-003 R1 y cuándo? ¿Qué evidencia identifica al cliente, fecha y alcance/revisión aceptados? Su aceptación figura pendiente.
4. Para evaluar el costo final puesto en destino, ¿qué importes y alcance tendrán transportes y tributos excluidos? El total actual solo cubre mercancía.

Siguiente acción humana: completar especificación y condiciones, documentar aceptación y someter el expediente a nueva revisión conservando este resultado. No se aprueba compra, importación ni instalación. No se exigen documentos de embarque, aduana o recepción de una operación aún no iniciada.

## 8. Límites

Revisión exclusivamente documental. Datos, identidades, aprobación declarada y vigencia son afirmaciones del PDF. No se verificaron autenticidad, autoridad real, factibilidad técnica, cumplimiento legal, costos externos ni llegada. Sin consulta de red ni comprobación externa. Los controles pertenecen a PEO-01 v1.0; esta revisión no constituye certificación ni declaración de conformidad ISO. No hay revisión anterior aportada para comparar cambios.

## Evidencia de extracción propia

Método: Python/pypdf, apertura del PDF real mediante `PdfReader`, iteración por todas las páginas y `page.extract_text()`. Una página encontrada y leída. Sin OCR. La extracción textual no acredita diseño visual ni autenticidad.

Comando ejecutado (PowerShell, stdout UTF-8):

```powershell
$env:PYTHONIOENCODING='utf-8'; @'
from pypdf import PdfReader
from pathlib import Path
import hashlib,json
p=Path('pruebas/entradas/E2E-03-proforma.pdf')
r=PdfReader(p)
print('PAGINAS:',len(r.pages))
for i,page in enumerate(r.pages,1):
 print(f'--- PAGINA {i} ---')
 print(page.extract_text())
for f in ['SKILL.md','PERFIL-EXPEDIENTE.md','pruebas/entradas/E2E-03-proforma.pdf']:
 print(json.dumps({'fuente':f,'sha256':hashlib.sha256(Path(f).read_bytes()).hexdigest()},ensure_ascii=False))
'@ | & 'C:\Program Files\WindowsApps\OpenAI.CodexPrimaryRuntime.v26-1112-737-0_26.1112.737.0_x64__3k8sg7r9htsxt\dependencies\python\python.exe' -
```

Texto original extraído, página 1 (transcripción automática, no comprobación externa):

```text
FICTICIO - SOLO PRUEBA TECNICA | Página 1
 FICTICIO — SOLO PRUEBA TÉCNICA
PROFORMA DEMO-PF-003 | R1 | Fecha: 2026-11-17
Vigencia: hasta 2026-12-01 inclusive.
Expediente: DEMO-003. Etapa solicitada: importación.
Cliente: Residencia Beta Demo. Contacto: beta@cliente.example.
Proyecto: mobiliario residencial, sillas de comedor.
Destino: Casa Demo B, Ciudad de Panamá, Panamá.
Proveedor: Demo Furniture Export. Contacto: ventas@exportador.example.
L1: silla modelo S-20; 20 unidades; ruta importación.
Dimensiones L x A x H: 500 x 550 x 850.
Material: estructura de acero y asiento de polipropileno.
Acabado: por confirmar.
Precio unitario: USD 80.00. Subtotal: USD 1600.00.
Embalaje: incluido. Transporte internacional: excluido.
Transporte local: excluido. Tributos de importación: excluidos.
Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00.
Total proforma: USD 1600.00. El total es de mercancía,
no costo final puesto en destino.
País de despacho: China. País de entrega: Panamá.
Preparación: 30 días calendario desde recepción del anticipo.
Transporte: estimado 35 días calendario desde despacho;
no hay fecha firme de llegada. No incluye instalación.
Las partes no han usado Incoterm en esta proforma.
Especificación y condiciones aprobadas: DEMO-PF-003 R1.
Aceptación del cliente: pendiente.

```

Incidencia de elaboración: un primer comando extenso para escribir los resultados terminó con código 1 y sin salida; se comprobó que la carpeta de resultados aún no existía. Se escribieron después los archivos con apply_patch y un comando más corto. No afectó la lectura de las fuentes.
