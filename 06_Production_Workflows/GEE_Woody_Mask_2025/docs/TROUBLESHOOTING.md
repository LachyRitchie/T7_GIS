# Troubleshooting Guide - GEE Woody Mask Workflow

**Complete troubleshooting guide for common issues and solutions**

## Quick Diagnosis

### Check Workflow Status
```bash
# Check if GEE is authenticated
python -c "import ee; ee.Initialize(); print('GEE OK')"

# Check Google Drive access
ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox"

# Check Python environment
conda list | grep earthengine
```

## Common Issues and Solutions

### 1. GEE Authentication Issues

#### Problem: GEE Initialization Failed
```
❌ GEE initialization failed: Please run: earthengine authenticate
```

**Solutions:**
```bash
# Clear existing authentication
earthengine authenticate --clear

# Re-authenticate
earthengine authenticate

# Verify authentication
python -c "import ee; ee.Initialize(); print('GEE authentication successful!')"
```

#### Problem: Authentication Expired
```
❌ GEE initialization failed: Authentication expired
```

**Solution:**
```bash
# Re-authenticate with same Google account
earthengine authenticate
```

#### Problem: Wrong Google Account
```
❌ GEE initialization failed: Access denied
```

**Solution:**
1. Check which Google account is authenticated
2. Ensure it has access to the GEE_Outbox folder
3. Re-authenticate with correct account

### 2. KML File Issues

#### Problem: No KML Files Found
```
❌ No KML files found in project directory: /path/to/project
```

**Solutions:**
```bash
# Check if KML files exist
ls -la /path/to/project/*.kml

# Specify KML file explicitly
python main_workflow.py --project_path "/path/to/project" --kml_name "boundary.kml"

# Check file permissions
ls -la /path/to/project/boundary.kml
```

#### Problem: Invalid KML Format
```
❌ Error processing KML: No coordinates found in KML file
```

**Solutions:**
1. **Check KML structure**:
   ```xml
   <!-- Valid KML structure -->
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

2. **Validate KML online**: Use online KML validators
3. **Convert from other formats**: Use QGIS to export as KML

#### Problem: Multiple KML Files
```
⚠️ Multiple KML files found, using: file1.kml
```

**Solution:**
```bash
# Specify the correct KML file
python main_workflow.py --project_path "/path/to/project" --kml_name "correct_file.kml"
```

### 3. Google Drive Issues

#### Problem: GEE_Outbox Not Accessible
```
❌ GEE_Outbox not accessible
```

**Solutions:**
```bash
# Check if Google Drive is mounted
ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/"

# Check if GEE_Outbox exists
ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox"

# Create GEE_Outbox if missing
mkdir -p "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox"

# Check folder permissions
ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox"
```

#### Problem: Google Drive Not Mounted
```
❌ Google Drive not accessible
```

**Solutions:**
1. **Check Google Drive app**: Ensure it's running
2. **Restart Google Drive**: Quit and restart the app
3. **Check mount point**: Verify the path is correct
4. **Re-authenticate Google Drive**: Sign out and back in

#### Problem: Permission Denied
```
❌ Permission denied: /path/to/GEE_Outbox
```

**Solutions:**
```bash
# Check folder permissions
ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox"

# Fix permissions if needed
chmod 755 "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox"

# Check if you own the folder
ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/" | grep GEE_Outbox
```

### 4. Processing Issues

#### Problem: No Sentinel-2 Images Found
```
❌ No Sentinel-2 images found for the specified date range and location
```

**Solutions:**
1. **Check date range**: Ensure dates are reasonable
2. **Check location**: Verify KML coordinates are valid
3. **Check cloud cover**: Try different date ranges
4. **Check GEE data availability**: Verify Sentinel-2 collection is accessible

#### Problem: Processing Timeout
```
⚠️ Partial completion: 3/5 files
```

**Solutions:**
1. **Check GEE console**: https://code.earthengine.google.com/tasks
2. **Wait longer**: Some tasks may still be processing
3. **Check file sizes**: Large properties take longer
4. **Retry failed tasks**: Re-run the workflow

#### Problem: GEE Tasks Failed
```
❌ Refined_B: FAILED - Export failed
```

**Solutions:**
1. **Check GEE console**: Look for detailed error messages
2. **Check property size**: Very large properties may exceed limits
3. **Check date range**: Try shorter date ranges
4. **Check cloud cover**: Try different date ranges

### 5. File Movement Issues

#### Problem: Files Not Moved
```
⚠️ File not found in GEE_Outbox: WoodyOriginal_Farm_20250123
```

**Solutions:**
1. **Check GEE_Outbox manually**:
   ```bash
   ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox/"
   ```

2. **Check file naming**: GEE may use different naming
3. **Wait longer**: Files may still be processing
4. **Check GEE console**: Verify tasks completed successfully

#### Problem: Partial File Movement
```
📊 Completed files: 3/5
```

**Solutions:**
1. **Check GEE console**: Look for failed tasks
2. **Wait longer**: Some tasks may still be processing
3. **Check file sizes**: Very large files take longer
4. **Retry failed tasks**: Re-run the workflow

### 6. Python Environment Issues

#### Problem: Module Not Found
```
❌ ModuleNotFoundError: No module named 'ee'
```

**Solutions:**
```bash
# Activate correct environment
conda activate t7_gis_professional

