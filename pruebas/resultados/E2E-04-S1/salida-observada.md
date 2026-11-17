# Informe documental

## 1. Identificación
DEMO-004, revisión de análisis 1. Etapa importación, antes del pedido al proveedor. L1: importación. Perfil PEO-01 v1.0; skill revisor-expedientes-mobiliario v1.0. Ficticio, solo prueba técnica. Sin revisión de análisis anterior aportada.

## 2. Fuentes
Correo E2E-04-correo.md, asunto «Datos para expediente DEMO-004», fecha 2026-11-18 10:00 UTC-05:00, remitente beta@cliente.example, firmado Luis Demo. Sin revisión declarada. Párrafo 1: expediente/etapa; párrafo 2: cantidad/acabado; párrafo 3: sustitución/total. Fecha posterior al día real de análisis (2026-11-17), conservada como dato sin autenticar.

PDF E2E-04-proforma.pdf, una página íntegramente abierta y extraída con pypdf: DEMO-PF-004 R1, fecha 2026-11-17, vigencia hasta 2026-12-01 inclusive. No hay archivos ilegibles ni otros adjuntos específicos mencionados. No se recibió revisión sustitutiva ni aceptación de los cambios.

## 3. Estado global
**CONFLICTO DOCUMENTAL**. R1 aceptada declara 20 unidades y negro mate; correo solicita 24 sillas y blanco mate sin confirmar sustitución ni nuevo total. La fecha más reciente no acredita sustitución aceptada.

## 4. Datos normalizados
Todos son datos aportados, sin comprobación externa. Las referencias PDF siguientes corresponden a página 1 y campo indicado.

| Campo | Original / normalizado | Estado; fuente |
|---|---|---|
| Expediente/etapa | DEMO-004; importación | aportado; PDF Expediente y correo párrafo 1 |
| Cliente/contacto | Residencia Beta Demo; beta@cliente.example | aportado; PDF Cliente |
| Proyecto/uso/destino | mobiliario residencial, sillas de comedor; Casa Demo B, Ciudad de Panamá, Panamá | aportado; PDF Proyecto/Destino |
| L1 producto | silla modelo S-20 | aportado; PDF L1; correo no declara cambio de modelo |
| Cantidad/unidad | PDF «20 unidades»; correo «24 sillas» | contradictorio; PDF L1/correo párrafo 2 |
| Dimensiones | «L x A x H: 500 x 550 x 850 mm»; largo 500 mm, ancho 550 mm, alto 850 mm | aportado; PDF Dimensiones |
| Material | estructura de acero y asiento de polipropileno | aportado; PDF Material |
| Acabado | PDF «negro mate»; correo «blanco mate» | contradictorio; PDF Acabado/correo párrafo 2 |
| Ruta | importación | aportado; PDF L1 |
| Proveedor/contacto | Demo Furniture Export; ventas@exportador.example | aportado; PDF Proveedor |
| Precio R1 | USD 80.00 unitario; subtotal USD 1600.00 | aportado; PDF Precio |
| Costos R1 | embalaje incluido; transporte internacional/local y tributos de importación excluidos | aportado; PDF costos |
| Impuestos/otros cargos R1 | USD 0.00 / USD 0.00 | aportado; PDF Impuestos |
| Total R1 | USD 1600.00, mercancía; no costo final puesto en destino | aportado; PDF Total |
| Nuevo total/costo final destino | NO APORTADO / NO APORTADO | faltante; correo párrafo 3 y exclusiones PDF |
| Pago | 30 % al confirmar pedido; 70 % antes del despacho | aportado; PDF Pago |
| País despacho/entrega | China / Panamá | aportado; PDF países; no acredita origen de fabricación |
| Preparación | 30 días calendario desde recepción del anticipo | aportado; PDF Preparación |
| Transporte | estimado 35 días calendario desde despacho; sin fecha firme de llegada | aportado; PDF Transporte |
| Instalación | no incluye | aportado; PDF instalación |
| Incoterm | «Las partes no han usado Incoterm en esta proforma» | aportado; PDF Incoterm |
| Revisión aceptada | DEMO-PF-004 R1; Luis Demo, beta@cliente.example, 2026-11-17, acepta expresamente líneas y condiciones | aportado; PDF Especificación/Constancia |
| Sustitución y aceptación de cambios | NO APORTADO | faltante; correo párrafo 3 |

