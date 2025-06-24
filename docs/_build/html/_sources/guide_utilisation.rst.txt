Guide d'utilisation
=================

Ce guide explique comment utiliser Py Stats Toolkit pour vos analyses statistiques avancées avec l'architecture polymorphique et les fonctionnalités d'historique intégrées.

Installation
----------

Installation de base
~~~~~~~~~~~~~~~~~

Pour installer Py Stats Toolkit, utilisez pip :

.. code-block:: bash

   pip install py-stats-toolkit

Installation avec dépendances optionnelles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour installer avec des dépendances supplémentaires :

.. code-block:: bash

   pip install py-stats-toolkit[all]

Installation pour le développement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour installer en mode développement :

.. code-block:: bash

   git clone https://github.com/votre-utilisateur/py-stats-toolkit.git
   cd py-stats-toolkit
   pip install -e ".[dev]"

Premiers pas
----------

Importation
~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import (
       AdvancedStatisticsEngine,
       AnomalyDetectionEngine,
       TemporalValidationEngine,
       AdvancedScoringEngine
   )
   
   # Modules de base avec historique
   from py_stats_toolkit.stats.descriptives.basic_stats import BasicStatistics
   from py_stats_toolkit.stats.correlation.correlation import Correlation
   from py_stats_toolkit.stats.regression.regression import Regression
   from py_stats_toolkit.visualization.basic_plots import BasicPlots
   
   # Modules utilitaires avec historique
   from py_stats_toolkit.utils.data_processor import DataProcessor
   from py_stats_toolkit.utils.data_validator import DataValidator

Création de données
~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd

   # Création de données de test
   np.random.seed(42)
   data_list = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
   data_series = pd.Series(data_list)
   data_array = np.array(data_list)
   data_df = pd.DataFrame({
       'A': np.random.normal(0, 1, 1000),
       'B': np.random.normal(2, 1.5, 1000),
       'C': np.random.normal(-1, 0.5, 1000)
   })

Base de Données et Historique
---------------------------

Sauvegarde Automatique
~~~~~~~~~~~~~~~~~~~~

Tous les modules de Py Stats Toolkit sauvegardent automatiquement leur historique d'analyses :

.. code-block:: python

   # Statistiques descriptives avec historique automatique
   stats = BasicStatistics()
   result = stats.process(data_df)
   
   # L'analyse est automatiquement sauvegardée dans data/basic_statistics_history.json
   print("Analyse sauvegardée automatiquement")
   
   # Afficher l'historique des analyses
   history = stats.get_statistics_history()
   print(f"Total d'analyses: {history['total_analyses']}")
   print(f"Dernière analyse: {history['last_analysis']}")

Analyse des Tendances
~~~~~~~~~~~~~~~~~~~

Utilisez les méthodes d'historique pour analyser les tendances d'utilisation :

.. code-block:: python

   # Corrélation avec historique
   corr = Correlation()
   result = corr.process(data_df, x_col='A', y_col='B', method='pearson')
   
   # Analyser l'historique des corrélations
   corr_history = corr.get_correlation_history()
   print(f"Méthodes utilisées: {corr_history['most_common_methods']}")
   print(f"Paires les plus corrélées: {corr_history['most_correlated_pairs']}")
   
   # Régression avec historique
   reg = Regression()
   result = reg.process(data_df, feature_cols=['A', 'B'], target_col='C')
   
   # Analyser l'historique des régressions
   reg_history = reg.get_regression_history()
   print(f"R² moyen: {reg_history['average_r2']:.4f}")
   print(f"Meilleurs modèles: {reg_history['best_models']}")

Modules Utilitaires
~~~~~~~~~~~~~~~~~~

Validation et traitement de données avec historique :

.. code-block:: python

   # Validation de données
   validator = DataValidator()
   validation = validator.process(data_df, validation_type='comprehensive')
   
   # Analyser l'historique des validations
   val_history = validator.get_validation_history()
   print(f"Taux de succès: {val_history['success_rate']:.2%}")
   
   # Traitement de données
   processor = DataProcessor()
   processed = processor.process(data_df, operation='standardize')
   
   # Analyser l'historique des traitements
   proc_history = processor.get_processing_history()
   print(f"Opérations effectuées: {proc_history['most_common_operations']}")

Script d'Analyse de la Base
~~~~~~~~~~~~~~~~~~~~~~~~~

Utilisez le script intégré pour analyser l'état complet de la base de données :

