# Google Earth Compatibility Issues - Complete Guide
**Last Updated:** 2025-09-08  
**Category:** Visualization Exports

## Critical Compatibility Issues

### 1. KMLSUPEROVERLAY Incompatibility

**Problem:** Google Earth Web and Google Earth Pro on Mac do NOT support KMLSUPEROVERLAY format.

**What KMLSUPEROVERLAY Creates:**
- NetworkLink elements (for loading tiles on demand)
- Region elements (for level-of-detail control)
- Complex tiled pyramid structure

**Why It Fails:**
- These are KML 2.2 advanced features
- Google Earth Web: No support
- Google Earth Pro on Mac: Silent failure (no error message)
- Result: Nothing happens when clicking the KMZ file

**Solution:**
- Use simple GroundOverlay KML instead
- Single image overlay approach
- Maximum compatibility across all Google Earth versions

### 2. PNG Transparency Failures

**Problem:** GDAL PNG conversion for binary masks fails to preserve transparency.

**What Goes Wrong:**
- GDAL creates black rectangles instead of transparent areas for value=0
- Source TIFFs have nodata=255 but PNG conversion treats everything as opaque
- Result: Giant black rectangle covering all of Australia instead of transparent suitable areas

**Root Cause:**
- GDAL PNG conversion doesn't automatically handle transparency for binary masks with nodata=255 values
- Wrong assumptions about GDAL behavior with binary data
- Missing transparency handling in conversion pipeline

**Solution:**
- Use QGIS rendered export instead of GDAL PNG conversion
- QGIS rendering engine handles edge cases better than GDAL
- If QGIS displays correctly, use QGIS export

### 3. File Size Issues

**Problem:** Oversized files cause Google Earth to crash or fail silently.

**Red Flags:**
- KMZ files >200MB for binary masks
- Processing time >30 minutes for simple tasks
- Files that "work" but cause Google Earth to be unstable

**Solutions:**
- Use full-resolution RGBA GeoTIFFs directly (preferred)
- Create lightweight KMZs only when specifically requested
- Always validate file sizes before delivery

## Recommended Approaches

### 1. Full-Resolution RGBA GeoTIFFs (PREFERRED)
- **Method:** Load GeoTIFF directly in Google Earth Pro
- **Benefits:** Full resolution, stable performance, no conversion complexity
- **Use case:** Production client deliverables

### 2. Simple GroundOverlay KML
- **Method:** Single image overlay with LatLonBox
- **Benefits:** Maximum compatibility, lightweight
- **Use case:** When KMZ format specifically required

### 3. QGIS Rendered Export
- **Method:** Export as rendered image from QGIS
- **Benefits:** Preserves QGIS styling, handles transparency correctly
- **Use case:** When QGIS already displays correctly

## Banned Methods

### ❌ KMLSUPEROVERLAY
- Incompatible with Google Earth
- Creates massive files
- Hours of processing for unusable results
- **Status:** PERMANENTLY BANNED

### ❌ Complex GDAL PNG Conversion
- Fails to preserve transparency
- Creates black rectangles instead of transparent areas
- **Status:** AVOID FOR BINARY MASKS

### ❌ Direct Binary Mask to KMZ
- No color mapping applied
- Creates unusable files
- **Status:** NEVER DO THIS

## Validation Requirements

### Before Delivery:
- [ ] File opens in Google Earth Pro
- [ ] File size reasonable for data type
- [ ] Transparency working correctly
- [ ] Colors/styling match requirements
- [ ] No error messages or crashes

### File Size Guidelines:
- **Binary mask KMZ:** 10-50MB normal, 50-100MB maximum
- **RGBA GeoTIFF:** 300-500MB acceptable for national scale
- **Red flag:** Any file >3x expected size

## Prevention Measures

1. **Always test in Google Earth** before delivery
2. **Use simple formats** for maximum compatibility
3. **Validate file sizes** before batch processing
4. **Leverage QGIS** when it displays correctly
5. **Avoid complex automation** for simple tasks

---

*This guide consolidates all Google Earth compatibility knowledge. Reference this before any Google Earth export task.*
