# Manual de Implantación - SGPR

## Objetivo
Este manual describe los pasos para desplegar la aplicación SGPR en un entorno servidor o de desarrollo de manera manual.

## Requisitos previos
- Sistema operativo: Linux (recomendado) o Windows con WSL2.
- Java (opcional para PlantUML si se quiere generar diagramas).
- PostgreSQL (en producción) o SQLite (desarrollo).

## Variables de entorno importantes
- DJANGO_SECRET_KEY
- DATABASE_URL (ejemplo: postgres://user:pass@db:5432/sgpr)
- DJANGO_DEBUG (False en producción)
- EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD (si se envían correos)

## Preparar la máquina
1. Clonar repositorio:
   git clone <repo> && cd SGPR
2. Copiar archivo de ejemplo `.env.example` a `.env` y editar variables.

## Despliegue en servidor (recomendado)

Se recomienda desplegar con un servidor de aplicaciones (p. ej. Gunicorn) y un proxy inverso (Nginx). Pasos resumidos:

1. Crear y activar entorno virtual en el servidor:
   python -m venv .venv
   source .venv/bin/activate
2. Instalar dependencias:
   pip install -r requirements.txt
3. Configurar variables de entorno (DJANGO_SECRET_KEY, DATABASE_URL, FERNET_KEY, etc.)
4. Ejecutar migraciones:
   python manage.py migrate
5. Recolectar archivos estáticos:
   python manage.py collectstatic --noinput
6. Configurar Gunicorn como servicio systemd (ejemplo `sgpr.service`) y Nginx como proxy inverso.
7. Verificar logs con `journalctl -u sgpr.service -f` y probar acceso vía Nginx.

## Despliegue manual
1. Crear entorno virtual Python 3.11+:
   python -m venv .venv
   .venv\Scripts\activate (Windows) / source .venv/bin/activate (Linux)
2. Instalar dependencias:
   pip install -r requirements.txt
3. Configurar variables de entorno o `settings_local.py`.
4. Ejecutar migraciones y crear superusuario.
5. Ejecutar servidor:
   python manage.py runserver 0.0.0.0:8000

## Generar ERD (opcional)
- Usar PlantUML:
  plantuml -tpng -o docs erd.puml
- O con plantuml.jar:
  java -jar plantuml.jar -tpng -o docs erd.puml

## Backups y restauración (resumen)
- Backup PostgreSQL:
  pg_dump -U <user> -h <host> -F c -b -v -f "/backups/sgpr-$(date +%F).dump" <dbname>
- Restaurar:
  pg_restore -U <user> -d <dbname> "/backups/sgpr-<fecha>.dump"

## Consideraciones de seguridad
- No versionar archivos `.env` con credenciales.
- Mantener DJANGO_DEBUG=False en producción.
- Configurar certificados HTTPS en el servidor web (Nginx/Traefik).

## Mantenimiento y actualizaciones
1. Para actualizar dependencias: revisar `requirements.txt` y ejecutar `pip install -r requirements.txt` en entorno controlado.
2. Migraciones de BD: siempre ejecutar `python manage.py migrate` y probar en entorno staging.

## Logs y monitoreo
- Revisar logs: `journalctl -u sgpr.service` si usa systemd.
- Configurar rotación de logs y alertas.

## Contacto
Equipo de soporte (persona responsable única). Incluir instrucciones de rollback y plan de contingencia en `/ops/`.

---

*Fin del Manual de Implantación.*
