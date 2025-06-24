#!/usr/bin/env python3
"""
Exemple d'utilisation des fonctionnalités d'historique de Py_Stats_Toolkit
"""

import numpy as np
import pandas as pd
from py_stats_toolkit.stats.descriptives.basic_stats import BasicStatistics
from py_stats_toolkit.stats.correlation.correlation import Correlation
from py_stats_toolkit.stats.regression.regression import Regression
from py_stats_toolkit.visualization.basic_plots import BasicPlots

def main():
    """Fonction principale de démonstration"""
    print("=" * 80)
    print("DÉMONSTRATION DES FONCTIONNALITÉS D'HISTORIQUE")
    print("=" * 80)
    
    # Créer des données de test
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.normal(0, 1, 100),
        'y': np.random.normal(0, 1, 100),
        'z': np.random.normal(0, 1, 100)
    })
    
    print(f"📊 Données de test créées: {len(data)} lignes")
    print(f"📋 Colonnes: {list(data.columns)}")
    print()
    
    # 1. Statistiques descriptives avec historique
    print("1️⃣ STATISTIQUES DESCRIPTIVES")
    print("-" * 40)
    stats_module = BasicStatistics()
    
    # Effectuer plusieurs analyses
    for i in range(3):
        print(f"   Analyse {i+1}...")
        result = stats_module.process(data, analysis_type=f"test_{i+1}")
        # Gérer la structure des résultats (peut être un dict simple ou par colonne)
        if isinstance(result, dict) and 'x' in result:
            # Résultats par colonne
            mean_x = result['x']['mean']
        else:
            # Résultats simples
            mean_x = result.get('mean', 0)
        print(f"   ✅ Moyenne: {mean_x:.4f}")
    
    # Afficher l'historique
    history_stats = stats_module.get_statistics_history()
    print(f"\n   📈 Historique des statistiques:")
    print(f"      Total d'analyses: {history_stats['total_analyses']}")
    print(f"      Points de données moyens: {history_stats['average_data_points']:.1f}")
    print(f"      Dernière analyse: {history_stats['last_analysis']}")
    print()
    
    # 2. Corrélation avec historique
    print("2️⃣ ANALYSE DE CORRÉLATION")
    print("-" * 40)
    corr_module = Correlation()
    
    # Effectuer plusieurs corrélations
    correlations = [
        ('x', 'y', 'pearson'),
        ('y', 'z', 'spearman'),
        ('x', 'z', 'kendall')
    ]
    
    for x_col, y_col, method in correlations:
        print(f"   Corrélation {x_col}-{y_col} ({method})...")
        result = corr_module.process(data, x_col=x_col, y_col=y_col, method=method)
        print(f"   ✅ Coefficient: {result['Coefficient']:.4f}")
    
    # Afficher l'historique
    history_corr = corr_module.get_correlation_history()
    print(f"\n   📈 Historique des corrélations:")
    print(f"      Total d'analyses: {history_corr['total_analyses']}")
    print(f"      Méthodes utilisées: {history_corr['most_common_methods']}")
    print(f"      Paires les plus corrélées: {len(history_corr['most_correlated_pairs'])}")
    print()
    
    # 3. Régression avec historique
    print("3️⃣ ANALYSE DE RÉGRESSION")
    print("-" * 40)
    reg_module = Regression()
    
    # Effectuer plusieurs régressions
    regressions = [
        (['x'], 'y'),
        (['y'], 'z'),
        (['x', 'y'], 'z')
    ]
    
    for features, target in regressions:
        print(f"   Régression {features} -> {target}...")
        result = reg_module.process(data, feature_cols=features, target_col=target)
        print(f"   ✅ R²: {result['R²']:.4f}")
    
    # Afficher l'historique
    history_reg = reg_module.get_regression_history()
    print(f"\n   📈 Historique des régressions:")
    print(f"      Total d'analyses: {history_reg['total_analyses']}")
    print(f"      R² moyen: {history_reg['average_r2']:.4f}")
    print(f"      Meilleurs modèles: {len(history_reg['best_models'])}")
    print()
    
    # 4. Visualisation avec historique
    print("4️⃣ VISUALISATION")
    print("-" * 40)
    viz_module = BasicPlots()
    
    # Créer plusieurs visualisations
    plots = [
        ('histogram', 'x', None, 'Distribution de X'),
        ('scatter', 'x', 'y', 'Nuage de points X vs Y'),
        ('boxplot', 'z', None, 'Boîte à moustaches de Z')
    ]
    
    for plot_type, x_col, y_col, title in plots:
        print(f"   Graphique {plot_type}...")
        result = viz_module.process(data, plot_type=plot_type, x_col=x_col, y_col=y_col, title=title)
        print(f"   ✅ Graphique créé: {type(result['figure']).__name__}")
    
    # Afficher l'historique
    history_viz = viz_module.get_visualization_history()
    print(f"\n   📈 Historique des visualisations:")
    print(f"      Total de graphiques: {history_viz['total_plots']}")
    print(f"      Types de graphiques: {history_viz['most_common_plot_types']}")
    print(f"      Colonnes les plus utilisées: {list(history_viz['most_used_columns'].keys())[:3]}")
    print()
    
    # 5. Résumé global
    print("5️⃣ RÉSUMÉ GLOBAL")
    print("-" * 40)
    
    total_analyses = (
        history_stats['total_analyses'] +
        history_corr['total_analyses'] +
        history_reg['total_analyses'] +
        history_viz['total_plots']
    )
    
    print(f"   🔢 Total d'analyses effectuées: {total_analyses}")
    print(f"   📊 Statistiques: {history_stats['total_analyses']} analyses")
    print(f"   🔗 Corrélations: {history_corr['total_analyses']} analyses")
    print(f"   📈 Régressions: {history_reg['total_analyses']} analyses")
    print(f"   📊 Visualisations: {history_viz['total_plots']} graphiques")
    print()
    
    print("=" * 80)
    print("✅ DÉMONSTRATION TERMINÉE")
    print("=" * 80)
    print("💡 Tous les modules sauvegardent maintenant automatiquement leur historique")
    print("💡 Utilisez les méthodes get_*_history() pour analyser les tendances")
    print("💡 Les fichiers JSON sont stockés dans le dossier 'data/'")

if __name__ == "__main__":
    main() 