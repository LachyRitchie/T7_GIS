# Critical Patterns (Updated Mon Sep  8 15:22:30 AWST 2025)

## Frequent Failures
Based on analysis of lessons learned:

   1 problem: |

## Successful Patterns
From tested_workflows.yml:

  method: qgis_rendered_export_kmz
  method: gdaldem_color_relief_simple_kml
  method: cookie_cutter_gdal_calc
  method: gdalwarp_with_tap
    method: "qgis_rendered_export"
    method: "gdaldem_color_relief"
    method: "rendered_export"

## Red Flags to Watch For

- File sizes >10x expected
- Processing time >2 hours for simple tasks
- Complex methods for simple problems
- Ignoring QGIS when it already displays correctly

## Quick Reference

### Binary Masks → Google Earth
1. **USE QGIS RENDERED EXPORT** - preserves transparency correctly
2. Create simple GroundOverlay KML manually
3. Zip KML + PNG into KMZ
4. Expected size: 1-2MB

### Continuous Data → Google Earth
1. gdaldem color-relief with color map
2. Verify 4-band RGBA output
3. gdal_translate to KML (NOT KMLSUPEROVERLAY)
4. Create simple GroundOverlay KML manually
5. Expected size: 50-200MB
