'''
=====================================================================
File : test_factorielle.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module test_factorielle.py

tags : module, stats
=====================================================================
Ce module Description du module test_factorielle.py

tags : module, stats
=====================================================================
'''

# Imports spécifiques au module
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

# Imports de la base
from py_stats_toolkit.Abstracts.AbstractClassBase import StatisticalModule

class TestFactorielle(unittest.TestCase):
    """
    Tests pour le module d'analyse factorielle.
    """
    
    def setUp(self):
        """
        Configuration initiale pour les tests.
        """
        self.data = pd.DataFrame({
            'var1': np.random.normal(0, 1, 100),
            'var2': np.random.normal(0, 1, 100),
            'var3': np.random.normal(0, 1, 100)
        })
        self.factorielle = StatisticalModule()
    
    def test_analyse_factorielle(self):
        """Test de l'analyse factorielle."""
        result = self.factorielle.process(
            self.data,
            n_factors=2
        )
        
        self.assertIn('Méthode', result)
        self.assertIn('Facteurs', result)
        self.assertIn('Valeurs propres', result)
        self.assertIn('Contributions', result)
        self.assertEqual(result['Méthode'], 'Analyse factorielle')
        self.assertEqual(len(result['Facteurs']), 2)
    
    def test_invalid_n_factors(self):
        """Test avec un nombre invalide de facteurs."""
        with self.assertRaises(ValueError):
            self.factorielle.process(
                self.data,
                n_factors=6  # Plus de facteurs que de variables
            )
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.factorielle.process(
                "invalid_data",
                n_factors=2
            )
    
    def test_insufficient_data(self):
        """Test avec des données insuffisantes."""
        small_data = pd.DataFrame({
            'var1': np.random.normal(0, 1, 5),
            'var2': np.random.normal(0, 1, 5)
        })
        
        with self.assertRaises(ValueError):
            self.factorielle.process(
                small_data,
                n_factors=2
            )

if __name__ == '__main__':
    unittest.main() 