# Documento Completo del Proyecto - SGPR

**Proyecto:** Sistema de Gestión de Permisos y Reportes (SGPR)

**Desarrollado bajo:** Metodología SCRUM

**Responsable del desarrollo:** Gabriela Urbina (análisis, diseño, desarrollo, pruebas e implementación)

**Periodo del proyecto:** 01/04/2026 — 30/06/2026

---

## 1. Visión

Ser la plataforma de referencia para la gestión y control de permisos laborales en la Fundación Guardería Infantil """La Alquitrana""", ofreciendo reportes precisos, reportes confiables y controles de auditoría que faciliten la toma de decisiones y el cumplimiento normativo.

## 2. Misión

Proveer una aplicación web segura y fácil de usar que centralice la gestión de solicitudes de permisos y reposos, automatice cálculos de días laborables, genere reportes visuales y exportables, y mantenga trazabilidad de todas las acciones mediante auditoría.

## 3. Objetivo general

Diseñar, desarrollar e implementar un sistema que permita registrar, revisar y reportar solicitudes de permiso y reposo, garantizando integridad, confidencialidad y trazabilidad de la información.

## 4. Objetivos específicos

- Implementar modelos de datos para Trabajador, Solicitud y Auditoría con cifrado para campos sensibles.
- Desarrollar interfaces para registro y gestión de solicitudes.
- Incorporar visualización de estadísticas con Chart.js y exportes PDF que reproduzcan los gráficos.
- Registrar auditoría de acciones críticas y mantener logs seguros.

## 5. Propósito y justificación

Centralizar la gestión de permisos reduce errores administrativos, agiliza procesos y provee evidencia documental ante auditorías. El sistema sustituye procesos manuales y facilita la generación de reportes para la Oficina de Gestión Humana de la Fundación Guardería Infantil """La Alquitrana""".

## 6. Alcance del proyecto

Incluye:
- Módulo Trabajadores (perfil y vínculo con usuario Django).
- Módulo Solicitudes (creación, edición, validación, cálculo automático de días laborables y adjuntos).
- Panel de Estadísticas (gráficos, filtrado, exportes PDF).
- Módulo Auditoría (registro de acciones con detalles cifrados).
- Despliegue en servidor (configuración básica: Gunicorn + Nginx). 

## 7. Descripción del proyecto

Aplicación web desarrollada en Python con Django. Frontend con plantillas y Chart.js para gráficos. Exportes PDF intentan capturar el canvas cliente (canvas.toDataURL); si falla (canvas tainted) se genera gráfico en servidor con matplotlib y se ensambla el PDF con ReportLab y Pillow. Campos sensibles (ej. cédula, motivo) se almacenan cifrados usando EncryptedTextField.


## 8. Stakeholders (Interesados)

- Administrador del sistema (Lic. Marbella Canelón)
- Recursos Humanos (Francismar Marchan)
- Trabajadores (usuarios finales)
- Auditoría interna
- Equipo de soporte Alquitrana (Ing. Trino Vera)
- Desarrollo principal (Tsu. Gabriela Urbina)

## 8.1 Usuarios

- Administrador del sistema (Lic Marbella Canelón): responsable de la configuración, administración de roles y políticas.
- Recursos Humanos (Francismar Marchan): principal actor que gestiona solicitudes, aprobaciones y reportes.
- Trabajadores (usuarios finales): generan solicitudes de permisos y consultan su historial.
- Auditoría interna: revisa registros y asegura cumplimiento normativo.
- Equipo de soporte Alquitrana (Ing. Trino Vera): realiza acompañamiento como parte del equipo tecnológico de la Fundación.


## 8.2 Roles de los Interesados (Scrum)

- Product Owner: Administrador del sistema (Lic Marbella Canelón). Es el propietario del producto, define prioridades, valida requisitos y asegura que el desarrollo aporte valor al negocio.
- Scrum Master / Scrum Developer: Gabriela Urbina (desarrolladora principal). Facilita el proceso Scrum, elimina impedimentos, colabora en el desarrollo y entrega funcionalidad de acuerdo con los criterios aceptados.
- Development Team: Gabriela Urbina (desarrolladora principal). Construye, despliega y mantiene el producto, asegurando calidad, seguridad y continuidad.
- Stakeholders clave: Recursos Humanos (Francismar Marchan), Trabajadores (usuarios finales) y Auditoría interna. Proveen retroalimentación, validan requisitos y evalúan el cumplimiento de necesidades.

## 8.2.1 Medios de comunicación y relaciones de la desarrolladora principal

