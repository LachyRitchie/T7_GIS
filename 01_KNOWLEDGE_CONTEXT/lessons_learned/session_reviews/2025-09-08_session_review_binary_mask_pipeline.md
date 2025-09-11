# Binary Mask → Google Earth Pipeline - Session Review
**Date:** 2025-09-08  
**Session Type:** Full Day Problem-Solving  
**Outcome:** Successful resolution with clear production path established

## Executive Summary

After 8+ hours of failed attempts, we successfully identified the correct approach for binary mask visualization in Google Earth. The solution is surprisingly simple: **use the full-resolution RGBA GeoTIFFs directly** rather than converting to KMZ.

## What We Tried

### 1. Initial Mask2 Pipeline Attempts
- **Script:** `mask2kmz.sh` with GDAL-based workflow
- **Steps:** Create alpha band → Build RGBA VRT → Set color interpretation → Export to KMZ
- **Goal:** Lightweight KMZs with transparency preserved
- **Result:** Technical success but impractical for production

### 2. Direct KMZ Conversion Attempts
- **KML Driver:** `-of KML` → Failed (no raster capabilities)
- **KMLSUPEROVERLAY:** `-of KMLSUPEROVERLAY` → Produced 480MB+ files, hours of processing
- **Google Earth:** Silent failures or crashes when opening files
- **Lesson:** KMLSUPEROVERLAY is fundamentally incompatible with modern Google Earth

### 3. Simplified GDAL Approaches
- **Method:** Scale binary to PNG + manual KML wrapper
- **Result:** Small files (83-255KB) that opened in Google Earth
- **Problem:** Brutal downsampling to 2048x2048 made results unusable for client work
- **Lesson:** Simple PNG export sacrifices too much detail for production use

### 4. Cursor's "Runaway" Automation
- **Issue:** Cursor kept reintroducing banned methods (KMLSUPEROVERLAY)
- **Problem:** Lack of strict guardrails led to repeated failures
- **Lesson:** Need tighter memory/rules to prevent fallback to known bad approaches

## What Didn't Work (and Why)

### ❌ KMLSUPEROVERLAY Approach
- **Problem:** Creates massive tiled outputs (480MB+)
- **Issue:** Incompatible with Google Earth Pro/Web
- **Result:** Hours of processing for unusable files
- **Status:** BANNED for binary masks

### ❌ Downsampled PNG + KMZ
- **Problem:** Resolution cap (~2048x2048) loses critical detail
- **Issue:** Unacceptable for national-scale client deliverables
- **Result:** Technically works but professionally unusable
- **Status:** Not viable for production

### ❌ Blind GDAL Scripting
- **Problem:** Led to wasted hours and inconsistent results
- **Issue:** Ignored existing QGIS solutions
- **Result:** Reinforced need for validation and testing
- **Status:** Requires better guardrails

## Where We Landed

### ✅ **Primary Solution: Full-Resolution RGBA GeoTIFFs**

**Files:** `PRODUCTS/*v3.4.tif` (all 6 binary mask layers)

**QA Results:**
- **CRS:** EPSG:4326 (WGS84) ✅
- **Structure:** RGBA with alpha transparency (Band 4) ✅
- **File Sizes:** 300-500MB (all <1GB) ✅
- **Dimensions:** ~162k × 139k pixels (consistent national scale) ✅
- **Status:** Production-ready, no corrections needed ✅

**Workflow:**
1. Load GeoTIFF directly in Google Earth Pro
2. Google Earth builds its own superoverlay internally
3. Result: Responsive, visually correct, full-resolution display

### ✅ **Backup Solution: Mask2 Pipeline**

**Script:** `mask2kmz.sh` (preserved and functional)

**Use Cases:**
- Lightweight KMZs for email/demo purposes
- When client explicitly requests KMZ format
- Low-resolution sharing scenarios

**Limitations:**
- Adds unnecessary complexity for production
- Either reduces resolution or bloats file sizes
- Less stable than direct GeoTIFF use

## Key Lessons Learned

### 1. **KMLSUPEROVERLAY is Forbidden**
- Always creates oversized, unstable outputs
- Incompatible with modern Google Earth
- Never use for binary mask visualization

### 2. **Simple PNG Scaling is Insufficient**
- Resolution caps make results unusable for client work
- Not viable for high-resolution deliverables
- Avoid for production binary mask exports

### 3. **RGBA GeoTIFFs are Gold Standard**
- Direct use in Google Earth is preferred approach
- Full resolution preserved
- Stable, responsive performance

### 4. **Use QGIS When It Works**
- If QGIS displays correctly → use that representation
- Don't try to rebuild with GDAL
- Leverage existing rendering solutions

### 5. **Cursor Needs Tighter Guardrails**
- Prevent drift into banned methods during "optimization"
- Enforce strict memory of failed approaches
- Require validation before batch processing

### 6. **Mask2 Pipeline is Niche Tool**
- Valid but not default approach
- Keep as secondary option only
- Don't overcomplicate simple tasks

### 7. **v3.4 Files are Production-Ready**
- All six masks pass QA validation
- No v3.5 corrections needed
- Ready for immediate client delivery

## System Prompt Updates Required

### 1. **Reinforce "No KMLSUPEROVERLAY" Rule**
- Add explicit ban for binary mask visualization
- Include file size warnings (>200MB = red flag)
- Require pre-flight testing for batch operations

### 2. **Prioritize RGBA GeoTIFF Direct Use**
- Make this the default approach for Google Earth
- Document the drag-and-drop workflow
- Emphasize stability and performance benefits

### 3. **Treat Mask2 Pipeline as Optional Fallback**
- Not default approach for production
- Only for specific use cases (lightweight sharing)
- Requires explicit justification for use

### 4. **Add Validation Requirements**
- File size checks before delivery
- Single-file testing before batch processing
- Visual verification in target application

## Final Decision

**Primary Delivery Path:** Use v3.4 full-resolution RGBA GeoTIFFs directly in Google Earth Pro

**Backup Path:** Mask2 → KMZ pipeline (for lightweight sharing only)

**Status:** Problem solved, production-ready solution established

---

*This session review should be referenced before any binary mask visualization task to prevent repetition of the 8-hour failure and ensure use of the correct approach.*