# Install missing packages
pip install earthengine-api

# Verify installation
python -c "import ee; print('GEE module OK')"
```

#### Problem: Wrong Python Version
```
❌ Python version 3.8 not supported
```

**Solutions:**
```bash
# Check Python version
python --version

# Activate correct environment
conda activate t7_gis_professional

# Verify version
python --version
# Should show: Python 3.11.x
```

#### Problem: Permission Denied
```
❌ Permission denied: /path/to/script
```

**Solutions:**
```bash
# Make scripts executable
chmod +x "/Volumes/T7 Shield/06_Production_Workflows/GEE_Woody_Mask_2025/scripts"/*.py

# Check file permissions
ls -la "/Volumes/T7 Shield/06_Production_Workflows/GEE_Woody_Mask_2025/scripts/"
```

## Advanced Troubleshooting

### Debug Mode
Enable detailed logging by modifying the script:

```python
# Add to main_workflow.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check GEE Task Status
```bash
# Check GEE console
open https://code.earthengine.google.com/tasks

# Or use Python
python -c "
import ee
ee.Initialize()
tasks = ee.batch.Task.list()
for task in tasks:
    print(f'{task.id}: {task.state}')
"
```

### Manual File Recovery
If automatic file movement fails:

```bash
# Check GEE_Outbox for files
ls -la "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox/"

# Move files manually
cp "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox/WoodyOriginal_Farm_20250123.tif" "/path/to/project/WORKFLOW_OUTPUTS/woody_masks/"
```

### Reset GEE Tasks
If tasks get stuck:

1. Go to GEE console: https://code.earthengine.google.com/tasks
2. Cancel any running tasks
3. Wait 5 minutes
4. Re-run the workflow

### Check System Resources
```bash
# Check disk space
df -h /Volumes/T7\ Shield

# Check memory usage
top -l 1 | grep Python

# Check network connectivity
ping google.com
```

## Performance Issues

### Slow Processing
**Causes:**
- Large property size
- High cloud cover in Sentinel-2 data
- GEE server load
- Network issues

**Solutions:**
1. **Reduce date range**: Use shorter time periods
2. **Increase cloud filter**: Filter out more cloudy images
3. **Check GEE status**: Look for server issues
4. **Try different times**: GEE performance varies

### Memory Issues
**Causes:**
- Very large properties
- Insufficient system memory
- Multiple concurrent processes

**Solutions:**
1. **Process smaller properties**: Break large properties into smaller areas
2. **Close other applications**: Free up system memory
3. **Use shorter date ranges**: Reduce data volume
4. **Process one property at a time**: Avoid concurrent processing

## Getting Help

### Check Logs
```bash
# Check workflow logs
ls -la "/path/to/project/WORKFLOW_OUTPUTS/logs/"

# View latest log
tail -f "/path/to/project/WORKFLOW_OUTPUTS/logs/workflow_log_*.txt"
```

### Verify Configuration
```bash
# Check configuration file
cat "/Volumes/T7 Shield/06_Production_Workflows/GEE_Woody_Mask_2025/scripts/config.json"

# Test GEE connection
python -c "import ee; ee.Initialize(); print('GEE connection OK')"
```

### Test with Simple Case
```bash
# Test with a small, simple property
python main_workflow.py --project_path "/path/to/small_test_property"
```

## Still Having Issues?

If none of the above solutions work:

1. **Check the main README.md** for additional information
2. **Review the setup guide** to ensure proper installation
3. **Test with a known working property** to isolate the issue
4. **Check GEE console** for detailed error messages
5. **Verify all prerequisites** are met

---

**Remember**: Most issues are related to authentication, file permissions, or GEE server status. Check these first before diving into more complex troubleshooting.
