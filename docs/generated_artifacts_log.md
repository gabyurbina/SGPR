# Registro de artefactos generados automáticamente

Fecha: 2026-06-04
Responsable de generación: Copilot-assisted automation (documentado por la desarrolladora)

Archivos añadidos para completar entregables faltantes:

- /docs/wireframe_login.svg — Wireframe del login (SVG)
- /docs/wireframe_dashboard.svg — Wireframe del panel principal (SVG)
- /docs/wireframe_form_solicitud.svg — Wireframe del formulario de solicitud (SVG)
- /docs/test_evidences.md — Documento con evidencias de pruebas y placeholders para capturas y reportes
- /ops/backup.ps1 — Script PowerShell de backup con rotación y ejemplo pg_dump

Razonamiento y contexto:
- Wireframes textualizados en SVG para evitar imágenes binarias y facilitar revisión en el repo.
- Test evidences documentadas para sustituir placeholders por capturas reales en staging.
- Script de backup básico compatible con entornos Windows; debe ajustarse a rutas y políticas de la organización.

Siguientes pasos recomendados:
1. Ejecutar pruebas en entorno staging y reemplazar placeholders (`docs/test_evidences/screenshots/*`).
2. Revisar y adaptar `ops/backup.ps1` a credenciales seguras y ubicación de backups.
3. Confirmar si desea que genere screenshots de muestra y archivos de reporte (pytest output) y procederé a generarlos o adjuntarlos.
