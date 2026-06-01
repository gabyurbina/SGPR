"""Funciones para generar datos estadísticos."""

from django.db.models import Count, Q
from .models import Solicitud
from datetime import datetime, timedelta


def obtener_estadisticas_solicitudes():
    """Obtiene estadísticas generales de solicitudes."""
    stats = {
        'total_solicitudes': Solicitud.objects.count(),
        'pendientes': Solicitud.objects.filter(estado='PENDIENTE').count(),
        'aprobadas': Solicitud.objects.filter(estado='APROBADO').count(),
        'rechazadas': Solicitud.objects.filter(estado='RECHAZADO').count(),
    }
    return stats


def obtener_estadisticas_por_tipo():
    """Obtiene el conteo de solicitudes por tipo (Permiso, Reposo)."""
    data = Solicitud.objects.values('tipo').annotate(count=Count('id')).order_by('tipo')
    return list(data)


def obtener_estadisticas_por_estado():
    """Obtiene el conteo de solicitudes por estado."""
    data = Solicitud.objects.values('estado').annotate(count=Count('id')).order_by('estado')
    return list(data)


def obtener_estadisticas_por_mes():
    """Obtiene solicitudes por mes (últimos 6 meses)."""
    desde = datetime.now() - timedelta(days=180)
    solicitudes = Solicitud.objects.filter(fecha_creacion__gte=desde)
    
    meses = {}
    for solicitud in solicitudes:
        mes = solicitud.fecha_creacion.strftime('%Y-%m')
        if mes not in meses:
            meses[mes] = {'total': 0, 'aprobadas': 0, 'rechazadas': 0, 'pendientes': 0}
        meses[mes]['total'] += 1
        meses[mes][solicitud.estado.lower()] = meses[mes].get(solicitud.estado.lower(), 0) + 1
    
    return meses


def obtener_estadisticas_por_departamento():
    """Obtiene solicitudes por departamento."""
    data = Solicitud.objects.values('trabajador__departamento').annotate(count=Count('id')).order_by('-count')
    return list(data)