- Gabriela Urbina mantiene comunicación directa con el Product Owner (Lic Marbella Canelón) para alinear prioridades, entregar funcionalidades y resolver dudas de negocio.
- Se relaciona con Recursos Humanos para validar requisitos funcionales, revisar reportes y ajustar el flujo de solicitudes.
- Recibe acompañamiento del Equipo de soporte Alquitrana para consultas de despliegue, backups y resolución de incidencias técnicas.
- Colabora con la Auditoría interna para definir registros de trazabilidad, criterios de auditoría y protección de datos sensibles.
- También recibe retroalimentación indirecta de los Trabajadores (usuarios finales) a través de Recursos Humanos y pruebas de usuario, para mejorar la usabilidad y el flujo de solicitudes.

## 8.3 Intereses por Usuario

### Administrador del sistema
- Interés en mantener el sistema estable y seguro.
- Interés en tener control sobre permisos y accesos.
- Interés en automatizar tareas administrativas.

### Recursos Humanos
- Interés en agilizar la aprobación de solicitudes.
- Interés en obtener datos y reportes precisos para gestión de personal.
- Interés en reducir errores y tiempos de trámite.

### Trabajadores (usuarios finales)
- Interés en la transparencia del estado de sus permisos.
- Interés en un proceso simple para enviar solicitudes y adjuntos.
- Interés en recibir confirmaciones y tener acceso a su historial.

### Auditoría interna
- Interés en contar con registros completos y auditable.
- Interés en la integridad y confidencialidad de los datos.
- Interés en demostrar cumplimiento normativo.

### Equipo de soporte Alquitrana
- Interés en acompañar el despliegue y dar soporte consultivo.
- Interés en disponer de documentación clara y actualizada.
- Interés en apoyar la continuidad operacional sin asumir la ejecución directa.

## 8.3 Necesidades, Producto y Valor por Usuario

### Administrador del sistema
- Necesidades: gestionar usuarios, roles y permisos; monitorear salud del sistema; configurar backups y mantener seguridad.
- Producto: panel de administración, control de roles, logs operativos, herramientas de backup y configuración.
- Valor: reduce tiempo de administración, centraliza controles y minimiza errores de configuración.

### Recursos Humanos
- Necesidades: revisar y aprobar solicitudes; generar reportes por periodo y trabajador; acceder a históricos y métricas.
- Producto: interfaz de gestión de solicitudes, filtros avanzados en el panel de estadísticas y exporte PDF de informes.
- Valor: mayor eficiencia en la gestión, evidencia documental para decisiones y menor trabajo manual.

### Trabajadores (usuarios finales)
- Necesidades: crear solicitudes con adjuntos, conocer el estado y ver su historial personal de permisos.
- Producto: formularios simples y guiados, subida y descarga de adjuntos, vista de estado y notificaciones.
- Valor: transparencia en procesos, menor carga administrativa y acceso rápido a comprobantes.

### Auditoría interna
- Necesidades: acceder a registros de acciones, buscar por usuario/tabla/fecha y garantizar integridad de los datos.
- Producto: repositorio de auditoría con búsquedas, exportes y campos sensibles cifrados; controles de acceso restringido.
- Valor: cumplimiento normativo, capacidad de investigación y evidencia confiable ante auditorías.

### Equipo de soporte Alquitrana
- Necesidades: contar con información clara para acompañar despliegues y respaldos sin asumir la ejecución directa.
- Producto: documentación de despliegue (Gunicorn+Nginx), guías de backup y recomendaciones de monitoreo.
- Valor: acompañamiento más efectivo, menos riesgos operativos y respaldo con conocimientos técnicos.


## 9. Historias de usuario / Casos de uso

- HU-001: Registrar trabajador.
- HU-002: Crear solicitud de permiso con adjunto.
- HU-003: Visualizar y filtrar solicitudes.
- HU-004: Aprobar o rechazar solicitud con observaciones.
- HU-005: Generar reporte PDF/XLSX del trabajador con gráficos.
- HU-006: Consultar registro de auditoría por usuario/tabla.

Para cada HU se documenta: actor, precondición, flujo principal, excepciones, postcondición.


## 10. Requerimientos funcionales

- RF1: CRUD para Trabajadores.
- RF2: CRUD para Solicitudes con validación de fechas y adjuntos.
- RF3: Cálculo automático de días_continuos y dias_laborables.
- RF4: Visualización de estadísticas con filtros.
- RF5: Exportar estadísticas a PDF incluyendo gráficos.
- RF6: Registro de auditoría para acciones críticas.
- RF7: Autenticación y control de permisos basados en Django.

## 11. Requerimientos no funcionales

