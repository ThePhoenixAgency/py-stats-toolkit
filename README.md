# Py_Stats_Toolkit

Un toolkit Python avancé pour l'analyse statistique avec polymorphisme et modularité.

## Description

Py_Stats_Toolkit est une bibliothèque Python complète pour l'analyse statistique avancée. Elle offre une architecture modulaire avec polymorphisme, permettant une utilisation flexible et extensible pour divers types d'analyses statistiques.

## Fonctionnalités principales

- **Statistiques descriptives** : Moyenne, médiane, écart-type, quartiles
- **Analyse de corrélation** : Pearson, Spearman, Kendall
- **Régression** : Linéaire avec sklearn
- **Visualisation** : Histogrammes, scatter plots, boxplots, heatmaps
- **Utilitaires** : Traitement et validation de données

## Installation

```bash
pip install py-stats-toolkit
```

## Utilisation rapide

### Exemple avec les modules du toolkit

```python
import numpy as np
import pandas as pd
from py_stats_toolkit import DescriptiveStatistics, LinearRegression, CorrelationAnalysis, DataVisualizer

# Création de données de test
np.random.seed(42)
data = pd.DataFrame({
    'x': np.random.normal(0, 1, 100),
    'y': 2 * np.random.normal(0, 1, 100) + 1 + np.random.normal(0, 0.1, 100)
})

# Statistiques descriptives
stats = DescriptiveStatistics()
result_stats = stats.analyze(data['x'])
print(f"Statistiques: {result_stats}")

# Corrélation
corr = CorrelationAnalysis()
result_corr = corr.analyze(data)
print(f"Corrélation: {result_corr}")

# Régression linéaire
reg = LinearRegression()
result_reg = reg.analyze(data[['x']], data['y'])
print(f"Régression: {result_reg}")

# Visualisation
viz = DataVisualizer()
result_viz = viz.analyze(data, plot_type='scatter')
print(f"Visualisation créée")
```

### Exemple avec polymorphisme

```python
from py_stats_toolkit import create_analysis_module, analyze_data

# Création automatique de module
stats_module = create_analysis_module('descriptives')
result = stats_module.analyze(data)

# Analyse directe avec polymorphisme
result = analyze_data(data, module_type='correlation')
```

## Modules disponibles

### Statistiques descriptives (`stats.descriptives`)
- Calcul de moyennes, médianes, écarts-types
- Quartiles et percentiles
- Analyse de distribution

### Corrélation (`stats.correlation`)
- Corrélation de Pearson
- Corrélation de Spearman
- Matrices de corrélation
- Auto-corrélation

### Régression (`stats.regression`)
- Régression linéaire avec sklearn
- Métriques d'évaluation (MSE, R²)
- Prédictions

### Visualisation (`visualization`)
- Histogrammes
- Scatter plots
- Boxplots
- Heatmaps de corrélation

### Utilitaires (`utils`)
- Traitement de données
- Validation de données
- Nettoyage automatique

## Architecture

Le toolkit utilise une architecture modulaire avec polymorphisme :

- **Classes de base** : Interfaces communes pour tous les modules
- **Moteurs spécialisés** : Implémentations spécifiques pour chaque type d'analyse
- **Utilitaires** : Fonctions d'aide pour le traitement de données
- **Visualisation** : Intégration avec matplotlib et seaborn

## Tests

Pour exécuter les tests :

```bash
python -m pytest tests/
```

Les tests sont autonomes et ne dépendent pas du package installé.

## Documentation

La documentation complète est disponible dans le dossier `docs/` :

- Guide d'installation
- Guide d'utilisation
- Exemples détaillés
- Documentation API

## Contribution

Les contributions sont les bienvenues ! Veuillez consulter le fichier `CONTRIBUTING.md` pour plus d'informations.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

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