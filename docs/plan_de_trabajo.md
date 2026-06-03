# Plan de Trabajo - SGPR

## Visión del documento
Plan de trabajo detallado: visión, abordaje, factores críticos de éxito, restricciones, dependencias, alcance, actividades, recursos y riesgos.

## Visión y abordaje
Visión: Entregar un sistema estable y documentado para la gestión de permisos y reportes.
Abordaje: Desarrollo incremental con sprints de 2 semanas; entregas iterativas y validación con stakeholders.

## Factores críticos de éxito
- Entregas incrementales funcionando en entorno de pruebas.
- Captura fiable de gráficos en exportes.
- Cifrado correcto de datos sensibles.

## Restricciones
- Un único desarrollador (limitación de recursos).
- Dependencia en tiempo de disponibilidad del cliente para validaciones.

## Dependencias
- Infraestructura (DB, servidor)
- Certificados TLS para producción

## Alcance
Ver sección "Alcance" en documento principal.

## Cronograma de actividades (resumen)
- Implementación modelos y CRUD (2 semanas)
- Estadísticas y exportes (3 semanas)
- Auditoría y seguridad (2 semanas)
- Despliegue y pruebas finales (2 semanas)

## Recursos
- 1 Desarrollador (responsable único)
- Servidor para despliegue

## Riesgos y mitigaciones
- Riesgo: Canvas tainted -> Mitigación: generar fallback en servidor
- Riesgo: Sobrecarga por exportes -> Mitigación: offload a workers


