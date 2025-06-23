Exemples
=======

Cette section présente des exemples d'utilisation de Py Stats Toolkit avec l'architecture polymorphique et les modules avancés.

Architecture Polymorphique
------------------------

Support Multiples Types de Données
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import AdvancedStatisticsEngine

   # Données de test
   data_list = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
   data_series = pd.Series(data_list)
   data_array = np.array(data_list)
   data_df = pd.DataFrame({
       'A': data_list,
       'B': [20, 25, 15, 35, 22, 30, 10, 25, 40, 18]
   })

   # Même fonction, différents types d'entrée
   engine = AdvancedStatisticsEngine()
   
   # Analyse avec liste Python
   scores_list = engine.get_detailed_scores(data_list)
   print("Scores (liste):", scores_list)
   
   # Analyse avec pandas Series
   scores_series = engine.get_detailed_scores(data_series)
   print("Scores (Series):", scores_series)
   
   # Analyse avec numpy array
   scores_array = engine.get_detailed_scores(data_array)
   print("Scores (array):", scores_array)
   
   # Analyse avec pandas DataFrame
   scores_df = engine.get_detailed_scores(data_df)
   print("Scores (DataFrame):", scores_df)

Factory Pattern et Analyse Automatique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import create_module, analyze_with_all_modules

   # Création via factory
   stats_engine = create_module('advanced_statistics')
   anomaly_engine = create_module('anomaly_detection')
   temporal_engine = create_module('temporal_validation')
   scoring_engine = create_module('advanced_scoring')
   
   # Analyse automatique avec tous les modules
   data = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
   all_results = analyze_with_all_modules(data)
   
   print("Résultats de l'analyse complète:")
   for module_name, results in all_results.items():
       print(f"\n{module_name}:")
       print(f"  Score global: {results.get('global_score', 'N/A')}")
       print(f"  Recommandations: {len(results.get('recommendations', []))}")

Modules Avancés
-------------

Statistiques Avancées
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   from py_stats_toolkit import AdvancedStatisticsEngine

   # Données de test
   data = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
   historical_data = [
       [10, 20, 30, 40, 50],
       [5, 15, 25, 35, 45],
       [12, 22, 32, 42, 52]
   ]

   # Création du moteur
   engine = AdvancedStatisticsEngine()
   
   # Scores détaillés
   scores = engine.get_detailed_scores(data)
   print("Scores détaillés:")
   for score_name, score_value in scores.items():
       print(f"  {score_name}: {score_value:.4f}")
   
   # Test d'équiprobabilité
   equiprob_test = engine.equiprobability_test(data)
   print(f"\nTest d'équiprobabilité:")
   print(f"  Équiprobable: {equiprob_test['is_equiprobable']}")
   print(f"  Confiance: {equiprob_test['confidence']:.4f}")
   print(f"  P-value: {equiprob_test['p_value']:.4f}")
   
   # Score global avec données historiques
   global_score = engine.global_score(
       data,
       date="2025-01-15",
       historical_data=historical_data
   )
   print(f"\nScore global: {global_score:.4f}")

Détection d'Anomalies
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import AnomalyDetectionEngine

   # Données normales et avec anomalies
   normal_data = [
       [10, 20, 30, 40, 50],
       [15, 25, 35, 45, 55],
       [12, 22, 32, 42, 52]
   ]
   
   anomalous_data = [
       [10, 20, 30, 40, 50],
       [15, 25, 35, 45, 55],
       [999, 999, 999, 999, 999],  # Anomalie évidente
       [12, 22, 32, 42, 52]
   ]

   # Création du moteur
   engine = AnomalyDetectionEngine()
   
   # Analyse des données normales
   normal_analysis = engine.comprehensive_anomaly_analysis(
       normal_data,
       data_type="generic"
   )
   
   print("Analyse des données normales:")
   print(f"  Score d'anomalie: {normal_analysis['global_anomaly_score']:.4f}")
   print(f"  Équiprobable: {normal_analysis['equiprobability_analysis']['is_equiprobable']}")
   
   # Analyse des données avec anomalies
   anomalous_analysis = engine.comprehensive_anomaly_analysis(
       anomalous_data,
       data_type="generic"
   )
   
   print("\nAnalyse des données avec anomalies:")
   print(f"  Score d'anomalie: {anomalous_analysis['global_anomaly_score']:.4f}")
   print(f"  Patterns anormaux: {anomalous_analysis['pattern_anomaly_analysis']['has_pattern_anomalies']}")
   print(f"  Recommandations: {anomalous_analysis['recommendations']}")

