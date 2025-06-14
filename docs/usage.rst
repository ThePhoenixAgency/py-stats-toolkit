Guide d'utilisation
=================

Ce guide vous montrera comment utiliser py-stats-toolkit pour vos analyses statistiques.

Premiers pas
-----------

Importez le package et créez une instance :

.. code-block:: python

    from py_stats_toolkit import StatsToolkit

    # Créer une instance
    toolkit = StatsToolkit()

Chargement des données
--------------------

Vous pouvez charger des données depuis différents formats :

.. code-block:: python

    # Depuis un fichier CSV
    data = toolkit.load_data('data.csv')

    # Depuis un DataFrame pandas
    import pandas as pd
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    data = toolkit.load_dataframe(df)

    # Depuis une liste
    data = toolkit.load_list([1, 2, 3, 4, 5])

Analyses statistiques
-------------------

Calculs de base :

.. code-block:: python

    # Moyenne
    mean = toolkit.mean(data)

    # Médiane
    median = toolkit.median(data)

    # Écart-type
    std = toolkit.std(data)

    # Variance
    var = toolkit.variance(data)

Analyses avancées
---------------

Analyses de régression :

.. code-block:: python

    # Régression linéaire
    model = toolkit.linear_regression(x, y)
    predictions = model.predict(x_new)

    # Régression polynomiale
    model = toolkit.polynomial_regression(x, y, degree=2)

Tests statistiques
----------------

Tests d'hypothèses :

.. code-block:: python

    # Test t
    t_stat, p_value = toolkit.t_test(sample1, sample2)

    # Test ANOVA
    f_stat, p_value = toolkit.anova(groups)

    # Test de chi-carré
    chi2_stat, p_value = toolkit.chi_square(observed, expected)

Visualisation
------------

Création de graphiques :

.. code-block:: python

    # Histogramme
    toolkit.plot_histogram(data, bins=10)

    # Nuage de points
    toolkit.plot_scatter(x, y)

    # Boîte à moustaches
    toolkit.plot_boxplot(data)

    # Graphique de régression
    toolkit.plot_regression(x, y, model)

Exportation des résultats
-----------------------

Sauvegarde des résultats :

.. code-block:: python

    # Sauvegarder en CSV
    toolkit.save_results(results, 'output.csv')

    # Sauvegarder en Excel
    toolkit.save_results(results, 'output.xlsx')

    # Sauvegarder en JSON
    toolkit.save_results(results, 'output.json')

Exemples complets
---------------

Analyse complète d'un jeu de données :

.. code-block:: python

    # Charger les données
    data = toolkit.load_data('data.csv')

    # Calculer les statistiques descriptives
    stats = toolkit.descriptive_stats(data)
    print(stats)

    # Créer des visualisations
    toolkit.plot_histogram(data)
    toolkit.plot_boxplot(data)

    # Effectuer des tests statistiques
    results = toolkit.run_tests(data)
    print(results)

    # Sauvegarder les résultats
    toolkit.save_results(results, 'analysis_results.xlsx')

Bonnes pratiques
--------------

1. Toujours vérifier la qualité des données :
   .. code-block:: python
       toolkit.check_data_quality(data)

2. Utiliser les méthodes de validation :
   .. code-block:: python
       toolkit.validate_input(data)

3. Gérer les exceptions :
   .. code-block:: python
       try:
           results = toolkit.analyze(data)
       except toolkit.DataError as e:
           print(f"Erreur de données : {e}")
       except toolkit.AnalysisError as e:
           print(f"Erreur d'analyse : {e}")

4. Documenter vos analyses :
   .. code-block:: python
       toolkit.set_analysis_metadata(
           title="Analyse des ventes",
           description="Analyse des ventes mensuelles",
           author="John Doe"
       ) 