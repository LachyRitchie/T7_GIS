# Shared Compliance Requirements
**Version:** 1.0  
**Used by:** Both GIS Strategist and GIS Engineer  
**Purpose:** Mandatory standards for all GIS operations

---

## 🎯 ACCU METHOD COMPLIANCE

### Critical Rule: NEVER Mix Methods
Each ACCU method is completely separate with distinct requirements:

| Method | Code | Key Requirements | FullCAM Config |
|--------|------|-----------------|----------------|
| **Environmental Plantings** | EP | Permanent plantings, biodiversity focus | Standard Mixed Species Environmental |
| **Human Induced Regeneration** | HIR | Natural regeneration, grazing management | HIR-specific calibration |
| **Plantation Forestry** | PF | Commercial timber, rotation schedules | Standard Pinus Radiata 30-year |

### Method Verification
```python
# ALWAYS verify method before processing
def verify_method_compliance(project_name, method):
    # Check folder name matches method
    assert method in project_name, f"Method mismatch: {method} not in {project_name}"
    
    # Check FullCAM settings match
    fullcam_config = load_fullcam_config()
    assert fullcam_config.method == method, "FullCAM config doesn't match method"
    
    return True
```

### Documentation Requirements
Every project MUST clearly state:
1. Which ACCU method applies
2. Which determination version
3. FullCAM configuration used
4. Any method-specific exclusions

---

## 📐 DATA STANDARDS

### Coordinate Reference Systems
```
Primary CRS:
- EPSG:3577 - GDA94 / Australian Albers (PREFERRED)
- EPSG:4326 - WGS84 (for web/Google Earth)

State-specific (when required):
- EPSG:28354 - GDA94 / MGA Zone 54 (QLD)
- EPSG:28355 - GDA94 / MGA Zone 55 (NSW)
- EPSG:28356 - GDA94 / MGA Zone 56 (VIC/TAS)
```

### Raster Standards
```python
# MANDATORY raster parameters
RASTER_STANDARDS = {
    'pixel_size': 25,           # meters
    'alignment': True,          # -tap flag
    'nodata': {
        'byte': 255,
        'int16': -9999,
        'float32': -9999.0
    },
    'compression': 'LZW',
    'tiled': 'YES',
    'blocksize': 256,
    'bigtiff': 'IF_NEEDED'     # >4GB
}

# GDAL command template
gdal_command = """
gdalwarp -t_srs EPSG:3577 \
    -tr 25 25 -tap \
    -co COMPRESS=LZW \
    -co TILED=YES \
    -co BLOCKXSIZE=256 \
    -co BLOCKYSIZE=256 \
    -co BIGTIFF=IF_NEEDED \
    input.tif output_v1.0.tif
"""
```

### Vector Standards
```
Formats:
- GeoPackage (.gpkg) - PREFERRED
- Shapefile (.shp) - Legacy only
- GeoJSON (.geojson) - Web transfer

Geometry:
- Always validate geometry
- Fix topology errors
- Simplify if >1M vertices
```

---

## 📂 WORKING FOLDER DISCIPLINE

### Mandatory Structure
```
ALL work happens in PROCESSING folders:

/03_DATA_PROJECTS/ProjectName/
├── CURRENT/           # Latest versions only
├── ARCHIVE/           # Old versions with dates
├── PROCESSING/        # ← ALL WORK HERE
│   ├── temp/         # Temporary files
│   ├── testing/      # Test runs
│   ├── logs/         # Command logs
│   └── scripts/      # Processing scripts
└── RECIPE.yml        # What was done

/04_FARM_ASSESSMENT/FarmName/
├── 01_AOI/           # Area of interest
├── 02_INPUTS/        # Source data
├── 03_PROCESSING/    # ← ALL WORK HERE
├── 04_OUTPUTS/       # Final deliverables
└── 05_FULLCAM/       # FullCAM files
```

