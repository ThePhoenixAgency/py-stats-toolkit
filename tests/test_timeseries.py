'''
import unittest
import pytest
=====================================================================
File : test_timeseries.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module test_timeseries.py

tags : module, stats
=====================================================================
Ce module Description du module test_timeseries.py

tags : module, stats
=====================================================================
'''

# Imports spécifiques au module
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

class TestTimeSeries(unittest.TestCase):
    """
    Tests pour le module de séries temporelles.
    """
    
    def setUp(self):
        """
        Configuration initiale pour les tests.
        """
        self.data = pd.DataFrame({
            'date': pd.date_range(start='2020-01-01', periods=100),
            'value': np.random.normal(0, 1, 100)
        })
    
    def test_analyse_timeseries(self):
        """Test de l'analyse de séries temporelles."""
        result = self.timeseries.process(
            self.data,
            method="decomposition",
            date_col='date',
            value_col='value'
        )
        
        self.assertIn('Méthode', result)
        self.assertIn('Tendance', result)
        self.assertIn('Saisonnalité', result)
        self.assertIn('Résidus', result)
        self.assertEqual(result['Méthode'], 'Décomposition')
    
    def test_invalid_method(self):
        """Test avec une méthode invalide."""
        with self.assertRaises(ValueError):
            self.timeseries.process(
                self.data,
                method="invalid_method",
                date_col='date',
                value_col='value'
            )
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.timeseries.process(
                "invalid_data",
                method="decomposition",
                date_col='date',
                value_col='value'
            )
    
    def test_missing_columns(self):
        """Test avec des colonnes manquantes."""
        with self.assertRaises(ValueError):
            self.timeseries.process(
                self.data,
                method="decomposition",
                date_col='invalid_date',
                value_col='value'
            )

if __name__ == '__main__':
    unittest.main() 