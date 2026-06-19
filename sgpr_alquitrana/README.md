# SGPR - Sistema de Gestión de Permisos y Reposos

*Aplicación Django para gestionar las solicitudes de permisos y reposos del personal, con control de usuarios, auditoría y exportación de reportes.

---

## Contenido

> Nota: no existe un archivo `readme.py` en este proyecto. La documentación principal se mantiene en `README.md`.

- [Requisitos](#requisitos)
- [Instalación local](#instalaci%C3%B3n-local)
- [Variables de entorno](#variables-de-entorno)
- [Ejecutar el proyecto](#ejecutar-el-proyecto)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Rutas principales](#rutas-principales)
- [Flujo de uso](#flujo-de-uso)
- [Notas de desarrollo](#notas-de-desarrollo)

---

## Requisitos

- Python 3.10+ (recomendado)
- pip
- SQLite (predeterminado) o PostgreSQL si se configura `DATABASE_URL`
- Node/NPM no son necesarios para correr el backend básico

---

## Instalación local

1. Clona el repositorio o copia el proyecto en tu máquina.

2. En la carpeta raíz del proyecto (`sgpr_alquitrana`), crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Si quieres, copia el ejemplo de variables de entorno:

   ```bash
   copy .env.example .env
   ```

---

## Variables de entorno

El proyecto carga algunos valores desde variables de entorno. Los valores predeterminados son seguros para desarrollo local.

- `DJANGO_SECRET_KEY`: clave secreta de Django.
- `DJANGO_DEBUG`: `True` o `False`.
- `DJANGO_ALLOWED_HOSTS`: hosts permitidos separados por espacios.
- `DATABASE_URL`: si se define, el proyecto usará esa base de datos en lugar de SQLite.
- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS`, `EMAIL_BACKEND`: para envío de correos.
- `DEFAULT_FROM_EMAIL`: emisor del correo.
- `FERNET_KEY`: clave para cifrado y descifrado de campos sensibles en la base de datos (`Auditoria.detalles`, `Solicitud.motivo`, `Trabajador.cedula_encrypted`).

Para generar una clave segura, usa:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Si `EMAIL_HOST` no está configurado, el sistema usa el backend de consola (`console.EmailBackend`) y el correo se imprimirá en la terminal en lugar de enviarse realmente.

El proyecto también carga automáticamente un archivo `.env` en la raíz del proyecto si existe.

---

## Ejecutar el proyecto

1. Ejecuta migraciones:

   ```bash
   python manage.py migrate
   ```

2. Crea un superusuario si lo deseas:

   ```bash
   python manage.py createsuperuser
   ```

3. Levanta el servidor:

   ```bash
   python manage.py runserver
   ```

4. Accede a la aplicación en:

   ```
   http://127.0.0.1:8000/
   ```

---

## Estructura del proyecto

- `manage.py`: comando principal para ejecutar Django.
- `requirements.txt`: dependencias del proyecto.
- `sgpr_alquitrana/`: configuración principal de Django.
  - `settings.py`: configuración de base, rutas, base de datos y correo.
  - `urls.py`: rutas globales del proyecto.
- `gestion_permisos/`: aplicación principal.
  - `models.py`: definición de los modelos `Trabajador`, `Solicitud` y `Auditoria`.
  - `views.py`: lógica del flujo principal y vistas.
  - `forms.py`: formularios de validación y presentación de datos.
  - `urls.py`: rutas internas de la aplicación.
  - `middleware.py`: middleware para obligar cambio de contraseña cuando sea necesario.
- `templates/`: plantillas HTML que renderiza Django.
- `static/`: archivos estáticos CSS, imágenes y recursos.
- `media/`: archivos subidos por los usuarios (adjuntos).

---

## Rutas principales

| Ruta | Qué ofrece |
| `/login/` | Login para todos los usuarios |
| `/logout/` | Cerrar sesión |
| `/` | Panel de solicitudes |
| `/registro/` | Registro de trabajador |
| `/solicitar/` | Envío de solicitud de permiso/repo |
| `/cambiar-contrasena/` | Cambio de contraseña |
| `/trabajadores/` | Listado de trabajadores (admin) |
| `/auditoria/` | Reporte de auditoría (admin) |
| `/trabajadores/descargar/xlsx/` | Exportar trabajadores a Excel |
| `/trabajadores/descargar/pdf/` | Exportar trabajadores a PDF |
| `/auditoria/descargar/xlsx/` | Exportar auditoría a Excel |
| `/auditoria/descargar/pdf/` | Exportar auditoría a PDF |
| `/api/trabajadores/registro/` | API JSON para registrar un trabajador |

---

## API de registro de trabajadores

La aplicación ahora expone una API simple para crear trabajadores desde un cliente JSON. Esta API registra al trabajador, crea el usuario `username=cedula`, utiliza `DEFAULT_PASSWORD` como contraseña inicial y la muestra en pantalla.

- Método: `POST`
- URL: `/api/trabajadores/registro/`
- Payload JSON:
  - `cedula`
  - `nombres`
  - `apellidos`
  - `cargo`
  - `departamento`
  - `email`

> Nota: el API valida que no exista ya un usuario con la misma cédula ni con el mismo correo electrónico.

Ejemplo:

```json
{
  "cedula": "12345678",
  "nombres": "Juan",
  "apellidos": "Pérez",
  "cargo": "Auxiliar",
  "departamento": "Gestión Humana",
  "email": "juan.perez@ejemplo.com"
}
```

---

## Flujo de uso

1. El usuario puede registrarse o iniciar sesión.
2. Un trabajador envía una solicitud con motivo y adjunto.
3. Gestión Humana revisa la solicitud:
   - Aprueba o rechaza con observaciones.
   - El botón de aprobar/rechazar no aparece si la solicitud ya está procesada.
4. Todas las acciones importantes se guardan en la tabla de auditoría.
5. El personal autorizado puede descargar reportes XLSX/PDF.

---

## Notas de desarrollo

- La validación de archivos limita a 5MB y solo permite PDF e imágenes.
- El campo `adjunto` se guarda en `media/justificantes/`.
- El middleware obliga al primer cambio de contraseña para los trabajadores que reciben contraseña por defecto.
- El sistema usa SQLite local por defecto, pero puede apuntar a PostgreSQL con `DATABASE_URL`.

---

## Seguridad y despliegue en producción

Recomendaciones mínimas para asegurar la aplicación antes de exponerla a Internet:

- Coloca en variables de entorno (no en el código) las claves sensibles:
   - `DJANGO_SECRET_KEY` (obligatorio en producción)
   - `DATABASE_URL` (usar Postgres/managed DB en producción)
   - `EMAIL_HOST` / `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` si usas SMTP
   - `FERNET_KEY` (clave para cifrado de campos sensibles)

   Nota: por seguridad el sistema no muestra contraseñas por defecto en pantalla ni en mensajes. Configure `DEFAULT_PASSWORD` solo para entornos controlados.

- En `requirements.txt` se añadieron `cryptography` (cifrado de campos) y `argon2-cffi` (hasher opcional). Para usar Argon2, exporta `USE_ARGON2=True`.

- En `sgpr_alquitrana/settings.py` hay variables que se debe ajustar en producción:
   - `DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS` con los dominios/hosts donde se desplegará
   - `SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`, `SECURE_SSL_REDIRECT=True`
   - `SECURE_HSTS_SECONDS` (ej. `31536000`) y `SECURE_HSTS_INCLUDE_SUBDOMAINS=True` cuando uses HTTPS

- Genera una `FERNET_KEY` segura con:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Luego exporta la clave en la máquina/contendor que ejecute la app.

- Usa HTTPS para exponer la app (Nginx + Gunicorn o servicios administrados). No expongas directamente `runserver`.

- Recomendación de despliegue: configura variables en un `.env` y despliega con Gunicorn + Nginx; para desarrollo use `python manage.py runserver`.

---

---


---

## Comentarios para otros desarrolladores y o mantenedores de la aplicación

- Revisa `gestion_permisos/views.py` para entender el comportamiento principal.
- `gestion_permisos/forms.py` contiene validaciones clave de datos y archivos.
- `gestion_permisos/models.py` calcula días continuos y laborables dentro de `Solicitud`.
- `templates/base.html` administra el layout, el menú y los botones globales.
- Para agregar un nuevo informe, extiende las vistas y agrega una ruta en `gestion_permisos/urls.py`.