Module de régression
=================

Le module `RegressionModule` permet d'effectuer des analyses de régression sur des données.

Description
----------

Ce module offre des fonctionnalités pour :

* Régression linéaire simple et multiple
* Régression polynomiale
* Régression logistique
* Régression ridge et lasso
* Évaluation des modèles
* Sélection de variables

Types de régression supportés
--------------------------

* Linéaire
* Polynomiale
* Logistique
* Ridge
* Lasso
* Elastic Net
* Support Vector Regression (SVR)
* Random Forest
* Gradient Boosting

Utilisation
---------

Exemple de base
~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit.stats.regression import RegressionModule

   # Créer des données de test
   X = pd.DataFrame({
       'x1': np.random.normal(0, 1, 100),
       'x2': np.random.normal(0, 1, 100)
   })
   y = 2 * X['x1'] + 3 * X['x2'] + np.random.normal(0, 0.1, 100)

   # Créer le module
   module = RegressionModule()

   # Effectuer une régression linéaire
   model = module.process(X, y, regression_type="linear")

   # Faire des prédictions
   predictions = module.predict(X)

   # Évaluer le modèle
   score = module.score(X, y)

Paramètres
~~~~~~~~

Le module accepte les paramètres suivants :

* `regression_type` (str) : Type de régression à utiliser
* `degree` (int, optionnel) : Degré pour la régression polynomiale
* `alpha` (float, optionnel) : Paramètre de régularisation
* `n_jobs` (int, optionnel) : Nombre de jobs pour le traitement parallèle
* `cv` (int, optionnel) : Nombre de plis pour la validation croisée

Méthodes
-------

process
~~~~~~

.. code-block:: python

   def process(self, X: pd.DataFrame, y: pd.Series, regression_type: str) -> object:
       """
       Effectue une régression sur les données.

       Args:
           X: Variables explicatives
           y: Variable à prédire
           regression_type: Type de régression à utiliser

       Returns:
           Modèle de régression ajusté
       """
       pass

predict
~~~~~~

.. code-block:: python

   def predict(self, X: pd.DataFrame) -> np.ndarray:
       """
       Fait des prédictions avec le modèle.

       Args:
           X: Variables explicatives

       Returns:
           Prédictions
       """
       pass

score
~~~~

.. code-block:: python

   def score(self, X: pd.DataFrame, y: pd.Series) -> float:
       """
       Évalue les performances du modèle.

       Args:
           X: Variables explicatives
           y: Valeurs réelles

       Returns:
           Score de performance
       """
       pass

Exemples avancés
-------------

Régression polynomiale
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Effectuer une régression polynomiale
   model = module.process(X, y, regression_type="polynomial", degree=3)
   
   # Visualiser les résultats
   import matplotlib.pyplot as plt
   
   plt.scatter(X['x1'], y, label='Données')
   plt.scatter(X['x1'], model.predict(X), label='Prédictions')
   plt.legend()
   plt.show()

Régression avec régularisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Effectuer une régression ridge
   model = module.process(X, y, regression_type="ridge", alpha=0.1)
   
   # Afficher les coefficients
   print("Coefficients:", model.coef_)
   print("Intercept:", model.intercept_)

Sélection de variables
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Effectuer une sélection de variables
   selected_features = module.select_features(X, y, threshold=0.01)
   
   # Afficher les variables sélectionnées
   print("Variables sélectionnées:", selected_features)

Validation croisée
~~~~~~~~~~~~~~~

.. code-block:: python

   # Effectuer une validation croisée
   cv_scores = module.cross_validate(X, y, cv=5)
   
   # Afficher les scores
   print("Scores de validation croisée:", cv_scores)
   print("Score moyen:", np.mean(cv_scores))

Bonnes pratiques
-------------

1. Préparation des données
   * Normalisez les variables
   * Gérez les valeurs manquantes
   * Détectez et traitez les outliers

2. Sélection du modèle
   * Commencez par des modèles simples
   * Utilisez la validation croisée
   * Comparez différents types de régression

3. Évaluation
   * Utilisez plusieurs métriques
   * Vérifiez les hypothèses
   * Analysez les résidus

4. Performance
   * Utilisez le traitement parallèle
   * Optimisez les hyperparamètres
   * Utilisez des techniques de réduction de dimension

Notes techniques
-------------

* Le module utilise scikit-learn pour les modèles de régression
* Les calculs sont effectués en parallèle pour les grands ensembles
* La mémoire utilisée dépend de la taille des données et du type de régression

Voir aussi
--------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`exemples` 