# Historias de Usuario Detalladas - SGPR

A continuación se documentan las historias de usuario principales con su flujo, excepciones y criterios de aceptación.

## HU-001: Registrar Trabajador
- Actor: Administrador / Recursos Humanos
- Precondición: Usuario admin autenticado
- Flujo principal:
  1. Ir a "Trabajadores → Nuevo".
  2. Completar cedula, nombres, apellidos, cargo, departamento, email.
  3. Enviar formulario.
  4. Sistema valida unicidad de cédula y correo.
  5. Se crea User y Trabajador, se cifra cedula en cedula_encrypted.
- Excepciones:
  - Cédula duplicada → error y no guarda.
  - Correo inválido → error de validación.
- Postcondición: Trabajador creado y accesible en el listado.
- Criterios de aceptación:
  - Se debe poder buscar trabajador por cédula.

## HU-002: Crear Solicitud de Permiso/Reposo
- Actor: Trabajador (o admin en representación)
- Precondición: Trabajador existente y autenticado
- Flujo principal:
  1. Abrir formulario "Nueva Solicitud".
  2. Ingresar tipo, fecha_inicio, fecha_fin, motivo, adjuntar justificante (opcional).
  3. Enviar.
  4. Sistema valida fechas (inicio ≤ fin), calcula dias_continuos y dias_laborables, valida adjunto.
  5. Guarda solicitud en estado PENDIENTE.
- Excepciones:
  - Fecha inválida → mostrar error.
  - Adjunto no permitido → rechazar.
- Postcondición: Solicitud registrada; notificación al revisor si aplica.
- Criterios de aceptación:
  - Cálculo de días correcto según feriados y fines de semana.

## HU-003: Revisar y Aprobar/Rechazar Solicitud
- Actor: Revisor / Administrador
- Precondición: Solicitud en estado PENDIENTE
- Flujo principal:
  1. Filtrar solicitudes pendientes.
  2. Seleccionar solicitud y revisar información y adjunto.
  3. Elegir Aprobar o Rechazar y opcionalmente añadir observaciones.
  4. Sistema registra acción en Auditoría.
- Excepciones: Solicitud ya procesada → no mostrar botones de acción.
- Postcondición: Estado actualizado y registro de auditoría.

## HU-004: Ver Estadísticas y Exportar
- Actor: Administrador / RRHH
- Precondición: Datos en sistema
- Flujo principal:
  1. Ir al panel "Estadísticas".
  2. Aplicar filtros (fechas, trabajador, tipo).
  3. Visualizar gráficos; si se desea exportar, presionar "Exportar PDF" o "Exportar XLSX".
  4. Si exporta PDF, cliente intenta capturar canvas; si falla, servidor genera gráfico con datos.
- Excepciones: Sin filtros aplicados → botón PDF deshabilitado (según requisito).
- Criterios de aceptación: El PDF/XLSX debe incluir datos tabulares y gráfico visible.

## HU-005: Consultar Auditoría
- Actor: Auditoría interna / Admin
- Precondición: Permiso para ver auditoría
- Flujo: Filtrar por usuario, tabla o fecha; visualizar detalles desencriptados según permisos.


# Fin de Historias de Usuario
