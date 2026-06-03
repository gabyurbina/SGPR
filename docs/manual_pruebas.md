# Manual de Pruebas / QA - SGPR

## Propósito
Documentar casos de prueba y procedimientos para validar la funcionalidad y estabilidad del sistema.

## Tipos de pruebas
- Unitarias: validar modelos y validaciones.
- Integración: flujos completos (crear solicitud, aprobar, generar reportes).
- Manuales: verificación visual de UI y exportes.
- Regresión: ejecutar pruebas tras cambios críticos.

## Cómo ejecutar pruebas
- Unit tests Django:
  python manage.py test
- Pruebas manuales:
  - Crear distintas solicitudes con combinaciones de fechas.
  - Subir adjuntos válidos e inválidos.
  - Probar filtros del panel de estadísticas.
  - Generar PDF/XLSX y verificar que los datos y gráficos se muestren.

## Casos de prueba principales
1. Crear solicitud con fecha inicio > fecha fin (esperar error de validación).
2. Crear solicitud con adjunto .exe (debe rechazarse).
3. Crear solicitud y aprobarla; verificar auditoría.
4. Generar estadísticas con y sin filtros; verificar estado de botón PDF.
5. Forzar canvas tainted (ejemplo: cargar imagen cross-origin) y verificar que el backend genere el gráfico en PDF.

## Registro de incidentes
- Registrar paso a paso cómo reproducir, logs relevantes y tiempo.
- Priorizar bugs por severidad: crítica, alta, media, baja.

## Entregables de QA
- Informe de pruebas con resultados y evidencias (capturas, PDFs generados).
- Lista de bugs abiertos y su estado.

---

*Fin del Manual de Pruebas.*
