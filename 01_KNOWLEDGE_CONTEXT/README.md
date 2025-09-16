# Knowledge Context - Complete Reference System
**Version:** 4.0  
**Last Updated:** 2025-09-15  
**Status:** PRODUCTION READY

## Overview

This directory contains the complete knowledge base for GIS and FullCAM work, organized for maximum efficiency and compliance with ACCU Scheme requirements.

## Quick Start

### 🚨 For Any Task - Check This First
**File:** `lessons_learned/CRITICAL_LEARNING_SUMMARY.md`
**Contains:** Most frequent failures, proven methods, red flags to avoid

### 📊 Binary Mask Work (Most Common Issue)
**File:** `lessons_learned/by_category/visualization_exports/binary_mask_workflow_complete_v4.0.md`
**Status:** AUTHORITATIVE - This is the ONLY guide to use for binary mask tasks
**Solves:** GEE export issues (80KB problem) + Google Earth visualization

### ✅ Production-Ready Workflows
**File:** `successful_pipelines/tested_workflows.yml`
**Contains:** 4 validated workflows with success metrics and troubleshooting

## Directory Structure

```
01_KNOWLEDGE_CONTEXT/
├── knowledge_index/          # Master index and search system
│   ├── knowledge_base_index.md   # Structured reference (START HERE)
│   └── manifest.json            # Current version and metadata
├── lessons_learned/          # Critical operational knowledge
│   ├── CRITICAL_LEARNING_SUMMARY.md  # Master summary (CHECK FIRST)
│   ├── by_category/
│   │   └── visualization_exports/
│   │       ├── binary_mask_workflow_complete_v4.0.md  # AUTHORITATIVE
│   │       ├── google_earth_compatibility_issues.md
│   │       ├── validation_rules.md
│   │       └── ARCHIVED_v3/      # Superseded documents
│   └── session_reviews/         # Historical context
├── reference_docs/           # Official ACCU and technical documentation
│   ├── EnvironmentalPlantings_2024_Active/  # Current EP method
│   ├── PlantationForestry_2022_Active/      # Current PF method  
│   ├── SoilCarbon_2021_Active/              # Current SC method
│   ├── HumanInducedRegeneration_2013_EXPIRED/  # Reference only
│   ├── FullCAM/                             # Comprehensive FullCAM docs
│   ├── General_CER_Guidance/               # CER guidance documents
│   └── General_Overarching_Policy/         # Policy and legislation
└── successful_pipelines/     # Validated production workflows
    └── tested_workflows.yml     # Production-ready methods
```

## Usage Guidelines

### Decision Framework
1. **Any task:** Check `CRITICAL_LEARNING_SUMMARY.md` first
2. **Binary masks:** Use `binary_mask_workflow_complete_v4.0.md` (ONLY authoritative source)
3. **Production work:** Reference `tested_workflows.yml` for validated approaches  
4. **ACCU compliance:** Use appropriate active method documentation
5. **FullCAM technical:** Start with `FullCAM/Consolidated/` for thematic guidance

### Search Priority Order
1. Critical Learning Summary (most important patterns)
2. Binary Mask Workflow v4.0 (most common technical issue)
3. Tested Workflows (validated production methods)
4. Current ACCU method docs (compliance requirements)
5. FullCAM documentation (technical implementation)

## Version 4.0 Improvements

### Content Consolidation
- **Binary mask docs:** 4 overlapping documents → 1 authoritative guide
- **Knowledge structure:** Reorganized for practical accessibility
- **Obsolete content:** Properly archived with clear supersession notes

### Production Focus
- **Critical patterns:** Extracted from 8+ months of lessons learned
- **Validated workflows:** Only production-ready methods included
- **Red flags:** Clear warnings about methods that waste time
- **Banned methods:** Permanently prohibited approaches documented

### Compliance Structure
- **Active methods only:** Current EP2024, PF2022, SC2021 prioritized
- **Expired methods:** Clearly marked as reference-only
- **Version control:** All content properly versioned and dated

## Critical Rules (Never Violate)

### Permanently Banned Methods
1. **KMLSUPEROVERLAY for binary masks** - Creates 480MB+ unusable files
2. **Direct binary mask to KMZ** - Bypasses proper color mapping  
3. **Downsampling production deliverables** - Loses critical detail

### Production Standards
1. **Binary masks:** ALWAYS use unmask(0) in GEE exports
2. **Google Earth:** Use RGBA GeoTIFF directly (primary method)
3. **File sizes:** <2GB total deliverable, <500MB single file
4. **Processing time:** >4 hours = wrong approach, find alternative

### Quality Gates
1. **Client practicality:** Verify they can download and use outputs
2. **File size validation:** 10x larger OR 90% smaller = error
3. **Method verification:** Cross-check with ACCU compliance
4. **Test first:** Always validate with single file before batch processing

## Emergency Quick Reference

| Problem | Solution Location | Key Action |
|---------|------------------|------------|
| 80KB GEE exports | binary_mask_workflow_v4.0.md | Use unmask(0) |
| Google Earth won't open KMZ | CRITICAL_LEARNING_SUMMARY.md | Check file size >200MB |
| Client can't download outputs | Decision Framework | Violates practicality rules |
| 8+ hour processing | CRITICAL_LEARNING_SUMMARY.md | Wrong methodology |
| ACCU compliance question | reference_docs/[Method]_Active/ | Use current methods only |

## Content Statistics

- **Total documents:** 89 (45 markdown, 35 PDF, 9 other)
- **Active ACCU methods:** 4 (EP2024, PF2022, SC2021, plus general guidance)
- **Lessons learned:** 8 documents (4 archived as superseded)
- **Production workflows:** 4 validated methods
- **FullCAM coverage:** Complete 2016 and 2020 documentation

## Maintenance

### When to Update
- **After major project completion:** Add lessons learned
- **Method changes:** Update ACCU method documentation
- **Tool discovery:** Add successful new workflows
- **Failure patterns:** Update critical learning summary

### Update Process
1. Add new content to appropriate category
2. Update CRITICAL_LEARNING_SUMMARY.md if patterns change
3. Archive superseded content with clear notes
4. Update manifest.json with new timestamp
5. Maintain version numbering for major changes

---

## Support

For questions about this knowledge base structure or content:
1. Check the master index: `knowledge_index/knowledge_base_index.md`
2. Review decision framework in system prompt (Section 2)
3. Search for existing solutions before creating new approaches

---

*This knowledge base represents 8+ months of practical GIS and FullCAM experience, organized for maximum efficiency and compliance. Version 4.0 eliminates organizational debt and focuses on production-ready methods.*