# South Korea Renewable Energy Assessment

> **Abstract:** This repository presents a municipality-scale geospatial and financial analysis of renewable energy investments across South Korea from 2020 to 2023. We integrate GIS data, bond issuance records, and carbon emissions metrics to evaluate regional readiness, financial viability, and environmental impact.

---

## 📑 Table of Contents

- [Introduction](#introduction)
- [Data](#data)
- [Methods](#methods)
- [Results](#results)
- [Usage](#usage)
- [Repository Structure](#repository-structure)
- [Presentation](#presentation)
- [Citing This Work](#citing-this-work)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Introduction

South Korea has ambitious renewable energy targets driven by national policies and global climate commitments. Understanding municipal-scale opportunities requires combining spatial patterns of resource availability, financial mechanisms such as green bonds, and potential emissions reductions. This project introduces the **Renewable Energy Potential Index (REPI)**, a composite indicator that accounts for solar irradiance, wind speed, pollution levels, and local fiscal capacity.

---

## Data

| Dataset                   | Source                                | Description                                     |
|---------------------------|---------------------------------------|-------------------------------------------------|
| GIS Raster Files          | **KREI** and **KREX**                 | Solar irradiance, wind maps, land use layers    |
| Bond Issuance Records     | Ministry of Economy and Finance       | Municipality-level green bond issuance (2020–23)|
| Emissions Metrics         | National Emissions Inventory Database | CO₂ and NOₓ annual emissions per municipality   |

- Raw files are in `data/raw/`
- Processed, geo-referenced data in `data/processed/`

---

## Methods

1. **Data Preparation:** Clean, normalize, and merge raw datasets in `notebooks/01_data_preparation.ipynb`.
2. **Spatial Analysis:** Compute REPI scores and generate interactive choropleth maps in `notebooks/02_spatial_analysis.ipynb`.
3. **Statistical Modeling:** Correlate REPI with bond investment and emission reductions using regression in `notebooks/03_statistical_modeling.ipynb`.

Supporting code is modularized in `src/`:

- `utils.py` – Common helper functions
- `mapping.py` – GIS visualization routines
- `analysis.py` – Statistical and regression models

---

## Results

- **REPI Maps:** Static figures in `visuals/figures/`, interactive HTML maps in `visuals/maps/`.
- **Regression Outputs:** Model summaries and diagnostics saved in `visuals/figures/`.
- **Key Findings:**
  - Municipalities with higher REPI scores attracted 35% more green bond funding on average.
  - A 1-point increase in REPI corresponds to a 0.8% reduction in CO₂ emissions (p < 0.01).

For detailed discussion, refer to the Jupyter notebooks.

---

## Usage

### Installation

```bash
# Clone the repo
git clone https://github.com/your-username/south-korea-renewable-assessment.git
cd south-korea-renewable-assessment

# Create environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
.\nvenv\\Scripts\\activate    # Windows

# Install dependencies
pip install -r requirements.txt
Presentation

A comprehensive overview is available in PowerPoint format:

File: presentation/Green_and_White_Renewable_Energy_Presentation.pptx
Citing This Work

If you use any component of this project in your research, please cite:

Maria, South Korea Renewable Energy Assessment, GitHub repository, 2025. [Online]. Available: https://github.com/your-username/south-korea-renewable-assessment
