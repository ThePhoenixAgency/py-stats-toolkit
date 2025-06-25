# Py_Stats_Toolkit

Un toolkit Python avancé pour l'analyse statistique avec polymorphisme et modularité.

## Description

Py_Stats_Toolkit est une bibliothèque Python complète pour l'analyse statistique avancée. Elle offre une architecture modulaire avec polymorphisme, permettant une utilisation flexible et extensible pour divers types d'analyses statistiques.

## Fonctionnalités principales

- **Statistiques descriptives avancées** : Moyenne, médiane, écart-type, asymétrie, aplatissement
- **Analyse de corrélation** : Pearson, Spearman, Kendall
- **Régression** : Linéaire, multiple, polynomiale
- **Analyse temporelle** : Validation temporelle, détection de saisonnalité
- **Détection d'anomalies** : Algorithmes avancés de détection
- **Scoring avancé** : Système de scoring multi-critères
- **Visualisation** : Graphiques intégrés
- **Utilitaires** : Traitement et validation de données

## Installation

```bash
pip install py-stats-toolkit
```

## Utilisation rapide

### Exemple autonome (sans dépendance au package)

```python
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression

# Création de données de test
np.random.seed(42)
data = pd.DataFrame({
    'x': np.random.normal(0, 1, 100),
    'y': 2 * np.random.normal(0, 1, 100) + 1 + np.random.normal(0, 0.1, 100)
})

# Statistiques descriptives
print("Statistiques descriptives :")
print(f"Moyenne x: {data['x'].mean():.4f}")
print(f"Écart-type x: {data['x'].std():.4f}")

# Corrélation
corr, p_value = stats.pearsonr(data['x'], data['y'])
print(f"Corrélation: {corr:.4f}")

# Régression linéaire
model = LinearRegression()
model.fit(data[['x']], data['y'])
print(f"Coefficient: {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")
```

### Exemple avec classes autonomes

```python
import numpy as np
import pandas as pd
from scipy import stats

class BasicStatistics:
    def process(self, data):
        return {
            'mean': data.mean(),
            'std': data.std(),
            'median': data.median()
        }

class CorrelationAnalysis:
    def process(self, data, x_col='x', y_col='y'):
        x, y = data[x_col], data[y_col]
        corr, p_value = stats.pearsonr(x, y)
        return {'correlation': corr, 'p_value': p_value}

# Utilisation
stats_engine = BasicStatistics()
corr_engine = CorrelationAnalysis()

result_stats = stats_engine.process(data['x'])
result_corr = corr_engine.process(data, 'x', 'y')

print(f"Statistiques: {result_stats}")
print(f"Corrélation: {result_corr}")
```

## Modules disponibles

### Statistiques de base
- Calcul de moyennes, médianes, écarts-types
- Analyse de distribution
- Tests de normalité

### Corrélation
- Corrélation de Pearson
- Corrélation de Spearman
- Matrices de corrélation

### Régression
- Régression linéaire simple
- Régression multiple
- Régression polynomiale

### Analyse temporelle
- Validation de cohérence temporelle
- Détection de saisonnalité
- Analyse de tendances

### Détection d'anomalies
- Algorithmes statistiques
- Détection de valeurs aberrantes
- Analyse de patterns

### Scoring avancé
- Scores multi-critères
- Pondération personnalisable
- Historique des scores

## Architecture

Le toolkit utilise une architecture modulaire avec polymorphisme :

- **Classes de base** : Interfaces communes pour tous les modules
- **Moteurs spécialisés** : Implémentations spécifiques pour chaque type d'analyse
- **Utilitaires** : Fonctions d'aide pour le traitement de données
- **Visualisation** : Intégration avec matplotlib et seaborn

## Configuration

Le toolkit peut être configuré via des fichiers de configuration ou des paramètres d'initialisation :

```python
# Configuration personnalisée
config = {
    'min_data_points': 10,
    'correlation_threshold': 0.7,
    'anomaly_threshold': 0.8
}
```

## Tests

Pour exécuter les tests :

```bash
python -m pytest tests/
```

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
- Corrections et améliorations post-release
- Nettoyage des dépendances
- Amélioration de la documentation

### Version 1.0.0
- Version initiale
- Modules de base implémentés
- Architecture modulaire complète 