.. code-block:: bash

   python show_database_summary.py

Ce script affiche :
- Total d'enregistrements par module
- Taille des fichiers d'historique
- Dates de dernière mise à jour
- Statistiques globales de la base

Architecture Polymorphique
------------------------

Support Multiples Types de Données
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Py Stats Toolkit supporte nativement plusieurs types de données :

.. code-block:: python

   # Même fonction, différents types d'entrée
   engine = AdvancedStatisticsEngine()
   
   # Liste Python
   scores_list = engine.get_detailed_scores(data_list)
   
   # Pandas Series
   scores_series = engine.get_detailed_scores(data_series)
   
   # Numpy Array
   scores_array = engine.get_detailed_scores(data_array)
   
   # Pandas DataFrame
   scores_df = engine.get_detailed_scores(data_df)

Factory Pattern
~~~~~~~~~~~~~

Utilisation du pattern Factory pour créer des modules :

.. code-block:: python

   from py_stats_toolkit import create_module, analyze_with_all_modules
   
   # Création via factory
   stats_engine = create_module('advanced_statistics')
   anomaly_engine = create_module('anomaly_detection')
   
   # Analyse automatique avec tous les modules
   all_results = analyze_with_all_modules(data_list)

Modules Avancés
-------------

Statistiques Avancées
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Création du moteur
   engine = AdvancedStatisticsEngine()
   
   # Scores détaillés
   scores = engine.get_detailed_scores(data_list)
   print("Scores:", scores)
   
   # Test d'équiprobabilité
   equiprob_test = engine.equiprobability_test(data_list)
   print("Test équiprobabilité:", equiprob_test)
   
   # Score global avec données historiques
   historical_data = [
       [10, 20, 30, 40, 50],
       [5, 15, 25, 35, 45]
   ]
   global_score = engine.global_score(
       data_list,
       date="2025-01-15",
       historical_data=historical_data
   )
   print("Score global:", global_score)

Détection d'Anomalies
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Création du moteur
   engine = AnomalyDetectionEngine()
   
   # Analyse complète d'anomalies
   analysis = engine.comprehensive_anomaly_analysis(
       data_list,
       data_type="generic"
   )
   
   print("Score d'anomalie global:", analysis['global_anomaly_score'])
   print("Recommandations:", analysis['recommendations'])
   
   # Analyse temporelle
   dates = ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"]
   temporal_analysis = engine.comprehensive_anomaly_analysis(
       data_list,
       data_type="time_series",
       dates=dates
   )

Validation Temporelle
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Création du moteur
   engine = TemporalValidationEngine()
   
   # Validation temporelle complète
   validation = engine.comprehensive_temporal_validation(
       data_list,
       dates=dates
   )
   
   print("Score temporel global:", validation['global_temporal_score'])
   print("Cohérence temporelle:", validation['temporal_consistency'])
   
   # Détection de patterns temporels
   patterns = engine.detect_temporal_patterns(data_list, dates=dates)

Scoring Avancé
~~~~~~~~~~~~

.. code-block:: python

   # Création du moteur
   engine = AdvancedScoringEngine()
   
   # Scores complets
   scores = engine.get_comprehensive_scores(data_list)
   
   # Scores relatifs
   reference_data = [20, 25, 15, 35, 22, 30, 10, 25, 40, 18]
   relative_scores = engine.get_relative_scores(data_list, reference_data)
   
   # Scoring pondéré
   weights = {
       'variance': 0.3,
       'coherence': 0.2,
       'fractal': 0.2,
       'entropy': 0.15,
       'lunar': 0.15
   }
   weighted_score = engine.get_weighted_score(
       data_list,
       weights=weights,
       date="2025-01-15"
   )
   
   # Interprétation des scores
   interpretation = engine.interpret_scores(data_list)

Modules de Base
-------------

Moyenne glissante
~~~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import MoyenneGlissanteModule

   # Création du module
   module = MoyenneGlissanteModule(window=20)

   # Calcul de la moyenne glissante
   result = module.process(data_series)

   # Affichage des résultats
   print(result.head())

Corrélation
~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import CorrelationModule

   # Création du module
   module = CorrelationModule(method='pearson')

   # Calcul de la matrice de corrélation
   result = module.process(data_df)

   # Affichage des résultats
   print(result)

   # Obtenir les paires de variables corrélées
   pairs = module.get_correlation_pairs(threshold=0.5)
   print(pairs)

