# GitHub Backup Strategy for T7 Shield
**Date:** 2025-01-21  
**Issue:** Scripts in project folders aren't backed up to GitHub

---

## 🔍 CURRENT SITUATION

### What's Tracked by Git
```
/Volumes/T7 Shield/
├── .git/                    # Git repository root
├── 00_SYSTEM_CONTROL/       # ✅ Tracked
├── 01_KNOWLEDGE_CONTEXT/    # ✅ Tracked
└── 03_DATA_PROJECTS/        # ❌ Not tracked (too large)
    └── ProjectX/
        └── PROCESSING/
            └── scripts/     # ⚠️ Important scripts not backed up!
```

### The Problem
- Git repo at root tracks system files
- Data projects contain valuable scripts
- But also contain huge data files (GB+)
- Can't track entire projects (too large for GitHub)

---

## 💡 SOLUTION: SELECTIVE SCRIPT COLLECTION

### Approach 1: Script Collection System
Create automated script collection that copies important scripts to tracked location:

```bash
# Collect all scripts from projects
/00_SYSTEM_CONTROL/automation/collect_project_scripts.sh

# Copies scripts to:
/00_SYSTEM_CONTROL/project_scripts/
├── 03_DATA_PROJECTS/
│   ├── Forest_Cover_2019/
│   │   ├── process_forest.sh
│   │   ├── mask_creation.py
│   │   └── README.md
│   └── EP_Exclusion/
│       └── exclusion_pipeline.sh
└── 04_FARM_ASSESSMENT/
    └── Hewitts_PF_TAS/
        ├── fullcam_prep.py
        └── boundary_extract.sh
```

### Approach 2: .gitignore Strategy
Configure Git to track ONLY scripts in project folders:

```gitignore
# Track only code in projects
!03_DATA_PROJECTS/**/*.sh
!03_DATA_PROJECTS/**/*.py
!03_DATA_PROJECTS/**/*.sql
!03_DATA_PROJECTS/**/*.yml
!03_DATA_PROJECTS/**/README.md
!03_DATA_PROJECTS/**/RECIPE.yml

# But ignore all data files
03_DATA_PROJECTS/**/*.tif
03_DATA_PROJECTS/**/*.gpkg
03_DATA_PROJECTS/**/*.shp
03_DATA_PROJECTS/**/*.tif.ovr
03_DATA_PROJECTS/**/*.aux.xml
```

### Approach 3: Separate Script Repository
Create dedicated repository for project scripts:

```
github.com/LachyRitchie/gis-project-scripts/
├── data_projects/
│   └── [project scripts]
└── farm_assessments/
    └── [farm scripts]
```

---

## 🚀 RECOMMENDED IMPLEMENTATION

### Hybrid Approach (Best of All Worlds)

1. **Immediate: Script Collection**
```bash
#!/bin/bash
# collect_scripts.sh - Run daily or after projects

SCRIPT_BACKUP="/Volumes/T7 Shield/00_SYSTEM_CONTROL/project_scripts"
mkdir -p "$SCRIPT_BACKUP"

# Find and copy all scripts
find /Volumes/T7\ Shield/03_DATA_PROJECTS -type f \
  \( -name "*.sh" -o -name "*.py" -o -name "*.sql" \) \
  -exec cp --parents {} "$SCRIPT_BACKUP" \;

# Also copy important docs
find /Volumes/T7\ Shield/03_DATA_PROJECTS -type f \
  \( -name "README.md" -o -name "RECIPE.yml" \) \
  -exec cp --parents {} "$SCRIPT_BACKUP" \;

# Commit to Git
cd /Volumes/T7\ Shield
git add 00_SYSTEM_CONTROL/project_scripts/
git commit -m "Backup project scripts $(date +%Y-%m-%d)"
git push
```

2. **Configure .gitignore**
```gitignore
# In root .gitignore

# Ignore large data files everywhere
*.tif
*.tif.ovr
*.gpkg
*.shp
*.dbf
*.shx
*.prj
*.aux.xml
*.cpg
*.qgz

# But track important files
!**/README.md
!**/RECIPE.yml
!**/*.model3
!**/*.qml
!**/*.qpt

# Track script backups
!00_SYSTEM_CONTROL/project_scripts/**
```

3. **Add to End-of-Project Protocol**
```markdown
## Script Backup Step
After project completion:
1. Run script collection: `bash collect_scripts.sh`
2. Verify scripts copied to `/00_SYSTEM_CONTROL/project_scripts/`
3. Commit to Git with project name
```

---

## 📋 IMPLEMENTATION CHECKLIST

- [ ] Create `/00_SYSTEM_CONTROL/project_scripts/` directory
- [ ] Write `collect_scripts.sh` automation
- [ ] Update `.gitignore` with selective rules
- [ ] Add to end-of-project protocol
- [ ] Test with existing project
- [ ] Schedule daily/weekly collection
- [ ] Document in README

---

## 🎯 BENEFITS

1. **All scripts backed up** without storing huge data files
2. **Searchable history** of all project code
3. **Reusable patterns** easily found
4. **GitHub size limits** respected
5. **No manual copying** required

---

## 🔄 AUTOMATION OPTIONS

### Option A: Cron Job (Mac LaunchAgent)
```xml
<!-- ~/Library/LaunchAgents/com.relanature.script.backup.plist -->
<key>ProgramArguments</key>
<array>
    <string>/Volumes/T7 Shield/00_SYSTEM_CONTROL/automation/collect_scripts.sh</string>
</array>
<key>StartCalendarInterval</key>
<dict>
    <key>Hour</key>
    <integer>18</integer> <!-- 6 PM daily -->
</dict>
```

### Option B: Git Pre-Commit Hook
```bash
#!/bin/sh
# .git/hooks/pre-commit
bash /Volumes/T7\ Shield/00_SYSTEM_CONTROL/automation/collect_scripts.sh
```

### Option C: Manual Trigger
Add to Engineer's end-of-project protocol

---

Ready to implement the script collection system?