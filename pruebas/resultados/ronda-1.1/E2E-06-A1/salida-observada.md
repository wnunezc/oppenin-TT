# Informe documental — DEMO-005

## 1. Identificación

Expediente DEMO-005, FICTICIO — SOLO PRUEBA TÉCNICA. Revisión de análisis 2, nueva e independiente sobre el antecedente recibido. Etapa: fabricación, antes de iniciar la operación. L1 tiene ruta de fabricación. Skill revisor-expedientes-mobiliario 1.1 y perfil PEO-01 v1.1. Las fechas de los documentos se conservan como fechas declaradas del expediente ficticio; el inicio real del análisis se conserva separadamente en inicio.txt.

## 2. Fuentes

Se leyeron íntegramente SKILL.md y PERFIL-EXPEDIENTE.md, y estas fuentes autorizadas:

- **C:** pruebas/entradas/E2E-05-correo.md. Remitente cliente@residencia-gamma.example; fecha 2026-11-17 11:00 UTC-05:00; asunto «Expediente DEMO-005 — fabricación de closet». No declara revisión ni identificador propio de correo.
- **F:** pruebas/entradas/E2E-05-ficha.md. FT-DEMO-005, fecha 2026-11-17, R2, expediente DEMO-005, L1.
- **M:** pruebas/entradas/E2E-06-medicion.md. MED-DEMO-005, fecha 2026-11-18, R1, expediente DEMO-005, L1, nicho de Casa Demo C.
- **A:** pruebas/resultados/ronda-1.1/E2E-05-A1/salida-observada.md. Informe documental previo, revisión de análisis 1, conservado sin modificación; antecedente de hallazgos, no sustituto de las fuentes C, F y M.

Recibidos: correo, ficha y registro de medición textuales, además del informe anterior. C decía que el registro no se adjuntaba y F declaraba «Registro de medición en sitio: no disponible»; ahora se aporta M como corrección de esa ausencia. No quedan documentos referenciados ausentes de los controles aplicables ni archivos recibidos ilegibles. No se enumeraron PDF o PNG para esta sesión.

Método: lectura directa e íntegra con PowerShell Get-Content -Raw; no se utilizó pypdf porque ninguna fuente autorizada es PDF. No se usaron OCR, renderizado, red ni comprobaciones externas. Se conservan copias propias de los bytes leídos en fuentes-leidas y sus SHA-256 en registro.json.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA**. La evidencia nueva satisface F04: registro de medición con fecha y responsable y confirmación explícita de incorporación a FT-DEMO-005 R2 aprobada, sin cambio de datos. Los controles obligatorios aplicables están satisfechos; no se identifican contradicciones pendientes. Este estado no autoriza fabricación, compra ni instalación.

## 4. Datos normalizados

