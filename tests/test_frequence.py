'''
=====================================================================
File : test_frequence.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module test_frequence.py

tags : module, stats
=====================================================================
Ce module Description du module test_frequence.py

tags : module, stats
=====================================================================
'''

# Imports spécifiques au module
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

# Imports de la base
from py_stats_toolkit.Abstracts.AbstractClassBase import StatisticalModule

class TestFrequence(unittest.TestCase):
    """
    Tests pour le module de fréquences.
    """
    
    def setUp(self):
        """
        Configuration initiale pour les tests.
        """
        self.data = pd.DataFrame({
            'categorie': ['A', 'B', 'A', 'C', 'B', 'A'],
            'valeur': [1, 2, 3, 4, 5, 6]
        })
        self.frequence = StatisticalModule()
    
    def test_analyse_frequence(self):
        """Test de l'analyse de fréquence."""
        result = self.frequence.process(
            self.data,
            category_col='categorie'
        )
        
        self.assertIn('Méthode', result)
        self.assertIn('Fréquences', result)
        self.assertIn('Pourcentages', result)
        self.assertEqual(result['Méthode'], 'Analyse de fréquence')
        self.assertEqual(len(result['Fréquences']), 3)
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.frequence.process(
                "invalid_data",
                category_col='categorie'
            )
    
    def test_missing_columns(self):
        """Test avec des colonnes manquantes."""
        with self.assertRaises(ValueError):
            self.frequence.process(
                self.data,
                category_col='invalid_col'
            )
    
    def test_empty_data(self):
        """Test avec des données vides."""
        empty_data = pd.DataFrame(columns=['categorie', 'valeur'])
        
        with self.assertRaises(ValueError):
            self.frequence.process(
                empty_data,
                category_col='categorie'
            )

if __name__ == '__main__':
    unittest.main() 