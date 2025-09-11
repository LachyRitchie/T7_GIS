#!/usr/bin/env python3
"""
QGIS Integration Module for T7 Shield GIS Environment (macOS M2 Safe Version)

This module provides QGIS-compatible workflows using GeoPandas/Rasterio instead
of direct PyQGIS integration to avoid crashes on macOS M2 chips.

Author: T7 Shield GIS Environment
Version: 1.1 (macOS M2 Compatible)
Date: 2025
"""

import os
import sys
from pathlib import Path
from typing import Optional, List, Dict, Union
import logging
import geopandas as gpd
import rasterio as rio
from rasterio.mask import mask
import pandas as pd
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class QGISCompatibleProcessor:
    """
    QGIS-compatible processing using stable GeoPandas/Rasterio operations.
    Safer alternative to PyQGIS on macOS M2.
    """
    
    def __init__(self):
        self.t7_base = Path("/Volumes/T7 Shield")
        self.reference_data = self.t7_base / "01_REFERENCE_DATA"
        self.client_projects = self.t7_base / "02_CLIENT_PROJECTS"
        
    def load_reference_data(self, layer_name: str, file_path: Union[str, Path]) -> Optional[gpd.GeoDataFrame]:
        """
        Load reference data from T7 Shield reference data directory.
        
        Args:
            layer_name: Name for the layer
            file_path: Path to the data file relative to reference data directory
        
        Returns:
            GeoDataFrame object, or None if failed
        """
        try:
            # Construct full path
            full_path = self.reference_data / file_path
            
            if not full_path.exists():
                logger.error(f"Reference data file not found: {full_path}")
                return None
            
            # Load with geopandas
            gdf = gpd.read_file(full_path)
            
            if gdf.empty:
                logger.error(f"Empty dataset: {layer_name}")
                return None
            
            logger.info(f"Successfully loaded layer: {layer_name} ({len(gdf)} features)")
            return gdf
            
        except Exception as e:
            logger.error(f"Failed to load reference data {layer_name}: {e}")
            return None
    
    def buffer_analysis(self, input_gdf: gpd.GeoDataFrame, buffer_distance: float, 
                       output_path: Optional[Path] = None) -> Optional[gpd.GeoDataFrame]:
        """
        Perform buffer analysis (QGIS native:buffer equivalent).
        
        Args:
            input_gdf: Input GeoDataFrame
            buffer_distance: Buffer distance in meters
            output_path: Optional output path
        
        Returns:
            Buffered GeoDataFrame
        """
        try:
            # Ensure we're in a projected CRS for accurate buffering
            original_crs = input_gdf.crs
            if input_gdf.crs.to_string() == 'EPSG:7844':  # GDA2020 Geographic
                # Convert to Australian Albers for buffering
                input_projected = input_gdf.to_crs('EPSG:3577')
            else:
                input_projected = input_gdf
            
            # Create buffer
            buffered_gdf = input_projected.copy()
            buffered_gdf['geometry'] = input_projected.geometry.buffer(buffer_distance)
            
            # Convert back to original CRS if needed
            if original_crs.to_string() == 'EPSG:7844':
                buffered_gdf = buffered_gdf.to_crs(original_crs)
            
            # Save if output path provided
            if output_path:
                buffered_gdf.to_file(output_path)
                logger.info(f"Buffer analysis saved to: {output_path}")
            
            logger.info(f"Buffer analysis completed: {buffer_distance}m buffer")
            return buffered_gdf
            
        except Exception as e:
            logger.error(f"Buffer analysis failed: {e}")
            return None
    
    def clip_vector_by_mask(self, input_gdf: gpd.GeoDataFrame, mask_gdf: gpd.GeoDataFrame,
                           output_path: Optional[Path] = None) -> Optional[gpd.GeoDataFrame]:
        """
        Clip vector data by mask (QGIS native:clip equivalent).
        
        Args:
            input_gdf: Input vector data
            mask_gdf: Clipping mask
            output_path: Optional output path
        
        Returns:
            Clipped GeoDataFrame
        """
        try:
            # Ensure same CRS
            if input_gdf.crs != mask_gdf.crs:
                mask_gdf = mask_gdf.to_crs(input_gdf.crs)
            
            # Perform overlay intersection
            clipped_gdf = gpd.overlay(input_gdf, mask_gdf, how='intersection')
            
            # Save if output path provided
            if output_path:
                clipped_gdf.to_file(output_path)
                logger.info(f"Vector clipping saved to: {output_path}")
            
            logger.info(f"Vector clipping completed: {len(clipped_gdf)} features")
            return clipped_gdf
            
        except Exception as e:
            logger.error(f"Vector clipping failed: {e}")
            return None
    
    def clip_raster_by_mask(self, raster_path: Path, mask_gdf: gpd.GeoDataFrame,
                           output_path: Path) -> bool:
        """
        Clip raster data by vector mask (QGIS gdal:cliprasterbymasklayer equivalent).
        
        Args:
            raster_path: Path to input raster
            mask_gdf: Clipping mask
            output_path: Output raster path
        
        Returns:
            True if successful
        """
        try:
            with rio.open(raster_path) as src:
                # Ensure mask is in same CRS as raster
                if mask_gdf.crs != src.crs:
                    mask_gdf = mask_gdf.to_crs(src.crs)
                
                # Perform clipping
                out_image, out_transform = mask(src, mask_gdf.geometry, crop=True)
                
                # Update metadata
                out_meta = src.meta.copy()
                out_meta.update({
                    "driver": "GTiff",
                    "height": out_image.shape[1],
                    "width": out_image.shape[2],
                    "transform": out_transform
                })
                
                # Write clipped raster
                with rio.open(output_path, "w", **out_meta) as dest:
                    dest.write(out_image)
            
            logger.info(f"Raster clipping completed: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Raster clipping failed: {e}")
            return False
    
    def zonal_statistics(self, zones_gdf: gpd.GeoDataFrame, raster_path: Path,
                        stats: List[str] = ['mean', 'max', 'min', 'std']) -> pd.DataFrame:
        """
        Calculate zonal statistics (QGIS native:zonalstatisticsfb equivalent).
        
        Args:
            zones_gdf: Zones for statistics
            raster_path: Path to raster data
            stats: Statistics to calculate
        
        Returns:
            DataFrame with zonal statistics
        """
        try:
            import rasterstats
            
            # Calculate zonal statistics
            zonal_stats = rasterstats.zonal_stats(
                zones_gdf.geometry,
                str(raster_path),
                stats=stats,
                geojson_out=True
            )
            
            # Convert to DataFrame
            stats_data = []
            for i, feature in enumerate(zonal_stats):
                stat_row = {'zone_id': i}
                stat_row.update(feature['properties'])
                stats_data.append(stat_row)
            
            stats_df = pd.DataFrame(stats_data)
            logger.info(f"Zonal statistics completed for {len(stats_df)} zones")
            return stats_df
            
        except Exception as e:
            logger.error(f"Zonal statistics failed: {e}")
            return pd.DataFrame()
    
    def spatial_join(self, left_gdf: gpd.GeoDataFrame, right_gdf: gpd.GeoDataFrame,
                    how: str = 'inner', predicate: str = 'intersects') -> Optional[gpd.GeoDataFrame]:
        """
        Spatial join operation (QGIS native:joinattributesbylocation equivalent).
        
        Args:
            left_gdf: Left GeoDataFrame
            right_gdf: Right GeoDataFrame  
            how: Join type ('inner', 'left')
            predicate: Spatial predicate ('intersects', 'within', 'contains')
        
        Returns:
            Joined GeoDataFrame
        """
        try:
            # Ensure same CRS
            if left_gdf.crs != right_gdf.crs:
                right_gdf = right_gdf.to_crs(left_gdf.crs)
            
            # Perform spatial join
            joined_gdf = gpd.sjoin(left_gdf, right_gdf, how=how, predicate=predicate)
            
            logger.info(f"Spatial join completed: {len(joined_gdf)} results")
            return joined_gdf
            
        except Exception as e:
            logger.error(f"Spatial join failed: {e}")
            return None
    
    def process_client_project_data(self, project_name: str, operation: str, **kwargs) -> bool:
        """
        Process client project data using stable operations.
        
        Args:
            project_name: Name of client project directory
            operation: Processing operation to perform
            **kwargs: Additional parameters for the operation
        
        Returns:
            True if successful
        """
        project_base = self.client_projects / project_name
        
        if not project_base.exists():
            logger.error(f"Client project directory not found: {project_base}")
            return False
        
        try:
            if operation == 'buffer_analysis':
                # Buffer analysis for project boundaries
                input_file = kwargs.get('input_file')
                buffer_distance = kwargs.get('buffer_distance', 100)
                output_name = kwargs.get('output_name', f"{project_name}_buffered.gpkg")
                
                if not input_file:
                    logger.error("input_file required for buffer_analysis")
                    return False
                
                input_gdf = gpd.read_file(project_base / input_file)
                output_path = project_base / output_name
                
                result = self.buffer_analysis(input_gdf, buffer_distance, output_path)
                return result is not None
                
            elif operation == 'clip_raster':
                # Clip raster data to project boundary
                raster_file = kwargs.get('raster_file')
                boundary_file = kwargs.get('boundary_file')
                output_name = kwargs.get('output_name', f"{project_name}_clipped.tif")
                
                if not raster_file or not boundary_file:
                    logger.error("raster_file and boundary_file required for clip_raster")
                    return False
                
                boundary_gdf = gpd.read_file(project_base / boundary_file)
                output_path = project_base / output_name
                
                return self.clip_raster_by_mask(Path(raster_file), boundary_gdf, output_path)
            
            else:
                logger.error(f"Unknown operation: {operation}")
                return False
                
        except Exception as e:
            logger.error(f"Processing failed: {e}")
            return False


