"""
Exemple d'utilisation avancée de py-stats-toolkit.
"""

from py_stats_toolkit import StatsToolkit
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

def main():
    # Créer une instance
    toolkit = StatsToolkit()

    # Charger le jeu de données Iris
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    # Analyse exploratoire
    print("Analyse exploratoire des données :")
    print("\nStatistiques descriptives :")
    stats = toolkit.descriptive_stats(df)
    print(stats)

    # Visualisation
    print("\nCréation des visualisations...")
    toolkit.plot_histogram(df['sepal length (cm)'], bins=20)
    toolkit.plot_boxplot(df[iris.feature_names])
    toolkit.plot_scatter(df['sepal length (cm)'], df['sepal width (cm)'])

    # Tests statistiques
    print("\nTests statistiques :")
    
    # Test ANOVA pour comparer les longueurs de sépale entre les espèces
    groups = [df[df['target'] == i]['sepal length (cm)'] for i in range(3)]
    f_stat, p_value = toolkit.anova(groups)
    print(f"\nTest ANOVA pour la longueur du sépale :")
    print(f"Statistique F : {f_stat:.4f}")
    print(f"Valeur p : {p_value:.4f}")

    # Test de chi-carré pour l'indépendance
    contingency = pd.crosstab(df['sepal length (cm)'].round(), df['target'])
    chi2_stat, p_value = toolkit.chi_square(contingency)
    print(f"\nTest de chi-carré :")
    print(f"Statistique chi2 : {chi2_stat:.4f}")
    print(f"Valeur p : {p_value:.4f}")

    # Régression polynomiale
    print("\nRégression polynomiale :")
    x = df['sepal length (cm)']
    y = df['sepal width (cm)']
    model = toolkit.polynomial_regression(x, y, degree=2)
    print(f"Coefficients : {model.coefficients}")
    print(f"R² : {model.r_squared:.4f}")

    # Analyse de corrélation
    print("\nMatrice de corrélation :")
    corr_matrix = toolkit.correlation_matrix(df[iris.feature_names])
    print(corr_matrix)

    # Analyse de régression multiple
    print("\nRégression multiple :")
    X = df[['sepal length (cm)', 'sepal width (cm)']]
    y = df['petal length (cm)']
    model = toolkit.multiple_regression(X, y)
    print(f"Coefficients : {model.coefficients}")
    print(f"R² : {model.r_squared:.4f}")

    # Sauvegarder les résultats
    results = {
        'descriptive_stats': stats,
        'anova_test': {
            'f_statistic': f_stat,
            'p_value': p_value
        },
        'chi_square_test': {
            'chi2_statistic': chi2_stat,
            'p_value': p_value
        },
        'polynomial_regression': {
            'coefficients': model.coefficients,
            'r_squared': model.r_squared
        },
        'correlation_matrix': corr_matrix,
        'multiple_regression': {
            'coefficients': model.coefficients,
            'r_squared': model.r_squared
        }
    }

    toolkit.save_results(results, 'advanced_analysis_results.json')

if __name__ == '__main__':
    main() 