- RNF1: Seguridad: cifrado en BD para campos sensibles.
- RNF2: Rendimiento: respuesta aceptable (<2s) en operaciones básicas con datasets pequeños.
- RNF3: Disponibilidad y despliegue reproducible en servidor (Gunicorn + Nginx).
- RNF4: Mantenibilidad: código documentado y pruebas básicas.
- RNF5: Portabilidad: soporte PostgreSQL/SQLite.


## 11.1 Requisitos de Alto Nivel del Proyecto

- RAL-01: Gestionar trabajadores y su vínculo con el usuario Django, manteniendo roles y perfiles actualizados.
- RAL-02: Administrar solicitudes de permisos y reposos con creación, edición, validación de fechas, adjuntos y cálculo automático de días laborables.
- RAL-03: Proveer un panel de estadísticas con gráficos dinámicos, filtros y exporte PDF de los resultados.
- RAL-04: Registrar auditoría de acciones críticas, incluyendo detalles cifrados y trazabilidad por usuario y tabla.
- RAL-05: Desplegar el sistema en servidor con una configuración reproducible de Gunicorn + Nginx y documentación de instalación.

## 11.2 Requisito con Criterio de Éxito

- RAL-01: El sistema debe permitir la creación, edición y eliminación de trabajadores con datos válidos y asociación a usuarios Django. Criterio de éxito: todas las operaciones CRUD son funcionales, los usuarios autenticados pueden acceder a su perfil, y el listado de trabajadores muestra información correcta.
- RAL-02: El sistema debe permitir gestionar solicitudes completas, validar fechas, calcular automáticamente días continuos y días laborables, y adjuntar archivos. Criterio de éxito: las solicitudes se guardan con cálculos correctos, los estados cambian a aprobado/rechazado, y el adjunto se almacena y descarga correctamente.
- RAL-03: El sistema debe mostrar estadísticas actualizadas con filtros por trabajador, tipo y rango de fechas, y exportar el informe en PDF. Criterio de éxito: los gráficos reflejan datos reales, los filtros funcionan correctamente, y el PDF generado incluye la gráfica y resumen de datos.
- RAL-04: El sistema debe capturar acciones críticas en auditoría con campos sensibles cifrados. Criterio de éxito: cada acción de aprobación, rechazo, edición o eliminación queda registrada y es recuperable solo por usuarios autorizados.
- RAL-05: El sistema debe documentar y soportar un despliegue reproducible en servidor con Gunicorn y Nginx. Criterio de éxito: el sistema arranca en el servidor bajo la configuración especificada y la documentación describe los pasos de despliegue.

## 11.3 Hitos

- Hito: El panel de estadísticas debe mostrar gráficos dinámicos y filtros funcionales. Realidad: la implementación se valida cuando los datos se actualizan correctamente en la interfaz.
- Hito: El sistema debe exportar informes en PDF desde estadísticas. Realidad: el hito se alcanza si el PDF se genera correctamente y contiene los datos esperados.
- Hito: La auditoría debe registrar acciones críticas con trazabilidad. Realidad: se cumple con registros completos y acceso controlado.
- Hito: El despliegue en servidor debe ser reproducible con Gunicorn/Nginx. Realidad: el hito se alcanza cuando el sistema arranca bajo la configuración documentada.

## 11.4 Riesgos

- Riesgo: Compatibilidad entre SQLite y PostgreSQL. Mitigación: probar el modelo de datos y las migraciones en ambos motores.
- Riesgo: Canvas tainted al capturar gráficos cliente-side para PDF. Mitigación: implementar fallback server-side con matplotlib y ReportLab.
- Riesgo: Pérdida o corrupción de adjuntos durante la carga o descarga. Mitigación: validar extensiones, tamaños y respaldar los archivos adjuntos.
- Riesgo: Acceso indebido a la auditoría o a datos sensibles. Mitigación: aplicar permisos estrictos y cifrado para los campos críticos.
- Riesgo: Retrasos en el despliegue por errores de configuración de Gunicorn/Nginx. Mitigación: documentar la configuración y realizar pruebas en un entorno similar al de producción.

## 11.5 Supuestos

- Se asume que el entorno de desarrollo y producción dispone de Python 3.11+ y las dependencias definidas en requirements.txt.
- Se asume que el servidor de producción contará con Gunicorn y Nginx instalados y accesibles para configuración.
- Se asume que los usuarios tendrán credenciales válidas en Django y roles definidos para control de acceso.
- Se asume que el volumen de datos será moderado, permitiendo tiempos de respuesta aceptables en operaciones básicas.
- Se asume que el equipo puede utilizar Chart.js para la visualización de estadísticas y que el navegador cliente soporta la biblioteca.
- Se asume que los adjuntos se almacenarán en el sistema de archivos local del proyecto o en un almacenamiento compatible disponible.

