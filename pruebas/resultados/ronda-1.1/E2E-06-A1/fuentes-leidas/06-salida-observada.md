# Informe documental — DEMO-005

## 1. Identificación

Expediente ficticio DEMO-005 — SOLO PRUEBA TÉCNICA. Revisión de análisis: 1, independiente. Etapa declarada: fabricación, antes de iniciar la operación. Ruta de L1: fabricación. Skill aplicada: revisor-expedientes-mobiliario 1.1; perfil PEO-01 v1.1. Las fechas documentales se conservan como datos del expediente y se distinguen del horario real registrado en inicio.txt y registro.json.

## 2. Fuentes

Se leyeron íntegramente las instrucciones SKILL.md y PERFIL-EXPEDIENTE.md y estas fuentes del caso:

- **C:** pruebas/entradas/E2E-05-correo.md. Correo de cliente@residencia-gamma.example, fecha declarada 2026-11-17 11:00 UTC-05:00, asunto «Expediente DEMO-005 — fabricación de closet». No declara identificador ni revisión propios de correo; no se inventan. Las referencias siguientes usan sus campos literales.
- **F:** pruebas/entradas/E2E-05-ficha.md. Ficha FT-DEMO-005, fecha 2026-11-17, revisión R2, vinculada a DEMO-005/L1.

Recibidos: correo y ficha textual. Referenciado ausente: registro de medición del nicho; C dice «Se menciona un registro de medición del nicho, pero no se adjunta» y F, campo Registro de medición en sitio, dice «no disponible». No hay archivos recibidos ilegibles ni PDF o PNG entre las fuentes enumeradas. No se aportó un informe anterior.

Método: lectura directa del texto completo de los cuatro archivos autorizados mediante PowerShell Get-Content -Raw. No se usó extracción PDF, renderizado, OCR, red ni comprobación externa. Se conserva una copia textual propia de la lectura y hashes SHA-256 de los bytes originales.

## 3. Estado global

**PENDIENTE DE INFORMACIÓN**. F04 se activa porque el closet está ajustado a un nicho existente; falta el registro de medición con fecha y responsable y la confirmación de incorporación a la revisión aprobada. No se detectaron contradicciones entre los valores aportados. La ausencia del documento es un faltante, no un archivo recibido ilegible.

## 4. Datos normalizados

| Dato | Valor original / valor de revisión | Estado del dato | Procedencia |
|---|---|---|---|
| Identificación y etapa | «DEMO-005»; «Etapa a revisar: fabricación» | aportado | C, Asunto y Etapa a revisar; F, Expediente |
| Cliente y contacto | «Residencia Gamma Demo»; «cliente@residencia-gamma.example» | aportado | C, Cliente y Contacto |
| Proyecto y destino | «Proyecto residencial»; «Casa Demo C, Ciudad de Panamá, Panamá» | aportado | C, Proyecto y Destino |
| Línea, descripción y cantidad | «L1: closet a medida ajustado a nicho existente, 1 unidad»; F: «línea L1; 1 closet ajustado a nicho existente» | aportado | C, L1; F, Expediente/línea |
| Dimensiones | «Dimensiones L x A x H: 2400 x 600 x 2400 mm»; largo 2400 mm, ancho 600 mm, alto 2400 mm | aportado | C y F, Dimensiones L x A x H |
| Material y acabado | «tablero melamínico de 18 mm»; «roble claro» | aportado | C, Material y Acabado; F, Tablero/acabado |
| Ruta y taller | «Ruta: fabricación»; «Taller Demo Local» | aportado | C, Ruta y Taller; F, Taller |
| Moneda y precio unitario | «USD 1200.00 por unidad» | aportado | C, USD/precio |
| Subtotal y total | «subtotal USD 1200.00»; «total USD 1200.00» | aportado | C, subtotal y total |
| Servicios y cargos | «Instalación incluida; transporte incluido; impuestos USD 0.00; otros cargos USD 0.00» | aportado | C, Instalación/transporte/impuestos/otros cargos |
| Pago | «50 % al aceptar y 50 % al terminar instalación» | aportado | C, Pago |
| Entrega | «Casa Demo C, 2026-12-15» | aportado | C, Entrega |
| Plazo de fabricación | «15 días calendario desde aprobación técnica» | aportado | C, Plazo de fabricación |
| Ficha controlada | «FT-DEMO-005, fecha 2026-11-17, revisión R2» | aportado | C, Ficha técnica adjunta; F, encabezado |
| Aceptación del cliente | «Acepto alcance, cantidades, especificaciones y condiciones de R2»; «Aceptación: Sara Demo, 2026-11-17» | aportado | C, Acepto y Aceptación; referencia a FT-DEMO-005 en campo precedente |
| Aprobación técnica | «Revisión técnica: Mateo Demo, 2026-11-17, aprueba esta ficha R2 según constancia ficticia de prueba» | aportado | F, Revisión técnica; ficha identificada en encabezado |
| Medición del nicho | Registro: NO APORTADO. Fecha, responsable y confirmación de incorporación a R2: NO APORTADO | faltante | C, última declaración; F, Registro de medición en sitio |

Comprobación decimal de importes declarados: 1 × USD 1200.00 = USD 1200.00 de subtotal; USD 1200.00 + USD 0.00 de impuestos + USD 0.00 de otros cargos = USD 1200.00 de total. Transporte e instalación constan incluidos, sin añadir un cargo inventado. No se convirtieron monedas ni dimensiones, ni se calculó una fecha a partir del plazo de fabricación. La fecha de entrega y el plazo declarado se conservan como declaraciones documentales, sin inferir una contradicción ni garantizar su factibilidad.

