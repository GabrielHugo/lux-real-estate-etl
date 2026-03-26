# Pipeline ETL : Marché Immobilier Luxembourgeois

Ce projet est un pipeline ETL (Extract, Transform, Load) autonome codé en Python. Son but est d'aspirer les données brutes de l'Observatoire de l'Habitat luxembourgeois, de les nettoyer, et de les centraliser dans une base de données relationnelle.

Étant très intéressé par l'investissement et les marchés financiers, j'ai choisi de structurer des données immobilières.

## Technologies utilisées
* **Langage :** Python (Code Orienté Objet)
* **Traitement de données :** Pandas, Numpy
* **Base de données :** SQL Server (SSMS)
* **ORM & Sécurité :** SQLAlchemy, PyODBC, Dotenv

## Comment ça fonctionne ?

Le projet est structuré autour de deux classes principales pour séparer les responsabilités :

### 1. Extract & Transform (`ExcelReader`)
* **Extraction :** Le script lit automatiquement toutes les feuilles (années 2010 à 2024) d'un fichier Excel source.
* **Transformation (Nettoyage) :** Utilisation de Pandas pour formater les données. Les lignes entièrement vides sont supprimées. La logique métier est appliquée : si une ligne ne contient pas le prix au m² ou le nom de la commune, elle est écartée pour ne pas fausser les futures analyses. Une colonne `annee` est ajoutée dynamiquement.

### 2. Load (`SqlConnector`)
* **Chargement :** Une fois l'historique complet fusionné dans un seul grand tableau (DataFrame), la classe se connecte à SQL Server.
* **Optimisation :** J'utilise la méthode `to_sql` de SQLAlchemy pour réaliser une insertion massive (Bulk Insert) des données nettoyées, plutôt qu'une boucle ligne par ligne, afin d'optimiser les performances. Les identifiants de connexion sont sécurisés via un fichier `.env`.

## Comment tester ce projet en local

1. Clonez ce dépôt sur votre machine.
2. Installez les dépendances nécessaires dans votre environnement virtuel :
   `pip install pandas numpy sqlalchemy pyodbc python-dotenv openpyxl`
3. Créez un fichier `.env` à la racine du projet et ajoutez vos identifiants SQL Server :
   ```text
   DB_SERVER=Nom_de_votre_serveur_SQL
   DB_NAME=Nom_de_votre_base_de_donnees