### Folder Rules
```
MANDATORY:
✓ All processing in PROCESSING folder
✓ No work at root level
✓ Archive before overwriting
✓ Clean temp files after job

FORBIDDEN:
✗ Creating /Volumes/T7 Shield/temp/
✗ Working in CURRENT directly
✗ Leaving test files scattered
✗ Processing in random locations
```

---

## 🏁 END-OF-PROJECT REQUIREMENTS

### Must Complete for EVERY Project
1. **Run end-of-project protocol**
   ```bash
   /Volumes/T7 Shield/00_SYSTEM_CONTROL/protocols/END_OF_PROJECT.md
   ```

2. **Create/Update RECIPE.yml**
   ```yaml
   project_name: "Forest_Cover_2019"
   date_completed: "2025-01-21"
   processing_steps:
     - step: 1
       tool: "gdalwarp"
       command: "gdalwarp -t_srs EPSG:3577..."
   outputs:
     - file: "ForestCover_National_2019_v1.0.tif"
       size_mb: 2048
   ```

3. **Update CURRENT_VERSIONS.yml**
   ```yaml
   ForestCover:
     current_version: "v1.0"
     file: "ForestCover_National_2019_v1.0.tif"
     location: "/03_DATA_PROJECTS/Forest_Cover_2019/"
     updated: "2025-01-21"
   ```

4. **Flag Large Files for Backup**
   ```
   Files >1GB requiring physical backup:
   - ForestCover_National_2019_v1.0.tif (2.1GB)
   - Biomass_National_2023_v2.0.tif (3.4GB)
   ```

---

## ⚠️ FULLCAM COMPLIANCE

### Server Configuration (CRITICAL)
```
EVERY FullCAM session MUST:
1. Select Internet → Server Settings
2. Tick "Use alternate"
3. Enter correct server:
   - 2020: http://www.fullcam.au/FullCAMServer2020
   - 2016: http://www.fullcam.au/FullCAMServer2016
4. Click OK
```

### Method-Specific Settings
| Setting | EP | HIR | PF |
|---------|----|----|-----|
| Soil Carbon | ❌ Prohibited | ❌ Prohibited | ✓ Optional |
| Forest Management | ❌ No | ✓ Yes | ✓ Yes |
| Calibration | Standard | HIR-specific | Commercial |
| Rotation | N/A | N/A | Schedule required |

### Validation Requirements
- Plot files must match CEA boundaries exactly
- Event timing must align with project start
- Management record must be complete
- Initial conditions must reflect baseline

---

## 🔍 QUALITY ASSURANCE

### Pre-Delivery Checklist
```markdown
## Quality Check
- [ ] CRS correct (EPSG:3577 or 4326)
- [ ] Pixel alignment verified (25m grid)
- [ ] NoData values correct
- [ ] File naming compliant
- [ ] Version documented
- [ ] RECIPE.yml created
- [ ] Tested in target application
- [ ] File size reasonable
- [ ] Pyramids built (if >100MB)
- [ ] Backup flagged (if >1GB)
```

### Validation Commands
```bash
# Check CRS
gdalinfo output.tif | grep "EPSG"

# Check alignment
gdalinfo output.tif | grep "Pixel Size"

# Check NoData
gdalinfo output.tif | grep "NoData"

# Check size
ls -lh output.tif

# Validate geometry
ogrinfo -al -geom=SUMMARY output.gpkg
```

---

## 🚨 CRITICAL WARNINGS

### NEVER
- Mix ACCU methods in one project
- Skip version numbers
- Process outside PROCESSING folders
- Deliver without testing
- Ignore FullCAM server settings
- Use non-standard pixel sizes
- Create files without versions

### ALWAYS
- Verify method compliance first
- Test with one file before batch
- Document what changed in each version
- Run end-of-project protocol
- Check file sizes before delivery
- Validate in target application
- Keep audit trail in RECIPE.yml

---

**Remember:** Compliance isn't optional. These requirements ensure ACCU scheme acceptance and client satisfaction.