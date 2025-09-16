# GEE Python API Syntax Errors and Debugging
**Date:** 2025-01-23  
**Context:** Mary Springs woody mask processing  
**Issue:** 89KB file exports instead of expected 50-200MB  

## Problem Summary
During Mary Springs woody vegetation mask processing, exports were completing successfully but producing tiny 89KB files instead of the expected 50-200MB files for a 9,752 hectare property at 10m resolution.

## Root Causes Identified

### 1. Boolean Operator Syntax Error
**Issue:** Incorrect use of `.And()` operator without proper parentheses
```python
# WRONG - causes syntax error or unexpected behavior
woody_conservative = woody_score.gt(0.15).And(ndvi_max.gt(0.25)).rename('woody')

# CORRECT - requires parentheses for complex operations
woody_conservative = (woody_score.gt(0.15).And(ndvi_max.gt(0.25))).rename('woody')
```

### 2. GEE Python API Specifics
- Use `.And()` not `.and()` for Earth Engine boolean operations
- Always wrap complex boolean logic in parentheses
- Python `and` operator doesn't work with Earth Engine objects

### 3. Export Validation Issues
- Small file sizes (89KB) indicate empty or nearly empty exports
- Need to verify actual pixel counts before export
- Check binary values are 0/1 only

## Debugging Process

### Step 1: Geometry Validation
```python
# Check boundary area
area = boundary.area().getInfo()
print(f"Boundary area: {area/10000:.2f} hectares")

# Verify geometry bounds
bounds = boundary.bounds().getInfo()
print(f"Bounds: {bounds}")
```

### Step 2: Imagery Validation
```python
# Check image count
count = s2.size().getInfo()
print(f"Sentinel-2 images: {count}")

# Verify pixel counts
pixel_count = clipped.reduceRegion(
    reducer=ee.Reducer.count(),
    geometry=boundary,
    scale=10,
    maxPixels=1e10
).getInfo()
print(f"Total pixels: {pixel_count}")
```

### Step 3: Content Validation
```python
# Sample values to check binary nature
sample = clipped.sample(region=boundary, scale=10, numPixels=20)
sample_values = sample.aggregate_array('woody').getInfo()
unique_values = list(set(sample_values))
print(f"Unique values: {unique_values}")  # Should be [0, 1]
```

### Step 4: Test Export
```python
# Create simple test image first
test_image = ee.Image.constant(1).clip(boundary).byte()
# Export and check file size
```

## Prevention Strategies

### 1. Always Test Small First
- Create debug exports before full processing
- Verify file sizes match expectations
- Check pixel counts and content

### 2. Syntax Validation
- Use parentheses for all complex boolean operations
- Test boolean logic separately before combining
- Verify `.And()` vs `.and()` usage

### 3. Export Monitoring
```python
# Monitor export status
while task.status()['state'] in ['READY', 'RUNNING']:
    status = task.status()
    print(f"Status: {status['state']}")
    time.sleep(30)

# Check final status
final_status = task.status()
if final_status['state'] == 'COMPLETED':
    print("✅ Export completed")
else:
    print(f"❌ Export failed: {final_status.get('error_message')}")
```

## Key Lessons

1. **Syntax Matters**: GEE Python API has specific syntax requirements
2. **Test Small**: Always validate with small exports first
3. **Monitor Content**: Check pixel counts and values before export
4. **Debug Systematically**: Geometry → Imagery → Content → Export
5. **File Size Validation**: Expected size = (area_hectares / 0.01) * bytes_per_pixel

## Expected File Sizes
- **10m resolution**: ~100 pixels per hectare
- **9,752 hectares**: ~975,200 pixels
- **Binary data**: 1 byte per pixel
- **Expected size**: ~1MB + overhead = 50-200MB

## Related Files
- `debug_gee_issues.py` - Comprehensive debugging script
- `debug_export_content.py` - Content validation script
- `check_export_status.py` - Export monitoring script

---
**Status:** Resolved  
**Impact:** High - prevents wasted processing time and incorrect outputs  
**Next Time:** Always run debug scripts before full exports