## 11.6 Restricciones

- El sistema debe ejecutarse sobre Django con plantillas HTML; no se contempla una aplicación SPA completa.
- El proyecto debe ser compatible con SQLite para desarrollo y PostgreSQL para producción.
- Las exportaciones de estadísticas deben ser en PDF; XLSX no es un requisito obligatorio para el panel de estadísticas.
- El despliegue debe apoyarse en Gunicorn + Nginx según la configuración descrita en la documentación.
- Los adjuntos deben limitarse a extensiones permitidas y tamaños máximos definidos por la aplicación.
- Los datos sensibles deben cifrarse en la base de datos y gestionarse con variables de entorno para las claves.
- El acceso a la auditoría y a los módulos críticos debe restringirse a usuarios autorizados.

---

## 12. Backlog del Producto

### Épica: Gestión de Trabajadores
Objetivo: registrar y administrar la información del personal, vinculándola al sistema Django para controlar permisos, roles y reportes.

- US-101: Registrar trabajador
  - Como administrador del sistema, deseo registrar un trabajador con datos personales y usuario asociado, para disponer de una base de personal actualizada.
  - Criterios de aceptación:
    1. El formulario solicita nombre, cédula, cargo, teléfono, correo y usuario Django.
    2. La cédula es única y su formato es validado.
    3. Al guardar, el trabajador queda disponible en el listado.
    4. Se muestra mensaje de éxito y no se permite duplicar cédulas.
  - Prioridad: Alta
  - Estimación: 5d
  - Dependencias: Ninguna
  - Sprint: 1
  - Estado: Por hacer
  - Comentarios: Se debe asegurar el vínculo correcto con el modelo User.

- US-102: Editar datos de trabajador
  - Como administrador del sistema, deseo editar la información de un trabajador existente, para corregir datos o actualizar su cargo.
  - Criterios de aceptación:
    1. El administrador puede cambiar nombre, cargo, teléfono y correo.
    2. El formulario conserva la cédula inmutable si ya existe.
    3. Los cambios se reflejan inmediatamente en el listado.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-101
  - Sprint: 1
  - Estado: Por hacer
  - Comentarios: Incluir validaciones mínimas de datos.

- US-103: Asociar trabajador a usuario Django
  - Como administrador del sistema, deseo vincular un trabajador con un usuario Django, para controlar acceso a solicitudes y perfiles.
  - Criterios de aceptación:
    1. Se puede asociar un trabajador a un usuario existente.
    2. No se permite asignar un usuario a más de un trabajador.
    3. El trabajador muestra el nombre de usuario asociado.
  - Prioridad: Media
  - Estimación: 2d
  - Dependencias: US-101
  - Sprint: 2
  - Estado: Por hacer
  - Comentarios: Usar relaciones OneToOne o ForeignKey según el modelo actual.

- US-104: Listar y buscar trabajadores
  - Como administrador del sistema, deseo ver un listado filtrable de trabajadores, para encontrar rápidamente registros por nombre, cédula o cargo.
  - Criterios de aceptación:
    1. El listado muestra nombre, cédula, cargo, estado y usuario asociado.
    2. Hay búsqueda por nombre, cédula y cargo.
    3. El listado es paginado si hay más de 10 registros.
  - Prioridad: Media
  - Estimación: 3d
  - Dependencias: US-101
  - Sprint: 2
  - Estado: Por hacer
  - Comentarios: Añadir opción de exportar listado básico en el futuro.

### Épica: Solicitudes
Objetivo: permitir crear, validar, gestionar y auditar solicitudes de permiso o reposo con cálculos automáticos y adjuntos.

- US-201: Crear solicitud de permiso/repo
  - Como trabajador, deseo crear una solicitud con fechas, tipo, motivo y adjunto, para tramitar mi permiso en la Fundación.
  - Criterios de aceptación:
    1. El formulario guarda fecha de inicio, fin, tipo, motivo y archivo adjunto.
    2. Se valida que fecha de inicio ≤ fecha de fin.
    3. El adjunto acepta PDF/JPG/PNG y no excede el límite configurado.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-101
  - Sprint: 2
  - Estado: Por hacer
  - Comentarios: El adjunto debe guardarse en `MEDIA_ROOT` con nombre seguro.

