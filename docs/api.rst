API Reference
============

Ce document fournit une référence détaillée de l'API de py-stats-toolkit.

Classes principales
-----------------

StatsToolkit
~~~~~~~~~~~

.. autoclass:: py_stats_toolkit.StatsToolkit
   :members:
   :undoc-members:
   :show-inheritance:

   .. automethod:: __init__

   .. automethod:: load_data
   .. automethod:: load_dataframe
   .. automethod:: load_list

   .. automethod:: mean
   .. automethod:: median
   .. automethod:: std
   .. automethod:: variance

   .. automethod:: linear_regression
   .. automethod:: polynomial_regression

   .. automethod:: t_test
   .. automethod:: anova
   .. automethod:: chi_square

   .. automethod:: plot_histogram
   .. automethod:: plot_scatter
   .. automethod:: plot_boxplot
   .. automethod:: plot_regression

   .. automethod:: save_results

Exceptions
---------

DataError
~~~~~~~~

.. autoexception:: py_stats_toolkit.DataError
   :members:
   :undoc-members:
   :show-inheritance:

AnalysisError
~~~~~~~~~~~

.. autoexception:: py_stats_toolkit.AnalysisError
   :members:
   :undoc-members:
   :show-inheritance:

Fonctions utilitaires
-------------------

.. automodule:: py_stats_toolkit.utils
   :members:
   :undoc-members:
   :show-inheritance:

Validation des données
~~~~~~~~~~~~~~~~~~~~

.. automodule:: py_stats_toolkit.validation
   :members:
   :undoc-members:
   :show-inheritance:

Visualisation
~~~~~~~~~~~

.. automodule:: py_stats_toolkit.visualization
   :members:
   :undoc-members:
   :show-inheritance:

Tests statistiques
~~~~~~~~~~~~~~~

.. automodule:: py_stats_toolkit.tests
   :members:
   :undoc-members:
   :show-inheritance:

Types personnalisés
----------------

.. automodule:: py_stats_toolkit.types
   :members:
   :undoc-members:
   :show-inheritance:

Constantes
--------

.. automodule:: py_stats_toolkit.constants
   :members:
   :undoc-members:
   :show-inheritance: 