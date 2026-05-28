from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from gestion_permisos.models import Trabajador, Solicitud
from django.utils import timezone
import random


class Command(BaseCommand):
    help = 'Crea datos de ejemplo: usuarios, trabajadores y solicitudes.'

    def handle(self, *args, **options):
        # Crear usuarios de ejemplo
        admin, created = User.objects.get_or_create(username='admin_seed', defaults={'email':'admin_seed@example.com'})
        if created:
            admin.set_password('adminseedpass')
            admin.is_staff = True
            admin.is_superuser = False
            admin.save()

        for i in range(1,6):
            username = f'user{i}'
            u, created = User.objects.get_or_create(username=username, defaults={'email':f'{username}@gmail.com'})
            if created:
                u.set_password('userpass')
                u.save()
            Trabajador.objects.get_or_create(user=u, cedula=f'V10000{i}', cargo='Docente')

        trabajadores = list(Trabajador.objects.all())
        tipos = ['PERMISO', 'REPOSO']
        motivos = ['Cita médica', 'Emergencia familiar', 'Asuntos personales']

        # Crear solicitudes de ejemplo
        for i in range(10):
            t = random.choice(trabajadores)
            inicio = timezone.now().date()
            fin = inicio
            Solicitud.objects.create(
                trabajador=t,
                tipo=random.choice(tipos),
                fecha_inicio=inicio,
                fecha_fin=fin,
                motivo=random.choice(motivos),
            )

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo creados. Usuarios: admin_seed,user1..user5 (contraseña: userpass)'))
