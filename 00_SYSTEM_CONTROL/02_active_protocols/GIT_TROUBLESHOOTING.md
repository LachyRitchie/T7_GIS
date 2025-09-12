# Git Troubleshooting Guide for T7 Shield
**Date:** 2025-01-11  
**Status:** ACTIVE  
**Issue:** External drive Git corruption with macOS resource fork files

---

## 🚨 CRITICAL GIT CORRUPTION PATTERN

### Root Cause
macOS resource fork files (`._pack-*.idx`) interfere with Git's pack index files on external drives, causing:
- "non-monotonic index" errors
- Terminal command hanging
- Git operations failure
- IDE "too many active changes" warnings

### Symptoms Checklist
- [ ] Terminal commands get stuck/hang (especially `git add`, `git status`)
- [ ] "non-monotonic index .git/objects/pack/._pack-*.idx" errors
- [ ] Git operations fail with corruption warnings
- [ ] "too many active changes" warnings in IDE
- [ ] `git gc --prune=now` fails with "unable to mark recent objects"

---

## 🔧 IMMEDIATE SOLUTIONS

### Level 1: Quick Fix
```bash
# Remove corrupted pack files
rm -f .git/objects/pack/._*

# Remove lock files
rm -f .git/index.lock

# Clean resource forks
find . -name "._*" -type f -delete 2>/dev/null || true
```

### Level 2: Reset Index
```bash
# Remove corrupted index
rm -f .git/index

# Reset Git state
git reset
```

### Level 3: Nuclear Option (Complete Rebuild)
```bash
# Check what we have committed
git log --oneline

# Backup current work
cp -r .git .git_backup

# Nuke and rebuild
rm -rf .git
git init
git config core.precomposeUnicode false
git config core.quotepath false
git config core.autocrlf false

# Reconnect to GitHub
git remote add origin https://github.com/LachyRitchie/T7_GIS.git

# Re-add system files only
git add .gitignore .cursorrules 00_SYSTEM_CONTROL/ 01_KNOWLEDGE_CONTEXT/
git commit -m "System control and knowledge base - fresh start after corruption fix"
git push -u origin main
```

---

## 🛡️ PREVENTION MEASURES

### Git Configuration (Run After Fresh Init)
```bash
git config core.precomposeUnicode false
git config core.quotepath false
git config core.autocrlf false
```

### Proper .gitignore (Already Implemented)
```gitignore
# macOS system files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
.fseventsd
.TemporaryItems
.AppleDouble
.LSOverride

# Large data files - exclude from Git per backup protocol
02_BASE_DATA/
03_DATA_PROJECTS/
04_FARM_ASSESSMENT/
05_TEMPLATES_LAYOUTS/
09_ARCHIVE/

# Additional data file types
*.tif
*.tif.ovr
*.gpkg
*.shp
*.dbf
*.shx
*.prj
*.aux.xml
*.cpg
*.qgz
```

### Backup Protocol Compliance
- ✅ **GitHub tracks:** System control, scripts, knowledge base only
- ❌ **Never track:** Large data directories (hundreds of GB)
- ✅ **Physical backup:** Data projects to T7 Backup drive
- ✅ **Google Drive:** Farm outputs (PDFs, KMZ, XML only)

---

## 📋 TROUBLESHOOTING CHECKLIST

### When Git Commands Hang
1. [ ] Press `Ctrl+C` to interrupt
2. [ ] Check for lock files: `ls -la .git/`
3. [ ] Remove lock files: `rm -f .git/index.lock`
4. [ ] Try selective file addition instead of `git add .`

### When "Too Many Active Changes" Warning Appears
1. [ ] Check Git status: `git status --porcelain | wc -l`
2. [ ] Verify .gitignore is working: `git status --ignored`
3. [ ] Remove system files from tracking: `git rm -r --cached .Spotlight-V100 .Trashes .fseventsd`
4. [ ] Update .gitignore if needed

### When Non-Monotonic Index Errors Occur
1. [ ] Remove corrupted pack files: `rm -f .git/objects/pack/._*`
2. [ ] Clean resource forks: `find . -name "._*" -type f -delete`
3. [ ] If persistent, use nuclear option (complete rebuild)

---

## ⚡ QUICK REFERENCE COMMANDS

### Emergency Git Reset
```bash
rm -rf .git && git init && git config core.precomposeUnicode false && git config core.quotepath false && git config core.autocrlf false
```

### Safe File Addition
```bash
# Instead of git add .
git add .gitignore .cursorrules 00_SYSTEM_CONTROL/ 01_KNOWLEDGE_CONTEXT/
```

### Check Repository Health
```bash
git status
git log --oneline
git remote -v
```

---

## 🎯 RECOVERY TIME ESTIMATES

- **Level 1 Fix:** 5-10 minutes
- **Level 2 Fix:** 10-15 minutes  
- **Level 3 Fix:** 30-60 minutes
- **Complete Rebuild:** 1-2 hours (including GitHub setup)

---

## 🔄 ALTERNATIVE SOLUTIONS

### If External Drive Issues Persist
1. **Move Git to Local Drive:** Clone repository to `~/T7_Shield_Git/` and symlink
2. **Use Script Collection System:** Implement automated script backup per backup protocol
3. **Separate Repositories:** Create dedicated repos for different data types

### Script Collection Approach (From Backup Protocol)
```bash
# Create script backup directory
mkdir -p /Volumes/T7\ Shield/00_SYSTEM_CONTROL/project_scripts

# Collect all scripts from projects
find /Volumes/T7\ Shield/03_DATA_PROJECTS -type f \
  \( -name "*.sh" -o -name "*.py" -o -name "*.sql" \) \
  -exec cp --parents {} /Volumes/T7\ Shield/00_SYSTEM_CONTROL/project_scripts/ \;

# Commit scripts to Git
git add 00_SYSTEM_CONTROL/project_scripts/
git commit -m "Backup project scripts $(date +%Y-%m-%d)"
```

---

## 📞 ESCALATION

### When to Use Nuclear Option
- Git commands consistently hang
- Multiple corruption errors persist
- Terminal becomes unresponsive
- Recovery time exceeds 30 minutes

### When to Consider Alternative Solutions
- External drive corruption is persistent
- Git operations fail more than 3 times per week
- Data loss risk becomes unacceptable

---

## 📝 LESSONS LEARNED

1. **External drives + Git + macOS = High corruption risk**
2. **Resource fork files are the primary culprit**
3. **Selective file tracking is essential for large datasets**
4. **Fresh Git initialization often faster than repair**
5. **Backup protocol compliance prevents most issues**

---

*This guide should be referenced whenever Git corruption issues occur on the T7 Shield system.*
