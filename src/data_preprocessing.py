# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:00:00 2025

@author: Roslan Paul NZAMBA NZAMBA
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the ESG data by handling missing values and outliers."""
    try:
        # Convertir "ESG Risk Percentile" en float (ex: "50th percentile" -> 0.50)
        if "ESG Risk Percentile" in df.columns:
            df["ESG Risk Percentile"] = df["ESG Risk Percentile"].str.extract("(\d+)").astype(float) / 100
            logger.info("Converted 'ESG Risk Percentile' to numeric.")
            
        # Handle missing values by filling with the mean
        df.fillna(df.mean(numeric_only=True), inplace=True)
        logger.info("Missing values filled with mean.")
        
        # Standardization (Z-score) and Min-Max scaling
        scaler_minmax = MinMaxScaler()
        scaler_standard = StandardScaler()

        numeric_cols_minmax = ['Total ESG Risk score', 'Environment Risk Score', 'Governance Risk Score', 'Social Risk Score']
        numeric_cols_standard = ['Controversy Score', 'ESG Risk Percentile']
        
        df[numeric_cols_minmax] = scaler_minmax.fit_transform(df[numeric_cols_minmax])
        df[numeric_cols_standard] = scaler_standard.fit_transform(df[numeric_cols_standard])
        logger.info("Data normalized and standardized.")
        
        # Handle outliers using winsorization (clipping extreme values)
        for col in numeric_cols_minmax:
            df[col] = np.clip(df[col], df[col].quantile(0.05), df[col].quantile(0.95))
        logger.info("Outliers handled using winsorization.")
        
        return df
    
    except Exception as e:
        logger.error(f"Error cleaning data: {str(e)}")
        raise

def save_cleaned_data(df: pd.DataFrame, output_dir: str, filename: str = "cleaned_esg_data.csv"):
    """Save the cleaned ESG data to a CSV file."""
    try:
        file_path = Path(output_dir) / filename
        df.to_csv(file_path, index=False)
        logger.info(f"Cleaned data saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving cleaned data: {str(e)}")
        raise
