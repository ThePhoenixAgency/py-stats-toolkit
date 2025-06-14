Guide de Contribution
===================

Merci de votre intérêt pour contribuer à py-stats-toolkit ! Ce guide vous aidera à contribuer au projet.

Préparation de l'environnement
----------------------------

1. Fork le projet sur GitHub
2. Clonez votre fork localement :

.. code-block:: bash

    git clone https://github.com/votre-username/py-stats-toolkit.git
    cd py-stats-toolkit

3. Créez un environnement virtuel :

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # ou
    venv\Scripts\activate     # Windows

4. Installez les dépendances de développement :

.. code-block:: bash

    pip install -r requirements-dev.txt
    pip install -e ".[dev]"

5. Configurez pre-commit :

.. code-block:: bash

    pre-commit install

Workflow de développement
-----------------------

1. Créez une branche pour votre fonctionnalité :

.. code-block:: bash

    git checkout -b feature/nouvelle-fonctionnalite

2. Développez votre fonctionnalité
3. Ajoutez des tests
4. Vérifiez le code :

.. code-block:: bash

    # Formatage
    black .
    isort .

    # Linting
    flake8

    # Tests
    pytest

5. Committez vos changements :

.. code-block:: bash

    git add .
    git commit -m "Description de vos changements"

6. Poussez vers votre fork :

.. code-block:: bash

    git push origin feature/nouvelle-fonctionnalite

7. Créez une Pull Request

Standards de code
---------------

Formatage
~~~~~~~~

- Utilisez Black pour le formatage
- Utilisez isort pour l'organisation des imports
- Longueur de ligne maximale : 88 caractères

Documentation
~~~~~~~~~~~

- Documentez toutes les classes et fonctions
- Utilisez le format Google pour les docstrings
- Incluez des exemples d'utilisation
- Mettez à jour la documentation si nécessaire

Tests
~~~~~

- Écrivez des tests unitaires pour les nouvelles fonctionnalités
- Maintenez une couverture de code > 80%
- Utilisez pytest pour les tests
- Incluez des tests pour les cas limites

Types
~~~~~

- Utilisez les annotations de type
- Vérifiez les types avec mypy
- Documentez les types complexes

Pull Requests
-----------

1. Assurez-vous que votre PR :
   - Résout un problème spécifique
   - Ajoute une fonctionnalité utile
   - Est bien documentée
   - Inclut des tests

2. Format de la PR :
   - Titre descriptif
   - Description détaillée
   - Référence aux issues concernées
   - Exemples d'utilisation

3. Processus de review :
   - Répondez aux commentaires
   - Mettez à jour votre PR si nécessaire
   - Attendez l'approbation d'au moins un mainteneur

Gestion des issues
---------------

1. Avant de créer une issue :
   - Vérifiez les issues existantes
   - Vérifiez la documentation
   - Vérifiez les discussions

2. Format de l'issue :
   - Titre clair et descriptif
   - Description détaillée
   - Étapes pour reproduire (si bug)
   - Comportement attendu
   - Environnement

3. Labels d'issue :
   - bug
   - enhancement
   - documentation
   - question
   - wontfix

Communication
-----------

- Soyez respectueux et professionnel
- Utilisez un langage clair et précis
- Répondez aux commentaires rapidement
- Demandez de l'aide si nécessaire

Merci de contribuer !
-------------------

Votre contribution est précieuse pour le projet. N'hésitez pas à :
- Signaler des bugs
- Suggérer des améliorations
- Améliorer la documentation
- Ajouter des fonctionnalités
- Partager vos idées 