## 🌿 Green Energy Korea Project

A spatial and financial analysis of renewable energy investment equity in South Korea (2015–2023).

# 📌 Overview

This repository presents a geospatial and econometric study on renewable energy development in South Korea. We constructed a custom Renewable Energy Potential Index (REPI) using national solar, wind, land use, and population datasets. The REPI was then compared with financial investment flows, green bond activity, and CO₂ emissions to uncover regional disparities and urban bias in national energy planning.

**This project integrates**

- Open-source GIS mapping

- Financial and emission regression models

- Green bond policy analysis

- Interactive REPI heatmaps & LISA spatial clustering

📁 *Repository Structure*

Green_Energy_Korea_Project/
├── data/
│   ├── raw/                # Original datasets (CSV, XLS)
│   └── processed/          # Cleaned or filtered data
├── notebooks/
│   └── south-korea.ipynb   # Main Jupyter notebook (analysis + visualizations)
├── scripts/                # Optional Python/R modules for modeling
├── figures/                # Exported figures for publication
├── outputs/                # Results: maps, graphs, reports
├── README.md               # This file
└── LICENSE

# 🧪 Research Objectives

Construct a Renewable Energy Potential Index (REPI) based on ecological and demographic indicators.

Analyze financial equity by correlating REPI with municipal investment and green bond flows.

Evaluate spatial autocorrelation of investment patterns using Moran’s I and LISA.

Propose policy reforms (REPI-linked subsidies, GIS capacity building, municipal green bond frameworks).

# 📊 Key Results and Visualizations

*REPI vs Investment Scatter Plot*



Interpretation: Jeju, Jeonbuk, and Gangwon had high REPI values but were underfunded. Urban areas with moderate REPI received majority investments.

*Green Bonds vs CO₂ Emissions*



Interpretation: Municipalities with active green bond programs like Gwangju show sharp reductions in CO₂ emissions.

*LISA Cluster Map*



Interpretation: High-high clusters in Seoul/Gyeonggi; low-low clusters in Jeju and Jeonbuk, highlighting systemic spatial inequality.

*GHG Emissions by Sector (Pie Chart)*



Interpretation: Industrial and transportation sectors dominate emissions; regional policies must be sector-aware.

# 📍 Technologies Used

Python (Pandas, GeoPandas, Folium, Matplotlib)

R (spdep, tidyverse, ggplot2)

ArcGIS Pro

QGIS (optional cross-check)

World Bank API, KOSIS, KEA, KMA Datasets

# 📂 Datasets

All raw data are located in data/raw/, including:

Korea Renewable Investment (2015–2023)

Solar Radiation & Wind Speed Rasters

Land Cover Classification

Population Pressure Metrics

Green Bond Issuance

CO₂ Emissions by Sector

Note: Large datasets (>1GB) are referenced via Kaggle or external links in the notebook.

# 🧠 How to Use

Clone the repository and run the notebook:

git clone https://github.com/yourusername/Green_Energy_Korea_Project.git
cd Green_Energy_Korea_Project/notebooks
jupyter notebook south-korea.ipynb

You may need to install dependencies:

pip install geopandas folium matplotlib pandas openpyxl

# 🧾 Citation

Maria Jose Lopez Mansueti. "Targeting Regional Climate Action: A Geospatial and Financial Analysis of Renewable Energy Investment in South Korea." 2025.[Preprint link or journal if submitted].

# 🤝 Contributions

Pull requests and forks are welcome. Please cite the original author if reusing this methodology or code.

# 📬 Contact

Author: Maria Jose Lopez Mansueti Email: majolopezmansueti@gmail.com

# 📄 License

This project is licensed under the MIT License – see the LICENSE file for details.

