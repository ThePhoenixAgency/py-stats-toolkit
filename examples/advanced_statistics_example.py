"""
Exemple d'utilisation du Py_Stats_Toolkit avec polymorphisme
============================================================

Ce script démontre l'utilisation des modules statistiques avancés
avec polymorphisme et surcharge de méthodes pour différents types de données.

Nouvelle structure organisée :
- advanced/ : Modules statistiques avancés
- analysis/ : Modules d'analyse temporelle  
- detection/ : Modules de détection d'anomalies
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import sys
import os

# Ajouter le répertoire parent au path pour importer le toolkit
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from py_stats_toolkit import (
    AdvancedStatisticsEngine,
    AnomalyDetectionEngine,
    TemporalValidationEngine,
    AdvancedScoringEngine,
    create_statistical_engine,
    analyze_data
)

def generate_sample_data(n_samples: int = 100) -> tuple:
    """Génère des données d'exemple pour les tests"""
    
    # Données temporelles avec tendance et saisonnalité
    dates = [datetime.now() - timedelta(days=i) for i in range(n_samples)]
    dates.reverse()
    
    # Série temporelle avec tendance
    trend = np.linspace(10, 50, n_samples)
    seasonality = 5 * np.sin(2 * np.pi * np.arange(n_samples) / 30)  # Saisonnalité mensuelle
    noise = np.random.normal(0, 2, n_samples)
    time_series = trend + seasonality + noise
    
    # Données historiques (simulation de tirages)
    historical_data = []
    for i in range(20):
        # Simuler des tirages de 6 nombres entre 1 et 49
        draw = np.random.choice(range(1, 50), size=6, replace=False)
        historical_data.append(draw.tolist())
    
    # Prédictions actuelles
    current_prediction = np.random.choice(range(1, 50), size=6, replace=False)
    
    # Valeurs réelles (pour le scoring)
    actual_values = np.random.choice(range(1, 50), size=6, replace=False)
    
    return {
        'dates': dates,
        'time_series': time_series,
        'historical_data': historical_data,
        'current_prediction': current_prediction,
        'actual_values': actual_values
    }

def demonstrate_polymorphism():
    """Démontre le polymorphisme avec différents types de données"""
    
    print("=" * 60)
    print("DÉMONSTRATION DU POLYMORPHISME")
    print("=" * 60)
    
    # Générer des données d'exemple
    data = generate_sample_data(50)
    
    # 1. Test avec différents types de données pour les statistiques avancées
    print("\n1. Statistiques Avancées - Polymorphisme des types de données:")
    print("-" * 50)
    
    stats_engine = AdvancedStatisticsEngine()
    
    # Test avec liste Python
    list_data = data['time_series'].tolist()
    scores_list = stats_engine.get_detailed_scores(list_data)
    print(f"Score global (List): {scores_list['global_score']:.3f}")
    
    # Test avec Series pandas
    series_data = pd.Series(data['time_series'])
    scores_series = stats_engine.get_detailed_scores(series_data)
    print(f"Score global (Series): {scores_series['global_score']:.3f}")
    
    # Test avec array numpy
    array_data = np.array(data['time_series'])
    scores_array = stats_engine.get_detailed_scores(array_data)
    print(f"Score global (Array): {scores_array['global_score']:.3f}")
    
    # Vérifier la cohérence des résultats
    print(f"Cohérence des résultats: {abs(scores_list['global_score'] - scores_array['global_score']) < 0.001}")

def demonstrate_engine_factory():
    """Démontre l'utilisation de la factory d'engines"""
    
    print("\n\n2. Factory d'Engines - Création polymorphique:")
    print("-" * 50)
    
    data = generate_sample_data(30)
    
    # Créer différents types d'engines
    engine_types = ["statistics", "anomaly", "validation", "scoring"]
    
    for engine_type in engine_types:
        print(f"\nEngine: {engine_type.upper()}")
        engine = create_statistical_engine(engine_type)
        
        # Utiliser l'engine avec polymorphisme
        if engine_type == "scoring":
            results = engine.process(
                data['current_prediction'],
                actual=data['actual_values'],
                date=datetime.now().isoformat()
            )
        else:
            results = engine.process(data['time_series'])
        
        print(f"  - Type d'engine: {type(engine).__name__}")
        print(f"  - Résultats obtenus: {len(results)} métriques")

def demonstrate_analyze_data_function():
    """Démontre la fonction analyze_data avec polymorphisme automatique"""
    
    print("\n\n3. Fonction analyze_data - Polymorphisme automatique:")
    print("-" * 50)
    
    data = generate_sample_data(40)
    
    # Analyser avec différents types d'engines
    engine_types = ["statistics", "anomaly", "validation"]
    
    for engine_type in engine_types:
        print(f"\nAnalyse avec {engine_type}:")
        results = analyze_data(data['time_series'], engine_type=engine_type)
        
        # Extraire les métriques principales
        if engine_type == "statistics":
            main_metric = results.get('global_score', 0.0)
        elif engine_type == "anomaly":
            main_metric = results.get('global_anomaly_score', 0.0)
        elif engine_type == "validation":
            main_metric = results.get('validation_stats', {}).get('stability_score', 0.0)
        
        print(f"  - Métrique principale: {main_metric:.3f}")
        print(f"  - Nombre de métriques calculées: {len(results)}")

