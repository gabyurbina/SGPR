from django.shortcuts import redirect
from django.urls import reverse


class PasswordResetRequiredMiddleware:
    """Redirige a la página de cambio de contraseña si el trabajador tiene obligatorio el cambio."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            password_change_url = reverse('cambiar_contrasena')
            login_url = reverse('login')
            # Si el trabajador debe cambiar la contraseña y está navegando fuera
            # de las páginas de login/cambio de contraseña o del admin, redirigimos.
            if (
                hasattr(request.user, 'trabajador')
                and request.user.trabajador.password_reset_required
                and request.user.username != 'trabajador'
                and request.path not in [password_change_url, login_url, reverse('logout')]
                and not request.path.startswith('/admin/')
            ):
                return redirect('cambiar_contrasena')
        return self.get_response(request)