- US-202: Validar fechas y calcular días
  - Como trabajador, deseo que el sistema calcule días_continuos y dias_laborables automáticamente, para saber el alcance real de mi permiso.
  - Criterios de aceptación:
    1. El sistema calcula días_continuos como diferencia inclusive.
    2. El sistema excluye sábados, domingos y feriados para dias_laborables.
    3. El cálculo se actualiza al crear o editar la solicitud.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-201
  - Sprint: 2
  - Estado: Por hacer
  - Comentarios: Incluir lista básica de feriados dentro del alcance del proyecto.

- US-203: Adjuntar archivos a la solicitud
  - Como trabajador, deseo adjuntar comprobantes o documentos al crear mi solicitud, para respaldar mi motivo.
  - Criterios de aceptación:
    1. El formulario permite cargar un archivo por solicitud.
    2. Solo se aceptan extensiones permitidas y tamaño máximo configurado.
    3. El adjunto puede descargarse desde la vista de detalle.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-201
  - Sprint: 3
  - Estado: Por hacer
  - Comentarios: Validar también el tipo MIME en el backend.

- US-204: Ver detalle y estado de solicitud
  - Como trabajador, deseo ver el detalle de mi solicitud, su estado y observaciones, para saber el resultado del trámite.
  - Criterios de aceptación:
    1. La vista muestra todos los campos, adjunto y estado de la solicitud.
    2. Incluye fecha de creación y última modificación.
    3. El estado puede ser Pendiente, Aprobado o Rechazado.
  - Prioridad: Media
  - Estimación: 3d
  - Dependencias: US-201
  - Sprint: 3
  - Estado: Por hacer
  - Comentarios: El detalle debe ser accesible solo al trabajador y al área de RRHH.

- US-205: Aprobar o rechazar solicitud con observaciones
  - Como Recursos Humanos, deseo aprobar o rechazar solicitudes con comentarios, para comunicar la decisión y dejar evidencia.
  - Criterios de aceptación:
    1. Recursos Humanos puede cambiar el estado de una solicitud.
    2. Debe agregar una observación al aprobar o rechazar.
    3. La acción queda registrada en el historial de auditoría.
  - Prioridad: Alta
  - Estimación: 4d
  - Dependencias: US-204, US-401
  - Sprint: 4
  - Estado: Por hacer
  - Comentarios: Incluir notificación interna si se dispone más adelante.

### Épica: Reportes y Estadísticas
Objetivo: entregar métricas y reportes visuales que faciliten el análisis de permisos y desempeño.

- US-301: Panel de estadísticas filtrable
  - Como Recursos Humanos, deseo ver gráficos de solicitudes por tipo, estado y periodo, para tomar decisiones informadas.
  - Criterios de aceptación:
    1. El panel muestra gráficos de barras y pastel con datos reales.
    2. Permite filtrar por rango de fechas, tipo de solicitud y trabajador.
    3. Los datos se actualizan al cambiar los filtros.
  - Prioridad: Alta
  - Estimación: 4d
  - Dependencias: US-201, US-204
  - Sprint: 3
  - Estado: Por hacer
  - Comentarios: Usar Chart.js en la interfaz.

- US-302: Exportar estadísticas a PDF
  - Como Recursos Humanos, deseo exportar el panel de estadísticas a PDF, para compartir informes oficiales.
  - Criterios de aceptación:
    1. El PDF incluye tablas de resumen e imágenes de los gráficos.
    2. Si la captura cliente falla, se genera el gráfico en servidor.
    3. El PDF es descargable desde la interfaz.
  - Prioridad: Alta
  - Estimación: 4d
  - Dependencias: US-301
  - Sprint: 4
  - Estado: Por hacer
  - Comentarios: Incluir fallback con matplotlib y ReportLab.

- US-303: Exportar solicitudes a XLSX
  - Como Recursos Humanos, deseo exportar un listado de solicitudes a XLSX, para análisis externo y archivo.
  - Criterios de aceptación:
    1. El archivo XLSX incluye filas con datos clave de cada solicitud.
    2. Se pueden aplicar los mismos filtros del panel antes de exportar.
    3. El archivo se descarga correctamente.
  - Prioridad: Media
  - Estimación: 3d
  - Dependencias: US-301
  - Sprint: 4
  - Estado: Por hacer
  - Comentarios: Uso de pandas o openpyxl según disponibilidad.

### Épica: Auditoría y Seguridad
Objetivo: garantizar trazabilidad, confidencialidad e integridad de acciones críticas.

