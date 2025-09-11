# T7 Shield System Restructure Plan
**Date:** 2025-01-21  
**Purpose:** Simplify and consolidate system organization

---

## 🎯 RESTRUCTURE OBJECTIVES
1. Consolidate scattered system files
2. Create clear separation between system control and project work
3. Establish shared components for both agents
4. Improve Git tracking of important files

---

## 📁 NEW STRUCTURE

```
/Volumes/T7 Shield/
├── 00_SYSTEM_CONTROL/           # ← NEW: All system governance
│   ├── prompts/                 # Agent prompts
│   │   ├── GIS_STRATEGIST.md
│   │   ├── GIS_ENGINEER.md
│   │   └── shared/              # Shared components
│   │       ├── NAMING_RULES.md
│   │       ├── EXECUTION_MATRIX.md
│   │       └── COMPLIANCE_REQUIREMENTS.md
│   ├── protocols/               # All protocols
│   │   ├── END_OF_PROJECT.md
│   │   ├── BACKUP.md
│   │   ├── LONG_RUNNING_SCRIPTS.md
│   │   └── quick_reference/    # Quick cards
│   ├── templates/               # All templates
│   │   ├── RECIPE.yml
│   │   ├── PROJECT_STRUCTURE.md
│   │   └── QGIS/               # QGIS templates
│   ├── automation/              # Scripts & tools
│   │   ├── backup_farms.sh
│   │   ├── align_documentation.sh
│   │   └── validation/         # Validation scripts
│   ├── patterns/                # ← NEW: Positive examples
│   │   ├── binary_mask_to_google_earth.md
│   │   ├── state_boundary_extraction.md
│   │   ├── fullcam_data_prep.md
│   │   └── carbon_yield_masking.md
│   └── .cursor/                 # ← MOVED: Cursor config
│       ├── .cursorrules
│       └── settings.json
│
├── 01_KNOWLEDGE_CONTEXT/        # ← RENAMED: Consolidate knowledge
│   ├── reference_docs/          # ← Was 02_KNOWLEDGE_BASE
│   │   ├── EnvironmentalPlantings/
│   │   ├── PlantationForestry/
│   │   ├── HumanInducedRegeneration/
│   │   ├── FullCAM/
│   │   └── CER_Guidance/
│   ├── lessons_learned/         # ← Moved from 01_CONTEXT
│   │   ├── by_category/
│   │   ├── session_reviews/
│   │   └── CRITICAL_SUMMARY.md
│   └── successful_pipelines/    # ← Moved from 01_CONTEXT
│       └── tested_workflows.yml
│
├── 02_BASE_DATA/                # ← RENAMED (was 03)
│   └── CURRENT/
│       └── CURRENT_VERSIONS.yml
│
├── 03_DATA_PROJECTS/            # ← RENAMED (was 04)
│
├── 04_FARM_ASSESSMENT/          # ← RENAMED (was 05)
│
├── 05_TEMPLATES_LAYOUTS/        # ← RENAMED (was 06)
│
├── 06_PYTHON_ENVIRONMENT/       # ← RENAMED (was 07)
│
├── 07_SCRIPTS/                  # ← RENAMED (was 08)
│
├── 08_TOOLS/                    # ← RENAMED (was 09_SYSTEM_TOOLS)
│
├── 09_ARCHIVE/                  # ← RENAMED (was 10)
│
└── PROCESSING/                  # Temporary workspace
```

---

## 🔄 KEY CHANGES

### 1. New Top-Level Organization
- **00_SYSTEM_CONTROL**: All governance in one place
- **01_KNOWLEDGE_CONTEXT**: All learning/reference together
- Numbers shifted down by 1 for remaining folders

