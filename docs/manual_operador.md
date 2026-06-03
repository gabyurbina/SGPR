# Manual del Operador / Administrador - SGPR

## Propósito
Guía para operadores o administradores que realizan tareas diarias de operación y soporte.

## Tareas diarias
- Verificar que el servicio web esté levantado (e.g. `systemctl status sgpr.service` o `ps aux | grep gunicorn`).
- Revisar logs: `journalctl -u sgpr.service --since "1 hour ago"` o revisar los archivos de logs de Gunicorn/Nginx.
- Verificar colas y tareas programadas si se usan (Celery).
- Comprobar integridad de backups y espacio en disco.

## Gestión de usuarios
- Crear/editar usuarios desde la interfaz de administración de Django o CLI.
- Asignar permisos y roles adecuados.

## Gestión de backups
- Verificar que backups automáticos se ejecuten.
- Probar restauraciones en entorno de staging mensualmente.

## Respuesta ante incidentes
- Recolectar logs y tiempo aproximado del incidente.
- Reproducir en entorno de prueba.
- Aplicar rollback si el cambio produce fallos.

## Monitorización
- Configurar alertas para: servicio caído, errores 5xx repetidos, uso alto de CPU/RAM.

## Procedimiento de mantenimiento programado
- Planificar ventana de mantenimiento.
- Avisar a usuarios con antelación.
- Ejecutar migraciones y pruebas de verificación.

---

*Fin del Manual del Operador.*