- US-401: Registrar acciones críticas en auditoría
  - Como auditor interno, deseo una bitácora de aprobaciones, rechazos, ediciones y eliminaciones, para contar con evidencia confiable.
  - Criterios de aceptación:
    1. Cada evento crítico se guarda con usuario, fecha, tabla y acción.
    2. Los detalles sensibles se cifran en la base de datos.
    3. El registro se puede consultar por usuarios autorizados.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-201, US-205
  - Sprint: 5
  - Estado: Por hacer
  - Comentarios: Aprovechar modelo de Auditoría ya planificado.

- US-402: Buscar auditoría por usuario/tabla/fecha
  - Como auditor interno, deseo filtrar registros de auditoría por usuario, tabla y fecha, para investigar incidentes eficientemente.
  - Criterios de aceptación:
    1. La interfaz permite ingresar criterios de búsqueda.
    2. Los resultados muestran registro, acción, fecha y detalle.
    3. Solo usuarios autorizados acceden al módulo.
  - Prioridad: Media
  - Estimación: 2d
  - Dependencias: US-401
  - Sprint: 5
  - Estado: Por hacer
  - Comentarios: Definir permisos concretos de acceso.

- US-403: Cifrar campos sensibles en base de datos
  - Como auditor interno, deseo que datos sensibles como cédula y motivo queden cifrados, para proteger la información personal.
  - Criterios de aceptación:
    1. Los campos sensibles se almacenan usando EncryptedTextField o equivalente.
    2. Las vistas autorizadas desencriptan los datos correctamente.
    3. Las claves de cifrado se gestionan con variables de entorno.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: US-201, US-401
  - Sprint: 5
  - Estado: Por hacer
  - Comentarios: Revisar configuración de FERNET_KEY y entornos.

### Épica: Infraestructura y Operación
Objetivo: asegurar despliegues, respaldos y documentación para operación estable.

- US-501: Backup y restauración automatizada
  - Como equipo de soporte, deseo un procedimiento de backup y restauración, para proteger los datos y recuperarlos ante fallos.
  - Criterios de aceptación:
    1. Existe script o tarea documentada para backup de base de datos.
    2. Existe procedimiento de restauración paso a paso.
    3. El backup incluye archivos adjuntos y base de datos.
  - Prioridad: Media
  - Estimación: 3d
  - Dependencias: US-503
  - Sprint: 6
  - Estado: Por hacer
  - Comentarios: Incluir ops/backup.ps1 y documentación en /docs.

- US-502: Despliegue reproducible Gunicorn + Nginx
  - Como equipo de soporte, deseo una configuración de despliegue reproducible, para instalar el sistema en producción con seguridad y estabilidad.
  - Criterios de aceptación:
    1. La aplicación se puede levantar con Gunicorn.
    2. Nginx actúa como proxy inverso con configuraciones de seguridad.
    3. Existe guía breve de despliegue.
  - Prioridad: Alta
  - Estimación: 2d
  - Dependencias: US-503
  - Sprint: 6
  - Estado: Por hacer
  - Comentarios: Utilizar ops/nginx_sgpr.conf y sgpr.service.

- US-503: Documentar manuales de usuario e implementación
  - Como equipo de soporte, deseo documentación clara de uso, instalación y respaldo, para entregar el sistema con guía completa.
  - Criterios de aceptación:
    1. Existen manuales de usuario y de implementación.
    2. La documentación incluye pasos de instalación, backups y restauración.
    3. El contenido está disponible en /docs.
  - Prioridad: Alta
  - Estimación: 3d
  - Dependencias: Ninguna
  - Sprint: 6
  - Estado: Por hacer
  - Comentarios: Actualizar manuales existentes /docs/manual_usuario.md y /docs/manual_implementacion.md.

---

## 13. Sprint Backlog (Periodo: 01/04/2026 → 30/06/2026)

Este periodo se organiza en seis sprints de dos semanas y una semana de cierre para entrega.

### Sprint 1 (01/04 — 14/04)
Objetivo: definir la base de datos, configurar el entorno y entregar el CRUD inicial de trabajadores.

- Historias y tareas:
  - US-101: Registrar trabajador (5d) — Estado: Por hacer
  - US-102: Editar datos de trabajador (3d) — Estado: Por hacer
  - Tarea: Configurar entorno virtual, dependencias y `requirements.txt` (1d)
  - Tarea: Crear migraciones y ejecutar pruebas unitarias de modelos (1d)

- Dependencias: ninguna
- Comentarios: foco en estabilidad de los modelos de `Trabajador`, `Solicitud` y `Auditoría`.

### Sprint 2 (15/04 — 28/04)
Objetivo: construir el flujo de solicitudes, validar fechas y vincular trabajadores a usuarios.

