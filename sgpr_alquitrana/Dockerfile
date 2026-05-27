FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el proyecto
COPY . /app/

ENV DJANGO_SETTINGS_MODULE=sgpr_alquitrana.settings

RUN adduser --disabled-password deploy || true
USER deploy

EXPOSE 8000

CMD ["gunicorn", "sgpr_alquitrana.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