Validation Temporelle
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import TemporalValidationEngine

   # Données temporelles
   time_series_data = [100, 105, 110, 108, 115, 120, 118, 125, 130, 128]
   dates = [
       "2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05",
       "2025-01-06", "2025-01-07", "2025-01-08", "2025-01-09", "2025-01-10"
   ]
   
   # Données avec tendance
   trend_data = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
   
   # Données avec saisonnalité
   seasonal_data = [10, 15, 20, 15, 10, 15, 20, 15, 10, 15]

   # Création du moteur
   engine = TemporalValidationEngine()
   
   # Validation temporelle complète
   validation = engine.comprehensive_temporal_validation(
       time_series_data,
       dates=dates
   )
   
   print("Validation temporelle:")
   print(f"  Score temporel global: {validation['global_temporal_score']:.4f}")
   print(f"  Cohérence temporelle: {validation['temporal_consistency']['is_consistent']}")
   print(f"  Cycles détectés: {validation['cycle_analysis']['has_cycles']}")
   
   # Analyse des tendances
   trend_validation = engine.comprehensive_temporal_validation(
       trend_data,
       dates=dates
   )
   
   print(f"\nAnalyse des tendances:")
   print(f"  Tendance détectée: {trend_validation['trend_analysis']['has_trend']}")
   print(f"  Direction: {trend_validation['trend_analysis']['trend_direction']}")
   print(f"  Force: {trend_validation['trend_analysis']['trend_strength']:.4f}")
   
   # Analyse de saisonnalité
   seasonal_validation = engine.comprehensive_temporal_validation(
       seasonal_data,
       dates=dates
   )
   
   print(f"\nAnalyse de saisonnalité:")
   print(f"  Saisonnalité détectée: {seasonal_validation['seasonality_analysis']['has_seasonality']}")
   print(f"  Force saisonnière: {seasonal_validation['seasonality_analysis']['seasonal_strength']:.4f}")

Scoring Avancé
~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import AdvancedScoringEngine

   # Données de test
   data = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
   reference_data = [20, 25, 15, 35, 22, 30, 10, 25, 40, 18]

   # Création du moteur
   engine = AdvancedScoringEngine()
   
   # Scores complets
   scores = engine.get_comprehensive_scores(data)
   print("Scores complets:")
   for score_name, score_value in scores.items():
       print(f"  {score_name}: {score_value:.4f}")
   
   # Scores relatifs
   relative_scores = engine.get_relative_scores(data, reference_data)
   print(f"\nScores relatifs:")
   for score_name, score_value in relative_scores.items():
       print(f"  {score_name}: {score_value:.4f}")
   
   # Scoring pondéré
   weights = {
       'variance': 0.3,
       'coherence': 0.2,
       'fractal': 0.2,
       'entropy': 0.15,
       'lunar': 0.15
   }
   weighted_score = engine.get_weighted_score(
       data,
       weights=weights,
       date="2025-01-15"
   )
   print(f"\nScore pondéré: {weighted_score:.4f}")
   
   # Interprétation des scores
   interpretation = engine.interpret_scores(data)
   print(f"\nInterprétation:")
   print(f"  Évaluation globale: {interpretation['overall_assessment']}")
   print(f"  Forces: {interpretation['strengths']}")
   print(f"  Faiblesses: {interpretation['weaknesses']}")
   print(f"  Recommandations: {interpretation['recommendations']}")

