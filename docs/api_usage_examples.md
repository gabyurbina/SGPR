# Uso de API - SGPR

## Crear Trabajador (curl)

curl -X POST http://localhost:8000/api/trabajadores/ \
  -H "Content-Type: application/json" \
  -d '{"cedula":"12345678","nombres":"Juan","apellidos":"Perez","cargo":"Auxiliar","email":"juan@ejemplo.com"}'

## Crear Solicitud (multipart)

curl -X POST http://localhost:8000/api/solicitudes/ \
  -F "trabajador_id=1" \
  -F "tipo=PERMISO" \
  -F "fecha_inicio=2026-06-01" \
  -F "fecha_fin=2026-06-02" \
  -F "motivo=Asunto" \
  -F "adjunto=@/path/to/file.pdf"

