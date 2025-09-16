# Usage Guide - GEE Woody Mask Workflow

**Complete guide for using the GEE Woody Mask Production Workflow**

## Quick Start

### Basic Usage
```bash
# Process a single property
python main_workflow.py --project_path "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Bonza_EP_WA_2025-01"
```

### With Specific KML File
```bash
# Specify a particular KML file
python main_workflow.py \
  --project_path "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Bonza_EP_WA_2025-01" \
  --kml_name "property_boundary.kml"
```

### With Custom Configuration
```bash
# Use custom settings
python main_workflow.py \
  --project_path "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Bonza_EP_WA_2025-01" \
  --config "/path/to/custom_config.json"
```

## Command Line Options

### Required Arguments
- `--project_path`: Path to Farm Assessment project folder

### Optional Arguments
- `--kml_name`: Specific KML filename (auto-detected if not provided)
- `--config`: Path to custom configuration JSON file
- `--property_name`: Property name override (auto-detected from folder if not provided)

### Examples

#### Process Property with Auto-Detection
```bash
python main_workflow.py --project_path "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Smithfield_EP_NSW_2025-01"
```
- Automatically finds KML file in `WORKFLOW_INPUTS/` folder
- Uses "Smithfield" as property name (from folder name)

#### Process with Specific KML
```bash
python main_workflow.py \
  --project_path "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Smithfield_EP_NSW_2025-01" \
  --kml_name "WORKFLOW_INPUTS/corrected_boundary.kml"
```

#### Process with Custom Property Name
```bash
python main_workflow.py \
  --project_path "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Smithfield_EP_NSW_2025-01" \
  --property_name "Smithfield_Farm"
```

## Input Requirements

### Farm Assessment Project Structure
```
/04_FARM_ASSESSMENT/PropertyName_Method_State_Date/
├── WORKFLOW_INPUTS/          # Required: User places KML here
│   └── PropertyName.kml      # Property boundary (required)
├── other_files...            # Other project files
└── WORKFLOW_OUTPUTS/         # Created by workflow
    ├── woody_masks/          # Generated masks go here
    └── logs/                 # Processing logs
```

### KML File Requirements
- **Location**: Must be in `WORKFLOW_INPUTS/` folder within the project
- **Format**: Standard KML with polygon coordinates
- **Structure**: Must contain `<coordinates>` element
- **Geometry**: Single polygon (first polygon used if multiple)
- **Naming**: Any `.kml` filename (first one found if multiple)

### Supported KML Examples
```xml
<!-- Simple polygon -->
<kml>
  <Document>
    <Placemark>
      <Polygon>
        <outerBoundaryIs>
          <LinearRing>
            <coordinates>151.2,-33.8 151.3,-33.8 151.3,-33.9 151.2,-33.9 151.2,-33.8</coordinates>
          </LinearRing>
        </outerBoundaryIs>
      </Polygon>
    </Placemark>
  </Document>
</kml>
```

## Output Structure

### Generated Files
Each successful run creates 5 GeoTIFF files:

```
WORKFLOW_OUTPUTS/woody_masks/
├── WoodyOriginal_FarmName_20250123.tif
├── WoodyRefinedB_FarmName_20250123.tif
├── WoodyRefinedC_FarmName_20250123.tif
├── WoodyRefinedD_FarmName_20250123.tif
└── WoodyRefinedE_FarmName_20250123.tif
```

### File Specifications
- **Format**: GeoTIFF
- **CRS**: EPSG:4326 (WGS84)
- **Scale**: 10m pixels
- **Compression**: LZW with cloud optimization
- **NoData**: 255 (excluded areas)
- **Values**: 0 (suitable), 1 (woody vegetation)

### Log Files
```
WORKFLOW_OUTPUTS/logs/
└── workflow_log_20250123_143022.txt
```

## Processing Workflow

### Stage 1: Initialization (30 seconds)
1. Load and validate KML boundary
2. Initialize Google Earth Engine
3. Create output directory structure
4. Validate Google Drive access

### Stage 2: Sentinel-2 Processing (2-10 minutes)
1. Load Sentinel-2 collection for property area
2. Filter by date range and cloud cover
3. Calculate NDVI for each image
4. Generate woody score components

### Stage 3: Mask Generation (1-5 minutes)
1. Calculate 5 woody mask methods
2. Apply canvas method for dense raster
3. Prepare exports with proper naming

### Stage 4: GEE Export (1-10 minutes)
1. Submit 5 export tasks to Google Earth Engine
2. Export to GEE_Outbox folder
3. Monitor task status

### Stage 5: File Monitoring (1-15 minutes)
1. Poll GEE_Outbox for completed files
2. Move files to project folder
3. Clean up GEE_Outbox
4. Verify all outputs received

## Configuration Options

### Default Settings
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

### Custom Configuration Example
```json
{
  "date_start": "2020-01-01",
  "date_end": "2024-12-31",
  "scale": 20,
  "max_wait": 3600,
  "poll_interval": 60
}
```

## Batch Processing

### Simple Batch Script
```bash
#!/bin/bash
# batch_process.sh

# List of properties to process
properties=(
    "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Property1_EP_NSW_2025-01"
    "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Property2_EP_QLD_2025-01"
    "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Property3_EP_WA_2025-01"
)

# Process each property
for prop in "${properties[@]}"; do
    echo "Processing: $prop"
    python main_workflow.py --project_path "$prop"
    
    if [ $? -eq 0 ]; then
        echo "✅ Completed: $prop"
    else
        echo "❌ Failed: $prop"
    fi
    echo "---"
done
```

