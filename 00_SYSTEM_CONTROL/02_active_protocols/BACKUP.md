# GIS Environment Backup Protocol v1.1
*Last Updated: 2025-01-09*
*Status: ACTIVE*
*GitHub: https://github.com/LachyRitchie/gis-context*

## Overview
Workflow-integrated preservation system that backs up critical data automatically while documenting processes for reconstruction. No separate reminders needed - all prompts are triggered by your actual work.

## The Three-Tier System

### Tier 1: GitHub (Context & Scripts)
**What:** System prompts, scripts, lessons, decisions
**When:** Immediately when created/updated
**How:** Git commit as part of workflow
**Recovery:** Clone repository

### Tier 2: Google Drive (Farm Outputs)
**What:** PDFs, KMZ, FullCAM XML files only
**When:** Daily at 10pm (automated)
**How:** LaunchAgent runs rsync script
**Recovery:** Download from Google Drive

### Tier 3: Physical Drive (Data Projects)
**What:** Completed data projects >1GB
**When:** On completion (system prompts you)
**How:** Manual clone when prompted by workflow
**Recovery:** Copy from backup drive

---

## Automated Components

### Daily Farm Backup (LaunchAgent)
- **Script:** `~/Scripts/backup_farms.sh`
- **Google Account:** admin@relanature.com (business)
- **Schedule:** Daily 10pm
- **Target:** admin@relanature.com Google Drive → My Drive → GIS_Backups/farms/
- **Size:** ~10MB per farm (PDFs, KMZ, XML only)
- **Bandwidth:** <100MB/day typical
- **Status Check:** Run `tail ~/gis_backup.log` during farm reviews

### GitHub Integration
- **Repository:** https://github.com/LachyRitchie/gis-context
- **Auto-tracked:** System prompts, RECIPE.yml files, logs
- **Push frequency:** After major decisions or system updates

---

## Workflow-Integrated Triggers

### Data Project Completion ("Victory Lap Protocol")
When Engineer completes a major data project:

1. **Engineer Action:**
   - Moves final output to `/03_BASE_DATA/DERIVED/`
   - Creates `RECIPE.yml` in project folder
   - Updates `CURRENT_VERSIONS.yml`

2. **Strategist Prompt:**
   ```
   🛑 DATA PROJECT COMPLETE
   - Project: [Name]
   - Size: [X GB]
   - ACTION REQUIRED: Connect T7 Backup drive for archive
   ```

3. **User Action:**
   - Connect T7 Backup drive
   - Run: `rsync -av --progress [project] /Volumes/T7_Backup/`
   - Confirm completion to continue

### Physical Backup (Workflow Triggered)
- **When:** After completing major data projects (>1GB)
- **Prompt:** System reminds you during work, not on schedule
- **Action:** Clone project or full T7 Shield to T7 Backup
- **Command:** `rsync -av --progress /Volumes/T7\ Shield/ /Volumes/T7_Backup/`
- **Duration:** ~2 hours for 200GB

---

## Recovery Procedures

### Scenario 1: Accidental Deletion
1. Check Google Drive for farm outputs
2. Check GitHub for scripts/configs
3. Check T7 Backup for last physical backup

### Scenario 2: T7 Shield Failure
1. **Hour 1:** Don't panic, check backups
   - T7 Backup drive (last physical backup)
   - Google Drive (recent farms)
   - GitHub (all context/scripts)

2. **Hour 2-4:** Rebuild core
   ```bash
   # New drive setup
   mkdir -p /Volumes/T7\ Shield/{01_SYSTEM,02_KNOWLEDGE_BASE,03_BASE_DATA,04_DATA_PROJECTS,05_FARM_ASSESSMENT}
   
   # Clone GitHub context
   git clone https://github.com/LachyRitchie/gis-context /Volumes/T7\ Shield/01_SYSTEM/
   
   # Restore from backup
   rsync -av /Volumes/T7_Backup/ /Volumes/T7\ Shield/
   ```

3. **Hour 5+:** Resume work
   - Download any missing base data using `/01_SYSTEM/base_data_sources.yml`
   - Recreate recent data projects using RECIPE files

### Scenario 3: Corrupted Project
1. Check RECIPE.yml for recreation steps
2. Re-run from backed up scripts
3. If scripts missing, check GitHub history

---

## File Locations

