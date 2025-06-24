Module d'analyse temporelle
========================

Le module `TimeSeriesModule` permet d'analyser et de modéliser des séries temporelles.

Description
----------

Ce module offre des fonctionnalités pour :

* Analyse de tendance
* Détection de saisonnalité
* Décomposition de séries temporelles
* Prévision
* Tests de stationnarité
* Transformation de données

Composantes analysées
------------------

* Tendance
* Saisonnalité
* Cyclicité
* Résidus
* Stationnarité
* Autocorrélation

Utilisation
---------

Exemple de base
~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit.stats.temporelle import TimeSeriesModule

   # Créer des données de test
   dates = pd.date_range(start='2020-01-01', periods=100, freq='D')
   data = pd.Series(
       np.sin(np.arange(100) * 0.1) + np.random.normal(0, 0.1, 100),
       index=dates
   )

   # Créer le module
   module = TimeSeriesModule()

   # Analyser la série temporelle
   result = module.process(data)

   # Obtenir la tendance
   trend = module.get_trend()

   # Obtenir la saisonnalité
   seasonality = module.get_seasonality()

Paramètres
~~~~~~~~

Le module accepte les paramètres suivants :

* `period` (int, optionnel) : Période de saisonnalité
* `trend_type` (str, optionnel) : Type de tendance ('linear', 'polynomial')
* `seasonal_type` (str, optionnel) : Type de saisonnalité ('additive', 'multiplicative')
* `n_jobs` (int, optionnel) : Nombre de jobs pour le traitement parallèle
* `batch_size` (int, optionnel) : Taille des lots pour le traitement par lots

Méthodes
-------

process
~~~~~~

.. code-block:: python

   def process(self, data: pd.Series) -> dict:
       """
       Analyse une série temporelle.

       Args:
           data: Série temporelle à analyser

       Returns:
           Dictionnaire contenant les résultats de l'analyse
       """
       pass

get_trend
~~~~~~~~

.. code-block:: python

   def get_trend(self) -> pd.Series:
       """
       Extrait la composante de tendance.

       Returns:
           Série temporelle de la tendance
       """
       pass

get_seasonality
~~~~~~~~~~~~~

.. code-block:: python

   def get_seasonality(self) -> pd.Series:
       """
       Extrait la composante saisonnière.

       Returns:
           Série temporelle de la saisonnalité
       """
       pass

Exemples avancés
-------------

Décomposition de série temporelle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Décomposer la série temporelle
   decomposition = module.decompose(data)
   
   # Visualiser les composantes
   import matplotlib.pyplot as plt
   
   fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 8))
   decomposition.observed.plot(ax=ax1)
   decomposition.trend.plot(ax=ax2)
   decomposition.seasonal.plot(ax=ax3)
   decomposition.resid.plot(ax=ax4)
   plt.tight_layout()
   plt.show()

Test de stationnarité
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Effectuer un test de stationnarité
   is_stationary = module.is_stationary(data)
   
   if not is_stationary:
       # Différencier la série
       diff_data = module.difference(data)
       
       # Vérifier à nouveau la stationnarité
       is_stationary = module.is_stationary(diff_data)

Analyse d'autocorrélation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Calculer l'autocorrélation
   acf = module.autocorrelation(lags=20)
   
   # Visualiser l'autocorrélation
   import matplotlib.pyplot as plt
   
   plt.stem(range(len(acf)), acf)
   plt.axhline(y=0, linestyle='-', color='black')
   plt.axhline(y=-1.96/np.sqrt(len(data)), linestyle='--', color='gray')
   plt.axhline(y=1.96/np.sqrt(len(data)), linestyle='--', color='gray')
   plt.title('Autocorrélation')
   plt.show()

Prévision
~~~~~~~

.. code-block:: python

   # Effectuer une prévision
   forecast = module.forecast(steps=10)
   
   # Visualiser la prévision
   import matplotlib.pyplot as plt
   
   plt.plot(data.index, data, label='Données')
   plt.plot(forecast.index, forecast, label='Prévision')
   plt.legend()
   plt.show()

Bonnes pratiques
-------------

1. Préparation des données
   * Vérifiez la fréquence des données
   * Gérez les valeurs manquantes
   * Normalisez les données si nécessaire

2. Analyse préliminaire
   * Visualisez les données
   * Testez la stationnarité
   * Identifiez les composantes

3. Modélisation
   * Choisissez le bon modèle
   * Validez les hypothèses
   * Évaluez les performances

4. Performance
   * Utilisez le traitement parallèle
   * Optimisez les paramètres
   * Gérez la mémoire efficacement

Notes techniques
-------------

* Le module utilise statsmodels pour l'analyse temporelle
* Les calculs sont effectués en parallèle pour les grands ensembles
* La mémoire utilisée dépend de la taille des données et des composantes

Voir aussi
--------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`exemples` 