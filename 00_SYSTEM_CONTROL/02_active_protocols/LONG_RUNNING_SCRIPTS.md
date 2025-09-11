# Long-Running Script Approval Process

## CRITICAL REQUIREMENT
**ALL long-running data processing scripts MUST be approved by the GIS strategist before execution.**

## Definition of "Long-Running Script"
Any script that meets ONE or more of these criteria:
- Expected runtime >30 minutes
- Processes >1GB of data
- Generates >100MB of output files
- Uses significant system resources (CPU, memory, disk)
- Creates multiple large files or directories
- Involves batch processing of multiple datasets

## Approval Process

### Step 1: Script Preparation
Before requesting approval, prepare:
1. **Script draft** with clear parameters and logic
2. **Expected runtime** estimate
3. **Input data** description and size
4. **Expected outputs** description and estimated size
5. **System requirements** (RAM, disk space, CPU)
6. **Risk assessment** (what could go wrong)

### Step 2: Approval Request
Present to GIS strategist:
```
APPROVAL REQUEST: [Script Name]
Expected Runtime: [X minutes/hours]
Data Processing: [X GB input → Y GB output]
System Impact: [RAM/CPU/Disk requirements]
Risk Level: [Low/Medium/High]
Justification: [Why this approach is needed]
```

### Step 3: Strategist Review
The strategist will evaluate:
- Technical approach correctness
- Resource requirements appropriateness
- Risk vs benefit analysis
- Alternative approaches
- Timing considerations

### Step 4: Approval or Modification
- **APPROVED**: Proceed with execution as specified
- **MODIFIED**: Implement changes and re-submit
- **REJECTED**: Find alternative approach

### Step 5: Execution Monitoring
During execution:
- Monitor progress and resource usage
- Report any deviations from approved plan
- Stop immediately if unexpected issues arise
- Document any changes made during execution

## Examples of Scripts Requiring Approval

### ✅ REQUIRES APPROVAL
- Batch processing 6+ states
- Creating superoverlays with gdal2tiles.py
- Large raster clipping operations
- Multi-file conversion pipelines
- Disk-intensive operations (>1GB)

### ❌ DOES NOT REQUIRE APPROVAL
- Simple file operations (copy, move, rename)
- Small dataset testing (<100MB)
- Quick validation scripts (<5 minutes)
- Documentation updates
- File structure organization

## Emergency Situations
If immediate action is required and strategist is unavailable:
1. Document the emergency situation
2. Use the most conservative approach possible
3. Process smallest possible dataset first
4. Notify strategist as soon as possible
5. Document all actions taken

## Documentation Requirements
After script execution:
1. Document actual vs expected runtime
2. Record actual vs expected output sizes
3. Note any deviations from approved plan
4. Update lessons learned if applicable
5. Archive script and outputs appropriately

## Consequences of Non-Compliance
Running unapproved long scripts may result in:
- Wasted computational resources
- Incorrect outputs requiring re-processing
- Project delays
- System performance issues
- Data corruption or loss

## Approval Checklist
Before submitting for approval:
- [ ] Script is technically sound
- [ ] Runtime estimate is realistic
- [ ] Resource requirements are documented
- [ ] Risk assessment is complete
- [ ] Alternative approaches considered
- [ ] Justification is clear
- [ ] Expected outputs are defined

---
**This process is MANDATORY and non-negotiable.**
**Date**: September 9, 2025
**Status**: Active
