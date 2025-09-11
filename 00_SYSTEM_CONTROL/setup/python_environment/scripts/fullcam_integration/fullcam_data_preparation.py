#!/usr/bin/env python3
"""
FullCAM Data Preparation Module for T7 Shield GIS Environment

This module provides utilities for preparing spatial data for FullCAM input
and processing FullCAM outputs for Australian forestry and carbon accounting.

IMPORTANT: FullCAM is a Windows-only .exe application that runs on AWS WorkSpaces.
This module prepares data for transfer to the Windows environment and processes
outputs returned from FullCAM analysis.

Author: T7 Shield GIS Environment
Version: 1.0
Date: 2025
"""

import pandas as pd
import geopandas as gpd
import rasterio as rio
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from datetime import datetime
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FullCAMDataProcessor:
    """Main class for FullCAM data preparation and analysis."""
    
    def __init__(self, t7_shield_base: str = "/Volumes/T7 Shield"):
        self.t7_base = Path(t7_shield_base)
        self.reference_data = self.t7_base / "01_REFERENCE_DATA"
        self.client_projects = self.t7_base / "02_CLIENT_PROJECTS"
        self.fullcam_docs = self.t7_base / "08_KNOWLEDGE BASE" / "fullcam-docs"
        
        # FullCAM method specifications
        self.fullcam_methods = {
            'environmental_plantings': {
                'determination': 'EP2024',
                'min_area_ha': 0.2,
                'max_area_ha': 10000,
                'required_fields': ['species', 'planting_year', 'area_ha', 'soil_type', 'rainfall_mm']
            },
            'plantation_forestry': {
                'determination': 'PF2022',
                'min_area_ha': 2.0,
                'max_area_ha': 50000,
                'required_fields': ['species', 'establishment_year', 'area_ha', 'management_regime']
            }
        }
    
    def validate_project_boundaries(self, boundary_file: Union[str, Path], 
                                  method: str = 'environmental_plantings') -> Dict:
        """
        Validate project boundaries against FullCAM requirements.
        
        Args:
            boundary_file: Path to boundary shapefile or geopackage
            method: FullCAM method ('environmental_plantings' or 'plantation_forestry')
        
        Returns:
            Dictionary with validation results
        """
        try:
            # Load boundary data
            gdf = gpd.read_file(boundary_file)
            
            # Ensure correct CRS (GDA2020 geographic)
            if gdf.crs != 'EPSG:7844':
                logger.info(f"Reprojecting from {gdf.crs} to GDA2020 (EPSG:7844)")
                gdf = gdf.to_crs('EPSG:7844')
            
            # Calculate areas in hectares
            gdf_projected = gdf.to_crs('EPSG:3577')  # Australian Albers for area calculation
            gdf['area_ha'] = gdf_projected.geometry.area / 10000
            
            # Validate against method requirements
            method_spec = self.fullcam_methods.get(method, {})
            min_area = method_spec.get('min_area_ha', 0.2)
            max_area = method_spec.get('max_area_ha', 10000)
            
            validation_results = {
                'total_features': len(gdf),
                'total_area_ha': gdf['area_ha'].sum(),
                'min_feature_area_ha': gdf['area_ha'].min(),
                'max_feature_area_ha': gdf['area_ha'].max(),
                'valid_features': 0,
                'invalid_features': [],
                'crs': str(gdf.crs),
                'method': method,
                'determination': method_spec.get('determination', 'Unknown')
            }
            
            # Check individual features
            for idx, row in gdf.iterrows():
                feature_area = row['area_ha']
                if min_area <= feature_area <= max_area:
                    validation_results['valid_features'] += 1
                else:
                    validation_results['invalid_features'].append({
                        'feature_id': idx,
                        'area_ha': feature_area,
                        'issue': f"Area {feature_area:.2f} ha outside valid range ({min_area}-{max_area} ha)"
                    })
            
            logger.info(f"Validation completed: {validation_results['valid_features']}/{validation_results['total_features']} features valid")
            return validation_results
            
        except Exception as e:
            logger.error(f"Boundary validation failed: {e}")
            return {'error': str(e)}
    
    def extract_reference_data_for_project(self, project_boundary: Union[str, Path], 
                                         output_dir: Optional[Path] = None) -> Dict:
        """
        Extract relevant reference data for a project area.
        
        Args:
            project_boundary: Path to project boundary file
            output_dir: Directory to save extracted data (optional)
        
        Returns:
            Dictionary with paths to extracted reference data
        """
        try:
            # Load project boundary
            boundary_gdf = gpd.read_file(project_boundary)
            if boundary_gdf.crs != 'EPSG:7844':
                boundary_gdf = boundary_gdf.to_crs('EPSG:7844')
            
            # Create output directory if not provided
            if output_dir is None:
                output_dir = Path(project_boundary).parent / "extracted_reference_data"
            output_dir.mkdir(exist_ok=True)
            
            extracted_data = {}
            
            # Extract soil data (Australian Soil Classification)
            soil_path = self.reference_data / "SOIL/AUSTRALIAN_SOIL_CLASSIFICATION/ASC_EV_C_P_AU_TRN_N.cog.tif"
            if soil_path.exists():
                soil_output = output_dir / "soil_classification_clipped.tif"
                self._clip_raster_to_boundary(soil_path, boundary_gdf, soil_output)
                extracted_data['soil_classification'] = soil_output
            
            # Extract rainfall data
            rainfall_path = self.reference_data / "CLIMATE/RAINFALL_LTA/LTA_rainfall.tif"
            if rainfall_path.exists():
                rainfall_output = output_dir / "rainfall_lta_clipped.tif"
                self._clip_raster_to_boundary(rainfall_path, boundary_gdf, rainfall_output)
                extracted_data['rainfall_lta'] = rainfall_output
            
            # Extract vegetation data (Pre-1750 Major Vegetation Groups)
            vegetation_path = self.reference_data / "VEGETATION/VEGETATION_GROUPS_PRE1750_MVG"
            if vegetation_path.exists():
                # Look for the main vegetation file
                for veg_file in vegetation_path.glob("*.tif"):
                    if "mvg" in veg_file.name.lower():
                        veg_output = output_dir / "vegetation_pre1750_clipped.tif"
                        self._clip_raster_to_boundary(veg_file, boundary_gdf, veg_output)
                        extracted_data['vegetation_pre1750'] = veg_output
                        break
            
            # Extract IBRA bioregions
            ibra_path = self.reference_data / "BOUNDARIES/BIOREGIONS_IBRA/IBRA7_subregions.shp"
            if ibra_path.exists():
                ibra_output = output_dir / "ibra_subregions_clipped.gpkg"
                self._clip_vector_to_boundary(ibra_path, boundary_gdf, ibra_output)
                extracted_data['ibra_subregions'] = ibra_output
            
            logger.info(f"Extracted {len(extracted_data)} reference datasets to {output_dir}")
            return extracted_data
            
        except Exception as e:
            logger.error(f"Reference data extraction failed: {e}")
            return {'error': str(e)}
    
    def prepare_species_data(self, species_list: List[str], method: str = 'environmental_plantings') -> pd.DataFrame:
        """
        Prepare species data with FullCAM-compatible parameters.
        
        Args:
            species_list: List of species names
            method: FullCAM method type
        
        Returns:
            DataFrame with species parameters
        """
        # Common Australian forestry species with typical FullCAM parameters
        species_parameters = {
            'Eucalyptus globulus': {
                'common_name': 'Tasmanian Blue Gum',
                'growth_rate': 'fast',
                'max_height_m': 60,
                'wood_density': 0.69,
                'suitable_regions': ['Tasmania', 'Victoria', 'South Australia', 'Western Australia']
            },
            'Eucalyptus camaldulensis': {
                'common_name': 'River Red Gum',
                'growth_rate': 'medium',
                'max_height_m': 45,
                'wood_density': 0.75,
                'suitable_regions': ['All mainland states']
            },
            'Pinus radiata': {
                'common_name': 'Monterey Pine',
                'growth_rate': 'fast',
                'max_height_m': 40,
                'wood_density': 0.42,
                'suitable_regions': ['Tasmania', 'Victoria', 'South Australia', 'Western Australia']
            },
            'Acacia melanoxylon': {
                'common_name': 'Blackwood',
                'growth_rate': 'medium',
                'max_height_m': 30,
                'wood_density': 0.64,
                'suitable_regions': ['Tasmania', 'Victoria', 'New South Wales']
            }
        }
        
        species_data = []
        for species in species_list:
            if species in species_parameters:
                data = species_parameters[species].copy()
                data['scientific_name'] = species
                data['fullcam_compatible'] = True
            else:
                # Default parameters for unlisted species
                data = {
                    'scientific_name': species,
                    'common_name': 'Unknown',
                    'growth_rate': 'medium',
                    'max_height_m': 25,
                    'wood_density': 0.55,
                    'suitable_regions': ['Check local suitability'],
                    'fullcam_compatible': False
                }
            
            species_data.append(data)
        
        return pd.DataFrame(species_data)
    
    def generate_fullcam_input_file(self, project_data: Dict, output_path: Optional[Path] = None) -> Path:
        """
        Generate FullCAM-compatible input file from project data.
        
        Args:
            project_data: Dictionary containing project information
            output_path: Path for output file (optional)
        
        Returns:
            Path to generated input file
        """
        try:
            if output_path is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = self.t7_base / f"10_PYTHON_ENVIRONMENT/exports/fullcam_input_{timestamp}.xlsx"
                output_path.parent.mkdir(exist_ok=True)
            
            # Create FullCAM input structure
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                
                # Project summary sheet
                summary_data = {
                    'Parameter': [
                        'Project Name', 'Method', 'Determination', 'Total Area (ha)',
                        'Number of Plots', 'Establishment Year', 'Crediting Period'
                    ],
                    'Value': [
                        project_data.get('name', 'Unknown'),
                        project_data.get('method', 'environmental_plantings'),
                        project_data.get('determination', 'EP2024'),
                        project_data.get('total_area_ha', 0),
                        project_data.get('num_plots', 1),
                        project_data.get('establishment_year', datetime.now().year),
                        project_data.get('crediting_period', 25)
                    ]
                }
                pd.DataFrame(summary_data).to_excel(writer, sheet_name='Project_Summary', index=False)
                
                # Plot details sheet
                plot_data = project_data.get('plots', [])
                if plot_data:
                    pd.DataFrame(plot_data).to_excel(writer, sheet_name='Plot_Details', index=False)
                
                # Species composition sheet
                species_data = project_data.get('species', [])
                if species_data:
                    pd.DataFrame(species_data).to_excel(writer, sheet_name='Species_Composition', index=False)
                
                # Site conditions sheet
                site_data = project_data.get('site_conditions', {})
                if site_data:
                    site_df = pd.DataFrame([site_data])
                    site_df.to_excel(writer, sheet_name='Site_Conditions', index=False)
            
            logger.info(f"FullCAM input file generated: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"FullCAM input generation failed: {e}")
            raise
    
    def analyze_carbon_potential(self, project_boundary: Union[str, Path], 
                               species: str = 'Eucalyptus globulus') -> Dict:
        """
        Analyze carbon sequestration potential for a project area.
        
        Args:
            project_boundary: Path to project boundary file
            species: Primary species for analysis
        
        Returns:
            Dictionary with carbon potential analysis
        """
        try:
            # Load project boundary
            boundary_gdf = gpd.read_file(project_boundary)
            if boundary_gdf.crs != 'EPSG:7844':
                boundary_gdf = boundary_gdf.to_crs('EPSG:7844')
            
            # Calculate total area
            boundary_projected = boundary_gdf.to_crs('EPSG:3577')
            total_area_ha = boundary_projected.geometry.area.sum() / 10000
            
            # Get species parameters
            species_df = self.prepare_species_data([species])
            species_params = species_df.iloc[0]
            
            # Load Forest Productivity Index if available
            fpi_path = self.reference_data / "BIOMASS_NATIONAL/SITE_POTENTIAL_FPI_V2/fpi_lta_2019.tif"
            
            productivity_factor = 1.0  # Default
            if fpi_path.exists():
                try:
                    # Extract FPI values for project area
                    with rio.open(fpi_path) as src:
                        # Get bounds of project area
                        bounds = boundary_gdf.total_bounds
                        
                        # Read FPI data for project area
                        window = rio.windows.from_bounds(*bounds, src.transform)
                        fpi_data = src.read(1, window=window)
                        
                        # Calculate mean productivity (excluding nodata)
                        valid_fpi = fpi_data[fpi_data != src.nodata]
                        if len(valid_fpi) > 0:
                            productivity_factor = np.mean(valid_fpi) / 100  # Convert percentage to factor
                
                except Exception as e:
                    logger.warning(f"Could not extract FPI data: {e}")
            
            # Estimate carbon sequestration potential
            # These are simplified estimates - actual FullCAM modeling required for precise values
            base_sequestration_rate = {
                'fast': 8.5,    # tCO2-e/ha/year for fast-growing species
                'medium': 6.0,  # tCO2-e/ha/year for medium-growing species
                'slow': 3.5     # tCO2-e/ha/year for slow-growing species
            }
            
            growth_rate = species_params.get('growth_rate', 'medium')
            annual_rate = base_sequestration_rate[growth_rate] * productivity_factor
            
            # Calculate totals for typical crediting period
            crediting_period = 25  # years
            total_sequestration = total_area_ha * annual_rate * crediting_period
            
            analysis_results = {
                'project_area_ha': round(total_area_ha, 2),
                'species': species,
                'growth_rate': growth_rate,
                'productivity_factor': round(productivity_factor, 3),
                'annual_sequestration_rate_per_ha': round(annual_rate, 2),
                'total_annual_sequestration_tco2e': round(total_area_ha * annual_rate, 2),
                'crediting_period_years': crediting_period,
                'total_potential_sequestration_tco2e': round(total_sequestration, 2),
                'analysis_date': datetime.now().isoformat(),
                'notes': [
                    'These are preliminary estimates only',
                    'Actual FullCAM modeling required for precise carbon accounting',
                    'Results depend on site-specific conditions and management practices'
                ]
            }
            
            logger.info(f"Carbon potential analysis completed for {total_area_ha:.2f} ha")
            return analysis_results
            
        except Exception as e:
            logger.error(f"Carbon potential analysis failed: {e}")
            return {'error': str(e)}
    
    def _clip_raster_to_boundary(self, raster_path: Path, boundary_gdf: gpd.GeoDataFrame, 
                                output_path: Path) -> bool:
        """Clip raster data to project boundary."""
        try:
            from rasterio.mask import mask
            
            # Ensure boundary is in same CRS as raster
            with rio.open(raster_path) as src:
                raster_crs = src.crs
                if boundary_gdf.crs != raster_crs:
                    boundary_gdf = boundary_gdf.to_crs(raster_crs)
                
                # Perform clipping
                out_image, out_transform = mask(src, boundary_gdf.geometry, crop=True)
                
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
                
                return True
                
        except Exception as e:
            logger.error(f"Raster clipping failed: {e}")
            return False
    
    def _clip_vector_to_boundary(self, vector_path: Path, boundary_gdf: gpd.GeoDataFrame,
                                output_path: Path) -> bool:
        """Clip vector data to project boundary."""
        try:
            # Load vector data
            vector_gdf = gpd.read_file(vector_path)
            
            # Ensure same CRS
            if vector_gdf.crs != boundary_gdf.crs:
                vector_gdf = vector_gdf.to_crs(boundary_gdf.crs)
            
            # Perform spatial intersection
            clipped_gdf = gpd.overlay(vector_gdf, boundary_gdf, how='intersection')
            
            # Save result
            clipped_gdf.to_file(output_path, driver='GPKG')
            
            return True
            
        except Exception as e:
            logger.error(f"Vector clipping failed: {e}")
            return False


def main():
    """Example usage of FullCAM data preparation tools."""
    print("T7 Shield FullCAM Data Preparation Module")
    print("========================================")
    
    # Initialize processor
    processor = FullCAMDataProcessor()
    
    print(f"✓ T7 Shield base: {processor.t7_base}")
    print(f"✓ Reference data: {processor.reference_data}")
    print(f"✓ FullCAM docs: {processor.fullcam_docs}")
    
    # Example: Prepare species data
    test_species = ['Eucalyptus globulus', 'Pinus radiata', 'Unknown species']
    species_df = processor.prepare_species_data(test_species)
    print(f"✓ Prepared data for {len(species_df)} species")
    
    # Show available FullCAM methods
    print("\nAvailable FullCAM methods:")
    for method, details in processor.fullcam_methods.items():
        print(f"  - {method}: {details['determination']}")


if __name__ == "__main__":
    main()