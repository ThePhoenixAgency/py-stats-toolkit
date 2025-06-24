Module de visualisation
====================

Le module `VisualisationModule` permet de créer des visualisations statistiques.

Description
----------

Ce module offre des fonctionnalités pour :

* Graphiques descriptifs
* Visualisations de corrélation
* Graphiques de distribution
* Visualisations de séries temporelles
* Graphiques de régression
* Visualisations de tests statistiques

Types de graphiques supportés
--------------------------

Graphiques descriptifs
~~~~~~~~~~~~~~~~~~

* Histogramme
* Diagramme en boîte
* Diagramme en violon
* Diagramme en barres
* Diagramme circulaire
* Nuage de points

Visualisations de corrélation
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Matrice de corrélation
* Heatmap
* Scatterplot matrix
* Corrélogramme
* Graphique de régression

Graphiques de distribution
~~~~~~~~~~~~~~~~~~~~~~~

* QQ-plot
* PP-plot
* Densité de probabilité
* Fonction de répartition
* Graphique de probabilité

Utilisation
---------

Exemple de base
~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import pandas as pd
   from py_stats_toolkit.visualisation import VisualisationModule

   # Créer des données de test
   data = pd.DataFrame({
       'A': np.random.normal(0, 1, 100),
       'B': np.random.normal(0, 1, 100),
       'C': np.random.normal(0, 1, 100)
   })

   # Créer le module
   module = VisualisationModule()

   # Créer un histogramme
   fig = module.process(data['A'], plot_type="histogram")

   # Créer une matrice de corrélation
   fig = module.process(data, plot_type="correlation")

   # Afficher les graphiques
   import matplotlib.pyplot as plt
   plt.show()

Paramètres
~~~~~~~~

Le module accepte les paramètres suivants :

* `plot_type` (str) : Type de graphique à créer
* `style` (str, optionnel) : Style de visualisation
* `palette` (str, optionnel) : Palette de couleurs
* `figsize` (tuple, optionnel) : Taille de la figure
* `dpi` (int, optionnel) : Résolution de la figure

Méthodes
-------

process
~~~~~~

.. code-block:: python

   def process(self, data: Union[pd.DataFrame, pd.Series, np.ndarray], plot_type: str) -> plt.Figure:
       """
       Crée un graphique.

       Args:
           data: Données à visualiser
           plot_type: Type de graphique à créer

       Returns:
           Figure matplotlib
       """
       pass

set_style
~~~~~~~~

.. code-block:: python

   def set_style(self, style: str) -> None:
       """
       Définit le style de visualisation.

       Args:
           style: Style à utiliser
       """
       pass

set_palette
~~~~~~~~~~

.. code-block:: python

   def set_palette(self, palette: str) -> None:
       """
       Définit la palette de couleurs.

       Args:
           palette: Palette à utiliser
       """
       pass

Exemples avancés
-------------

Visualisation de distribution
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Créer un QQ-plot
   fig = module.process(
       data['A'],
       plot_type="qqplot",
       reference="normal"
   )
   
   # Créer un graphique de densité
   fig = module.process(
       data['A'],
       plot_type="density",
       kernel="gaussian"
   )

Visualisation de corrélation
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Créer une heatmap de corrélation
   fig = module.process(
       data,
       plot_type="correlation",
       method="pearson",
       annot=True
   )
   
   # Créer une scatterplot matrix
   fig = module.process(
       data,
       plot_type="scatter_matrix",
       diagonal="kde"
   )

Visualisation de série temporelle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Créer un graphique de série temporelle
   fig = module.process(
       time_series,
       plot_type="timeseries",
       show_trend=True,
       show_seasonal=True
   )
   
   # Créer un graphique de décomposition
   fig = module.process(
       time_series,
       plot_type="decomposition",
       period=12
   )

Visualisation de régression
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Créer un graphique de régression
   fig = module.process(
       (X, y),
       plot_type="regression",
       show_residuals=True,
       show_ci=True
   )
   
   # Créer un graphique de résidus
   fig = module.process(
       (X, y),
       plot_type="residuals",
       show_normality=True
   )

Bonnes pratiques
-------------

1. Choix du graphique
   * Adaptez le type de graphique aux données
   * Utilisez des graphiques appropriés
   * Évitez les graphiques trompeurs

2. Style et présentation
   * Utilisez des couleurs cohérentes
   * Ajoutez des titres et labels
   * Incluez des légendes

3. Interprétation
   * Ajoutez des annotations
   * Incluez des intervalles de confiance
   * Montrez les tendances

4. Performance
   * Optimisez la taille des figures
   * Gérez la mémoire efficacement
   * Utilisez des formats appropriés

Notes techniques
-------------

* Le module utilise matplotlib et seaborn
* Les graphiques sont personnalisables
* La mémoire utilisée dépend de la taille des données

Voir aussi
--------

* :ref:`guide_utilisation`
* :ref:`api`
* :ref:`exemples` 