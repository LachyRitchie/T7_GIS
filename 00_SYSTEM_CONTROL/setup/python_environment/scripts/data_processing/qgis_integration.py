#!/usr/bin/env python3
"""
QGIS Integration Module for T7 Shield GIS Environment

This module provides utilities for integrating Python scripts with QGIS,
particularly useful for Australian forestry and carbon accounting workflows.

Author: T7 Shield GIS Environment
Version: 1.0
Date: 2025
"""

import os
import sys
from pathlib import Path
from typing import Optional, List, Dict, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class QGISEnvironment:
    """Manages QGIS environment initialization and cleanup."""
    
    def __init__(self):
        self.qgs = None
        self.processing = None
        self.initialized = False
    
    def initialize(self):
        """Initialize QGIS application for standalone scripts."""
        try:
            from qgis.core import QgsApplication, QgsProject
            import qgis.utils
            
            # Initialize QGIS Application
            QgsApplication.setPrefixPath('/opt/homebrew/Caskroom/miniconda/base/envs/t7_gis_professional', True)
            self.qgs = QgsApplication([], False)
            self.qgs.initQgis()
            
            # Initialize processing
            sys.path.append('/opt/homebrew/Caskroom/miniconda/base/envs/t7_gis_professional/share/qgis/python/plugins')
            from processing.core.Processing import Processing
            Processing.initialize()
            self.processing = Processing
            
            self.initialized = True
            logger.info("QGIS environment initialized successfully")
            return True
            
        except ImportError as e:
            logger.error(f"Failed to import QGIS modules: {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to initialize QGIS: {e}")
            return False
    
    def cleanup(self):
        """Clean up QGIS application."""
        if self.qgs and self.initialized:
            self.qgs.exitQgis()
            logger.info("QGIS environment cleaned up")
    
    def __enter__(self):
        """Context manager entry."""
        self.initialize()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.cleanup()


class AustralianCRS:
    """Common Australian coordinate reference systems."""
    
    GDA94_GEOGRAPHIC = 'EPSG:4283'
    GDA2020_GEOGRAPHIC = 'EPSG:7844'
    MGA_ZONE_50 = 'EPSG:28350'  # WA
    MGA_ZONE_51 = 'EPSG:28351'  # WA/NT
    MGA_ZONE_52 = 'EPSG:28352'  # NT/SA
    MGA_ZONE_53 = 'EPSG:28353'  # SA/QLD
    MGA_ZONE_54 = 'EPSG:28354'  # QLD/NSW
    MGA_ZONE_55 = 'EPSG:28355'  # NSW/VIC
    MGA_ZONE_56 = 'EPSG:28356'  # VIC/TAS
    
    @classmethod
    def get_mga_zone_for_longitude(cls, longitude: float) -> str:
        """Get MGA zone for given longitude."""
        zone_map = {
            range(114, 120): cls.MGA_ZONE_50,
            range(120, 126): cls.MGA_ZONE_51,
            range(126, 132): cls.MGA_ZONE_52,
            range(132, 138): cls.MGA_ZONE_53,
            range(138, 144): cls.MGA_ZONE_54,
            range(144, 150): cls.MGA_ZONE_55,
            range(150, 156): cls.MGA_ZONE_56,
        }
        
        for zone_range, epsg in zone_map.items():
            if longitude in zone_range:
                return epsg
        
        # Default to zone 55 if outside mapped range
        return cls.MGA_ZONE_55


def load_reference_data(layer_name: str, file_path: Union[str, Path]) -> Optional[object]:
    """
    Load reference data from T7 Shield reference data directory.
    
    Args:
        layer_name: Name for the layer
        file_path: Path to the data file relative to reference data directory
    
    Returns:
        QgsVectorLayer or QgsRasterLayer object, or None if failed
    """
    with QGISEnvironment() as qgis_env:
        if not qgis_env.initialized:
            return None
        
        from qgis.core import QgsVectorLayer, QgsRasterLayer, QgsProject
        
        # Construct full path
        reference_base = Path("/Volumes/T7 Shield/01_REFERENCE_DATA")
        full_path = reference_base / file_path
        
        if not full_path.exists():
            logger.error(f"Reference data file not found: {full_path}")
            return None
        
        # Determine layer type and create appropriate layer
        file_ext = full_path.suffix.lower()
        
        if file_ext in ['.shp', '.gpkg', '.geojson', '.kml']:
            layer = QgsVectorLayer(str(full_path), layer_name, "ogr")
        elif file_ext in ['.tif', '.tiff', '.img', '.asc']:
            layer = QgsRasterLayer(str(full_path), layer_name)
        else:
            logger.error(f"Unsupported file format: {file_ext}")
            return None
        
        if not layer.isValid():
            logger.error(f"Failed to load layer: {layer_name}")
            return None
        
        # Add to current project
        QgsProject.instance().addMapLayer(layer)
        logger.info(f"Successfully loaded layer: {layer_name}")
        
        return layer


