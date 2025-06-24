#!/usr/bin/env python3
"""
Exemple d'utilisation des modules utilitaires avec historique de Py_Stats_Toolkit
"""

import numpy as np
import pandas as pd
from py_stats_toolkit.utils.data_processor import DataProcessor
from py_stats_toolkit.utils.data_validator import DataValidator

def main():
    """Fonction principale de démonstration"""
    print("=" * 80)
    print("DÉMONSTRATION DES MODULES UTILITAIRES AVEC HISTORIQUE")
    print("=" * 80)
    
    # Créer des données de test avec quelques problèmes
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.normal(0, 1, 100),
        'y': np.random.normal(0, 1, 100),
        'z': np.random.normal(0, 1, 100)
    })
    
    # Ajouter quelques valeurs manquantes et extrêmes
    data.loc[10:15, 'x'] = np.nan
    data.loc[20, 'y'] = 1000  # Valeur extrême
    data.loc[25, 'z'] = -1000  # Valeur extrême
    
    print(f"📊 Données de test créées: {len(data)} lignes")
    print(f"📋 Colonnes: {list(data.columns)}")
    print(f"🔍 Valeurs manquantes: {data.isnull().sum().sum()}")
    print()
    
    # 1. Validation des données
    print("1️⃣ VALIDATION DES DONNÉES")
    print("-" * 40)
    validator = DataValidator()
    
    # Effectuer plusieurs validations
    validation_types = ['comprehensive', 'numeric', 'missing', 'dimensions']
    
    for vtype in validation_types:
        print(f"   Validation {vtype}...")
        result = validator.process(data, validation_type=vtype)
        status = "✅" if result['is_valid'] else "❌"
        print(f"   {status} Valid: {result['is_valid']}, Issues: {len(result['issues'])}, Warnings: {len(result['warnings'])}")
    
    # Afficher l'historique
    history_val = validator.get_validation_history()
    print(f"\n   📈 Historique des validations:")
    print(f"      Total de validations: {history_val['total_validations']}")
    print(f"      Taux de succès: {history_val['success_rate']:.2%}")
    print(f"      Types de validation: {history_val['most_common_validation_types']}")
    print()
    
    # 2. Traitement des données
    print("2️⃣ TRAITEMENT DES DONNÉES")
    print("-" * 40)
    processor = DataProcessor()
    
    # Effectuer plusieurs traitements
    operations = [
        ('standardize', 'Standardisation'),
        ('normalize', 'Normalisation'),
        ('robust_scale', 'Normalisation robuste'),
        ('handle_missing', 'Traitement des valeurs manquantes')
    ]
    
    for operation, description in operations:
        print(f"   {description}...")
        if operation == 'handle_missing':
            result = processor.process(data, operation=operation, strategy='mean')
        else:
            result = processor.process(data, operation=operation)
        
        processed_data = result['processed_data']
        print(f"   ✅ Opération: {result['operation_info']}")
        print(f"   📊 Forme: {result['original_shape']} -> {result['processed_shape']}")
        
        # Afficher quelques statistiques
        if hasattr(processed_data, 'describe'):
            stats = processed_data.describe()
            print(f"   📈 Moyenne après traitement: {stats.loc['mean', 'x']:.4f}")
    
    # Afficher l'historique
    history_proc = processor.get_processing_history()
    print(f"\n   📈 Historique des traitements:")
    print(f"      Total d'opérations: {history_proc['total_operations']}")
    print(f"      Opérations les plus utilisées: {history_proc['most_common_operations']}")
    print(f"      Stratégies les plus utilisées: {history_proc['most_common_strategies']}")
    print()
    
    # 3. Workflow complet
    print("3️⃣ WORKFLOW COMPLET")
    print("-" * 40)
    
    # Créer de nouvelles données
    new_data = pd.DataFrame({
        'feature1': np.random.normal(10, 5, 50),
        'feature2': np.random.normal(20, 10, 50),
        'target': np.random.normal(100, 15, 50)
    })
    
    print(f"   📊 Nouvelles données: {len(new_data)} lignes")
    
    # 1. Valider les données
    print("   🔍 Étape 1: Validation...")
    val_result = validator.process(new_data, validation_type='comprehensive')
    print(f"   ✅ Validation: {'OK' if val_result['is_valid'] else 'ÉCHEC'}")
    
    if not val_result['is_valid']:
        print(f"   ⚠️ Problèmes détectés: {val_result['issues']}")
    
    # 2. Traiter les données
    print("   🔧 Étape 2: Traitement...")
    proc_result = processor.process(new_data, operation='standardize')
    print(f"   ✅ Traitement: {proc_result['operation_info']}")
    
    # 3. Afficher les résultats
    print("   📊 Étape 3: Résultats...")
    processed_stats = proc_result['statistics']
    print(f"   📈 Statistiques après standardisation:")
    
    # Gérer les différents types de statistiques
    if isinstance(processed_stats, dict):
        mean_val = processed_stats.get('mean', 'N/A')
        std_val = processed_stats.get('std', 'N/A')
        
        if isinstance(mean_val, (int, float)):
            print(f"      Moyenne: {mean_val:.4f}")
        else:
            print(f"      Moyenne: {mean_val}")
            
        if isinstance(std_val, (int, float)):
            print(f"      Écart-type: {std_val:.4f}")
        else:
            print(f"      Écart-type: {std_val}")
    else:
        print(f"      Statistiques: {processed_stats}")
    print()
    
    # 4. Résumé global
    print("4️⃣ RÉSUMÉ GLOBAL")
    print("-" * 40)
    
    total_operations = (
        history_val['total_validations'] +
        history_proc['total_operations']
    )
    
    print(f"   🔢 Total d'opérations effectuées: {total_operations}")
    print(f"   🔍 Validations: {history_val['total_validations']} opérations")
    print(f"   🔧 Traitements: {history_proc['total_operations']} opérations")
    print(f"   📊 Taux de succès des validations: {history_val['success_rate']:.2%}")
    print()
    
    print("=" * 80)
    print("✅ DÉMONSTRATION TERMINÉE")
    print("=" * 80)
    print("💡 Les modules utilitaires sauvegardent automatiquement leur historique")
    print("💡 Utilisez les méthodes get_*_history() pour analyser les tendances")
    print("💡 Les fichiers JSON sont stockés dans le dossier 'data/'")

if __name__ == "__main__":
    main() 