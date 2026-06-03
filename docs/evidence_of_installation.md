# Evidencia de Instalación y Puesta en Producción - SGPR

## Estado actual
- Entorno de desarrollo: probado localmente con `python manage.py runserver`.
- Entorno de producción: se proporcionan ejemplos de unit file systemd y configuración Nginx en `/ops/`.

## Pasos realizados (sugeridos para cliente)
1. Transferir código a servidor: `git clone` o despliegue por CI.
2. Crear entorno virtual y activar.
3. Instalar dependencias.
4. Configurar variables de entorno (DJANGO_SECRET_KEY, DATABASE_URL, FERNET_KEY).
5. Ejecutar migraciones y collectstatic.
6. Configurar y habilitar `sgpr.service` (systemd) y Nginx.

## Evidencias (a completar por quien instale)
- Fecha de despliegue:
- Servidor/host:
- Capturas de pantalla de la aplicación en producción:
- Logs de verificación (journalctl, nginx):

(Agregar archivos de evidencia en `/docs/test_evidences/`).
