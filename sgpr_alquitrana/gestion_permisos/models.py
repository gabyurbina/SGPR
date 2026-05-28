"""Modelos de datos para SGPR: Trabajador, Solicitud y Auditoria.
Código sencillo y comentado para principiantes.
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import os


def validar_extension_archivo(value):
    """Valida que la extensión del archivo esté permitida.
    Permitimos .pdf, .png, .jpg, .jpeg
    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Solo se permiten archivos PDF, PNG, JPG o JPEG.')


class Trabajador(models.Model):
    """Información del trabajador vinculada a un `User` de Django."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=15, unique=True)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100, default='', verbose_name='Ubicación Administrativa')
    password_reset_required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.cedula}"


class Solicitud(models.Model):
    """Modelo que representa una solicitud de permiso o reposo."""
    ESTADOS = (
        ('PENDIENTE', 'Pendiente'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
    )
    TIPOS = (
        ('PERMISO', 'Permiso General'),
        ('REPOSO', 'Reposo Médico'),
        ('PERMISO_CUIDO_MATERNO', 'Permiso por Cuidado Materno'),
        ('PERMISO_CUIDO_PATERNO', 'Permiso por Cuidado Paterno'),
        ('PERMISO_DEPORTIVO', 'Permiso Deportivo'),
        ('INASISTENCIA_INJUSTIFICADA', 'Inasistencia Injustificada'),
        ('INASISTENCIA_JUSTIFICADA', 'Inasistencia Justificada'),
    )

    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='solicitudes')
    tipo = models.CharField(max_length=30, choices=TIPOS)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    motivo = models.TextField()
    adjunto = models.FileField(upload_to='justificantes/', validators=[validar_extension_archivo], null=True, blank=True)
    dias_continuos = models.IntegerField(default=0)
    dias_laborables = models.IntegerField(default=0)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='PENDIENTE')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    revisado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='revisiones')
    observaciones_admin = models.TextField(null=True, blank=True)

    def _easter_sunday(self, year):
        """Calcula la fecha de Domingo de Resurrección para el año dado."""
        from datetime import date

        a = year % 19
        b = year // 100
        c = year % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1
        return date(year, month, day)

    def _feriados_venezuela(self, year):
        """Devuelve un conjunto de feriados oficiales en Venezuela para un año determinado."""
        from datetime import date, timedelta

        easter = self._easter_sunday(year)
        carn_monday = easter - timedelta(days=48)
        carn_tuesday = easter - timedelta(days=47)
        good_friday = easter - timedelta(days=2)

        return {
            date(year, 1, 1),
            date(year, 4, 19),
            date(year, 5, 1),
            date(year, 6, 24),
            date(year, 7, 5),
            date(year, 7, 24),
            date(year, 10, 12),
            date(year, 12, 24),
            date(year, 12, 25),
            date(year, 12, 31),
            carn_monday,
            carn_tuesday,
            good_friday,
        }

    def _contar_dias_laborables(self):
        """Cuenta los días laborables entre fecha_inicio y fecha_fin, excluyendo fines de semana y feriados."""
        from datetime import timedelta

        dias = 0
        current = self.fecha_inicio
        while current <= self.fecha_fin:
            if current.weekday() < 5 and current not in self._feriados_venezuela(current.year):
                dias += 1
            current += timedelta(days=1)
        return dias

    def clean(self):
        """Validación: la fecha de inicio no puede ser mayor que la de fin."""
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_inicio > self.fecha_fin:
                raise ValidationError('La fecha de inicio no puede ser posterior a la fecha de finalización.')
            self.dias_continuos = (self.fecha_fin - self.fecha_inicio).days + 1
            self.dias_laborables = self._contar_dias_laborables()

    def save(self, *args, **kwargs):
        """Asegura que los días se actualicen antes de guardar."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo} - {self.trabajador.user.last_name} ({self.estado})"


class Auditoria(models.Model):
    """Registro de auditoría para acciones críticas del sistema."""
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    accion = models.CharField(max_length=255)
    tabla_afectada = models.CharField(max_length=100)
    registro_id = models.IntegerField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    detalles = models.TextField()

    class Meta:
        verbose_name_plural = "Registros de Auditoría"
        ordering = ['-fecha_hora']

    def __str__(self):
        return f"{self.fecha_hora} - {self.usuario_nombre_completo} - {self.accion}"

    @property
    def usuario_nombre_completo(self):
        if self.usuario:
            full_name = self.usuario.get_full_name().strip()
            return full_name if full_name else self.usuario.username
        return 'Sistema'
