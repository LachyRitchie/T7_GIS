# Knowledge Base Index - Structured Reference
# Version: 4.0
# Last Updated: 2025-09-15
# Status: PRODUCTION READY

## Quick Access - Critical Production Methods

### 🚨 CRITICAL: Binary Mask Workflow
**Location:** `lessons_learned/by_category/visualization_exports/binary_mask_workflow_complete_v4.0.md`
**Status:** AUTHORITATIVE - Use this ONLY for all binary mask tasks
**Scope:** Complete workflow from GEE export to Google Earth visualization
**Key Solution:** ALWAYS use unmask(0) in GEE exports, load RGBA GeoTIFF directly in Google Earth

### ✅ Validated Production Workflows  
**Location:** `successful_pipelines/tested_workflows.yml`
**Status:** PRODUCTION READY
**Contains:** 4 validated workflows with success metrics and troubleshooting
- google_earth_binary_mask (qgis_rendered_export)
- carbon_yield_heatmap (gdaldem_color_relief)
- native_title_clipping (cookie_cutter_gdal_calc)
- raster_alignment (gdalwarp_with_tap)

### 📋 Critical Learning Summary
**Location:** `lessons_learned/CRITICAL_LEARNING_SUMMARY.md`
**Status:** MASTER REFERENCE
**Contents:** Frequent failures, successful patterns, red flags, banned methods

---

## Reference Documentation by ACCU Method

### Environmental Plantings (CURRENT - 2024)
**Location:** `reference_docs/EnvironmentalPlantings_2024_Active/`
**Key Files:**
- EP2024-Determination.pdf (Legal requirements)
- EP2024-FullCAM-Guidelines.pdf (Technical implementation)
- EP2024-Explanatory-Statement.pdf (Background and context)

### Plantation Forestry (CURRENT - 2022)  
**Location:** `reference_docs/PlantationForestry_2022_Active/`
**Key Files:**
- Plantation_Forestry_2022-FullCAM-Guidelines.pdf
- Plantation_Forestry_2022-Method-Guidance.pdf
- Financial assessment guidance.pdf

### Human Induced Regeneration (EXPIRED - 2013)
**Location:** `reference_docs/HumanInducedRegeneration_2013_EXPIRED/`
**Status:** REFERENCE ONLY - Method expired but content useful for context

### Soil Carbon (CURRENT - 2021)
**Location:** `reference_docs/SoilCarbon_2021_Active/`
**Focus:** Measurement-based soil carbon methodology

---

## FullCAM Documentation (Comprehensive)

### Consolidated Documentation (RECOMMENDED)
**Location:** `reference_docs/FullCAM/Consolidated/`
**Structure:** Organized by functional batches (Getting Started, Site Configuration, etc.)
**Versions:** Both 2016 and 2020 consolidated into thematic documents

### Individual Help Files (DETAILED REFERENCE)
**Location:** `reference_docs/FullCAM/FullCAM.exe_2016/` and `reference_docs/FullCAM/FullCAM.exe_2020/`
**Contents:** Individual help files for specific functions (280+ files each)
**Use Case:** Detailed reference for specific FullCAM functions

---

## Lessons Learned (Version 4.0 Structure)

### By Category Organization
**Location:** `lessons_learned/by_category/`

#### Visualization Exports
- **binary_mask_workflow_complete_v4.0.md** (AUTHORITATIVE)
- google_earth_compatibility_issues.md
- validation_rules.md
- ARCHIVED_v3/ (Superseded documents)

### Session Reviews (Historical Context)
**Location:** `lessons_learned/session_reviews/`
- 2025-09-08_session_review_binary_mask_pipeline.md
- 2025-09-09_state_geotiff_creation_success.md

### Technical References
- gee_python_api_syntax_errors_2025-01-23.md (GEE Python patterns)

---

## Permanently Banned Methods 🚫

### KMLSUPEROVERLAY for Binary Masks
**Reason:** Incompatible with Google Earth Pro/Web
**Creates:** 480MB+ unusable files
**Status:** PERMANENTLY BANNED

### Direct Binary Mask to KMZ (without RGBA)
**Reason:** Bypasses proper color mapping
**Creates:** Massive files Google Earth can't open
**Status:** PERMANENTLY BANNED

### Downsampling Production Deliverables
**Reason:** Loses critical detail for client analysis
**Quality:** Professionally unacceptable
**Status:** NOT VIABLE FOR PRODUCTION

---

## Search Strategy (Priority Order)

1. **CRITICAL_LEARNING_SUMMARY.md** - Check first for all tasks
2. **binary_mask_workflow_complete_v4.0.md** - Authoritative for binary masks  
3. **tested_workflows.yml** - Validated production methods
4. **Current ACCU method docs** - EP2024, PF2022, etc.
5. **FullCAM Consolidated** - Thematic FullCAM guidance
6. **Individual FullCAM files** - Specific function details

---

## File Size and Practicality Guidelines

### Client Delivery Limits
- **Total deliverable:** <2GB (practical download limit)
- **Single file:** <500MB (recommended)
- **KMZ files:** <200MB (red flag if larger)

### Processing Time Thresholds  
- **GUI tasks:** <5 minutes
- **Engineer handover:** >5 minutes OR >100MB OR >5 files
- **Abort processing:** >4 hours (find alternative approach)

### Quality Validation
- **Binary masks:** 1-500MB depending on scale
- **Continuous rasters:** 50-200MB typical
- **File size red flags:** 10x larger OR 90% smaller than expected

---

## Version Control and Status

### Current Production Version: 4.0
- **Binary mask methodology:** v4.0 (consolidated authoritative guide)
- **Critical learning summary:** v4.0 (updated patterns and rules)
- **Knowledge structure:** Reorganized 2025-09-15
- **All v1-v3 binary mask docs:** ARCHIVED (superseded)

### Migration Notes
- **Old path:** /08_KNOWLEDGE BASE/ (deprecated)
- **New path:** /01_KNOWLEDGE_CONTEXT/ (current)
- **Migration date:** 2025-09-15
- **All content:** Reorganized and consolidated

---

## Emergency Quick Reference

### "My binary mask exports are 80KB instead of expected MB"
→ Use unmask(0) in GEE export - See binary_mask_workflow_complete_v4.0.md

### "Google Earth won't open my KMZ file"
→ Check file size >200MB = red flag. Use RGBA GeoTIFF directly instead

### "Client can't download 5GB of outputs"  
→ Violates practicality guidelines. Find alternative approach first

### "Processing taking 8+ hours"
→ Wrong methodology. Check CRITICAL_LEARNING_SUMMARY.md for simpler approach

### "Need current ACCU method guidance"
→ EP2024 or PF2022 in reference_docs (NOT expired HIR2013)

---

*This index represents the complete knowledge base as of 2025-09-15. All content has been reorganized for maximum accessibility and production readiness.*