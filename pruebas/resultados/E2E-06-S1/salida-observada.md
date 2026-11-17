# Informe documental

## 1. Identificación

Expediente **DEMO-005**. Revisión de análisis **2**, emitida el 17 de noviembre de 2026 (America/Panama, UTC-05). Etapa: **fabricación**, antes del inicio de la operación. Única línea L1, ruta explícita de fabricación. Perfil **PEO-01 v1.0**; skill **revisor-expedientes-mobiliario**, instrucciones v1.0. **FICTICIO — SOLO PRUEBA TÉCNICA**. Se conserva el informe de análisis 1 y se revisa la evidencia adicional recibida.

## 2. Fuentes

Leídas íntegramente como texto, sin OCR ni comprobación externa:

- **C** — `pruebas/entradas/E2E-05-correo.md`: asunto «Expediente DEMO-005 — fabricación de closet», fecha 2026-11-17 11:00 UTC-05:00, remitente cliente@residencia-gamma.example. Sin identificador o revisión propios adicionales; identificado por asunto y fecha. Remite a FT-DEMO-005 R2.
- **F** — `pruebas/entradas/E2E-05-ficha.md`: FT-DEMO-005, fecha 2026-11-17, revisión R2, expediente DEMO-005, L1.
- **M** — `pruebas/entradas/E2E-06-medicion.md`: MED-DEMO-005, fecha 2026-11-18, revisión R1, DEMO-005/L1, nicho de Casa Demo C. Incluye confirmación técnica fechada 2026-11-18 de Mateo Demo.
- **A1** — `pruebas/resultados/E2E-05-S1/salida-observada.md`: informe de análisis 1, emitido 2026-11-17, aportado como antecedente. No se modifica y no sustituye los documentos fuente.

Documentos rectores leídos: `SKILL.md` y `PERFIL-EXPEDIENTE.md`. No hay archivos recibidos ilegibles. El registro antes mencionado como ausente está ahora disponible como M. No se identifican otros documentos obligatorios referenciados y ausentes.

Las fechas se conservan literalmente: M y su confirmación declaran 2026-11-18, posterior a la fecha de esta revisión. Se registra la afirmación documental, sin certificar que la medición o la confirmación hayan ocurrido físicamente ni corregir sus fechas. No se aplican requisitos cronológicos adicionales no definidos en PEO-01.

## 3. Estado global

**DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA**.

Los controles obligatorios aplicables están satisfechos documentalmente. M aporta el registro fechado, responsable y confirmación expresa de incorporación a FT-DEMO-005 R2 sin cambios, resolviendo H01/F04 del antecedente. No se detectan contradicciones aplicables pendientes. Este estado no autoriza producción, compra, importación ni instalación.

## 4. Datos normalizados

«Aportado» significa declarado en las fuentes, sin comprobación externa. L = largo; A = ancho; H = alto. No se realizan conversiones dimensionales.

