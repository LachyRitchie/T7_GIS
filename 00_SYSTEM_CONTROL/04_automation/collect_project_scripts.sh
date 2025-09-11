#!/bin/bash
# Script Collection System for T7 Shield
# Purpose: Backup all project scripts to Git-tracked location
# Date: 2025-01-21

set -e

echo "======================================"
echo "PROJECT SCRIPT COLLECTION"
echo "======================================"
echo ""

# Configuration
T7_ROOT="/Volumes/T7 Shield"
BACKUP_DIR="$T7_ROOT/00_SYSTEM_CONTROL/project_scripts"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="$BACKUP_DIR/collection_log.txt"

# Create backup directory structure
mkdir -p "$BACKUP_DIR/03_DATA_PROJECTS"
mkdir -p "$BACKUP_DIR/04_FARM_ASSESSMENT"
mkdir -p "$BACKUP_DIR/logs"

echo "$(date): Starting script collection" >> "$LOG_FILE"

# Function to collect scripts from a directory
collect_scripts() {
    local source_dir="$1"
    local dest_base="$2"
    local count=0
    
    echo "Scanning $source_dir..."
    
    # Find all script files
    while IFS= read -r -d '' file; do
        # Get relative path
        rel_path="${file#$source_dir/}"
        
        # Create destination directory
        dest_dir="$dest_base/$(dirname "$rel_path")"
        mkdir -p "$dest_dir"
        
        # Copy file
        cp "$file" "$dest_dir/"
        ((count++))
        
        echo "  ✓ $(basename "$file")"
    done < <(find "$source_dir" -type f \( \
        -name "*.sh" -o \
        -name "*.py" -o \
        -name "*.sql" -o \
        -name "*.r" -o \
        -name "*.R" -o \
        -name "Makefile" -o \
        -name "*.yml" -o \
        -name "*.yaml" -o \
        -name "*.json" \
    \) -print0 2>/dev/null)
    
    echo "  Collected $count scripts"
    echo ""
    
    return $count
}

# Function to collect documentation
collect_docs() {
    local source_dir="$1"
    local dest_base="$2"
    local count=0
    
    echo "Collecting documentation from $source_dir..."
    
    while IFS= read -r -d '' file; do
        rel_path="${file#$source_dir/}"
        dest_dir="$dest_base/$(dirname "$rel_path")"
        mkdir -p "$dest_dir"
        cp "$file" "$dest_dir/"
        ((count++))
        echo "  ✓ $(basename "$file")"
    done < <(find "$source_dir" -type f \( \
        -name "README.md" -o \
        -name "RECIPE.yml" -o \
        -name "*.md" -o \
        -name "*.txt" \
    \) ! -path "*/.*" -print0 2>/dev/null)
    
    echo "  Collected $count documents"
    echo ""
    
    return $count
}

# Collect from DATA_PROJECTS
echo "Step 1: Collecting from DATA_PROJECTS..."
echo "----------------------------------------"
if [ -d "$T7_ROOT/03_DATA_PROJECTS" ]; then
    collect_scripts "$T7_ROOT/03_DATA_PROJECTS" "$BACKUP_DIR/03_DATA_PROJECTS"
    collect_docs "$T7_ROOT/03_DATA_PROJECTS" "$BACKUP_DIR/03_DATA_PROJECTS"
else
    echo "  No DATA_PROJECTS directory found"
fi

# Collect from FARM_ASSESSMENT
echo "Step 2: Collecting from FARM_ASSESSMENT..."
echo "----------------------------------------"
if [ -d "$T7_ROOT/04_FARM_ASSESSMENT" ]; then
    collect_scripts "$T7_ROOT/04_FARM_ASSESSMENT" "$BACKUP_DIR/04_FARM_ASSESSMENT"
    collect_docs "$T7_ROOT/04_FARM_ASSESSMENT" "$BACKUP_DIR/04_FARM_ASSESSMENT"
else
    echo "  No FARM_ASSESSMENT directory found"
fi

# Collect QGIS files
echo "Step 3: Collecting QGIS assets..."
echo "----------------------------------------"
mkdir -p "$BACKUP_DIR/qgis_assets"
count=0

for ext in "qml" "qpt" "model3"; do
    while IFS= read -r -d '' file; do
        project_name=$(basename "$(dirname "$(dirname "$file")")")
        dest="$BACKUP_DIR/qgis_assets/${project_name}"
        mkdir -p "$dest"
        cp "$file" "$dest/"
        ((count++))
        echo "  ✓ $(basename "$file")"
    done < <(find "$T7_ROOT" -type f -name "*.$ext" ! -path "*/.*" -print0 2>/dev/null)
done

echo "  Collected $count QGIS assets"
echo ""

# Create inventory
echo "Step 4: Creating inventory..."
echo "----------------------------------------"
cat > "$BACKUP_DIR/INVENTORY.md" << EOF
# Project Scripts Inventory
Generated: $(date)

## Statistics
- Collection timestamp: $TIMESTAMP
- Data Project scripts: $(find "$BACKUP_DIR/03_DATA_PROJECTS" -type f -name "*.sh" -o -name "*.py" | wc -l)
- Farm Assessment scripts: $(find "$BACKUP_DIR/04_FARM_ASSESSMENT" -type f -name "*.sh" -o -name "*.py" | wc -l)
- QGIS assets: $(find "$BACKUP_DIR/qgis_assets" -type f | wc -l)
- Total size: $(du -sh "$BACKUP_DIR" | cut -f1)

## Recent Additions
$(find "$BACKUP_DIR" -type f -mtime -1 -exec basename {} \; | head -10)

## Projects Included
### Data Projects
$(ls -1 "$BACKUP_DIR/03_DATA_PROJECTS" 2>/dev/null | head -20)

### Farm Assessments
$(ls -1 "$BACKUP_DIR/04_FARM_ASSESSMENT" 2>/dev/null | head -20)
EOF

echo "✓ Inventory created"
echo ""

# Git operations
echo "Step 5: Committing to Git..."
echo "----------------------------------------"
cd "$T7_ROOT"

# Check if Git repo exists
if [ -d ".git" ]; then
    # Add files
    git add -A "00_SYSTEM_CONTROL/project_scripts/"
    
    # Check if there are changes
    if git diff --staged --quiet; then
        echo "  No new scripts to commit"
    else
        # Commit
        git commit -m "Backup project scripts - $(date +%Y-%m-%d)" \
                   -m "Automated collection from active projects"
        echo "✓ Committed to Git"
        
        # Push if remote exists
        if git remote | grep -q origin; then
            git push origin main 2>/dev/null && echo "✓ Pushed to GitHub" || echo "⚠ Push failed - manual push needed"
        fi
    fi
else
    echo "⚠ No Git repository found"
fi
echo ""

# Cleanup old backups (keep last 30 days)
echo "Step 6: Cleanup..."
echo "----------------------------------------"
find "$BACKUP_DIR/logs" -name "*.log" -mtime +30 -delete 2>/dev/null
echo "✓ Cleaned old logs"
echo ""

# Summary
echo "======================================"
echo "COLLECTION COMPLETE"
echo "======================================"
echo ""
echo "Scripts backed up to:"
echo "  $BACKUP_DIR"
echo ""
echo "View inventory:"
echo "  cat $BACKUP_DIR/INVENTORY.md"
echo ""
echo "Next collection recommended:"
echo "  - After completing any project"
echo "  - Weekly on Fridays"
echo "  - Before major system changes"
echo ""

# Log completion
echo "$(date): Collection complete" >> "$LOG_FILE"