# END OF PROJECT PROTOCOL
**Version:** 1.0  
**Last Updated:** 2025-01-21  
**Purpose:** Standardized checklist for GIS Engineer to execute at project completion

---

## 🚀 QUICK START
When instructed to "run the end-of-project protocol", execute ALL sections below in order.

---

## 1️⃣ PROJECT CLASSIFICATION
Determine project type FIRST:

```bash
# Check which folder you're in:
pwd
```

- **DATA PROJECT** → In `/03_DATA_PROJECTS/` → Do ALL sections
- **FARM ASSESSMENT** → In `/04_FARM_ASSESSMENT/` → Skip sections 3 & 7
- **BASE DATA UPDATE** → In `/02_BASE_DATA/` → Do sections 2, 3, 7, 8 only

---

## 2️⃣ OUTPUT VERIFICATION CHECKLIST

### File Organization
```bash
# From project root, verify structure:
find . -type f -name "*_temp*" -o -name "*_FIXED*" -o -name "*_backup*" | head -20

# If forbidden suffixes found, rename to proper versions:
# Pattern: What_Where_When_Version.ext
```

**Check:**
- [ ] NO files with forbidden suffixes (_FIXED, _aligned, _temp, _processed, _FINAL)
- [ ] All outputs follow naming convention: `What_Where_When_Version.ext`
- [ ] Working files contained in `/PROCESSING/` subfolder
- [ ] Final outputs in project root or appropriate subfolder

### Archive Old Versions
```bash
# Create archive if needed
mkdir -p ARCHIVE/$(date +%Y%m%d)

# Move superseded versions (keep only latest)
# Example: mv ForestCover_National_2019_v1.0.tif ARCHIVE/$(date +%Y%m%d)/
```

---

## 3️⃣ RECIPE.YML CREATION (DATA PROJECTS ONLY)

### Check if RECIPE.yml exists:
```bash
ls -la RECIPE.yml
```

### If missing, create from template:
```bash
cp /Volumes/T7\ Shield/00_SYSTEM_CONTROL/02_active_protocols/RECIPE.yml ./RECIPE.yml
```

### Update RECIPE.yml with:
```yaml
# Required fields to complete:
project_name: "[ProjectName]"
date_completed: "YYYY-MM-DD"
data_sources:
  - source: "[Input file used]"
    version: "[Version number]"
    location: "[Path to source]"
processing_steps:
  - step: 1
    tool: "[GDAL/QGIS/Python]"
    command: "[Actual command used]"
outputs:
  - file: "[Output filename]"
    size_mb: [Size in MB]
    crs: "EPSG:XXXX"
validation:
  pixel_size: "25m"
  extent_matches_source: true/false
  nodata_value: 255
```

### Validate RECIPE.yml:
```bash
# Check it's readable
head -20 RECIPE.yml
```

---

## 4️⃣ UPDATE CURRENT_VERSIONS.YML

### For ANY new versioned outputs:
```bash
# Open for editing
cat /Volumes/T7\ Shield/02_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml
```

### Add/update entries:
```yaml
# Format for each dataset:
dataset_name:
  current_version: "vX.X"
  file: "Filename_Location_Date_vX.X.ext"
  location: "/path/to/file"
  updated: "YYYY-MM-DD"
  notes: "What changed in this version"
```

### Verify update:
```bash
grep -A 3 "[YourDatasetName]" /Volumes/T7\ Shield/02_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml
```

---

## 5️⃣ BACKUP REQUIREMENTS CHECK

### Identify large files needing physical backup:
```bash
# Find all files >1GB
find . -type f -size +1G -exec ls -lh {} \; 2>/dev/null | awk '{print $9, $5}'
```

### Create backup manifest:
```bash
# If large files found, create manifest
echo "=== BACKUP REQUIRED ===" > BACKUP_MANIFEST.txt
echo "Date: $(date)" >> BACKUP_MANIFEST.txt
echo "Project: $(pwd)" >> BACKUP_MANIFEST.txt
echo "" >> BACKUP_MANIFEST.txt
echo "Files requiring physical backup:" >> BACKUP_MANIFEST.txt
find . -type f -size +1G -exec ls -lh {} \; 2>/dev/null >> BACKUP_MANIFEST.txt
```

### Flag for user:
```
⚠️ PHYSICAL BACKUP NEEDED:
The following files exceed 1GB and need manual backup to external drive:
[List files]
Total size: [XXX GB]
```

