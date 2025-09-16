# Binary Mask Complete Workflow - GEE to Google Earth
**Version:** 4.0  
**Last Updated:** 2025-09-15  
**Status:** PRODUCTION READY  
**Category:** Visualization Exports

## Executive Summary

Complete workflow for binary mask creation, export from Google Earth Engine, and visualization in Google Earth Pro. This consolidates all previous lessons learned into a single authoritative guide.

---

## Part 1: Google Earth Engine Export Issues

### The 80KB Export Problem

**Symptom:** Binary masks display correctly in GEE console but export as tiny 80KB files instead of expected 1MB+ files.

**Root Cause:** Masked pixels are excluded from exports, not assigned explicit values. The visualization pipeline handles masks differently than the export pipeline.

### Primary Solution: unmask() Function

**ALWAYS use `unmask()` before exporting binary masks:**

```javascript
// WRONG - Creates 80KB files
var binaryMask = image.gt(threshold);
Export.image.toDrive({
  image: binaryMask.toUint8(),
  description: 'binary_export_fails'
});

// CORRECT - Creates proper sized files
var binaryMask = image.gt(threshold);
var exportReady = binaryMask.unmask(0);  // Fill masked pixels with 0
Export.image.toDrive({
  image: exportReady.toUint8(),
  description: 'binary_export_works',
  scale: 30,
  region: geometry,
  maxPixels: 1e13,
  formatOptions: {
    noData: 255,
    cloudOptimized: true
  }
});
```

### Critical Export Parameters

```javascript
// Complete working export configuration
Export.image.toDrive({
  image: binaryMask.unmask(0).toUint8(),
  description: 'binary_mask_export',
  scale: 30,
  region: geometry.bounds(),  // Use rectangular bounds
  maxPixels: 1e13,
  fileFormat: 'GeoTIFF',
  formatOptions: {
    noData: 255,
    cloudOptimized: true
  },
  crs: 'EPSG:4326'
});
```

### Float64 vs Uint8 Behavior

- **Float64:** Preserves all pixels including nulls (larger files, ~21MB)
- **Uint8:** Compresses masked areas aggressively (80KB without unmask())
- **Solution:** Use `unmask(0)` before converting to Uint8

### Pre-Export Validation

```javascript
// Verify pixel counts before export
var stats = binaryMask.reduceRegion({
  reducer: ee.Reducer.count().combine(
    ee.Reducer.frequencyHistogram(), '', true
  ),
  geometry: geometry,
  scale: 30,
  maxPixels: 1e9
});
print('Pixel statistics:', stats);

// Check for masked pixels
var maskedCount = binaryMask.mask().not().reduceRegion({
  reducer: ee.Reducer.sum(),
  geometry: geometry,
  scale: 30,
  maxPixels: 1e9
});
print('Masked pixels:', maskedCount);
```

---

## Part 2: Google Earth Visualization

### Primary Method: Direct RGBA GeoTIFF Loading

**Workflow:**
1. **Load GeoTIFF directly in Google Earth Pro**
2. **Google Earth builds internal superoverlay automatically**
3. **Result:** Responsive, full-resolution, stable display

**When to Use:**
- Production client deliverables
- Analysis work requiring full detail
- Any binary mask visualization task

**Benefits:**
- Full resolution preserved (no downsampling)
- Stable performance (no conversion complexity)
- Proven reliability (Google Earth handles internally)
- No file size issues

### RGBA GeoTIFF Requirements

```bash
# Proper RGBA structure for Google Earth
# CRS: EPSG:4326 (WGS84)
# Structure: 4 bands (Red, Green, Blue, Alpha)
# Alpha Channel: 255 where mask=1 (excluded), 0 where mask=0 (suitable)
# NoData: 255 for excluded areas, 0 for suitable areas

# Example GDAL command for proper RGBA creation
gdal_calc.py -A input_binary.tif \
  --outfile=rgba_output.tif \
  --calc="255*(A==0)" \
  --NoDataValue=255 \
  --type=Byte \
  --format=GTiff \
  --co="COMPRESS=LZW" \
  --co="TILED=YES"
```

### Backup Method: Lightweight KMZ

**Use Cases:**
- Email sharing
- Demo purposes
- Client explicitly requests KMZ format

**Pipeline:**
1. Create alpha band using gdal_calc.py
2. Build RGBA VRT with proper band interpretation
3. Export to PNG (NOT KMLSUPEROVERLAY)
4. Create simple KML with bounds
5. Package as KMZ

**Script Location:** `mask2kmz.sh` (preserved and functional)

### File Size Expectations

- **National scale:** 300-500MB (acceptable)
- **State scale:** 50-200MB
- **Regional scale:** 10-50MB
- **Property scale:** 1-10MB

---

## Part 3: Banned Methods (NEVER USE)

### ❌ KMLSUPEROVERLAY
- **Problem:** Creates 480MB+ files, hours of processing
- **Issue:** Incompatible with Google Earth Pro/Web
- **Result:** Silent failures or crashes
- **Status:** PERMANENTLY BANNED

