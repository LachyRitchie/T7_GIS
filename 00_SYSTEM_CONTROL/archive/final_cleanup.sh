#!/bin/bash
# Final cleanup script for T7 Shield restructure
# Date: 2025-01-21

echo "Cleaning up remaining empty folders..."

# Remove empty 08_TOOLS if it exists
if [ -d "/Volumes/T7 Shield/08_TOOLS/_DRIVE_TOOLS" ]; then
    rmdir "/Volumes/T7 Shield/08_TOOLS/_DRIVE_TOOLS" 2>/dev/null
    echo "Removed empty _DRIVE_TOOLS subfolder"
fi

if [ -d "/Volumes/T7 Shield/08_TOOLS" ]; then
    rmdir "/Volumes/T7 Shield/08_TOOLS" 2>/dev/null
    echo "Removed empty 08_TOOLS folder"
fi

echo "Cleanup complete!"
echo ""
echo "Final structure:"
echo "- 00_SYSTEM_CONTROL (system & setup)"
echo "- 01_KNOWLEDGE_CONTEXT (knowledge & learning)"
echo "- 02_BASE_DATA (source data)"
echo "- 03_DATA_PROJECTS (active projects)"
echo "- 04_FARM_ASSESSMENT (farms)"
echo "- 05_TEMPLATES_LAYOUTS (templates)"
echo "- 09_ARCHIVE (old materials)"
