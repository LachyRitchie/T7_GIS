#!/bin/bash
# Test script to validate END_OF_PROJECT_PROTOCOL.md commands
# Run this to ensure all commands in the protocol work correctly

echo "======================================"
echo "END-OF-PROJECT PROTOCOL TEST"
echo "======================================"
echo ""

# Test 1: Check for forbidden suffixes
echo "TEST 1: Checking for forbidden suffixes..."
find /Volumes/T7\ Shield/04_DATA_PROJECTS -type f \( -name "*_FIXED*" -o -name "*_temp*" -o -name "*_aligned*" \) 2>/dev/null | head -5
echo "✓ Test 1 complete"
echo ""

# Test 2: Check RECIPE template exists
echo "TEST 2: Verifying RECIPE template..."
if [ -f "/Volumes/T7 Shield/01_SYSTEM/RECIPE_TEMPLATE.yml" ]; then
    echo "✓ RECIPE template found"
else
    echo "✗ RECIPE template missing!"
fi
echo ""

# Test 3: Check CURRENT_VERSIONS.yml exists
echo "TEST 3: Verifying CURRENT_VERSIONS.yml..."
if [ -f "/Volumes/T7 Shield/03_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml" ]; then
    echo "✓ CURRENT_VERSIONS.yml found"
    echo "Last 5 lines:"
    tail -5 "/Volumes/T7 Shield/03_BASE_DATA/CURRENT/CURRENT_VERSIONS.yml"
else
    echo "✗ CURRENT_VERSIONS.yml missing!"
fi
echo ""

# Test 4: Check Git repository
echo "TEST 4: Checking Git repository..."
cd /Volumes/T7\ Shield/
if git status &>/dev/null; then
    echo "✓ Git repository found"
    git remote -v | head -1
else
    echo "✗ No Git repository"
fi
echo ""

# Test 5: Find large files
echo "TEST 5: Finding files >1GB..."
echo "Checking 04_DATA_PROJECTS for large files..."
find /Volumes/T7\ Shield/04_DATA_PROJECTS -type f -size +1G 2>/dev/null | wc -l | xargs -I {} echo "{} files found >1GB"
echo ""

echo "======================================"
echo "PROTOCOL TEST COMPLETE"
echo "======================================"
echo ""
echo "If all tests passed, the protocol is ready to use."
echo "Run with: bash /Volumes/T7 Shield/01_SYSTEM/END_OF_PROJECT_PROTOCOL.md"
