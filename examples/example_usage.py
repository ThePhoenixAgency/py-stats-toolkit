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
    
    print("=== Exemple d'utilisation de Py_Stats_Toolkit ===\n")
    
    # Statistiques descriptives
    print("1. Statistiques descriptives :")
    stats = BasicStatistics()
    result_stats = stats.process(data['x'])  # Utilise directement la colonne
    print(f"   Moyenne : {result_stats['mean']:.4f}")
    print(f"   Médiane : {result_stats['median']:.4f}")
    print(f"   Écart-type : {result_stats['std']:.4f}")
    print(f"   Min : {result_stats['min']:.4f}")
    print(f"   Max : {result_stats['max']:.4f}")
    print(f"   Asymétrie : {result_stats['skewness']:.4f}")
    print(f"   Aplatissement : {result_stats['kurtosis']:.4f}\n")
    
    # Corrélation
    print("2. Corrélation :")
    corr = Correlation()
    result_corr = corr.process(data, method="pearson", x_col='x', y_col='y')
    print(f"   Méthode : {result_corr['Méthode']}")
    print(f"   Coefficient : {result_corr['Coefficient']:.4f}")
    print(f"   P-valeur : {result_corr['p-valeur']:.4f}\n")
    
    # Régression
    print("3. Régression linéaire :")
    reg = Regression()
    result_reg = reg.process(data, target_col='y', feature_cols=['x'])
    print(f"   Coefficient x : {result_reg['Coefficients']['x']:.4f}")
    print(f"   Intercept : {result_reg['Intercept']:.4f}")
    print(f"   R² : {result_reg['R²']:.4f}")
    print(f"   MSE : {result_reg['MSE']:.4f}\n")
    
    # Visualisation
    print("4. Visualisation :")
    plots = BasicPlots()
    result_plot = plots.process(data, plot_type="scatter", x_col='x', y_col='y', 
                               title="Nuage de points X vs Y", xlabel="X", ylabel="Y")
    print(f"   Graphique créé : {type(result_plot['figure'])}")
    print("   (Le graphique peut être affiché avec plt.show())\n")
    
    # Statistiques sur tout le DataFrame
    print("5. Statistiques sur tout le DataFrame :")
    result_all_stats = stats.process(data)
    print("   Statistiques par colonne :")
    for col, col_stats in result_all_stats.items():
        print(f"   - {col} : moyenne={col_stats['mean']:.4f}, std={col_stats['std']:.4f}")

if __name__ == "__main__":
    main() 