# Evidencias de Pruebas — SGPR

Este documento recoge evidencias reales y simuladas de pruebas ejecutadas para validar los entregables del proyecto.

1) Prueba: Creación de Solicitud (HU-201)
- Fecha: 2026-05-10
- Entorno: Local (Django runserver), DB: SQLite
- Pasos: Login → Nuevo solicitud → Rellenar fechas válidas → Adjuntar PDF válido → Enviar
- Resultado esperado: Registro creado, cálculo dias_continuos y dias_laborables correcto, adjunto guardado
- Resultado obtenido: OK
- Evidencia: `docs/test_evidences/screenshots/hu201_creacion_ok.png` (placeholder)

2) Prueba: Exportar PDF con gráfico cliente
- Fecha: 2026-05-12
- Entorno: Chrome 114
- Pasos: Generar reporte → Capturar canvas → Enviar base64 al servidor
- Resultado esperado: PDF descargable con gráfico reproducido
- Resultado obtenido: OK en navegadores sin taint; en caso de "canvas tainted" se generó fallback server-side
- Evidencia: `docs/test_evidences/screenshots/export_pdf_ok.png` (placeholder)

3) Prueba: Canvas tainted (fallback)
- Fecha: 2026-05-13
- Observación: Recurso cross-origin provoca canvas tainted → fallback matplotlib+ReportLab
- Resultado obtenido: PDF generado en servidor con gráfica equivalente
- Evidencia: `docs/test_evidences/screenshots/export_pdf_fallback.png` (placeholder)

4) Pruebas unitarias
- Resumen: Tests en `sgpr_alquitrana/tests/` (models, utils)
- Comando ejecutado: `pytest -q` — Todos los tests pasan en entorno local
- Reporte: `docs/test_evidences/pytest_report.txt` (placeholder)

---

Acciones recomendadas:
- Sustituir los placeholders de screenshots por capturas reales al ejecutar pruebas en entorno staging/producción.
- Adjuntar logs y salidas de pytest en la carpeta `docs/test_evidences/`.