### ❌ Direct Binary Mask to KMZ
```bash
# WRONG - Creates 480MB unusable file
gdal_translate input_binary.tif output.kmz
```

### ❌ Downsampled PNG + KMZ
- **Problem:** Resolution cap (~2048x2048) loses critical detail
- **Issue:** Unacceptable for client deliverables
- **Result:** Technically works but professionally unusable

---

## Part 4: Production Workflow

### Step 1: GEE Export (Proper Configuration)
```javascript
// Create binary mask
var binaryMask = image.classify(classifier);

// Pre-export validation
var stats = binaryMask.reduceRegion({
  reducer: ee.Reducer.frequencyHistogram(),
  geometry: geometry,
  scale: 30,
  maxPixels: 1e9
});
print('Value distribution:', stats);

// Prepare for export
var exportReady = binaryMask.unmask(0);

// Export with proper settings
Export.image.toDrive({
  image: exportReady.toUint8(),
  description: 'binary_mask_for_google_earth',
  scale: 30,
  crs: 'EPSG:4326',
  region: geometry.bounds(),
  maxPixels: 1e13,
  fileFormat: 'GeoTIFF',
  formatOptions: {
    noData: 255,
    cloudOptimized: true
  }
});
```

### Step 2: RGBA Conversion (if needed)
```bash
# Only if GEE export isn't already RGBA
gdal_calc.py -A binary_mask.tif \
  --outfile=rgba_mask.tif \
  --calc="255*(A==0)" \
  --NoDataValue=255 \
  --type=Byte
```

### Step 3: Google Earth Pro Loading
1. **File → Open → Select GeoTIFF**
2. **Google Earth processes automatically**
3. **Verify display and transparency**

### Step 4: Quality Validation
- [ ] CRS is EPSG:4326
- [ ] File size appropriate for scale
- [ ] Opens correctly in Google Earth Pro
- [ ] Transparency working correctly
- [ ] Full resolution preserved

---

## Part 5: Common Mistakes to Avoid

### 1. **Skipping unmask() in GEE**
```javascript
// WRONG
var mask = image.gt(threshold);
Export.image.toDrive({image: mask.toUint8()});

// CORRECT
var mask = image.gt(threshold).unmask(0);
Export.image.toDrive({image: mask.toUint8()});
```

### 2. **Using Complex Geometry for Export Region**
```javascript
// WRONG - Causes inefficiency
region: complexPolygon

// CORRECT - Use bounds and mask the image
region: complexPolygon.bounds()
image: maskedImage.clip(complexPolygon)
```

### 3. **Ignoring QGIS When It Works**
- If QGIS displays correctly, use QGIS export
- Don't try to recreate with GDAL unnecessarily

### 4. **Converting Working Solutions**
- If direct GeoTIFF works, don't convert to KMZ
- Simple solutions are often the best solutions

---

## Part 6: Troubleshooting

### File Too Large (>500MB)
- Check if this is expected for national scale
- Verify RGBA structure is correct
- Consider if direct GeoTIFF use is better than conversion

### File Won't Open in Google Earth
- Check file size (should be <1GB for GeoTIFFs)
- Verify CRS is EPSG:4326
- Test with simple gdal_translate first

### Wrong Colors/Transparency
- Verify alpha channel is present and correct
- Check that color mapping was applied correctly
- Ensure RGBA output has 4 bands

### Export Still Tiny After unmask()
- Check that sameFootprint parameter: `unmask(0, false)`
- Verify geometry is correct
- Use rectangular bounds for region parameter

---

## Part 7: Production Ready Examples

**Location:** `/Volumes/T7 Shield/04_DATA_PROJECTS/Native_Title_EP_Exploration_National__Sept2025/PRODUCTS/`

**Validated Files:**
- `250mmRainfallConstraint_NativeTitle_v3.4.tif` (305MB)
- `ForestCover_2019_NativeTitle_v3.4.tif` (436MB)
- `ForestCover_2023_NativeTitle_v3.4.tif` (506MB)
- `Pre1750MVG_ForestPotential_NativeTitle_v3.4.tif` (346MB)
- `EPCarbonYield_NativeTitle_v3.4.tif` (6.1MB)
- `EPSuitabilityExclusions_Combined_NativeTitle_v3.4.tif` (450MB)

**Status:** All files QA validated, production-ready, no corrections needed

---

## Part 8: Critical Rules Summary

1. **ALWAYS use `unmask(0)` before exporting from GEE**
2. **Use RGBA GeoTIFFs directly in Google Earth Pro**
3. **Don't overcomplicate - simple solutions work best**
4. **Test with small dataset first**
5. **File size validation: KMZ >200MB = red flag**
6. **No KMLSUPEROVERLAY for binary masks**
7. **No downsampling for production deliverables**
8. **Use rectangular bounds for export regions**
9. **Set explicit noData values in formatOptions**
10. **Validate before batch processing**

---

*This guide consolidates all binary mask workflow knowledge. Reference this document for ALL binary mask tasks to prevent repetition of past failures.*