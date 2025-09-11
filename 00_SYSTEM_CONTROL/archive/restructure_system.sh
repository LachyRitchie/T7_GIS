#!/bin/bash
# T7 Shield System Restructure Script
# Date: 2025-01-21
# Purpose: Reorganize system folders for clarity and maintainability

set -e  # Exit on error

echo "========================================="
echo "T7 SHIELD SYSTEM RESTRUCTURE"
echo "========================================="
echo ""
echo "This script will reorganize the system folders."
echo "A backup will be created first."
echo ""
read -p "Press Enter to continue or Ctrl+C to cancel..."
echo ""

# Set root directory
T7_ROOT="/Volumes/T7 Shield"
cd "$T7_ROOT"

# Create timestamp for backup
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "Step 1: Creating backup of current structure..."
echo "----------------------------------------"
# Create backup list of current structure
find . -type d -maxdepth 3 | sort > "structure_backup_${TIMESTAMP}.txt"
echo "✓ Structure snapshot saved to structure_backup_${TIMESTAMP}.txt"
echo ""

echo "Step 2: Creating new directory structure..."
echo "----------------------------------------"

# Create 00_SYSTEM_CONTROL structure
mkdir -p 00_SYSTEM_CONTROL/prompts/shared
mkdir -p 00_SYSTEM_CONTROL/protocols/quick_reference
mkdir -p 00_SYSTEM_CONTROL/templates/QGIS
mkdir -p 00_SYSTEM_CONTROL/automation/validation
mkdir -p 00_SYSTEM_CONTROL/patterns
mkdir -p 00_SYSTEM_CONTROL/.cursor
echo "✓ Created 00_SYSTEM_CONTROL structure"

# Create 01_KNOWLEDGE_CONTEXT structure
mkdir -p 01_KNOWLEDGE_CONTEXT/reference_docs
mkdir -p 01_KNOWLEDGE_CONTEXT/lessons_learned
mkdir -p 01_KNOWLEDGE_CONTEXT/successful_pipelines
echo "✓ Created 01_KNOWLEDGE_CONTEXT structure"
echo ""

echo "Step 3: Moving system control files..."
echo "----------------------------------------"

# Move protocols from 01_SYSTEM to 00_SYSTEM_CONTROL/protocols
if [ -d "01_SYSTEM" ]; then
    echo "Moving protocols..."
    for file in 01_SYSTEM/*.md; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            # Clean up naming
            new_name="${filename//_PROTOCOL/}"
            new_name="${new_name//_QUICK_REFERENCE/}"
            mv "$file" "00_SYSTEM_CONTROL/protocols/$new_name"
            echo "  ✓ Moved $filename → protocols/$new_name"
        fi
    done
    
    # Move templates
    for file in 01_SYSTEM/*.yml; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            new_name="${filename//_TEMPLATE/}"
            mv "$file" "00_SYSTEM_CONTROL/templates/$new_name"
            echo "  ✓ Moved $filename → templates/$new_name"
        fi
    done
    
    # Move scripts
    for file in 01_SYSTEM/*.sh; do
        if [ -f "$file" ]; then
            mv "$file" "00_SYSTEM_CONTROL/automation/"
            echo "  ✓ Moved $(basename $file) → automation/"
        fi
    done
fi

# Move agent prompts
if [ -d "01_CONTEXT/agent_config" ]; then
    echo "Moving agent prompts..."
    if [ -f "01_CONTEXT/agent_config/GIS_ENGINEER_SYSTEM_PROMPT.md" ]; then
        mv "01_CONTEXT/agent_config/GIS_ENGINEER_SYSTEM_PROMPT.md" \
           "00_SYSTEM_CONTROL/prompts/GIS_ENGINEER.md"
        echo "  ✓ Moved GIS Engineer prompt"
    fi
    
    if [ -f "01_CONTEXT/agent_config/LONG_RUNNING_SCRIPT_APPROVAL_PROCESS.md" ]; then
        mv "01_CONTEXT/agent_config/LONG_RUNNING_SCRIPT_APPROVAL_PROCESS.md" \
           "00_SYSTEM_CONTROL/protocols/LONG_RUNNING_SCRIPTS.md"
        echo "  ✓ Moved long-running script protocol"
    fi
fi

# Move cursor rules
if [ -f ".cursorrules" ]; then
    cp ".cursorrules" "00_SYSTEM_CONTROL/.cursor/.cursorrules"
    echo "  ✓ Copied .cursorrules to new location"
fi
echo ""

echo "Step 4: Moving knowledge and context..."
echo "----------------------------------------"

# Move knowledge base
if [ -d "02_KNOWLEDGE_BASE" ]; then
    echo "Moving reference documentation..."
    for dir in 02_KNOWLEDGE_BASE/*/; do
        if [ -d "$dir" ]; then
            dirname=$(basename "$dir")
            mv "$dir" "01_KNOWLEDGE_CONTEXT/reference_docs/"
            echo "  ✓ Moved $dirname"
        fi
    done
