# Manual de Respaldo y Restauración - SGPR

## Objetivo
Describir procedimientos para respaldar y restaurar la base de datos y archivos esenciales de la aplicación.

## Respaldos (PostgreSQL)
- Backup completo diario (ejemplo):
  pg_dump -U <user> -h <host> -F c -b -v -f "/backups/sgpr-$(date +%F).dump" <dbname>
- Copiar carpeta `media/` (adjuntos) a almacenamiento seguro.
- Recomendar retención mínima: 7 días; rotación semanal para almacenamiento a largo plazo.

## Restauración
- Crear base de datos destino y usuario con permisos.
- Restaurar dump:
  pg_restore -U <user> -d <dbname> "/backups/sgpr-<fecha>.dump"
- Restaurar archivos `media/` desde copia.

## Verificación post-restauración
- Ejecutar migraciones si fuese necesario.
- Crear superuser y comprobar acceso.
- Realizar pruebas funcionales básicas: login, listado de trabajadores y solicitudes.

## Automatización (ejemplo de script)
- `/ops/backup.sh` (ejemplo):
  #!/bin/bash
  TIMESTAMP=$(date +"%F")
  pg_dump -U $DB_USER -h $DB_HOST -F c -b -v -f "/backups/sgpr-$TIMESTAMP.dump" $DB_NAME
  rsync -avz /srv/sgpr/media /backups/media-$TIMESTAMP

## Consideraciones de seguridad
- Encriptar backups en reposo.
- Restringir acceso a carpetas de backups mediante permisos de sistema.

---

*Fin del Manual de Respaldo y Restauración.*
