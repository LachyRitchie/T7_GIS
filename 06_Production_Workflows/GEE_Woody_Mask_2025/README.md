# GEE Woody Mask Production Workflow v1.0

**Complete automated workflow for processing KML boundaries and generating woody vegetation masks using Google Earth Engine**

## Overview

This production workflow processes KML property boundaries through Google Earth Engine to generate 5 proven woody vegetation masks. It automatically handles file monitoring, movement from Google Drive, and organizes outputs in the proper Farm Assessment project structure.

## What This Workflow Does

1. **Reads KML boundary files** from Farm Assessment project folders
2. **Processes through Google Earth Engine** using Sentinel-2 NDVI data
3. **Generates 5 woody mask methods**:
   - Original (Score > 0.15)
   - Refined B (Score + Vegetation History)
   - Refined C (Score + P25)
   - Refined D (Score > 0.16)
   - Refined E (Combined method)
4. **Automatically monitors GEE_Outbox** for completed files
5. **Moves outputs** to project folder in organized structure
6. **Handles errors gracefully** with comprehensive logging

## Prerequisites

### 1. Google Earth Engine Authentication
```bash
# Run this once to authenticate
earthengine authenticate
```

### 2. Python Environment
```bash
# Activate the T7 GIS environment
conda activate t7_gis_professional

# Install additional requirements
pip install -r requirements.txt
```

### 3. Google Drive Access
- Ensure Google Drive is mounted and accessible
- Verify GEE_Outbox folder exists in Google Drive
- Check path: `~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox`

## Quick Start

### Single Property Processing
```bash
python main_workflow.py --project_path "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Bonza_EP_WA_2025-01"
```

### With Specific KML File
```bash
python main_workflow.py \
  --project_path "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Bonza_EP_WA_2025-01" \
  --kml_name "property_boundary.kml"
```

### With Custom Configuration
```bash
python main_workflow.py \
  --project_path "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Bonza_EP_WA_2025-01" \
  --config "/path/to/custom_config.json"
```

## Input Requirements

### Farm Assessment Project Structure
```
/04_FARM_ASSESSMENT/PropertyName_Method_State_Date/
├── PropertyName.kml          # Property boundary (auto-detected)
├── other_files...            # Other project files
└── WORKFLOW_OUTPUTS/         # Created by workflow
    ├── woody_masks/          # Generated masks go here
    └── logs/                 # Processing logs
```

### KML File Requirements
- Must contain valid polygon coordinates
- Standard KML format with `<coordinates>` element
- Single polygon per file (first polygon used if multiple)

## Output Structure

### Generated Files
Each run creates 5 GeoTIFF files in the project's `WORKFLOW_OUTPUTS/woody_masks/` folder:

```
WoodyOriginal_FarmName_20250123.tif
WoodyRefinedB_FarmName_20250123.tif
WoodyRefinedC_FarmName_20250123.tif
WoodyRefinedD_FarmName_20250123.tif
WoodyRefinedE_FarmName_20250123.tif
```

### File Specifications
- **Format**: GeoTIFF
- **CRS**: EPSG:4326 (WGS84)
- **Scale**: 10m pixels
- **Compression**: LZW with cloud optimization
- **NoData**: 255 (excluded areas)
- **Values**: 0 (suitable), 1 (woody vegetation)

## Configuration

### Default Settings (config.json)
```json
{
  "gee_outbox": "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox",
  "output_subfolder": "WORKFLOW_OUTPUTS",
  "expected_outputs": 5,
  "poll_interval": 30,
  "max_wait": 1800,
  "date_start": "2019-01-01",
  "date_end": "2025-01-01",
  "scale": 10,
  "crs": "EPSG:4326",
  "max_pixels": 10000000000000
}
```

### Custom Configuration
Create a custom JSON file to override defaults:

```json
{
  "date_start": "2020-01-01",
  "date_end": "2024-12-31",
  "scale": 20,
  "max_wait": 3600
}
```

## Processing Times

### Typical Performance
- **Small property** (<100ha): 2-5 minutes
- **Medium property** (100-1000ha): 5-15 minutes  
- **Large property** (>1000ha): 15-30 minutes

### Factors Affecting Speed
- Property size and complexity
- Cloud cover in Sentinel-2 data
- Google Earth Engine server load
- Network speed for file transfers

## Error Handling

### Common Issues and Solutions

#### GEE Authentication Failed
```
❌ GEE initialization failed: Please run: earthengine authenticate
```
**Solution**: Run `earthengine authenticate` and follow prompts

#### KML File Not Found
```
❌ No KML files found in project directory
```
**Solution**: Ensure KML file exists in project folder or specify with `--kml_name`

#### Google Drive Not Accessible
```
❌ GEE_Outbox not accessible
```
**Solution**: Check Google Drive mount and folder permissions

#### Processing Timeout
```
⚠️ Partial completion: 3/5 files
```
**Solution**: Check GEE_Outbox manually, files may still be processing

### Log Files
Check `WORKFLOW_OUTPUTS/logs/` for detailed processing logs and error information.

## Batch Processing

### Multiple Properties
For processing multiple properties, create a simple batch script:

```bash
#!/bin/bash
# batch_process.sh

properties=(
    "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Property1_EP_NSW_2025-01"
    "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Property2_EP_QLD_2025-01"
    "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Property3_EP_WA_2025-01"
)

for prop in "${properties[@]}"; do
    echo "Processing: $prop"
    python main_workflow.py --project_path "$prop"
    echo "Completed: $prop"
    echo "---"
done
```

## Quality Assurance

### Pre-Processing Validation
- ✅ KML file exists and is valid
- ✅ GEE authentication active
- ✅ Google Drive accessible
- ✅ Project folder structure correct

### Post-Processing Validation
- ✅ All 5 output files generated
- ✅ Files moved to correct location
- ✅ File sizes reasonable (>1MB each)
- ✅ GEE_Outbox cleaned up

### File Size Expectations
- **Small property**: 1-5MB per file
- **Medium property**: 5-20MB per file
- **Large property**: 20-100MB per file

## Troubleshooting

### Debug Mode
Add `--verbose` flag for detailed output (if implemented in future versions).

### Manual File Recovery
If automatic file movement fails, check GEE_Outbox manually:
```bash
ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox/"
```

### Reset GEE Tasks
If tasks get stuck, cancel them in GEE console:
https://code.earthengine.google.com/tasks

## Support

### Documentation
- **Setup Guide**: `docs/SETUP.md`
- **Usage Guide**: `docs/USAGE.md`
- **Troubleshooting**: `docs/TROUBLESHOOTING.md`

### Version Information
- **Workflow Version**: 1.0
- **Python Requirements**: 3.11+
- **GEE API Version**: 0.1.370+
- **Last Updated**: 2025-01-23

---

**Author**: GIS Engineer  
**System**: T7 Shield GIS Workflows  
**Category**: Production Workflow
