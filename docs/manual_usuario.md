# Manual de Usuario - SGPR

## Introducción
Guía de uso para usuarios finales (trabajadores, revisores y administradores) del sistema SGPR.

## Acceso
1. URL: http://<servidor>:8000/
2. Ingrese usuario y contraseña provistos por el administrador.
3. En caso de olvido de contraseña, use el flujo de recuperación o contacte al administrador.

## Navegación principal
- Menú: Inicio, Trabajadores, Solicitudes, Estadísticas, Reportes, Auditoría, Mi Perfil.

## Funcionalidades principales
### 1) Registrar una solicitud
- Ir a: Solicitudes → Nueva solicitud
- Completar: trabajador (si aplica), tipo, fecha inicio, fecha fin, motivo, adjuntar justificante (PDF/PNG/JPG/JPEG)
- Validaciones: fecha_inicio ≤ fecha_fin; adjuntos con extensiones permitidas.
- Guardar: la solicitud queda en estado PENDIENTE.

### 2) Revisar solicitudes (revisor)
- Filtrar por estado, trabajador o fecha.
- Abrir solicitud y usar botones Aprobar / Rechazar.
- Al aprobar/rechazar, añadir observaciones si se desea.

### 3) Panel de estadísticas
- Ir a: Estadísticas
- Usar filtros: rango de fechas, trabajador, tipo.
- Los gráficos se muestran en pantalla con leyenda y colores.
- Exportes:
  - Descargar XLSX: botón "Exportar XLSX".
  - Descargar PDF: botón "Exportar PDF" (si no hay filtros aplicados, el botón estará deshabilitado).

Nota sobre exportes: El PDF intenta incorporar el gráfico mostrado. Si el navegador impide la captura del canvas (tainted), el sistema generará el gráfico en servidor como fallback; el resultado visual puede variar levemente.

### 4) Reportes del trabajador
- Acceder a: Trabajadores → seleccionar trabajador → Reportes
- Genera PDF/XLSX con información del trabajador y detalle de solicitudes.
- El encabezado incluye: "Reporte del trabajador: — Cédula: <número>" (la cédula se muestra solo aquí, no dentro del gráfico).

### 5) Auditoría
- Los registros de auditoría están disponibles para usuarios con permisos.
- Permiten ver acciones críticas, quién las realizó y la fecha.
- Los detalles están cifrados en BD y se muestran desencriptados en la UI según permisos.

## Preguntas frecuentes (FAQ)
- Q: ¿Por qué no aparece el gráfico en el PDF? 
  A: Si el navegador bloqueó la captura del canvas por contenido cross-origin, el backend genera una imagen alternativa. Verifique recursos externos con CORS configurado.

- Q: ¿Qué formatos soporta el adjunto? 
  A: PDF, PNG, JPG, JPEG.

## Contacto y soporte
Contactar al administrador del sistema o al equipo de soporte con la referencia del error y capturas de pantalla.

---

*Fin del Manual de Usuario.*