def process_client_project_data(project_name: str, operation: str, **kwargs) -> bool:
    """
    Process client project data using QGIS algorithms.
    
    Args:
        project_name: Name of client project directory
        operation: Processing operation to perform
        **kwargs: Additional parameters for the operation
    
    Returns:
        True if successful, False otherwise
    """
    with QGISEnvironment() as qgis_env:
        if not qgis_env.initialized:
            return False
        
        import processing
        from qgis.core import QgsProject
        
        project_base = Path(f"/Volumes/T7 Shield/02_CLIENT_PROJECTS/{project_name}")
        
        if not project_base.exists():
            logger.error(f"Client project directory not found: {project_base}")
            return False
        
        try:
            if operation == 'buffer_analysis':
                # Example buffer analysis for forest boundaries
                input_layer = kwargs.get('input_layer')
                buffer_distance = kwargs.get('buffer_distance', 100)
                output_path = project_base / f"{project_name}_buffered.gpkg"
                
                result = processing.run("native:buffer", {
                    'INPUT': input_layer,
                    'DISTANCE': buffer_distance,
                    'SEGMENTS': 10,
                    'OUTPUT': str(output_path)
                })
                
                logger.info(f"Buffer analysis completed: {output_path}")
                return True
                
            elif operation == 'clip_raster':
                # Clip raster data to project boundary
                raster_path = kwargs.get('raster_path')
                boundary_path = kwargs.get('boundary_path')
                output_path = project_base / f"{project_name}_clipped.tif"
                
                result = processing.run("gdal:cliprasterbymasklayer", {
                    'INPUT': raster_path,
                    'MASK': boundary_path,
                    'OUTPUT': str(output_path)
                })
                
                logger.info(f"Raster clipping completed: {output_path}")
                return True
            
            else:
                logger.error(f"Unknown operation: {operation}")
                return False
                
        except Exception as e:
            logger.error(f"Processing failed: {e}")
            return False


def export_for_fullcam(project_data: Dict, output_format: str = 'csv') -> Optional[Path]:
    """
    Export processed data in format suitable for FullCAM input.
    
    Args:
        project_data: Dictionary containing project information
        output_format: Output format ('csv', 'xlsx')
    
    Returns:
        Path to exported file, or None if failed
    """
    try:
        import pandas as pd
        from datetime import datetime
        
        # Create output directory
        output_dir = Path("/Volumes/T7 Shield/10_PYTHON_ENVIRONMENT/exports")
        output_dir.mkdir(exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"fullcam_export_{timestamp}.{output_format}"
        output_path = output_dir / filename
        
        # Convert to DataFrame
        df = pd.DataFrame(project_data)
        
        # Export based on format
        if output_format == 'csv':
            df.to_csv(output_path, index=False)
        elif output_format == 'xlsx':
            df.to_excel(output_path, index=False)
        else:
            logger.error(f"Unsupported output format: {output_format}")
            return None
        
        logger.info(f"FullCAM export completed: {output_path}")
        return output_path
        
    except Exception as e:
        logger.error(f"Export failed: {e}")
        return None


def main():
    """Example usage of the QGIS integration module."""
    print("T7 Shield QGIS Integration Module")
    print("=================================")
    
    # Test QGIS environment initialization
    with QGISEnvironment() as qgis_env:
        if qgis_env.initialized:
            print("✓ QGIS environment initialized successfully")
            
            # Example: Load state boundaries
            layer = load_reference_data(
                "Australian States", 
                "BOUNDARIES/STATE_BOUNDARIES/STE_2021_AUST_GDA2020.shp"
            )
            
            if layer:
                print(f"✓ Loaded reference layer with {layer.featureCount()} features")
            
            # Example: Get MGA zone for Perth (longitude ~115.8)
            mga_zone = AustralianCRS.get_mga_zone_for_longitude(115.8)
            print(f"✓ MGA zone for Perth: {mga_zone}")
            
        else:
            print("✗ Failed to initialize QGIS environment")


if __name__ == "__main__":
    main()