#!/usr/bin/env python3
"""
Script de nettoyage automatique des fichiers cache et temporaires
"""

import os
import shutil
from pathlib import Path

def clean_cache():
    """Nettoie tous les fichiers cache et temporaires"""
    print("🧹 Nettoyage des fichiers cache et temporaires...")
    
    # Dossiers à supprimer
    dirs_to_remove = [
        'dist',
        'build',
        '.pytest_cache',
        'py_stats_toolkit.egg-info',
        'venv',
        'env',
        '.venv',
        'htmlcov',
        '.mypy_cache',
        '.ruff_cache',
        '__pycache__'
    ]
    
    # Fichiers à supprimer
    files_to_remove = [
        '*.pyc',
        '*.pyo',
        '*.pyd',
        '*.so',
        '*.whl',
        '*.tar.gz',
        '*.log',
        '*.tmp',
        '*.temp',
        '.coverage',
        'coverage.xml'
    ]
    
    # Supprimer les dossiers
    for dir_name in dirs_to_remove:
        dir_path = Path(dir_name)
        if dir_path.exists():
            try:
                shutil.rmtree(dir_path)
                print(f"✅ Supprimé: {dir_name}")
            except Exception as e:
                print(f"❌ Erreur lors de la suppression de {dir_name}: {e}")
    
    # Supprimer les fichiers
    for pattern in files_to_remove:
        for file_path in Path('.').rglob(pattern):
            try:
                file_path.unlink()
                print(f"✅ Supprimé: {file_path}")
            except Exception as e:
                print(f"❌ Erreur lors de la suppression de {file_path}: {e}")
    
    # Supprimer les dossiers __pycache__ récursivement
    for pycache_dir in Path('.').rglob('__pycache__'):
        try:
            shutil.rmtree(pycache_dir)
            print(f"✅ Supprimé: {pycache_dir}")
        except Exception as e:
            print(f"❌ Erreur lors de la suppression de {pycache_dir}: {e}")
    
    print("🎉 Nettoyage terminé !")

if __name__ == "__main__":
    clean_cache() 