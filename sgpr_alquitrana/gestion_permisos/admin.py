from django.contrib import admin
from django import forms
from .models import Trabajador, Solicitud, Auditoria


class TrabajadorAdminForm(forms.ModelForm):
    new_password = forms.CharField(
        label='Nueva contraseña (dejar en blanco para no cambiar)',
        widget=forms.PasswordInput,
        required=False,
        help_text='Ingrese una nueva contraseña para el usuario asociado si desea cambiarla desde el admin.',
    )

    class Meta:
        model = Trabajador
        fields = '__all__'


@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    change_list_template = 'admin/gestion_permisos/trabajador/change_list.html'
    form = TrabajadorAdminForm
    list_display = ('user', 'cedula', 'cargo', 'departamento', 'password_reset_required')
    list_filter = ('cargo', 'departamento', 'password_reset_required')
    search_fields = ('user__username', 'cedula', 'user__last_name')

    def save_model(self, request, obj, form, change):
        # Si se indicó nueva contraseña, aplicarla al User relacionado
        new_password = form.cleaned_data.get('new_password')
        if new_password:
            user = obj.user
            user.set_password(new_password)
            user.save()
            obj.password_reset_required = False
        super().save_model(request, obj, form, change)


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('id', 'trabajador', 'tipo', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'tipo')
    search_fields = ('trabajador__cedula', 'trabajador__user__last_name')


@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ('fecha_hora', 'usuario', 'accion', 'tabla_afectada', 'registro_id')
    readonly_fields = ('fecha_hora',)
