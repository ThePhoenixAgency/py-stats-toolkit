import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from py_stats_toolkit.stats.descriptives import MoyenneGlissanteModule
from py_stats_toolkit.stats.correlation import CorrelationModule
from py_stats_toolkit.stats.probabilistes import ProbabilistesModule
from py_stats_toolkit.biostats import BioStatsModule
from py_stats_toolkit.visualization import VisualizationModule

def main():
    # Génération de données de test
    np.random.seed(42)
    
    # Données pour l'analyse descriptive
    temps = pd.date_range(start='2020-01-01', periods=100, freq='D')
    valeurs = np.random.normal(0, 1, 100).cumsum()
    donnees_series = pd.Series(valeurs, index=temps)
    
    # Données pour l'analyse de corrélation
    donnees_corr = pd.DataFrame({
        'A': np.random.normal(0, 1, 100),
        'B': np.random.normal(0, 1, 100) + 0.5 * np.random.normal(0, 1, 100),
        'C': np.random.normal(0, 1, 100) - 0.3 * np.random.normal(0, 1, 100)
    })
    
    # Données pour les tests statistiques
    donnees_test = pd.DataFrame({
        'groupe': ['A'] * 50 + ['B'] * 50,
        'valeur': np.concatenate([
            np.random.normal(0, 1, 50),
            np.random.normal(1, 1, 50)
        ])
    })
    
    # 1. Analyse descriptive avec moyenne glissante
    print("\n1. Analyse descriptive avec moyenne glissante")
    moyenne_glissante = MoyenneGlissanteModule(window_size=5, n_jobs=-1)
    resultat_moyenne = moyenne_glissante.process(donnees_series)
    print(f"Moyenne glissante calculée sur {len(resultat_moyenne)} points")
    
    # 2. Analyse de corrélation
    print("\n2. Analyse de corrélation")
    correlation = CorrelationModule(n_jobs=-1)
    matrice_corr = correlation.process(donnees_corr)
    print("\nMatrice de corrélation:")
    print(matrice_corr)
    
    paires_corr = correlation.get_correlation_pairs(threshold=0.3)
    print("\nPaires de variables corrélées (seuil > 0.3):")
    for paire in paires_corr:
        print(f"{paire[0]} - {paire[1]}: {paire[2]:.3f}")
    
    # 3. Analyse probabiliste
    print("\n3. Analyse probabiliste")
    probabiliste = ProbabilistesModule(n_jobs=-1)
    distribution = probabiliste.process(donnees_series, distribution_type="normal")
    print("\nParamètres de la distribution normale:")
    print(f"Moyenne: {distribution['mean']:.3f}")
    print(f"Écart-type: {distribution['std']:.3f}")
    
    # 4. Tests statistiques
    print("\n4. Tests statistiques")
    biostats = BioStatsModule(n_jobs=-1)
    resultat_test = biostats.process(
        donnees_test,
        test_type="t-test",
        group_col='groupe',
        value_col='valeur'
    )
    print("\nRésultats du test t:")
    print(f"Statistique t: {resultat_test['Statistique t']:.3f}")
    print(f"p-valeur: {resultat_test['p-valeur']:.3f}")
    
    # 5. Visualisation
    print("\n5. Visualisation")
    viz = VisualizationModule(n_jobs=-1)
    
    # Histogramme
    fig_hist = viz.process(donnees_series, plot_type="histogram")
    plt.savefig('histogramme.png')
    plt.close(fig_hist)
    
    # Matrice de corrélation
    fig_corr = viz.plot_correlation_matrix(donnees_corr)
    plt.savefig('matrice_correlation.png')
    plt.close(fig_corr)
    
    # Série temporelle
    fig_ts = viz.plot_time_series(
        pd.DataFrame({'temps': temps, 'valeur': valeurs}),
        time_col='temps',
        value_col='valeur'
    )
    plt.savefig('serie_temporelle.png')
    plt.close(fig_ts)
    
    print("\nGraphiques sauvegardés dans les fichiers:")
    print("- histogramme.png")
    print("- matrice_correlation.png")
    print("- serie_temporelle.png")

if __name__ == "__main__":
    main() 