Aritmética decimal R1: 20 × USD 80.00 = USD 1600.00; USD 1600.00 + USD 0.00 impuestos + USD 0.00 otros cargos = USD 1600.00. Embalaje incluido. Esto no valida un nuevo total para 24 unidades ni convierte costos excluidos en cero. No se suman plazos estimados para prometer llegada.

## 5. Checklist
| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí | satisfecho | PDF Expediente/correo párrafo 1: identificador ficticio y etapa |
| P02 | Sí | satisfecho | PDF Cliente y contacto |
| P03 | Sí | satisfecho | PDF Proyecto/Destino residencial identificado |
| P04 | Sí, L1 | contradictorio | 20 unidades PDF frente a 24 sillas correo |
| P05 | Sí, L1 | contradictorio | Ejes, dimensiones y material aportados; negro mate frente a blanco mate |
| P06 | Sí, L1 | satisfecho | Ruta importación explícita |
| P07 | Sí | faltante | R1 aritméticamente coherente; nuevo total no confirmado; exclusiones no cuantificadas para costo final |
| P08 | Sí | satisfecho | Plazos con hitos, destino y exclusión de instalación; transporte expresamente estimado |
| P09 | Sí | contradictorio | R1 identificada, fechada y aceptada; correo incompatible sin sustitución confirmada; sin revisión propia declarada |
| P10 | Sí | faltante | Aceptación explícita R1; falta aceptación del alcance cambiado y su revisión |
| F01 | No | NA | L1 solo importación, no fabricación |
| F02 | No | NA | L1 solo importación, no fabricación |
| F03 | No | NA | L1 solo importación, no fabricación |
| F04 | No | NA | L1 solo importación; sin fabricación ajustada a espacio existente declarada |
| F05 | No | NA | L1 solo importación, no fabricación |
| I01 | Sí | satisfecho | PDF proveedor, número, fecha, R1 y vigencia explícita |
| I02 | Sí | contradictorio | L1 S-20 disponible; cantidad/acabado incompatibles entre fuentes |
| I03 | Sí | satisfecho | Despacho China, entrega Panamá |
| I04 | Sí | faltante | R1 declara moneda, pago y alcance de costos; total actualizado no aportado |
| I05 | Sí | satisfecho | Preparación desde anticipo y transporte desde despacho; no exige además llegada firme |
| I06 | Condición no activada | NA | PDF declara ausencia de Incoterm; costos evaluados con I04 |

## 6. Hallazgos
| ID | Requisitos | Evidencia y consecuencia | Acción requerida |
|---|---|---|---|
| H01 | P04/I02 | PDF p.1 L1:20; correo párrafo 2:24. Cantidad no unificada | Confirmar cantidad final y documentarla en revisión identificada |
| H02 | P05/I02 | PDF p.1 Acabado:negro mate; correo párrafo 2:blanco mate. Especificación incompatible | Confirmar acabado y reflejarlo en revisión aplicable |
| H03 | P07/I04 | PDF USD 1600.00 para 20; correo párrafo 3 no confirma nuevo total | Aportar condiciones comerciales completas del alcance final, con precio, subtotal, cargos/impuestos, total, pago y alcance de exclusiones/costos pendientes |
| H04 | P09/P10 | R1 aceptada; correo no confirma sustitución | Identificar versión vigente, documentar sustitución si corresponde y aceptación explícita de revisión y cambios con identidad/fecha |
| H05 | P09 | Correo fechado 2026-11-18, análisis 2026-11-17; dato no autenticado | Aclarar si fecha ficticia intencional o requiere corrección documental; no elegir automáticamente una versión por fecha |

