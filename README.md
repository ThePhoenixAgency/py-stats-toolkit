# Py-Stats-Toolkit

Une bibliothèque Python complète pour l'analyse statistique avancée et le traitement des données.

## 🚀 Fonctionnalités

- **Analyse Statistique** : Méthodes statistiques fondamentales et avancées
- **Séries Temporelles** : Analyse et prévision de séries temporelles
- **Régression** : Modèles de régression linéaire et non-linéaire
- **Tests Statistiques** : Tests paramétriques et non-paramétriques
- **Visualisation** : Outils de visualisation de données
- **Théorie des Jeux** : Analyse des interactions stratégiques
- **Fractales** : Analyse des structures fractales
- **Chaînes de Markov** : Analyse des processus stochastiques
- **Réseaux Complexes** : Analyse des structures de réseaux
- **Algorithmes Génétiques** : Optimisation par algorithmes génétiques

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🛠️ Utilisation

```python
from py_stats_toolkit import (
    StatisticalModule,
    TimeSeriesModule,
    RegressionModule,
    TestModule,
    VisualizationModule,
    GameTheoryModule,
    FractalModule,
    MarkovChainModule,
    AdvancedTimeSeriesModule,
    NetworkAnalysisModule,
    GeneticAlgorithmModule
)

# Exemple d'utilisation d'un algorithme génétique
def fitness_function(individual):
    return np.sum(individual)  # Exemple simple

ga = GeneticAlgorithmModule()
results = ga.process(
    fitness_function,
    population_size=100,
    chromosome_length=10,
    generations=50
)
```

## 📚 Documentation

La documentation complète est disponible dans le dossier `docs/`.

### Modules Principaux

- **StatisticalModule** : Analyse statistique de base
- **TimeSeriesModule** : Analyse des séries temporelles
- **RegressionModule** : Modèles de régression
- **TestModule** : Tests statistiques
- **VisualizationModule** : Visualisation de données
- **GameTheoryModule** : Analyse de la théorie des jeux
- **FractalModule** : Analyse des fractales
- **MarkovChainModule** : Analyse des chaînes de Markov
- **AdvancedTimeSeriesModule** : Analyse avancée des séries temporelles
- **NetworkAnalysisModule** : Analyse des réseaux complexes
- **GeneticAlgorithmModule** : Optimisation par algorithmes génétiques

## 🧪 Tests

```bash
pytest tests/
```

## 📝 Licence

MIT License

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 📞 Support

Pour toute question ou problème, veuillez ouvrir une issue sur GitHub.

## 📊 Exemples

Des exemples d'utilisation sont disponibles dans le dossier `examples/`.

## 🔧 Développement

Pour installer les dépendances de développement :

```bash
pip install -e ".[dev]"
```

## 📈 Roadmap

- [ ] Implémentation des méthodes manquantes
- [ ] Amélioration de la documentation
- [ ] Ajout de nouveaux tests
- [ ] Optimisation des performances
- [ ] Support de nouvelles fonctionnalités
- [ ] Ajout d'autres types d'algorithmes d'optimisation 