def demonstrate_method_overloading():
    """Démontre la surcharge de méthodes"""
    
    print("\n\n4. Surcharge de Méthodes:")
    print("-" * 50)
    
    data = generate_sample_data(25)
    
    # Test de surcharge avec différents types de données
    scoring_engine = AdvancedScoringEngine()
    
    # Test avec différents types de prédictions
    prediction_types = {
        'Liste': data['current_prediction'].tolist(),
        'Series': pd.Series(data['current_prediction']),
        'Array': np.array(data['current_prediction'])
    }
    
    for pred_type, prediction in prediction_types.items():
        print(f"\nPrédiction ({pred_type}):")
        scores = scoring_engine.calculate_detailed_scores(
            prediction,
            actual=data['actual_values'],
            date=datetime.now().isoformat()
        )
        print(f"  - Score global: {scores['global_score']:.3f}")
        print(f"  - Score de cohérence: {scores['coherence_score']:.3f}")
        print(f"  - Score de stabilité: {scores['stability_score']:.3f}")

def demonstrate_inheritance_and_polymorphism():
    """Démontre l'héritage et le polymorphisme"""
    
    print("\n\n5. Héritage et Polymorphisme:")
    print("-" * 50)
    
    # Créer des instances de différents engines
    engines = [
        AdvancedStatisticsEngine(),
        AnomalyDetectionEngine(),
        TemporalValidationEngine(),
        AdvancedScoringEngine()
    ]
    
    for i, engine in enumerate(engines):
        print(f"\nEngine {i+1}: {type(engine).__name__}")
        
        # Vérifier les méthodes communes
        print(f"  - Méthode configure disponible: {hasattr(engine, 'configure')}")
        print(f"  - Méthode process disponible: {hasattr(engine, 'process')}")
        print(f"  - Méthode get_parameters disponible: {hasattr(engine, 'get_parameters')}")
        
        # Configurer l'engine
        engine.configure(test_param="valeur_test")
        params = engine.get_parameters()
        print(f"  - Paramètres configurés: {len(params)} paramètres")

def demonstrate_comprehensive_analysis():
    """Démontre une analyse complète avec tous les engines"""
    
    print("\n\n6. Analyse Complète - Tous les Engines:")
    print("-" * 50)
    
    data = generate_sample_data(60)
    
    # Créer tous les engines
    stats_engine = AdvancedStatisticsEngine()
    anomaly_engine = AnomalyDetectionEngine()
    validation_engine = TemporalValidationEngine()
    scoring_engine = AdvancedScoringEngine()
    
    # Analyser les données avec chaque engine
    print("\nAnalyse statistique avancée:")
    stats_results = stats_engine.process(data['time_series'])
    print(f"  - Score global: {stats_results['global_score']:.3f}")
    print(f"  - Score de variance: {stats_results['variance_score']:.3f}")
    print(f"  - Score d'entropie: {stats_results['entropy_score']:.3f}")
    
    print("\nDétection d'anomalies:")
    anomaly_results = anomaly_engine.process(data['time_series'])
    print(f"  - Score d'anomalie global: {anomaly_results['global_anomaly_score']:.3f}")
    print(f"  - Patterns anormaux détectés: {anomaly_results['pattern_anomaly_analysis']['has_pattern_anomalies']}")
    
    print("\nValidation temporelle:")
    validation_results = validation_engine.process(data['time_series'])
    print(f"  - Stabilité: {validation_results['is_stable']}")
    print(f"  - Score de stabilité: {validation_results['validation_stats']['stability_score']:.3f}")
    
    print("\nScoring avancé:")
    scoring_results = scoring_engine.process(
        data['current_prediction'],
        actual=data['actual_values'],
        date=datetime.now().isoformat()
    )
    print(f"  - Score global: {scoring_results['global_score']:.3f}")
    print(f"  - Recommandations: {len(scoring_results['recommendations'])}")

def main():
    """Fonction principale"""
    
    print("PY_STATS_TOOLKIT - DÉMONSTRATION DU POLYMORPHISME")
    print("=" * 60)
    print("Ce script démontre l'utilisation du toolkit avec polymorphisme,")
    print("surcharge de méthodes et architecture orientée objet.")
    print("=" * 60)
    
    try:
        # Démontrer le polymorphisme
        demonstrate_polymorphism()
        
        # Démontrer la factory d'engines
        demonstrate_engine_factory()
        
        # Démontrer la fonction analyze_data
        demonstrate_analyze_data_function()
        
        # Démontrer la surcharge de méthodes
        demonstrate_method_overloading()
        
        # Démontrer l'héritage et le polymorphisme
        demonstrate_inheritance_and_polymorphism()
        
        # Démontrer une analyse complète
        demonstrate_comprehensive_analysis()
        
        print("\n" + "=" * 60)
        print("DÉMONSTRATION TERMINÉE AVEC SUCCÈS!")
        print("=" * 60)
        print("\nRésumé des fonctionnalités démontrées:")
        print("✓ Polymorphisme avec différents types de données")
        print("✓ Factory pattern pour la création d'engines")
        print("✓ Surcharge de méthodes")
        print("✓ Héritage et architecture orientée objet")
        print("✓ Analyse complète avec tous les modules")
        
    except Exception as e:
        print(f"\nErreur lors de la démonstration: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 