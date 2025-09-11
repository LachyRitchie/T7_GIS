#!/bin/bash
# Weekly Memory Consolidation Script
# Consolidates lessons into patterns and updates critical summary

cd "/Volumes/T7 Shield/01_CONTEXT/lessons_learned/"

echo "# Critical Patterns (Updated $(date))" > CRITICAL_LEARNING_SUMMARY.md
echo "" >> CRITICAL_LEARNING_SUMMARY.md

echo "## Frequent Failures" >> CRITICAL_LEARNING_SUMMARY.md
echo "Based on analysis of lessons learned:" >> CRITICAL_LEARNING_SUMMARY.md
echo "" >> CRITICAL_LEARNING_SUMMARY.md

# Extract common problems
grep -h "problem:" by_category/*/*.md 2>/dev/null | sort | uniq -c | sort -rn >> CRITICAL_LEARNING_SUMMARY.md

echo "" >> CRITICAL_LEARNING_SUMMARY.md
echo "## Successful Patterns" >> CRITICAL_LEARNING_SUMMARY.md
echo "From tested_workflows.yml:" >> CRITICAL_LEARNING_SUMMARY.md
echo "" >> CRITICAL_LEARNING_SUMMARY.md

# Extract successful methods
grep -h "method:" ../successful_pipelines/tested_workflows.yml >> CRITICAL_LEARNING_SUMMARY.md

echo "" >> CRITICAL_LEARNING_SUMMARY.md
echo "## Red Flags to Watch For" >> CRITICAL_LEARNING_SUMMARY.md
echo "" >> CRITICAL_LEARNING_SUMMARY.md
echo "- File sizes >10x expected" >> CRITICAL_LEARNING_SUMMARY.md
echo "- Processing time >2 hours for simple tasks" >> CRITICAL_LEARNING_SUMMARY.md
echo "- Complex methods for simple problems" >> CRITICAL_LEARNING_SUMMARY.md
echo "- Ignoring QGIS when it already displays correctly" >> CRITICAL_LEARNING_SUMMARY.md

echo "" >> CRITICAL_LEARNING_SUMMARY.md
echo "## Quick Reference" >> CRITICAL_LEARNING_SUMMARY.md
echo "" >> CRITICAL_LEARNING_SUMMARY.md
echo "### Binary Masks → Google Earth" >> CRITICAL_LEARNING_SUMMARY.md
echo "1. Use QGIS rendered export" >> CRITICAL_LEARNING_SUMMARY.md
echo "2. gdal_translate to KMZ" >> CRITICAL_LEARNING_SUMMARY.md
echo "3. Expected size: 10-50MB" >> CRITICAL_LEARNING_SUMMARY.md
echo "" >> CRITICAL_LEARNING_SUMMARY.md
echo "### Continuous Data → Google Earth" >> CRITICAL_LEARNING_SUMMARY.md
echo "1. gdaldem color-relief with color map" >> CRITICAL_LEARNING_SUMMARY.md
echo "2. Verify 4-band RGBA output" >> CRITICAL_LEARNING_SUMMARY.md
echo "3. gdal_translate to KMZ" >> CRITICAL_LEARNING_SUMMARY.md
echo "4. Expected size: 50-200MB" >> CRITICAL_LEARNING_SUMMARY.md

echo "Memory consolidation completed: $(date)"
