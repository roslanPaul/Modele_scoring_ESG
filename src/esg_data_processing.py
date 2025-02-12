# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:03:16 2025

@author: Roslan Paul NZAMBA NZAMBA
"""

import pandas as pd
import logging
from pathlib import Path

from data_preprocessing import clean_data, save_cleaned_data



def configure_logging():
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('esg_data_processing.log'),
            logging.StreamHandler()
            ]
        )
    return logging.getLogger(__name__)

logger = configure_logging()

def load_esg_data(file_path: str) -> pd.DataFrame:
    """Load ESG data from local CSV file."""
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully loaded data from {file_path}")
        return df
    except Exception as e:
        logger.error(f"Error loading ESG data: {str(e)}")
        raise
        
def save_processed_data(df: pd.DataFrame, output_dir: str, filename: str = "processed_esg_data.csv"):
    """Save the processed ESG data to a CSV file."""
    try:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        file_path = output_path / filename
        df.to_csv(file_path, index=False)
        logger.info(f"Processed data saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving processed data: {str(e)}")
        raise
        
def main():
    """Main function to process ESG data from a local Kaggle dataset."""
    
   
    try:
        input_file = r"C:/Users/HP/OneDrive/Documenten/1-Projects/Professionnel/Projets pro/Modele_scoring_ESG/data/raw/SP 500 ESG Risk Ratings.csv"
        output_folder = r"C:/Users/HP/OneDrive/Documenten/1-Projects/Professionnel/Projets pro/Modele_scoring_ESG/data/processed/"
        
        
        df_esg = load_esg_data(input_file)
        
        df_esg.dropna(inplace=True)
        
        # save_processed_data(df_esg, output_folder)
        
        cleaned_df = clean_data(df_esg)
        save_cleaned_data(cleaned_df, output_folder)
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise
        
if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        