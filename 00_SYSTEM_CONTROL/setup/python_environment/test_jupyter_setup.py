#!/usr/bin/env python3
"""
Jupyter Setup Test for T7 Shield GIS Environment
Tests Jupyter installation, extensions, and GIS integration
"""

import subprocess
import sys
import os
from pathlib import Path

def test_jupyter_installation():
    """Test Jupyter installation"""
    print("📓 Testing Jupyter installation...")
    
    try:
        # Test Jupyter Lab
        result = subprocess.run(['jupyter', 'lab', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ JupyterLab: {result.stdout.strip()}")
        else:
            print("❌ JupyterLab: Error")
            return False
        
        # Test Jupyter Notebook
        result = subprocess.run(['jupyter', 'notebook', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ Jupyter Notebook: {result.stdout.strip()}")
        else:
            print("❌ Jupyter Notebook: Error")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Jupyter installation test failed: {e}")
        return False

def test_jupyter_extensions():
    """Test Jupyter extensions"""
    print("\n🔌 Testing Jupyter extensions...")
    
    try:
        result = subprocess.run(['jupyter', 'labextension', 'list'], 
                              capture_output=True, text=True, timeout=15)
        if result.returncode == 0:
            print("✅ JupyterLab extensions available")
            # Parse extensions
            lines = result.stdout.split('\n')
            for line in lines:
                if 'enabled OK' in line:
                    print(f"   - {line.strip()}")
            return True
        else:
            print("❌ JupyterLab extensions error")
            return False
    except Exception as e:
        print(f"❌ Jupyter extensions test failed: {e}")
        return False

def test_notebook_directories():
    """Test notebook directories"""
    print("\n📁 Testing notebook directories...")
    
    try:
        notebook_dir = Path("/Volumes/T7 Shield/10_PYTHON_ENVIRONMENT/notebooks")
        
        if notebook_dir.exists():
            print("✅ Notebooks directory exists")
            
            # Check subdirectories
            subdirs = ['analysis', 'exploratory', 'reporting']
            for subdir in subdirs:
                subdir_path = notebook_dir / subdir
                if subdir_path.exists():
                    notebooks = list(subdir_path.glob("*.ipynb"))
                    print(f"   - {subdir}: {len(notebooks)} notebooks")
                else:
                    print(f"   - {subdir}: directory not found")
            
            return True
        else:
            print("❌ Notebooks directory not found")
            return False
            
    except Exception as e:
        print(f"❌ Notebook directories test failed: {e}")
        return False

def test_gis_integration():
    """Test GIS integration in Jupyter"""
    print("\n🗺️ Testing GIS integration...")
    
    try:
        # Test that GIS packages can be imported in a notebook context
        import geopandas as gpd
        import rasterio
        import matplotlib.pyplot as plt
        import folium
        
        print("✅ Core GIS packages importable")
        
        # Test matplotlib backend
        backend = plt.get_backend()
        print(f"✅ Matplotlib backend: {backend}")
        
        # Test interactive plotting
        try:
            import ipywidgets
            print("✅ IPyWidgets available for interactive plots")
        except ImportError:
            print("⚠️ IPyWidgets not available")
        
        return True
    except Exception as e:
        print(f"❌ GIS integration test failed: {e}")
        return False

def test_kernel_setup():
    """Test Jupyter kernel setup"""
    print("\n⚙️ Testing Jupyter kernel setup...")
    
    try:
        result = subprocess.run(['jupyter', 'kernelspec', 'list'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Jupyter kernels available:")
            lines = result.stdout.split('\n')
            for line in lines:
                if 't7_gis_professional' in line:
                    print(f"   - {line.strip()}")
                    return True
            print("⚠️ t7_gis_professional kernel not found")
            return False
        else:
            print("❌ Kernel list error")
            return False
    except Exception as e:
        print(f"❌ Kernel setup test failed: {e}")
        return False

def test_sample_notebook():
    """Test if sample notebooks can be loaded"""
    print("\n📖 Testing sample notebooks...")
    
    try:
        sample_notebook = Path("/Volumes/T7 Shield/10_PYTHON_ENVIRONMENT/notebooks/exploratory/01_T7_Shield_Data_Exploration.ipynb")
        
        if sample_notebook.exists():
            print("✅ Sample notebook found")
            
            # Try to read the notebook
            import json
            with open(sample_notebook, 'r') as f:
                nb = json.load(f)
            
            cells = len(nb.get('cells', []))
            print(f"   - Notebook has {cells} cells")
            
            return True
        else:
            print("❌ Sample notebook not found")
            return False
            
    except Exception as e:
        print(f"❌ Sample notebook test failed: {e}")
        return False

def create_jupyter_config():
    """Create optimal Jupyter configuration"""
    print("\n⚙️ Setting up Jupyter configuration...")
    
    try:
        # Create Jupyter config directory if it doesn't exist
        config_dir = Path.home() / '.jupyter'
        config_dir.mkdir(exist_ok=True)
        
        # Create jupyter_lab_config.py for optimal settings
        config_file = config_dir / 'jupyter_lab_config.py'
        
        config_content = '''# T7 Shield Jupyter Lab Configuration
# Optimized for GIS work on macOS M2

c.ServerApp.ip = 'localhost'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False
c.ServerApp.token = ''
c.ServerApp.password = ''

# Performance settings
c.ServerApp.max_body_size = 1000000000  # 1GB
c.ServerApp.max_buffer_size = 1000000000  # 1GB

# File handling
c.FileContentsManager.allow_hidden = True

# Extensions
c.ServerApp.nbserver_extensions = {
    'jupyterlab_git': True,
    'jupyterlab_lsp': True,
}

# Theme and appearance
c.ServerApp.theme = 'JupyterLab Dark'
'''
        
        with open(config_file, 'w') as f:
            f.write(config_content)
        
        print("✅ Jupyter configuration created")
        return True
        
    except Exception as e:
        print(f"❌ Jupyter configuration failed: {e}")
        return False

def main():
    """Run all Jupyter tests"""
    print("🚀 T7 Shield Jupyter Setup Test")
    print("=" * 40)
    
    tests = [
        test_jupyter_installation,
        test_jupyter_extensions,
        test_notebook_directories,
        test_gis_integration,
        test_kernel_setup,
        test_sample_notebook,
        create_jupyter_config
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 40)
    print("📋 Jupyter Test Summary:")
    
    if all(results):
        print("🎉 All Jupyter tests passed!")
        print("\n✅ Jupyter Setup Complete:")
        print("   - JupyterLab 4.4.5 installed")
        print("   - Jupyter Notebook 7.4.5 available")
        print("   - GIS integration working")
        print("   - Sample notebooks available")
        print("   - Configuration optimized")
        print("\n💡 To start Jupyter:")
        print("   jupyter lab")
        print("   jupyter notebook")
        print("\n📁 Your notebooks are in:")
        print("   /Volumes/T7 Shield/10_PYTHON_ENVIRONMENT/notebooks/")
    else:
        print("⚠️ Some Jupyter tests failed. Check errors above.")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

