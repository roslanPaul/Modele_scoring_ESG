# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:00:00 2025

@author: Roslan Paul NZAMBA NZAMBA
"""

import os
import pandas as pd
import numpy as np
from config import *


# Assurer la reproductibilite
np.random.seed(RANDOM_SEED)

def load_data(filepath=RAW_DATA_DIR):
    """
    Charge les donnes brutes depuis un fichier CSV.
    """
    try:
        df = pd.read_csv(filepath, delimiter=",", encoding="utf-8", quotechar='"')
        df.columns = [col.strip() for col in df.columns] # Nettoyage des noms de colonnes
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des donnes : {e}")
        return None

def clean_data(df):
    """
    Nettoie les donnees en supprimant les colonnes manquantes,
    en remplissant les valeurs nulles et en normalisant les valeurs numeriques

    """
    # Supprimer les collonnes ayant un trop grand nombre de valeurs manquantes
    missing_ratio = df.isnull().mean()
    cols_to_drop = missing_ratio[missing_ratio > MISSING_VALUES_THRESHOLD].index.tolist()
    df.drop(columns=cols_to_drop, inplace=True)
    
    # Remplir les valeurs manquantes restantes
    for col in df.columns:
        if col in NUMERIC_COLUMNS:
            df[col] = df[col].replace("-", np.nan).astype(float) # Convertir les valeurs "-" en NaN
            df[col] = df[col].fillna(df[col].median()) # Remplacer NaN par la mediane
        elif col in CATEGORICAL_COLUMNS:
            df[col] = df[col].fillna("Unknown") # Remplacer NaN par "Unknown"
    
    return df

def encode_categorical(df):
    """
    Encode les variables categorielles en utilisant One-Hot Encoding ou Label Encoding.
    """
    
    if CATEGORICAL_ENCODING_METHOD == "one_hot":
        df = pd.get_dummies(df, columns=CATEGORICAL_COLUMNS, drop_first=True)
    elif CATEGORICAL_ENCODING_METHOD == "label_encoding":
        from sklearn.preprocessing import LabelEncoder
        for col in CATEGORICAL_COLUMNS:
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col])
    return df

def remove_outliers(df):
    """
    Supprime les valeurs aberrantes des colonnes numeriques.
    """
    if OUTLIER_REMOVAL_METHOD == "z-score":
        from scipy.stats import zscore
        z_scores = df[NUMERIC_COLUMNS].apply(zscore)
        df = df[(np.abs(z_scores) < 3).all(axis=1)]
        
    elif OUTLIER_REMOVAL_METHOD == "iqr":
        Q1 = df[NUMERIC_COLUMNS].quantile(0.25)
        Q3 = df[NUMERIC_COLUMNS].quantile(0.75)
        IQR = Q3 - Q1
        df = df[~((df[NUMERIC_COLUMNS]<(Q1 - 1.5 * IQR)) | (df[NUMERIC_COLUMNS] > (Q3 + 1.5 * IQR))).any(axis=1)]
        
    return df

def preprocess_data():
    """
    Charge, nettoie, encode et filtre les valeurs aberrantes des donnes ESG.
    Sauvegarde les donnes nettoyes dans un fichier CSV.

    """
    df = load_data()
    if df is not None:
        
        df = clean_data(df)
        df = encode_categorical(df)
        df = remove_outliers(df)
        
        df.to_csv(CLEANED_DATA_FILE, index=False, encoding="utf-8")
        print(f"Données nettoyées et sauvegardées dans {CLEANED_DATA_FILE}")

    else:
        print("Echec du pretraitement des donnees.")

if __name__ == "__main__":
    preprocess_data()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    