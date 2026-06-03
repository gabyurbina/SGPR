# Informe de Pruebas Consolidado - SGPR

## Resumen ejecutivo
Se realizaron pruebas unitarias y manuales sobre flujos críticos: creación de solicitudes, aprobación, exportes PDF/XLSX y auditoría.

## Casos probados
- Validaciones de fechas y adjuntos
- Exportes PDF con canvas válido y canvas tainted (fallback)
- Auditoría al aprobar/rechazar solicitudes

## Resultados
- Errores críticos: 0
- Errores menores: ajustes de formato en PDF (corregidos)

## Evidencias
- Carpeta `/docs/test_evidences/` (capturas y PDFs de ejemplo) — generar si se requiere.

## Recomendaciones
- Ejecutar pruebas en Chrome, Firefox y Edge; documentar diferencias.
