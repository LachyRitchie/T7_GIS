# Shared Execution Matrix
**Version:** 1.0  
**Used by:** Both GIS Strategist and GIS Engineer  
**Purpose:** Determine when Engineer executes vs. returns to Strategist

---

## 🚦 DECISION MATRIX

### Core Rule: If ANY threshold is exceeded → Return to Strategist

| Criterion | Engineer Executes | Return to Strategist | Notes |
|-----------|------------------|---------------------|-------|
| **File size** | < 100 MB | ≥ 100 MB | Per file |
| **Processing time** | < 5 min | ≥ 5 min | Estimated |
| **Number of files** | < 5 | ≥ 5 | In batch |
| **Total output** | < 500 MB | ≥ 500 MB | All files combined |
| **Script runtime** | < 30 min | ≥ 30 min | Needs approval |
| **Batch processing** | No | Yes | Multiple datasets |
| **Complex calculation** | No | Yes | Multi-step analysis |
| **Confidence level** | High | Any uncertainty | When in doubt, ask |

---

## 📊 DETAILED THRESHOLDS

### File Size Thresholds
```
Single file:
✅ < 100 MB    → Engineer proceeds
⚠️ 100-500 MB  → Check approach first
❌ > 500 MB    → Return to Strategist

Total output:
✅ < 500 MB    → Engineer proceeds
⚠️ 500MB-1GB   → Need approval
❌ > 1 GB      → Return to Strategist
```

### Time Thresholds
```
Quick tasks:
✅ < 5 min     → Engineer proceeds
⚠️ 5-30 min    → Document approach
❌ > 30 min    → Need approval first

Scripts:
✅ < 30 min    → Can execute
⚠️ 30-60 min   → Need explicit approval
❌ > 60 min    → Requires detailed plan
```

### Complexity Thresholds
```
Simple:
✅ Single command        → Execute
✅ Tested pattern       → Execute
✅ <5 files            → Execute

Complex:
❌ Multi-step pipeline  → Plan first
❌ Untested approach   → Verify first
❌ Batch processing    → Get approval
```

---

## 🔄 HANDBACK PROTOCOL

### When to Return to Strategist

**IMMEDIATE RETURN if:**
- Output will exceed 1GB
- Processing will take >1 hour
- Approach is unclear
- Previous attempt failed
- Client requirements ambiguous

### How to Return
```markdown
## RETURNING TO STRATEGIST
**Reason:** [Exceeded file size threshold / Processing time / Uncertainty]
**Current status:** [What's completed]
**Blocked by:** [Specific issue]
**Estimated:** [Size/time if proceeding]
**Options:** 
1. [Alternative approach]
2. [Different method]
3. [Reduced scope]
```

---

## ✅ PROCEEDING PROTOCOL

### When Engineer Can Proceed

**PROCEED if ALL true:**
- [ ] Output < 100MB per file
- [ ] Total < 500MB
- [ ] Runtime < 5 min
- [ ] Pattern is tested
- [ ] Approach is clear
- [ ] Single dataset or <5 files

### Pre-Execution Checklist
```python
def can_proceed(task):
    if task.output_size > 100:  # MB
        return False, "File too large"
    if task.runtime > 5:  # minutes
        return False, "Too long"
    if task.file_count > 5:
        return False, "Too many files"
    if not task.pattern_tested:
        return False, "Untested approach"
    return True, "Proceed"
```

---

## 🚨 APPROVAL REQUIREMENTS

### Long-Running Scripts (>30 min)

**MUST provide:**
1. Complete script draft
2. Expected runtime estimate
3. Resource requirements (CPU/RAM/Disk)
4. Output size estimate
5. Test results from sample

**Approval format:**
```markdown
## SCRIPT APPROVAL REQUEST
**Script purpose:** [What it does]
**Estimated runtime:** [X hours]
**Input data:** [Size and count]
**Output size:** [Expected GB]
**Resources needed:** [CPU/RAM/Disk]
**Test results:** [Sample output]
**Script:** [Full code]
```

---

## 📈 ESCALATION TRIGGERS

### Automatic Escalation
These ALWAYS require Strategist involvement:
- 🔴 Any FullCAM preparation
- 🔴 ACCU compliance decisions
- 🔴 Client deliverables
- 🔴 Method selection
- 🔴 Error recovery after failure

### Progressive Escalation
Start with Engineer, escalate if needed:
1. Try standard approach
2. If blocked → Try alternative
3. If still blocked → Return to Strategist
4. Document what was tried

---

## 🎯 QUICK DECISION TREE

```
Is output >100MB?
├─ YES → Return to Strategist
└─ NO → Continue
    │
    Will it take >5min?
    ├─ YES → Get approval
    └─ NO → Continue
        │
        Is it >5 files?
        ├─ YES → Check total size
        │   ├─ >500MB → Return
        │   └─ <500MB → Proceed carefully
        └─ NO → Continue
            │
            Am I confident?
            ├─ NO → Ask Strategist
            └─ YES → PROCEED
```

---

## 📋 EXAMPLES

### Example 1: Single State Extraction
- Input: National dataset (2GB)
- Output: State subset (~80MB)
- Time: ~3 minutes
- **Decision:** ✅ Engineer proceeds

### Example 2: Batch Processing 10 Farms
- Input: 10 farm boundaries
- Output: 10 masked rasters
- Time: ~45 minutes total
- **Decision:** ❌ Return to Strategist

### Example 3: Create Binary Mask
- Input: 1 raster (500MB)
- Output: 1 mask (100MB)
- Time: ~4 minutes
- **Decision:** ✅ Engineer proceeds (just under threshold)

### Example 4: Mosaic 50 Tiles
- Input: 50 tiles × 100MB
- Output: 1 mosaic (5GB)
- Time: ~2 hours
- **Decision:** ❌ Return to Strategist immediately

---

**Remember:** When in doubt, ASK. It's better to check than to waste time on the wrong approach.