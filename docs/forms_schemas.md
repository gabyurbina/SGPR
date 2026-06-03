# Esquemas de Formularios Digitales - SGPR

Documentación técnica de formularios (campos, tipos y validaciones).

## Formulario: Trabajador
- cedula: string, requerido, maxLength=15, unique, pattern: dígitos
- nombres: string, requerido, maxLength=100
- apellidos: string, requerido, maxLength=100
- cargo: string, requerido, maxLength=100
- departamento: string, opcional, maxLength=100
- email: string, requerido, formato email
- password_reset_required: boolean, default false

Validaciones server-side y client-side: todos los campos requeridos, cedula única y email válido.

## Formulario: Solicitud
- trabajador_id: integer, requerido (select)
- tipo: enum ['PERMISO','REPOSO','PERMISO_CUIDO_MATERNO','PERMISO_CUIDO_PATERNO','PERMISO_DEPORTIVO','INASISTENCIA_INJUSTIFICADA','INASISTENCIA_JUSTIFICADA']
- fecha_inicio: date, requerido
- fecha_fin: date, requerido
- motivo: text, requerido, encrypted at rest
- adjunto: file, opcional, aceptados: .pdf, .png, .jpg, .jpeg, max_size=5MB

Validaciones adicionales:
- fecha_inicio <= fecha_fin
- calcular dias_continuos = (fecha_fin - fecha_inicio) + 1
- calcular dias_laborables excluyendo fines de semana y feriados

## Esquema JSON de ejemplo (Solicitud)
{
  "trabajador_id": 123,
  "tipo": "PERMISO",
  "fecha_inicio": "2026-06-01",
  "fecha_fin": "2026-06-03",
  "motivo": "Cuidado médico",
  "adjunto": <binary>
}

## Recomendación
Implementar validaciones tanto en frontend (UX) como server-side para garantizar seguridad y consistencia.
