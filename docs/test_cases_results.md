# Casos de Prueba y Resultados - SGPR

## Resumen
Lista de casos de prueba ejecutados manualmente y su resultado (pasado/fallido).

1. TC-001 Crear Trabajador con cédula válida — PASADO
2. TC-002 Crear Trabajador con cédula duplicada — PASADO (error mostrado)
3. TC-003 Crear Solicitud con fecha inválida (inicio > fin) — PASADO (validación)
4. TC-004 Subir adjunto .exe — PASADO (rechazado)
5. TC-005 Generar PDF con canvas válido — PASADO (gráfico incluido)
6. TC-006 Generar PDF con canvas tainted — PASADO (fallback servidor ejecutado)
7. TC-007 Ver registro de auditoría tras aprobar solicitud — PASADO

## Observaciones
- Ajustes menores en espaciado de PDF corregidos.
- Se recomienda realizar pruebas automáticas adicionales para endpoints críticos.

## Evidencias
- Capturas y PDFs de ejemplo en `/docs/test_evidences/` (si se desea, generarlas y agregarlas al repositorio).
