# T7 Shield Professional GIS Environment - Quick Start Guide

Welcome to your bulletproof, professional-grade GIS environment for Australian forestry and carbon accounting work!

## 🚀 Getting Started

### 1. Activate the Environment
```bash
# Navigate to the Python environment
cd "/Volumes/T7 Shield/10_PYTHON_ENVIRONMENT"

# Activate the conda environment
conda activate t7_gis_professional

# Verify installation
python -c "import geopandas, rasterio, qgis.core; print('✓ GIS environment ready!')"
```

### 2. Launch Jupyter Lab
```bash
# Start Jupyter Lab for interactive analysis
cd notebooks/
jupyter lab

# Your browser will open with the Jupyter interface
# Start with: exploratory/01_T7_Shield_Data_Exploration.ipynb
```

### 3. Test GIS Integration (macOS M2 Safe)
```bash
# Run the safe QGIS integration test (no crashes)
cd scripts/data_processing/
python qgis_integration_safe.py
```

**Note for macOS M2 Users**: Direct PyQGIS integration may cause crashes on M2 chips. Use the safe version (`qgis_integration_safe.py`) which provides all QGIS functionality through stable GeoPandas/Rasterio operations.

## 📁 Directory Structure

```
10_PYTHON_ENVIRONMENT/
├── README.md                 # Comprehensive documentation
├── QUICKSTART_GUIDE.md      # This guide
├── configs/                 # Environment configurations
│   ├── gis_environment.yml  # Conda environment spec
│   └── requirements.txt     # Python packages list
├── scripts/                 # Production-ready scripts
│   ├── data_processing/     # GIS processing tools
│   ├── spatial_analysis/    # Analysis algorithms
│   └── fullcam_integration/ # AWS WorkSpaces FullCAM tools
├── notebooks/               # Jupyter analysis notebooks
│   ├── exploratory/         # Data exploration
│   ├── analysis/           # Detailed analysis workflows  
│   └── reporting/          # Report generation
└── tools/                  # Custom development tools
    ├── qgis_plugins/       # Custom QGIS plugins
    └── processing_algorithms/ # Custom algorithms
```

## ⚡ Quick Tasks

### Load Australian Reference Data
```python
import geopandas as gpd
from pathlib import Path

# Load state boundaries
states = gpd.read_file("/Volumes/T7 Shield/01_REFERENCE_DATA/BOUNDARIES/STATE_BOUNDARIES/STE_2021_AUST_GDA2020.shp")
print(f"Loaded {len(states)} states/territories")

# Load IBRA bioregions  
ibra = gpd.read_file("/Volumes/T7 Shield/01_REFERENCE_DATA/BOUNDARIES/BIOREGIONS_IBRA/IBRA7_subregions.shp")
print(f"Loaded {len(ibra)} bioregions")
```

### Process Client Project Data
```python
# Use the QGIS integration module
from scripts.data_processing.qgis_integration import load_reference_data, process_client_project_data

# Load reference layer
layer = load_reference_data("States", "BOUNDARIES/STATE_BOUNDARIES/STE_2021_AUST_GDA2020.shp")

# Process client data (example)
process_client_project_data("MARY_SPRINGS_EP_WA", "buffer_analysis", 
                           input_layer=layer, buffer_distance=1000)
```

### Prepare FullCAM Data Package
```python
from scripts.fullcam_integration.aws_workspaces_transfer import AWSWorkSpacesTransfer

# Initialize transfer manager
transfer_manager = AWSWorkSpacesTransfer()

# Create data package for AWS WorkSpaces
project_data = {
    'name': 'Mary_Springs_Environmental_Planting',
    'method': 'environmental_plantings',
    'total_area_ha': 150.0,
    'establishment_year': 2025,
    'spatial_files': [
        {'path': '/Volumes/T7 Shield/02_CLIENT_PROJECTS/MARY_SPRINGS_EP_WA/boundary.gpkg', 'type': 'boundary'}
    ]
}

package_path = transfer_manager.create_fullcam_data_package("mary_springs", project_data)
print(f"FullCAM package ready: {package_path}")
```