Modules de Base
-------------

Analyse descriptive
----------------

Moyenne glissante
~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import MoyenneGlissanteModule

   # Création de données
   np.random.seed(42)
   data = pd.Series(np.random.normal(0, 1, 1000))

   # Création du module
   module = MoyenneGlissanteModule(
       window=20,
       n_jobs=4,
       batch_size=100
   )

   # Calcul de la moyenne glissante
   result = module.process(data)

   # Affichage des résultats
   print(result.head())

   # Visualisation
   import matplotlib.pyplot as plt
   plt.figure(figsize=(12, 6))
   plt.plot(data, label='Données')
   plt.plot(result, label='Moyenne glissante')
   plt.legend()
   plt.show()

Analyse de corrélation
-------------------

Matrice de corrélation
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import CorrelationModule

   # Création de données
   np.random.seed(42)
   data = pd.DataFrame({
       'A': np.random.normal(0, 1, 1000),
       'B': np.random.normal(2, 1.5, 1000),
       'C': np.random.normal(-1, 0.5, 1000)
   })

   # Création du module
   module = CorrelationModule(
       method='pearson',
       n_jobs=4
   )

   # Calcul de la matrice de corrélation
   result = module.process(data)

   # Affichage des résultats
   print(result)

   # Obtenir les paires de variables corrélées
   pairs = module.get_correlation_pairs(threshold=0.5)
   print(pairs)

   # Visualisation
   import seaborn as sns
   plt.figure(figsize=(10, 8))
   sns.heatmap(result, annot=True, cmap='coolwarm')
   plt.show()

Analyse probabiliste
-----------------

Ajustement de distribution
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import ProbabilistesModule

   # Création de données
   np.random.seed(42)
   data = pd.Series(np.random.normal(0, 1, 1000))

   # Création du module
   module = ProbabilistesModule(
       distribution='normal',
       n_jobs=4,
       batch_size=100
   )

   # Ajustement de la distribution
   result = module.process(data)

   # Calcul de la densité de probabilité
   x = np.linspace(-3, 3, 100)
   pdf = module.probability_density(x)

   # Calcul de la fonction de répartition
   cdf = module.cumulative_distribution(x)

   # Visualisation
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
   
   # Densité de probabilité
   ax1.hist(data, bins=30, density=True, alpha=0.6)
   ax1.plot(x, pdf, 'r-', lw=2)
   ax1.set_title('Densité de probabilité')
   
   # Fonction de répartition
   ax2.plot(x, cdf, 'b-', lw=2)
   ax2.set_title('Fonction de répartition')
   
   plt.show()

Analyse temporelle
--------------

Décomposition de série temporelle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import TimeSeriesModule

   # Création de données
   np.random.seed(42)
   t = np.arange(1000)
   trend = 0.1 * t
   seasonal = 10 * np.sin(2 * np.pi * t / 100)
   noise = np.random.normal(0, 1, 1000)
   data = pd.Series(trend + seasonal + noise)

   # Création du module
   module = TimeSeriesModule(
       period=100,
       n_jobs=4,
       batch_size=100
   )

   # Analyse de la série temporelle
   result = module.process(data)

   # Obtention des composantes
   trend = module.get_trend()
   seasonal = module.get_seasonality()

   # Visualisation
   fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))
   
   # Série originale
   ax1.plot(data)
   ax1.set_title('Série temporelle')
   
   # Tendance
   ax2.plot(trend)
   ax2.set_title('Tendance')
   
   # Saisonnalité
   ax3.plot(seasonal)
   ax3.set_title('Saisonnalité')
   
   plt.tight_layout()
   plt.show()

Tests statistiques
--------------