## 7. Preguntas y siguiente acción humana
1. ¿Cantidad final 20 o 24 unidades, acabado negro mate o blanco mate?
2. ¿Qué proforma/revisión queda vigente y qué evidencia confirma sustitución, si corresponde? Aportar condiciones comerciales completas de esa revisión.
3. ¿Qué evidencia con identidad y fecha acepta expresamente la revisión y sus cambios?
4. ¿La fecha futura del correo es intencional en esta ficción o debe corregirse?

Conciliar cantidad, acabado, revisión y condiciones comerciales; aportar aceptación final y realizar nueva revisión documental. Este informe no aprueba operaciones. No se exigen documentos aduaneros/de embarque ya emitidos para esta etapa previa.

## 8. Límites
Revisión exclusivamente documental. Sin comprobación externa de autenticidad, autoridad, calidad, factibilidad o cumplimiento técnico/legal/aduanero. No hay certificación ISO; PEO-01 es un perfil de demostración. No se consultó texto normativo ni referencias externas. La aceptación ficticia documentada no acredita firma legal ni autoridad real. No se ejecutaron operaciones externas.

## Evidencia de extracción propia
Lectura completa de skill, perfil y correo mediante PowerShell Get-Content -Raw -Encoding UTF8. PDF real abierto mediante Python/pypdf y extracción textual de todas sus páginas, 1 de 1; sin OCR. El comando y el texto íntegro se incorporan a continuación.

```text
$env:PYTHONIOENCODING='utf-8'; Python suministrado ejecutado por entrada estándar:
from pypdf import PdfReader
p='pruebas/entradas/E2E-04-proforma.pdf'
r=PdfReader(p)
print('PAGINAS:',len(r.pages))
for i,page in enumerate(r.pages,1):
 print(f'\n--- PAGINA {i} ---\n{page.extract_text()}')
```

Texto original extraído:
```text
--- PAGINA 1 ---
FICTICIO - SOLO PRUEBA TECNICA | Página 1
 FICTICIO — SOLO PRUEBA TÉCNICA
PROFORMA DEMO-PF-004 | R1 | Fecha: 2026-11-17
Vigencia: hasta 2026-12-01 inclusive.
Expediente: DEMO-004. Etapa solicitada: importación.
Cliente: Residencia Beta Demo. Contacto: beta@cliente.example.
Proyecto: mobiliario residencial, sillas de comedor.
Destino: Casa Demo B, Ciudad de Panamá, Panamá.
Proveedor: Demo Furniture Export. Contacto: ventas@exportador.example.
L1: silla modelo S-20; 20 unidades; ruta importación.
Dimensiones L x A x H: 500 x 550 x 850 mm.
Material: estructura de acero y asiento de polipropileno.
Acabado: negro mate.
Precio unitario: USD 80.00. Subtotal: USD 1600.00.
Embalaje: incluido. Transporte internacional: excluido.
Transporte local: excluido. Tributos de importación: excluidos.
Impuestos de esta proforma: USD 0.00. Otros cargos: USD 0.00.
Total proforma: USD 1600.00. El total es de mercancía,
no costo final puesto en destino.
Pago: 30 % al confirmar pedido y 70 % antes del despacho.
País de despacho: China. País de entrega: Panamá.
Preparación: 30 días calendario desde recepción del anticipo.
Transporte: estimado 35 días calendario desde despacho;
no hay fecha firme de llegada. No incluye instalación.
Las partes no han usado Incoterm en esta proforma.
Especificación y condiciones aprobadas: DEMO-PF-004 R1.
Constancia ficticia de aceptación del cliente:
Luis Demo, beta@cliente.example, 2026-11-17,
acepta expresamente las líneas y condiciones de DEMO-PF-004 R1.

```
