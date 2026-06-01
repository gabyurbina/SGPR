"""Funciones para agregar gráficos a exportaciones Excel y PDF."""

from io import BytesIO
from openpyxl.drawing.image import Image as ExcelImage
from reportlab.platypus import Image as ReportLabImage
from .generador_graficos import (
    generar_grafico_pastel_png,
    generar_grafico_barras_png,
    generar_grafico_lineas_png,
)
from .estadisticas import (
    obtener_estadisticas_por_tipo,
    obtener_estadisticas_por_estado,
    obtener_estadisticas_por_departamento,
    obtener_estadisticas_por_mes,
)


def agregar_graficos_a_excel(hoja, workbook):
    """Agrega gráficos a una hoja de Excel."""
    try:
        # Gráfico 1: Por tipo
        por_tipo = obtener_estadisticas_por_tipo()
        if por_tipo:
            tipos = [item['tipo'] for item in por_tipo]
            cantidad_tipo = [item['count'] for item in por_tipo]
            grafico_tipo = generar_grafico_barras_png(tipos, cantidad_tipo, 'Solicitudes por Tipo')
            img1 = ExcelImage(grafico_tipo)
            img1.width = 400
            img1.height = 250
            hoja.add_image(img1, 'A15')
        
        # Gráfico 2: Por estado
        por_estado = obtener_estadisticas_por_estado()
        if por_estado:
            estados = [item['estado'] for item in por_estado]
            cantidad_estado = [item['count'] for item in por_estado]
            grafico_estado = generar_grafico_pastel_png(cantidad_estado, estados, 'Distribución por Estado')
            img2 = ExcelImage(grafico_estado)
            img2.width = 400
            img2.height = 250
            hoja.add_image(img2, 'K15')
    except Exception as e:
        print(f"Error al agregar gráficos a Excel: {str(e)}")
        pass


def obtener_graficos_para_pdf():
    """Obtiene gráficos como imágenes ReportLab para PDF."""
    graficos = {}
    
    try:
        # Gráfico 1: Por tipo
        por_tipo = obtener_estadisticas_por_tipo()
        if por_tipo:
            tipos = [item['tipo'] for item in por_tipo]
            cantidad_tipo = [item['count'] for item in por_tipo]
            buffer = generar_grafico_barras_png(tipos, cantidad_tipo, 'Solicitudes por Tipo')
            graficos['tipo'] = ReportLabImage(buffer, width=350, height=200)
        
        # Gráfico 2: Por estado
        por_estado = obtener_estadisticas_por_estado()
        if por_estado:
            estados = [item['estado'] for item in por_estado]
            cantidad_estado = [item['count'] for item in por_estado]
            buffer = generar_grafico_pastel_png(cantidad_estado, estados, 'Distribución por Estado')
            graficos['estado'] = ReportLabImage(buffer, width=350, height=200)
        
        # Gráfico 3: Por departamento
        por_depto = obtener_estadisticas_por_departamento()
        if por_depto:
            deptos = [item['trabajador__departamento'] or 'Sin departamento' for item in por_depto[:10]]
            cantidad_depto = [item['count'] for item in por_depto[:10]]
            buffer = generar_grafico_barras_png(deptos, cantidad_depto, 'Top 10 Departamentos', 'Solicitudes')
            graficos['depto'] = ReportLabImage(buffer, width=350, height=200)
        
        # Gráfico 4: Por mes
        por_mes = obtener_estadisticas_por_mes()
        if por_mes:
            buffer = generar_grafico_lineas_png(por_mes, 'Solicitudes por Mes (últimos 6 meses)')
            graficos['mes'] = ReportLabImage(buffer, width=500, height=250)
    
    except Exception as e:
        print(f"Error al obtener gráficos para PDF: {str(e)}")
        pass
    
    return graficos
