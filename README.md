# Py Stats Toolkit

Un kit d'outils statistiques avancés en Python avec architecture polymorphique moderne.

## 📋 Description

Py Stats Toolkit est une bibliothèque Python puissante et intuitive conçue pour l'analyse statistique avancée. Elle offre une architecture polymorphique moderne qui supporte nativement multiples types de données (listes, pandas Series, numpy arrays, DataFrames) et un ensemble complet d'outils pour l'analyse de données, la détection d'anomalies, la validation temporelle et le scoring avancé.

## ✨ Fonctionnalités

### 🏗️ Architecture Polymorphique
- **Support Multiples Types** : Listes Python, pandas Series, numpy arrays, DataFrames
- **Surcharge de Méthodes** : Interface unifiée pour différents types d'entrées
- **Factory Pattern** : Création simplifiée d'instances de modules
- **Analyse Automatique** : Traitement automatique avec tous les modules disponibles

### 🔬 Modules Avancés
- **Statistiques Avancées** : Analyse de variance, cohérence, scores fractals et d'entropie
- **Détection d'Anomalies** : Analyse d'équiprobabilité, cycles temporels, patterns anormaux
- **Validation Temporelle** : Cohérence temporelle, cycles, tendances, saisonnalité
- **Scoring Avancé** : Scores relatifs, pondérés, interprétation automatique

### 📊 Modules de Base
- **Statistiques descriptives** : Moyenne, médiane, écart-type, etc.
- **Analyse de corrélation** : Pearson, Spearman, Kendall
- **Régression** : Régression linéaire avec métriques
- **Visualisation** : Histogrammes, boxplots, nuages de points, etc.
- **Séries temporelles** : Analyse et prévision
- **Probabilités** : Distributions et tests statistiques

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation via pip

```bash
pip install py-stats-toolkit
```

### Installation depuis les sources

```bash
git clone https://github.com/PhoenixGuardianTools/py-stats-toolkit.git
cd py-stats-toolkit
pip install -e .
```

## 📦 Dépendances principales

- numpy >= 1.20.0
- pandas >= 1.3.0
- scikit-learn >= 0.24.0
- seaborn >= 0.11.0
- matplotlib >= 3.4.0
- scipy >= 1.7.0
- lifelines >= 0.26.0
- joblib >= 1.0.0
- statsmodels >= 0.13.0
- ephem >= 4.1.0

## 🛠️ Utilisation

### Architecture Polymorphique

```python
import numpy as np
import pandas as pd
from py_stats_toolkit import AdvancedStatisticsEngine

# Données de test
data_list = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
data_series = pd.Series(data_list)
data_array = np.array(data_list)

# Même fonction, différents types d'entrée
engine = AdvancedStatisticsEngine()

# Analyse polymorphique
scores_list = engine.get_detailed_scores(data_list)
scores_series = engine.get_detailed_scores(data_series)
scores_array = engine.get_detailed_scores(data_array)

print("Scores (liste):", scores_list)
print("Scores (Series):", scores_series)
print("Scores (array):", scores_array)
```

### Factory Pattern et Analyse Automatique

```python
from py_stats_toolkit import create_module, analyze_with_all_modules

# Création via factory
stats_engine = create_module('advanced_statistics')
anomaly_engine = create_module('anomaly_detection')

# Analyse automatique avec tous les modules
data = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
all_results = analyze_with_all_modules(data)

print("Résultats de l'analyse complète:")
for module_name, results in all_results.items():
    print(f"{module_name}: {results.get('global_score', 'N/A')}")
```

### Modules Avancés

```python
from py_stats_toolkit import (
    AdvancedStatisticsEngine,
    AnomalyDetectionEngine,
    TemporalValidationEngine,
    AdvancedScoringEngine
)

# Statistiques avancées
stats_engine = AdvancedStatisticsEngine()
scores = stats_engine.get_detailed_scores(data_list)
equiprob_test = stats_engine.equiprobability_test(data_list)

# Détection d'anomalies
anomaly_engine = AnomalyDetectionEngine()
analysis = anomaly_engine.comprehensive_anomaly_analysis(data_list, data_type="generic")

# Validation temporelle
temporal_engine = TemporalValidationEngine()
dates = ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"]
validation = temporal_engine.comprehensive_temporal_validation(data_list, dates=dates)

# Scoring avancé
scoring_engine = AdvancedScoringEngine()
comprehensive_scores = scoring_engine.get_comprehensive_scores(data_list)
interpretation = scoring_engine.interpret_scores(data_list)
```

### Modules de Base

```python
from py_stats_toolkit.stats.descriptives.basic_stats import BasicStatistics
from py_stats_toolkit.stats.correlation.correlation import Correlation
from py_stats_toolkit.visualization.basic_plots import BasicPlots
import pandas as pd
import numpy as np

# Création de données de test
data = pd.DataFrame({
    'x': np.random.normal(0, 1, 100),
    'y': np.random.normal(0, 1, 100)
})

# Statistiques descriptives
stats = BasicStatistics()
results = stats.process(data)
print("Statistiques descriptives:", results)

# Analyse de corrélation
corr = Correlation()
results = corr.process(data, method='pearson', x_col='x', y_col='y')
print("Corrélation:", results)

# Visualisation
plots = BasicPlots()
fig = plots.process(data, plot_type='scatter', x_col='x', y_col='y')
```

## 🏛️ Architecture

### Organisation des Modules

```
py_stats_toolkit/
├── advanced/           # Statistiques avancées
├── analysis/           # Validation temporelle
├── detection/          # Détection d'anomalies
├── stats/              # Modules statistiques de base
├── visualization/      # Modules de visualisation
└── __init__.py         # Interface principale
```

### Classe de Base

Tous les modules héritent de `StatisticalModule` qui fournit :
- Interface commune avec polymorphisme
- Méthodes `configure()`, `process()`, `get_parameters()`, `get_results()`
- Support automatique de multiples types de données

## 📚 Documentation

La documentation complète est disponible sur [ReadTheDocs](https://py-stats-toolkit.readthedocs.io/).

### Sections principales :
- **Guide d'utilisation** : Architecture polymorphique et modules avancés
- **Exemples** : Cas d'usage concrets avec polymorphisme
- **API Reference** : Documentation complète de l'API
- **Installation** : Guide d'installation et configuration

## 🧪 Tests

Exécuter les tests :

```bash
# Tests unitaires
python -m pytest tests/

# Tests spécifiques aux modules avancés
python -m pytest tests/test_advanced_statistics.py
python -m pytest tests/test_anomaly_detection.py
python -m pytest tests/test_temporal_validation.py
python -m pytest tests/test_advanced_scoring.py
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

### Guidelines de contribution :
- Respecter l'architecture polymorphique
- Ajouter des tests pour les nouvelles fonctionnalités
- Documenter les nouvelles méthodes
- Maintenir la compatibilité avec les types de données existants

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🔒 Sécurité

Pour signaler une vulnérabilité de sécurité, veuillez consulter notre [politique de sécurité](SECURITY.md).

## 📞 Contact

- Email : contact@phonxproject.onmicrosoft.fr
- GitHub : [PhoenixGuardianTools/py-stats-toolkit](https://github.com/PhoenixGuardianTools/py-stats-toolkit)

## 🙏 Remerciements

Merci à tous les contributeurs qui ont participé au développement de ce projet.

## 🚀 Roadmap

- [ ] Support de nouveaux types de données (Dask, PySpark)
- [ ] Modules de machine learning avancés
- [ ] Interface graphique web
- [ ] Intégration avec des bases de données
- [ ] Optimisations de performance supplémentaires 