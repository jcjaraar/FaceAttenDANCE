# Script de backup para FaceAttenDANCE (Windows PowerShell)

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "💾 FaceAttenDANCE - Backup Script" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

# Configuración
$BACKUP_DIR = ".\backups"
$DATE = Get-Date -Format "yyyyMMdd_HHmmss"
$BACKUP_FILE = "faceattendance_backup_$DATE.zip"

# Crear directorio de backup si no existe
if (-not (Test-Path $BACKUP_DIR)) {
    New-Item -ItemType Directory -Path $BACKUP_DIR | Out-Null
}

Write-Host "📁 Creando backup en $BACKUP_DIR\$BACKUP_FILE"

# Archivos a incluir
$exclude = @(
    "__pycache__",
    "*.pyc",
    ".git",
    "venv",
    ".venv",
    "backups"
)

$files = Get-ChildItem -Path . -Exclude $exclude -Recurse

try {
    Compress-Archive -Path $files -DestinationPath "$BACKUP_DIR\$BACKUP_FILE" -Force
    Write-Host "✅ Backup completado: $BACKUP_FILE" -ForegroundColor Green

    # Tamaño del archivo
    $size = (Get-Item "$BACKUP_DIR\$BACKUP_FILE").Length / 1MB
    Write-Host "   Tamaño: $([math]::Round($size, 2)) MB"

    # Limpiar backups antiguos (mantener últimos 10)
    Write-Host "🧹 Limpiando backups antiguos..."
    $backups = Get-ChildItem -Path $BACKUP_DIR -Filter "*.zip" | Sort-Object LastWriteTime -Descending
    if ($backups.Count -gt 10) {
        $backups | Select-Object -Skip 10 | ForEach-Object {
            Remove-Item $_.FullName -Force
            Write-Host "   Eliminado: $($_.Name)"
        }
    }

    Write-Host "✅ Proceso completado" -ForegroundColor Green

} catch {
    Write-Host "❌ Error al crear backup: $_" -ForegroundColor Red
    exit 1
}