| Dato | Valor original y normalizado | Estado y procedencia |
|---|---|---|
| Identificador y etapa | «DEMO-005»; «fabricación» | aportado — C, asunto/etapa; F y M, expediente |
| Cliente y contacto | «Residencia Gamma Demo»; cliente@residencia-gamma.example | aportado — C, cliente/contacto |
| Proyecto y destino | «Proyecto residencial»; «Casa Demo C, Ciudad de Panamá, Panamá» | aportado — C, proyecto/destino; M, nicho de Casa Demo C |
| Línea y cantidad | «L1: closet a medida ajustado a nicho existente, 1 unidad» | aportado — C, línea; F, expediente/línea y «1 closet ajustado a nicho existente» |
| Dimensiones aceptadas | «Dimensiones L x A x H: 2400 x 600 x 2400 mm» → largo 2400 mm, ancho 600 mm, alto 2400 mm | aportado — C y F, dimensiones |
| Dimensiones de medición | «L x A x H = 2400 x 600 x 2400 mm» → largo 2400 mm, ancho 600 mm, alto 2400 mm | aportado — M, medición; coincidencia textual exacta con C/F, sin tolerancias inventadas |
| Material y acabado | «tablero melamínico de 18 mm»; «roble claro» | aportado — C y F, material/acabado |
| Ruta y taller | «fabricación»; «Taller Demo Local» | aportado — C, ruta/taller; F, taller |
| Moneda/precio/subtotal | «USD 1200.00 por unidad»; «subtotal USD 1200.00» | aportado — C, condiciones comerciales |
| Alcance y cargos | «Instalación incluida; transporte incluido; impuestos USD 0.00; otros cargos USD 0.00» | aportado — C, alcance/cargos; no se asigna precio separado a servicios incluidos |
| Total y pago | «total USD 1200.00»; «50 % al aceptar y 50 % al terminar instalación» | aportado — C, total/pago |
| Entrega | «Casa Demo C, 2026-12-15» | aportado — C, entrega |
| Fabricación | «15 días calendario desde aprobación técnica» | aportado — C, plazo; hito explícito, sin derivar fecha final |
| Ficha aplicable | «FT-DEMO-005, fecha 2026-11-17, revisión R2» | aportado — C, ficha adjunta; F, encabezado |
| Aceptación del cliente | «Acepto alcance, cantidades, especificaciones y condiciones de R2»; «Sara Demo, 2026-11-17» | aportado — C, aceptación; no se acredita autoridad legal |
| Revisión técnica | «Mateo Demo, 2026-11-17, aprueba esta ficha R2 según constancia ficticia de prueba» | aportado — F, revisión técnica |
| Registro de medición | «MED-DEMO-005, fecha 2026-11-18, revisión R1»; «Medición registrada por Mateo Demo» | aportado — M, encabezado y medición |
| Incorporación a R2 | «El responsable técnico confirma expresamente que esta medición se incorporó y corresponde a FT-DEMO-005 R2, sin cambiar sus datos»; «Confirmación técnica: Mateo Demo, 2026-11-18» | aportado — M, confirmación; no implica nueva revisión de ficha |
| Ausencia histórica | C: «no se adjunta»; F: «no disponible» | aportado — campos de medición de las fuentes iniciales; describen su disponibilidad anterior. M aporta ahora el documento y su vínculo explícito, sin alterar C/F |

Operaciones decimales de apoyo, comparadas a centavos:

- 1 unidad × USD 1200.00/unidad = **USD 1200.00**, coincide con el subtotal declarado.
- USD 1200.00 + USD 0.00 de impuestos + USD 0.00 de otros cargos = **USD 1200.00**, coincide con el total. Transporte e instalación se declaran incluidos; no se inventan importes separados.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Obligatorio, base de fabricación | satisfecho | C, asunto y etapa: DEMO-005/fabricación. Identificador ficticio, sin atribución a ERP real. |
| P02 | Obligatorio | satisfecho | C, cliente/contacto: Residencia Gamma Demo y correo explícito. |
| P03 | Obligatorio | satisfecho | C, proyecto residencial y Casa Demo C, Ciudad de Panamá, Panamá; destino suficiente para la demostración. |
| P04 | Obligatorio | satisfecho | C, L1, closet ajustado a nicho, 1 unidad; F corresponde a L1 y 1 closet. |
| P05 | Obligatorio | satisfecho | C/F: largo, ancho, alto 2400/600/2400 mm; tablero melamínico de 18 mm, roble claro. M coincide. |
| P06 | Obligatorio | satisfecho | C, ruta de fabricación explícita para L1. |
| P07 | Obligatorio | satisfecho | C, USD, unitario/subtotal/total, impuestos y otros cargos, servicios incluidos y pago. Aritmética mostrada sin discrepancia. |
| P08 | Obligatorio | satisfecho | C, entrega 2026-12-15 y destino; instalación incluida. |
| P09 | Obligatorio | satisfecho | FT-DEMO-005 R2 de 2026-11-17 disponible, identificada y aceptada en C; M, MED-DEMO-005 R1 de 2026-11-18, vinculado expresamente a DEMO-005/L1 y R2 sin cambios. C identificado por asunto/fecha, sin revisión propia declarada. |
| P10 | Obligatorio | satisfecho | C, aceptación expresa de alcance, cantidades, especificaciones y condiciones R2 por Sara Demo, 2026-11-17. M no declara modificación de esos datos. |
| F01 | Obligatorio para L1 | satisfecho | C/F, Taller Demo Local y línea L1. |
| F02 | Obligatorio para L1 | satisfecho | F, ficha FT-DEMO-005 R2 disponible, línea/cantidad/especificaciones correspondientes a lo aceptado. M confirma correspondencia sin cambios. |
| F03 | Obligatorio para L1 | satisfecho | F, Mateo Demo, 2026-11-17, aprobación de esta ficha R2, identificada en encabezado. Se registra evidencia ficticia, sin sustituir revisión técnica. |
| F04 | Condicional activado | satisfecho | C/F declaran ajuste a nicho existente. M aporta registro MED-DEMO-005 R1, fecha 2026-11-18, responsable Mateo Demo y confirmación técnica expresa de incorporación a FT-DEMO-005 R2 aprobada, sin cambiar sus datos. |
| F05 | Obligatorio para L1 | satisfecho | C, 15 días calendario desde aprobación técnica, destino Casa Demo C; entrega declarada. No se promete fecha derivada. |
| I01 | No aplicable | NA | C declara ruta exclusivamente de fabricación en L1; no se exige proveedor/proforma de importación. |
| I02 | No aplicable | NA | Ruta explícita de fabricación; no hay líneas de importación. |
| I03 | No aplicable | NA | Ruta explícita de fabricación; no se exige país de despacho internacional. |
| I04 | No aplicable | NA | Ruta explícita de fabricación; comerciales revisados en P07. |
| I05 | No aplicable | NA | Ruta explícita de fabricación; plazo revisado en F05. |
| I06 | No aplicable | NA | Sin ruta de importación ni Incoterm utilizado por las fuentes. |

