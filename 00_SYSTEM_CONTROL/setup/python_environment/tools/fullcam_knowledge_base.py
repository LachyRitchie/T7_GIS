#!/usr/bin/env python3
"""
FullCAM Knowledge Base Integration System

This module extracts and organizes knowledge from your FullCAM documentation PDFs
to provide intelligent guidance for carbon accounting workflows.

Author: T7 Shield GIS Environment
Version: 1.0
Date: 2025
"""

import pandas as pd
import json
from pathlib import Path
from typing import Dict, List, Optional, Union
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FullCAMKnowledgeBase:
    """
    Intelligent FullCAM knowledge system extracted from official documentation.
    """
    
    def __init__(self):
        self.t7_base = Path("/Volumes/T7 Shield")
        self.docs_path = self.t7_base / "08_KNOWLEDGE BASE" / "fullcam-docs"
        self.knowledge = self._build_knowledge_base()
    
    def _build_knowledge_base(self) -> Dict:
        """Build comprehensive knowledge base from documentation analysis."""
        return {
            "versions": {
                "current_required": "FullCAM 2020",
                "determination": "Environmental Plantings 2024 (EP2024)",
                "version_date": "March 2025",
                "browser_url": "https://www.fullcam.gov.au/"
            },
            
            "species_calibrations": {
                "mixed_species_environmental": {
                    "fullcam_name": "Mixed species environmental planting",
                    "determination_name": "Mixed species environmental planting",
                    "description": "For mixed species environmental plantings",
                    "applicable_sections": ["section 20"]
                },
                "mallee_eucalypt": {
                    "fullcam_name": "Mallee eucalypt species", 
                    "determination_name": "Mallee eucalypt planting",
                    "description": "For plantings comprised predominantly of mallee-eucalypt species",
                    "applicable_sections": ["section 19"]
                }
            },
            
            "planting_configurations": {
                "block_plantings": {
                    "description": "Block plantings on land managed for environmental services",
                    "min_stocking_density": 200,  # stems per hectare
                    "fullcam_event": "Mixed species environmental plantings: Block plantings >200 stems per hectare",
                    "sampling_required": False
                },
                "belt_plantings_low_density": {
                    "description": "Low density linear plantings",
                    "density_range": [200, 1500],  # stems per hectare
                    "fullcam_event": "Belt plantings <1500 sph", 
                    "sampling_required": False
                },
                "belt_plantings_high_density": {
                    "description": "High density linear plantings",
                    "min_density": 1500,  # stems per hectare
                    "fullcam_event": "Belt plantings >1500 sph",
                    "sampling_required": True
                }
            },
            
            "required_events": {
                "tree_planting": {
                    "mandatory": True,
                    "fullcam_type": "Tree planting",
                    "notes": "All project modelling must commence with a Plant Trees event",
                    "date_format": "DD/MM/YYYY",
                    "timing": "Must be the planting date for the CEA"
                },
                "wildfire_trees_not_killed": {
                    "mandatory": "If occurs",
                    "fullcam_type": "Forest fire",
                    "standard_event": "Wildfire – trees not killed",
                    "requires_percentage": True
                },
                "wildfire_trees_killed": {
                    "mandatory": "If occurs", 
                    "fullcam_type": "Forest fire",
                    "standard_event": "Wildfire – trees killed",
                    "requires_percentage": True
                },
                "prescribed_fire": {
                    "mandatory": "If occurs",
                    "fullcam_type": "Forest fire", 
                    "standard_event": "Prescribed burn",
                    "requires_percentage": True
                },
                "thinning": {
                    "mandatory": "If occurs",
                    "fullcam_type": "Forest thinning",
                    "standard_event": "Initial clearing: no product recovery",
                    "requires_percentage": True
                }
            },
            
            "required_outputs": {
                "tree_carbon_pool": "Carbon / Forest / Plants / C mass of trees",
                "ch4_emissions": "Carbon / Whole / Emissions / CH4 emitted due to fire", 
                "n2o_emissions": "Nitrogen / Whole / Emissions / N2O emitted due to fire",
                "debris_pool": "Other / Carbon Projects / C mass of forest debris"
            },
            
            "determination_equations": {
                "equation_9": {
                    "parameters": ["CDti", "CDdi"],
                    "description": "Initial carbon stocks"
                },
                "equation_10": {
                    "parameters": ["Cti", "Cdi"],
                    "description": "Current carbon stocks"
                },
                "equation_11": {
                    "parameters": ["ECH4i"], 
                    "description": "CH4 emissions from fire"
                },
                "equation_12": {
                    "parameters": ["EN2Oi"],
                    "description": "N2O emissions from fire"
                }
            },
            
            "workflow_steps": [
                "Access FullCAM 2020 at https://www.fullcam.gov.au/",
                "Request access to FullCAM 2020 (not default 2024 version)",
                "Create new simulation from Environmental Plantings Template",
                "Configure timing (start = planting date, format YYYY,MM)",
                "Enter model point coordinates (center of CEA, 5 decimal places)",
                "Select ERF Methods and query spatial data",
                "Choose species calibration (Mixed species or Mallee eucalypt)",
                "Skip Site, Trees, Soil, Initial Conditions tabs",
                "Add all required events with correct dates and percentages",
                "Select required outputs only",
                "Run simulation and download CSV results"
            ],
            
            "compliance_requirements": {
                "cea_requirements": "Separate plot files for each Carbon Estimation Area",
                "model_point": "Roughly center of CEA and representative",
                "coordinate_precision": "5 decimal places required",
                "spatial_data_refresh": "Must query spatial data each time software is run",
                "settings_changes": "Only change settings as indicated in guidelines",
                "version_consistency": "Create new plot file for each FullCAM/Guidelines version"
            }
        }
    
    def get_species_guidance(self, planting_type: str) -> Dict:
        """Get species selection guidance based on planting type."""
        planting_type_lower = planting_type.lower()
        
        if "mallee" in planting_type_lower:
            return self.knowledge["species_calibrations"]["mallee_eucalypt"]
        else:
            return self.knowledge["species_calibrations"]["mixed_species_environmental"]
    
    def get_planting_configuration(self, geometry: str, density_sph: Optional[int] = None) -> Dict:
        """Get planting configuration guidance."""
        geometry_lower = geometry.lower()
        
        if "block" in geometry_lower:
            return self.knowledge["planting_configurations"]["block_plantings"]
        elif "belt" in geometry_lower or "linear" in geometry_lower:
            if density_sph and density_sph >= 1500:
                return self.knowledge["planting_configurations"]["belt_plantings_high_density"]
            else:
                return self.knowledge["planting_configurations"]["belt_plantings_low_density"]
        else:
            # Default to mixed species block
            return self.knowledge["planting_configurations"]["block_plantings"]
    
    def validate_project_requirements(self, project_data: Dict) -> Dict:
        """Validate project against FullCAM requirements."""
        validation_results = {
            "compliant": True,
            "issues": [],
            "recommendations": []
        }
        
        # Check required fields
        required_fields = ["planting_date", "species_type", "geometry", "total_area_ha"]
        for field in required_fields:
            if field not in project_data:
                validation_results["issues"].append(f"Missing required field: {field}")
                validation_results["compliant"] = False
        
        # Check area requirements (Environmental Plantings: 0.2 - 10,000 ha)
        if "total_area_ha" in project_data:
            area = project_data["total_area_ha"]
            if area < 0.2:
                validation_results["issues"].append(f"Area {area} ha below minimum 0.2 ha")
                validation_results["compliant"] = False
            elif area > 10000:
                validation_results["issues"].append(f"Area {area} ha above maximum 10,000 ha")
                validation_results["compliant"] = False
        
        # Check species type
        if "species_type" in project_data:
            species_type = project_data["species_type"].lower()
            if species_type not in ["mixed_species", "mallee_eucalypt"]:
                validation_results["recommendations"].append(
                    "Species type should be 'mixed_species' or 'mallee_eucalypt'"
                )
        
        # Check coordinate precision if provided
        if "coordinates" in project_data:
            coords = project_data["coordinates"]
            if "latitude" in coords and "longitude" in coords:
                lat_decimals = len(str(coords["latitude"]).split(".")[-1])
                lon_decimals = len(str(coords["longitude"]).split(".")[-1])
                if lat_decimals < 5 or lon_decimals < 5:
                    validation_results["recommendations"].append(
                        "Coordinates should have 5 decimal places precision"
                    )
        
        return validation_results
    
    def get_event_guidance(self, event_type: str) -> Dict:
        """Get guidance for modeling specific events."""
        event_type_clean = event_type.lower().replace(" ", "_").replace("-", "_")
        
        # Map variations to standard keys
        event_mapping = {
            "planting": "tree_planting",
            "plant_trees": "tree_planting", 
            "fire": "wildfire_trees_not_killed",
            "wildfire": "wildfire_trees_not_killed",
            "prescribed_burn": "prescribed_fire",
            "thin": "thinning",
            "thinning": "thinning"
        }
        
        # Try direct match first, then mapping
        event_key = event_type_clean
        if event_key not in self.knowledge["required_events"]:
            event_key = event_mapping.get(event_type_clean, "tree_planting")
        
        return self.knowledge["required_events"].get(event_key, {})
    
    def generate_fullcam_checklist(self, project_data: Dict) -> List[str]:
        """Generate step-by-step FullCAM checklist for a project."""
        checklist = [
            "□ Access FullCAM 2020 browser application",
            "□ Request access to FullCAM 2020 (not 2024) in User Profile", 
            "□ Create New Simulation from Environmental Plantings Template",
            "□ Name plot file with CEA identifier",
            "□ Save plot file immediately"
        ]
        
        # Add timing configuration
        if "planting_date" in project_data:
            planting_date = project_data["planting_date"]
            checklist.append(f"□ Set timing: start date = {planting_date} (planting date)")
            checklist.append("□ Turn OFF 'Calendar dates' slider")
        else:
            checklist.append("□ Set timing: start date = planting date (YYYY,MM format)")
        
        # Add location configuration  
        if "coordinates" in project_data:
            coords = project_data["coordinates"]
            checklist.append(f"□ Enter coordinates: {coords.get('latitude', 'XX.XXXXX')}, {coords.get('longitude', 'XXX.XXXXX')}")
        else:
            checklist.append("□ Enter model point coordinates (center of CEA, 5 decimal places)")
        
        # Add species selection
        species_guidance = self.get_species_guidance(project_data.get("species_type", "mixed"))
        checklist.append("□ Select ERF Methods in Forest category dropdown")
        checklist.append("□ Click 'Query FullCAM spatial data'")
        checklist.append(f"□ Select '{species_guidance['fullcam_name']}'")
        
        # Add standard steps
        checklist.extend([
            "□ Skip Site, Trees, Soil, Initial Conditions tabs",
            "□ Go to Events tab",
            "□ Add Tree Planting event (mandatory first event)",
        ])
        
        # Add conditional events
        if project_data.get("wildfires"):
            checklist.append("□ Add wildfire events with affected percentages")
        if project_data.get("prescribed_burns"):
            checklist.append("□ Add prescribed burn events")
        if project_data.get("thinning_events"):
            checklist.append("□ Add thinning events")
        
        # Final steps
        checklist.extend([
            "□ Navigate to Output Windows tab",
            "□ Verify required outputs selected (tree carbon, CH4, N2O, debris)",
            "□ Run simulation",
            "□ Download CSV results for offset calculations"
        ])
        
        return checklist
    
    def get_determination_guidance(self, equation_number: int) -> Dict:
        """Get guidance for specific determination equations."""
        eq_key = f"equation_{equation_number}"
        return self.knowledge["determination_equations"].get(eq_key, {})
    
    def export_knowledge_summary(self, output_path: Optional[Path] = None) -> Path:
        """Export knowledge base summary to JSON file."""
        if output_path is None:
            output_path = self.t7_base / "10_PYTHON_ENVIRONMENT/tools/fullcam_knowledge_export.json"
        
        with open(output_path, 'w') as f:
            json.dump(self.knowledge, f, indent=2, default=str)
        
        logger.info(f"Knowledge base exported to: {output_path}")
        return output_path


