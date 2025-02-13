# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:19:24 2025

@author: HP
"""
import pandas as pd
import numpy as np
from config import *

def load_clean_data(filepath=CLEANED_DATA_FILE):
    """
    Charge les donnees nettoyees depuis un fichier CSV.
    """
    
    try:
        df = pd.read_csv(filepath, delimiter=",", encoding="utf-8", quotechar='"')
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des donnees nettoyees: {e}")
        return None
    
def compute_esg_score(df):
    """
    Calcule le score ESG en ponderant les criteres Environnementaux (E), Sociaux (S), Gouvernance (G)
    """
    if not all(weight in df.columns for weight in ESG_WEIGHTS.keys()):
        missing_cols = [col for col in ESG_WEIGHTS.keys() if col not in df.columns]
        raise ValueError(f"Les colonnes suivantes sont manquantes dans les donnees : {missing_cols}")
       
    # Normalisation des valeurs entre 0 et 1 pour eviter les ecarts d'echelle
    for col in ESG_WEIGHTS.keys():
        min_val, max_val = df[col].min(), df[col].max()
        df[col] = (df[col] - min_val)/(max_val - min_val) if max_val > min_val else 0
        
    # Calcul du score ESG pondere
    df["ESG_Score"] = sum(df[col] * weight for col, weight in ESG_WEIGHTS.items())
    
    return df

def save_scored_data(df):
    """ 
    Sauvegarde les donnees avec le score ESG calcule.
    """
    
    try:
        df.to_csv(FINAL_SCORED_FILE, index=False, encoding="utf-8")
        print(f"Scores ESG calcules et sauvegardes dans {FINAL_SCORED_FILE}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des scores ESG : {e}")
        
def process_esg_scoring():
    """ 
    Pipeline complet pour charger les donnees nettoyees, calculer le score ESG et les resultats.
    """ 
    df = load_clean_data()
    if df is not None:
        df = compute_esg_score(df)
        save_scored_data(df)
    else:
        print("Impossible de calculer les scores ESG en raison d'une erreur de chargement des donnees.")

if __name__ == "__main__":
    process_esg_scoring()

