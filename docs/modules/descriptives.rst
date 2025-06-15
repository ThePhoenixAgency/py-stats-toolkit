Module de moyenne glissante
=========================

Le module `MoyenneGlissanteModule` permet de calculer des moyennes glissantes sur des séries de données.

Description
----------

La moyenne glissante est une technique statistique qui calcule la moyenne d'un sous-ensemble de données en faisant "glisser" une fenêtre de taille fixe sur les données. Cette technique est particulièrement utile pour :

* Lisser les données
* Identifier les tendances
* Réduire le bruit dans les séries temporelles

Utilisation
---------

Exemple de base
~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit.stats.descriptives import MoyenneGlissanteModule

   # Créer des données de test
   data = pd.Series(np.random.randn(100))

   # Créer le module avec une fenêtre de taille 5
   module = MoyenneGlissanteModule(window_size=5)

   # Calculer la moyenne glissante
   result = module.process(data)

   print(result)

Paramètres
~~~~~~~~

Le module accepte les paramètres suivants :

* `window_size` (int) : Taille de la fenêtre glissante
* `min_periods` (int, optionnel) : Nombre minimum de périodes requises pour le calcul
* `center` (bool, optionnel) : Si True, centre la fenêtre sur l'observation actuelle
* `win_type` (str, optionnel) : Type de fenêtre (ex: 'boxcar', 'triang', 'blackman')

Méthodes
-------

process
~~~~~~

.. code-block:: python

   def process(self, data: Union[pd.Series, np.ndarray]) -> pd.Series:
       """
       Calcule la moyenne glissante sur les données.

       Args:
           data: Données d'entrée (série pandas ou tableau numpy)

       Returns:
           Série pandas contenant la moyenne glissante
       """
       pass

Exemples avancés
-------------

Moyenne glissante centrée
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Créer le module avec une fenêtre centrée
   module = MoyenneGlissanteModule(window_size=5, center=True)
   result = module.process(data)

Moyenne glissante pondérée
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Créer le module avec une fenêtre triangulaire
   module = MoyenneGlissanteModule(window_size=5, win_type='triang')
   result = module.process(data)

Traitement de données manquantes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Créer le module avec un minimum de périodes
   module = MoyenneGlissanteModule(window_size=5, min_periods=3)
   result = module.process(data)

Bonnes pratiques
-------------

1. Choix de la taille de fenêtre
   * Petite fenêtre : plus sensible aux variations
   * Grande fenêtre : plus lisse mais peut masquer des tendances

2. Gestion des données manquantes
   * Utilisez `min_periods` pour contrôler le traitement des données manquantes
   * Vérifiez les valeurs NaN dans les résultats

3. Performance
   * Pour les grands ensembles de données, utilisez le traitement parallèle
   * Ajustez la taille de fenêtre en fonction de la mémoire disponible

Notes techniques
-------------

* Le module utilise pandas.rolling() en interne
* Les calculs sont effectués en parallèle pour les grands ensembles de données
* La mémoire utilisée est proportionnelle à la taille de la fenêtre

Voir aussi
--------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`exemples` 