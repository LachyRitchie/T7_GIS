# Lessons Learned - Organization Guide

## Structure Overview

This directory is organized to provide efficient context loading and clear knowledge management:

```
lessons_learned/
├── by_category/                    # Categorized technical lessons
│   ├── visualization_exports/     # Google Earth, KMZ, binary masks
│   ├── data_processing/           # Raster/vector processing
│   └── [other categories...]      # Future categories
├── session_reviews/               # High-level session summaries
└── README.md                      # This file
```

## How to Use This Structure

### For Technical Implementation
- **Check `by_category/`** for specific technical guidance
- **Each category contains consolidated, comprehensive guides**
- **No duplicate information across files**

### For Session Context
- **Check `session_reviews/`** for high-level summaries
- **Use for understanding overall project context**
- **Reference specific technical files for implementation details**

## Key Files

### Visualization Exports
- **`binary_mask_visualization_complete.md`** - Complete guide for binary mask visualization
- **`google_earth_compatibility_issues.md`** - Google Earth compatibility problems and solutions
- **`validation_rules.md`** - File size and quality validation requirements

### Session Reviews
- **`2025-09-08_session_review_binary_mask_pipeline.md`** - Complete session summary

## Context Loading Strategy

1. **Start with category-specific files** for technical tasks
2. **Reference session reviews** for project context
3. **Cross-reference between files** when needed
4. **Update consolidated files** rather than creating new scattered files

## Maintenance Rules

1. **Consolidate related information** into single comprehensive files
2. **Keep categories focused** on specific technical areas
3. **Update existing files** rather than creating duplicates
4. **Move session summaries** to `session_reviews/` directory
5. **Remove duplicate files** immediately

## Benefits of This Organization

- **Efficient context loading** - One file per topic
- **No duplicate information** - Single source of truth
- **Clear categorization** - Easy to find relevant content
- **Comprehensive coverage** - All related info in one place
- **Easy maintenance** - Update one file instead of many

---

*This organization prevents the confusion of scattered, duplicate files and ensures efficient knowledge retrieval.*
