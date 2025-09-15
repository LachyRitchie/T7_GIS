# Critical Patterns (Updated 2025-09-15)

## Most Frequent Failures
Based on comprehensive analysis of lessons learned:

### 1. Binary Mask Export Issues (80KB Problem)
- **Problem:** GEE exports binary masks as tiny files despite correct console display
- **Root Cause:** Masked pixels excluded from export, not assigned explicit values
- **Solution:** ALWAYS use `unmask(0)` before exporting from GEE
- **Reference:** `by_category/visualization_exports/binary_mask_workflow_complete_v4.0.md`

### 2. Overcomplicating Simple Solutions
- **Problem:** Converting working solutions unnecessarily (QGIS → GDAL → KMZ → failure)
- **Root Cause:** Ignoring simple solutions that already work
- **Solution:** If QGIS displays correctly, use QGIS export directly

### 3. File Size Red Flags
- **Problem:** Not validating expected vs actual file sizes
- **Root Cause:** Processing errors or wrong parameters
- **Solution:** Calculate expected size: (area_hectares / 0.01) * bytes_per_pixel

## Proven Successful Patterns

### Binary Masks → Google Earth (PRODUCTION METHOD)
```
1. GEE Export: Use unmask(0) before export, EPSG:4326, proper formatOptions
2. Google Earth: Load RGBA GeoTIFF directly (Google Earth handles superoverlay)
3. Expected size: 300-500MB (national), 50-200MB (state), 1-10MB (property)
4. Status: PRODUCTION READY
```

### Continuous Data → Google Earth
```
1. gdaldem color-relief with proper color mapping
2. Verify 4-band RGBA output
3. gdal_translate to simple KML (NOT KMLSUPEROVERLAY)
4. Manual GroundOverlay KML creation
5. Expected size: 50-200MB
```

### GEE Python API Exports
```
1. Complex boolean operations: (condition1.And(condition2))
2. Pre-validation: Check pixel counts and geometry
3. Export parameters: unmask(0), rectangular bounds, maxPixels=1e13
4. File size validation before batch processing
```

## Red Flags to Watch For

### Critical Warnings
- **80KB files from GEE:** Missing unmask() function
- **480MB+ KMZ files:** Using KMLSUPEROVERLAY (banned)
- **Processing >4 hours:** Wrong approach, reconsider methodology
- **Client delivery >2GB:** Impractical, find alternative

### Size Validation Rules
- **Binary masks:** 1-500MB depending on scale
- **Continuous rasters:** 50-200MB typical
- **KMZ files:** >200MB = red flag, investigate immediately
- **Client downloads:** >2GB = impractical for most clients

## Banned Methods (NEVER USE)

### ❌ KMLSUPEROVERLAY for Binary Masks
- Creates 480MB+ unusable files
- Incompatible with Google Earth Pro/Web
- Status: PERMANENTLY BANNED

### ❌ Direct Binary Mask to KMZ without RGBA
- Creates massive files Google Earth can't open
- Bypasses proper color mapping
- Status: ALWAYS FAILS

### ❌ Downsampling Production Deliverables
- Loses critical detail for client analysis
- Professionally unacceptable quality
- Status: NOT VIABLE FOR PRODUCTION

## Quick Reference by Task

### Binary Mask Creation & Visualization
**Primary Method:** Direct RGBA GeoTIFF loading in Google Earth Pro
**Backup Method:** Lightweight KMZ using mask2kmz.sh script
**Critical Step:** ALWAYS use unmask(0) in GEE exports
**File Size:** 1-500MB (varies by scale)

### Large-Scale Raster Processing
**Tool Selection:** Follow execution matrix in system prompt
**Thresholds:** >5 files OR >100MB OR >5min = handover to Engineer
**Critical Step:** Test with single file first
**Validation:** Verify client can actually use output format

### GEE Export Troubleshooting
**Pre-flight:** Check pixel counts, geometry validity, value distribution
**Export Config:** unmask(0), rectangular bounds, proper formatOptions
**Post-validation:** Verify file size matches expected calculation
**Red Flag:** 80KB files = export error, not data sparsity

## Current Production Files

**Location:** `/Volumes/T7 Shield/04_DATA_PROJECTS/Native_Title_EP_Exploration_National__Sept2025/PRODUCTS/`
**Status:** QA validated, production-ready
**Total Size:** 2.1GB (6 files)
**Method:** Binary mask workflow v4.0
**Client Compatible:** Yes (RGBA GeoTIFF format)

---

**Last Updated:** 2025-09-15  
**Version:** 4.0  
**Next Review:** After next major project completion