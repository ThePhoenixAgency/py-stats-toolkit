Installation
============

Prérequis
---------

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- git (optionnel, pour l'installation depuis le code source)

Installation depuis PyPI
----------------------

La méthode la plus simple pour installer py-stats-toolkit est d'utiliser pip :

.. code-block:: bash

    pip install py-stats-toolkit

Installation depuis le code source
--------------------------------

Pour installer la dernière version de développement :

.. code-block:: bash

    git clone https://github.com/your-username/py-stats-toolkit.git
    cd py-stats-toolkit
    pip install -e ".[dev]"

Dépendances de développement
--------------------------

Pour contribuer au projet, installez les dépendances de développement :

.. code-block:: bash

    pip install -r requirements-dev.txt

Cela installera :
- pytest pour les tests
- black pour le formatage
- flake8 pour le linting
- mypy pour le typage statique
- sphinx pour la documentation
- pre-commit pour les hooks git

Configuration de l'environnement de développement
----------------------------------------------

1. Créez un environnement virtuel :

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # ou
    venv\Scripts\activate     # Windows

2. Installez les dépendances :

.. code-block:: bash

    pip install -r requirements-dev.txt
    pip install -e ".[dev]"

3. Configurez pre-commit :

.. code-block:: bash

    pre-commit install

Vérification de l'installation
----------------------------

Pour vérifier que l'installation est correcte :

.. code-block:: python

    from py_stats_toolkit import __version__
    print(f"py-stats-toolkit version: {__version__}")

Dépannage
---------

Si vous rencontrez des problèmes lors de l'installation :

1. Vérifiez votre version de Python :
   .. code-block:: bash
       python --version

2. Mettez à jour pip :
   .. code-block:: bash
       python -m pip install --upgrade pip

3. Nettoyez le cache pip :
   .. code-block:: bash
       pip cache purge

4. Réinstallez les dépendances :
   .. code-block:: bash
       pip uninstall py-stats-toolkit
       pip install py-stats-toolkit 