Analyse probabiliste
~~~~~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import ProbabilistesModule

   # Création du module
   module = ProbabilistesModule(distribution='normal')

   # Ajustement de la distribution
   result = module.process(data_series)

   # Calcul de la densité de probabilité
   x = np.linspace(-3, 3, 100)
   pdf = module.probability_density(x)

   # Calcul de la fonction de répartition
   cdf = module.cumulative_distribution(x)

Traitement parallèle
-----------------

Configuration
~~~~~~~~~~

.. code-block:: python

   # Création d'un module avec traitement parallèle
   module = MoyenneGlissanteModule(
       window=20,
       n_jobs=4,  # Nombre de processus
       batch_size=100  # Taille des lots
   )

Utilisation
~~~~~~~~~

Le traitement parallèle est automatique pour les grandes séries de données.
Pour les petits ensembles de données, le traitement séquentiel est utilisé.

Visualisation
----------

Création de graphiques
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import VisualisationModule

   # Création du module
   viz = VisualisationModule(style='seaborn')

   # Histogramme
   viz.process(data_series, plot_type='histogram')

   # Matrice de corrélation
   viz.process(data_df, plot_type='correlation')

   # Graphique de distribution
   viz.process(data_series, plot_type='distribution')

Personnalisation
~~~~~~~~~~~~

.. code-block:: python

   # Configuration du style
   viz.set_style('darkgrid')
   viz.set_palette('deep')

   # Configuration de la taille
   viz.set_figsize((12, 8))
   viz.set_dpi(100)

Tests statistiques
--------------

Tests de normalité
~~~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import TestsModule

   # Création du module
   tests = TestsModule(test_type='normality')

   # Test de normalité
   result = tests.process(data_series)
   print(result)

Tests de corrélation
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Test de corrélation
   result = tests.process(
       data_df[['A', 'B']],
       test_type='correlation'
   )
   print(result)

Configuration et Personnalisation
-----------------------------

Configuration des Modules
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Configuration d'un module
   engine = AdvancedStatisticsEngine()
   engine.configure(
       variance_weight=0.3,
       coherence_weight=0.2,
       fractal_weight=0.2,
       entropy_weight=0.15,
       lunar_weight=0.15
   )
   
   # Récupération des paramètres
   params = engine.get_parameters()
   print("Paramètres:", params)

Héritage et Extension
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from py_stats_toolkit import StatisticalModule
   
   class CustomModule(StatisticalModule):
       def __init__(self):
           super().__init__()
           self.configure(custom_param="value")
       
       def process(self, data):
           # Logique personnalisée
           return {"custom_result": "value"}

Meilleures pratiques
-----------------

Préparation des données
~~~~~~~~~~~~~~~~~~~

* Vérifiez les valeurs manquantes
* Normalisez les données si nécessaire
* Vérifiez les outliers
* Assurez-vous que les types de données sont corrects
* Utilisez le polymorphisme pour tester différents formats

Performance
~~~~~~~~~

* Utilisez le traitement parallèle pour les grands ensembles de données
* Ajustez la taille des lots selon votre mémoire disponible
* Évitez les opérations redondantes
* Utilisez les méthodes vectorisées quand c'est possible
* Profitez du polymorphisme pour optimiser les types de données

Visualisation
~~~~~~~~~~

* Choisissez le type de graphique approprié
* Utilisez des couleurs cohérentes
* Ajoutez des titres et des labels clairs
* Incluez des légendes quand nécessaire

Architecture
~~~~~~~~~~

* Utilisez la factory pour créer des modules
* Exploitez le polymorphisme pour la flexibilité
* Configurez les modules selon vos besoins
* Utilisez l'analyse automatique pour des résultats complets

Dépannage
-------

Erreurs courantes
~~~~~~~~~~~~~

* **ValueError**: Vérifiez les types de données et les dimensions
* **MemoryError**: Réduisez la taille des lots ou utilisez le traitement par lots
* **TypeError**: Vérifiez les paramètres des fonctions
* **ImportError**: Vérifiez que tous les modules sont installés

Solutions
~~~~~~~

* Utilisez la documentation pour vérifier les paramètres
* Vérifiez les exemples dans la documentation
* Testez avec différents types de données
* Consultez les issues sur GitHub
* Contactez le support si nécessaire

Voir aussi
--------

* :ref:`api`
* :ref:`exemples`
* :ref:`installation` 