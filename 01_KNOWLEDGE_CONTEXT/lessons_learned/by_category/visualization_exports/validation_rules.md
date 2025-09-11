# GIS Engineer Validation Rules - Visualization Exports

## MANDATORY OUTPUT VALIDATION
Before delivering any visualization products:

### File Size Validation
- **KMZ files:** 10-100MB normal, NEVER >200MB
- **TIFF files:** Check against expected size for resolution/coverage
- **If output is >3x expected size:** STOP and investigate immediately

### Binary Mask Specific Checks
- **Must have RGBA channels:** Verify 4-band output after color mapping
- **Color mapping applied:** Check that 0/1 values became transparent/white
- **Test in target application:** Always test ONE file before batch processing

### Pre-Flight Testing Requirements
1. **Single file test:** Process one file completely before batch operations
2. **Application verification:** Open test file in target application (Google Earth, QGIS, etc.)
3. **Size validation:** Confirm file size is reasonable for data type
4. **Visual inspection:** Verify colors/styling match expectations

## Binary Mask Visualization Pipeline

### CORRECT Workflow for Binary Masks → Google Earth:
```
1. Binary Mask (0/1 values)
2. Apply color map: 0→transparent, 1→white
3. Verify RGBA output (4 bands)
4. Convert to KMZ
5. Test in Google Earth
6. Batch process remaining files
```

### WRONG Workflow (What Caused Failure):
```
1. Binary Mask (0/1 values)
2. Direct KMZ conversion ❌
3. Result: 480MB unusable file
```

## When QGIS Already Displays Correctly

### Use QGIS Rendered Export:
1. **QGIS displays correctly** → Use "Export as Rendered Image"
2. **Simple conversion** → gdal_translate to KMZ
3. **Don't recreate** → Don't rebuild styling from scratch

### Expected File Sizes by Scale:
- **National scale:** ~50MB KMZ
- **State scale:** ~10-20MB KMZ  
- **Regional scale:** ~5-10MB KMZ
- **Property scale:** ~1-5MB KMZ

## Red Flags to Watch For

### File Size Red Flags:
- KMZ >200MB for binary masks
- TIFF >500MB for 25m resolution
- Any file >3x expected size

### Processing Red Flags:
- No intermediate validation steps
- Batch processing without single-file test
- Complex workflows for simple tasks
- Ignoring existing QGIS styling

## Quality Gates

### Before Starting Batch Processing:
- [ ] Single file test completed
- [ ] File size validated
- [ ] Target application test passed
- [ ] Visual inspection completed

### Before Delivery:
- [ ] All files <200MB
- [ ] All files open in target application
- [ ] Colors/styling match requirements
- [ ] Documentation complete

---
*These validation rules prevent costly mistakes and ensure reliable delivery of visualization products.*
