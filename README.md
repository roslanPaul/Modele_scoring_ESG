# 🌱 ESG Scoring Model using Machine Learning

Ce projet a pour objectif de construire un modèle de **scoring ESG (Environnemental, Social et Gouvernance)** à partir de données financières et extra-financières en utilisant des algorithmes de **machine learning**. Il s'inscrit dans une logique de finance responsable et vise à aider les parties prenantes à mieux évaluer la performance durable des entreprises.

---

## 📁 Structure du Projet

```bash
Modele_scoring_ESG/
│
├── data/
│   ├── raw_data/               # Données brutes (CSV ou téléchargées depuis Kaggle)
│   ├── processed_data/         # Données nettoyées et prétraitées
│
├── notebooks/
│   ├── 01_data_collection.ipynb        # Collecte et chargement des données
│   ├── 02_data_cleaning.ipynb          # Nettoyage des données
│   ├── 03_feature_engineering.ipynb    # Transformation des variables
│   ├── 04_model_training.ipynb         # Entraînement des modèles ML
│   └── 05_visualization.ipynb          # Visualisation et interprétation
│
├── src/
│   ├── config.py                # Fichier de configuration global
│   ├── data_preprocessing.py   # Fonctions de nettoyage et de traitement
│   ├── ml_models.py            # Modèles de machine learning
│   ├── esg_scoring.py          # Calcul des scores ESG
│   └── visualization.py        # Fonctions de visualisation
│
├── reports/                    # Rapports, figures et exports
│
├── requirements.txt            # Liste des packages Python
├── README.md                   # Description du projet
└── .gitignore                  # Fichiers à ignorer dans le versionning
```

---

## 🎯 Objectifs

- Intégrer des données ESG issues de sources variées (Kaggle, CSV locaux)
- Nettoyer, transformer et enrichir ces données
- Construire un **modèle de scoring ESG** interprétable
- Utiliser des algorithmes comme **Random Forest** et **XGBoost**
- Visualiser les résultats avec des dashboards interactifs

---

## ⚙️ Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/votre-utilisateur/Modele_scoring_ESG.git
   cd Modele_scoring_ESG
   ```

2. **Créer un environnement virtuel :**
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/macOS
   env\Scripts\activate     # Windows
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧠 Modèles de Machine Learning

Les algorithmes utilisés incluent :
- **Random Forest**
- **XGBoost**
- (Possiblement) Réseaux de neurones pour des scores avancés

L’évaluation est faite à l’aide de métriques comme la **RMSE**, l’**accuracy**, ou le **ROC-AUC** selon la nature des labels ESG.

---

## 📊 Visualisations

Les visualisations des scores, des corrélations ESG, et des performances modèles sont générées via :
- `matplotlib` / `seaborn`
- `plotly`
- Dash ou Streamlit (si applicable)

---

## 📦 Données

Les données sont issues de Kaggle, notamment :
- `SP_500_ESG_Risk_Ratings.csv`
- Autres sources possibles : Sustainalytics, MSCI ESG Ratings (selon la disponibilité)

---

## 🧾 Exemple d'utilisation

```python
from src.esg_scoring import compute_esg_score
from src.ml_models import train_random_forest_model

df = load_preprocessed_data("data/processed_data/esg_cleaned.csv")
scores = compute_esg_score(df)
model = train_random_forest_model(df, target="esg_score")
```

---

## ✅ À faire

- [x] Collecte de données
- [x] Prétraitement et Feature Engineering
- [x] Entraînement de modèles de scoring
- [ ] Dashboard interactif pour la visualisation
- [ ] Documentation des modules

---

## 👨🏾‍💻 Auteur

**Roslan P. H. Nzamba Nzamba**  
MBA Finance & Data Performance – ESLSCA Business School  
Passionné par l'IA, la finance durable et l’analyse de données.  
📍 Basé à Créteil, Île-de-France.

---

## 📜 Licence

Ce projet est open-source sous licence MIT.  
*Utilisation académique ou personnelle uniquement. Contactez l’auteur pour toute utilisation commerciale.*

---

Souhaite-tu que je le formate aussi pour GitHub (avec emojis, badges, etc.) ou que je te crée le fichier prêt à télécharger ?

![Untitled-document-Google-Docs-03-07-2025_08_45_PM](https://github.com/user-attachments/assets/efd9c457-9f58-441f-a15b-781bfd8df52f)
![Untitled-document-Google-Docs-03-07-2025_08_45_PM2](https://github.com/user-attachments/assets/6ccb8f9a-bfcc-4c75-b025-43f29e2dd6fc)
![Untitled-document-Google-Docs-03-07-2025_08_45_PM1](https://github.com/user-attachments/assets/ed16257c-90e5-44dd-a60f-452f120506b1)
![Untitled-document-Google-Docs-03-07](https://github.com/user-attachments/assets/d16607b3-4534-4a1f-89f4-6e624ce10c74)