Tests de normalité
~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import TestsModule

   # Création de données
   np.random.seed(42)
   data = pd.Series(np.random.normal(0, 1, 1000))

   # Création du module
   module = TestsModule(
       test_type='normality',
       n_jobs=4
   )

   # Test de normalité
   result = module.process(data)

   # Affichage des résultats
   print(result)

   # Visualisation
   import scipy.stats as stats
   
   plt.figure(figsize=(10, 5))
   
   # Histogramme
   plt.subplot(121)
   plt.hist(data, bins=30, density=True, alpha=0.6)
   x = np.linspace(-3, 3, 100)
   plt.plot(x, stats.norm.pdf(x, 0, 1), 'r-', lw=2)
   plt.title('Histogramme')
   
   # QQ-plot
   plt.subplot(122)
   stats.probplot(data, dist="norm", plot=plt)
   plt.title('QQ-plot')
   
   plt.tight_layout()
   plt.show()

Visualisation
----------

Graphiques multiples
~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import VisualisationModule

   # Création de données
   np.random.seed(42)
   data = pd.DataFrame({
       'A': np.random.normal(0, 1, 1000),
       'B': np.random.normal(2, 1.5, 1000),
       'C': np.random.normal(-1, 0.5, 1000)
   })

   # Création du module
   viz = VisualisationModule(style='seaborn')

   # Histogramme
   viz.process(data['A'], plot_type='histogram')

   # Matrice de corrélation
   viz.process(data, plot_type='correlation')

   # Graphique de distribution
   viz.process(data['A'], plot_type='distribution')

Configuration et Personnalisation
-----------------------------

Configuration des Modules
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import AdvancedStatisticsEngine

   # Création et configuration du moteur
   engine = AdvancedStatisticsEngine()
   
   # Configuration personnalisée
   engine.configure(
       variance_weight=0.3,
       coherence_weight=0.2,
       fractal_weight=0.2,
       entropy_weight=0.15,
       lunar_weight=0.15,
       custom_threshold=0.05
   )
   
   # Récupération des paramètres
   params = engine.get_parameters()
   print("Paramètres configurés:")
   for key, value in params.items():
       print(f"  {key}: {value}")
   
   # Utilisation avec configuration personnalisée
   data = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
   scores = engine.get_detailed_scores(data)
   print(f"\nScores avec configuration personnalisée:")
   for score_name, score_value in scores.items():
       print(f"  {score_name}: {score_value:.4f}")

Héritage et Extension
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import StatisticalModule
   import numpy as np

   class CustomAnalysisModule(StatisticalModule):
       def __init__(self):
           super().__init__()
           self.configure(
               custom_parameter="default_value",
               analysis_type="comprehensive"
           )
       
       def process(self, data):
           # Conversion polymorphique
           if hasattr(data, 'values'):
               data_array = data.values
           elif isinstance(data, list):
               data_array = np.array(data)
           else:
               data_array = data
           
           # Logique personnalisée
           mean_val = np.mean(data_array)
           std_val = np.std(data_array)
           
           return {
               "custom_mean": mean_val,
               "custom_std": std_val,
               "custom_score": mean_val / (std_val + 1e-8),
               "analysis_type": self.get_parameters()['analysis_type']
           }
       
       def custom_analysis(self, data):
           """Méthode personnalisée supplémentaire"""
           result = self.process(data)
           result['custom_metric'] = len(data) * result['custom_score']
           return result

   # Utilisation du module personnalisé
   custom_module = CustomAnalysisModule()
   custom_module.configure(analysis_type="advanced")
   
   data = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
   result = custom_module.process(data)
   print("Résultats du module personnalisé:")
   for key, value in result.items():
       print(f"  {key}: {value}")
   
   # Utilisation de la méthode personnalisée
   custom_result = custom_module.custom_analysis(data)
   print(f"\nMétrique personnalisée: {custom_result['custom_metric']:.4f}")

Voir aussi
--------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`installation` 