fi

# Move lessons learned
if [ -d "01_CONTEXT/lessons_learned" ]; then
    echo "Moving lessons learned..."
    cp -r 01_CONTEXT/lessons_learned/* 01_KNOWLEDGE_CONTEXT/lessons_learned/
    echo "  ✓ Moved lessons learned"
fi

# Move successful pipelines
if [ -d "01_CONTEXT/successful_pipelines" ]; then
    echo "Moving successful pipelines..."
    cp -r 01_CONTEXT/successful_pipelines/* 01_KNOWLEDGE_CONTEXT/successful_pipelines/
    echo "  ✓ Moved successful pipelines"
fi
echo ""

echo "Step 5: Creating shared components..."
echo "----------------------------------------"

# Create shared naming rules
cat > "00_SYSTEM_CONTROL/prompts/shared/NAMING_RULES.md" << 'EOF'
# Shared Naming Rules
**Used by both GIS Strategist and GIS Engineer**

## File Naming Pattern
**MANDATORY:** `What_Where_When_Version.ext`

### Examples
- `ForestCover_National_2019_v1.0.tif`
- `EPExclusion_NSW_v2.1.gpkg`
- `CarbonYield_QLD_2023_v1.0.tif`

### Version Rules
- Initial: v1.0
- Minor fix: v1.0 → v1.1
- Major change: v1.x → v2.0
- NEVER reuse version numbers
- NEVER use descriptive suffixes

### Forbidden Suffixes
AUTOMATIC REJECTION if file contains:
- `_fixed`, `_FIXED`
- `_aligned`, `_ALIGNED`
- `_temp`, `_temporary`, `_tmp`
- `_final`, `_FINAL`
- `_processed`, `_processing`
- `_combined`, `_merged`
- `_backup`, `_copy`
- `_new`, `_old`, `_original`

## Folder Naming Patterns

### Data Projects
`What_DataDate_Where__ProjectDate`
- Note the DOUBLE UNDERSCORE before project date
- Example: `Forest_Cover_2019_National__Sept2025`

### Farm Assessments
`PropertyName_Method_State_YYYY-MM`
- Method codes: EP, HIR, PF
- Example: `Hewitts_PF_TAS_2025-01`
EOF
echo "✓ Created shared naming rules"

# Create shared execution matrix
cat > "00_SYSTEM_CONTROL/prompts/shared/EXECUTION_MATRIX.md" << 'EOF'
# Shared Execution Matrix
**Determines whether Engineer executes or returns to Strategist**

## Decision Matrix
| Criterion | Engineer Executes | Return to Strategist |
|-----------|------------------|---------------------|
| File size | < 100 MB | ≥ 100 MB |
| Runtime | < 5 min | ≥ 5 min |
| File count | < 5 | ≥ 5 |
| Total output | < 500 MB | ≥ 500 MB |
| Script runtime | < 30 min | ≥ 30 min |
| Confidence | High | Any uncertainty |

## Rules
- If ANY threshold exceeded → Return to Strategist
- Always test with single file first
- Get approval for long-running scripts
EOF
echo "✓ Created shared execution matrix"

# Create shared compliance requirements
cat > "00_SYSTEM_CONTROL/prompts/shared/COMPLIANCE_REQUIREMENTS.md" << 'EOF'
# Shared Compliance Requirements
**Mandatory for all GIS operations**

## ACCU Method Compliance
- NEVER mix methods (EP, HIR, PF)
- Always verify FullCAM settings match method
- Cross-check with method determination

## Data Standards
- CRS: EPSG:3577 (Albers) or EPSG:4326 (WGS84)
- Resolution: 25m pixels with -tap alignment
- NoData: 255 (byte), -9999 (float)
- Compression: LZW, TILED=YES, BIGTIFF if >4GB

## Working Folder Discipline
- ALL work in PROCESSING/ subfolder
- NEVER create folders at root level
- Archive old versions before creating new

## End-of-Project Requirements
- Run END_OF_PROJECT protocol
- Create/update RECIPE.yml
- Update CURRENT_VERSIONS.yml
- Flag files >1GB for backup
EOF
echo "✓ Created shared compliance requirements"
echo ""

echo "Step 6: Creating backward compatibility symlinks..."
echo "----------------------------------------"

# Create symlinks for transition period
ln -sf "00_SYSTEM_CONTROL/prompts" "01_CONTEXT/agent_config"
ln -sf "01_KNOWLEDGE_CONTEXT/reference_docs" "02_KNOWLEDGE_BASE"
ln -sf "00_SYSTEM_CONTROL/.cursor/.cursorrules" ".cursorrules"
echo "✓ Created compatibility symlinks"
echo ""

echo "Step 7: Updating .cursorrules..."
echo "----------------------------------------"

# Update .cursorrules with new paths
cat > "00_SYSTEM_CONTROL/.cursor/.cursorrules" << 'EOF'
# T7 Shield Cursor Configuration
# Updated: 2025-01-21 - Post-restructure

# System control
system_control_path: 00_SYSTEM_CONTROL/

# Prompts location
strategist_prompt: 00_SYSTEM_CONTROL/prompts/GIS_STRATEGIST.md
engineer_prompt: 00_SYSTEM_CONTROL/prompts/GIS_ENGINEER.md
shared_rules: 00_SYSTEM_CONTROL/prompts/shared/

# Knowledge and context
knowledge_path: 01_KNOWLEDGE_CONTEXT/
reference_docs: 01_KNOWLEDGE_CONTEXT/reference_docs/
lessons_learned: 01_KNOWLEDGE_CONTEXT/lessons_learned/
successful_pipelines: 01_KNOWLEDGE_CONTEXT/successful_pipelines/

# Data paths
base_data_path: 02_BASE_DATA/
data_projects_path: 03_DATA_PROJECTS/
farm_assessments_path: 04_FARM_ASSESSMENT/

# Protocols
end_of_project_protocol: 00_SYSTEM_CONTROL/protocols/END_OF_PROJECT.md
backup_protocol: 00_SYSTEM_CONTROL/protocols/BACKUP.md

# Critical reminders:
# - Follow naming rules in shared/NAMING_RULES.md
# - Check execution matrix in shared/EXECUTION_MATRIX.md
# - Run end-of-project protocol after major tasks
# - All work in PROCESSING/ subfolders
EOF
echo "✓ Updated .cursorrules"

# Also update the symlinked version
cp "00_SYSTEM_CONTROL/.cursor/.cursorrules" ".cursorrules"
echo ""

echo "Step 8: Creating migration report..."
echo "----------------------------------------"

# Create migration report
cat > "00_SYSTEM_CONTROL/MIGRATION_REPORT_${TIMESTAMP}.md" << EOF
# System Restructure Migration Report
Generated: $(date)

## Completed Actions
✓ Created new directory structure
✓ Moved system control files to 00_SYSTEM_CONTROL
✓ Moved knowledge to 01_KNOWLEDGE_CONTEXT
✓ Created shared components
✓ Updated .cursorrules
✓ Created backward compatibility symlinks

## New Structure
- 00_SYSTEM_CONTROL - All governance
- 01_KNOWLEDGE_CONTEXT - All knowledge/learning
- 02_BASE_DATA - Source datasets (was 03)
- 03_DATA_PROJECTS - Processing (was 04)
- 04_FARM_ASSESSMENT - Farms (was 05)

## Remaining Tasks
- [ ] Update GIS Strategist prompt with new paths
- [ ] Update GIS Engineer prompt with new paths
- [ ] Update backup scripts with new paths
- [ ] Test both agents with new structure
- [ ] Rename remaining folders (06-10)
- [ ] Remove old empty directories
- [ ] Remove compatibility symlinks (after testing)

## Backup
Structure snapshot: structure_backup_${TIMESTAMP}.txt
EOF

echo "✓ Migration report created"
echo ""

echo "========================================="
echo "RESTRUCTURE PARTIALLY COMPLETE"
echo "========================================="
echo ""
echo "✅ Completed:"
echo "  - New structure created"
echo "  - System files moved"
echo "  - Shared components created"
echo "  - Compatibility symlinks in place"
echo ""
echo "⚠️ Still needed:"
echo "  - Update prompts with new paths"
echo "  - Rename folders 06-10"
echo "  - Test everything works"
echo "  - Update Git tracking"
echo ""
echo "See: 00_SYSTEM_CONTROL/MIGRATION_REPORT_${TIMESTAMP}.md"
