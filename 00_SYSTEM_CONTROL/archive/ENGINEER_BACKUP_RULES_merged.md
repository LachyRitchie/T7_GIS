# GIS Engineer Backup Integration
# ADD THIS SECTION TO .cursorrules

## Backup Protocols

### During Data Projects
When completing any data project in /04_DATA_PROJECTS/:
1. Move final outputs to /03_BASE_DATA/DERIVED/
2. Create RECIPE.yml from template in /01_SYSTEM/
3. Update CURRENT_VERSIONS.yml
4. Alert Strategist: "Data project complete - backup required"

### File Preservation Rules
- NEVER delete from */04_OUTPUTS/ folders
- NEVER modify CURRENT_VERSIONS.yml without backup
- NEVER overwrite files in /03_BASE_DATA/DERIVED/
- ALWAYS preserve RECIPE.yml files

### Backup Triggers
Flag for Strategist when:
- Creating outputs >1GB
- Completing a multi-day project  
- Modifying core data layers
- Before any destructive operations

### Recovery Support
If data loss occurs:
1. Check /01_SYSTEM/BACKUP_PROTOCOL.md
2. Look for RECIPE.yml to recreate
3. Check base_data_sources.yml for downloads
4. Never attempt recovery without Strategist

### Daily Discipline
- Note critical files in execution log
- Flag large outputs: "Created 2.3GB output - needs backup"
- Preserve all scripts used in /PROCESSING/
- Document any manual steps in RECIPE.yml