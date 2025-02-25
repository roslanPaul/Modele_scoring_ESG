# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:07:13 2025

@author: Roslan Paul NZAMBA NZAMBA
"""

import os

# Definition des chemins principaux
BASE_DIR = r"C:\Users\HP\OneDrive\Documenten\1-Projects\Professionnel\Projets pro\Modele_scoring_ESG"
DATA_DIR = os.path.join(BASE_DIR, "data\\")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
CLEANED_DATA_DIR = os.path.join(DATA_DIR, "cleaned")
NOTEBOOKS_DIR = os.path.join(BASE_DIR, "notebooks")
SRC_DIR = os.path.join(BASE_DIR, "src")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
FIGURES_DIR = os.path.join(REPORTS_DIR, "figures")
VISUALIZATION_OUTPUT_DIR = os.path.join(FIGURES_DIR, "visualizations")  
MODEL_OUTPUT_DIR = os.path.join(BASE_DIR, "models")


# Ajout ici

# Fichiers de donnees
RAW_DATA_FILE = os.path.join(RAW_DATA_DIR, "SP 500 ESG Risk Ratings.csv")
CLEANED_DATA_FILE = os.path.join(CLEANED_DATA_DIR, "cleaned_esg_data.csv")
FINAL_SCORED_FILE = os.path.join(CLEANED_DATA_DIR, "final_scored_data.csv")

# Colonnes des donnes ESG
COLUMN_NAMES = [
    "Symbol", "Name", "Address", "Sector", "Industry", "Full Time Employees", "Description", "Total ESG Risk Score", "Environment Risk Score", "Governance Risk Score", "Social Risk Score", "Controversy Level", "Controversy Score", "ESG Risk Percentile", "ESG Risk Level"
    ]

# Colonnes numeriques pour analyse statistique et normalisation
NUMERIC_COLUMNS = [
    "Total ESG Risk Score", "Environment Risk Score", "Governance Risk Score", "Social Risk Score", "Controversy Score"
    ]

# Colonnes categorielles
CATEGORICAL_COLUMNS = ["Sector", "Industry", "Controversy Level", "ESG Risk Level"]

# Parametres de nettoyage des donnees
MISSING_VALUES_THRESHOLD = 0.3 # Supprime les colonnes avec plus de 30% de valeurs manquantes
CATEGORICAL_ENCODING_METHOD = "one_hot" # Methode d'encodage des variables categorielles
OUTLIER_REMOVAL_METHOD = "z_score" # Methode de suppression aberrantes

# Parametres de scoring ESG (ponderations)
ESG_WEIGHTS = {
    "Environment Risk Score": 0.4,
    "Social Risk Score": 0.3,
    "Governance Risk Score": 0.3,
    }

# Parametres des modeles Machine Learning
ML_MODEL_PARAMS = {
    "random_forest": {
        "n_estimators": 100,
        "max_depth": None,
        "random_state": 42,
        },
    "xgboost": {
        "n_estimators": 200,
        "learning_rate": 0.05,
        "max_depth": 6,
        "random_state": 42,
        },
    }

# Autres parametres
RANDOM_SEED = 42 # Assurer la reproductibilite des resultats
LOG_LEVEL = "INFO" # Niveau de log : DEBUG, INFO, WARNING ERROR, CRITICAL

# Création des répertoires nécessaires s'ils n'existent pas
def create_directories():
    directories = [
        DATA_DIR,
        RAW_DATA_DIR,
        CLEANED_DATA_DIR,
        NOTEBOOKS_DIR,
        SRC_DIR,
        REPORTS_DIR,
        FIGURES_DIR,
        VISUALIZATION_OUTPUT_DIR,
        MODEL_OUTPUT_DIR
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Création du répertoire : {directory}")

if __name__ == "__main__":
    print("Configuration chargee avec succes.")

