| Dato | Valor original y valor de revisión | Estado del dato | Procedencia |
|---|---|---|---|
| Expediente y etapa | «DEMO-005»; «Etapa a revisar: fabricación» | aportado | C, asunto y Etapa a revisar; F y M, Expediente |
| Cliente y contacto | «Residencia Gamma Demo»; «cliente@residencia-gamma.example» | aportado | C, Cliente y Contacto; correo identificado en fuentes |
| Proyecto y destino | «Proyecto residencial»; «Casa Demo C, Ciudad de Panamá, Panamá» | aportado | C, Proyecto y Destino |
| Línea y cantidad | «L1: closet a medida ajustado a nicho existente, 1 unidad»; F: «línea L1; 1 closet ajustado a nicho existente» | aportado | C, L1; F, Expediente/línea |
| Dimensiones | C y F: «Dimensiones L x A x H: 2400 x 600 x 2400 mm»; M: «L x A x H = 2400 x 600 x 2400 mm». Largo 2400 mm, ancho 600 mm, alto 2400 mm | aportado | C y F, Dimensiones; M, Medición registrada |
| Material y acabado | «tablero melamínico de 18 mm»; «roble claro» | aportado | C, Material/Acabado; F, Tablero/acabado |
| Ruta y fabricante | «Ruta: fabricación»; «Taller Demo Local» | aportado | C, Ruta/Taller; F, Taller |
| Precio, subtotal y total | «USD 1200.00 por unidad»; «subtotal USD 1200.00»; «total USD 1200.00» | aportado | C, condiciones comerciales |
| Servicios y cargos | «Instalación incluida; transporte incluido; impuestos USD 0.00; otros cargos USD 0.00» | aportado | C, Instalación/transporte/impuestos/otros cargos |
| Pago | «50 % al aceptar y 50 % al terminar instalación» | aportado | C, Pago |
| Entrega | «Casa Demo C, 2026-12-15» | aportado | C, Entrega |
| Plazo de fabricación | «15 días calendario desde aprobación técnica» | aportado | C, Plazo de fabricación |
| Ficha controlada | «FT-DEMO-005, fecha 2026-11-17, revisión R2» | aportado | C, Ficha técnica adjunta; F, encabezado |
| Aceptación | «Acepto alcance, cantidades, especificaciones y condiciones de R2»; «Aceptación: Sara Demo, 2026-11-17» | aportado | C, Acepto/Aceptación, tras referencia a FT-DEMO-005 R2 |
| Aprobación técnica de ficha | «Revisión técnica: Mateo Demo, 2026-11-17, aprueba esta ficha R2 según constancia ficticia de prueba» | aportado | F, Revisión técnica y encabezado |
| Registro de medición | «Registro MED-DEMO-005, fecha 2026-11-18, revisión R1»; «Medición registrada por Mateo Demo» | aportado | M, encabezado y Medición registrada; DEMO-005/L1/nicho de Casa Demo C |
| Incorporación a ficha | «El responsable técnico confirma expresamente que esta medición se incorporó y corresponde a FT-DEMO-005 R2, sin cambiar sus datos»; «Confirmación técnica: Mateo Demo, 2026-11-18» | aportado | M, confirmación e identidad/fecha |

Apoyo aritmético decimal, a centavos: 1 × USD 1200.00 = USD 1200.00 de subtotal; USD 1200.00 + USD 0.00 de impuestos + USD 0.00 de otros cargos = USD 1200.00 de total. Transporte e instalación constan incluidos. No se convirtieron monedas ni unidades; las tres dimensiones coinciden en mm. No se calcularon fechas a partir de plazos ni se comprobó factibilidad de la entrega.