## 🎯 Common Workflows

### 1. New Client Project Analysis
1. Create project directory in `/02_CLIENT_PROJECTS/`
2. Use `notebooks/exploratory/01_T7_Shield_Data_Exploration.ipynb` as template
3. Load project boundaries and reference data
4. Perform spatial analysis using QGIS integration tools
5. Generate reports and visualizations

### 2. FullCAM Carbon Accounting
1. Prepare project data using `scripts/fullcam_integration/fullcam_data_preparation.py`
2. Create AWS WorkSpaces transfer package
3. Transfer to Windows environment via AWS WorkSpaces
4. Run FullCAM analysis on Windows
5. Process results back on T7 Shield

### 3. Reference Data Analysis
1. Use existing reference datasets in `/01_REFERENCE_DATA/`
2. Extract relevant data for project areas
3. Perform overlays and spatial joins
4. Create summary statistics and visualizations

## 🔧 Key Features

### ✅ Complete GIS Stack
- **GeoPandas 1.1+**: Vector data processing
- **Rasterio 1.3+**: Raster data handling  
- **QGIS 3.34**: Full QGIS integration
- **Shapely 2.0+**: Geometric operations
- **PyProj 3.6+**: Coordinate transformations

### ✅ Performance Optimized
- **Dask**: Large dataset processing
- **Xarray**: Multi-dimensional data
- **Parallel processing**: Multi-core support
- **Memory efficient**: Optimized data types

### ✅ Australian Forestry Focus
- **GDA2020 support**: Latest Australian datum
- **FullCAM integration**: AWS WorkSpaces workflow
- **IBRA regions**: Biogeographic data
- **Forest productivity**: Site potential analysis

### ✅ Professional Development
- **Jupyter Lab**: Interactive analysis
- **Code quality**: Black, flake8, pytest
- **Documentation**: Comprehensive guides
- **Version control**: Git ready

## 🔄 AWS WorkSpaces FullCAM Workflow

Since FullCAM is Windows-only and you're on macOS M2:

1. **Prepare on T7 Shield (macOS)**
   ```python
   # Create transfer package
   package = transfer_manager.create_fullcam_data_package(project_name, data)
   ```

2. **Transfer to AWS WorkSpaces**
   - Connect to AWS WorkSpaces
   - Transfer ZIP package to Windows environment
   - Extract maintaining directory structure

3. **Run FullCAM (Windows)**
   - Open FullCAM application
   - Import spatial data and Excel template
   - Configure analysis parameters
   - Generate carbon calculations

4. **Return Results**
   - Export all FullCAM outputs
   - ZIP results package
   - Transfer back to T7 Shield

5. **Process Results (macOS)**
   ```python
   # Analyze returned results  
   results = transfer_manager.process_fullcam_outputs(results_zip, project_name)
   ```

## 🆘 Troubleshooting

### Environment Issues
```bash
# Recreate environment if needed
conda env remove -n t7_gis_professional
conda env create -f configs/gis_environment.yml
```

### QGIS Integration Problems
```bash
# Test QGIS availability
python -c "import qgis.core; print('QGIS available')"

# If fails, check conda environment
conda list qgis
```

### Large Dataset Performance
```python
# Use Dask for large datasets
import dask_geopandas as dgpd
ddf = dgpd.read_file("large_dataset.shp", npartitions=4)
result = ddf.groupby('attribute').sum().compute()
```

## 📞 Support

- **Documentation**: Check `README.md` for detailed information
- **Examples**: Explore notebooks in `notebooks/exploratory/`
- **Scripts**: Review `scripts/` for production workflows
- **FullCAM**: Consult `/08_KNOWLEDGE BASE/fullcam-docs/`

## 🎉 You're Ready!

Your T7 Shield professional GIS environment is fully configured and ready for:
- ✅ Australian forestry analysis
- ✅ Carbon accounting workflows  
- ✅ FullCAM data preparation
- ✅ Professional GIS operations
- ✅ Large-scale data processing

Start with the exploration notebook and build from there. Happy analyzing! 🌳📊