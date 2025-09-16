# Pre-Flight Checklist - Visualization Export Tasks

## 🚨 MANDATORY CHECKS BEFORE STARTING

### 1. Pattern Recognition
- [ ] **Task type identified:** Binary mask, continuous data, or vector?
- [ ] **Similar task found:** Check `/01_KNOWLEDGE_CONTEXT/successful_pipelines/tested_workflows.yml`
- [ ] **Lessons learned reviewed:** Check relevant category in `/01_KNOWLEDGE_CONTEXT/lessons_learned/`
- [ ] **Method selected:** Based on pattern matching and proven workflows

### 2. File Size Estimation
- [ ] **Expected output size calculated:**
  - Binary mask KMZ: 10-50MB
  - Continuous data KMZ: 50-200MB
  - TIFF files: Varies by resolution and coverage
- [ ] **Red flag check:** If >200MB, propose alternative
- [ ] **Resolution appropriate:** Not oversampling unnecessarily

### 3. Method Validation
- [ ] **QGIS already correct?** → Use rendered export
- [ ] **Binary mask?** → Apply color mapping first
- [ ] **Continuous data?** → Use gdaldem color-relief
- [ ] **Complex task?** → Check for simpler alternative

### 4. Pre-Flight Testing Plan
- [ ] **Single file test:** Process ONE file completely first
- [ ] **Target application test:** Verify opens in Google Earth/QGIS
- [ ] **Size validation:** Confirm reasonable file size
- [ ] **Visual inspection:** Colors/styling match requirements

### 5. Red Flags to Watch For
- [ ] **Processing time >2 hours** for simple task
- [ ] **File size >10x expected**
- [ ] **Complex method** for simple problem
- [ ] **Ignoring QGIS** when it already displays correctly
- [ ] **No validation steps** planned

## ✅ READY TO PROCEED CRITERIA

**Only start batch processing when:**
- [ ] Single file test completed successfully
- [ ] File size validated (<200MB for KMZ)
- [ ] Target application test passed
- [ ] Visual appearance confirmed
- [ ] Method proven to work

## 🛑 STOP AND INVESTIGATE

**Immediately stop if:**
- File size >3x expected
- Processing time >2 hours for simple task
- Target application won't open file
- Visual appearance doesn't match requirements
- Any error messages during processing

## 📝 DOCUMENTATION REQUIREMENTS

**Before delivery:**
- [ ] All files <200MB
- [ ] All files open in target application
- [ ] Colors/styling match requirements
- [ ] Processing log created
- [ ] Success added to `/01_KNOWLEDGE_CONTEXT/successful_pipelines/tested_workflows.yml`

---
*This checklist prevents costly mistakes and ensures reliable delivery.*
