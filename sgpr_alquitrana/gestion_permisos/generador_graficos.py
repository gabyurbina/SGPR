"""Funciones para generar gráficos en Excel y PDF."""

import io
from datetime import datetime
import base64

import matplotlib
matplotlib.use('Agg')  # Backend sin interfaz gráfica
import matplotlib.pyplot as plt

from .estadisticas import (
    obtener_estadisticas_solicitudes,
    obtener_estadisticas_por_tipo,
    obtener_estadisticas_por_estado,
    obtener_estadisticas_por_mes,
    obtener_estadisticas_por_departamento,
)


def generar_grafico_pastel_png(datos, labels, titulo):
    """Genera un gráfico de pastel en PNG y retorna como BytesIO."""
    fig, ax = plt.subplots(figsize=(8, 6))
    colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    ax.pie(datos, labels=labels, autopct='%1.1f%%', colors=colores[:len(datos)], startangle=90)
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
    buffer.seek(0)
    plt.close(fig)
    return buffer


def generar_grafico_barras_png(categorias, datos, titulo, etiqueta_datos='Cantidad'):
    """Genera un gráfico de barras en PNG y retorna como BytesIO."""
    fig, ax = plt.subplots(figsize=(10, 6))
    colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    bars = ax.bar(range(len(categorias)), datos, color=colores[:len(categorias)])
    ax.set_xticks(range(len(categorias)))
    ax.set_xticklabels(categorias, rotation=45, ha='right')
    ax.set_ylabel(etiqueta_datos, fontsize=12)
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    # Agregar valores en las barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
    buffer.seek(0)
    plt.close(fig)
    return buffer


def generar_grafico_lineas_png(meses_dict, titulo):
    """Genera un gráfico de líneas en PNG y retorna como BytesIO."""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x_labels = sorted(list(meses_dict.keys()))
    y_datos = [meses_dict[mes]['total'] for mes in x_labels]
    
    ax.plot(range(len(x_labels)), y_datos, marker='o', linewidth=2, markersize=8, color='#4ECDC4', label='Total')
    ax.fill_between(range(len(x_labels)), y_datos, alpha=0.3, color='#4ECDC4')
    
    ax.set_xlabel('Mes', fontsize=12)
    ax.set_ylabel('Cantidad', fontsize=12)
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.set_xticks(range(len(x_labels)))
    ax.set_xticklabels(x_labels, rotation=45, ha='right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
    buffer.seek(0)
    plt.close(fig)
    return buffer


def grafico_a_base64(buffer):
    """Convierte un BytesIO con PNG a string base64 para insertar en HTML/PDF."""
    return base64.b64encode(buffer.getvalue()).decode('utf-8')


def obtener_graficos_base64():
    """Obtiene todos los gráficos en base64 para incrustación en reportes."""
    
    # Datos por tipo
    por_tipo = obtener_estadisticas_por_tipo()
    tipos = [item['tipo'] for item in por_tipo]
    cantidad_tipo = [item['count'] for item in por_tipo]
    grafico_tipo = generar_grafico_barras_png(tipos, cantidad_tipo, 'Solicitudes por Tipo')
    base64_tipo = grafico_a_base64(grafico_tipo)
    
    # Datos por estado
    por_estado = obtener_estadisticas_por_estado()
    estados = [item['estado'] for item in por_estado]
    cantidad_estado = [item['count'] for item in por_estado]
    grafico_estado = generar_grafico_pastel_png(cantidad_estado, estados, 'Distribución por Estado')
    base64_estado = grafico_a_base64(grafico_estado)
    
    # Datos por departamento
    por_depto = obtener_estadisticas_por_departamento()
    deptos = [item['trabajador__departamento'] or 'Sin departamento' for item in por_depto[:10]]
    cantidad_depto = [item['count'] for item in por_depto[:10]]
    grafico_depto = generar_grafico_barras_png(deptos, cantidad_depto, 'Top 10 Departamentos', 'Solicitudes')
    base64_depto = grafico_a_base64(grafico_depto)
    
    # Datos por mes
    por_mes = obtener_estadisticas_por_mes()
    if por_mes:
        grafico_mes = generar_grafico_lineas_png(por_mes, 'Solicitudes por Mes (últimos 6 meses)')
        base64_mes = grafico_a_base64(grafico_mes)
    else:
        base64_mes = None
    
    return {
        'grafico_tipo': f'data:image/png;base64,{base64_tipo}',
        'grafico_estado': f'data:image/png;base64,{base64_estado}',
        'grafico_depto': f'data:image/png;base64,{base64_depto}',
        'grafico_mes': f'data:image/png;base64,{base64_mes}' if base64_mes else None,
    }
