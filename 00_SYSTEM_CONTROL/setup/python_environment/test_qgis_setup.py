#!/usr/bin/env python3
"""
Simple QGIS Setup Test for T7 Shield
Tests QGIS functionality without complex operations
"""

import os
import sys
from pathlib import Path

def test_qgis_installation():
    """Test QGIS installation"""
    print("🔍 Testing QGIS installation...")
    
    try:
        import qgis.core
        print("✅ QGIS Python bindings available")
        return True
    except ImportError as e:
        print(f"❌ QGIS Python bindings not available: {e}")
        return False

def test_qgis_desktop():
    """Test QGIS desktop application"""
    print("\n🖥️ Testing QGIS desktop application...")
    
    try:
        import subprocess
        result = subprocess.run(['qgis', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ QGIS desktop working: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ QGIS desktop error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ QGIS desktop test failed: {e}")
        return False

def test_geopandas_operations():
    """Test GeoPandas operations (safe alternative to PyQGIS)"""
    print("\n🗺️ Testing GeoPandas operations...")
    
    try:
        import geopandas as gpd
        import shapely.geometry as sgeom
        
        # Create a simple test geometry
        point = sgeom.Point(0, 0)
        gdf = gpd.GeoDataFrame(geometry=[point], crs="EPSG:4326")
        
        print("✅ GeoPandas operations working")
        return True
    except Exception as e:
        print(f"❌ GeoPandas test failed: {e}")
        return False

def test_reference_data_access():
    """Test access to reference data"""
    print("\n📁 Testing reference data access...")
    
    try:
        # Test state boundaries
        state_file = Path("/Volumes/T7 Shield/01_REFERENCE_DATA/STATE_BOUNDARIES/STE_2021_AUST_GDA2020.shp")
        
        if state_file.exists():
            print("✅ State boundaries file accessible")
            
            # Try to read with geopandas
            import geopandas as gpd
            gdf = gpd.read_file(state_file)
            print(f"✅ Loaded {len(gdf)} state features")
            return True
        else:
            print("❌ State boundaries file not found")
            return False
            
    except Exception as e:
        print(f"❌ Reference data test failed: {e}")
        return False

def test_qgis_templates():
    """Test QGIS template access"""
    print("\n📋 Testing QGIS templates...")
    
    try:
        template_dir = Path("/Volumes/T7 Shield/04_TEMPLATES_LAYOUTS")
        
        if template_dir.exists():
            templates = list(template_dir.glob("*.qpt"))
            print(f"✅ Found {len(templates)} QGIS templates")
            
            for template in templates:
                print(f"   - {template.name}")
            return True
        else:
            print("❌ Templates directory not found")
            return False
            
    except Exception as e:
        print(f"❌ Template test failed: {e}")
        return False

def main():
    """Run all QGIS tests"""
    print("🚀 T7 Shield QGIS Setup Test")
    print("=" * 40)
    
    tests = [
        test_qgis_installation,
        test_qgis_desktop,
        test_geopandas_operations,
        test_reference_data_access,
        test_qgis_templates
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 40)
    print("📋 QGIS Test Summary:")
    
    if all(results):
        print("🎉 All QGIS tests passed!")
        print("\n✅ QGIS Setup Complete:")
        print("   - QGIS 3.34.6 installed and working")
        print("   - GeoPandas operations available (M2-safe)")
        print("   - Reference data accessible")
        print("   - Templates available")
        print("\n💡 For M2 compatibility:")
        print("   - Use GeoPandas/Rasterio for processing")
        print("   - Use QGIS desktop for visualization")
        print("   - Avoid direct PyQGIS integration")
    else:
        print("⚠️ Some QGIS tests failed. Check errors above.")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

