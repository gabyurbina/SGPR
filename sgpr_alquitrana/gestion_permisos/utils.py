"""Utilidades de seguridad: cifrado simétrico para campos sensibles.

Usa `FERNET_KEY` desde variables de entorno. Generar una clave segura con:

  python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

Guarde esa clave en la variable de entorno `FERNET_KEY` en producción."""

import os
import logging
import binascii
from cryptography.fernet import Fernet, InvalidToken

logger = logging.getLogger(__name__)


def _get_fernet():
    key = os.environ.get('FERNET_KEY')
    if not key:
        # No bloquear en desarrollo, pero advertir.
        logger.warning('FERNET_KEY no encontrada en entorno; se generará una clave temporal (no usar en producción)')
        return Fernet(Fernet.generate_key())
    return Fernet(key.encode() if isinstance(key, str) else key)


def encrypt_text(plain_text: str) -> str:
    if plain_text is None:
        return ''
    f = _get_fernet()
    token = f.encrypt(plain_text.encode('utf-8'))
    return token.decode('utf-8')


def decrypt_text(token: str) -> str:
    if not token:
        return ''
    f = _get_fernet()
    try:
        plain = f.decrypt(token.encode('utf-8'))
        return plain.decode('utf-8')
    except (InvalidToken, binascii.Error, ValueError) as e:
        # No mostrar traza completa para tokens inválidos (puede ocurrir por datos no cifrados
        # o keys incompatibles). Registrar aviso con información mínima y devolver el valor
        # original para que el resto de la aplicación pueda manejarlo.
        try:
            preview = (token[:32] + '...') if isinstance(token, str) and len(token) > 32 else token
        except Exception:
            preview = '<no-preview>'
        logger.warning("No se pudo descifrar token (no válido o padding incorrecto): %s; error=%s", preview, str(e))
        return token