- Historias y tareas:
  - US-201: Crear solicitud de permiso/repo (3d) — Estado: Por hacer
  - US-202: Validar fechas y calcular días (3d) — Estado: Por hacer
  - US-103: Asociar trabajador a usuario Django (2d) — Estado: Por hacer
  - Tarea: Integración inicial de trabajador y solicitud (2d)

- Dependencias: US-101
- Comentarios: asegurar que los cálculos de días sean correctos antes de avanzar en UI.

### Sprint 3 (29/04 — 12/05)
Objetivo: implementar la subida de adjuntos, el detalle de solicitud y el panel de estadísticas filtrable.

- Historias y tareas:
  - US-203: Adjuntar archivos a la solicitud (3d) — Estado: Por hacer
  - US-204: Ver detalle y estado de solicitud (3d) — Estado: Por hacer
  - US-301: Panel de estadísticas filtrable (4d) — Estado: Por hacer
  - Tarea: Ajustes visuales y responsive en Chart.js (1d)

- Dependencias: US-201, US-204
- Comentarios: probar la experiencia de usuario con datos reales de ejemplo.

### Sprint 4 (13/05 — 26/05)
Objetivo: entregar exportes de informes y garantizar la generación de PDF con fallback servidor.

- Historias y tareas:
  - US-302: Exportar estadísticas a PDF (4d) — Estado: Por hacer
  - US-303: Exportar solicitudes a XLSX (2d) — Estado: Por hacer
  - Tarea: Implementar fallback servidor para gráficos PDF (2d)
  - Tarea: Ajustes de formato y márgenes en exportes (1d)

- Dependencias: US-301
- Comentarios: validar el tamaño y legibilidad del PDF en papel y pantalla.

### Sprint 5 (27/05 — 09/06)
Objetivo: habilitar auditoría, seguridad y cifrado de datos sensibles.

- Historias y tareas:
  - US-401: Registrar acciones críticas en auditoría (3d) — Estado: Por hacer
  - US-402: Buscar auditoría por usuario/tabla/fecha (2d) — Estado: Por hacer
  - US-403: Cifrar campos sensibles en base de datos (3d) — Estado: Por hacer
  - Tarea: Revisar configuración de `FERNET_KEY` y variables de entorno (1d)

- Dependencias: US-201, US-205
- Comentarios: la seguridad y trazabilidad son requisitos clave antes del despliegue.

### Sprint 6 (10/06 — 23/06)
Objetivo: cerrar el proyecto con despliegue reproducible, backups y documentación.

- Historias y tareas:
  - US-501: Backup y restauración automatizada (3d) — Estado: Por hacer
  - US-502: Despliegue reproducible Gunicorn + Nginx (2d) — Estado: Por hacer
  - US-503: Documentar manuales de usuario e implementación (3d) — Estado: Por hacer
  - Tarea: Pruebas finales de integración y corrección de bugs (2d)
  - Tarea: Preparar entregables y capacitación breve (1d)

- Dependencias: US-403, US-302
- Comentarios: priorizar la entrega estable y la documentación clara.

### Semana de cierre y entrega (24/06 — 30/06)
Objetivo: revisión final, validación con stakeholders y ajustes de entrega.

- Actividades:
  - Revisión de aceptación con Product Owner y RRHH.
  - Ajustes menores en PDF, filtros y validaciones.
  - Corrección de comentarios de auditoría y documentación.
  - Preparación del paquete final de entrega.

- Comentarios: esta semana actúa como buffer para asegurar la culminación del proyecto el 30/06/2026.

---

## 14. Acta de seguimiento de reuniones del Sprint (plantilla y ejemplo)

**Acta — Reunión de seguimiento (Daily/Weekly)**

- Fecha: 2026-05-05
- Participantes: Desarrolladora (Gabriela Urbina)
- Objetivos del día/sprint: Finalizar exportes PDF; corregir tamaño de gráficos
- Avances: Captura cliente funciona en navegador X; fallback en servidor implementado
- Bloqueos: Canvas tainted en navegadores con recursos cross-origin
- Acuerdos: Enviar paleta de colores desde frontend al backend en próxima iteración
- Próximos pasos: Ajustar márgenes en ReportLab; generar PDF de prueba

(Guardar actas en `/docs/actas/` con fecha en el nombre).

---

## 15. Informe consolidado mensual de acciones

### Abril 2026
- Implementación de modelos y CRUD básicos.
- Configuración inicial del entorno de despliegue en servidor.
- Pruebas unitarias de modelos.

