"""Configuración mínima del proyecto Django para desarrollo local."""
import os
from pathlib import Path
import dj_database_url

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno desde .env si el archivo existe
for env_path in [BASE_DIR / '.env', BASE_DIR.parent / '.env']:
    if env_path.exists():
        with env_path.open(encoding='utf-8') as env_file:
            for line in env_file:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value

# Seguridad: usar variables de entorno en producción
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cambiar-esta-clave-por-una-segura')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Contraseña por defecto para registros / restablecimientos.
# En producción, configure DEFAULT_PASSWORD en el entorno y no la deje en el código.
DEFAULT_PASSWORD = os.environ.get('DEFAULT_PASSWORD', 'SGPR2026*')

# Hosts permitidos (en producción configure la URL/host real)
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost 127.0.0.1').split()

# Aplicaciones instaladas (mínimas)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion_permisos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'gestion_permisos.middleware.PasswordResetRequiredMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sgpr_alquitrana.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sgpr_alquitrana.wsgi.application'

# Base de datos: SQLite para simplificar el arranque
DATABASES = {}
# Si existe la variable DATABASE_URL la usamos (Postgres en despliegue), si no usamos sqlite local
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

# Internacionalización
LANGUAGE_CODE = 'es-ve'
TIME_ZONE = 'America/Caracas'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estáticos y media
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# WhiteNoise: archivos estáticos comprimidos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Simple configuración de login
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# Email: usar backend SMTP si se proporciona EMAIL_HOST; si no, usar consola.
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'no-reply@localhost')
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
if EMAIL_HOST:
    EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
else:
    # En entornos sin servidor SMTP configurado, imprimimos correos en consola.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
