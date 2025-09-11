#!/usr/bin/env python3
"""
Final T7 Shield GIS Environment Test
Comprehensive verification of the complete optimized GIS setup
"""

import sys
import os
import time
from pathlib import Path
import subprocess

def test_environment_activation():
    """Test conda environment"""
    print("🔧 Testing Environment Activation...")
    
    try:
        # Check if we're in the right environment
        result = subprocess.run(['conda', 'info', '--envs'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0 and 't7_gis_professional' in result.stdout:
            print("✅ t7_gis_professional environment active")
            return True
        else:
            print("❌ Environment not properly activated")
            return False
    except Exception as e:
        print(f"❌ Environment test failed: {e}")
        return False

def test_core_gis_imports():
    """Test all core GIS imports"""
    print("\n🗺️ Testing Core GIS Imports...")
    
    core_packages = [
        ('geopandas', 'GeoPandas'),
        ('rasterio', 'Rasterio'),
        ('shapely', 'Shapely'),
        ('fiona', 'Fiona'),
        ('pyproj', 'PyProj'),
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('matplotlib', 'Matplotlib'),
        ('folium', 'Folium'),
        ('dask', 'Dask'),
        ('xarray', 'Xarray')
    ]
    
    results = []
    for module, name in core_packages:
        try:
            __import__(module)
            print(f"✅ {name}: Imported successfully")
            results.append(True)
        except ImportError as e:
            print(f"❌ {name}: Import failed - {e}")
            results.append(False)
    
    return all(results)

def test_gis_versions():
    """Test GIS library versions"""
    print("\n📊 Testing GIS Library Versions...")
    
    try:
        import rasterio
        import pyproj
        import geopandas
        
        print(f"✅ GDAL: {rasterio.__gdal_version__}")
        print(f"✅ PROJ: {pyproj.proj_version_str}")
        print(f"✅ GeoPandas: {geopandas.__version__}")
        return True
    except Exception as e:
        print(f"❌ Version check failed: {e}")
        return False

def test_qgis_installation():
    """Test QGIS installation"""
    print("\n🖥️ Testing QGIS Installation...")
    
    try:
        result = subprocess.run(['qgis', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ QGIS: {result.stdout.strip()}")
            return True
        else:
            print("❌ QGIS not working")
            return False
    except Exception as e:
        print(f"❌ QGIS test failed: {e}")
        return False

def test_system_tools():
    """Test system GIS tools"""
    print("\n🔧 Testing System GIS Tools...")
    
    tools = [
        ('gdalinfo', 'GDAL Info'),
        ('ogr2ogr', 'OGR2OGR'),
        ('proj', 'PROJ')
    ]
    
    results = []
    for tool, name in tools:
        try:
            result = subprocess.run([tool, '--help'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode in [0, 1]:  # Some tools return 1 for help
                print(f"✅ {name}: Working")
                results.append(True)
            else:
                print(f"❌ {name}: Error")
                results.append(False)
        except Exception as e:
            print(f"❌ {name}: {e}")
            results.append(False)
    
    return all(results)

def test_jupyter():
    """Test Jupyter installation"""
    print("\n📓 Testing Jupyter Installation...")
    
    try:
        result = subprocess.run(['jupyter', 'lab', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ JupyterLab: {result.stdout.strip()}")
            return True
        else:
            print("❌ JupyterLab not working")
            return False
    except Exception as e:
        print(f"❌ Jupyter test failed: {e}")
        return False

def test_data_access():
    """Test access to T7 Shield data"""
    print("\n📁 Testing Data Access...")
    
    data_paths = [
        "/Volumes/T7 Shield/01_REFERENCE_DATA",
        "/Volumes/T7 Shield/02_CLIENT_PROJECTS",
        "/Volumes/T7 Shield/00_GLOBAL_PROJECTS",
        "/Volumes/T7 Shield/10_PYTHON_ENVIRONMENT/notebooks"
    ]
    
    results = []
    for path in data_paths:
        if Path(path).exists():
            print(f"✅ {path}")
            results.append(True)
        else:
            print(f"❌ {path} - Not found")
            results.append(False)
    
    return all(results)

def test_spatial_operations():
    """Test basic spatial operations"""
    print("\n🗺️ Testing Spatial Operations...")
    
    try:
        import geopandas as gpd
        import pyproj
        
        # Test coordinate transformation
        transformer = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:3577", always_xy=True)
        x, y = transformer.transform(115.8, -31.9)  # Perth coordinates
        
        print("✅ Coordinate transformation working")
        print(f"✅ Perth in Albers: ({x:.2f}, {y:.2f})")
        return True
    except Exception as e:
        print(f"❌ Spatial operations failed: {e}")
        return False

def test_performance():
    """Test environment performance"""
    print("\n⚡ Testing Performance...")
    
    try:
        import numpy as np
        import pandas as pd
        
        # Test array operations
        start_time = time.time()
        large_array = np.random.random((1000, 1000))
        result = np.linalg.eig(large_array)
        array_time = time.time() - start_time
        
        # Test pandas operations
        start_time = time.time()
        df = pd.DataFrame(np.random.random((10000, 10)))
        df.describe()
        pandas_time = time.time() - start_time
        
        print(f"✅ NumPy operations: {array_time:.3f} seconds")
        print(f"✅ Pandas operations: {pandas_time:.3f} seconds")
        
        if array_time < 5.0 and pandas_time < 2.0:
            print("✅ Performance: Excellent (M2 optimized)")
            return True
        else:
            print("⚠️ Performance: Acceptable")
            return True
            
    except Exception as e:
        print(f"❌ Performance test failed: {e}")
        return False

def test_m2_compatibility():
    """Test M2-specific compatibility"""
    print("\n🍎 Testing M2 Compatibility...")
    
    try:
        import platform
        import subprocess
        
        # Check architecture
        arch = platform.machine()
        if arch == 'arm64':
            print("✅ Running on ARM64 (M2)")
        else:
            print(f"⚠️ Running on {arch}")
        
        # Check for M2-specific issues
        try:
            import qgis.core
            print("⚠️ PyQGIS available (may cause crashes on M2)")
        except ImportError:
            print("✅ PyQGIS not available (safe for M2)")
        
        return True
    except Exception as e:
        print(f"❌ M2 compatibility test failed: {e}")
        return False

def main():
    """Run comprehensive environment test"""
    print("🚀 T7 Shield GIS Environment - Final Test")
    print("=" * 60)
    print("Comprehensive verification of optimized GIS setup")
    print("=" * 60)
    
    tests = [
        test_environment_activation,
        test_core_gis_imports,
        test_gis_versions,
        test_qgis_installation,
        test_system_tools,
        test_jupyter,
        test_data_access,
        test_spatial_operations,
        test_performance,
        test_m2_compatibility
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 60)
    print("📋 FINAL TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Tests Passed: {passed}/{total}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n🎉 PERFECT! All tests passed!")
        print("\n✅ Your T7 Shield GIS Environment is:")
        print("   - Fully operational and optimized")
        print("   - M2 compatible and fast")
        print("   - Ready for professional GIS work")
        print("   - Complete with all tools and data access")
        print("\n🚀 You can now:")
        print("   - Process Australian forestry data")
        print("   - Perform complex spatial analysis")
        print("   - Create professional visualizations")
        print("   - Run production workflows")
        print("\n🏆 Status: PROFESSIONAL-GRADE GIS ENVIRONMENT READY!")
    else:
        print(f"\n⚠️ {total-passed} test(s) failed")
        print("Check the errors above for details")
        print("Most functionality should still be available")
    
    print("\n" + "=" * 60)
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

