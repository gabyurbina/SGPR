# Documento del Proyecto - SGPR

> Documento completo del sistema de Gestión de Permisos y Reportes (SGPR). Desarrollado bajo metodología SCRUM como Responsable del desarrollo: Gabriela Urbinaa que ejecutó todas las actividades de análisis, diseño, desarrollo, pruebas e implementación.

---

## Tabla de contenidos

- [Visión](#visión)
- [Misión](#misión)
- [Objetivo general](#objetivo-general)
- [Objetivos específicos](#objetivos-específicos)
- [Propósito y justificación](#propósito-y-justificación)
- [Alcance del proyecto](#alcance-del-proyecto)
- [Descripción general del proyecto](#descripción-general-del-proyecto)
- [Stakeholders (Interesados)](#stakeholders-interesados)
- [Historias de usuario (Casos de uso)](#historias-de-usuario-casos-de-uso)
- [Requerimientos funcionales](#requerimientos-funcionales)
- [Requerimientos no funcionales](#requerimientos-no-funcionales)
- [Backlog del Producto](#backlog-del-producto-ejemplos-de-épicas-y-user-stories)
- [Sprint Backlog](#sprint-backlog-ejemplo-de-un-sprint-de-2-semanas)
- [Acta de seguimiento](#acta-de-seguimiento-plantilla-con-entrada-real)
- [Informe consolidado mensual](#informe-consolidado-mensual-de-acciones-de-implementación)
- [Winframes y diseño de la interfaz](#winframes-y-diseño-de-la-interfaz)
- [Diagrama de Base de Datos (MER)](#diagrama-de-base-de-datos-mer)
- [Interfaces de entrada y salida del sistema](#interfaces-de-entrada-y-salida-del-sistema)
- [Web Services básicos de los procesos](#web-services-básicos-de-los-procesos)
- [Base de datos (backup)](#base-de-datos-backup)
- [Desarrollo e implementación por módulos](#desarrollo-e-implementación-por-módulos)
- [Formularios digitales (estructura)](#formularios-digitales-estructura)
- [Módulos integrados y pruebas de instalación](#módulos-integrados-y-pruebas-de-instalación)
- [Código y archivos fuentes](#código-y-archivos-fuentes)
- [Informe de testeo / Pruebas realizadas](#informe-de-testeo--pruebas-realizadas)
- [Manuales técnicos](#manuales-técnicos)
- [Documentos de retrospectiva final del proyecto](#documentos-de-retrospectiva-final-del-proyecto)
- [Anexos y recomendaciones finales](#anexos-y-recomendaciones-finales)


## Visión

Ser la plataforma líder en la gestión y control de permisos y reposos laborales, ofreciendo informes precisos, exportes confiables (PDF/XLSX) y una experiencia intuitiva que facilite la toma de decisiones a nivel administrativo.

## Misión

Proveer una solución web segura, auditable y eficiente para el registro, revisión y análisis de solicitudes laborales, automatizando cálculos de días laborables y generando reportes adaptables a las necesidades institucionales.

## Objetivo general

Desarrollar e implementar una plataforma web que permita gestionar solicitudes de permisos y reposos, garantizando integridad de datos, trazabilidad y generación de reportes (visualización y exportes) para la administración.

## Objetivos específicos

- Registrar y gestionar solicitudes de permisos y reposos por trabajador.
- Calcular automáticamente días continuos y días laborables considerando feriados.
- Permitir adjuntar justificantes y validar formatos permitidos.
- Generar reportes visuales y exportables (PDF/XLSX) que reproduzcan los gráficos de la vista.
- Registrar auditoría de acciones críticas con detalle cifrado.
- Mantener la seguridad y la confidencialidad de información sensible (cédulas, motivos) mediante cifrado en BD.

## Propósito y justificación

El sistema centraliza la gestión de permisos, reduce errores administrativos, acelera procesos de revisión y aporta trazabilidad mediante auditorías. Justifica la inversión al disminuir tiempos administrativos y mejorar cumplimiento normativo.

## Alcance del proyecto

Incluye: módulo de trabajadores, registro de solicitudes, gestión de estados (PENDIENTE/APROBADO/RECHAZADO), cálculo de días laborables, generación de reportes con gráficos, exportes PDF/XLSX, auditoría y control de accesos. No incluye: integración SSO externa (salvo Django auth), ni migraciones masivas automáticas.

## Descripción general del proyecto

Aplicación web desarrollada en Python usando Django, con frontend que utiliza Chart.js para visualización. Exportes PDF se generan combinando captura client-side (canvas.toDataURL) y fallback server-side (matplotlib + ReportLab) si el canvas está "tainted". Se cifra información sensible con EncryptedTextField.

## Stakeholders (Interesados)

- Administrador del sistema (Lic. Marbella Canelón)
- Recursos Humanos (Francismar Marchan)
- Trabajadores (usuarios finales)
- Auditoría interna
- Equipo de IT/Soporte (Ing. Trino Vera)
- Desarrollo principal (Gabriela Urbina)

## Historias de usuario (Casos de uso)

1. Como trabajador, quiero registrar una solicitud de permiso o reposo con fechas, motivo y adjunto, para que mi solicitud quede disponible en el sistema y pueda dar soporte documental.
   - Incluye validación de fechas, subida de archivo y almacenamiento seguro del justificante.

2. Como trabajador, quiero consultar el estado y el detalle de mis solicitudes, para verificar si fueron aprobadas, rechazadas o están pendientes y revisar las observaciones.
   - Debe mostrar el estado, el cálculo de días continuos y días laborables, y el adjunto asociado.

3. Como responsable de Recursos Humanos, quiero ver solicitudes pendientes y procesarlas, para aprobar o rechazar permisos con observaciones y mantener la trazabilidad del proceso.
   - Debe permitir filtrar por trabajador, tipo de solicitud y periodo.

4. Como administrador del sistema, quiero gestionar trabajadores y asociarlos a usuarios Django, para controlar perfiles, roles y acceso seguro a la aplicación.
   - Incluye CRUD de trabajadores y vínculo con la cuenta de usuario.

5. Como administrador o supervisor, quiero acceder a un panel de estadísticas con gráficos filtrables, para analizar tendencias de permisos, tipos de solicitudes y tiempos de aprobación.
   - La vista debe actualizarse con los filtros y mostrar gráficos interactivos.

6. Como responsable de auditoría, quiero consultar el historial de acciones críticas y ver detalles cifrados, para validar el cumplimiento normativo y asegurar la integridad de los registros.
   - La auditoría debe registrar aprobaciones, rechazos, ediciones y eliminaciones.

7. Como usuario del sistema, quiero exportar reportes en PDF y XLSX con los datos y gráficos visibles, para compartir informes oficiales sin perder la fidelidad de la información.
   - Incluye fallback servidor si la captura de gráficos cliente falla.

## Requerimientos funcionales

- RF1: Registrar Trabajador asociado a User de Django.
- RF2: Registrar Solicitud con tipo, fechas, motivo cifrado y adjunto.
- RF3: Validar extensiones de adjuntos (.pdf, .png, .jpg, .jpeg).
- RF4: Calcular dias_continuos y dias_laborables al guardar Solicitud.
- RF5: Visualizar estadísticas con gráficos interactorios (Chart.js).
- RF6: Exportar estadísticas a PDF/XLSX con gráficos incorporados.
- RF7: Registrar Auditoria en cada acción crítica.
- RF8: Control de acceso mediante permisos de Django.

## Requerimientos no funcionales

- RNF1: Seguridad: cifrado de campos sensibles en repositorio.
- RNF2: Rendimiento: respuesta < 2s en consultas básicas para datasets pequeños.
- RNF3: Disponibilidad: despliegue reproducible en servidor (p.ej. Gunicorn + Nginx) o mediante entorno virtual.
- RNF4: Portabilidad: compatible con PostgreSQL y SQLite para desarrollo.
- RNF5: Mantenibilidad: código documentado en español.

## Backlog del Producto (épicas y user stories desarrolladas)

### Épica: Gestión de Trabajadores
Esta épica cubre la creación, edición y búsqueda de trabajadores, lo que garantiza que el personal esté correctamente registrado y asociado a los permisos de Django.

- US-101: Registrar trabajador
  - Como administrador del sistema, quiero ingresar un trabajador con datos personales y asociarlo a un usuario Django, para mantener un registro formalizado y controlado de cada empleado.
  - Criterios de aceptación:
    - El formulario captura nombre, cédula, cargo, teléfono, correo y usuario asociado.
    - La cédula se valida como única.
    - El trabajador se almacena en la base de datos y aparece en el listado.
  - Caso de estudio: La Administradora crea el perfil de "María Pérez" con cédula 12345678, su cargo y el usuario Django vinculado. Al guardar, María aparece en el listado y puede iniciar sesión para generar solicitudes.

- US-102: Editar trabajador
  - Como administrador del sistema, quiero actualizar datos de un trabajador existente, para corregir información y mantener el registro actualizado.
  - Criterios de aceptación:
    - Se pueden cambiar nombre, cargo, teléfono y correo.
    - La cédula permanece inalterable si ya está registrada.
  - Caso de estudio: Se corrige el cargo de "José Ramírez" de asistente a supervisor sin modificar su cédula, y la actualización se refleja inmediatamente en la ficha.

- US-103: Listar y buscar trabajadores
  - Como administrador del sistema, quiero filtrar y buscar trabajadores por nombre, cédula y cargo, para encontrar rápidamente registros.
  - Criterios de aceptación:
    - El listado es paginado cuando hay más de 10 registros.
    - La búsqueda es rápida y muestra resultados instantáneos.
  - Caso de estudio: La Administradora busca a "María" y filtra por cargo "Docente" para encontrar rápidamente la ficha y revisar sus solicitudes.

### Épica: Solicitudes
Esta épica aborda el flujo completo de creación, cálculo, visualización y revisión de solicitudes de permiso y reposo.

- US-201: Crear solicitud de permiso o reposo
  - Como trabajador, quiero registrar una solicitud con fechas, tipo, motivo y adjunto, para que mi solicitud quede registrada y respaldada.
  - Criterios de aceptación:
    - Se valida que fecha de inicio no sea posterior a fecha de fin.
    - Se permite adjuntar PDF/JPG/PNG dentro de un límite de tamaño.
  - Caso de estudio: El trabajador envía una solicitud por dos días de permiso con justificante médico en PDF. El sistema valida las fechas y guarda el archivo en la carpeta de adjuntos.

- US-202: Calcular días continuos y laborables
  - Como trabajador, quiero que el sistema calcule los días continuos y laborales automáticamente, para saber cuánto tiempo cubre mi permiso.
  - Criterios de aceptación:
    - El cálculo excluye sábados y domingos.
    - Se consideran feriados predeterminados.
  - Caso de estudio: Una solicitud del 10 al 14 de junio muestra 5 días continuos y 3 días laborables, excluyendo el fin de semana.

- US-203: Consultar detalle de solicitud
  - Como trabajador, quiero ver el detalle de mi solicitud, estado y observaciones, para saber si fue aprobada o rechazada y por qué.
  - Criterios de aceptación:
    - Se muestra el estado, fecha de creación, cálculo de días y adjunto asociado.
  - Caso de estudio: El trabajador revisa una solicitud rechazada y lee la observación "Motivo insuficiente" para completar la información una próxima vez.

- US-204: Aprobar o rechazar solicitud con observaciones
  - Como responsable de Recursos Humanos, quiero revisar solicitudes pendientes y cambiarlas a aprobado o rechazado con comentarios, para completar el proceso de revisión.
  - Criterios de aceptación:
    - La acción queda registrada en auditoría.
    - Se exige un comentario al aprobar o rechazar.
  - Caso de estudio: RRHH aprueba una solicitud de reposo y registra la observación "Aprobado por cumplimiento de normativa"; el histórico queda disponible para auditoría.

### Épica: Reportes y Estadísticas
Esta épica permite la visualización y exportación de datos clave para la toma de decisiones en la dirección y gestión de personal.

- US-301: Panel de estadísticas filtrables
  - Como supervisor, quiero ver gráficos de solicitudes por tipo, estado y periodo, para analizar el comportamiento de permisos en la Fundación.
  - Criterios de aceptación:
    - Los filtros por fecha, tipo y trabajador actualizan los gráficos.
    - Se muestran gráficos de barras y pastel.
  - Caso de estudio: El supervisor filtra las solicitudes del último mes y observa que el 60% son permisos médicos, lo que ayuda a programar mejor la cobertura.

- US-302: Exportar estadísticas a PDF
  - Como supervisor, quiero generar un PDF con los resultados del panel, para compartir un informe formal.
  - Criterios de aceptación:
    - El PDF incluye tablas de resumen y las imágenes de los gráficos.
    - Existe fallback servidor si falla la captura de canvas cliente.
  - Caso de estudio: Se genera un informe PDF para la reunión mensual y el documento contiene exactamente los gráficos vistos en pantalla.

- US-303: Exportar lista de solicitudes a XLSX
  - Como supervisor, quiero descargar un archivo XLSX de las solicitudes filtradas, para trabajar con datos en hojas de cálculo.
  - Criterios de aceptación:
    - El export contiene los campos clave de cada solicitud.
    - Aplica los filtros seleccionados en la interfaz.
  - Caso de estudio: RRHH exporta solicitudes de junio y utiliza Excel para sumar días laborables y comparar con el presupuesto de personal.

### Épica: Auditoría y Seguridad
Esta épica asegura trazabilidad y confidencialidad de las acciones críticas en el sistema.

- US-401: Registrar auditoría de acciones críticas
  - Como auditor, quiero que el sistema registre aprobaciones, rechazos, ediciones y eliminaciones, para contar con evidencia de los cambios.
  - Criterios de aceptación:
    - El registro guarda usuario, fecha, tabla, acción y detalle.
    - Se cifran los campos sensibles.
  - Caso de estudio: La auditoría muestra que el administrador editó una solicitud y el motivo quedó registrado con cédula cifrada.

- US-402: Consultar auditoría por filtros
  - Como auditor, quiero buscar registros de auditoría por usuario, tabla y fecha, para investigar eventos específicos.
  - Criterios de aceptación:
    - El módulo ofrece búsqueda por usuario, tabla y rango de fechas.
    - Solo usuarios autorizados acceden a la auditoría.
  - Caso de estudio: El auditor filtra registros de mayo para encontrar todas las aprobaciones hechas por RRHH.

- US-403: Cifrar datos sensibles en la BD
  - Como auditor, quiero que datos como cédula y motivo queden cifrados, para proteger la confidencialidad de la información.
  - Criterios de aceptación:
    - Los datos se almacenan cifrados.
    - Las vistas autorizadas desencriptan correctamente para visualización.
  - Caso de estudio: La oficina de auditoría valida que la cédula del trabajador no sea legible directamente en la base de datos.

### Épica: Infraestructura y operación
Esta épica cubre la documentación, respaldo y configuración para mantener el sistema en producción.

- US-501: Documentar despliegue y backups
  - Como equipo de soporte, quiero guías de despliegue y respaldo, para instalar el sistema y recuperar datos en caso de fallo.
  - Criterios de aceptación:
    - Existen manuales de despliegue y respaldo en `/docs`.
    - Hay instrucciones para Gunicorn + Nginx y backup de base de datos.
  - Caso de estudio: El soporte sigue la guía de despliegue para replicar el entorno productivo en un servidor nuevo.

- US-502: Preparar backup y restauración automatizada
  - Como equipo de soporte, quiero un procedimiento de backup automatizado y pruebas de restauración, para asegurar la disponibilidad de datos.
  - Criterios de aceptación:
    - Se documentan scripts o pasos de backup.
    - Se detalla el proceso de restauración.
  - Caso de estudio: Se ejecuta un backup nocturno y se verifica la restauración exitosa en un entorno de pruebas.

- US-503: Documentar manuales de usuario e implementación
  - Como equipo de soporte, quiero manuales claros de uso e instalación, para entregar el sistema con respaldo documental.
  - Criterios de aceptación:
    - Existen manuales de usuario e implementación en `/docs`.
    - La documentación incluye pasos de instalación, backups y restauración.
  - Caso de estudio: El cliente lee el manual y sigue los pasos para crear un nuevo usuario y revisar el módulo de solicitudes.

## Sprint Backlog (ejemplo de un sprint de 2 semanas)

- Tarea 1: Implementar modelos Trabajador y Solicitud (2 días)
- Tarea 2: Crear vista de listado y formulario (3 días)
- Tarea 3: Implementar Chart.js en estadisticas (2 días)
- Tarea 4: Implementar export PDF con fallback (4 días)
- Tarea 5: Pruebas unitarias y correcciones (3 días)

## Acta de seguimiento (Plantilla con entrada real)

**Sprint:** 2026-05-01 → 2026-05-14
**Asistentes:** Desarrolladora (única persona)
**Objetivos sprint:** Implementar módulo de solicitudes y reportes básicos.
**Avances:** Modelos y vistas implementados; gráficos en UI funcionales; export PDF con capturas implementado.
**Bloqueos:** Canvas "tainted" en ciertos navegadores cuando se cargan recursos cross-origin.
**Acciones:** Implementar fallback en servidor (matplotlib); ajustar tamaños de imagen en PDF.

## Informe consolidado mensual de acciones de implementación

- Mes: Mayo 2026
- Actividades:
  - Definición de requisitos y diseño ER
  - Implementación de modelos y lógica de negocio
  - Desarrollo de vistas y exportes (PDF/XLSX)
  - Pruebas manuales y correcciones
- Resultados: Plataforma en versión funcional para pruebas internas.

## Winframes y diseño de la interfaz

- Estructura de páginas: Login, Lista Trabajadores, Formulario Solicitud, Panel de Estadísticas, Reportes.
- Diseño: HTML/CSS con Bootstrap básico; elementos Chart.js para gráficos.
- Nota: Wireframes y mockups se deben anexar como imágenes en carpeta `/docs/wireframes/`.

## Diagrama de Base de Datos (MER)

Se incluye el archivo PlantUML con el MER en `erd.puml`.

![MER del sistema](./erd.puml)

> Nota: Para obtener una imagen (PNG/SVG) de `erd.puml`, usar la extensión PlantUML en VS Code o generar con plantuml.jar.

## Interfaces de entrada y salida del sistema

- Entrada:
  - Formularios HTML para crear/editar Solicitud y Trabajador.
  - Archivos adjuntos (PDF/PNG/JPG).
  - Parámetros de filtrado en estadísticas (fechas, trabajador, tipo).
- Salida:
  - Vistas HTML con tablas y gráficos.
  - Exportes: PDF y XLSX descargables.
  - Registros de auditoría en BD.

## Web Services básicos de los procesos

- `GET /api/solicitudes/` — Listar solicitudes (filtros opcionales)
- `POST /api/solicitudes/` — Crear solicitud (payload JSON + multipart adjunto)
- `GET /api/estadisticas/` — Obtener datos para gráficas (JSON)
- `POST /api/export/pdf/` — Generar PDF (acepta imágenes base64 o datos para fallback)

## Base de datos (backup)

- Recomendación: backups diarios en PostgreSQL con `pg_dump` en entorno de producción.
- Folder recomendado para copias: `/backups/` con rotación 7 días.

## Desarrollo e implementación por módulos

- Módulo Trabajadores: modelos, vistas, templates, pruebas unitarias.
- Módulo Solicitudes: validaciones, cálculo de días, adjuntos.
- Módulo Estadísticas: recopilación de datos, generación de gráficos, exportes.
- Módulo Auditoría: registro de acciones con detalles cifrados.

## Formularios digitales (estructura)

Ejemplo: Formulario de Solicitud
- trabajador_id (select)
- tipo (select)
- fecha_inicio (date)
- fecha_fin (date)
- motivo (textarea)
- adjunto (file)

## Módulos integrados y pruebas de instalación

- La aplicación fue desplegada y probada localmente en entorno de desarrollo (Django runserver). Para producción, siga el Manual de Implantación para desplegar con Gunicorn + Nginx o configure el servidor según las políticas de su organización.

## Código y archivos fuentes

- Repositorio contiene código Django, templates, static, scripts de utilidades y archivos de configuración.
- Se entregan fuentes limpias, con comentarios en español y sin credenciales embebidas.

## Informe de testeo / Pruebas realizadas

- Pruebas unitarias básicas sobre modelos y validaciones.
- Pruebas manuales de flujo: crear solicitud, aprobar/rechazar, generar reportes, exportes PDF/XLSX.
- Casos verificados: canvas válido, canvas tainted (fallback), adjuntos inválidos rechazados.

## Manuales técnicos

- Manual de Usuario: guía para crear solicitudes, revisar y generar reportes (ubicado en `/docs/manual_usuario.md`).
- Manual de Implementación: pasos para desplegar en servidor (Gunicorn + Nginx) y restaurar backups (`/docs/manual_implementacion.md`).

**Manuales disponibles en /docs/**:

- [Manual de Usuario](./docs/manual_usuario.md)
- [Manual de Implantación](./docs/manual_implementacion.md)
- [Manual para Mantenedores](./docs/manual_mantenedores.md)
- [Manual del Operador](./docs/manual_operador.md)
- [Manual de Respaldo y Restauración](./docs/manual_respaldo_restauracion.md)
- [Manual de Pruebas / QA](./docs/manual_pruebas.md)

## Documentos de retrospectiva final del proyecto

- Resumen: trabajo desarrollado por única persona utilizando SCRUM adaptado (sprints cortos, reuniones diarias y revisiones). Lecciones aprendidas: importancia de definir paleta de colores compartida, manejar canvas tainted y limitar tamaño de payloads base64.

---

### Anexos y recomendaciones finales

- Generar imagen `erd.png` desde `erd.puml` y colocar en `/docs/` para inclusión en la documentación.
- Crear carpeta `/docs/wireframes/` y añadir capturas de UI.
- Añadir scripts de backup y restauración en `/ops/`.
- Documentar el proceso de generación de exports y las limitaciones por canvas tainted.

---

**Metodología:** SCRUM (Sprints, Backlog, Actas). Desarrolladora: Gabriela Urbina (full responsibility: análisis, diseño, desarrollo, pruebas, despliegue).

**Fecha de creación del documento:** 30/06/2026


