# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:10:00 2025

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import FINAL_SCORED_FILE, VISUALIZATION_OUTPUT_DIR

# S'assure que le dossier sortie existe
import os
os.makedirs(VISUALIZATION_OUTPUT_DIR, exist_ok=True)

def load_scored_data(filepath=FINAL_SCORED_FILE):
    """
    Charge les donnees contenant les scores ESG.
    """
    try:
        df = pd.read_csv(filepath, delimiter=",", encoding="utf-8", quotechar='"')
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des donnees ESG scorees : {e}")
        return None
    
def plot_esg_distribution(df):
    """ 
    Visualise la distribution des scores ESG.
    """
   
       
    plt.figure(figsize=(10,5))
    sns.histplot(df["ESG_Score"], bins=20, kde=True, color="blue")
    plt.title("Distribution des scores ESG")
    plt.xlabel("Score ESG")
    plt.ylabel("Nombre d'entreprises")
    plt.grid()
    plt.savefig(os.path.join(VISUALIZATION_OUTPUT_DIR, "esg_distribution.png"))
    plt.show()
    
def plot_sector_esg_scores(df):
    """
    Visualise la moyenne des scores ESG par secteur.
    """ 
    # Identifier les colonnes de secteur
    sector_columns = [col for col in df.columns if col.startswith('Sector_')]
    
    # Créer une nouvelle colonne 'Sector' basée sur les colonnes one-hot
    df['Sector'] = ''
    for col in sector_columns:
        sector_name = col.replace('Sector_', '')
        df.loc[df[col] == 1, 'Sector'] = sector_name
       
    plt.figure(figsize=(12,6))
    sector_scores = df.groupby("Sector")["ESG_Score"].mean().sort_values()
    sector_scores.plot(kind="barh", color="green")
    plt.title("Score ESG moyen par secteur")
    plt.xlabel("Score ESG moyen")
    plt.ylabel("Secteur")
    plt.grid()
    plt.savefig(os.path.join(VISUALIZATION_OUTPUT_DIR, "sector_esg_scores.png"))
    plt.show()
    
def plot_esg_components(df):
    """
    Compare les composantes des Scores ESG

    """
    plt.figure(figsize=(10,5))
    df_melted = df.melt(id_vars=["Symbol", "Name"],
                        value_vars=["Environment Risk Score", "Social Risk Score", "Governance Risk Score"],
                        var_name="Component",
                        value_name="Score")
    
    # Version corrigée utilisant hue au lieu de palette directement
    sns.boxplot(data=df_melted, 
                x="Component", 
                y="Score", 
                hue="Component",  # Ajout du paramètre hue
                legend=False)     # Suppression de la légende car redondante
    
    plt.title("Comparaison des composantes ESG")
    plt.grid()
    plt.savefig(os.path.join(VISUALIZATION_OUTPUT_DIR, "esg_components_comparison.png"))
    plt.show()
    
def generate_visualizations():
    """
    Charge les donnees et genere toutes les visualisations.
    """
    df = load_scored_data()
    if df is not None:
        plot_esg_distribution(df)
        plot_sector_esg_scores(df)
        plot_esg_components(df)
    else:
        print("Impossible de generer les visualisations en raison d'une erreur de chargement des donnees.")
        
if __name__=="__main__":
    generate_visualizations()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    