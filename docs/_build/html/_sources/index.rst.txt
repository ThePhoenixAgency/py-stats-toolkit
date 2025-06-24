.. Py Stats Toolkit documentation master file, created by
   sphinx-quickstart on Wed Mar 13 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Py Stats Toolkit
=============

Py Stats Toolkit est une bibliothèque Python complète pour l'analyse statistique avancée avec une architecture polymorphique moderne.

Fonctionnalités
------------

* **Architecture Polymorphique** : Support natif de multiples types de données (listes, pandas Series, numpy arrays, DataFrames)
* **Modules Avancés** : Statistiques avancées, détection d'anomalies, validation temporelle, scoring avancé
* **Analyse Descriptive** : Statistiques de base et analyses exploratoires
* **Analyse de Corrélation** : Corrélations multiples et matrices de corrélation
* **Méthodes Probabilistes** : Distributions et tests probabilistes
* **Régression** : Régression linéaire et non-linéaire
* **Analyse Temporelle** : Séries temporelles et analyses temporelles
* **Tests Statistiques** : Tests paramétriques et non-paramétriques
* **Visualisation** : Graphiques et visualisations avancées

Installation
----------

Pour installer Py Stats Toolkit :

.. code-block:: bash

   pip install py-stats-toolkit

Pour plus de détails, consultez la section :ref:`installation`.

Guide d'utilisation
----------------

Exemple avec polymorphisme :

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import AdvancedStatisticsEngine

   # Données de test
   data_list = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
   data_series = pd.Series(data_list)
   data_array = np.array(data_list)

   # Moteur de statistiques avancées
   engine = AdvancedStatisticsEngine()
   
   # Analyse polymorphique - fonctionne avec tous les types
   scores_list = engine.get_detailed_scores(data_list)
   scores_series = engine.get_detailed_scores(data_series)
   scores_array = engine.get_detailed_scores(data_array)

Pour plus d'exemples, consultez la section :ref:`guide_utilisation`.

Architecture Polymorphique
------------------------

Py Stats Toolkit utilise une architecture orientée objet avec polymorphisme :

* **Classe de Base** : `StatisticalModule` fournit l'interface commune
* **Surcharge de Méthodes** : Chaque module supporte différents types d'entrées
* **Factory Pattern** : Création simplifiée d'instances de modules
* **Analyse Automatique** : Traitement automatique avec tous les modules disponibles

Modules Avancés
-------------

Statistiques Avancées
~~~~~~~~~~~~~~~~~~

* Analyse de variance et cohérence
* Scores fractals et d'entropie
* Tests d'équiprobabilité
* Intégration de cycles lunaires
* Corrélations et analyses ANOVA

Détection d'Anomalies
~~~~~~~~~~~~~~~~~~

* Analyse d'équiprobabilité
* Détection de cycles temporels
* Analyse de patterns anormaux
* Détection de cycles morts
* Analyse fractale

Validation Temporelle
~~~~~~~~~~~~~~~~~~

* Cohérence temporelle
* Analyse de cycles et tendances
* Détection de saisonnalité
* Validation de prévisions
* Analyse de patterns temporels

Scoring Avancé
~~~~~~~~~~~~

* Scores relatifs et pondérés
* Interprétation automatique
* Comparaison de datasets
* Recommandations intelligentes

Documentation
----------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`exemples`
* :ref:`installation`

Modules de Base
-------------

Analyse descriptive
~~~~~~~~~~~~~~

* Moyenne glissante
* Statistiques descriptives
* Analyse de fréquence

Analyse de corrélation
~~~~~~~~~~~~~~~~~~

* Corrélation de Pearson
* Corrélation de Spearman
* Matrice de corrélation

Méthodes probabilistes
~~~~~~~~~~~~~~~~~~

* Distributions normales
* Distributions exponentielles
* Tests de normalité

Régression
~~~~~~~~

* Régression linéaire
* Régression multiple
* Régression non-linéaire

Analyse temporelle
~~~~~~~~~~~~~~

* Décomposition de séries temporelles
* Détection de tendance
* Analyse de saisonnalité

Tests statistiques
~~~~~~~~~~~~~~

* Tests paramétriques
* Tests non-paramétriques
* Tests d'hypothèses

Visualisation
~~~~~~~~~~

* Graphiques descriptifs
* Graphiques de corrélation
* Graphiques de distribution

Exemples
-------

Pour des exemples détaillés, consultez la section :ref:`exemples`.

API Reference
-----------

Pour la documentation complète de l'API, consultez la section :ref:`api`.

Contribution
----------

Les contributions sont les bienvenues ! Consultez notre guide de contribution pour plus de détails.

Licence
------

Py Stats Toolkit est distribué sous la licence MIT. Voir le fichier LICENSE pour plus de détails.

Auteurs
------

* Votre Nom <votre.email@example.com>

Remerciements
-----------

* NumPy
* Pandas
* SciPy
* scikit-learn
* statsmodels
* matplotlib
* seaborn

Contact
------

* Email : votre.email@example.com
* GitHub : https://github.com/votre-utilisateur/py-stats-toolkit
* Documentation : https://py-stats-toolkit.readthedocs.io/

.. toctree::
   :maxdepth: 2
   :caption: Contenu:

   guide_utilisation
   api
   exemples
   installation

Bienvenue dans la documentation de Py Stats Toolkit !
===================================================

Py Stats Toolkit est une bibliothèque Python complète pour l'analyse statistique avancée avec une architecture polymorphique moderne. Elle offre une interface unifiée et intuitive pour effectuer des analyses statistiques complexes sur différents types de données.

.. toctree::
   :maxdepth: 2
   :caption: Contenu:

   installation
   guide_utilisation
   modules/descriptives
   modules/correlation
   modules/probabilistes
   modules/regression
   modules/temporelle
   modules/tests
   modules/visualisation
   api
   contribution
   changelog

Indices et tables
================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search` 