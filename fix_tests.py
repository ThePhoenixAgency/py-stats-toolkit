#!/usr/bin/env python3
"""
Script pour corriger automatiquement les problèmes d'imports dans les tests
"""

import os
import re
from pathlib import Path

def fix_test_file(file_path):
    """Corrige les imports dans un fichier de test"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ajouter les imports manquants
    if 'import unittest' not in content:
        # Trouver la ligne après les commentaires
        lines = content.split('\n')
        insert_index = 0
        
        for i, line in enumerate(lines):
            if line.strip().startswith('#') or line.strip().startswith("'''") or line.strip().startswith('"""'):
                continue
            if line.strip() == '':
                continue
            insert_index = i
            break
        
        # Insérer les imports manquants
        imports_to_add = [
            'import unittest',
            'import pytest',
            'import numpy as np',
            'import pandas as pd'
        ]
        
        # Vérifier quels imports sont déjà présents
        existing_imports = []
        for line in lines:
            if line.strip().startswith('import ') or line.strip().startswith('from '):
                existing_imports.append(line.strip())
        
        # Ajouter seulement les imports manquants
        new_imports = []
        for imp in imports_to_add:
            if not any(imp.split()[1] in existing for existing in existing_imports):
                new_imports.append(imp)
        
        if new_imports:
            lines.insert(insert_index, '\n'.join(new_imports))
            content = '\n'.join(lines)
    
    # Corriger les références à unittest.TestCase
    if 'class Test' in content and 'unittest.TestCase' not in content:
        content = re.sub(r'class (Test\w+)\(([^)]+)\):', r'class \1(unittest.TestCase):', content)
    
    # Corriger les références à pytest.fixture
    if '@pytest.fixture' in content and 'import pytest' not in content:
        if 'import pytest' not in content:
            content = 'import pytest\n' + content
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Corrigé: {file_path}")

def main():
    """Fonction principale"""
    tests_dir = Path('tests')
    
    if not tests_dir.exists():
        print("Dossier tests non trouvé")
        return
    
    # Lister tous les fichiers de test
    test_files = list(tests_dir.glob('test_*.py'))
    
    print(f"Trouvé {len(test_files)} fichiers de test")
    
    for test_file in test_files:
        try:
            fix_test_file(test_file)
        except Exception as e:
            print(f"Erreur lors de la correction de {test_file}: {e}")

if __name__ == '__main__':
    main() 