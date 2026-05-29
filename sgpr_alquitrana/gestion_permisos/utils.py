"""Utilidades de seguridad: cifrado simétrico para campos sensibles.

Usa `FERNET_KEY` desde variables de entorno. Generar una clave segura con:

  python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

Guarde esa clave en la variable de entorno `FERNET_KEY` en producción.
"""
import os
import logging
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
    except InvalidToken:
        logger.exception('Token de cifrado inválido al intentar descifrar')
        return token
