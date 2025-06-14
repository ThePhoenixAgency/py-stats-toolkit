# Exemples Pratiques - Py-Stats-Toolkit

## Analyse de Données Financières

```python
import pandas as pd
import numpy as np
from py_stats_toolkit.stats import StatisticalAnalyzer
from py_stats_toolkit.ml import MLPredictor

# Chargement des données
data = pd.read_csv('financial_data.csv')

# Configuration de l'analyse
config = {
    'method': 'pearson',
    'confidence_level': 0.95,
    'bootstrap_samples': 1000
}

# Analyse statistique
analyzer = StatisticalAnalyzer(config)
results = analyzer.analyze(
    data=data,
    features=['price', 'volume', 'volatility'],
    target='returns'
)

# Prédiction avec ML
predictor = MLPredictor({
    'algorithm': 'random_forest',
    'n_estimators': 100
})

predictor.train(
    X_train=data[['price', 'volume', 'volatility']],
    y_train=data['returns']
)

predictions = predictor.predict(
    X_test=new_data[['price', 'volume', 'volatility']]
)
```

## Optimisation de Portefeuille

```python
from py_stats_toolkit.genetic import GeneticOptimizer
from py_stats_toolkit.stats import StatisticalAnalyzer

# Données historiques
returns = pd.DataFrame({
    'stock1': [0.01, 0.02, -0.01, ...],
    'stock2': [0.02, -0.01, 0.03, ...],
    'stock3': [-0.01, 0.03, 0.01, ...]
})

# Configuration de l'optimisation
config = {
    'population_size': 100,
    'generations': 50,
    'mutation_rate': 0.1,
    'crossover_rate': 0.8
}

# Optimisation
optimizer = GeneticOptimizer(config)
weights = optimizer.optimize(
    objective_function=portfolio_optimization,
    constraints={
        'sum_weights': 1.0,
        'min_weight': 0.0,
        'max_weight': 0.4
    }
)
```

## Analyse de Séries Temporelles

```python
from py_stats_toolkit.stats import TimeSeriesAnalyzer
from py_stats_toolkit.ml import MLPredictor

# Données temporelles
time_series = pd.Series([1, 2, 3, 4, 5, ...], index=pd.date_range('2020-01-01', periods=100))

# Analyse
analyzer = TimeSeriesAnalyzer()
results = analyzer.analyze(
    data=time_series,
    seasonality=True,
    trend=True
)

# Prédiction
predictor = MLPredictor({
    'algorithm': 'lstm',
    'sequence_length': 10
})

predictor.train(
    X_train=prepare_sequences(time_series),
    y_train=prepare_targets(time_series)
)

forecast = predictor.predict(
    X_test=prepare_test_sequences(time_series)
)
```

## Analyse de Clustering

```python
from py_stats_toolkit.ml import ClusterAnalyzer
from py_stats_toolkit.stats import StatisticalAnalyzer

# Données
data = pd.DataFrame({
    'feature1': [...],
    'feature2': [...],
    'feature3': [...]
})

# Clustering
clusterer = ClusterAnalyzer({
    'algorithm': 'kmeans',
    'n_clusters': 3
})

clusters = clusterer.fit_predict(data)

# Analyse des clusters
analyzer = StatisticalAnalyzer()
cluster_analysis = analyzer.analyze(
    data=data,
    features=['feature1', 'feature2', 'feature3'],
    target='cluster'
)
```

## Optimisation de Paramètres

```python
from py_stats_toolkit.genetic import GeneticOptimizer
from py_stats_toolkit.ml import MLPredictor

# Configuration de l'optimisation
config = {
    'population_size': 50,
    'generations': 30,
    'mutation_rate': 0.2
}

# Fonction objectif
def objective_function(params):
    model = MLPredictor(params)
    model.train(X_train, y_train)
    return model.evaluate(X_val, y_val)

# Optimisation
optimizer = GeneticOptimizer(config)
best_params = optimizer.optimize(
    objective_function=objective_function,
    bounds={
        'learning_rate': (0.001, 0.1),
        'n_estimators': (50, 200),
        'max_depth': (3, 10)
    }
)
```

## Visualisation des Résultats

```python
import matplotlib.pyplot as plt
from py_stats_toolkit.utils import DataProcessor

# Traitement des données
processor = DataProcessor()
processed_data = processor.process(data)

# Création des visualisations
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Distribution
axes[0, 0].hist(processed_data['feature1'])
axes[0, 0].set_title('Distribution')

# Corrélation
axes[0, 1].scatter(processed_data['feature1'], processed_data['feature2'])
axes[0, 1].set_title('Corrélation')

# Série temporelle
axes[1, 0].plot(processed_data['time'], processed_data['value'])
axes[1, 0].set_title('Série temporelle')

# Clusters
axes[1, 1].scatter(processed_data['feature1'], processed_data['feature2'], c=clusters)
axes[1, 1].set_title('Clusters')

plt.tight_layout()
plt.show()
``` 