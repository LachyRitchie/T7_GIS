# Binary Mask Visualization - Primary Method Established
**Date:** 2025-09-08  
**Status:** PRODUCTION READY  
**Priority:** HIGH

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

## Critical Rules

1. **Use RGBA GeoTIFFs directly** - This is the gold standard
2. **Don't overcomplicate** - If QGIS displays correctly, use that
3. **Test before batch processing** - Always validate one file first
4. **File size validation** - KMZ >200MB = red flag, investigate immediately
5. **No KMLSUPEROVERLAY** - Never use this format for binary masks

## Files Ready for Production

**Location:** `/Volumes/T7 Shield/04_DATA_PROJECTS/Native_Title_EP_Exploration_National__Sept2025/PRODUCTS/`

**Files:**
- `250mmRainfallConstraint_NativeTitle_v3.4.tif` (305MB)
- `ForestCover_2019_NativeTitle_v3.4.tif` (436MB)
- `ForestCover_2023_NativeTitle_v3.4.tif` (506MB)
- `Pre1750MVG_ForestPotential_NativeTitle_v3.4.tif` (346MB)
- `EPCarbonYield_NativeTitle_v3.4.tif` (6.1MB)
- `EPSuitabilityExclusions_Combined_NativeTitle_v3.4.tif` (450MB)

**Status:** All files QA validated, production-ready, no corrections needed

---

*This method should be used for ALL binary mask visualization tasks. The 8-hour failure taught us that simple solutions are often the best solutions.*
