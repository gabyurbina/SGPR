# Product Backlog - SGPR (Priorizado)

## Épica: Gestión de Trabajadores
Objetivo: registrar y administrar la información del personal, vinculándola al sistema Django para controlar permisos, roles y reportes.

- US-101: Registrar trabajador
  - Como administrador del sistema, deseo registrar un trabajador con datos personales y usuario asociado, para disponer de una base de personal actualizada.
  - Criterios de aceptación:
    1. El formulario solicita nombre, cédula, cargo, teléfono, correo y usuario Django.
    2. La cédula es única y su formato es validado.
    3. Al guardar, el trabajador queda disponible en el listado.
  - Prioridad: Alta
  - Estimación: 5d
  - Dependencias: Ninguna
  - Sprint: 1
  - Estado: Planificado

- US-102: Editar datos de trabajador
  - Como administrador del sistema, deseo editar la información de un trabajador existente, para corregir datos o actualizar su cargo.
  - Criterios de aceptación:
    1. El administrador puede cambiar nombre, cargo, teléfono y correo.
    2. El formulario conserva la cédula inmutable si ya existe.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-101
  - Sprint: 1
  - Estado: Planificado

- US-103: Asociar trabajador a usuario Django
  - Como administrador del sistema, deseo vincular un trabajador con un usuario Django, para controlar acceso a solicitudes y perfiles.
  - Criterios de aceptación:
    1. Se puede asociar un trabajador a un usuario existente.
    2. No se permite asignar un usuario a más de un trabajador.
  - Prioridad: Media
  - Estimación: 2d
  - Dependencias: US-101
  - Sprint: 2
  - Estado: Planificado

- US-104: Listar y buscar trabajadores
  - Como administrador del sistema, deseo ver un listado filtrable de trabajadores, para encontrar rápidamente registros por nombre, cédula o cargo.
  - Criterios de aceptación:
    1. El listado muestra nombre, cédula, cargo, estado y usuario asociado.
    2. Hay búsqueda por nombre, cédula y cargo.
  - Prioridad: Media
  - Estimación: 3d
  - Dependencias: US-101
  - Sprint: 2
  - Estado: Planificado

## Épica: Solicitudes
Objetivo: permitir crear, validar, gestionar y auditar solicitudes de permiso o reposo con cálculos automáticos y adjuntos.

- US-201: Crear solicitud de permiso/repo
  - Como trabajador, deseo crear una solicitud con fechas, tipo, motivo y adjunto, para tramitar mi permiso en la Fundación.
  - Criterios de aceptación:
    1. El formulario guarda fecha de inicio, fin, tipo, motivo y archivo adjunto.
    2. Se valida que fecha de inicio ≤ fecha de fin.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-101
  - Sprint: 2
  - Estado: Planificado

- US-202: Validar fechas y calcular días
  - Como trabajador, deseo que el sistema calcule días_continuos y dias_laborables automáticamente, para saber el alcance real de mi permiso.
  - Criterios de aceptación:
    1. El sistema calcula días_continuos como diferencia inclusive.
    2. El sistema excluye sábados, domingos y feriados para dias_laborables.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-201
  - Sprint: 2
  - Estado: Planificado

- US-203: Adjuntar archivos a la solicitud
  - Como trabajador, deseo adjuntar comprobantes o documentos al crear mi solicitud, para respaldar mi motivo.
  - Criterios de aceptación:
    1. El formulario permite cargar un archivo por solicitud.
    2. Solo se aceptan extensiones permitidas y tamaño máximo configurado.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-201
  - Sprint: 3
  - Estado: Planificado

- US-204: Ver detalle y estado de solicitud
  - Como trabajador, deseo ver el detalle de mi solicitud, su estado y observaciones, para saber el resultado del trámite.
  - Criterios de aceptación:
    1. La vista muestra todos los campos, adjunto y estado de la solicitud.
    2. El estado puede ser Pendiente, Aprobado o Rechazado.
  - Prioridad: Media
  - Estimación: 3d
  - Dependencias: US-201
  - Sprint: 3
  - Estado: Planificado

- US-205: Aprobar o rechazar solicitud con observaciones
  - Como Recursos Humanos, deseo aprobar o rechazar solicitudes con comentarios, para comunicar la decisión y dejar evidencia.
  - Criterios de aceptación:
    1. Recursos Humanos puede cambiar el estado de una solicitud.
    2. Debe agregar una observación al aprobar o rechazar.
  - Prioridad: Alta
  - Estimación: 4d
  - Dependencias: US-204, US-401
  - Sprint: 4
  - Estado: Planificado

