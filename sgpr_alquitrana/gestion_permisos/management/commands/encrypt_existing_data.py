from django.core.management.base import BaseCommand
from gestion_permisos.models import Trabajador, Solicitud, Auditoria
from gestion_permisos.utils import encrypt_text

class Command(BaseCommand):
    help = 'Encripta datos existentes en campos configurados (cedula_encrypted, motivo, detalles) una vez aplicadas las migraciones.'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando encriptado de datos existentes...')

        # Trabajadores: generar cedula_encrypted
        t_count = 0
        for t in Trabajador.objects.all():
            try:
                if t.cedula:
                    t.cedula_encrypted = encrypt_text(t.cedula)
                    t.save(update_fields=['cedula_encrypted'])
                    t_count += 1
            except Exception as e:
                self.stderr.write(f'Error cifrando trabajador {t.id}: {e}')
        self.stdout.write(self.style.SUCCESS(f'Cedulas cifradas: {t_count}'))

        # Solicitudes: re-guardar para que el campo EncryptedTextField cifre motivo
        s_count = 0
        for s in Solicitud.objects.all():
            try:
                # reasignar motivo para que get_prep_value lo cifre
                s.save(update_fields=['motivo'])
                s_count += 1
            except Exception as e:
                self.stderr.write(f'Error cifrando solicitud {s.id}: {e}')
        self.stdout.write(self.style.SUCCESS(f'Solicitudes procesadas (motivo): {s_count}'))

        # Auditoria: re-guardar para cifrar detalles
        a_count = 0
        for a in Auditoria.objects.all():
            try:
                a.save(update_fields=['detalles'])
                a_count += 1
            except Exception as e:
                self.stderr.write(f'Error cifrando auditoria {a.id}: {e}')
        self.stdout.write(self.style.SUCCESS(f'Auditorias procesadas (detalles): {a_count}'))

        self.stdout.write(self.style.SUCCESS('Proceso completado.'))
