
"""
data_pipeline.py

Automates downloading raw data via Kaggle API and processing it into cleaned CSVs.
"""

import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from docx import Document

# Paths
RAW_DIR = 'data/raw'
PROCESSED_DIR = 'data/processed'

# Ensure directories exist
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Kaggle dataset details
KAGGLE_DATASET = 'your-username/your-dataset-slug'  # Replace with your Kaggle dataset slug

def download_raw_data():
    """Download raw files from Kaggle."""
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(KAGGLE_DATASET, path=RAW_DIR, unzip=True)
    print('Raw data downloaded to', RAW_DIR)

def load_raw_files():
    """Load raw CSV, Excel, and DOCX files into DataFrames."""
    # Time-series indicators
    df_ind = pd.read_csv(os.path.join(RAW_DIR, 'API_KOR_DS2_en_csv_v2_15934.csv'), skiprows=4)
    country_meta = pd.read_csv(os.path.join(RAW_DIR, 'Metadata_Country_API_KOR_DS2_en_csv_v2_15934.csv'))
    indicator_meta = pd.read_csv(os.path.join(RAW_DIR, 'Metadata_Indicator_API_KOR_DS2_en_csv_v2_15934.csv'))
    muni_stats = pd.read_excel(os.path.join(RAW_DIR, 'Korea Rep Data v2.xls'))
    
    # DOCX parsing for municipalities
    doc = Document(os.path.join(RAW_DIR, 'AAA Municipality.docx'))
    muni_list = []
    for para in doc.paragraphs:
        if "\t" in para.text:
            code, name = para.text.split("\t", 1)
            muni_list.append({'MunicipalityCode': code.strip(), 'MunicipalityName': name.strip()})
    muni_meta = pd.DataFrame(muni_list)
    
    return df_ind, country_meta, indicator_meta, muni_stats, muni_meta

def clean_and_process(df_ind, country_meta, indicator_meta, muni_stats, muni_meta):
    """Clean, standardize, and save processed CSVs."""
    # Melt indicators to long format, filter years 2020-2023
    ind_long = df_ind.melt(
        id_vars=['Country Name','Country Code','Indicator Name','Indicator Code'],
        var_name='Year', value_name='Value'
    )
    ind_long = ind_long[ind_long['Year'].astype(int).between(2020, 2023)]
    ind_long.to_csv(os.path.join(PROCESSED_DIR, 'indicators.csv'), index=False)
    
    # Rename metadata for consistency
    country_meta = country_meta.rename(columns={'Country Code':'CountryCode','Country Name':'CountryName'})
    country_meta.to_csv(os.path.join(PROCESSED_DIR, 'country_metadata.csv'), index=False)
    
    indicator_meta = indicator_meta.rename(columns={'Indicator Code':'IndCode','Indicator Name':'IndName'})
    indicator_meta.to_csv(os.path.join(PROCESSED_DIR, 'indicator_metadata.csv'), index=False)
    
    muni_stats = muni_stats.rename(columns={'Code':'MunicipalityCode'})
    muni_stats.to_csv(os.path.join(PROCESSED_DIR, 'municipal_stats.csv'), index=False)
    
    muni_meta.to_csv(os.path.join(PROCESSED_DIR, 'municipality_metadata.csv'), index=False)
    
    # Merge all into a single dataset
    df = ind_long.merge(country_meta, left_on='Country Code', right_on='CountryCode')
    df = df.merge(indicator_meta, left_on='Indicator Code', right_on='IndCode')
    merged = df.merge(muni_stats, on='MunicipalityCode', how='left')
    merged.to_csv(os.path.join(PROCESSED_DIR, 'merged_dataset.csv'), index=False)
    print('Processed data saved to', PROCESSED_DIR)

if __name__ == '__main__':
    download_raw_data()
    df_ind, country_meta, indicator_meta, muni_stats, muni_meta = load_raw_files()
    clean_and_process(df_ind, country_meta, indicator_meta, muni_stats, muni_meta)
