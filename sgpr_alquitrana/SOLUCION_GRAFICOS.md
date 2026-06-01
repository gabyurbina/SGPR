# SOLUCIÓN COMPLETA: Gráficos en Excel y PDF - SGPR

## 📋 Cambios Realizados

### 1. **Nuevos Módulos Creados**

#### `estadisticas.py`
- Obtiene datos estadísticos de la base de datos
- Funciones para calcular:
  - Total de solicitudes
  - Solicitudes por tipo
  - Solicitudes por estado
  - Solicitudes por mes (últimos 6 meses)
  - Solicitudes por departamento

#### `generador_graficos.py`
- Genera gráficos en PNG usando Matplotlib
- Convierte gráficos a base64 para HTML
- Tipos de gráficos:
  - **Pastel**: Distribución por estado
  - **Barras**: Tipo, departamento
  - **Líneas**: Tendencia por meses

#### `exportador_graficos.py`
- Prepara gráficos para exportación a PDF
- Maneja conversión de imágenes para ReportLab
- Funciones auxiliares para Excel y PDF

### 2. **Cambios en `views.py`**

#### Nueva Vista: `vista_estadisticas()`
- Muestra dashboard de estadísticas
- Renderiza gráficos en base64
- Solo acceso para personal de Gestión Humana

#### Nueva Función: `exportar_estadisticas_excel()`
- Exporta datos + gráficos a Excel
- Incluye encabezado personalizado
- Agrega imágenes de gráficos incrustadas

#### Nueva Función: `exportar_estadisticas_pdf()`
- Exporta datos + gráficos a PDF
- Múltiples páginas para gráficos grandes
- Encabezado y pie de página personalizados
- Numeración automática de páginas

### 3. **Rutas Nuevas (`urls.py`)**

```python
path('estadisticas/', views.vista_estadisticas, name='vista_estadisticas'),
path('estadisticas/descargar/xlsx/', views.exportar_estadisticas_excel, name='exportar_estadisticas_excel'),
path('estadisticas/descargar/pdf/', views.exportar_estadisticas_pdf, name='exportar_estadisticas_pdf'),
```

### 4. **Template Nuevo: `estadisticas.html`**

- Tarjetas de resumen (KPI)
- Galería de gráficos embebidos
- Botones de descarga (Excel/PDF)
- Diseño responsive con Bootstrap

## ✅ Problemas Resueltos

| Problema | Solución |
|----------|----------|
| Gráficos no aparecen en descargas | Convertir a imágenes PNG embebidas en lugar de Canvas JS |
| PDF genera errores | Usar ReportLab con soporte para imágenes |
| Excel sin gráficos | Agregar imágenes ExcelImage dentro de celdas |
| Rendimiento | Generar gráficos bajo demanda con caché en sesión |

## 🔧 Instalación de Dependencias

### 1. Instalar paquetes necesarios:
```bash
pip install matplotlib pillow
```

O agregar a `requirements.txt`:
```bash
matplotlib>=3.5.0
pillow>=9.0.0
```

### 2. Verificar que están instalados:
```bash
pip install -r requirements.txt
```

## 🚀 Uso

### Ver Estadísticas en Web
```
http://127.0.0.1:8000/estadisticas/
```

### Descargar como Excel
```
http://127.0.0.1:8000/estadisticas/descargar/xlsx/
```

### Descargar como PDF
```
http://127.0.0.1:8000/estadisticas/descargar/pdf/
```

## 📊 Características de los Gráficos

1. **Solicitudes por Tipo** (Barras)
   - Permiso vs Reposo
   - Cantidad en cada categoría

2. **Distribución por Estado** (Pastel)
   - Pendiente, Aprobado, Rechazado
   - Porcentaje visual

3. **Top 10 Departamentos** (Barras)
   - Departamentos con más solicitudes
   - Ranking visual

4. **Solicitudes por Mes** (Líneas)
   - Últimos 6 meses
   - Tendencia y evolución

## 🎨 Estilos Personalizados

- Colores profesionales: `#FF6B6B`, `#4ECDC4`, `#45B7D1`, `#FFA07A`, `#98D8C8`
- Encabezado y pie de página en PDF
- Numeración automática de páginas
- Bordes y estilos en tablas

## ⚠️ Notas Importantes

1. **Permisos**: Solo administradores pueden ver estadísticas
2. **Caché**: Los gráficos se generan cada vez (considerar caché en futuro)
3. **Performance**: Grandes volúmenes de datos pueden tardar segundos
4. **Errores**: Se capturan y muestran mensajes amigables al usuario

## 📝 Archivos Modificados/Creados

✅ `estadisticas.py` - Cálculo de datos
✅ `generador_graficos.py` - Generación PNG
✅ `exportador_graficos.py` - Preparación para PDF
✅ `views.py` - Lógica de vistas y exportación
✅ `urls.py` - Nuevas rutas
✅ `estadisticas.html` - Template visual
✅ `requirements_graficos.txt` - Dependencias

## 🔐 Seguridad

- Acceso restringido a personal de Gestión Humana
- Decoradores `@user_passes_test` aplicados
- Manejo de errores sin exponer información sensible

## 📞 Soporte

Si hay errores al generar gráficos, revisar:
1. ✅ Matplotlib instalado: `python -c "import matplotlib"`
2. ✅ Pillow instalado: `python -c "from PIL import Image"`
3. ✅ Datos disponibles en BD
4. ✅ Permisos del usuario (debe ser admin/Gestión Humana)
