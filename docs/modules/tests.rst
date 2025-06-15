Module de tests statistiques
=========================

Le module `TestsModule` permet d'effectuer des tests statistiques sur des données.

Description
----------

Ce module offre des fonctionnalités pour :

* Tests paramétriques
* Tests non paramétriques
* Tests d'hypothèses
* Tests de normalité
* Tests d'égalité des variances
* Tests d'indépendance

Types de tests supportés
---------------------

Tests paramétriques
~~~~~~~~~~~~~~~~

* Test t de Student
* Test F
* Test Z
* ANOVA
* MANOVA
* Test de régression

Tests non paramétriques
~~~~~~~~~~~~~~~~~~~

* Test de Wilcoxon
* Test de Mann-Whitney
* Test de Kruskal-Wallis
* Test de Friedman
* Test du chi-carré
* Test de Kolmogorov-Smirnov

Tests de normalité
~~~~~~~~~~~~~~

* Test de Shapiro-Wilk
* Test de D'Agostino-Pearson
* Test de Anderson-Darling
* Test de Lilliefors

Utilisation
---------

Exemple de base
~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit.stats.tests import TestsModule

   # Créer des données de test
   group1 = np.random.normal(0, 1, 100)
   group2 = np.random.normal(0.5, 1, 100)

   # Créer le module
   module = TestsModule()

   # Effectuer un test t
   result = module.process(group1, group2, test_type="t-test")

   # Afficher les résultats
   print(f"Statistique de test: {result['statistic']}")
   print(f"p-valeur: {result['p_value']}")
   print(f"Rejeter H0: {result['reject_h0']}")

Paramètres
~~~~~~~~

Le module accepte les paramètres suivants :

* `test_type` (str) : Type de test à effectuer
* `alpha` (float, optionnel) : Niveau de significativité
* `alternative` (str, optionnel) : Hypothèse alternative
* `n_jobs` (int, optionnel) : Nombre de jobs pour le traitement parallèle
* `batch_size` (int, optionnel) : Taille des lots pour le traitement par lots

Méthodes
-------

process
~~~~~~

.. code-block:: python

   def process(self, data1: np.ndarray, data2: np.ndarray = None, test_type: str) -> dict:
       """
       Effectue un test statistique.

       Args:
           data1: Premier échantillon
           data2: Deuxième échantillon (optionnel)
           test_type: Type de test à effectuer

       Returns:
           Dictionnaire contenant les résultats du test
       """
       pass

check_normality
~~~~~~~~~~~~

.. code-block:: python

   def check_normality(self, data: np.ndarray) -> dict:
       """
       Vérifie la normalité des données.

       Args:
           data: Données à tester

       Returns:
           Dictionnaire contenant les résultats des tests de normalité
       """
       pass

check_homogeneity
~~~~~~~~~~~~~~

.. code-block:: python

   def check_homogeneity(self, data1: np.ndarray, data2: np.ndarray) -> dict:
       """
       Vérifie l'homogénéité des variances.

       Args:
           data1: Premier échantillon
           data2: Deuxième échantillon

       Returns:
           Dictionnaire contenant les résultats du test
       """
       pass

Exemples avancés
-------------

Test t apparié
~~~~~~~~~~~

.. code-block:: python

   # Effectuer un test t apparié
   result = module.process(
       before_treatment,
       after_treatment,
       test_type="paired-t-test"
   )
   
   # Afficher les résultats
   print("Résultats du test t apparié:")
   print(f"Différence moyenne: {result['mean_diff']}")
   print(f"Intervalle de confiance: {result['ci']}")

ANOVA à plusieurs facteurs
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Effectuer une ANOVA à plusieurs facteurs
   result = module.process(
       [group1, group2, group3],
       test_type="anova",
       factors=['treatment', 'time']
   )
   
   # Afficher le tableau ANOVA
   print(result['anova_table'])

Test de normalité multiple
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Effectuer plusieurs tests de normalité
   normality_tests = module.check_normality(data)
   
   # Afficher les résultats
   for test_name, test_result in normality_tests.items():
       print(f"\nTest {test_name}:")
       print(f"Statistique: {test_result['statistic']}")
       print(f"p-valeur: {test_result['p_value']}")

Test non paramétrique
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Effectuer un test de Mann-Whitney
   result = module.process(
       group1,
       group2,
       test_type="mann-whitney"
   )
   
   # Afficher les résultats
   print("Résultats du test de Mann-Whitney:")
   print(f"Statistique U: {result['statistic']}")
   print(f"p-valeur: {result['p_value']}")

Bonnes pratiques
-------------

1. Choix du test
   * Vérifiez les hypothèses
   * Choisissez le test approprié
   * Considérez les alternatives non paramétriques

2. Interprétation
   * Examinez la p-valeur
   * Considérez la taille d'effet
   * Vérifiez les intervalles de confiance

3. Validation
   * Vérifiez la normalité
   * Testez l'homogénéité des variances
   * Examinez les résidus

4. Performance
   * Utilisez le traitement parallèle
   * Optimisez la taille des échantillons
   * Gérez la mémoire efficacement

Notes techniques
-------------

* Le module utilise scipy.stats pour les tests statistiques
* Les calculs sont effectués en parallèle pour les grands ensembles
* La mémoire utilisée dépend de la taille des échantillons

Voir aussi
--------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`exemples` 