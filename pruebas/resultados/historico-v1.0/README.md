# Revisor de expedientes de mobiliario

Skill de inteligencia artificial para revisar la integridad y coherencia documental de pedidos de mobiliario residencial y corporativo antes de compra, fabricación o importación.

Recibe manualmente correos, fichas, PDF e imágenes compatibles con la IA utilizada. Entrega un informe de fuentes, datos, faltantes, contradicciones y preguntas para revisión humana, según el perfil de demostración **PEO-01 v1.0**.

## Documentación

| Documento | Contenido |
|---|---|
| [Explicación](EXPLICACION.md) | Problema propuesto, destinatarios, utilidad y ejemplo ejecutado con datos ficticios; máximo una página. |
| [Guía de uso](GUIA-DE-USO.md) | Activación manual, entradas admitidas, interpretación de resultados y límites. |
| [Skill](SKILL.md) | Instrucciones reutilizables, versión 1.0. Usar junto con el perfil. |
| [Perfil documental](PERFIL-EXPEDIENTE.md) | Controles PEO-01 v1.0, aplicabilidad por etapa y ruta, estados y referencias internacionales. |
| [Reporte de creación](REPORTE-CREACION.md) | Proceso real, herramientas, prompts, fechas, problemas, validaciones y limitaciones. |
| [Resultados de pruebas](pruebas/RESULTADOS.md) | Comparación esperado/observado, veredictos locales y enlaces a evidencias. |
| [Especificación de desarrollo](PROMPTD-CREACION-SKILL.md) | Alcance complementario autorizado y definición de los siete escenarios originales. |

## Cómo probarla

1. Abrir una conversación nueva en una IA que pueda leer los medios aportados y cargar [SKILL.md](SKILL.md) y [PERFIL-EXPEDIENTE.md](PERFIL-EXPEDIENTE.md). Para herramientas sin archivos auxiliares, copiar las [instrucciones completas reunidas](pruebas/resultados/instrucciones-completas.txt).
2. Seguir la activación de la [guía de uso](GUIA-DE-USO.md) y aportar únicamente los documentos del expediente. Para empezar, puede utilizarse el [correo ficticio DEMO-001](pruebas/entradas/E2E-01-correo.md).
3. Solicitar: `Revisa este expediente en la etapa indicada y entrega tu informe documental`.

Durante una prueba independiente, no cargar la especificación de desarrollo, los resultados esperados ni las respuestas de otros casos. Para una corrección, aportar deliberadamente el informe anterior y la nueva evidencia.

## Validación y evidencias

Se conservaron **14 ejecuciones completas**: las 13 previstas para los siete escenarios originales y sus repeticiones, más una prueba de imagen documental legible. Las 14 fueron aprobadas contra sus criterios locales, con observaciones de calidad documentadas. También se conservaron tres intentos CLI interrumpidos por rechazo del modelo configurado; no cuentan como ejecuciones completas.

- [Entradas ficticias](pruebas/entradas/): correos, fichas, cuatro proformas PDF y una imagen PNG.
- [Salidas y registros](pruebas/resultados/): informes observados, prompts, métodos de lectura y hashes por ejecución.
- [Comparación detallada](pruebas/RESULTADOS.md): criterios, resultados, observaciones y límites de consistencia.
- [Comprobaciones deterministas](pruebas/resultados/validacion-artefactos.json): 47 comprobaciones complementarias; no sustituyen las pruebas con IA.
- [Vista de impresión de la explicación](pruebas/resultados/validacion-fixtures/EXPLICACION-A4.png): una página A4 con márgenes de 2 cm y texto de 11 pt.

## Alcance y límites

Todos los expedientes de prueba son ficticios. La skill no conecta buzones, envía mensajes ni autoriza compras, fabricación, importación o instalación. El estado «DOCUMENTACIÓN SUFICIENTE PARA REVISIÓN HUMANA» tampoco autoriza esas operaciones.

PEO-01 contiene reglas de esta demostración: sus campos no se atribuyen a ISO ni acreditan certificación. La adopción empresarial requiere validación de la empresa. No se comprobaron autenticidad documental, factibilidad técnica ni cumplimiento legal.

La identidad exacta del modelo servido en las sesiones completas no está expuesta. No se validaron OCR de PDF escaneado, imágenes borrosas, texto manuscrito o fotografías de muebles. Los resultados locales no representan aceptación del evaluador ni garantizan el mismo comportamiento en otras herramientas.

El enunciado original (`PRUEBA TECNICA IT.pdf`) y su reproducción (`TASK.MD`) se mantienen ignorados por Git; no se necesitan para activar la skill.
