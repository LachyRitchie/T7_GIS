# END-OF-PROJECT PROTOCOL - QUICK REFERENCE

## When to Run This Protocol

**GIS Engineer:** Run when instructed: "Run the end-of-project protocol"

**GIS Strategist:** Instruct Engineer to run after:
- ✅ Data project completion (03_DATA_PROJECTS)
- ✅ Farm assessment completion (04_FARM_ASSESSMENT)  
- ✅ Base data updates (02_BASE_DATA)
- ✅ Any major processing job >1GB
- ✅ Before switching to new project
- ✅ Weekly for ongoing projects (Friday)

## Full Protocol Location
`/Volumes/T7 Shield/00_SYSTEM_CONTROL/02_active_protocols/END_OF_PROJECT.md`

## What It Does
1. Verifies outputs are properly named
2. Archives old versions
3. Creates/updates RECIPE.yml
4. Updates CURRENT_VERSIONS.yml
5. Flags large files for backup
6. Commits to GitHub
7. Generates completion report
8. Cleans PROCESSING folders

## Project-Specific Actions
- **Data Projects:** All steps (1-9)
- **Farm Assessments:** Skip RECIPE & GitHub (skip 3 & 7)
- **Base Data:** Only verification & documentation (2,3,7,8)

## Key Outputs
- `PROJECT_COMPLETE.txt` - Summary report
- `BACKUP_MANIFEST.txt` - Files needing physical backup (if any)
- `RECIPE.yml` - Processing documentation
- Updated `/02_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml`

## Time Required
~5-10 minutes depending on project size

---
**Remember:** This protocol ensures consistency, documentation, and backup readiness across all GIS projects.
