# Shared Naming Rules
**Version:** 1.0  
**Used by:** Both GIS Strategist and GIS Engineer  
**Authority:** This is the SINGLE SOURCE OF TRUTH for naming conventions

---

## 📝 FILE NAMING PATTERN

### Mandatory Pattern: `What_Where_When_Version.ext`

**Components:**
- **What:** Descriptive name (CamelCase)
- **Where:** Location (National, NSW, QLD, Farm, etc.)
- **When:** Year or date (optional for static datasets)
- **Version:** vX.Y format (ALWAYS required)
- **ext:** File extension

### ✅ CORRECT Examples
```
ForestCover_National_2019_v1.0.tif
EPExclusion_National_v2.0.tif
CarbonYield_NSW_2023_v1.1.tif
PropertyBoundary_Hewitts_v1.0.gpkg
CEABoundaries_National_v2.1.shp
PlantingMask_QLD_2023_v1.0.tif
```

### ❌ FORBIDDEN Suffixes (AUTOMATIC REJECTION)
```
NEVER USE THESE:
_fixed, _FIXED          → Use version increment instead
_aligned, _ALIGNED      → Use version increment instead  
_temp, _temporary, _tmp → Use PROCESSING/temp/ folder
_final, _FINAL         → Use version number
_processed, _processing → Already in PROCESSING folder
_combined, _merged     → Use descriptive What component
_backup, _copy         → Use ARCHIVE folder
_new, _old, _original  → Use version system
_test, _testing        → Use PROCESSING/testing/ folder
_corrected, _updated   → Use version increment
```

---

## 📁 FOLDER NAMING PATTERNS

### Data Projects
**Pattern:** `What_DataDate_Where__ProjectDate`

⚠️ **CRITICAL:** Note the DOUBLE UNDERSCORE (`__`) before project date!

**Examples:**
```
✅ Forest_Cover_2019_National__Sept2025
✅ EP_Exclusion_Mask_National__Jan2025
✅ Carbon_Yield_2023_NSW__Feb2025

❌ Forest_Cover_2019_National_Sept2025  (missing double underscore)
❌ EP_Exclusion_FINAL                   (missing project date)
❌ Forest_Cover_v2                       (wrong pattern entirely)
```

### Farm Assessments
**Pattern:** `PropertyName_Method_State_YYYY-MM`

**Method Codes:**
- EP = Environmental Plantings
- HIR = Human Induced Regeneration
- PF = Plantation Forestry

**Examples:**
```
✅ Hewitts_PF_TAS_2025-01
✅ Smithfield_EP_NSW_2025-02
✅ Riverside_HIR_QLD_2024-12

❌ Hewitts_Farm_Assessment     (missing method, state, date)
❌ Smithfield_Project          (wrong pattern)
❌ Riverside_EP_Assessment     (missing state and date)
```

---

## 🔢 VERSION RULES

### Version Numbering
- **Initial version:** Always v1.0
- **Minor fix/adjustment:** v1.0 → v1.1 → v1.2 → v1.3...
- **Major methodology change:** v1.x → v2.0
- **NEVER skip versions:** Must increment sequentially
- **NEVER reuse versions:** Once v1.1 exists, never overwrite

### When to Increment
| Change Type | Version Change | Example |
|------------|---------------|---------|
| Fix alignment | Minor | v1.0 → v1.1 |
| Add pyramids | Minor | v1.1 → v1.2 |
| Fix NoData | Minor | v1.2 → v1.3 |
| Change methodology | Major | v1.3 → v2.0 |
| New data source | Major | v2.0 → v3.0 |

### Documentation
Every version change MUST be logged:
```bash
echo "v1.1: Aligned to standard 25m grid" >> version_log.txt
echo "v1.2: Added pyramids for performance" >> version_log.txt
echo "v2.0: Recreated with 2023 source data" >> version_log.txt
```

---

## 🚫 VALIDATION PROTOCOL

### Before Creating ANY File
```python
# MANDATORY VALIDATION
filename = "proposed_filename.tif"

# Check 1: Pattern compliance
pattern = r'^[A-Z][a-zA-Z]+(_[A-Z][a-zA-Z]+)+_v\d+\.\d+\.\w+$'
assert re.match(pattern, filename), f"Invalid pattern: {filename}"

# Check 2: No forbidden suffixes
forbidden = ['_fixed', '_aligned', '_temp', '_final', '_processed']
for suffix in forbidden:
    assert suffix not in filename.lower(), f"Forbidden suffix: {suffix}"

# Check 3: Version exists
assert re.search(r'_v\d+\.\d+', filename), "Missing version number"

print(f"✅ VALIDATED: {filename}")
```

---

## 📂 WORKING FOLDER DISCIPLINE

### ALL Work Happens In PROCESSING Folders

**Data Projects:**
```
/03_DATA_PROJECTS/ProjectName/
└── PROCESSING/          ← ALL WORK HERE
    ├── temp/           ← Temporary files
    ├── testing/        ← Test runs
    ├── logs/           ← Processing logs
    └── scripts/        ← Project scripts
```

**Farm Assessments:**
```
/04_FARM_ASSESSMENT/FarmName/
└── 03_PROCESSING/       ← ALL WORK HERE
```

### NEVER Create These
```
❌ /Volumes/T7 Shield/temp_work/
❌ /Volumes/T7 Shield/rainfall_processing/
❌ /Volumes/T7 Shield/my_analysis/
❌ Any folder at root level for temporary work
```

---

## ⚡ QUICK REFERENCE

### Naming Checklist
- [ ] Follows What_Where_When_Version pattern
- [ ] Has version number (vX.Y)
- [ ] No forbidden suffixes
- [ ] CamelCase for What component
- [ ] Stored in correct PROCESSING folder

### Common Mistakes to Avoid
1. **Adding descriptive suffixes** → Use version log instead
2. **Forgetting version numbers** → Always required
3. **Creating root-level folders** → Use PROCESSING
4. **Mixing naming patterns** → Follow ONE pattern
5. **Reusing version numbers** → Always increment

---

**Remember:** This document is the ONLY authority on naming. If in doubt, check here first.