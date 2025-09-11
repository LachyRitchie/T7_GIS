#!/usr/bin/env python3
"""
T7 Shield GIS Environment Verification Script

This script verifies that all components of the T7 Shield professional GIS environment
are properly installed and configured.

Run this script after setup to ensure everything is working correctly.
"""

import sys
import os
from pathlib import Path
import importlib
import pandas as pd

def test_import(module_name, description):
    """Test importing a module and return status."""
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, '__version__', 'Unknown version')
        return True, f"✓ {description}: {version}"
    except ImportError as e:
        return False, f"❌ {description}: Import failed - {e}"
    except Exception as e:
        return False, f"❌ {description}: Error - {e}"

def verify_directory_structure():
    """Verify T7 Shield directory structure."""
    print("=" * 60)
    print("DIRECTORY STRUCTURE VERIFICATION")
    print("=" * 60)
    
    t7_base = Path("/Volumes/T7 Shield")
    python_env = t7_base / "10_PYTHON_ENVIRONMENT"
    
    required_dirs = [
        t7_base / "01_REFERENCE_DATA",
        t7_base / "02_CLIENT_PROJECTS", 
        t7_base / "08_KNOWLEDGE BASE" / "fullcam-docs",
        python_env,
        python_env / "scripts",
        python_env / "notebooks",
        python_env / "tools",
        python_env / "configs"
    ]
    
    all_good = True
    for dir_path in required_dirs:
        if dir_path.exists():
            print(f"✓ {dir_path.name}")
        else:
            print(f"❌ {dir_path.name} - Missing")
            all_good = False
    
    return all_good

def verify_core_libraries():
    """Verify core GIS libraries."""
    print("\n" + "=" * 60)
    print("CORE LIBRARIES VERIFICATION")
    print("=" * 60)
    
    libraries = [
        ('pandas', 'Pandas Data Analysis'),
        ('numpy', 'NumPy Scientific Computing'),
        ('geopandas', 'GeoPandas Geospatial Data'),
        ('rasterio', 'Rasterio Geospatial Raster I/O'),
        ('shapely', 'Shapely Geometric Operations'),
        ('pyproj', 'PyProj Coordinate Transformations'),
        ('fiona', 'Fiona Spatial Data I/O'),
        ('matplotlib', 'Matplotlib Plotting'),
        ('seaborn', 'Seaborn Statistical Visualization'),
        ('folium', 'Folium Interactive Maps'),
        ('jupyter', 'Jupyter Notebook'),
        ('qgis.core', 'QGIS Core'),
    ]
    
    results = []
    for module, description in libraries:
        success, message = test_import(module, description)
        results.append(success)
        print(message)
    
    return all(results)

def verify_specialized_libraries():
    """Verify specialized GIS libraries."""
    print("\n" + "=" * 60)
    print("SPECIALIZED LIBRARIES VERIFICATION")
    print("=" * 60)
    
    libraries = [
        ('dask', 'Dask Parallel Computing'),
        ('xarray', 'Xarray Multi-dimensional Data'),
        ('rasterstats', 'Rasterstats Zonal Statistics'),
        ('geocoder', 'Geocoder Geocoding'),
        ('earthpy', 'EarthPy Earth Analytics'),
        ('osmnx', 'OSMnx OpenStreetMap'),
        ('scikit-learn', 'Scikit-learn Machine Learning'),
        ('scipy', 'SciPy Scientific Library'),
    ]
    
    results = []
    for module, description in libraries:
        success, message = test_import(module, description)
        results.append(success)
        print(message)
    
    return all(results)

def verify_data_access():
    """Verify access to reference data."""
    print("\n" + "=" * 60)
    print("DATA ACCESS VERIFICATION") 
    print("=" * 60)
    
    t7_base = Path("/Volumes/T7 Shield")
    
    # Check key reference datasets
    key_datasets = [
        ("Australian States", "01_REFERENCE_DATA/BOUNDARIES/STATE_BOUNDARIES/STE_2021_AUST_GDA2020.shp"),
        ("IBRA Bioregions", "01_REFERENCE_DATA/BOUNDARIES/BIOREGIONS_IBRA/IBRA7_subregions.shp"),
        ("Rainfall LTA", "01_REFERENCE_DATA/CLIMATE/RAINFALL_LTA/LTA_rainfall.tif"),
        ("Soil Classification", "01_REFERENCE_DATA/SOIL/AUSTRALIAN_SOIL_CLASSIFICATION/ASC_EV_C_P_AU_TRN_N.cog.tif"),
    ]
    
    all_good = True
    for name, path in key_datasets:
        full_path = t7_base / path
        if full_path.exists():
            print(f"✓ {name}")
        else:
            print(f"❌ {name} - Not found at {path}")
            all_good = False
    
    return all_good

