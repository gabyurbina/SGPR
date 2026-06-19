# Sprint Backlog — Sprint 5 (27/05 — 09/06)

## Objetivo del sprint
Habilitar auditoría, seguridad y cifrado de datos sensibles.

## Historias y tareas incluidas
- US-401: Registrar acciones críticas en auditoría
  - Prioridad: Alta
  - Estimación: 3d
  - Estado: Por hacer
  - Dependencias: US-201, US-205
  - Comentarios: Aprovechar modelo de Auditoría existente.

- US-402: Buscar auditoría por usuario/tabla/fecha
  - Prioridad: Media
  - Estimación: 2d
  - Estado: Por hacer
  - Dependencias: US-401
  - Comentarios: Definir permisos concretos de acceso.

- US-403: Cifrar campos sensibles en base de datos
  - Prioridad: Alta
  - Estimación: 3d
  - Estado: Por hacer
  - Dependencias: US-201, US-401
  - Comentarios: Revisar configuración de FERNET_KEY.

- Tarea: Revisar configuración de `FERNET_KEY` y variables de entorno
  - Estimación: 1d
  - Estado: Por hacer

## Dependencias
- US-201, US-205

## Responsable
Desarrolladora principal
