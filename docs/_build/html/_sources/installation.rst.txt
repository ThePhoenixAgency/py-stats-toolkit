Installation
==========

Cette section explique comment installer Py Stats Toolkit.

Prérequis
-------

* Python 3.8 ou supérieur
* pip (gestionnaire de paquets Python)
* git (pour l'installation depuis le dépôt)

Installation de base
----------------

Installation via pip
~~~~~~~~~~~~~~~~

Pour installer la dernière version stable :

.. code-block:: bash

   pip install py-stats-toolkit

Installation d'une version spécifique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour installer une version spécifique :

.. code-block:: bash

   pip install py-stats-toolkit==1.0.0

Installation avec dépendances optionnelles
--------------------------------------

Installation complète
~~~~~~~~~~~~~~~~~

Pour installer avec toutes les dépendances optionnelles :

.. code-block:: bash

   pip install py-stats-toolkit[all]

Installation avec des dépendances spécifiques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour installer avec des dépendances spécifiques :

.. code-block:: bash

   pip install py-stats-toolkit[visualization]  # Pour la visualisation
   pip install py-stats-toolkit[parallel]       # Pour le traitement parallèle
   pip install py-stats-toolkit[tests]          # Pour les tests statistiques

Installation pour le développement
------------------------------

Installation depuis le dépôt
~~~~~~~~~~~~~~~~~~~~~~~~

Pour installer depuis le dépôt GitHub :

.. code-block:: bash

   git clone https://github.com/votre-utilisateur/py-stats-toolkit.git
   cd py-stats-toolkit
   pip install -e ".[dev]"

Installation des dépendances de développement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour installer les dépendances de développement :

.. code-block:: bash

   pip install -r requirements-dev.txt

Vérification de l'installation
--------------------------

Test d'importation
~~~~~~~~~~~~~~

Pour vérifier que l'installation est correcte :

.. code-block:: python

   from py_stats_toolkit import MoyenneGlissanteModule
   print("Installation réussie !")

Test des fonctionnalités
~~~~~~~~~~~~~~~~~~~~

Pour tester les fonctionnalités de base :

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import MoyenneGlissanteModule

   # Création de données de test
   data = pd.Series(np.random.normal(0, 1, 100))

   # Test du module
   module = MoyenneGlissanteModule(window=5)
   result = module.process(data)
   print(result.head())

Dépendances
--------

Dépendances principales
~~~~~~~~~~~~~~~~~~~

* numpy >= 1.20.0
* pandas >= 1.3.0
* scipy >= 1.7.0
* scikit-learn >= 0.24.0
* statsmodels >= 0.12.0

Dépendances optionnelles
~~~~~~~~~~~~~~~~~~~~

* matplotlib >= 3.4.0 (visualisation)
* seaborn >= 0.11.0 (visualisation)
* joblib >= 1.0.0 (traitement parallèle)
* pytest >= 6.0.0 (tests)
* sphinx >= 4.0.0 (documentation)

Dépendances de développement
~~~~~~~~~~~~~~~~~~~~~~~~

* black (formatage)
* flake8 (linting)
* mypy (vérification de types)
* pytest-cov (couverture de tests)
* sphinx-rtd-theme (documentation)

Résolution des problèmes
--------------------

Erreurs courantes
~~~~~~~~~~~~~

* **ModuleNotFoundError**: Vérifiez que toutes les dépendances sont installées
* **ImportError**: Vérifiez la version de Python
* **PermissionError**: Utilisez `sudo` ou un environnement virtuel

Solutions
~~~~~~~

1. Créer un environnement virtuel :

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

2. Mettre à jour pip :

.. code-block:: bash

   pip install --upgrade pip

3. Réinstaller les dépendances :

.. code-block:: bash

   pip uninstall py-stats-toolkit
   pip install py-stats-toolkit

Voir aussi
--------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`exemples`

Support
-------

Pour toute question ou problème d'installation, consultez :

* La documentation en ligne
* Les issues sur GitHub
* Le forum de la communauté 