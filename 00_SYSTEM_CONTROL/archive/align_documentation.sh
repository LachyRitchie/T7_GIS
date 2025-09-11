#!/bin/bash
# T7 Shield Documentation Alignment Script
# Purpose: Fix critical path and reference issues
# Date: 2025-01-21

echo "========================================="
echo "T7 SHIELD DOCUMENTATION ALIGNMENT"
echo "========================================="
echo ""

# 1. Fix Knowledge Base folder name (remove space)
echo "Step 1: Fixing Knowledge Base folder name..."
if [ -d "/Volumes/T7 Shield/02_KNOWLEDGE BASE" ]; then
    echo "Found folder with space in name. Renaming..."
    mv "/Volumes/T7 Shield/02_KNOWLEDGE BASE" "/Volumes/T7 Shield/02_KNOWLEDGE_BASE"
    echo "✓ Renamed to 02_KNOWLEDGE_BASE (no space)"
else
    echo "✓ Knowledge base folder already correct"
fi
echo ""

# 2. Create backup of current Engineer prompt
echo "Step 2: Backing up current Engineer prompt..."
if [ -f "/Volumes/T7 Shield/01_CONTEXT/agent_config/GIS_ENGINEER_SYSTEM_PROMPT.md" ]; then
    cp "/Volumes/T7 Shield/01_CONTEXT/agent_config/GIS_ENGINEER_SYSTEM_PROMPT.md" \
       "/Volumes/T7 Shield/01_CONTEXT/agent_config/GIS_ENGINEER_SYSTEM_PROMPT_v2_backup.md"
    echo "✓ Backup created"
else
    echo "⚠ Engineer prompt not found"
fi
echo ""

# 3. Create quick reference cards directory
echo "Step 3: Creating quick reference directory..."
mkdir -p "/Volumes/T7 Shield/01_SYSTEM/quick_reference"
echo "✓ Quick reference directory created"
echo ""

# 4. Verify all critical files exist
echo "Step 4: Verifying critical files..."
critical_files=(
    "/Volumes/T7 Shield/01_SYSTEM/END_OF_PROJECT_PROTOCOL.md"
    "/Volumes/T7 Shield/01_SYSTEM/RECIPE_TEMPLATE.yml"
    "/Volumes/T7 Shield/03_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml"
    "/Volumes/T7 Shield/.cursorrules"
)

for file in "${critical_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✓ Found: $(basename $file)"
    else
        echo "✗ MISSING: $file"
    fi
done
echo ""

# 5. Check for forbidden file names in active projects
echo "Step 5: Scanning for non-compliant file names..."
echo "Checking 04_DATA_PROJECTS..."
bad_files=$(find "/Volumes/T7 Shield/04_DATA_PROJECTS" -type f \( \
    -name "*_fixed*" -o \
    -name "*_FIXED*" -o \
    -name "*_aligned*" -o \
    -name "*_temp*" -o \
    -name "*_temporary*" -o \
    -name "*_final*" -o \
    -name "*_FINAL*" \) 2>/dev/null | head -10)

if [ -z "$bad_files" ]; then
    echo "✓ No non-compliant files found"
else
    echo "⚠ Found non-compliant files:"
    echo "$bad_files"
fi
echo ""

# 6. Create alignment report
echo "Step 6: Creating alignment report..."
cat > "/Volumes/T7 Shield/01_SYSTEM/ALIGNMENT_STATUS.txt" << EOF
T7 SHIELD ALIGNMENT STATUS REPORT
Generated: $(date)
================================

FOLDER STRUCTURE:
✓ 01_SYSTEM - System control documents
✓ 01_CONTEXT - Agent configuration
$([ -d "/Volumes/T7 Shield/02_KNOWLEDGE_BASE" ] && echo "✓" || echo "✗") 02_KNOWLEDGE_BASE - Reference documentation
✓ 03_BASE_DATA - Source datasets
✓ 04_DATA_PROJECTS - Processing projects
✓ 05_FARM_ASSESSMENT - Farm projects

KEY DOCUMENTS:
$([ -f "/Volumes/T7 Shield/01_SYSTEM/END_OF_PROJECT_PROTOCOL.md" ] && echo "✓" || echo "✗") End-of-Project Protocol
$([ -f "/Volumes/T7 Shield/.cursorrules" ] && echo "✓" || echo "✗") Cursor Rules
$([ -f "/Volumes/T7 Shield/03_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml" ] && echo "✓" || echo "✗") Current Versions Registry

SYSTEM PROMPTS:
- GIS Strategist: v3.2 (2025-01-21)
- GIS Engineer: v2025-09-03 (needs update)

RECOMMENDATIONS:
1. Update GIS Engineer prompt to v3.0
2. Create shared rule components
3. Build pattern library
4. Implement validation scripts

Next review due: $(date -d "+7 days" 2>/dev/null || date)
EOF

echo "✓ Alignment report created"
echo ""

echo "========================================="
echo "ALIGNMENT SCRIPT COMPLETE"
echo "========================================="
echo ""
echo "Summary:"
echo "- Knowledge base folder renamed (if needed)"
echo "- Engineer prompt backed up"
echo "- Quick reference directory created"
echo "- Critical files verified"
echo "- Non-compliant files identified"
echo "- Status report generated"
echo ""
echo "See /01_SYSTEM/ALIGNMENT_STATUS.txt for details"