### Advanced Batch with Error Handling
```bash
#!/bin/bash
# advanced_batch.sh

# Configuration
LOG_FILE="batch_processing_$(date +%Y%m%d_%H%M%S).log"
SUCCESS_COUNT=0
FAILED_COUNT=0

# Properties to process
properties=(
    "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Property1_EP_NSW_2025-01"
    "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Property2_EP_QLD_2025-01"
    "/Volumes/T7 Shield/04_FARM_ASSESSMENT/Property3_EP_WA_2025-01"
)

echo "Starting batch processing at $(date)" | tee -a "$LOG_FILE"

for prop in "${properties[@]}"; do
    echo "Processing: $prop" | tee -a "$LOG_FILE"
    
    python main_workflow.py --project_path "$prop" 2>&1 | tee -a "$LOG_FILE"
    
    if [ $? -eq 0 ]; then
        echo "✅ Completed: $prop" | tee -a "$LOG_FILE"
        ((SUCCESS_COUNT++))
    else
        echo "❌ Failed: $prop" | tee -a "$LOG_FILE"
        ((FAILED_COUNT++))
    fi
    echo "---" | tee -a "$LOG_FILE"
done

echo "Batch processing completed at $(date)" | tee -a "$LOG_FILE"
echo "Success: $SUCCESS_COUNT, Failed: $FAILED_COUNT" | tee -a "$LOG_FILE"
```

## Monitoring Progress

### Real-Time Monitoring
The workflow provides real-time progress updates:

```
🌍 GEE WOODY MASK PRODUCTION WORKFLOW v1.0
============================================================
Start time: 2025-01-23 14:30:22

📋 CONFIGURATION:
Property: Bonza
Project: /Volumes/T7 Shield/04_FARM_ASSESSMENT/BONZA_EP_WA
KML: /Volumes/T7 Shield/04_FARM_ASSESSMENT/BONZA_EP_WA/Bonza_Farm.kml
GEE Outbox: /Users/lachyritchie/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox
Output: /Volumes/T7 Shield/04_FARM_ASSESSMENT/BONZA_EP_WA/WORKFLOW_OUTPUTS

🔧 Initializing Google Earth Engine...
✅ GEE initialized successfully

📁 Loading KML boundary: /Volumes/T7 Shield/04_FARM_ASSESSMENT/BONZA_EP_WA/Bonza_Farm.kml
✅ Boundary loaded successfully
📍 Boundary bounds: [[151.2, -33.8], [151.3, -33.9]]

🚀 Starting GEE processing: Bonza

============================================================
Processing: Bonza
Date range: 2019-01-01 to 2025-01-01
============================================================

📡 Loading Sentinel-2 data...
Found 127 Sentinel-2 images

🧮 Calculating woody score components...

🎨 Creating canvas for dense raster...

🔨 Processing Original method
   Description: Original Best (Score > 0.15) - "Still very strong!"
📤 Exporting: WoodyOriginal_Bonza_20250123
  ✅ Task started - ID: 1234567890123456789

🔨 Processing Refined_B method
   Description: Refined B (Score + Veg History) - "Very strong! Might catch recent clearing"
📤 Exporting: WoodyRefinedB_Bonza_20250123
  ✅ Task started - ID: 1234567890123456790

[... continues for all 5 methods ...]

============================================================
📊 Monitoring export tasks and moving files...
============================================================

⏳ Original: RUNNING
⏳ Refined_B: RUNNING
⏳ Refined_C: RUNNING
⏳ Refined_D: RUNNING
⏳ Refined_E: RUNNING

⏰ Elapsed time: 2.1 minutes
⏳ Waiting 30 seconds before next check...

✅ Original: COMPLETED - WoodyOriginal_Bonza_20250123
📁 Moved: WoodyOriginal_Bonza_20250123
✅ Refined_B: COMPLETED - WoodyRefinedB_Bonza_20250123
📁 Moved: WoodyRefinedB_Bonza_20250123

[... continues until all files complete ...]

🎉 Monitoring complete! Total time: 8.3 minutes
📊 Completed files: 5/5
✅ All expected files completed and moved successfully!

============================================================
🎉 PROCESSING COMPLETE!
============================================================
📁 Outputs saved to: /Volumes/T7 Shield/04_FARM_ASSESSMENT/BONZA_EP_WA/WORKFLOW_OUTPUTS/woody_masks
📊 Generated files:
  - WoodyOriginal_Bonza_20250123.tif
  - WoodyRefinedB_Bonza_20250123.tif
  - WoodyRefinedC_Bonza_20250123.tif
  - WoodyRefinedD_Bonza_20250123.tif
  - WoodyRefinedE_Bonza_20250123.tif

⏰ Completed at: 2025-01-23 14:38:45
```

## Quality Assurance

### Pre-Processing Checks
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
- **Small property** (<100ha): 1-5MB per file
- **Medium property** (100-1000ha): 5-20MB per file
- **Large property** (>1000ha): 20-100MB per file

## Next Steps

After successful processing:

1. **Load in QGIS**: Import the generated GeoTIFF files
2. **Apply styling**: Use the provided QML style files
3. **Create visualizations**: Generate maps and reports
4. **Archive results**: Move to appropriate project folders

## Troubleshooting

For common issues and solutions, see `docs/TROUBLESHOOTING.md`.

---

**Ready to process your first property?** Start with a small test property to verify everything is working correctly!
