#!/bin/bash
# Daily Backup Script for Farm Assessments
# Runs via LaunchAgent at 10pm daily
# Only backs up critical small files to Google Drive

# Configuration
SOURCE_DIR="/Volumes/T7 Shield/05_FARM_ASSESSMENT"
DEST_DIR="$HOME/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GIS_Backups/farms"
LOG_FILE="$HOME/gis_backup.log"
MAX_SIZE="100M"

# Create destination if it doesn't exist
mkdir -p "$DEST_DIR"

# Log start
echo "$(date '+%Y-%m-%d %H:%M:%S') - Starting farm backup" >> "$LOG_FILE"

# Check if source exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ERROR: Source directory not found" >> "$LOG_FILE"
    exit 1
fi

# Count files before backup
BEFORE_COUNT=$(find "$DEST_DIR" -type f | wc -l)

# Perform backup - only specific file types
rsync -av \
  --include="*/" \
  --include="*.pdf" \
  --include="*.kmz" \
  --include="*.kml" \
  --include="*.xml" \
  --include="*.json" \
  --include="RECIPE.yml" \
  --exclude="*" \
  --max-size="$MAX_SIZE" \
  "$SOURCE_DIR/" \
  "$DEST_DIR/" 2>&1 | tail -n 20 >> "$LOG_FILE"

# Check if rsync succeeded
if [ $? -eq 0 ]; then
    AFTER_COUNT=$(find "$DEST_DIR" -type f | wc -l)
    NEW_FILES=$((AFTER_COUNT - BEFORE_COUNT))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - SUCCESS: Backup complete. $NEW_FILES new files." >> "$LOG_FILE"
    
    # Alert if backup is getting large
    BACKUP_SIZE=$(du -sh "$DEST_DIR" | cut -f1)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Total backup size: $BACKUP_SIZE" >> "$LOG_FILE"
else
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ERROR: Backup failed" >> "$LOG_FILE"
    
    # Send alert (you could add email/notification here)
    osascript -e 'display notification "GIS backup failed - check log" with title "Backup Error"'
fi

# Rotate log if it's getting large (keep last 1000 lines)
LOG_LINES=$(wc -l < "$LOG_FILE")
if [ "$LOG_LINES" -gt 1000 ]; then
    tail -n 500 "$LOG_FILE" > "$LOG_FILE.tmp"
    mv "$LOG_FILE.tmp" "$LOG_FILE"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Log rotated" >> "$LOG_FILE"
fi