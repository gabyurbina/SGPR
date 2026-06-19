#!/usr/bin/env python
"""Script de gestión para el proyecto Django.
Este archivo permite ejecutar comandos como `runserver`, `migrate`, etc."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sgpr_alquitrana.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Asegúrese de que esté instalado y disponible en su PYTHONPATH."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