### 2. Consolidated Locations
| Old Location | New Location | Benefit |
|--------------|--------------|---------|
| `/01_SYSTEM/*` | `/00_SYSTEM_CONTROL/protocols/` | All protocols together |
| `/01_CONTEXT/agent_config/*` | `/00_SYSTEM_CONTROL/prompts/` | All prompts together |
| `/01_CONTEXT/lessons_learned/*` | `/01_KNOWLEDGE_CONTEXT/lessons_learned/` | Knowledge consolidated |
| `/.cursorrules` | `/00_SYSTEM_CONTROL/.cursor/.cursorrules` | Config with system |
| `/02_KNOWLEDGE_BASE/*` | `/01_KNOWLEDGE_CONTEXT/reference_docs/` | Clear naming |

### 3. New Additions
- **Shared components**: Reduce duplication between prompts
- **Patterns library**: Positive examples of common tasks
- **Validation scripts**: Automated compliance checking

---

## 🚀 MIGRATION STEPS

### Phase 1: Create New Structure
```bash
# Create new directories
mkdir -p 00_SYSTEM_CONTROL/{prompts/shared,protocols/quick_reference,templates/QGIS,automation/validation,patterns}
mkdir -p 01_KNOWLEDGE_CONTEXT/{reference_docs,lessons_learned,successful_pipelines}
```

### Phase 2: Move System Files
```bash
# Move protocols
mv 01_SYSTEM/*.md 00_SYSTEM_CONTROL/protocols/
mv 01_SYSTEM/*.yml 00_SYSTEM_CONTROL/templates/

# Move prompts
mv 01_CONTEXT/agent_config/*PROMPT*.md 00_SYSTEM_CONTROL/prompts/

# Move cursor config
mkdir -p 00_SYSTEM_CONTROL/.cursor
mv .cursorrules 00_SYSTEM_CONTROL/.cursor/
```

### Phase 3: Move Knowledge
```bash
# Move knowledge base
mv "02_KNOWLEDGE_BASE"/* 01_KNOWLEDGE_CONTEXT/reference_docs/

# Move lessons learned
mv 01_CONTEXT/lessons_learned/* 01_KNOWLEDGE_CONTEXT/lessons_learned/
mv 01_CONTEXT/successful_pipelines/* 01_KNOWLEDGE_CONTEXT/successful_pipelines/
```

### Phase 4: Rename Data Folders
```bash
# Rename in sequence
mv 03_BASE_DATA 02_BASE_DATA
mv 04_DATA_PROJECTS 03_DATA_PROJECTS
mv 05_FARM_ASSESSMENT 04_FARM_ASSESSMENT
# ... etc
```

### Phase 5: Update References
- Update all prompts with new paths
- Update .cursorrules with new locations
- Update backup scripts
- Create symlinks for backward compatibility

---

## 📋 POST-MIGRATION CHECKLIST

- [ ] All system files in 00_SYSTEM_CONTROL
- [ ] All knowledge in 01_KNOWLEDGE_CONTEXT
- [ ] Data folders renumbered correctly
- [ ] .cursorrules updated with new paths
- [ ] Prompts updated with new references
- [ ] Backup scripts updated
- [ ] Git tracking updated
- [ ] Test both agents can find resources

---

## 🔗 BACKWARD COMPATIBILITY

Create symlinks during transition:
```bash
ln -s 00_SYSTEM_CONTROL/prompts 01_CONTEXT/agent_config
ln -s 01_KNOWLEDGE_CONTEXT/reference_docs 02_KNOWLEDGE_BASE
ln -s 00_SYSTEM_CONTROL/.cursor/.cursorrules .cursorrules
```

Remove after confirming everything works.

---

## ⚠️ RISKS & MITIGATION

| Risk | Mitigation |
|------|------------|
| Broken references | Create symlinks first |
| Lost files | Full backup before starting |
| Agent confusion | Update prompts immediately |
| Git issues | Commit before and after |

---

## ✅ SUCCESS CRITERIA

1. Simpler, more logical structure
2. All files findable in predictable locations
3. No duplication of rules/protocols
4. Both agents work without errors
5. Git tracks all important files

---

Ready to proceed? Run migration script when approved.