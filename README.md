# Py-Stats-Toolkit

Un toolkit Python complet pour l'analyse statistique et le traitement des données, conçu pour être simple d'utilisation tout en offrant des fonctionnalités avancées.

## 🚀 Installation

### Installation depuis PyPI (recommandé)

```bash
pip install py-stats-toolkit==1.0.3
```

### Installation depuis les sources

```bash
git clone https://github.com/PhoenixGuardianTools/py-stats-toolkit.git
cd py-stats-toolkit
pip install -e .
```

## 📦 Fonctionnalités

### Statistiques Descriptives
- Calcul automatique de toutes les statistiques descriptives
- Gestion des valeurs manquantes
- Validation des données

### Régression Linéaire
- Régression linéaire simple et multiple
- Validation des hypothèses
- Diagnostics complets

### Analyse de Corrélation
- Matrices de corrélation
- Tests de significativité
- Visualisations avancées

### Visualisation
- Graphiques statistiques professionnels
- Personnalisation complète
- Export en haute qualité

## 🔧 Utilisation Rapide

```python
from py_stats_toolkit.stats import descriptives, regression, correlation
from py_stats_toolkit.visualization import plots
import pandas as pd

# Charger vos données
data = pd.read_csv('votre_fichier.csv')

# Statistiques descriptives
stats = descriptives.calculate_descriptive_statistics(data)
print(stats)

# Régression linéaire
model = regression.linear_regression(data, 'variable_cible', ['var1', 'var2'])
print(model.summary())

# Visualisation
plots.create_correlation_matrix(data)
```

## 🛠️ Scripts Utilitaires

### Publication Automatisée

Le projet inclut plusieurs scripts pour automatiser la publication :

#### `publish_automated.py` (Recommandé)
Publication PyPI 100% automatisée sans interaction utilisateur :

```bash
# Avec token PyPI
set TWINE_PASSWORD=ton_token_pypi
python publish_automated.py

# Ou avec fichier .pypirc
python publish_automated.py
```

#### `build_and_ready.py`
Prépare le package pour publication manuelle :

```bash
python build_and_ready.py
```

#### `release_and_publish.py`
Publication complète avec release GitHub (nécessite GITHUB_TOKEN) :

```bash
set GITHUB_TOKEN=ton_token_github
set TWINE_PASSWORD=ton_token_pypi
python release_and_publish.py
```

#### `clean_cache.py`
Nettoie tous les fichiers cache et temporaires :

```bash
python clean_cache.py
```

## 🔄 Workflow GitHub Actions

Le projet utilise GitHub Actions pour l'automatisation :

1. **Création d'une release** sur GitHub
2. **Déclenchement automatique** du workflow
3. **Build et tests** automatiques
4. **Publication PyPI** automatique

## 📚 Documentation

- [Documentation complète](https://py-stats-toolkit.readthedocs.io/)
- [Exemples d'utilisation](https://github.com/PhoenixGuardianTools/py-stats-toolkit/tree/main/examples)
- [Guide de contribution](CONTRIBUTING.md)

## 🧪 Tests

```bash
# Installation des dépendances de développement
pip install -r requirements-dev.txt

# Exécution des tests
python -m pytest tests/

# Avec couverture
python -m pytest tests/ --cov=py_stats_toolkit --cov-report=html
```

## 📋 Dépendances

### Dépendances principales
- numpy >= 1.20.0
- pandas >= 1.3.0
- scipy >= 1.7.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- statsmodels >= 0.13.0
- scikit-learn >= 1.0.0
- networkx >= 2.6.0
- deap >= 1.3.0

### Dépendances de développement
- pytest >= 7.0.0
- black >= 22.0.0
- isort >= 5.0.0
- flake8 >= 4.0.0
- mypy >= 0.900

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez notre [guide de contribution](CONTRIBUTING.md) pour plus de détails.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🔗 Liens Utiles

- [PyPI](https://pypi.org/project/py-stats-toolkit/)
- [GitHub](https://github.com/PhoenixGuardianTools/py-stats-toolkit)
- [Issues](https://github.com/PhoenixGuardianTools/py-stats-toolkit/issues)
- [Releases](https://github.com/PhoenixGuardianTools/py-stats-toolkit/releases)

## 📞 Contact

- Email : autopublisher.ai@gmail.com
- GitHub : [PhoenixGuardianTools](https://github.com/PhoenixGuardianTools)

---

**Version actuelle : 1.0.3** - Automatisation complète de la publication 