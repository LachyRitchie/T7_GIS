# Setup Guide - GEE Woody Mask Workflow

**One-time setup instructions for the GEE Woody Mask Production Workflow**

## Prerequisites

### 1. System Requirements
- **Operating System**: macOS (tested on macOS 14.6.0)
- **Python**: 3.11+ (via conda)
- **Storage**: 1GB free space for temporary files
- **Network**: Stable internet connection for GEE access

### 2. Required Software
- **Conda**: For Python environment management
- **Google Earth Engine CLI**: For authentication
- **Google Drive**: Mounted and accessible

## Step-by-Step Setup

### Step 1: Activate Python Environment

```bash
# Activate the T7 GIS environment
conda activate t7_gis_professional

# Verify Python version
python --version
# Should show: Python 3.11.x
```

### Step 2: Install Additional Dependencies

```bash
# Navigate to workflow directory
cd "/Volumes/T7 Shield/06_Production_Workflows/GEE_Woody_Mask_2025/scripts"

# Install requirements
pip install -r requirements.txt
```

### Step 3: Google Earth Engine Authentication

```bash
# Authenticate with Google Earth Engine
earthengine authenticate

# Follow the prompts:
# 1. Open the provided URL in your browser
# 2. Sign in with your Google account
# 3. Copy the authorization code
# 4. Paste it back in the terminal
```

**Important**: Use the same Google account that has access to the GEE_Outbox folder.

### Step 4: Verify Google Drive Access

```bash
# Check if Google Drive is mounted
ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/"

# Verify GEE_Outbox folder exists
ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox"
```

If the GEE_Outbox folder doesn't exist, create it:
```bash
mkdir -p "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox"
```

### Step 5: Test GEE Connection

```bash
# Test GEE authentication
python -c "import ee; ee.Initialize(); print('GEE authentication successful!')"
```

Expected output:
```
GEE authentication successful!
```

### Step 6: Verify Workflow Structure

```bash
# Check workflow directory structure
ls -la "/Volumes/T7 Shield/06_Production_Workflows/GEE_Woody_Mask_2025/"

# Should show:
# README.md
# RECIPE.yml
# CURRENT_VERSION.txt
# scripts/
# docs/
# archive/
```

## Configuration

### Default Configuration
The workflow uses default settings from `scripts/config.json`. No changes needed for basic usage.

### Custom Configuration (Optional)
Create a custom configuration file to override defaults:

```json
{
  "date_start": "2020-01-01",
  "date_end": "2024-12-31",
  "scale": 20,
  "max_wait": 3600
}
```

## Verification Test

### Run a Test with Existing Data
```bash
# Test with an existing Farm Assessment project
python main_workflow.py --project_path "/Volumes/T7 Shield/04_FARM_ASSESSMENT/BONZA_EP_WA"

# Expected output:
# - GEE initialization successful
# - KML boundary loaded
# - 5 export tasks started
# - Files monitored and moved to project folder
```

## Troubleshooting Setup Issues

### GEE Authentication Fails
```bash
# Clear existing authentication
earthengine authenticate --clear

# Re-authenticate
earthengine authenticate
```

### Google Drive Not Accessible
1. Check if Google Drive is running
2. Verify folder permissions
3. Try accessing the folder in Finder first

### Python Environment Issues
```bash
# Recreate conda environment
conda create -n t7_gis_professional python=3.11
conda activate t7_gis_professional

# Install all dependencies
pip install -r requirements.txt
```

### Permission Issues
```bash
# Make scripts executable
chmod +x "/Volumes/T7 Shield/06_Production_Workflows/GEE_Woody_Mask_2025/scripts"/*.py
```

## Environment Variables (Optional)

Set these environment variables for enhanced logging:

```bash
# Add to ~/.zshrc or ~/.bash_profile
export GEE_WORKFLOW_DEBUG=1
export GEE_WORKFLOW_LOG_LEVEL=INFO
```

## Next Steps

After successful setup:

1. **Read the Usage Guide**: `docs/USAGE.md`
2. **Test with a small property**: Use an existing Farm Assessment project
3. **Review the Troubleshooting Guide**: `docs/TROUBLESHOOTING.md`

## Support

If you encounter issues during setup:

1. Check the troubleshooting section above
2. Review the main README.md
3. Check GEE console for task status: https://code.earthengine.google.com/tasks
4. Verify Google Drive folder permissions

---

**Setup completed successfully?** Proceed to the Usage Guide to start processing properties!
