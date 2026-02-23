#!/bin/bash
# Script de backup para FaceAttenDANCE

echo "========================================="
echo "💾 FaceAttenDANCE - Backup Script"
echo "========================================="

# Configuración
BACKUP_DIR="./backups"
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="faceattendance_backup_$DATE.tar.gz"

# Crear directorio de backup si no existe
mkdir -p $BACKUP_DIR

echo "📁 Creando backup en $BACKUP_DIR/$BACKUP_FILE"

# Archivos a incluir
tar -czf "$BACKUP_DIR/$BACKUP_FILE" \
    --exclude="__pycache__" \
    --exclude="*.pyc" \
    --exclude=".git" \
    --exclude="venv" \
    --exclude=".venv" \
    --exclude="$BACKUP_DIR" \
    . 2>/dev/null

# Verificar resultado
if [ $? -eq 0 ]; then
    echo "✅ Backup completado: $BACKUP_FILE"
    echo "   Tamaño: $(du -h "$BACKUP_DIR/$BACKUP_FILE" | cut -f1)"
else
    echo "❌ Error al crear backup"
    exit 1
fi

# Limpiar backups antiguos (mantener últimos 10)
echo "🧹 Limpiando backups antiguos..."
cd $BACKUP_DIR
ls -t *.tar.gz | tail -n +11 | xargs -r rm

echo "✅ Proceso completado"