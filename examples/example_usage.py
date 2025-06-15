'''
=====================================================================
File : example_usage.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module example_usage.py

tags : module, stats, example
=====================================================================
Ce module contient des exemples d'utilisation de la bibliothèque.

tags : module, stats, example
=====================================================================
'''

import numpy as np
import pandas as pd
from py_stats_toolkit.stats.descriptives.basic_stats import BasicStatistics
from py_stats_toolkit.stats.correlation.correlation import Correlation
from py_stats_toolkit.stats.regression.regression import Regression
from py_stats_toolkit.visualization.basic_plots import BasicPlots

def main():
    """Exemple d'utilisation de la bibliothèque."""
    # Création de données de test
    np.random.seed(42)
    n_samples = 100
    data = pd.DataFrame({
        'x': np.random.normal(0, 1, n_samples),
        'y': 2 * np.random.normal(0, 1, n_samples) + 1 + np.random.normal(0, 0.1, n_samples),
        'z': np.random.normal(0, 1, n_samples)
    })
    
    # Statistiques descriptives
    stats = BasicStatistics()
    result_stats = stats.process(data, method="descriptives", value_col='x')
    print("\nStatistiques descriptives :")
    print(result_stats)
    
    # Corrélation
    corr = Correlation()
    result_corr = corr.process(data, method="pearson", x_col='x', y_col='y')
    print("\nCorrélation :")
    print(result_corr)
    
    # Régression
    reg = Regression()
    result_reg = reg.process(data, method="lineaire", x_col='x', y_col='y')
    print("\nRégression :")
    print(result_reg)
    
    # Visualisation
    plots = BasicPlots()
    result_plot = plots.process(data, plot_type="scatter", x_col='x', y_col='y')
    print("\nVisualisation :")
    print(result_plot)

if __name__ == "__main__":
    main() 