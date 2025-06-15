Guide d'utilisation
=================

Ce guide explique comment utiliser Py Stats Toolkit pour vos analyses statistiques.

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

   from py_stats_toolkit import MoyenneGlissanteModule, CorrelationModule, ProbabilistesModule

Création de données
~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd

   # Création de données de test
   np.random.seed(42)
   data = pd.DataFrame({
       'A': np.random.normal(0, 1, 1000),
       'B': np.random.normal(2, 1.5, 1000),
       'C': np.random.normal(-1, 0.5, 1000)
   })

Utilisation des modules
--------------------

Moyenne glissante
~~~~~~~~~~~~~~

.. code-block:: python

   # Création du module
   module = MoyenneGlissanteModule(window=20)

   # Calcul de la moyenne glissante
   result = module.process(data['A'])

   # Affichage des résultats
   print(result.head())

Corrélation
~~~~~~~~~

.. code-block:: python

   # Création du module
   module = CorrelationModule(method='pearson')

   # Calcul de la matrice de corrélation
   result = module.process(data)

   # Affichage des résultats
   print(result)

   # Obtenir les paires de variables corrélées
   pairs = module.get_correlation_pairs(threshold=0.5)
   print(pairs)

Analyse probabiliste
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Création du module
   module = ProbabilistesModule(distribution='normal')

   # Ajustement de la distribution
   result = module.process(data['A'])

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
   viz.process(data['A'], plot_type='histogram')

   # Matrice de corrélation
   viz.process(data, plot_type='correlation')

   # Graphique de distribution
   viz.process(data['A'], plot_type='distribution')

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
   result = tests.process(data['A'])
   print(result)

Tests de corrélation
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Test de corrélation
   result = tests.process(
       data[['A', 'B']],
       test_type='correlation'
   )
   print(result)

Meilleures pratiques
-----------------

Préparation des données
~~~~~~~~~~~~~~~~~~~

* Vérifiez les valeurs manquantes
* Normalisez les données si nécessaire
* Vérifiez les outliers
* Assurez-vous que les types de données sont corrects

Performance
~~~~~~~~~

* Utilisez le traitement parallèle pour les grands ensembles de données
* Ajustez la taille des lots selon votre mémoire disponible
* Évitez les opérations redondantes
* Utilisez les méthodes vectorisées quand c'est possible

Visualisation
~~~~~~~~~~

* Choisissez le type de graphique approprié
* Utilisez des couleurs cohérentes
* Ajoutez des titres et des labels clairs
* Incluez des légendes quand nécessaire

Dépannage
-------

Erreurs courantes
~~~~~~~~~~~~~

* **ValueError**: Vérifiez les types de données et les dimensions
* **MemoryError**: Réduisez la taille des lots ou utilisez le traitement par lots
* **TypeError**: Vérifiez les paramètres des fonctions

Solutions
~~~~~~~

* Utilisez la documentation pour vérifier les paramètres
* Vérifiez les exemples dans la documentation
* Consultez les issues sur GitHub
* Contactez le support si nécessaire

Voir aussi
--------

* :ref:`api`
* :ref:`exemples`
* :ref:`installation` 