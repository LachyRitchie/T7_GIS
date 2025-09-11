#!/usr/bin/env python3
"""
Test script for T7 Shield GIS Environment
Verifies all components are working correctly
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test all core GIS imports"""
    print("🔍 Testing core GIS imports...")
    
    try:
        import geopandas as gpd
        import rasterio
        import shapely
        import fiona
        import pyproj
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import dask
        import xarray
        print("✅ All core packages imported successfully!")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_versions():
    """Test and display key library versions"""
    print("\n📊 Checking library versions...")
    
    try:
        import rasterio
        import pyproj
        import geopandas
        import shapely
        
        print(f"GDAL version: {rasterio.__gdal_version__}")
        print(f"PROJ version: {pyproj.proj_version_str}")
        print(f"GeoPandas version: {geopandas.__version__}")
        print(f"Shapely version: {shapely.__version__}")
        return True
    except Exception as e:
        print(f"❌ Version check error: {e}")
        return False

def test_data_access():
    """Test access to T7 Shield data directories"""
    print("\n📁 Testing data directory access...")
    
    # Test access to key directories
    data_dirs = [
        "/Volumes/T7 Shield/01_REFERENCE_DATA",
        "/Volumes/T7 Shield/02_CLIENT_PROJECTS", 
        "/Volumes/T7 Shield/00_GLOBAL_PROJECTS"
    ]
    
    for dir_path in data_dirs:
        if os.path.exists(dir_path):
            print(f"✅ {dir_path} - accessible")
        else:
            print(f"❌ {dir_path} - not found")
    
    return True

def test_simple_geospatial_operations():
    """Test basic geospatial operations"""
    print("\n🗺️ Testing basic geospatial operations...")
    
    try:
        import pyproj
        
        # Test coordinate transformation
        transformer = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
        x, y = transformer.transform(0, 0)
        
        print("✅ Basic geospatial operations working")
        return True
    except Exception as e:
        print(f"❌ Geospatial operations error: {e}")
        return False

def test_jupyter():
    """Test Jupyter installation"""
    print("\n📓 Testing Jupyter installation...")
    
    try:
        import jupyter
        import jupyterlab
        print("✅ Jupyter and JupyterLab available")
        return True
    except ImportError as e:
        print(f"❌ Jupyter error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 T7 Shield GIS Environment Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_versions,
        test_data_access,
        test_simple_geospatial_operations,
        test_jupyter
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 50)
    print("📋 Test Summary:")
    
    if all(results):
        print("🎉 All tests passed! Your GIS environment is ready.")
        print("\nNext steps:")
        print("1. Activate environment: conda activate t7_gis_professional")
        print("2. Start Jupyter: jupyter lab")
        print("3. Begin your GIS analysis!")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
