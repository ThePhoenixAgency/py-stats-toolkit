"""
Exemple d'utilisation basique de py-stats-toolkit.
"""

from py_stats_toolkit import StatsToolkit
import numpy as np
import pandas as pd

def main():
    # Créer une instance
    toolkit = StatsToolkit()

    # Générer des données d'exemple
    np.random.seed(42)
    data = np.random.normal(0, 1, 1000)
    
    # Calculer les statistiques descriptives
    mean = toolkit.mean(data)
    median = toolkit.median(data)
    std = toolkit.std(data)
    var = toolkit.variance(data)

    print("Statistiques descriptives :")
    print(f"Moyenne : {mean:.4f}")
    print(f"Médiane : {median:.4f}")
    print(f"Écart-type : {std:.4f}")
    print(f"Variance : {var:.4f}")

    # Créer un DataFrame
    df = pd.DataFrame({
        'x': np.random.normal(0, 1, 100),
        'y': np.random.normal(0, 1, 100)
    })

    # Effectuer une régression linéaire
    model = toolkit.linear_regression(df['x'], df['y'])
    predictions = model.predict(df['x'])

    # Visualiser les résultats
    toolkit.plot_scatter(df['x'], df['y'])
    toolkit.plot_regression(df['x'], df['y'], model)

    # Effectuer un test t
    sample1 = np.random.normal(0, 1, 50)
    sample2 = np.random.normal(0.5, 1, 50)
    t_stat, p_value = toolkit.t_test(sample1, sample2)

    print("\nTest t :")
    print(f"Statistique t : {t_stat:.4f}")
    print(f"Valeur p : {p_value:.4f}")

    # Sauvegarder les résultats
    results = {
        'descriptive_stats': {
            'mean': mean,
            'median': median,
            'std': std,
            'variance': var
        },
        'regression': {
            'slope': model.slope,
            'intercept': model.intercept,
            'r_squared': model.r_squared
        },
        't_test': {
            't_statistic': t_stat,
            'p_value': p_value
        }
    }

    toolkit.save_results(results, 'analysis_results.json')

if __name__ == '__main__':
    main() 