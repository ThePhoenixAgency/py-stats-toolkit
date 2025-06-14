# 🎯 Optimiseur Génétique Euromillions

Ce projet vise à générer des grilles optimisées pour l'Euromillions en combinant :
- Statistiques avancées (fréquences, entropie, fractales, etc.)
- Modules catégorisés (fondamentaux, cycliques, génétiques, probabilistes, topologiques)
- Algorithme génétique auto-adaptatif
- Moteur de prédiction entièrement automatisé

---

## 📦 Installation

```bash
python install.py
```

Cela :
- Crée les dossiers nécessaires
- Organise les fichiers selon l'architecture du projet

---

## 🚀 Lancement du moteur

### Option 1 — Grille + Fichier

```bash
./launch_prediction.sh
```

> Sauvegarde dans `strategie_euromillions_force.json`

### Option 2 — Grille + Affichage immédiat

```bash
./launch_and_print.sh
```

> Affiche la grille dans le terminal

---

## 📁 Structure simplifiée du projet

```
📦 /core
  ├─ prediction_engine.py
  ├─ trainer.py
  ├─ rules.py
  ├─ ...
📦 /modules
  ├─ fondamentaux/
  ├─ cycliques/
  ├─ génétiques/
  ├─ probabilistes/
  ├─ topologiques/
📦 /data
  ├─ euromillions2.csv
📄 install.py
📄 launch_prediction.sh
📄 launch_and_print.sh
📄 README.md
```

---

## 🔒 .gitignore

Seuls les fichiers suivants sont **conservés** dans le dépôt :
- `README.md`
- `install.py`
- `launch_*.sh`
- Fichiers sources dans `/core/` et `/modules/`

# Mes Bibliothèques Python Personnelles

Ce dépôt contient mes bibliothèques Python personnelles, organisées par catégories.

## Structure

```
mes_libs/
├── genetic/           # Modules d'optimisation génétique
├── stats/            # Modules statistiques
├── ml/               # Modules de machine learning
└── utils/            # Utilitaires généraux
```

## Installation

```bash
# Installation depuis GitHub
pip install git+https://github.com/votre-username/mes_libs.git

# Installation d'une catégorie spécifique
pip install git+https://github.com/votre-username/mes_libs.git#subdirectory=genetic
```

## Utilisation

```python
# Import des modules
from mes_libs.genetic import GeneticOptimizer
from mes_libs.stats import StatisticalAnalyzer
from mes_libs.ml import MLPredictor
from mes_libs.utils import DataProcessor
```

## Développement

1. Cloner le dépôt :
```bash
git clone https://github.com/votre-username/mes_libs.git
cd mes_libs
```

2. Installer en mode développement :
```bash
pip install -e .
```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Ouvrir une issue pour signaler un bug
- Proposer une pull request pour ajouter une fonctionnalité
- Améliorer la documentation

## Licence

MIT License

---

# 📊 Py-Stats-Toolkit

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-active-success)]()
[![Version](https://img.shields.io/badge/version-0.1.0-blue)]()
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen)](https://github.com/PhoenixGuardianTools/py-stats-toolkit/wiki)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Coverage](https://img.shields.io/badge/coverage-85%25-green)]()

> Une collection d'outils statistiques Python pour l'analyse de données et l'optimisation, développée par PhoenixGuardianTools.

## 🇫🇷 Français

### Description
Py-Stats-Toolkit est une collection d'outils statistiques Python pour l'analyse de données et l'optimisation. Cette bibliothèque offre une suite complète de modules pour les analyses statistiques, le machine learning et l'optimisation génétique.

### Fonctionnalités Principales
- **Module Statistique** : Analyse de distributions, corrélations, séries temporelles
- **Module Machine Learning** : Prédiction, classification, régression, clustering
- **Module Génétique** : Algorithmes d'optimisation, stratégies de sélection
- **Utilitaires** : Traitement de données, gestion de fichiers, logging

### Installation
```bash
# Installation depuis GitHub
pip install git+https://github.com/PhoenixGuardianTools/py-stats-toolkit.git

# Installation en mode développement
pip install -e git+https://github.com/PhoenixGuardianTools/py-stats-toolkit.git#egg=py-stats-toolkit
```

### Utilisation
```python
from py_stats_toolkit.stats import StatisticalAnalyzer
from py_stats_toolkit.ml import MLPredictor
from py_stats_toolkit.genetic import GeneticOptimizer

# Exemple d'analyse statistique
analyzer = StatisticalAnalyzer()
results = analyzer.analyze(data)

# Exemple de prédiction ML
predictor = MLPredictor()
predictions = predictor.predict(features)

# Exemple d'optimisation génétique
optimizer = GeneticOptimizer()
solution = optimizer.optimize(problem)
```

### Structure du Projet
```
py-stats-toolkit/
├── stats/           # Modules statistiques
├── ml/             # Modules de machine learning
├── genetic/        # Modules d'optimisation génétique
└── utils/          # Utilitaires
```

### Contribution
Les contributions sont les bienvenues ! N'hésitez pas à :
- Ouvrir une issue pour signaler un bug
- Proposer une pull request pour ajouter une fonctionnalité
- Améliorer la documentation

### Licence
MIT License

---

## 🇬🇧 English

### Description
Py-Stats-Toolkit is a collection of Python statistical tools for data analysis and optimization. This library provides a comprehensive suite of modules for statistical analysis, machine learning, and genetic optimization.

### Key Features
- **Statistical Module**: Distribution analysis, correlations, time series
- **Machine Learning Module**: Prediction, classification, regression, clustering
- **Genetic Module**: Optimization algorithms, selection strategies
- **Utilities**: Data processing, file handling, logging

### Installation
```bash
# Install from GitHub
pip install git+https://github.com/PhoenixGuardianTools/py-stats-toolkit.git

# Development installation
pip install -e git+https://github.com/PhoenixGuardianTools/py-stats-toolkit.git#egg=py-stats-toolkit
```

### Usage
```python
from py_stats_toolkit.stats import StatisticalAnalyzer
from py_stats_toolkit.ml import MLPredictor
from py_stats_toolkit.genetic import GeneticOptimizer

# Statistical analysis example
analyzer = StatisticalAnalyzer()
results = analyzer.analyze(data)

# ML prediction example
predictor = MLPredictor()
predictions = predictor.predict(features)

# Genetic optimization example
optimizer = GeneticOptimizer()
solution = optimizer.optimize(problem)
```

### Project Structure
```
py-stats-toolkit/
├── stats/           # Statistical modules
├── ml/             # Machine learning modules
├── genetic/        # Genetic optimization modules
└── utils/          # Utilities
```

### Contributing
Contributions are welcome! Feel free to:
- Open an issue to report a bug
- Submit a pull request to add a feature
- Improve the documentation

### License
MIT License
