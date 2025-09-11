# GIS ENGINEER QUICK REFERENCE CARD
**Keep this open while working**

---

## 🚦 DECISION FLOWCHART
```
Is task clear? → NO → Ask Strategist
     ↓ YES
Will it take >5min? → YES → Get approval
     ↓ NO  
Will output be >100MB? → YES → Check approach
     ↓ NO
Do I know the pattern? → NO → Check lessons_learned/
     ↓ YES
PROCEED WITH TASK
```

---

## ✅ FILE NAMING CHEATSHEET

### The ONLY Pattern Allowed
`What_Where_When_Version.ext`

### Quick Examples
```bash
# Raster data
ForestCover_National_2019_v1.0.tif
ForestCover_NSW_2019_v1.0.tif
ForestCover_Farm_2019_v1.0.tif

# Vector data  
PropertyBoundary_Hewitts_v1.0.gpkg
CEABoundaries_National_v2.1.shp

# Masks
EPExclusion_National_v1.0.tif
PlantingMask_QLD_2023_v1.0.tif
```

### Version Incrementing
- First version: v1.0
- Minor fix: v1.0 → v1.1
- Another fix: v1.1 → v1.2
- Major change: v1.2 → v2.0

### ❌ NEVER USE THESE
```
file_FIXED.tif        → Use v1.1
file_aligned.tif      → Use v1.1
file_temp.tif         → Use PROCESSING/temp/
file_final.tif        → Use v1.0
file_processed.tif    → Use descriptive What
```

---

## 📁 WHERE TO WORK

### Data Projects
```
/03_DATA_PROJECTS/ProjectName/
└── PROCESSING/          ← ALL WORK HERE
    ├── temp/           ← Temporary files
    ├── logs/           ← Command logs
    └── testing/        ← Test runs
```

### Farm Assessments
```
/04_FARM_ASSESSMENT/PropertyName_Method_State_Date/
└── 03_PROCESSING/       ← ALL WORK HERE
```

### NEVER Create Folders At Root Level

---

## 🎯 PROVEN PATTERNS

### Binary Mask → Google Earth
```bash
# Method: RGBA GeoTIFF
gdal_translate -of GTiff \
  -b 1 -b 1 -b 1 -b 1 \
  -colorinterp_1 red \
  -colorinterp_2 green \
  -colorinterp_3 blue \
  -colorinterp_4 alpha \
  -scale_4 0 1 0 255 \
  input.tif output_v1.0.tif
```

### Standard GDAL Settings
```bash
-co COMPRESS=LZW \
-co TILED=YES \
-co BLOCKXSIZE=256 \
-co BLOCKYSIZE=256 \
-co BIGTIFF=YES
```

### Standard Alignment
```bash
-tr 25 25 -tap  # 25m pixels, grid aligned
```

---

## 🔍 BEFORE EVERY TASK

1. **Check Lessons Learned**
   ```bash
   ls /01_KNOWLEDGE_CONTEXT/lessons_learned/by_category/
   ```

2. **Check Current Versions**
   ```bash
   grep "dataset_name" /02_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml
   ```

3. **Estimate Output**
   - Size: Will it be >100MB?
   - Time: Will it take >5min?
   - Count: More than 5 files?

4. **Test First**
   - Always test with ONE file
   - Verify output is correct
   - Check file size is reasonable

---

## 🏁 AFTER EVERY JOB

Run the end-of-project protocol:
```bash
# Follow the checklist at:
/Volumes/T7 Shield/00_SYSTEM_CONTROL/02_active_protocols/END_OF_PROJECT.md
```

This handles:
- File verification
- RECIPE.yml creation  
- Version registry update
- Backup flagging
- Completion report

---

## 🚨 WHEN TO STOP & ASK

**STOP if:**
- Output will be >500MB
- Processing will take >30min
- You're not sure about approach
- File naming isn't clear
- Previous attempt failed

**ASK for:**
- Clarification on requirements
- Approval for long-running scripts
- Alternative approaches
- Help with errors

---

## 💻 COMMAND TEMPLATES

### Create Aligned Raster
```bash
gdalwarp -t_srs EPSG:3577 -tr 25 25 -tap \
  -co COMPRESS=LZW -co TILED=YES \
  input_v1.0.tif output_v1.1.tif
```

### Extract State Boundary
```bash
ogr2ogr -where "STATE='NSW'" \
  NSW_Boundary_v1.0.gpkg \
  /02_BASE_DATA/Australia_Boundaries_v1.0.gpkg
```

### Build Pyramids
```bash
gdaladdo -ro --config COMPRESS_OVERVIEW LZW \
  file_v1.0.tif 2 4 8 16 32 64 128
```

### Create Binary Mask
```bash
gdal_calc.py -A input.tif \
  --calc="(A>0)*1" \
  --NoDataValue=255 \
  --outfile=Mask_Location_v1.0.tif
```

---

## 📞 QUICK PATHS

```bash
# Your workspace
cd /Volumes/T7\ Shield/03_DATA_PROJECTS/

# Lessons learned
cd /Volumes/T7\ Shield/01_KNOWLEDGE_CONTEXT/lessons_learned/

# Current versions
cat /Volumes/T7\ Shield/02_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml

# Protocols
ls /Volumes/T7\ Shield/00_SYSTEM_CONTROL/02_active_protocols/
```

---

## ⚡ KEYBOARD SHORTCUTS

Remember:
- `Cmd+K` to clear terminal
- `Ctrl+C` to stop processing
- `Tab` for path completion
- `history | grep gdal` to find past commands

---

**Golden Rule:** When in doubt, ASK. Better to clarify than to redo.