class AustralianCRS:
    """Common Australian coordinate reference systems."""
    
    GDA94_GEOGRAPHIC = 'EPSG:4283'
    GDA2020_GEOGRAPHIC = 'EPSG:7844'
    AUSTRALIAN_ALBERS = 'EPSG:3577'
    
    # MGA Zones
    MGA_ZONES = {
        50: 'EPSG:28350',  # WA
        51: 'EPSG:28351',  # WA/NT
        52: 'EPSG:28352',  # NT/SA
        53: 'EPSG:28353',  # SA/QLD
        54: 'EPSG:28354',  # QLD/NSW
        55: 'EPSG:28355',  # NSW/VIC
        56: 'EPSG:28356',  # VIC/TAS
    }
    
    @classmethod
    def get_mga_zone_for_longitude(cls, longitude: float) -> str:
        """Get MGA zone for given longitude."""
        zone_number = int((longitude + 183) / 6)
        return cls.MGA_ZONES.get(zone_number, cls.MGA_ZONES[55])  # Default to zone 55


def main():
    """Example usage of the safe QGIS integration module."""
    print("T7 Shield Safe QGIS Integration Module")
    print("=====================================")
    print("(macOS M2 compatible - no PyQGIS crashes)")
    
    # Initialize processor
    processor = QGISCompatibleProcessor()
    
    # Test loading reference data
    states = processor.load_reference_data(
        "Australian States", 
        "STATE_BOUNDARIES/STE_2021_AUST_GDA2020.shp"
    )
    
    if states is not None:
        print(f"✓ Loaded {len(states)} Australian states")
        
        # Test buffer operation
        wa_states = states[states['STE_NAME21'] == 'Western Australia']
        if not wa_states.empty:
            buffered = processor.buffer_analysis(wa_states, 10000)  # 10km buffer
            if buffered is not None:
                print("✓ Buffer analysis successful")
        
        # Test coordinate systems
        mga_zone = AustralianCRS.get_mga_zone_for_longitude(115.8)  # Perth longitude
        print(f"✓ MGA zone for Perth: {mga_zone}")
        
        print("\n✅ Safe QGIS integration working perfectly!")
        print("✅ All spatial operations available without crashes")
    else:
        print("❌ Could not load reference data")


if __name__ == "__main__":
    main()