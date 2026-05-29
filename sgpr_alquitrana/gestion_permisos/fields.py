from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils import encrypt_text, decrypt_text


class EncryptedTextField(models.TextField):
    description = _('Texto encriptado (Fernet)')

    def get_prep_value(self, value):
        # Antes de guardar en la base, cifrar
        if value is None:
            return value
        if value == '':
            return ''
        return encrypt_text(str(value))

    def from_db_value(self, value, expression, connection):
        # Al leer de la base, intentar descifrar; si no es un token válido, devolver tal cual
        if value is None:
            return value
        try:
            return decrypt_text(value)
        except Exception:
            return value

    def to_python(self, value):
        # Cuando Django convierte el valor a python
        if value is None:
            return value
        # Si parece un token (base64-like) intentaremos descifrar
        try:
            return decrypt_text(value)
        except Exception:
            return value