def verify_fullcam_docs():
    """Verify FullCAM documentation."""
    print("\n" + "=" * 60)
    print("FULLCAM DOCUMENTATION VERIFICATION")
    print("=" * 60)
    
    fullcam_docs = Path("/Volumes/T7 Shield/08_KNOWLEDGE BASE/fullcam-docs")
    
    if not fullcam_docs.exists():
        print("❌ FullCAM docs directory not found")
        return False
    
    # Count PDF documents
    pdf_count = len(list(fullcam_docs.rglob("*.pdf")))
    print(f"✓ FullCAM documentation directory exists")
    print(f"✓ Found {pdf_count} PDF documents")
    
    return True

def verify_scripts():
    """Verify custom scripts."""
    print("\n" + "=" * 60)
    print("CUSTOM SCRIPTS VERIFICATION")
    print("=" * 60)
    
    scripts_base = Path("/Volumes/T7 Shield/10_PYTHON_ENVIRONMENT/scripts")
    
    key_scripts = [
        "data_processing/qgis_integration.py",
        "fullcam_integration/fullcam_data_preparation.py", 
        "fullcam_integration/aws_workspaces_transfer.py"
    ]
    
    all_good = True
    for script in key_scripts:
        script_path = scripts_base / script
        if script_path.exists():
            print(f"✓ {script}")
        else:
            print(f"❌ {script} - Missing")
            all_good = False
    
    return all_good

def verify_notebooks():
    """Verify Jupyter notebooks."""
    print("\n" + "=" * 60)
    print("JUPYTER NOTEBOOKS VERIFICATION")
    print("=" * 60)
    
    notebooks_base = Path("/Volumes/T7 Shield/10_PYTHON_ENVIRONMENT/notebooks")
    
    key_notebooks = [
        "exploratory/01_T7_Shield_Data_Exploration.ipynb",
        "analysis/02_Spatial_Analysis_Workflows.ipynb"
    ]
    
    all_good = True
    for notebook in key_notebooks:
        notebook_path = notebooks_base / notebook
        if notebook_path.exists():
            print(f"✓ {notebook}")
        else:
            print(f"❌ {notebook} - Missing")
            all_good = False
    
    return all_good

def test_qgis_functionality():
    """Test QGIS functionality."""
    print("\n" + "=" * 60)
    print("QGIS FUNCTIONALITY TEST")
    print("=" * 60)
    
    try:
        from qgis.core import QgsApplication, QgsVectorLayer
        
        # Initialize QGIS (minimal test)
        QgsApplication.setPrefixPath('/opt/homebrew/Caskroom/miniconda/base/envs/t7_gis_professional', True)
        qgs = QgsApplication([], False)
        qgs.initQgis()
        
        # Test loading a layer
        states_path = "/Volumes/T7 Shield/01_REFERENCE_DATA/BOUNDARIES/STATE_BOUNDARIES/STE_2021_AUST_GDA2020.shp"
        if Path(states_path).exists():
            layer = QgsVectorLayer(states_path, "states_test", "ogr")
            if layer.isValid():
                feature_count = layer.featureCount()
                print(f"✓ QGIS layer loading: {feature_count} features loaded")
                success = True
            else:
                print("❌ QGIS layer loading failed")
                success = False
        else:
            print("❌ States shapefile not found for QGIS test")
            success = False
        
        qgs.exitQgis()
        return success
        
    except Exception as e:
        print(f"❌ QGIS functionality test failed: {e}")
        return False

def main():
    """Main verification function."""
    print("T7 SHIELD GIS ENVIRONMENT VERIFICATION")
    print("=" * 60)
    print("Verifying professional GIS environment setup...")
    print("This may take a few moments...")
    
    # Run all verification tests
    tests = [
        ("Directory Structure", verify_directory_structure),
        ("Core Libraries", verify_core_libraries), 
        ("Specialized Libraries", verify_specialized_libraries),
        ("Data Access", verify_data_access),
        ("FullCAM Documentation", verify_fullcam_docs),
        ("Custom Scripts", verify_scripts),
        ("Jupyter Notebooks", verify_notebooks),
        ("QGIS Functionality", test_qgis_functionality)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        icon = "✓" if result else "❌"
        print(f"{icon} {test_name:<30} {status}")
    
    print("-" * 60)
    print(f"TOTAL: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 CONGRATULATIONS! 🎉")
        print("Your T7 Shield professional GIS environment is fully operational!")
        print("\nNext steps:")
        print("1. Launch Jupyter Lab: cd notebooks && jupyter lab")
        print("2. Start with: 01_T7_Shield_Data_Exploration.ipynb")
        print("3. Explore your client project data")
        print("4. Begin FullCAM data preparation workflows")
        print("\nYour environment is bulletproof and ready for professional work! 🌳📊")
    else:
        print("\n⚠️  ATTENTION REQUIRED")
        print(f"{total - passed} tests failed. Please review the failed components above.")
        print("Contact support if you need assistance resolving these issues.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)