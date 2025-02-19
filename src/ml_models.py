import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from config import FINAL_SCORED_FILE, MODEL_OUTPUT_DIR

# Assurez-vous que le dossier de sortie existe
os.makedirs(MODEL_OUTPUT_DIR, exist_ok=True)

def load_data(filepath=FINAL_SCORED_FILE):
    """
    Charge les donnes contenant les scores ESG et les caracteristiques des entreprises 
    """
    try:
        df = pd.read_csv(filepath, delimiter=",", encoding="utf-8", quotechar='"', on_bad_lines='skip')
        # Nettoyage des noms de colonnes (suppression des espaces inutiles)
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des donnees : {e}")
        return None
    
def preprocess_data(df):
    """
    Prépare les données pour l'entraînement du modèle.
    Sépare les variables explicatives et la variable cible (ESG_Score).
    Applique l'encodage et la normalisation nécessaires.
    """
    # Renommer pour uniformiser (Total ESG Risk score -> Total ESG Risk Score)
    df.rename(columns={'Total ESG Risk score': 'Total ESG Risk Score'}, inplace=True)
    
    # Vérifier que la colonne cible existe
    if "ESG_Score" not in df.columns:
        raise ValueError("La colonne 'ESG_Score' n'existe pas dans le DataFrame.")
    
    # Supprimer les lignes sans score ESG
    df = df.dropna(subset=["ESG_Score"])
    
    # Liste des colonnes numériques attendues
    numerical_features = [
        "Total ESG Risk Score", "Environment Risk Score", 
        "Social Risk Score", "Governance Risk Score", "Controversy Score", "Full Time Employees"
    ]
    # Garder uniquement celles présentes dans le DataFrame
    numerical_features = [col for col in numerical_features if col in df.columns]
    
    
    
    # Pour chaque colonne numérique, supprimer les virgules, tenter la conversion en float,
    # et supprimer les lignes posant problème (ex: '78th percentile')
    for col in numerical_features:
        # Supprimer les virgules
        cleaned = df[col].astype(str).str.replace(",", "")
        # Convertir en float en remplaçant les erreurs par NaN
        df[col] = pd.to_numeric(cleaned, errors='coerce')
        # Supprimer les lignes où la conversion a échoué
        df = df.dropna(subset=[col])
    
    # Séparer les features explicatives (X) et la cible (y)
    # On supprime les colonnes non explicatives
    drop_cols = ["Symbol", "Name", "Address", "Description", "ESG_Score", "ESG Risk Percentile"]
    X = df.drop(columns=drop_cols)
    y = df["ESG_Score"].astype(float)
    
    # Identification des colonnes catégorielles déjà encodées (elles sont issues d'un one-hot encoding)
    # Ici, on considère que toutes les colonnes restantes qui ne sont pas numériques sont déjà encodées.
    categorical_features = [col for col in X.columns if col not in numerical_features]
    
    # Création du préprocesseur : normalisation des variables numériques, et passage direct des autres colonnes
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_features)
        ],
        remainder='passthrough'
    )
    
    return X, y, preprocessor

def train_models(X, y, preprocessor):
    """
    Entraine plusieurs modeles de machine learning et evaluer leurs performances. 
    Sauvegarde le meilleur modele dans un fichier.
    """
    # Separation des donnees en train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Modeles a tester
    models = {
        "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
        "RidgeRegression": Ridge(alpha=1.0)
    }

    best_model = None
    best_score = -np.inf

    for name, model in models.items():
        pipeline = Pipeline([("preprocessor", preprocessor), ("model", model)])

        # Entrement du modele
        pipeline.fit(X_train, y_train)

        # Predictions et evaluation
        y_pred = pipeline.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)

        print(f"Modele : {name}")
        print(f" - MAE : {mae}")
        print(f" - RMSE : {rmse}")
        print(f" - R2 : {r2:2f}\n")

        # Selection du meilleur modele
        if r2 > best_score:
            best_score = r2
            best_model = pipeline
            best_model_name = name

        # Sauvegarde du meilleur modele
        if best_model:
            model_path = os.path.join(MODEL_OUTPUT_DIR, f"{best_model_name}_best_model.pkl")
            joblib.dump(best_model, model_path)
            print(f"Meilleur modele sauvegarde : {best_model_name} -> {model_path}")

def main():
    """
    Fonction principale pour charger, pretraiter, entrainer et sauvegarder les modeles.
    """
    df = load_data()
    if df is not None:
        X, y, preprocessor = preprocess_data(df)
        train_models(X, y, preprocessor)
    else:
        print("Erreur : impossible de charger les donnes pour l'entrainement.")

if __name__ == "__main__":
    main()