from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def vista_estadisticas(request):
    """Vista placeholder para estadísticas. Reemplazar con lógica real según sea necesario."""
    return render(request, 'gestion_permisos/estadisticas.html', {})
