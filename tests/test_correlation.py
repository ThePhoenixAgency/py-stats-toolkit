'''
=====================================================================
File : test_correlation.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module test_correlation.py

tags : module, stats
=====================================================================
Ce module Description du module test_correlation.py

tags : module, stats
=====================================================================
'''

# Imports spécifiques au module
import unittest
import pytest
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

# Imports de la base
from py_stats_toolkit.stats.correlation.correlation import Correlation

class TestCorrelation(unittest.TestCase):
    """
    Tests pour le module de corrélation.
    """
    
    def setUp(self):
        """
        Configuration initiale pour les tests.
        """
        np.random.seed(42)
        self.data = pd.DataFrame({
            'x': np.random.normal(0, 1, 100),
            'y': np.random.normal(0, 1, 100),
            'z': np.random.normal(0, 1, 100)
        })
        self.correlation = Correlation()
    
    def test_pearson_correlation(self):
        """Test de la corrélation de Pearson."""
        result = self.correlation.process(
            self.data,
            method="pearson",
            x_col='x',
            y_col='y'
        )
        
        self.assertIn('Méthode', result)
        self.assertIn('Coefficient', result)
        self.assertIn('p-valeur', result)
        self.assertEqual(result['Méthode'], 'Pearson')
        self.assertIsInstance(result['Coefficient'], float)
        self.assertIsInstance(result['p-valeur'], float)
        self.assertTrue(-1 <= result['Coefficient'] <= 1)
        self.assertTrue(0 <= result['p-valeur'] <= 1)
    
    def test_spearman_correlation(self):
        """Test de la corrélation de Spearman."""
        result = self.correlation.process(
            self.data,
            method="spearman",
            x_col='x',
            y_col='y'
        )
        
        self.assertIn('Méthode', result)
        self.assertIn('Coefficient', result)
        self.assertIn('p-valeur', result)
        self.assertEqual(result['Méthode'], 'Spearman')
        self.assertIsInstance(result['Coefficient'], float)
        self.assertIsInstance(result['p-valeur'], float)
        self.assertTrue(-1 <= result['Coefficient'] <= 1)
        self.assertTrue(0 <= result['p-valeur'] <= 1)
    
    def test_kendall_correlation(self):
        """Test de la corrélation de Kendall."""
        result = self.correlation.process(
            self.data,
            method="kendall",
            x_col='x',
            y_col='y'
        )
        
        self.assertIn('Méthode', result)
        self.assertIn('Coefficient', result)
        self.assertIn('p-valeur', result)
        self.assertEqual(result['Méthode'], 'Kendall')
        self.assertIsInstance(result['Coefficient'], float)
        self.assertIsInstance(result['p-valeur'], float)
        self.assertTrue(-1 <= result['Coefficient'] <= 1)
        self.assertTrue(0 <= result['p-valeur'] <= 1)
    
    def test_invalid_method(self):
        """Test avec une méthode invalide."""
        with self.assertRaises(ValueError):
            self.correlation.process(
                self.data,
                method="invalid_method",
                x_col='x',
                y_col='y'
            )
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.correlation.process(
                "invalid_data",
                method="pearson",
                x_col='x',
                y_col='y'
            )
    
    def test_missing_columns(self):
        """Test avec des colonnes manquantes."""
        with self.assertRaises(ValueError):
            self.correlation.process(
                self.data,
                method="pearson",
                x_col='invalid_x',
                y_col='y'
            )
    
    def test_missing_parameters(self):
        """Test avec des paramètres manquants."""
        with self.assertRaises(ValueError):
            self.correlation.process(
                self.data,
                method="pearson"
            )
    
    def test_perfect_correlation(self):
        """Test avec une corrélation parfaite."""
        perfect_data = pd.DataFrame({
            'x': np.arange(100),
            'y': np.arange(100)
        })
        
        result = self.correlation.process(
            perfect_data,
            method="pearson",
            x_col='x',
            y_col='y'
        )
        
        self.assertAlmostEqual(result['Coefficient'], 1.0, places=10)
    
    def test_negative_correlation(self):
        """Test avec une corrélation négative."""
        negative_data = pd.DataFrame({
            'x': np.arange(100),
            'y': -np.arange(100)
        })
        
        result = self.correlation.process(
            negative_data,
            method="pearson",
            x_col='x',
            y_col='y'
        )
        
        self.assertAlmostEqual(result['Coefficient'], -1.0, places=10)
    
    def test_no_correlation(self):
        """Test avec aucune corrélation."""
        no_corr_data = pd.DataFrame({
            'x': np.random.normal(0, 1, 100),
            'y': np.random.normal(0, 1, 100)
        })
        
        result = self.correlation.process(
            no_corr_data,
            method="pearson",
            x_col='x',
            y_col='y'
        )
        
        self.assertIsInstance(result['Coefficient'], float)
        self.assertTrue(-1 <= result['Coefficient'] <= 1)

if __name__ == '__main__':
    unittest.main() 