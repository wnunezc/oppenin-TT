# Revisor de expedientes de mobiliario

Skill de inteligencia artificial para revisar la integridad y coherencia documental de pedidos de mobiliario residencial y corporativo antes de compra, fabricación o importación. Entrega: **versión inicial**.

Recibe manualmente correos, fichas, PDF e imágenes compatibles con la IA utilizada. Entrega un informe de fuentes, datos, faltantes, contradicciones y preguntas para revisión humana, según el perfil de demostración **PEO-01 (versión inicial)**.

Los cambios, correcciones y rondas de validación pertenecen a esta misma versión inicial. Los números conservados en rutas o evidencias son etiquetas internas de trabajo; no representan versiones liberadas ni versionado en Git.

## Documentación

| Documento | Contenido |
|---|---|
| [Explicación](EXPLICACION.md) | Problema propuesto, destinatarios, utilidad y ejemplo ejecutado con datos ficticios; máximo una página. |
| [Guía de uso](GUIA-DE-USO.md) | Activación manual, entradas admitidas, interpretación de resultados y límites. |
| [Skill](SKILL.md) | Instrucciones reutilizables, versión inicial. Usar junto con el perfil. |
| [Perfil documental](PERFIL-EXPEDIENTE.md) | Controles PEO-01 (versión inicial), precisión autorizada de P09, aplicabilidad por etapa y ruta, estados y referencias internacionales. |
| [Reporte de creación](REPORTE-CREACION.md) | Proceso real, herramientas, prompts, fechas, problemas, validaciones y limitaciones. |
| [Resultados de pruebas](pruebas/RESULTADOS.md) | Comparación esperado/observado, veredictos locales y enlaces a evidencias. |
| [Especificación de desarrollo](PROMPTD-CREACION-SKILL.md) | Alcance y siete escenarios originales; se conserva como antecedente. La precisión posterior autorizada de P09 está en el perfil activo. |

## Cómo probarla

1. Abrir una conversación nueva en una IA que pueda leer los medios aportados y cargar [SKILL.md](SKILL.md) y [PERFIL-EXPEDIENTE.md](PERFIL-EXPEDIENTE.md). Para herramientas sin archivos auxiliares, copiar las [instrucciones completas reunidas](pruebas/resultados/instrucciones-completas.txt).
2. Seguir la activación de la [guía de uso](GUIA-DE-USO.md) y aportar únicamente los documentos del expediente. Para empezar, puede utilizarse el [correo ficticio DEMO-001](pruebas/entradas/E2E-01-correo.md).
3. Solicitar: `Revisa este expediente en la etapa indicada y entrega tu informe documental`.

Durante una prueba independiente, no cargar la especificación de desarrollo, los resultados esperados ni las respuestas de otros casos. Para una corrección, aportar deliberadamente el informe anterior y la nueva evidencia.

## Validación y evidencias

**El estado del expediente no es el resultado de la prueba.** Si un expediente incompleto devuelve `PENDIENTE DE INFORMACIÓN` y detecta los faltantes esperados, la prueba se aprueba. Los casos de conflicto e ilegibilidad deliberados también se evalúan contra su comportamiento esperado. No se exige redacción idéntica ni que todos los expedientes resulten suficientes.

La ronda de revalidación completó **18 ejecuciones aprobadas contra sus criterios funcionales**: las trece mínimas, una de imagen documental legible y cuatro de robustez (PDF escaneado, imagen ilegible, archivo dañado e instrucciones maliciosas en imagen). E2E-02/03/04 conservaron estado global y hallazgos obligatorios en sus tres ejecuciones completas; se documenta una variación auxiliar de P09 en E2E-04, sin aprobación de la versión no resuelta. Los tres intentos A3 interrumpidos por límite de uso se conservaron y se reintentaron en sesiones limpias A4; no cuentan como ejecuciones completas. La primera ronda de pruebas permanece como historial.

- [Entradas ficticias](pruebas/entradas/): correos, fichas, las cuatro proformas originales e imágenes y variantes controladas de robustez.
- [Salidas y registros de la ronda de revalidación](pruebas/resultados/ronda-1.1/): informes observados, solicitudes, sellos reales, métodos de lectura y hashes por ejecución.
- [Documentación de preparación previa](pruebas/resultados/historico-v1.0/): copia previa a las correcciones; las respuestas históricas permanecen intactas en sus directorios originales.
- [Comparación detallada](pruebas/RESULTADOS.md): criterios, resultados, observaciones y límites de consistencia.
- [Validaciones de artefactos y conservación](pruebas/resultados/ronda-1.1/validacion-artefactos.json): controles complementarios de la versión activa; no sustituyen las pruebas con IA.
- [Vista de impresión de la explicación](pruebas/resultados/validacion-fixtures/EXPLICACION-A4.png): una página A4 con márgenes de 2 cm y texto de 11 pt.

## Alcance y límites

Todos los expedientes de prueba son ficticios. La skill no conecta buzones, envía mensajes ni autoriza compras, fabricación, importación o instalación. El estado «DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA» tampoco autoriza esas operaciones.

PEO-01 contiene reglas de esta demostración: sus campos no se atribuyen a ISO ni acreditan certificación. La adopción empresarial requiere validación de la empresa. No se comprobaron autenticidad documental, factibilidad técnica ni cumplimiento legal.

La identidad exacta del modelo servido en las sesiones completas no está expuesta. La skill registra el método de lectura realmente disponible: visión de un render no se presenta como OCR. No se deducen medidas, materiales o aprobaciones de fotografías ni se completa texto ilegible. Los resultados locales no representan aceptación del evaluador ni garantizan el mismo comportamiento en otras herramientas.

Por autorización expresa del usuario, el enunciado original (`PRUEBA TECNICA IT.pdf`), su reproducción (`TASK.MD`) y los demás archivos se incluyen en la entrega inicial. No se necesitan para activar la skill. El repositorio de destino autorizado es [wnunezc/oppenin-TT](https://github.com/wnunezc/oppenin-TT).
