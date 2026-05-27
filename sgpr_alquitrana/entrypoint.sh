#!/bin/sh
set -e

# Espera por la BD y aplica migraciones, luego collectstatic
echo "Esperando la base de datos..."
sleep 3

# Ejecutar migraciones
python manage.py migrate --noinput

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

exec "$@"
