# Py_Stats_Toolkit

## Description

Py_Stats_Toolkit est une bibliothèque Python complète pour l'analyse statistique avancée. Elle offre une architecture modulaire avec polymorphisme, permettant une utilisation flexible et extensible pour l'analyse de données.

## Installation

```bash
pip install py-stats-toolkit
```

## Utilisation rapide

```python
import pandas as pd
from py_stats_toolkit import DescriptiveStatistics, LinearRegression, CorrelationAnalysis, DataVisualizer

# Créer des données d'exemple
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 5, 4, 5]
})

# Statistiques descriptives
stats = DescriptiveStatistics()
result = stats.analyze(data)
print(result)

# Régression linéaire
reg = LinearRegression()
reg_result = reg.analyze(data, target='y')
print(reg_result)

# Analyse de corrélation
corr = CorrelationAnalysis()
corr_result = corr.analyze(data)
print(corr_result)

# Visualisation
viz = DataVisualizer()
viz.plot_correlation_matrix(data)
```

## Utilisation avancée avec polymorphisme

```python
from py_stats_toolkit import create_analysis_module, analyze_data

# Créer un module d'analyse avec polymorphisme
module = create_analysis_module("descriptives", precision=2)

# Analyser des données automatiquement
result = analyze_data(data, module_type="regression", target='y')
```

## Modules disponibles

- **DescriptiveStatistics** : Statistiques descriptives de base
- **LinearRegression** : Régression linéaire avec validation
- **CorrelationAnalysis** : Analyse de corrélation multivariée
- **DataVisualizer** : Visualisations statistiques avancées
- **DataProcessor** : Traitement et nettoyage de données
- **DataValidator** : Validation et vérification de données

## Documentation

Pour plus d'informations, consultez la [documentation complète](https://py-stats-toolkit.readthedocs.io/).

## Contribution

Les contributions sont les bienvenues ! Consultez notre guide de contribution pour plus de détails.

## Licence

Ce projet est sous licence MIT.

## Contact

- **Auteur** : Phoenix Project
- **Email** : contact@phonxproject.onmicrosoft.fr
- **Version** : 1.0.1

## Changelog

### Version 1.0.1
- Structure PyPI conforme
- Modules autonomes et fonctionnels
- Tests indépendants
- Documentation mise à jour
- Nettoyage complet des dépendances obsolètes

### Version 1.0.0
- Version initiale
- Modules de base implémentés
- Architecture modulaire complète 