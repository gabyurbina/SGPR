# Manual para Mantenedores / Desarrolladores - SGPR

## Propósito
Guía técnica para mantenedores y desarrolladores que den soporte al código fuente, realicen mejoras y mantengan operativa la plataforma.

## Estructura del proyecto
- `sgpr_alquitrana/` — aplicación Django principal (models, views, templates, static)
- `templates/` — plantillas HTML
- `static/` — CSS, JS, imágenes
- `docs/` — documentación, manuales y actas
- Instrucciones de despliegue en servidor (Gunicorn + Nginx) — despliegue
- `requirements.txt` — dependencias Python

## Flujo de desarrollo
1. Crear rama feature: `git checkout -b feature/descripcion`
2. Implementar y agregar tests.
3. Ejecutar pruebas locales: `pytest` o `python manage.py test`.
4. Hacer PR y revisar cambios (en este caso, la responsable única hace merge tras pruebas).

## Dependencias y entorno
- Python 3.11+
- Recomendado usar virtualenv
- Mantener `requirements.txt` actualizado

## Ejecutar tests
- Unit tests: `python manage.py test`
- Pruebas de integración manuales para exportes (PDF/XLSX)

## Migraciones de base de datos
1. Crear migración: `python manage.py makemigrations`
2. Aplicar migración: `python manage.py migrate`
3. Revisar cambios y ejecutar pruebas.

## Control de versiones y release
- Etiquetar versiones: `git tag -a vX.Y -m "Release X.Y"`
- Crear changelog con cambios relevantes.

## Manejo de errores y debugging
- Revisar logs: `journalctl -u sgpr.service` o `python manage.py runserver` para reproducciones locales.
- Habilitar logging DEBUG sólo en entornos de desarrollo.

## Tareas de mantenimiento rutinarias
- Actualizar dependencias trimestralmente.
- Revisar backups diarios y verificar restauraciones periódicas.
- Ejecutar pruebas de regresión después de upgrades de dependencias.

## Despliegue de parches urgentes
1. Crear rama hotfix desde main.
2. Aplicar cambios mínimos y testear en staging.
3. Migraciones: revisar impacto antes de ejecutar en producción.
4. Desplegar y monitorear.

## Documentación técnica adicional
- Añadir documentación de nuevas APIs en `/docs/api.md`.
- Mantener comentarios en español en el código.

---

*Fin del Manual para Mantenedores.*
