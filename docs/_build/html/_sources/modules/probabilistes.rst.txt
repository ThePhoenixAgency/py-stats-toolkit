Module probabiliste
================

Le module `ProbabilistesModule` permet d'analyser et de modéliser des distributions de probabilité.

Description
----------

Ce module offre des fonctionnalités pour :

* Ajuster des distributions de probabilité aux données
* Calculer des densités de probabilité
* Calculer des fonctions de répartition
* Générer des nombres aléatoires selon une distribution

Distributions supportées
---------------------

* Normale (Gaussienne)
* Exponentielle
* Gamma
* Beta
* Uniforme
* Log-normale
* Chi-carré
* Student
* Fisher
* Poisson
* Binomiale
* Géométrique

Utilisation
---------

Exemple de base
~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit.stats.probabilistes import ProbabilistesModule

   # Créer des données de test
   data = np.random.normal(0, 1, 1000)

   # Créer le module
   module = ProbabilistesModule()

   # Ajuster une distribution normale
   distribution = module.process(data, distribution_type="normal")

   # Calculer la densité de probabilité
   x = np.linspace(-3, 3, 100)
   pdf = module.probability_density(x)

   # Calculer la fonction de répartition
   cdf = module.cumulative_distribution(x)

Paramètres
~~~~~~~~

Le module accepte les paramètres suivants :

* `distribution_type` (str) : Type de distribution à ajuster
* `method` (str, optionnel) : Méthode d'estimation ('mle', 'moments', 'quantiles')
* `n_jobs` (int, optionnel) : Nombre de jobs pour le traitement parallèle
* `batch_size` (int, optionnel) : Taille des lots pour le traitement par lots

Méthodes
-------

process
~~~~~~

.. code-block:: python

   def process(self, data: np.ndarray, distribution_type: str) -> object:
       """
       Ajuste une distribution aux données.

       Args:
           data: Données à analyser
           distribution_type: Type de distribution à ajuster

       Returns:
           Objet de distribution ajusté
       """
       pass

probability_density
~~~~~~~~~~~~~~~~

.. code-block:: python

   def probability_density(self, x: np.ndarray) -> np.ndarray:
       """
       Calcule la densité de probabilité.

       Args:
           x: Points où calculer la densité

       Returns:
           Valeurs de la densité de probabilité
       """
       pass

cumulative_distribution
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def cumulative_distribution(self, x: np.ndarray) -> np.ndarray:
       """
       Calcule la fonction de répartition.

       Args:
           x: Points où calculer la fonction de répartition

       Returns:
           Valeurs de la fonction de répartition
       """
       pass

Exemples avancés
-------------

Ajustement de plusieurs distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Essayer plusieurs distributions
   distributions = ["normal", "exponential", "gamma"]
   results = {}
   
   for dist in distributions:
       try:
           results[dist] = module.process(data, distribution_type=dist)
       except:
           print(f"Impossible d'ajuster la distribution {dist}")

Test d'adéquation
~~~~~~~~~~~~~~

.. code-block:: python

   # Effectuer un test de Kolmogorov-Smirnov
   from scipy import stats
   
   # Ajuster la distribution
   dist = module.process(data, distribution_type="normal")
   
   # Calculer la statistique de test
   ks_stat, p_value = stats.kstest(data, dist.cdf)
   
   print(f"Statistique KS: {ks_stat:.3f}")
   print(f"p-valeur: {p_value:.3f}")

Génération de nombres aléatoires
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Générer des nombres selon la distribution ajustée
   n_samples = 1000
   samples = module.generate_samples(n_samples)
   
   # Comparer avec les données originales
   import matplotlib.pyplot as plt
   
   plt.hist(data, bins=30, alpha=0.5, label='Données originales')
   plt.hist(samples, bins=30, alpha=0.5, label='Échantillons générés')
   plt.legend()
   plt.show()

Bonnes pratiques
-------------

1. Choix de la distribution
   * Examinez d'abord les données visuellement
   * Testez plusieurs distributions
   * Utilisez des tests d'adéquation

2. Validation des résultats
   * Vérifiez les paramètres estimés
   * Comparez les quantiles théoriques et empiriques
   * Effectuez des tests de validation croisée

3. Performance
   * Utilisez le traitement parallèle pour les grands ensembles
   * Ajustez la taille des lots selon la mémoire disponible
   * Préférez les méthodes d'estimation rapides pour les données volumineuses

Notes techniques
-------------

* Le module utilise scipy.stats pour les distributions
* Les calculs sont effectués en parallèle pour les grands ensembles
* La mémoire utilisée dépend de la taille des données et des lots

Voir aussi
--------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`exemples` 