# Backup script (PowerShell) — placeholder
# Requiere: pg_dump en PATH y variables de entorno configuradas: $env:PGHOST, $env:PGUSER, $env:PGPASSWORD, $env:PGDATABASE

$backupDir = "D:\Backups\sgpr"  # Ajustar según política de la organización
if (!(Test-Path $backupDir)) { New-Item -ItemType Directory -Path $backupDir -Force }

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$filename = "sgpr_backup_$timestamp.sql"
$filepath = Join-Path $backupDir $filename

Write-Host "Iniciando backup: $filepath"

# Comando de ejemplo para PostgreSQL; ajustar opciones según necesidades
pg_dump --format=custom --file="$filepath" --no-owner --no-acl

if ($LASTEXITCODE -eq 0) {
    Write-Host "Backup completado: $filepath"
} else {
    Write-Error "Backup fallido. Código: $LASTEXITCODE"
}

# Rotación: conservar últimos 7 archivos
Get-ChildItem -Path $backupDir -Filter "sgpr_backup_*.sql" | Sort-Object LastWriteTime -Descending | Select-Object -Skip 7 | Remove-Item -Force -ErrorAction SilentlyContinue
