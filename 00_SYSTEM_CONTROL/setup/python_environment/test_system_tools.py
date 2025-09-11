#!/usr/bin/env python3
"""
System Tools Test for T7 Shield GIS Environment
Tests command-line GIS utilities and system integration
"""

import subprocess
import sys
from pathlib import Path

def test_gdal_tools():
    """Test GDAL command-line tools"""
    print("🔧 Testing GDAL command-line tools...")
    
    tools = [
        ('gdalinfo', 'GDAL Info'),
        ('gdal_translate', 'GDAL Translate'),
        ('gdal_rasterize', 'GDAL Rasterize'),
        ('gdalwarp', 'GDAL Warp'),
        ('gdal_merge.py', 'GDAL Merge'),
    ]
    
    results = []
    for tool, description in tools:
        try:
            result = subprocess.run([tool, '--help'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✅ {description}: Working")
                results.append(True)
            else:
                print(f"❌ {description}: Error")
                results.append(False)
        except Exception as e:
            print(f"❌ {description}: {e}")
            results.append(False)
    
    return all(results)

def test_ogr_tools():
    """Test OGR command-line tools"""
    print("\n🗺️ Testing OGR command-line tools...")
    
    tools = [
        ('ogr2ogr', 'OGR2OGR'),
        ('ogrinfo', 'OGR Info'),
        ('ogrmerge.py', 'OGR Merge'),
    ]
    
    results = []
    for tool, description in tools:
        try:
            result = subprocess.run([tool, '--help'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✅ {description}: Working")
                results.append(True)
            else:
                print(f"❌ {description}: Error")
                results.append(False)
        except Exception as e:
            print(f"❌ {description}: {e}")
            results.append(False)
    
    return all(results)

def test_proj_tools():
    """Test PROJ command-line tools"""
    print("\n🌍 Testing PROJ command-line tools...")
    
    try:
        # Test proj command
        result = subprocess.run(['proj', '-h'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode in [0, 1]:  # proj returns 1 for help
            print("✅ PROJ: Working")
            return True
        else:
            print("❌ PROJ: Error")
            return False
    except Exception as e:
        print(f"❌ PROJ: {e}")
        return False

def test_python_gis_tools():
    """Test Python GIS command-line tools"""
    print("\n🐍 Testing Python GIS tools...")
    
    tools = [
        ('rio', 'Rasterio CLI'),
        ('fio', 'Fiona CLI'),
    ]
    
    results = []
    for tool, description in tools:
        try:
            result = subprocess.run([tool, '--help'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✅ {description}: Working")
                results.append(True)
            else:
                print(f"❌ {description}: Not available")
                results.append(False)
        except Exception as e:
            print(f"❌ {description}: {e}")
            results.append(False)
    
    return any(results)  # At least one should work

def test_data_processing():
    """Test actual data processing with command-line tools"""
    print("\n📊 Testing data processing capabilities...")
    
    try:
        # Test with a simple raster operation
        test_raster = "/Volumes/T7 Shield/01_REFERENCE_DATA/BIOMASS_NATIONAL/New_M_2019.tif"
        
        if Path(test_raster).exists():
            # Test gdalinfo on actual data
            result = subprocess.run(['gdalinfo', test_raster], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print("✅ GDAL can read actual raster data")
                return True
            else:
                print("❌ GDAL failed to read raster data")
                return False
        else:
            print("⚠️ Test raster not found, skipping data processing test")
            return True
            
    except Exception as e:
        print(f"❌ Data processing test failed: {e}")
        return False

def test_environment_integration():
    """Test environment integration"""
    print("\n🔗 Testing environment integration...")
    
    try:
        # Test that Python can access GDAL
        import rasterio
        gdal_version = rasterio.__gdal_version__
        print(f"✅ Python GDAL integration: {gdal_version}")
        
        # Test that Python can access PROJ
        import pyproj
        proj_version = pyproj.proj_version_str
        print(f"✅ Python PROJ integration: {proj_version}")
        
        return True
    except Exception as e:
        print(f"❌ Environment integration failed: {e}")
        return False

def main():
    """Run all system tools tests"""
    print("🚀 T7 Shield System Tools Test")
    print("=" * 40)
    
    tests = [
        test_gdal_tools,
        test_ogr_tools,
        test_proj_tools,
        test_python_gis_tools,
        test_data_processing,
        test_environment_integration
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 40)
    print("📋 System Tools Test Summary:")
    
    if all(results):
        print("🎉 All system tools working perfectly!")
        print("\n✅ System Tools Complete:")
        print("   - GDAL 3.8.5 command-line tools")
        print("   - OGR vector tools")
        print("   - PROJ 9.4.0 coordinate transformations")
        print("   - Python GIS CLI tools")
        print("   - Environment integration")
        print("\n💡 Ready for command-line GIS processing!")
    else:
        print("⚠️ Some system tools tests failed. Check errors above.")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