### Mayo 2026
- Desarrollo de panel de estadísticas y Chart.js.
- Implementación de export PDF con captura cliente y fallback servidor.
- Correcciones de UI y formato de reportes.

### Junio 2026
- Auditoría y seguridad reforzadas.
- Tests de integración y despliegue en servidor.
- Documentación y manuales técnicos.

---

## 16. Wireframes y diseño de interfaz

- Páginas principales: Login, Listado Trabajadores, Formulario Solicitud, Panel Estadísticas, Detalle Solicitud.
- Organización responsive con Bootstrap y componentes accesibles.
- Incluir wireframes en `/docs/wireframes/` (PNG/SVG).

---

## 17. Diagrama de Base de Datos (MER)

Se incluye `erd.puml` en el repositorio. Para imagen generada usar PlantUML.

![MER del sistema](./erd.puml)

---

## 18. Interfaces de entrada y salida

Entradas:
- Formularios HTML (crear/editar solicitudes y trabajadores)
- Archivos adjuntos (multipart)
- Parámetros de filtrado en panel de estadísticas (fechas, trabajador, tipo)

Salidas:
- Vistas HTML con tablas y gráficos
- Exportes PDF y XLSX
- Registros de auditoría

---

## 19. Web Services básicos (APIs)

- `GET /api/solicitudes/` — listar solicitudes (filtros: trabajador_id, estado, fecha)
- `POST /api/solicitudes/` — crear solicitud (multipart)
- `GET /api/estadisticas/` — datos para graficas (JSON)
- `POST /api/export/pdf/` — generar PDF (recibe imágenes base64 o datos de fallback)

Asegurar autenticación y control de acceso en cada endpoint.

---

## 20. Base de datos (backup y restauración)

- Recomendación: usar `pg_dump` para PostgreSQL y rotación diaria. Scripts en `/ops/backup.sh`.
- Mantener backups en un directorio seguro (`/backups/`) con retención mínima de 7 días.

---

## 21. Desarrollo e implementación de módulos

- Trabajadores: implementado (modelos, vistas, templates)
- Solicitudes: implementado (validaciones, adjuntos, cálculos)
- Estadísticas: implementado (Chart.js, exportes)
- Auditoría: implementado (registro y almacenamiento cifrado)

Módulos probados localmente con `runserver`. (Despliegue en servidor probado según plan de lanzamiento).

---

## 22. Formularios digitales (estructura)

**Formulario Solicitud**
- trabajador_id (select)
- tipo (select)
- fecha_inicio (date)
- fecha_fin (date)
- motivo (textarea)
- adjunto (file)

Validaciones: fechas coherentes, adjunto extensión permitida, motivo obligatorio.

---

## 23. Módulos integrados y pruebas de instalación

- Instalar dependencias: `pip install -r requirements.txt`.
- Levantar servicios en producción: iniciar el servidor de aplicaciones (p. ej. Gunicorn) y configurar Nginx como proxy inverso.
- Verificar acceso en `http://localhost:8000`.

---

## 24. Código y archivos fuentes

- Repositorio contiene: `sgpr_alquitrana/` (app Django), `templates/`, `static/`, `erd.puml`.
- Código documentado.

---

## 25. Informe de testeo / pruebas realizadas

- Pruebas unitarias de modelos y validaciones.
- Pruebas funcionales manuales: creación de solicitudes, aprobación, exportes, auditoría.
- Casos especiales: canvas tainted (verificado fallback), adjuntos inválidos rechazados.

---

## 26. Manuales técnicos

- Manual de usuario (`/docs/manual_usuario.md`) — Uso del sistema, generación de reportes.
- Manual de implementación (`/docs/manual_implementacion.md`) — Despliegue en servidor, restauración de backups.

---

## 27. Documentos de retrospectiva final

- Lecciones aprendidas: definir paleta de colores consistente, manejar limitaciones de canvas, priorizar tamaño de payload base64.
- Recomendaciones: automatizar backups, pruebas en múltiples navegadores y entornos, documentar procesos operativos.

---

## 28. Entregables y evidencia de instalación

- Código fuente y documentación en el repositorio.
- `erd.puml` con MER y explicación.
- Scripts de backup y despliegue en `/ops/`.
- Carpetas `/docs/manuals/`, `/docs/wireframes/`, `/docs/actas/` con archivos correspondientes.

---

## 29. Firma y declaración

Declaro que este proyecto fue desarrollado bajo SCRUM y que la persona indicada (desarrolladora) ejecutó todas las actividades de análisis, diseño, desarrollo, pruebas e implementación.

**Fecha de generación del documento:** 30-06-2026


---

*Fin del documento.*