## Épica: Reportes y Estadísticas
Objetivo: entregar métricas y reportes visuales que faciliten el análisis de permisos y desempeño.

- US-301: Panel de estadísticas filtrable
  - Como Recursos Humanos, deseo ver gráficos de solicitudes por tipo, estado y periodo, para tomar decisiones informadas.
  - Criterios de aceptación:
    1. El panel muestra gráficos de barras y pastel con datos reales.
    2. Permite filtrar por rango de fechas, tipo de solicitud y trabajador.
  - Prioridad: Alta
  - Estimación: 4d
  - Dependencias: US-201, US-204
  - Sprint: 3
  - Estado: Planificado

- US-302: Exportar estadísticas a PDF
  - Como Recursos Humanos, deseo exportar el panel de estadísticas a PDF, para compartir informes oficiales.
  - Criterios de aceptación:
    1. El PDF incluye tablas de resumen e imágenes de los gráficos.
    2. Si la captura cliente falla, se genera el gráfico en servidor.
  - Prioridad: Alta
  - Estimación: 4d
  - Dependencias: US-301
  - Sprint: 4
  - Estado: Planificado

- US-303: Exportar solicitudes a XLSX
  - Como Recursos Humanos, deseo exportar un listado de solicitudes a XLSX, para análisis externo y archivo.
  - Criterios de aceptación:
    1. El archivo XLSX incluye filas con datos clave de cada solicitud.
    2. Se pueden aplicar los mismos filtros del panel antes de exportar.
  - Prioridad: Media
  - Estimación: 3d
  - Dependencias: US-301
  - Sprint: 4
  - Estado: Planificado

## Épica: Auditoría y Seguridad
Objetivo: garantizar trazabilidad, confidencialidad e integridad de acciones críticas.

- US-401: Registrar acciones críticas en auditoría
  - Como auditor interno, deseo una bitácora de aprobaciones, rechazos, ediciones y eliminaciones, para contar con evidencia confiable.
  - Criterios de aceptación:
    1. Cada evento crítico se guarda con usuario, fecha, tabla y acción.
    2. Los detalles sensibles se cifran en la base de datos.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-201, US-205
  - Sprint: 5
  - Estado: Planificado

- US-402: Buscar auditoría por usuario/tabla/fecha
  - Como auditor interno, deseo filtrar registros de auditoría por usuario, tabla y fecha, para investigar incidentes eficientemente.
  - Criterios de aceptación:
    1. La interfaz permite ingresar criterios de búsqueda.
    2. Solo usuarios autorizados acceden al módulo.
  - Prioridad: Media
  - Estimación: 2d
  - Dependencias: US-401
  - Sprint: 5
  - Estado: Planificado

- US-403: Cifrar campos sensibles en base de datos
  - Como auditor interno, deseo que datos sensibles como cédula y motivo queden cifrados, para proteger la información personal.
  - Criterios de aceptación:
    1. Los campos sensibles se almacenan usando EncryptedTextField o equivalente.
    2. Las vistas autorizadas desencriptan los datos correctamente.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-201, US-401
  - Sprint: 5
  - Estado: Planificado

## Épica: Infraestructura y Operación
Objetivo: asegurar despliegues, respaldos y documentación para operación estable.

- US-501: Backup y restauración automatizada
  - Como equipo de soporte, deseo un procedimiento de backup y restauración, para proteger los datos y recuperarlos ante fallos.
  - Criterios de aceptación:
    1. Existe script o tarea documentada para backup de base de datos.
    2. Existe procedimiento de restauración paso a paso.
  - Prioridad: Media
  - Estimación: 3d
  - Dependencias: US-503
  - Sprint: 6
  - Estado: Planificado

- US-502: Despliegue reproducible Gunicorn + Nginx
  - Como equipo de soporte, deseo una configuración de despliegue reproducible, para instalar el sistema en producción con seguridad y estabilidad.
  - Criterios de aceptación:
    1. La aplicación se puede levantar con Gunicorn.
    2. Nginx actúa como proxy inverso con configuraciones de seguridad.
  - Prioridad: Alta
  - Estimación: 2d
  - Dependencias: US-503
  - Sprint: 6
  - Estado: Planificado

- US-503: Documentar manuales de usuario e implementación
  - Como equipo de soporte, deseo documentación clara de uso, instalación y respaldo, para entregar el sistema con guía completa.
  - Criterios de aceptación:
    1. Existen manuales de usuario y de implementación.
    2. La documentación incluye pasos de instalación, backups y restauración.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: Ninguna
  - Sprint: 6
  - Estado: Planificado