## 6. Hallazgos

### H01 — Medición del nicho y vínculo con ficha aprobada: resuelto documentalmente

**Requisito:** F04, L1. **Antecedente:** A1 registró la ausencia del registro y de su incorporación a la ficha; C decía «no se adjunta» y F «no disponible».

**Nueva evidencia:** M, MED-DEMO-005 R1, fecha 2026-11-18, registra la medición por Mateo Demo para DEMO-005/L1 en Casa Demo C. Sus dimensiones 2400 x 600 x 2400 mm coinciden exactamente con C/F. Su confirmación técnica por Mateo Demo, 2026-11-18, declara expresamente incorporación y correspondencia a FT-DEMO-005 R2 «sin cambiar sus datos».

**Consecuencia documental:** quedan aportados fecha, responsable y vínculo con la revisión aprobada. La resolución se fundamenta en esa evidencia explícita, no en que el documento tenga fecha más reciente. No hay modificación declarada de R2 que exija inferir una sustitución o una aceptación nueva. Las afirmaciones anteriores de ausencia se conservan como antecedente de disponibilidad, sin reescribir las fuentes.

**Acción requerida:** ninguna evidencia adicional para cerrar H01 conforme a PEO-01; someter el conjunto y esta revisión al examen humano. No se identifican otros hallazgos abiertos bajo el perfil aplicado.

## 7. Preguntas y siguiente acción humana

No quedan preguntas bloqueantes bajo PEO-01 con los documentos aportados. La siguiente acción humana es revisar el expediente completo junto con esta revisión 2 y el antecedente conservado, considerando las fechas documentadas literalmente y los límites de comprobación. No se emite autorización de fabricación, compra, importación ni instalación.

## 8. Límites

Revisión exclusivamente documental de textos recibidos. No se comprobó externamente autenticidad, identidad, autoridad de firmantes, fechas de ejecución de hechos, medición física, materiales, calidad, factibilidad ni capacidad del taller. No se efectuaron ingeniería, planos, cálculos estructurales ni validación técnica o legal. No se emplearon red, plugins, OCR ni visión; no se enviaron mensajes ni se ejecutaron acciones externas.

Los requisitos son propios del perfil de demostración PEO-01 v1.0. No se afirma conformidad ni certificación ISO ni se atribuyen estos campos a una obligación universal de ISO. Las referencias normativas del perfil no se verificaron externamente.

## 9. Cambios respecto a revisión anterior

| Elemento | Revisión 1 aportada | Revisión 2 y evidencia |
|---|---|---|
| Fuentes del expediente | C y F; medición ausente | Se incorpora M, MED-DEMO-005 R1, con identidad, fecha, revisión y vínculo al expediente/L1. A1 se conserva intacto. |
| Datos de medición | Registro, fecha y responsable: NO APORTADO | M aporta 2400 x 600 x 2400 mm, fecha 2026-11-18 y responsable Mateo Demo. |
| Incorporación a R2 | NO APORTADO | M confirma expresamente incorporación/correspondencia a FT-DEMO-005 R2 sin cambios, por Mateo Demo el 2026-11-18. |
| F04 / H01 | faltante / abierto | satisfecho / resuelto documentalmente por M. |
| Estado global | PENDIENTE DE INFORMACIÓN | DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA; no autoriza operación. |
| Otros controles y valores | Base, fabricación salvo F04 satisfechos; importación NA | Se mantienen tras cotejo de C/F/M. No cambia la ficha aceptada R2, cantidad, dimensiones, condiciones comerciales ni entrega declaradas. |

No se modifica retrospectivamente el informe anterior ni se afirma que la medición hubiera estado aportada en aquella revisión.
