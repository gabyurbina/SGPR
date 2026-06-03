# Plan de Trabajo Detallado - SGPR (Extendido)

## Visión y abordaje
Visión: Entregar la plataforma SGPR completamente documentada y operativa en servidor.
Abordaje: Desarrollo incremental SCRUM con sprints de 2 semanas y entregas iterativas.

## Objetivos críticos
- Entregar módulo de Solicitudes con exportes funcionales.
- Garantizar trazabilidad mediante auditoría cifrada.

## Desglose de actividades (alto nivel)
- A1: Preparación del entorno y dependencias (2 días)
- A2: Modelado y migraciones (3 días)
- A3: Formularios y CRUD (5 días)
- A4: Estadísticas y exportes (10 días)
- A5: Auditoría y seguridad (5 días)
- A6: Pruebas y despliegue (8 días)

## Riesgos y mitigaciones
- Dependencia de un único desarrollador — mitigación: documentar pasos operativos y code comments.
- Canvas tainted — mitigación: fallback server-side y documentación de CORS.
- Payloads grandes en base64 — mitigación: recompress images client-side o limitar resoluciones.

## Recursos
- 1 Desarrollador (responsable única)
- Servidor para pruebas/producción

## Cronograma detallado
Ver `docs/cronograma_gantt.md` para vista por sprint. Este plan fue respetado durante el desarrollo.

## Criterios de finalización
- Todas las historias en el backlog Mínimo Producto Viable (MVP) resueltas.
- Documentación completa entregada.
- Plan de mantenimiento definido.

