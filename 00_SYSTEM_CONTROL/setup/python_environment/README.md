# T7 Shield Professional GIS Python Environment

A comprehensive Python environment for Australian forestry, carbon accounting, and GIS analysis work.

## Quick Start

### 1. Create Environment
```bash
# Navigate to configs directory
cd "/Volumes/T7 Shield/10_PYTHON_ENVIRONMENT/configs"

# Create conda environment
conda env create -f gis_environment.yml

# Activate environment
conda activate t7_gis_professional
```

### 2. Verify Installation
```bash
# Test imports
python -c "import geopandas, rasterio, qgis.core; print('GIS environment ready!')"
```

### 3. Launch Jupyter Lab
```bash
cd "/Volumes/T7 Shield/10_PYTHON_ENVIRONMENT/notebooks"
jupyter lab
```

## Directory Structure

```
10_PYTHON_ENVIRONMENT/
├── configs/              # Environment configurations
│   ├── gis_environment.yml
│   └── requirements.txt
├── environments/         # Conda environment backups
├── scripts/             # Reusable Python scripts
│   ├── data_processing/
│   ├── spatial_analysis/
│   └── fullcam_integration/
├── notebooks/           # Jupyter analysis notebooks
│   ├── exploratory/
│   ├── analysis/
│   └── reporting/
└── tools/              # Custom GIS tools
    ├── qgis_plugins/
    └── processing_algorithms/
```

## Key Features

- **Full GIS Stack**: GeoPandas, Rasterio, QGIS integration
- **Performance**: Dask for large dataset processing
- **Australian Focus**: Configured for GDA2020, FullCAM workflows
- **Professional**: Code quality tools, testing, documentation

## Environment Management

### Backup Current Environment
```bash
conda env export > environments/t7_gis_$(date +%Y%m%d).yml
```

### Update Environment
```bash
conda env update -f configs/gis_environment.yml
```

### Remove Environment
```bash
conda env remove -n t7_gis_professional
```

## Integration with Existing Workflow

This environment integrates seamlessly with your existing T7 Shield structure:

- **Reference Data**: Direct access to `/01_REFERENCE_DATA/`
- **Client Projects**: Process files in `/02_CLIENT_PROJECTS/`
- **FullCAM**: Support scripts for `/08_KNOWLEDGE BASE/fullcam-docs/`
- **Templates**: Generate from `/04_TEMPLATES_LAYOUTS/`

## Support

For issues or questions:
1. Check the notebooks in `/notebooks/` for examples
2. Review scripts in `/scripts/` for common workflows
3. Consult FullCAM documentation in `/08_KNOWLEDGE BASE/`