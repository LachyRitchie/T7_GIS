#!/usr/bin/env python3
"""
GEE Woody Mask Production Workflow v1.0
=======================================
Complete automated workflow for processing KML boundaries and generating woody vegetation masks

Features:
- Parameterized for any Farm Assessment project
- Automatic GEE_Outbox monitoring and file movement
- Comprehensive error handling and logging
- Production-ready configuration management

Author: GIS Engineer
Date: 2025-01-23
Version: 1.0
"""

import ee
import time
import os
import shutil
import json
import argparse
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET
from file_monitor import GEEFileMonitor
from gee_processor import GEEProcessor

# =============================================================================
# CONFIGURATION MANAGEMENT
# =============================================================================

def load_config(config_path=None):
    """Load configuration from file or use defaults"""
    default_config = {
        "gee_outbox": "~/Library/CloudStorage/GoogleDrive-admin@relanature.com/My Drive/GEE_Outbox",
        "output_subfolder": "WORKFLOW_OUTPUTS",
        "expected_outputs": 5,
        "poll_interval": 30,
        "max_wait": 1800,
        "date_start": "2019-01-01",
        "date_end": "2025-01-01",
        "scale": 10,
        "crs": "EPSG:4326",
        "max_pixels": 1e13
    }
    
    if config_path and os.path.exists(config_path):
        with open(config_path, 'r') as f:
            user_config = json.load(f)
            default_config.update(user_config)
    
    # Expand user paths
    default_config["gee_outbox"] = os.path.expanduser(default_config["gee_outbox"])
    
    return default_config

# =============================================================================
# KML PROCESSING
# =============================================================================

def load_kml_boundary(file_path, property_name):
    """Load KML boundary and convert to GEE FeatureCollection"""
    print(f"📁 Loading KML boundary: {file_path}")
    
    try:
        # Parse KML
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Find coordinates (simplified - assumes single Polygon)
        coords_elem = root.find('.//{http://www.opengis.net/kml/2.2}coordinates')
        if coords_elem is None:
            raise ValueError("No coordinates found in KML file")
        
        coords_text = coords_elem.text.strip()
        coords = []
        
        for coord_pair in coords_text.split():
            if coord_pair.strip():
                lon, lat, alt = coord_pair.split(',')
                coords.append([float(lon), float(lat)])
        
        # Create GeoJSON
        geojson = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {"name": property_name},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [coords]
                }
            }]
        }
        
        # Convert to GEE FeatureCollection
        return ee.FeatureCollection(geojson)
        
    except Exception as e:
        print(f"❌ Error processing KML: {e}")
        raise

# =============================================================================
# WORKFLOW ORCHESTRATION
# =============================================================================

def validate_inputs(project_path, kml_path=None):
    """Validate input paths and find KML if not specified"""
    project_path = Path(project_path)
    
    if not project_path.exists():
        raise ValueError(f"Project path does not exist: {project_path}")
    
    # Find KML file if not specified
    if kml_path is None:
        kml_files = list(project_path.glob("*.kml"))
        if not kml_files:
            raise ValueError(f"No KML files found in project directory: {project_path}")
        elif len(kml_files) > 1:
            print(f"⚠️  Multiple KML files found, using: {kml_files[0].name}")
        kml_path = kml_files[0]
    else:
        kml_path = Path(kml_path)
        if not kml_path.exists():
            raise ValueError(f"KML file does not exist: {kml_path}")
    
    return project_path, kml_path

def setup_output_structure(project_path, output_subfolder):
    """Create output directory structure"""
    output_dir = Path(project_path) / output_subfolder
    output_dir.mkdir(exist_ok=True)
    
    # Create subdirectories
    (output_dir / "woody_masks").mkdir(exist_ok=True)
    (output_dir / "logs").mkdir(exist_ok=True)
    
    return output_dir

def main():
    """Main execution workflow"""
    parser = argparse.ArgumentParser(description='GEE Woody Mask Production Workflow')
    parser.add_argument('--project_path', required=True, 
                       help='Path to Farm Assessment project folder')
    parser.add_argument('--kml_name', 
                       help='Specific KML filename (auto-detected if not provided)')
    parser.add_argument('--config', 
                       help='Path to configuration JSON file')
    parser.add_argument('--property_name', 
                       help='Property name override (auto-detected from folder if not provided)')
    
    args = parser.parse_args()
    
    print("🌍 GEE WOODY MASK PRODUCTION WORKFLOW v1.0")
    print("=" * 60)
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Load configuration
        config = load_config(args.config)
        
        # Validate inputs
        project_path, kml_path = validate_inputs(args.project_path, args.kml_name)
        
        # Extract property name
        if args.property_name:
            property_name = args.property_name
        else:
            property_name = project_path.name.split('_')[0]  # First part before underscore
        
        print(f"\n📋 CONFIGURATION:")
        print(f"Property: {property_name}")
        print(f"Project: {project_path}")
        print(f"KML: {kml_path}")
        print(f"GEE Outbox: {config['gee_outbox']}")
        
        # Setup output structure
        output_dir = setup_output_structure(project_path, config['output_subfolder'])
        print(f"Output: {output_dir}")
        
        # Initialize GEE
        print("\n🔧 Initializing Google Earth Engine...")
        try:
            ee.Initialize()
            print("✅ GEE initialized successfully")
        except Exception as e:
            print(f"❌ GEE initialization failed: {e}")
            print("Please run: earthengine authenticate")
            return 1
        
        # Load boundary
        try:
            boundary = load_kml_boundary(kml_path, property_name)
            print("✅ Boundary loaded successfully")
            
            # Get boundary info
            bounds = boundary.geometry().bounds().getInfo()
            print(f"📍 Boundary bounds: {bounds}")
            
        except Exception as e:
            print(f"❌ Failed to load boundary: {e}")
            return 1
        
        # Process with GEE
        print(f"\n🚀 Starting GEE processing: {property_name}")
        processor = GEEProcessor(config)
        
        try:
            tasks, folder_name = processor.calculate_woody_masks(
                property_boundary=boundary,
                property_name=property_name,
                date_start=config['date_start'],
                date_end=config['date_end']
            )
            
            if not tasks:
                print("❌ No tasks created")
                return 1
            
            # Monitor and move files
            print(f"\n📊 Monitoring GEE tasks and moving files...")
            monitor = GEEFileMonitor(config)
            
            success = monitor.monitor_and_move_files(
                tasks=tasks,
                project_path=project_path,
                output_dir=output_dir,
                property_name=property_name
            )
            
            if success:
                print("\n" + "="*60)
                print("🎉 PROCESSING COMPLETE!")
                print("="*60)
                print(f"📁 Outputs saved to: {output_dir / 'woody_masks'}")
                print("📊 Generated files:")
                for method in ['Original', 'RefinedB', 'RefinedC', 'RefinedD', 'RefinedE']:
                    farm_name = property_name.replace('_', '')
                    current_timestamp = datetime.now().strftime('%Y%m%d')
                    print(f"  - Woody{method}_{farm_name}_{current_timestamp}.tif")
            else:
                print("❌ Processing failed or incomplete")
                return 1
        
        except Exception as e:
            print(f"❌ Processing failed: {e}")
            return 1
        
        print(f"\n⏰ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return 0
        
    except Exception as e:
        print(f"❌ Workflow failed: {e}")
        return 1

if __name__ == '__main__':
    exit(main())
