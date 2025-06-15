Exemples
=======

Cette section présente des exemples d'utilisation de Py Stats Toolkit.

Analyse descriptive
----------------

Moyenne glissante
~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import MoyenneGlissanteModule

   # Création de données
   np.random.seed(42)
   data = pd.Series(np.random.normal(0, 1, 1000))

   # Création du module
   module = MoyenneGlissanteModule(
       window=20,
       n_jobs=4,
       batch_size=100
   )

   # Calcul de la moyenne glissante
   result = module.process(data)

   # Affichage des résultats
   print(result.head())

   # Visualisation
   import matplotlib.pyplot as plt
   plt.figure(figsize=(12, 6))
   plt.plot(data, label='Données')
   plt.plot(result, label='Moyenne glissante')
   plt.legend()
   plt.show()

Analyse de corrélation
-------------------

Matrice de corrélation
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import CorrelationModule

   # Création de données
   np.random.seed(42)
   data = pd.DataFrame({
       'A': np.random.normal(0, 1, 1000),
       'B': np.random.normal(2, 1.5, 1000),
       'C': np.random.normal(-1, 0.5, 1000)
   })

   # Création du module
   module = CorrelationModule(
       method='pearson',
       n_jobs=4
   )

   # Calcul de la matrice de corrélation
   result = module.process(data)

   # Affichage des résultats
   print(result)

   # Obtenir les paires de variables corrélées
   pairs = module.get_correlation_pairs(threshold=0.5)
   print(pairs)

   # Visualisation
   import seaborn as sns
   plt.figure(figsize=(10, 8))
   sns.heatmap(result, annot=True, cmap='coolwarm')
   plt.show()

Analyse probabiliste
-----------------

Ajustement de distribution
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import ProbabilistesModule

   # Création de données
   np.random.seed(42)
   data = pd.Series(np.random.normal(0, 1, 1000))

   # Création du module
   module = ProbabilistesModule(
       distribution='normal',
       n_jobs=4,
       batch_size=100
   )

   # Ajustement de la distribution
   result = module.process(data)

   # Calcul de la densité de probabilité
   x = np.linspace(-3, 3, 100)
   pdf = module.probability_density(x)

   # Calcul de la fonction de répartition
   cdf = module.cumulative_distribution(x)

   # Visualisation
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
   
   # Densité de probabilité
   ax1.hist(data, bins=30, density=True, alpha=0.6)
   ax1.plot(x, pdf, 'r-', lw=2)
   ax1.set_title('Densité de probabilité')
   
   # Fonction de répartition
   ax2.plot(x, cdf, 'b-', lw=2)
   ax2.set_title('Fonction de répartition')
   
   plt.show()

Analyse temporelle
--------------

Décomposition de série temporelle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import TimeSeriesModule

   # Création de données
   np.random.seed(42)
   t = np.arange(1000)
   trend = 0.1 * t
   seasonal = 10 * np.sin(2 * np.pi * t / 100)
   noise = np.random.normal(0, 1, 1000)
   data = pd.Series(trend + seasonal + noise)

   # Création du module
   module = TimeSeriesModule(
       period=100,
       n_jobs=4,
       batch_size=100
   )

   # Analyse de la série temporelle
   result = module.process(data)

   # Obtention des composantes
   trend = module.get_trend()
   seasonal = module.get_seasonality()

   # Visualisation
   fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))
   
   # Série originale
   ax1.plot(data)
   ax1.set_title('Série temporelle')
   
   # Tendance
   ax2.plot(trend)
   ax2.set_title('Tendance')
   
   # Saisonnalité
   ax3.plot(seasonal)
   ax3.set_title('Saisonnalité')
   
   plt.tight_layout()
   plt.show()

Tests statistiques
--------------

Tests de normalité
~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import TestsModule

   # Création de données
   np.random.seed(42)
   data = pd.Series(np.random.normal(0, 1, 1000))

   # Création du module
   module = TestsModule(
       test_type='normality',
       n_jobs=4
   )

   # Test de normalité
   result = module.process(data)

   # Affichage des résultats
   print(result)

   # Visualisation
   import scipy.stats as stats
   
   plt.figure(figsize=(10, 5))
   
   # Histogramme
   plt.subplot(121)
   plt.hist(data, bins=30, density=True, alpha=0.6)
   x = np.linspace(-3, 3, 100)
   plt.plot(x, stats.norm.pdf(x, 0, 1), 'r-', lw=2)
   plt.title('Histogramme')
   
   # QQ-plot
   plt.subplot(122)
   stats.probplot(data, dist="norm", plot=plt)
   plt.title('QQ-plot')
   
   plt.tight_layout()
   plt.show()

Visualisation
----------

Graphiques multiples
~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit import VisualisationModule

   # Création de données
   np.random.seed(42)
   data = pd.DataFrame({
       'A': np.random.normal(0, 1, 1000),
       'B': np.random.normal(2, 1.5, 1000),
       'C': np.random.normal(-1, 0.5, 1000)
   })

   # Création du module
   viz = VisualisationModule(
       style='seaborn',
       palette='deep'
   )

   # Configuration
   viz.set_figsize((15, 10))
   viz.set_dpi(100)

   # Création des graphiques
   fig = plt.figure(figsize=(15, 10))
   
   # Histogramme
   plt.subplot(221)
   viz.process(data['A'], plot_type='histogram')
   plt.title('Histogramme')
   
   # Matrice de corrélation
   plt.subplot(222)
   viz.process(data, plot_type='correlation')
   plt.title('Matrice de corrélation')
   
   # Graphique de distribution
   plt.subplot(223)
   viz.process(data['A'], plot_type='distribution')
   plt.title('Distribution')
   
   # Nuage de points
   plt.subplot(224)
   viz.process(data[['A', 'B']], plot_type='scatter')
   plt.title('Nuage de points')
   
   plt.tight_layout()
   plt.show()

Voir aussi
--------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`installation` 