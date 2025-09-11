# Binary Mask Visualization - Complete Guide
**Last Updated:** 2025-09-08  
**Status:** PRODUCTION READY  
**Category:** Visualization Exports

## Executive Summary

After 8+ hours of failed attempts, we established the correct approach for binary mask visualization in Google Earth. **Use full-resolution RGBA GeoTIFFs directly** rather than converting to KMZ.

## Primary Method: Full-Resolution RGBA GeoTIFFs

### Workflow
1. **Load GeoTIFF directly in Google Earth Pro**
2. **Google Earth builds internal superoverlay automatically**
3. **Result:** Responsive, full-resolution, stable display

### When to Use
- **Production client deliverables**
- **Analysis work requiring full detail**
- **Any binary mask visualization task**

### Benefits
- **Full resolution preserved** (no downsampling)
- **Stable performance** (no conversion complexity)
- **Proven reliability** (Google Earth handles internally)
- **No file size issues** (no 480MB disasters)

## Backup Method: Mask2 Pipeline

### Script
- **File:** `mask2kmz.sh` (preserved and functional)
- **Use cases:** Lightweight sharing, email/demo purposes
- **When client explicitly requests KMZ format**

### Pipeline Steps
1. Create alpha band (gdal_calc.py)
2. Build RGBA VRT with proper band interpretation
3. Export to PNG (NOT KMLSUPEROVERLAY)
4. Create simple KML with bounds
5. Package as KMZ

### Limitations
- **Adds unnecessary complexity** for production
- **Either reduces resolution or bloats file sizes**
- **Less stable than direct GeoTIFF use**

## Banned Methods

### ❌ KMLSUPEROVERLAY
- **Problem:** Creates 480MB+ files, hours of processing
- **Issue:** Incompatible with Google Earth Pro/Web
- **Result:** Silent failures or crashes
- **Status:** PERMANENTLY BANNED

### ❌ Downsampled PNG + KMZ
- **Problem:** Resolution cap (~2048x2048) loses critical detail
- **Issue:** Unacceptable for client deliverables
- **Result:** Technically works but professionally unusable
- **Status:** NOT VIABLE FOR PRODUCTION

### ❌ Direct Binary Mask to KMZ
- **Problem:** No color mapping applied
- **Issue:** Creates unusable files
- **Result:** 480MB files that Google Earth cannot open
- **Status:** NEVER DO THIS

## Technical Details

### RGBA GeoTIFF Requirements
- **CRS:** EPSG:4326 (WGS84)
- **Structure:** 4 bands (Red, Green, Blue, Alpha)
- **Alpha Channel:** 255 where mask=1 (excluded), 0 where mask=0 (suitable)
- **NoData:** 255 for excluded areas, 0 for suitable areas

### File Size Expectations
- **National scale:** 300-500MB (acceptable)
- **State scale:** 50-200MB
- **Regional scale:** 10-50MB
- **Property scale:** 1-10MB

### Validation Checklist
- [ ] CRS is EPSG:4326
- [ ] 4 bands present (RGBA)
- [ ] Alpha channel working correctly
- [ ] File size reasonable for scale
- [ ] Opens correctly in Google Earth Pro

## Common Mistakes to Avoid

### 1. **Converting Binary Masks Directly to KMZ**
```bash
# WRONG - Creates 480MB unusable file
gdal_translate input_binary.tif output.kmz
```

### 2. **Using KMLSUPEROVERLAY**
```bash
# WRONG - Incompatible with Google Earth
gdal_translate -of KMLSUPEROVERLAY input.tif output.kmz
```

### 3. **Downsampling for "Efficiency"**
```bash
# WRONG - Loses critical detail
gdal_translate -of PNG -outsize 2048 2048 input.tif output.png
```

### 4. **Ignoring QGIS When It Works**
- If QGIS displays correctly, use QGIS export
- Don't try to recreate with GDAL
- Leverage existing rendering solutions

## Troubleshooting

### File Too Large (>500MB)
- Check if this is expected for national scale
- Verify RGBA structure is correct
- Consider if direct GeoTIFF use is better

### File Won't Open in Google Earth
- Check file size (should be <1GB for GeoTIFFs)
- Verify CRS is EPSG:4326
- Test with simple gdal_translate first

### Wrong Colors/Transparency
- Verify alpha channel is present
- Check that color mapping was applied correctly
- Ensure RGBA output has 4 bands

## Production Files Ready

**Location:** `/Volumes/T7 Shield/04_DATA_PROJECTS/Native_Title_EP_Exploration_National__Sept2025/PRODUCTS/`

**Files:**
- `250mmRainfallConstraint_NativeTitle_v3.4.tif` (305MB)
- `ForestCover_2019_NativeTitle_v3.4.tif` (436MB)
- `ForestCover_2023_NativeTitle_v3.4.tif` (506MB)
- `Pre1750MVG_ForestPotential_NativeTitle_v3.4.tif` (346MB)
- `EPCarbonYield_NativeTitle_v3.4.tif` (6.1MB)
- `EPSuitabilityExclusions_Combined_NativeTitle_v3.4.tif` (450MB)

**Status:** All files QA validated, production-ready, no corrections needed

## Critical Rules

1. **Use RGBA GeoTIFFs directly** - This is the gold standard
2. **Don't overcomplicate** - If QGIS displays correctly, use that
3. **Test before batch processing** - Always validate one file first
4. **File size validation** - KMZ >200MB = red flag, investigate immediately
5. **No KMLSUPEROVERLAY** - Never use this format for binary masks
6. **No downsampling** - Preserve full resolution for client deliverables

---

*This guide consolidates all binary mask visualization knowledge. Reference this before any binary mask task to prevent repetition of the 8-hour failure.*