## 5. Checklist

| ID | Aplicabilidad | Estado | Evidencia y motivo |
|---|---|---|---|
| P01 | Sí, base de fabricación | satisfecho | C, Asunto y Etapa a revisar: DEMO-005 y fabricación; F vincula expediente. Identificador ficticio, sin atribución a ERP. |
| P02 | Sí | satisfecho | C, Cliente/Contacto: Residencia Gamma Demo y correo explícito. |
| P03 | Sí | satisfecho | C, Proyecto/Destino: residencial, Casa Demo C, Ciudad de Panamá, Panamá. |
| P04 | Sí, L1 | satisfecho | C, L1: identificador, closet a medida, 1 unidad; F confirma línea y cantidad. |
| P05 | Sí, L1 | satisfecho | C y F, Dimensiones/material/acabado: L x A x H 2400 x 600 x 2400 mm, tablero melamínico 18 mm, roble claro. |
| P06 | Sí, L1 | satisfecho | C, Ruta: fabricación, explícita. |
| P07 | Sí | satisfecho | C, USD/subtotal/cargos/total/Pago: USD 1200.00 unitario y total; cargos declarados; pago 50 %/50 %. Aritmética mostrada arriba. |
| P08 | Sí | satisfecho | C, Entrega: 2026-12-15 a Casa Demo C; instalación incluida. |
| P09 | Sí | satisfecho | C identificado por remitente/fecha/asunto; FT-DEMO-005 de 2026-11-17 R2, DEMO-005/L1. C aporta aceptación atribuida a Sara Demo con fecha y alcance R2; F aporta aprobación de esta ficha R2 atribuida a Mateo Demo y fecha. No se acredita autenticidad ni autoridad. |
| P10 | Sí | satisfecho | C, Acepto/Aceptación: alcance, cantidades, especificaciones y condiciones R2; Sara Demo, 2026-11-17, vinculada a la ficha identificada. |
| F01 | Sí, fabricación L1 | satisfecho | C, Ruta/Taller y F, Taller: Taller Demo Local asociado a L1. |
| F02 | Sí, fabricación L1 | satisfecho | F disponible: FT-DEMO-005 R2, DEMO-005/L1, 1 closet, especificaciones coincidentes con C y aceptación R2. |
| F03 | Sí, fabricación L1 | satisfecho | F, Revisión técnica: Mateo Demo, 2026-11-17, aprueba esta ficha R2; encabezado identifica FT-DEMO-005. Evidencia documental ficticia, sin sustituir revisión técnica. |
| F04 | Sí, ajuste a espacio existente | faltante | C y F declaran ajuste a nicho existente. C no adjunta registro y F lo declara no disponible; faltan fecha, responsable y confirmación de incorporación a R2. |
| F05 | Sí, fabricación L1 | satisfecho | C, Plazo de fabricación: 15 días calendario desde aprobación técnica; C, Entrega/Destino: Casa Demo C, Ciudad de Panamá, Panamá. |
| I01 | No | NA | C, Ruta: fabricación; ninguna línea declara importación. |
| I02 | No | NA | L1 solo fabricación según C; no corresponde cotejo con proforma de importación. |
| I03 | No | NA | No hay ruta de importación declarada; C identifica el destino de fabricación/entrega. |
| I04 | No | NA | No hay línea de importación; condiciones comerciales se revisan en P07. |
| I05 | No | NA | No hay línea de importación; el plazo de fabricación se revisa en F05. |
| I06 | No | NA | Ruta solo fabricación; las fuentes recibidas no utilizan Incoterm. |

## 6. Hallazgos

**H01 — F04: registro de medición e incorporación no aportados.** C, L1 y F, descripción, declaran un closet «ajustado a nicho existente». C informa que el registro se menciona pero no se adjunta; F, Registro de medición en sitio, declara «no disponible». No se aportan las mediciones documentadas, su fecha y responsable ni la confirmación de incorporación a FT-DEMO-005 R2 aprobada. Consecuencia: no está satisfecho el control documental del ajuste al espacio existente; el expediente queda pendiente. Acción requerida: aportar el registro fechado e identificado con su responsable y una constancia que vincule su incorporación a la revisión aprobada. Las dimensiones de la ficha y su aprobación técnica no sustituyen esa evidencia.

## 7. Preguntas y siguiente acción humana

Para resolver H01/F04: ¿pueden aportar el registro de medición del nicho con fecha y responsable y la confirmación explícita de que esas mediciones se incorporaron a FT-DEMO-005 R2 aprobada?

Siguiente acción humana: incorporar esa evidencia y someter el expediente a una nueva revisión documental, conservando este informe. Si la evidencia cambia la ficha, deben identificarse la nueva revisión y las aprobaciones técnicas y aceptación del cliente correspondientes al alcance modificado. Este informe no autoriza la fabricación.

## 8. Límites

Revisión exclusivamente documental de las fuentes recibidas. Las identidades, fechas, aprobaciones, importes y datos técnicos se registran según lo declarado, sin comprobación externa de autenticidad, autoridad, medidas del sitio, calidad del material, factibilidad, plazos o cumplimiento técnico/legal. No constituye ingeniería, certificación ni declaración de conformidad ISO. Los controles pertenecen a PEO-01 v1.1; no se realizó consulta externa ni validación normativa. No se emite veredicto de prueba.