.. Py Stats Toolkit documentation master file, created by
   sphinx-quickstart on Wed Mar 13 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Py Stats Toolkit
=============

Py Stats Toolkit est une bibliothèque Python complète pour l'analyse statistique et la visualisation de données.

Fonctionnalités
------------

* Analyse descriptive
* Analyse de corrélation
* Méthodes probabilistes
* Régression
* Analyse temporelle
* Tests statistiques
* Visualisation

Installation
----------

Pour installer Py Stats Toolkit :

.. code-block:: bash

   pip install py-stats-toolkit

Pour plus de détails, consultez la section :ref:`installation`.

Guide d'utilisation
----------------

Exemple simple :

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import MoyenneGlissanteModule

   # Création de données
   data = pd.Series(np.random.normal(0, 1, 1000))

   # Calcul de la moyenne glissante
   module = MoyenneGlissanteModule(window=20)
   result = module.process(data)

Pour plus d'exemples, consultez la section :ref:`guide_utilisation`.

Documentation
----------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`exemples`
* :ref:`installation`

Modules
------

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

Py Stats Toolkit est une bibliothèque Python complète pour l'analyse statistique et la visualisation de données. Elle offre une interface unifiée et intuitive pour effectuer des analyses statistiques avancées.

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