"""Formularios para la app gestion_permisos.
Incluye validación del tamaño del archivo (5MB máximo) y extensiones.
"""
import os

from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Solicitud, Trabajador


class CedulaAuthenticationForm(AuthenticationForm):
    """Formulario de login que solicita la cédula en lugar del nombre de usuario."""
    username = forms.CharField(
        label='Número Cédula',
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['tipo', 'fecha_inicio', 'fecha_fin', 'motivo', 'adjunto']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'adjunto': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.png,.jpg,.jpeg'}),
        }

    def clean_adjunto(self):
        archivo = self.cleaned_data.get('adjunto')
        if archivo:
            # Limitar tamaño a 5MB
            if archivo.size > 5 * 1024 * 1024:
                raise forms.ValidationError('El archivo excede el tamaño máximo permitido (5MB).')
            # Validar extensiones permitidas
            ext = os.path.splitext(archivo.name)[1].lower()
            allowed = ['.pdf', '.png', '.jpg', '.jpeg']
            if ext not in allowed:
                raise forms.ValidationError(
                    'El archivo que está adjuntando no está permitido, por favor verifique que el archivo que esté cargando sea el correcto.'
                )
        return archivo


class EvaluacionSolicitudForm(forms.Form):
    observaciones_admin = forms.CharField(
        label='Comentario al trabajador',
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        required=True,
        help_text='Este mensaje se mostrará al trabajador solicitante.',
    )


class RegistroTrabajadorForm(forms.ModelForm):
    cedula = forms.CharField(
        label='Cédula',
        max_length=15,
        validators=[RegexValidator(r'^\d+$', 'La cédula solo debe contener números, sin letras ni caracteres especiales.')],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'inputmode': 'numeric',
                'pattern': '[0-9]+',
                'title': 'Solo números',
                'maxlength': '15',
            }
        ),
    )
    nombres = forms.CharField(label='Nombres', widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(label='Apellidos', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    # Registration uses DEFAULT_PASSWORD; users must change at first login.

    class Meta:
        model = Trabajador
        fields = ['cedula', 'cargo', 'departamento']
        widgets = {
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if not cedula.isdigit():
            raise forms.ValidationError('La cédula solo debe contener números, sin letras ni caracteres especiales.')
        if Trabajador.objects.filter(cedula=cedula).exists():
            raise forms.ValidationError('Ya existe un trabajador registrado con esta cédula.')
        return cedula

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Ya existe un usuario registrado con este correo electrónico.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class TrabajadorEditForm(forms.ModelForm):
    cedula = forms.CharField(
        label='Cédula',
        max_length=15,
        validators=[RegexValidator(r'^\d+$', 'La cédula solo debe contener números, sin letras ni caracteres especiales.')],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'inputmode': 'numeric',
                'pattern': '[0-9]+',
                'title': 'Solo números',
                'maxlength': '15',
            }
        ),
    )
    nombres = forms.CharField(label='Nombres', widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(label='Apellidos', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        help_text='Deja vacío si no quieres cambiar la contraseña.',
    )

    class Meta:
        model = Trabajador
        fields = ['cedula', 'cargo', 'departamento']
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'inputmode': 'numeric', 'pattern': '[0-9]*', 'title': 'Solo números'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['nombres'].initial = self.instance.user.first_name
            self.fields['apellidos'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if not cedula.isdigit():
            raise forms.ValidationError('La cédula solo debe contener números, sin letras ni caracteres especiales.')
        if Trabajador.objects.filter(cedula=cedula).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un trabajador registrado con esta cédula.')
        return cedula

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and self.instance and self.instance.user:
            if User.objects.filter(email__iexact=email).exclude(pk=self.instance.user.pk).exists():
                raise forms.ValidationError('Ya existe un usuario registrado con este correo electrónico.')
        return email

    def save(self, commit=True):
        # Guardar primero los datos del trabajador y el usuario asociado.
        trabajador = super().save(commit=False)
        trabajador.user.first_name = self.cleaned_data['nombres']
        trabajador.user.last_name = self.cleaned_data['apellidos']
        correo = self.cleaned_data.get('email')
        if correo:
            trabajador.user.email = correo
        password = self.cleaned_data.get('password')
        if password:
            trabajador.user.set_password(password)
            trabajador.password_reset_required = False
        if commit:
            trabajador.user.save()
            trabajador.save()
        return trabajador

class EliminarTrabajadorForm(forms.Form):
    motivo = forms.CharField(
        label='Motivo de eliminación',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escriba la razón por la cual se elimina este trabajador...'}),
        required=True,
        help_text='Debe indicar el motivo de la eliminación para dejar el registro en auditoría.',
    )