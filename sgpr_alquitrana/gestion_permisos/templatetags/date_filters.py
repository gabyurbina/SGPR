import datetime

from django import template

register = template.Library()


def format_datetime(value):
    """Formato uniforme para fechas y horas: DD-MM-YYYY hh:mm:ss a.m./p.m."""
    if value is None:
        return ''

    if isinstance(value, datetime.date) and not isinstance(value, datetime.datetime):
        value = datetime.datetime.combine(value, datetime.time.min)

    if not isinstance(value, datetime.datetime):
        return str(value)

    formatted = value.strftime('%d-%m-%Y %I:%M:%S %p')
    return formatted.replace('AM', 'a.m.').replace('PM', 'p.m.')


register.filter('format_datetime', format_datetime)