La fecha posterior de M se conserva: documenta la confirmación de incorporación el 2026-11-18 y no cambia retroactivamente la fecha de aprobación de F ni la aceptación de C, ambas del 2026-11-17. Su declaración expresa de correspondencia e inexistencia de cambios permite resolver la ausencia anterior sin inferir una nueva versión ni una contradicción dimensional. No se pide corregir la fecha futura del fixture por comparación con la hora real de análisis.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de fabricación | satisfecho | C, asunto/etapa: DEMO-005 y fabricación. F y M vinculan expediente. Identificador ficticio, sin atribución a ERP. |
| P02 | Sí | satisfecho | C, Cliente/Contacto: Residencia Gamma Demo y cliente@residencia-gamma.example. |
| P03 | Sí | satisfecho | C, Proyecto/Destino: residencial; Casa Demo C, Ciudad de Panamá, Panamá. |
| P04 | Sí, L1 | satisfecho | C, L1 y F, expediente/línea: closet a medida, L1, 1 unidad. |
| P05 | Sí, L1 | satisfecho | C y F: L x A x H 2400 x 600 x 2400 mm; tablero melamínico 18 mm, roble claro. M confirma las medidas, sin deducirlas de imágenes. |
| P06 | Sí, L1 | satisfecho | C, Ruta: fabricación expresamente declarada. |
| P07 | Sí | satisfecho | C, condiciones comerciales/Pago: USD, precio unitario, subtotal, cargos, total y pago 50 %/50 %. Operaciones decimales mostradas arriba. |
| P08 | Sí | satisfecho | C, Entrega: Casa Demo C, 2026-12-15; instalación incluida. |
| P09 | Sí | satisfecho | C identificado por remitente, fecha y asunto. F: FT-DEMO-005, 2026-11-17, R2, DEMO-005/L1; aceptación de Sara Demo y aprobación de Mateo Demo fechadas y vinculadas. M: MED-DEMO-005, 2026-11-18, R1, DEMO-005/L1; confirmación técnica expresa atribuida a Mateo Demo el 2026-11-18, vinculada a esta medición y FT-DEMO-005 R2. No se verifica autoridad ni autenticidad. |
| P10 | Sí | satisfecho | C, Acepto/Aceptación: Sara Demo, 2026-11-17, alcance, cantidades, especificaciones y condiciones de R2. M confirma que no cambia los datos de la ficha aceptada. |
| F01 | Sí, fabricación L1 | satisfecho | C, Taller y F, Taller: Taller Demo Local para la línea L1. |
| F02 | Sí, fabricación L1 | satisfecho | F disponible, FT-DEMO-005 R2, DEMO-005/L1, 1 closet, dimensiones/material/acabado coincidentes con C y aceptación R2. |
| F03 | Sí, fabricación L1 | satisfecho | F, Revisión técnica: Mateo Demo aprueba esta ficha R2 el 2026-11-17, identificada como FT-DEMO-005 en encabezado. |
| F04 | Sí, ajuste a nicho existente | satisfecho | C y F activan condición. M, MED-DEMO-005 R1 de 2026-11-18: medición por Mateo Demo y confirmación explícita de incorporación/correspondencia a FT-DEMO-005 R2, sin cambiar datos; Mateo Demo, 2026-11-18. |
| F05 | Sí, fabricación L1 | satisfecho | C, Plazo de fabricación: 15 días calendario desde aprobación técnica; C, Entrega/Destino: Casa Demo C, Ciudad de Panamá, Panamá. |
| I01 | No | NA | C declara fabricación como única ruta de L1; no hay línea de importación. |
| I02 | No | NA | Única línea de fabricación según C; no procede cotejo con proforma de importación. |
| I03 | No | NA | No hay ruta de importación declarada; destino de entrega consta en C. |
| I04 | No | NA | No hay línea de importación; condiciones comerciales evaluadas en P07. |
| I05 | No | NA | No hay línea de importación; plazo aplicable evaluado en F05. |
| I06 | No | NA | Ruta de fabricación; las fuentes del caso no utilizan Incoterm. |

## 6. Hallazgos

**H01 — F04, resuelto en esta revisión.** El antecedente A registraba la ausencia de medición e incorporación a la ficha; C y F conservan esas declaraciones originales. M aporta MED-DEMO-005 R1, fecha 2026-11-18, DEMO-005/L1, medición por Mateo Demo de 2400 x 600 x 2400 mm y confirmación técnica expresa de incorporación a FT-DEMO-005 R2 sin cambios, atribuida y fechada. Consecuencia documental: F04 queda satisfecho; no queda acción de aporte pendiente por este hallazgo.

No se identificaron otros faltantes, contradicciones aplicables ni fuentes esenciales ilegibles en el material autorizado. Las fechas y aprobaciones se registran como declaraciones del expediente ficticio, sin comprobación externa.

## 7. Preguntas y siguiente acción humana

No hay preguntas bloqueantes de PEO-01 v1.1 con estas fuentes. Siguiente acción humana: revisar conjuntamente la ficha R2, el registro MED-DEMO-005 R1 y este informe antes de decidir sobre la fabricación. El estado documental no constituye aprobación de la operación ni sustituye la revisión técnica humana.

## 8. Límites

Revisión exclusivamente documental. No se comprobaron externamente medidas, identidad o autoridad de las personas, autenticidad de documentos, calidad, capacidad del taller, factibilidad, plazos ni cumplimiento técnico/legal. No constituye ingeniería, dictamen legal, certificación ni conformidad ISO. Los 21 controles pertenecen a PEO-01 v1.1; no se consultó red ni texto normativo externo. No se emite veredicto de prueba.

## 9. Cambios respecto a revisión anterior

El informe A, revisión 1, queda intacto. Se agrega M como nueva fuente. H01/F04 pasa de faltante a satisfecho por el registro fechado con responsable y confirmación expresa de incorporación a la ficha aprobada sin cambios. El estado global pasa de PENDIENTE DE INFORMACIÓN a DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA. Los datos de producto, condiciones, ficha R2, aprobación técnica y aceptación se mantienen según las fuentes originales. No se borran ni reescriben las declaraciones previas de ausencia.