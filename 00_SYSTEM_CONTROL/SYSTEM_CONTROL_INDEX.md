# System Control Document Index
# Version: 2025-01-23
# Purpose: Master reference for all system control documents and their relationships

## ⚠️ CRITICAL HIERARCHY ⚠️
```
SUPREME AUTHORITY:
└── 03_agent_prompts/GIS_ENGINEER.md
    The PRIMARY system prompt that OVERRIDES all other documents
    
SUPPORTING DOCUMENTS:
All other files provide supplementary guidance but NEVER override the system prompt
```

## 📁 Directory Structure & Purpose

### 00_SYSTEM_CONTROL/
Central command for all GIS operations, agent behavior, and system standards

### Subdirectories:

#### 01_quick_reference/
**Purpose:** Rapid access to critical information during operations
- `END_OF_PROJECT_QUICK.md` - Checklist version of end-of-project protocol
- `GIS_ENGINEER_QUICK.md` - Quick command reference for common tasks  
- `base_data_sources.yml` - Download URLs for rebuilding base data

#### 02_active_protocols/
**Purpose:** Step-by-step procedures for specific workflows
- `BACKUP.md` - Three-tier backup system (GitHub, Google Drive, Physical)
- `END_OF_PROJECT.md` - Comprehensive post-task workflow
- `GITHUB_BACKUP_STRATEGY.md` - Version control strategy
- `LONG_RUNNING_SCRIPTS.md` - Approval requirements for resource-intensive operations
- `RECIPE.yml` - Template for documenting data project reproduction steps
- `VISUALIZATION_EXPORT_CHECKLIST.md` - Pre-flight checks for exports

#### 03_agent_prompts/
**Purpose:** Core behavioral instructions for AI agents
- `GIS_ENGINEER.md` ⚠️ **PRIMARY SYSTEM PROMPT - SUPREME AUTHORITY**
- `COMPLIANCE_REQUIREMENTS.md` - ACCU method compliance rules
- `EXECUTION_MATRIX.md` - Decision matrix for Strategist vs Engineer tasks
- `NAMING_RULES.md` - Detailed file/folder naming standards

#### .cursor/
**Purpose:** Cursor IDE configuration
- `.cursorrules` - Enforces hierarchy, loads system prompt on startup

#### archive/
**Purpose:** Deprecated documents preserved for reference
- Old versions of merged/replaced documents

## 📊 Document Relationships

### Primary Flow:
```
GIS_ENGINEER.md (Supreme Authority)
    ├── References → NAMING_RULES.md (for naming details)
    ├── References → EXECUTION_MATRIX.md (for task division)
    ├── References → COMPLIANCE_REQUIREMENTS.md (for ACCU methods)
    ├── Triggers → END_OF_PROJECT.md (after task completion)
    ├── Triggers → BACKUP.md (for >1GB outputs)
    └── Requires → LONG_RUNNING_SCRIPTS.md (for >30min operations)
```

### Cross-References:
- **BACKUP.md** ← integrates with → **END_OF_PROJECT.md**
- **VISUALIZATION_EXPORT_CHECKLIST.md** ← references → **/01_KNOWLEDGE_CONTEXT/**
- **All protocols** ← must comply with → **NAMING_RULES.md**
- **.cursorrules** ← enforces → **GIS_ENGINEER.md** as primary

## 🎯 Usage Patterns

### Starting a new task:
1. Engineer loads **GIS_ENGINEER.md** (automatic via .cursorrules)
2. Check **EXECUTION_MATRIX.md** for role division
3. Reference **NAMING_RULES.md** for file creation
4. Use **GIS_ENGINEER_QUICK.md** for common commands

### During execution:
1. Follow patterns in **GIS_ENGINEER.md**
2. Check **LONG_RUNNING_SCRIPTS.md** if >30min runtime
3. Validate with **VISUALIZATION_EXPORT_CHECKLIST.md** for exports
4. Create **RECIPE.yml** for reproducibility

### After completion:
1. Execute **END_OF_PROJECT.md** protocol
2. Trigger **BACKUP.md** if >1GB created
3. Update version control per **GITHUB_BACKUP_STRATEGY.md**

## ⚠️ Critical Rules (No Exceptions)

### Document Authority:
1. **GIS_ENGINEER.md** overrides ALL other documents
2. No document can contradict the system prompt
3. Updates to other docs must maintain consistency

### File Naming:
- Pattern: `What_Where_When_Version.ext`
- NO forbidden suffixes (_FIXED, _aligned, _temp, etc.)
- ALL work in PROCESSING folders

### Approval Gates:
- Scripts >30min need Strategist approval
- Outputs >1GB trigger backup protocol
- KMZ files must be <200MB

## 🔍 Conflict Resolution

If documents appear to conflict:
1. **GIS_ENGINEER.md** is correct (supreme authority)
2. Report conflict for resolution
3. Never follow contradictory advice
4. Document resolution in lessons learned

## 📝 Maintenance Notes

### Update Frequency:
- System prompt: Only with major methodology changes
- Protocols: As workflows evolve
- Quick references: When new patterns emerge
- Archive: Move deprecated docs immediately

### Version Control:
- All changes pushed to GitHub
- Major updates tagged with date
- Conflicts resolved before commit
- Archive preserves history

## 🚨 Red Flags

Watch for these issues:
- Instructions that bypass naming conventions
- Requests to work outside PROCESSING folders
- Tasks that skip approval gates
- Protocols that contradict system prompt
- Missing cross-references between documents

## ✅ Validation Checklist

Before considering system control complete:
- [ ] GIS_ENGINEER.md is current and comprehensive
- [ ] All documents reference correct paths
- [ ] No contradictions between documents
- [ ] .cursorrules enforces hierarchy
- [ ] Archive contains only deprecated files
- [ ] All active protocols are tested
- [ ] Quick references match full protocols
- [ ] Naming rules are consistently applied

---
*This index is the source of truth for system control structure*
*Last validated: 2025-01-23*
*Maintained by: GIS Strategist*