### Critical Files to Track
```
/Volumes/T7 Shield/
├── 01_SYSTEM/
│   ├── BACKUP_PROTOCOL.md (this file)
│   ├── base_data_sources.yml
│   ├── derived_data_registry.yml
│   └── backup.log
├── 03_BASE_DATA/
│   ├── CURRENT/
│   │   └── CURRENT_VERSIONS.yml ← GitHub
│   └── DERIVED/ ← Physical backup
└── 05_FARM_ASSESSMENT/
    └── */04_OUTPUTS/ ← Google Drive (PDFs only)
```

### Scripts Location
```
~/Scripts/
└── backup_farms.sh ← Daily automated
```

---

## Integrated Maintenance

### Daily (Automated)
- Farm outputs → Google Drive (10pm)
- Check log when reviewing farms: `tail ~/gis_backup.log`

### On Project Completion (System Prompted)
- Data projects → T7 Backup (when >1GB complete)
- Update RECIPE.yml (Engineer does this)
- Push to GitHub (after major updates)

### No Scheduled Reminders Needed
- Physical backups triggered by project completion
- Log checks happen during normal farm review
- GitHub pushes happen with system updates

---

## Space Requirements

### Google Drive
- Current: ~15MB (farms)
- Growth: ~100MB/month
- Limit: 15GB free
- Monitor during farm reviews

### GitHub
- Current: ~10MB (text/scripts)
- Growth: Minimal
- Limit: 1GB free

### T7 Backup
- Current: Match T7 Shield
- Need: 2TB drive minimum
- Backup when prompted by system

---

## Troubleshooting

### "Backup didn't run"
1. Check LaunchAgent: `launchctl list | grep backup`
2. Check log: `tail ~/gis_backup.log`
3. Test manually: `~/Scripts/backup_farms.sh`

### "Out of Google Drive space"
1. Archive old farms to T7 Backup
2. Remove from Google Drive
3. Note in backup.log

### "Can't find a file"
1. Check CURRENT_VERSIONS.yml for location
2. Check RECIPE.yml for how to recreate
3. Check base_data_sources.yml for download URL

---

## Integration Points

### GIS Strategist System Prompt
```markdown
## Backup Integration
- Check backup.log during farm reviews
- Prompt T7 Backup after data projects >1GB
- Ensure RECIPE.yml creation
- Push updates to GitHub after system changes
```

### GIS Engineer Rules (.cursorrules)
**⚠️ CRITICAL: These rules supplement but DO NOT replace the GIS_ENGINEER.md system prompt**
**The system prompt at /00_SYSTEM_CONTROL/03_agent_prompts/GIS_ENGINEER.md is PRIMARY**

#### Core Requirements
- Create RECIPE.yml for all data projects
- Flag >1GB outputs for backup
- Never delete from 04_OUTPUTS folders
- Preserve all processing scripts in /PROCESSING/

#### File Preservation Rules
- NEVER delete from */04_OUTPUTS/ folders
- NEVER modify CURRENT_VERSIONS.yml without backup
- NEVER overwrite files in /03_BASE_DATA/DERIVED/
- ALWAYS preserve RECIPE.yml files
- ALWAYS document manual steps in RECIPE.yml

#### Backup Triggers
Flag for Strategist when:
- Creating outputs >1GB ("Created 2.3GB output - needs backup")
- Completing a multi-day project
- Modifying core data layers
- Before any destructive operations

#### Data Project Completion
When completing any project in /04_DATA_PROJECTS/:
1. Move final outputs to /03_BASE_DATA/DERIVED/
2. Create RECIPE.yml from template
3. Update CURRENT_VERSIONS.yml
4. Alert Strategist: "Data project complete - backup required"

#### Recovery Support
If data loss occurs:
1. Check BACKUP_PROTOCOL.md first
2. Look for RECIPE.yml to recreate
3. Check base_data_sources.yml for downloads
4. Never attempt recovery without Strategist

#### Daily Discipline
- Note critical files in execution log
- Flag large outputs with size in messages
- Preserve all scripts used
- Document any manual steps

---

## Contact & Support
- **System Owner:** Locky
- **GitHub Repo:** https://github.com/LachyRitchie/gis-context
- **Technical Support:** GIS Strategist + GIS Engineer
- **Recovery Time Objective:** 4 hours
- **Recovery Point Objective:** 1 day for farms, last backup for projects

---

*END OF PROTOCOL - No external reminders needed, all integrated into workflow*