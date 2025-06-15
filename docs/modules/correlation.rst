Module de corrélation
===================

Le module `CorrelationModule` permet d'analyser les corrélations entre variables dans un ensemble de données.

Description
----------

La corrélation mesure la relation linéaire entre deux variables. Ce module offre plusieurs méthodes de calcul de corrélation :

* Corrélation de Pearson (corrélation linéaire)
* Corrélation de Spearman (corrélation de rang)
* Corrélation de Kendall (corrélation de rang)

Utilisation
---------

Exemple de base
~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit.stats.correlation import CorrelationModule

   # Créer des données de test
   data = pd.DataFrame({
       'A': np.random.normal(0, 1, 100),
       'B': np.random.normal(0, 1, 100),
       'C': np.random.normal(0, 1, 100)
   })

   # Créer le module
   module = CorrelationModule()

   # Calculer la matrice de corrélation
   result = module.process(data)

   print(result)

Paramètres
~~~~~~~~

Le module accepte les paramètres suivants :

* `method` (str) : Méthode de corrélation ('pearson', 'spearman', 'kendall')
* `min_periods` (int, optionnel) : Nombre minimum de périodes requises
* `threshold` (float, optionnel) : Seuil de corrélation pour filtrer les résultats

Méthodes
-------

process
~~~~~~

.. code-block:: python

   def process(self, data: pd.DataFrame) -> pd.DataFrame:
       """
       Calcule la matrice de corrélation.

       Args:
           data: DataFrame contenant les variables à analyser

       Returns:
           DataFrame contenant la matrice de corrélation
       """
       pass

get_correlation_pairs
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def get_correlation_pairs(self, threshold: float = 0.5) -> List[Tuple[str, str, float]]:
       """
       Retourne les paires de variables dont la corrélation dépasse le seuil.

       Args:
           threshold: Seuil de corrélation (valeur absolue)

       Returns:
           Liste de tuples (var1, var2, corr)
       """
       pass

Exemples avancés
-------------

Corrélation de Spearman
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Créer le module avec la méthode de Spearman
   module = CorrelationModule(method='spearman')
   result = module.process(data)

Filtrage des corrélations
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Obtenir les paires de variables fortement corrélées
   pairs = module.get_correlation_pairs(threshold=0.7)
   for var1, var2, corr in pairs:
       print(f"{var1} - {var2}: {corr:.3f}")

Traitement de données manquantes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Créer le module avec un minimum de périodes
   module = CorrelationModule(min_periods=50)
   result = module.process(data)

Bonnes pratiques
-------------

1. Choix de la méthode
   * Pearson : pour les relations linéaires
   * Spearman : pour les relations monotones
   * Kendall : pour les petits échantillons

2. Interprétation des résultats
   * |r| > 0.7 : forte corrélation
   * 0.5 < |r| < 0.7 : corrélation modérée
   * |r| < 0.5 : faible corrélation

3. Performance
   * Utilisez le traitement parallèle pour les grands ensembles de données
   * Filtrez les variables non pertinentes avant l'analyse

Notes techniques
-------------

* Le module utilise scipy.stats pour les calculs de corrélation
* Les calculs sont effectués en parallèle pour les grands ensembles de données
* La mémoire utilisée est proportionnelle au nombre de variables

Voir aussi
--------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`exemples` 