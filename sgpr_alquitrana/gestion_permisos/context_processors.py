from .models import Trabajador


def user_role_context(request):
    is_trabajador = False
    mostrar_solicitar = False

    if request.user.is_authenticated:
        is_trabajador = Trabajador.objects.filter(user=request.user).exists()
        mostrar_solicitar = is_trabajador and request.user.username != 'admin'

    return {
        'es_trabajador': is_trabajador,
        'mostrar_solicitar': mostrar_solicitar,
    }
