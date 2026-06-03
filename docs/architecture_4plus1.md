# Arquitectura 4+1 del Sistema SGPR

Este documento presenta las cinco vistas de arquitectura (4+1) de la solución: Vistas Lógica, Desarrollo, Proceso, Física y Escenarios.

## Visión general
Tecnologías principales: Django (Python), PostgreSQL (producción), SQLite (desarrollo), Chart.js (frontend), ReportLab/Pillow/matplotlib (generación de PDFs). Despliegue recomendado: Gunicorn + Nginx.

---

## Vista Lógica (Logical View)
- Componentes principales:
  - Módulo Trabajadores (modelos, formularios)
  - Módulo Solicitudes (lógica de negocio, cálculo de días)
  - Módulo Estadísticas (recolección de datos, endpoint JSON, generación de gráficos)
  - Módulo Auditoría (registro de acciones, EncryptedTextField)
  - Módulo Exportes (captura canvas, fallback matplotlib, generación PDF/XLSX)
- Responsabilidades y relaciones: los controladores (views) coordinan entre modelos y templates; servicios utilitarios realizan cifrado y generación de reportes.

---

## Vista de Desarrollo (Development View)
- Organización del código:
  - `sgpr_alquitrana/` (app principal)
    - `models.py` (Trabajador, Solicitud, Auditoria)
    - `views.py` (endpoints web y export)
    - `templates/` (estadisticas, lista_trabajadores, etc.)
    - `static/` (JS Chart.js wrappers, CSS)
- Paquetes y dependencias: requirements.txt (Django, Pillow, reportlab, matplotlib, psycopg2-binary, cryptography)

---

## Vista de Proceso (Process View)
- Flujo de ejecución clave:
  - Usuario solicita página estadísticas -> servidor devuelve HTML + JS (Chart.js) -> cliente renderiza canvas
  - Export PDF: cliente intenta canvas.toDataURL -> si éxito envía base64 al endpoint export/pdf -> servidor ensambla PDF y responde
  - Si canvas tainted -> cliente envía datos raw (series) -> servidor genera gráfico con matplotlib y ensambla PDF
- Tareas asíncronas y concurrencia: tareas de generación de PDF deben ser rápidas; para cargas largas considerar delegar a worker (Celery).

---

## Vista Física (Physical View)
- Despliegue en contenedores:
  - `web` (Django + Gunicorn / uWSGI)
  - `db` (PostgreSQL)
  - `nginx` (proxy y TLS)
- Volúmenes:
  - `/srv/sgpr/media` (archivos adjuntos)
  - `/backups` (dumps)

---

## Escenarios / Casos de uso (Use-case View)
1. Crear Solicitud: actor -> formulario -> validaciones -> persistencia.
2. Generar Reporte PDF: actor -> filtro -> render canvas -> capture/ fallback -> obtener PDF.
3. Auditoría: cualquier acción crítica crea un registro en Auditoria.

---

## Recomendaciones arquitectónicas
- Definir paleta de colores única y enviarla al backend para coherencia en exportes.
- Externalizar generación pesada (PDF grandes) a workers si se requiere concurrencia.
- Forzar políticas de CORS en recursos externos para evitar canvas tainted.


