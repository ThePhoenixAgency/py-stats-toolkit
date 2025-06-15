# Py Stats Toolkit

Un kit d'outils statistiques en Python pour l'analyse de données.

## 📋 Description

Py Stats Toolkit est une bibliothèque Python puissante et intuitive conçue pour simplifier l'analyse statistique. Elle offre un ensemble complet d'outils pour l'analyse de données, la visualisation et le traitement statistique.

## ✨ Fonctionnalités

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

## 📚 Documentation

La documentation complète est disponible sur [ReadTheDocs](https://py-stats-toolkit.readthedocs.io/).

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🔒 Sécurité

Pour signaler une vulnérabilité de sécurité, veuillez consulter notre [politique de sécurité](SECURITY.md).

## 📞 Contact

- Email : contact@phonxproject.onmicrosoft.fr
- GitHub : [Phoenix Project](https://github.com/phoenixproject)

## 🙏 Remerciements

Merci à tous les contributeurs qui ont participé au développement de ce projet. 