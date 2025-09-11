#!/usr/bin/env python3
"""
AWS WorkSpaces FullCAM Data Transfer Module

This module manages data preparation and transfer for FullCAM analysis via AWS WorkSpaces.
Since FullCAM is a Windows-only .exe application and you're using macOS with M2 chip,
this provides workflows for preparing data packages for AWS WorkSpaces transfer.

Workflow:
1. Prepare data on T7 Shield (macOS)
2. Package for AWS WorkSpaces transfer
3. Process FullCAM outputs when returned

Author: T7 Shield GIS Environment
Version: 1.0  
Date: 2025
"""

import pandas as pd
import geopandas as gpd
import zipfile
import shutil
import json
from pathlib import Path
from typing import Dict, List, Optional, Union
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AWSWorkSpacesTransfer:
    """Manages data preparation and transfer for AWS WorkSpaces FullCAM analysis."""
    
    def __init__(self, t7_shield_base: str = "/Volumes/T7 Shield"):
        self.t7_base = Path(t7_shield_base)
        self.reference_data = self.t7_base / "01_REFERENCE_DATA"
        self.client_projects = self.t7_base / "02_CLIENT_PROJECTS"
        self.transfers_dir = self.t7_base / "10_PYTHON_ENVIRONMENT" / "aws_transfers"
        self.transfers_dir.mkdir(exist_ok=True)
        
        # Create subdirectories for transfer management
        (self.transfers_dir / "outbound").mkdir(exist_ok=True)
        (self.transfers_dir / "inbound").mkdir(exist_ok=True)
        (self.transfers_dir / "archive").mkdir(exist_ok=True)
    
    def create_fullcam_data_package(self, project_name: str, project_data: Dict) -> Path:
        """
        Create a complete data package ready for AWS WorkSpaces transfer.
        
        Args:
            project_name: Name of the project
            project_data: Dictionary containing all project information
            
        Returns:
            Path to the created transfer package
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            package_name = f"fullcam_package_{project_name}_{timestamp}"
            package_dir = self.transfers_dir / "outbound" / package_name
            package_dir.mkdir(exist_ok=True)
            
            # Create package structure
            (package_dir / "spatial_data").mkdir()
            (package_dir / "reference_data").mkdir() 
            (package_dir / "documentation").mkdir()
            (package_dir / "outputs").mkdir()  # For FullCAM results
            
            package_manifest = {
                "package_info": {
                    "project_name": project_name,
                    "created_date": datetime.now().isoformat(),
                    "created_by": "T7 Shield GIS Environment",
                    "mac_platform": "M2 chip - requires AWS WorkSpaces",
                    "fullcam_version_required": "Latest version on AWS WorkSpaces"
                },
                "files_included": [],
                "transfer_instructions": self._get_transfer_instructions()
            }
            
            # Copy spatial data files
            spatial_files = project_data.get('spatial_files', [])
            for file_info in spatial_files:
                source_path = Path(file_info['path'])
                if source_path.exists():
                    dest_path = package_dir / "spatial_data" / source_path.name
                    shutil.copy2(source_path, dest_path)
                    package_manifest["files_included"].append({
                        "file": source_path.name,
                        "type": "spatial_data",
                        "size_mb": round(dest_path.stat().st_size / (1024*1024), 2)
                    })
            
            # Copy relevant reference data
            ref_files = project_data.get('reference_files', [])
            for file_info in ref_files:
                source_path = Path(file_info['path'])
                if source_path.exists():
                    dest_path = package_dir / "reference_data" / source_path.name
                    shutil.copy2(source_path, dest_path)
                    package_manifest["files_included"].append({
                        "file": source_path.name,
                        "type": "reference_data", 
                        "size_mb": round(dest_path.stat().st_size / (1024*1024), 2)
                    })
            
            # Create FullCAM input specifications
            fullcam_spec = self._create_fullcam_specification(project_data)
            spec_path = package_dir / "FullCAM_Input_Specification.json"
            with open(spec_path, 'w') as f:
                json.dump(fullcam_spec, f, indent=2)
            
            package_manifest["files_included"].append({
                "file": "FullCAM_Input_Specification.json",
                "type": "configuration",
                "size_mb": round(spec_path.stat().st_size / (1024*1024), 2)
            })
            
            # Create Excel template for FullCAM
            excel_template = self._create_fullcam_excel_template(project_data)
            excel_path = package_dir / f"FullCAM_Template_{project_name}.xlsx"
            with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
                for sheet_name, data in excel_template.items():
                    if isinstance(data, pd.DataFrame):
                        data.to_excel(writer, sheet_name=sheet_name, index=False)
                    else:
                        # Convert dict to DataFrame
                        pd.DataFrame([data]).to_excel(writer, sheet_name=sheet_name, index=False)
            
            package_manifest["files_included"].append({
                "file": f"FullCAM_Template_{project_name}.xlsx",
                "type": "fullcam_template",
                "size_mb": round(excel_path.stat().st_size / (1024*1024), 2)
            })
            
            # Copy FullCAM documentation
            fullcam_docs = self.t7_base / "08_KNOWLEDGE BASE" / "fullcam-docs"
            if fullcam_docs.exists():
                for doc_file in fullcam_docs.rglob("*.pdf"):
                    dest_path = package_dir / "documentation" / doc_file.name
                    shutil.copy2(doc_file, dest_path)
                    package_manifest["files_included"].append({
                        "file": doc_file.name,
                        "type": "documentation",
                        "size_mb": round(dest_path.stat().st_size / (1024*1024), 2)
                    })
            
            # Create README for AWS WorkSpaces user
            readme_content = self._create_aws_readme(project_name, project_data)
            readme_path = package_dir / "README_AWS_WorkSpaces.md"
            with open(readme_path, 'w') as f:
                f.write(readme_content)
            
            # Save manifest
            manifest_path = package_dir / "package_manifest.json"
            with open(manifest_path, 'w') as f:
                json.dump(package_manifest, f, indent=2)
            
            # Create ZIP package for easy transfer
            zip_path = self.transfers_dir / "outbound" / f"{package_name}.zip"
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file_path in package_dir.rglob('*'):
                    if file_path.is_file():
                        arcname = file_path.relative_to(package_dir)
                        zipf.write(file_path, arcname)
            
            # Calculate total package size
            total_size_mb = sum(info["size_mb"] for info in package_manifest["files_included"])
            
            logger.info(f"FullCAM data package created: {package_name}")
            logger.info(f"Package size: {total_size_mb:.2f} MB")
            logger.info(f"ZIP package: {zip_path}")
            
            return zip_path
            
        except Exception as e:
            logger.error(f"Failed to create FullCAM data package: {e}")
            raise
    
    def process_fullcam_outputs(self, results_zip_path: Union[str, Path], 
                               project_name: str) -> Dict:
        """
        Process FullCAM outputs returned from AWS WorkSpaces.
        
        Args:
            results_zip_path: Path to ZIP file with FullCAM results
            project_name: Name of the project
            
        Returns:
            Dictionary with processed results and analysis
        """
        try:
            results_zip = Path(results_zip_path)
            if not results_zip.exists():
                raise FileNotFoundError(f"Results ZIP not found: {results_zip}")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            extract_dir = self.transfers_dir / "inbound" / f"{project_name}_{timestamp}"
            extract_dir.mkdir(exist_ok=True)
            
            # Extract results
            with zipfile.ZipFile(results_zip, 'r') as zipf:
                zipf.extractall(extract_dir)
            
            logger.info(f"Extracted FullCAM results to: {extract_dir}")
            
            # Process different result types
            results_summary = {
                "project_name": project_name,
                "processed_date": datetime.now().isoformat(),
                "results_location": str(extract_dir),
                "carbon_results": None,
                "reports": [],
                "plots": [],
                "errors": []
            }
            
            # Look for common FullCAM output files
            for file_path in extract_dir.rglob('*'):
                if file_path.is_file():
                    file_name = file_path.name.lower()
                    
                    if file_name.endswith('.csv') and 'carbon' in file_name:
                        # Process carbon results CSV
                        try:
                            carbon_df = pd.read_csv(file_path)
                            results_summary["carbon_results"] = {
                                "file_path": str(file_path),
                                "total_sequestration_tco2e": carbon_df.get('Total_Sequestration_tCO2e', [0])[0] if 'Total_Sequestration_tCO2e' in carbon_df.columns else None,
                                "summary_stats": carbon_df.describe().to_dict() if not carbon_df.empty else None
                            }
                        except Exception as e:
                            results_summary["errors"].append(f"Failed to process carbon results: {e}")
                    
                    elif file_name.endswith(('.pdf', '.docx')):
                        results_summary["reports"].append(str(file_path))
                    
                    elif file_name.endswith(('.png', '.jpg', '.jpeg')):
                        results_summary["plots"].append(str(file_path))
            
            # Create summary report
            summary_path = extract_dir / f"T7_Shield_Results_Summary_{project_name}.json"
            with open(summary_path, 'w') as f:
                json.dump(results_summary, f, indent=2)
            
            # Move original ZIP to archive
            archive_path = self.transfers_dir / "archive" / results_zip.name
            shutil.move(results_zip, archive_path)
            
            logger.info(f"FullCAM results processed successfully")
            return results_summary
            
        except Exception as e:
            logger.error(f"Failed to process FullCAM outputs: {e}")
            return {"error": str(e)}
    
    def _get_transfer_instructions(self) -> List[str]:
        """Get instructions for AWS WorkSpaces transfer."""
        return [
            "1. Connect to AWS WorkSpaces using your credentials",
            "2. Transfer this package to the Windows environment",
            "3. Extract all files maintaining directory structure", 
            "4. Open FullCAM application on Windows",
            "5. Use the Excel template and spatial data as inputs",
            "6. Follow the README_AWS_WorkSpaces.md instructions",
            "7. Export all FullCAM results and reports",
            "8. ZIP all outputs and transfer back to T7 Shield",
            "9. Use process_fullcam_outputs() to analyze results"
        ]
    
    def _create_fullcam_specification(self, project_data: Dict) -> Dict:
        """Create FullCAM input specification."""
        return {
            "project_details": {
                "name": project_data.get('name', 'Unknown'),
                "method": project_data.get('method', 'environmental_plantings'),
                "total_area_ha": project_data.get('total_area_ha', 0),
                "establishment_year": project_data.get('establishment_year', datetime.now().year)
            },
            "spatial_requirements": {
                "coordinate_system": "GDA2020 Geographic (EPSG:7844)",
                "minimum_area_ha": 0.2 if project_data.get('method') == 'environmental_plantings' else 2.0,
                "file_formats": ["Shapefile", "GeoPackage", "GeoTIFF"]
            },
            "fullcam_settings": {
                "crediting_period_years": project_data.get('crediting_period', 25),
                "climate_data_source": "BoM Long-term Average",
                "soil_data_source": "Australian Soil Classification"
            }
        }
    
    def _create_fullcam_excel_template(self, project_data: Dict) -> Dict:
        """Create Excel template for FullCAM input."""
        return {
            "Project_Summary": pd.DataFrame([{
                "Project_Name": project_data.get('name', 'Unknown'),
                "Method": project_data.get('method', 'environmental_plantings'),  
                "Total_Area_ha": project_data.get('total_area_ha', 0),
                "Establishment_Year": project_data.get('establishment_year', datetime.now().year),
                "Crediting_Period": project_data.get('crediting_period', 25)
            }]),
            "Species_List": pd.DataFrame(project_data.get('species_list', [
                {"Species": "Eucalyptus globulus", "Percentage": 60},
                {"Species": "Eucalyptus camaldulensis", "Percentage": 40}
            ])),
            "Site_Conditions": pd.DataFrame([{
                "Average_Rainfall_mm": project_data.get('rainfall_mm', 800),
                "Soil_Type": project_data.get('soil_type', 'Unknown'),
                "Slope_Percent": project_data.get('slope_percent', 5),
                "Aspect": project_data.get('aspect', 'North')
            }])
        }
    
    def _create_aws_readme(self, project_name: str, project_data: Dict) -> str:
        """Create README for AWS WorkSpaces user."""
        return f"""# FullCAM Analysis - {project_name}