---

## 6️⃣ CLEAN PROCESSING FOLDERS

### Remove temporary files:
```bash
# List what will be deleted (dry run)
find PROCESSING -type f \( -name "*.aux.xml" -o -name "*.cpg" -o -name "*.qgz~" \) -print

# If safe, delete
find PROCESSING -type f \( -name "*.aux.xml" -o -name "*.cpg" -o -name "*.qgz~" \) -delete

# Remove empty directories
find PROCESSING -type d -empty -delete
```

### Compress if keeping:
```bash
# If PROCESSING has valuable intermediate files
tar -czf PROCESSING_archive_$(date +%Y%m%d).tar.gz PROCESSING/
# Then clear originals if compression successful
```

---

## 7️⃣ GITHUB COMMIT (DATA PROJECTS & BASE DATA)

### Check for repository:
```bash
cd /Volumes/T7\ Shield/
git status 2>/dev/null || echo "No Git repo found"
```

### If repo exists, commit important changes:
```bash
# Add documentation and recipes only (not large data files)
git add 00_SYSTEM_CONTROL/*.md
git add 02_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml
git add */RECIPE.yml
git add */*.qml */*.qpt */*.model3

# Commit with descriptive message
git commit -m "Project complete: [ProjectName] - [Brief description]"

# Push if remote configured
git push origin main 2>/dev/null || echo "Remote not configured"
```

---

## 8️⃣ GENERATE COMPLETION REPORT

### Create report:
```bash
cat << EOF > PROJECT_COMPLETE.txt
PROJECT COMPLETION REPORT
========================
Date: $(date)
Project: $(basename $(pwd))
Location: $(pwd)

OUTPUTS CREATED:
$(ls -lh *.tif *.gpkg *.shp 2>/dev/null | awk '{print "- " $9 " (" $5 ")"}')

TOTAL SIZE:
$(du -sh . | awk '{print $1}')

RECIPE: $([ -f RECIPE.yml ] && echo "✓ Created" || echo "✗ Missing")
CURRENT_VERSIONS: $(grep -q $(basename $(pwd)) /Volumes/T7\ Shield/02_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml && echo "✓ Updated" || echo "✗ Not updated")
BACKUP NEEDED: $(find . -size +1G 2>/dev/null | wc -l) files >1GB

PROCESSING FOLDER: $([ -d PROCESSING ] && echo "✓ Cleaned" || echo "N/A")

CHECKLIST COMPLETE: $(date +"%Y-%m-%d %H:%M")
EOF

cat PROJECT_COMPLETE.txt
```

---

## 9️⃣ FINAL VERIFICATION

### Run final checks:
```bash
# Confirm no forbidden suffixes remain
echo "Forbidden suffixes check:"
find . -type f \( -name "*_FIXED*" -o -name "*_temp*" -o -name "*_aligned*" \) 2>/dev/null | wc -l

# Confirm CURRENT_VERSIONS updated
echo "CURRENT_VERSIONS check:"
tail -20 /Volumes/T7\ Shield/02_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml

# Confirm documentation present
echo "Documentation check:"
ls -la *.yml *.txt *.md 2>/dev/null
```

---

## 🎯 COMPLETION MESSAGE

Copy and send to user:

```
✅ END-OF-PROJECT PROTOCOL COMPLETE

Project: [Project Name]
Location: [Path]

COMPLETED:
✓ Outputs verified and properly named
✓ Old versions archived
✓ RECIPE.yml [created/updated]
✓ CURRENT_VERSIONS.yml [updated/checked]
✓ Processing folders cleaned
✓ GitHub committed
✓ Completion report generated

ACTION REQUIRED:
[If applicable:]
⚠️ Physical backup needed for X files totaling XX GB
⚠️ See BACKUP_MANIFEST.txt for details

Report saved: PROJECT_COMPLETE.txt
```

---

## 📌 QUICK REFERENCE

**For Data Projects:** Do ALL sections (1-9)  
**For Farm Assessments:** Skip sections 3 & 7  
**For Base Data Updates:** Do sections 2, 3, 7, 8 only  

**Key Files:**
- `/00_SYSTEM_CONTROL/02_active_protocols/RECIPE.yml` - Recipe template
- `/02_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml` - Version registry
- GitHub repo: `https://github.com/LachyRitchie/gis-context`

**Questions?** Check with GIS Strategist before proceeding if unsure.
