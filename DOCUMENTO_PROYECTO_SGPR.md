# Documento Completo del Proyecto - SGPR

**Proyecto:** Sistema de Gestión de Permisos y Reportes (SGPR)

**Desarrollado bajo:** Metodología SCRUM

**Responsable del desarrollo:** Gabriela Urbina (análisis, diseño, desarrollo, pruebas e implementación)

**Periodo de Sprint:** 01/04/2026 — 30/06/2026

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

---

## 8. Stakeholders (Interesados)

- Administrador del sistema (Lic. Marbella Canelón)
- Recursos Humanos (Francismar Marchan)
- Trabajadores (usuarios finales)
- Auditoría interna
- Equipo de soporte/IT (Ing. Trino Vera)
- Desarrollo principal (Gabriela Urbina)

## 8.1 Usuarios

- Administrador del sistema (Lic Marbella Canelón): responsable de la configuración, administración de roles y políticas.
- Recursos Humanos (Francismar Marchan): principal actor que gestiona solicitudes, aprobaciones y reportes.
- Trabajadores (usuarios finales): generan solicitudes de permisos y consultan su historial.
- Auditoría interna: revisa registros y asegura cumplimiento normativo.
- Equipo de soporte/IT (Ing. Trino Vera): mantiene la infraestructura, despliegues y backups.

## 8.2 Roles de los Interesados (Scrum)

- Product Owner: Recursos Humanos (Francismar Marchan). Representa la voz del cliente, prioriza el backlog del producto y valida el valor entregado.
- Scrum Master / Facilitador: Administrador del sistema (Lic Marbella Canelón). Facilita el proceso Scrum, elimina impedimentos y asegura que el equipo siga buenas prácticas.
- Development Team: Gabriela Urbina (desarrolladora principal), Equipo de soporte/IT (Ing. Trino Vera) y el equipo técnico. Construyen, despliegan y mantienen el producto, asegurando calidad y entrega continua.
- Stakeholders clave: Trabajadores (usuarios finales) y Auditoría interna. Proveen retroalimentación, validan requisitos y evalúan el cumplimiento de necesidades.

## 8.2.1 Medios de comunicación y relaciones de la desarrolladora principal

- Gabriela Urbina mantiene comunicación directa con Recursos Humanos para validar requisitos funcionales, priorizar solicitudes y ajustar reportes.
- Se relaciona con el Administrador del sistema para coordinar accesos, permisos, y requerimientos de infraestructura y seguridad.
- Trabaja con el Equipo de soporte/IT para desplegar el sistema, gestionar backups y resolver incidencias técnicas.
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

### Equipo de soporte/IT
- Interés en despliegues consistentes y documentación clara.
- Interés en detectar y resolver incidentes rápido.
- Interés en mantener el rendimiento y disponibilidad del sistema.

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

### Equipo de soporte/IT
- Necesidades: despliegues reproducibles, acceso a logs y métricas, procedimientos de recuperación y monitoreo.
- Producto: documentación de despliegue (Gunicorn+Nginx), scripts de backup, endpoints de salud y logs centralizados.
- Valor: despliegues más rápidos y seguros, menor tiempo de inactividad y mejor respuesta ante incidentes.

---

## 9. Historias de usuario / Casos de uso

- HU-001: Registrar trabajador.
- HU-002: Crear solicitud de permiso con adjunto.
- HU-003: Visualizar y filtrar solicitudes.
- HU-004: Aprobar o rechazar solicitud con observaciones.
- HU-005: Generar reporte PDF/XLSX del trabajador con gráficos.
- HU-006: Consultar registro de auditoría por usuario/tabla.

Para cada HU se documenta: actor, precondición, flujo principal, excepciones, postcondición.

---

## 10. Requerimientos funcionales (selección principal)

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

---

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

- Se asume que el entorno de desarrollo y producción dispone de Python 3.11+ y las dependencias definidas en `requirements.txt`.
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

## 12. Backlog del Producto (epicas y user stories principales)

- Épica: Gestión de Trabajadores
  - US-101: Implementar modelo Trabajador y enlace con User
  - US-102: Formulario y listados
- Épica: Solicitudes
  - US-201: Crear Solicitud, validaciones, adjuntos
  - US-202: Calculo de días y reglas de feriados
- Épica: Reportes y Estadísticas
  - US-301: Chart.js en UI
  - US-302: Export PDF (cliente+servidor)
  - US-303: Export XLSX
- Épica: Auditoría
  - US-401: Registrar acciones con detalles cifrados

---

## 13. Sprint Backlog (Periodo: 01/04/2026 → 30/06/2026)

Este periodo abarca 3 meses. Se propone dividir en sprints de 2 semanas. Resumen:

- Sprint 1 (01/04 — 14/04): Modelos y configuración base
  - Implementar modelos: Trabajador, Solicitud, Auditoria
  - Configuración Django y entorno virtual básico
  - Pruebas unitarias de modelos

- Sprint 2 (15/04 — 28/04): Formularios y CRUD
  - Formulario Solicitud y validaciones
  - Adjuntos y validación de extensiones
  - Encriptación de campos

- Sprint 3 (29/04 — 12/05): Estadísticas UI
  - Integrar Chart.js, filtros, paleta de colores
  - Ajustes visuales y pruebas manuales

- Sprint 4 (13/05 — 26/05): Exportes PDF
  - Captura canvas client-side y envío base64
  - Implementar fallback server-side (matplotlib+ReportLab)
  - Pruebas de exportes y ajustes de tamaño/espaciado

- Sprint 5 (27/05 — 09/06): Auditoría y seguridad
  - Registro de auditoría en acciones críticas
  - Revisar cifrado y gestión de claves (env vars)

- Sprint 6 (10/06 — 23/06): Deploy y pruebas finales
  - Ajustes de despliegue en servidor, scripts backup
  - Pruebas de integración y corrección de bugs

- Buffer/Entrega (24/06 — 30/06): Documentación final, manuales, retrospectiva y entrega al cliente.

(Tareas detalladas y estimaciones se registran en el backlog del proyecto).

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

## 21. Desarrollo e implementación de módulos (estado resumido)

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
- Código documentado en español; no contiene credenciales.

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

**Fecha de generación del documento:** 2026-06-03


---

*Fin del documento.*