## AWS WorkSpaces FullCAM Analysis Instructions

This package was prepared on macOS (T7 Shield) for FullCAM analysis on Windows via AWS WorkSpaces.

### Package Contents:
- **spatial_data/**: GIS files for the project area
- **reference_data/**: Australian reference datasets  
- **documentation/**: FullCAM method documentation
- **FullCAM_Template_{project_name}.xlsx**: Pre-configured FullCAM input template
- **FullCAM_Input_Specification.json**: Technical specifications

### AWS WorkSpaces Workflow:

1. **Connect to AWS WorkSpaces**
   - Use your AWS WorkSpaces credentials
   - Ensure FullCAM application is installed

2. **Import Data**
   - Extract all files maintaining directory structure
   - Open FullCAM application
   - Use the Excel template as starting point

3. **FullCAM Configuration**
   - Method: {project_data.get('method', 'environmental_plantings')}
   - Total Area: {project_data.get('total_area_ha', 'TBD')} hectares
   - Establishment Year: {project_data.get('establishment_year', datetime.now().year)}

4. **Spatial Data Input**
   - Import shapefiles from spatial_data/ directory
   - Ensure coordinate system is GDA2020 (EPSG:7844)
   - Verify area calculations match template

5. **Reference Data**
   - Use provided climate and soil data
   - Reference documentation in documentation/ folder

6. **Export Results**
   - Export all carbon calculations as CSV
   - Generate all available reports (PDF/Word)
   - Save any charts or plots
   - Include FullCAM project file (.fcam)

7. **Return Transfer**
   - ZIP all outputs maintaining file names
   - Transfer back to T7 Shield for processing
   - Use the process_fullcam_outputs() function

### Support:
- Review FullCAM documentation in documentation/ folder
- Check FullCAM_Input_Specification.json for technical details
- Contact T7 Shield team for data questions

### Notes:
- This package was created on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- Original platform: macOS with M2 chip (FullCAM not compatible)
- Target platform: Windows via AWS WorkSpaces
"""


def main():
    """Example usage of AWS WorkSpaces transfer tools."""
    print("T7 Shield AWS WorkSpaces FullCAM Transfer Module")
    print("=" * 50)
    
    # Initialize transfer manager
    transfer_manager = AWSWorkSpacesTransfer()
    
    print(f"✓ Transfer directory: {transfer_manager.transfers_dir}")
    print("✓ Ready for AWS WorkSpaces FullCAM data transfer")
    
    # Example project data structure
    example_project = {
        'name': 'Example_Environmental_Planting',
        'method': 'environmental_plantings',
        'total_area_ha': 25.5,
        'establishment_year': 2025,
        'crediting_period': 25,
        'spatial_files': [
            {'path': '/example/path/boundary.shp', 'type': 'boundary'}
        ],
        'reference_files': [
            {'path': '/example/path/soil_data.tif', 'type': 'soil'}
        ],
        'species_list': [
            {'Species': 'Eucalyptus globulus', 'Percentage': 70},
            {'Species': 'Acacia melanoxylon', 'Percentage': 30}
        ]
    }
    
    print("\\nExample project data structure:")
    print(f"- Project: {example_project['name']}")
    print(f"- Method: {example_project['method']}")  
    print(f"- Area: {example_project['total_area_ha']} ha")
    print("\\n✓ Ready to create data packages for AWS WorkSpaces transfer")


if __name__ == "__main__":
    main()