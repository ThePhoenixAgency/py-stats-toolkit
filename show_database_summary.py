#!/usr/bin/env python3
"""
Script pour afficher un résumé complet de la base de données Py_Stats_Toolkit
"""

import json
import os
from datetime import datetime
from pathlib import Path

def load_json_file(file_path):
    """Charge un fichier JSON avec gestion d'erreur"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        return None

def analyze_history_file(file_path, module_name):
    """Analyse un fichier d'historique et retourne des statistiques"""
    data = load_json_file(file_path)
    if data is None:
        return {
            'module': module_name,
            'status': 'Erreur de chargement',
            'total_records': 0,
            'last_update': None,
            'file_size': os.path.getsize(file_path) if os.path.exists(file_path) else 0
        }
    
    if not data:
        return {
            'module': module_name,
            'status': 'Vide',
            'total_records': 0,
            'last_update': None,
            'file_size': os.path.getsize(file_path)
        }
    
    total_records = len(data)
    last_update = data[-1]['timestamp'] if data else None
    
    # Analyser les types de données
    data_points = [record.get('data_points', 0) for record in data]
    avg_data_points = sum(data_points) / len(data_points) if data_points else 0
    
    return {
        'module': module_name,
        'status': 'Actif',
        'total_records': total_records,
        'last_update': last_update,
        'file_size': os.path.getsize(file_path),
        'avg_data_points': avg_data_points
    }

def main():
    """Fonction principale"""
    print("=" * 80)
    print("RÉSUMÉ DE LA BASE DE DONNÉES PY_STATS_TOOLKIT")
    print("=" * 80)
    
    data_dir = Path("data")
    if not data_dir.exists():
        print("❌ Dossier 'data' non trouvé")
        return
    
    # Fichiers d'historique attendus
    history_files = {
        'anomaly_detection_history.json': 'Détection d\'anomalies',
        'temporal_validation_history.json': 'Validation temporelle',
        'advanced_scoring_history.json': 'Scoring avancé',
        'basic_statistics_history.json': 'Statistiques de base',
        'correlation_history.json': 'Corrélation',
        'regression_history.json': 'Régression',
        'visualization_history.json': 'Visualisation',
        'data_processing_history.json': 'Traitement de données',
        'data_validation_history.json': 'Validation de données'
    }
    
    print(f"\n📊 ANALYSE DES FICHIERS D'HISTORIQUE")
    print("-" * 50)
    
    total_records = 0
    total_size = 0
    active_modules = 0
    
    for filename, module_name in history_files.items():
        file_path = data_dir / filename
        stats = analyze_history_file(file_path, module_name)
        
        status_icon = "✅" if stats['status'] == 'Actif' else "⚠️" if stats['status'] == 'Vide' else "❌"
        
        print(f"{status_icon} {module_name}:")
        print(f"   📁 Fichier: {filename}")
        print(f"   📈 Enregistrements: {stats['total_records']}")
        print(f"   📅 Dernière mise à jour: {stats['last_update'] or 'N/A'}")
        print(f"   💾 Taille: {stats['file_size']} octets")
        if stats['status'] == 'Actif' and stats['total_records'] > 0:
            print(f"   📊 Points de données moyens: {stats['avg_data_points']:.1f}")
        print()
        
        total_records += stats['total_records']
        total_size += stats['file_size']
        if stats['status'] == 'Actif':
            active_modules += 1
    
    print("=" * 80)
    print("📋 RÉSUMÉ GLOBAL")
    print("=" * 80)
    print(f"🔢 Total d'enregistrements: {total_records}")
    print(f"📁 Modules actifs: {active_modules}/{len(history_files)}")
    print(f"💾 Taille totale de la base: {total_size} octets ({total_size/1024:.1f} KB)")
    print(f"📅 Date d'analyse: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Vérifier la cohérence
    print(f"\n🔍 VÉRIFICATIONS")
    print("-" * 30)
    
    if active_modules == len(history_files):
        print("✅ Tous les modules contribuent à la base de données")
    else:
        print(f"⚠️ {len(history_files) - active_modules} module(s) n'ont pas encore d'historique")
    
    if total_records > 0:
        print("✅ La base de données contient des données")
    else:
        print("❌ La base de données est vide")
    
    print("\n" + "=" * 80)
    print("✅ ANALYSE TERMINÉE")
    print("=" * 80)

if __name__ == "__main__":
    main() 