class FullCAMConsultant:
    """
    Interactive FullCAM consultation system using the knowledge base.
    """
    
    def __init__(self):
        self.kb = FullCAMKnowledgeBase()
    
    def consult_project_setup(self, project_data: Dict) -> Dict:
        """Provide comprehensive project setup consultation."""
        consultation = {
            "project_validation": self.kb.validate_project_requirements(project_data),
            "species_guidance": self.kb.get_species_guidance(project_data.get("species_type", "mixed")),
            "configuration_guidance": self.kb.get_planting_configuration(
                project_data.get("geometry", "block"),
                project_data.get("density_sph")
            ),
            "fullcam_checklist": self.kb.generate_fullcam_checklist(project_data),
            "version_requirements": self.kb.knowledge["versions"]
        }
        
        return consultation
    
    def consult_event_modeling(self, events: List[str]) -> Dict:
        """Provide guidance for modeling specific events."""
        event_guidance = {}
        for event in events:
            event_guidance[event] = self.kb.get_event_guidance(event)
        
        return {
            "event_guidance": event_guidance,
            "mandatory_events": ["tree_planting"],
            "conditional_events": ["wildfires", "prescribed_burns", "thinning"]
        }


def main():
    """Example usage of the FullCAM Knowledge Base system."""
    print("T7 Shield FullCAM Knowledge Base System")
    print("=" * 45)
    
    # Initialize knowledge base
    kb = FullCAMKnowledgeBase()
    consultant = FullCAMConsultant()
    
    print(f"✓ Knowledge base initialized from {len(kb.knowledge)} categories")
    print(f"✓ Current FullCAM version: {kb.knowledge['versions']['current_required']}")
    print(f"✓ Determination: {kb.knowledge['versions']['determination']}")
    
    # Example consultation
    example_project = {
        "name": "Example Environmental Planting",
        "species_type": "mixed_species",
        "geometry": "block", 
        "total_area_ha": 25.5,
        "planting_date": "2025,01",
        "coordinates": {"latitude": -31.95054, "longitude": 115.86050}
    }
    
    print("\n" + "=" * 45)
    print("EXAMPLE PROJECT CONSULTATION:")
    print("=" * 45)
    
    consultation = consultant.consult_project_setup(example_project)
    
    print(f"Project validation: {'✓ COMPLIANT' if consultation['project_validation']['compliant'] else '❌ ISSUES FOUND'}")
    print(f"Species calibration: {consultation['species_guidance']['fullcam_name']}")
    print(f"Configuration: {consultation['configuration_guidance']['description']}")
    
    print("\nFullCAM Checklist (first 5 items):")
    for item in consultation['fullcam_checklist'][:5]:
        print(f"  {item}")
    print(f"  ... and {len(consultation['fullcam_checklist']) - 5} more steps")
    
    # Export knowledge base
    export_path = kb.export_knowledge_summary()
    print(f"\n✓ Knowledge base exported to: {export_path.name}")
    
    print("\n🎯 FullCAM Knowledge Base ready for integration!")


if __name__ == "__main__":
    main()