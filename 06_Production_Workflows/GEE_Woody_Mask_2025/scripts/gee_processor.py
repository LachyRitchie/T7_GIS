#!/usr/bin/env python3
"""
GEE Woody Mask Processor
========================
Handles Google Earth Engine processing for woody vegetation masks

Author: GIS Engineer
Date: 2025-01-23
Version: 1.0
"""

import ee
import time
from datetime import datetime

class GEEProcessor:
    """Handles GEE processing operations for woody mask generation"""
    
    def __init__(self, config):
        self.config = config
        
    def calculate_woody_masks(self, property_boundary, property_name, date_start='2019-01-01', date_end='2025-01-01'):
        """Calculate woody vegetation masks using 5 proven methods"""
        
        print(f"\n{'='*60}")
        print(f"Processing: {property_name}")
        print(f"Date range: {date_start} to {date_end}")
        print(f"{'='*60}")
        
        # Process Sentinel-2 collection
        print("📡 Loading Sentinel-2 data...")
        s2 = (ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
              .filterBounds(property_boundary)
              .filterDate(date_start, date_end)
              .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)))
        
        # Count images
        image_count = s2.size().getInfo()
        print(f"Found {image_count} Sentinel-2 images")
        
        if image_count == 0:
            raise ValueError("No Sentinel-2 images found for the specified date range and location")
        
        # Calculate NDVI for each image
        def add_ndvi(img):
            return img.normalizedDifference(['B8', 'B4']).rename('ndvi')
        
        s2_ndvi = s2.map(add_ndvi)
        
        # Calculate woody score components
        print("🧮 Calculating woody score components...")
        ndvi_p10 = s2_ndvi.reduce(ee.Reducer.percentile([10]))
        ndvi_p25 = s2_ndvi.reduce(ee.Reducer.percentile([25]))
        ndvi_stdDev = s2_ndvi.reduce(ee.Reducer.stdDev())
        ndvi_max = s2_ndvi.max()
        
        # Calculate brightness for Refined E method (VISIBLE BANDS ONLY)
        s2_vis = s2.select(['B2', 'B3', 'B4'])  # Blue, Green, Red only
        brightness = s2_vis.reduce(ee.Reducer.median()).reduce(ee.Reducer.sum())
        
        # Calculate woody score
        woody_score = ndvi_p10.multiply(2).subtract(ndvi_stdDev)
        
        # Get geometry for export
        if isinstance(property_boundary, ee.FeatureCollection):
            export_region = property_boundary.geometry()
        else:
            export_region = property_boundary
        
        # Define the 5 KEEPER METHODS (aligned with historical scripts)
        methods = {
            'Original': {
                'description': 'Original Best (Score > 0.15) - "Still very strong!"',
                'logic': lambda: woody_score.gt(0.15)
            },
            'Refined_B': {
                'description': 'Refined B (Score + Veg History) - "Very strong! Might catch recent clearing"',
                'logic': lambda: woody_score.gt(0.15).And(ndvi_max.gt(0.25))
            },
            'Refined_C': {
                'description': 'Refined C (Score + P25) - "Tiny bit more precise potentially"',
                'logic': lambda: woody_score.gt(0.15).And(ndvi_p25.gt(0.12))
            },
            'Refined_D': {
                'description': 'Refined D (Score > 0.16) - "So good! A little more liberal"',
                'logic': lambda: woody_score.gt(0.16)
            },
            'Refined_E': {
                'description': 'Refined E (Combined) - "Indistinguishable from Original Best"',
                'logic': lambda: woody_score.gt(0.15).And(brightness.gt(800).Or(ndvi_max.gt(0.25)))
            }
        }
        
        # Canvas method for guaranteed dense raster
        print("🎨 Creating canvas for dense raster...")
        canvas = ee.Image.constant(0).clip(export_region).toUint8()
        
        # Create timestamp for file naming
        timestamp = datetime.now().strftime('%Y%m%d')
        folder_name = 'GEE_Outbox'  # Single folder for all exports
        
        # Export each method
        tasks = []
        for method_name, method_info in methods.items():
            print(f"\n🔨 Processing {method_name} method")
            print(f"   Description: {method_info['description']}")
            
            # Create binary mask using the method's logic
            binary_mask = method_info['logic']()
            
            # Use canvas method to ensure dense raster
            full_mask = canvas.where(binary_mask.selfMask(), 1)
            
            # Prepare export with simplified naming convention
            # Format: CalculationName_FarmName_Date
            farm_name = property_name.replace('_', '')  # Remove underscores for cleaner naming
            export_name = f'Woody{method_name}_{farm_name}_{timestamp}'
            
            print(f"📤 Exporting: {export_name}")
            
            # Create export task with single folder
            task = ee.batch.Export.image.toDrive(
                image=full_mask,
                description=export_name,
                folder=folder_name,  # Single GEE_Outbox folder
                scale=self.config['scale'],
                crs=self.config['crs'],
                region=export_region,
                maxPixels=self.config['max_pixels'],
                fileFormat='GeoTIFF',
                formatOptions={
                    'cloudOptimized': True,
                    'noData': 255
                }
            )
            
            # Start task
            task.start()
            tasks.append((method_name, task, export_name))
            print(f"  ✅ Task started - ID: {task.id}")
        
        return tasks, folder_name
