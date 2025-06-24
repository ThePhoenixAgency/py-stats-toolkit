'''
=====================================================================
File : test_regression.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module test_regression.py

tags : module, stats
=====================================================================
Ce module Description du module test_regression.py

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
from py_stats_toolkit.stats.regression.regression import Regression

class TestRegression(unittest.TestCase):
    """
    Tests pour le module de régression.
    """
    
    def setUp(self):
        """
        Configuration initiale pour les tests.
        """
        np.random.seed(42)
        self.X = np.random.normal(0, 1, (100, 2))
        self.y_linear = 2 * self.X[:, 0] + 3 * self.X[:, 1] + np.random.normal(0, 0.1, 100)
        
        self.data = pd.DataFrame({
            'x1': self.X[:, 0],
            'x2': self.X[:, 1],
            'y': self.y_linear
        })
        
        self.regression = Regression()
    
    def test_linear_regression(self):
        """Test de la régression linéaire."""
        result = self.regression.process(
            self.data,
            target_col='y',
            feature_cols=['x1', 'x2']
        )
        
        self.assertIn('Coefficients', result)
        self.assertIn('Intercept', result)
        self.assertIn('R²', result)
        self.assertIn('MSE', result)
        
        self.assertIsInstance(result['Coefficients'], dict)
        self.assertIsInstance(result['Intercept'], float)
        self.assertIsInstance(result['R²'], float)
        self.assertIsInstance(result['MSE'], float)
        self.assertTrue(0 <= result['R²'] <= 1)
        self.assertTrue(result['MSE'] >= 0)
    
    def test_regression_coefficients(self):
        """Test des coefficients de régression."""
        result = self.regression.process(
            self.data,
            target_col='y',
            feature_cols=['x1', 'x2']
        )
        
        # Vérifier que les coefficients sont dans le bon ordre
        self.assertIn('x1', result['Coefficients'])
        self.assertIn('x2', result['Coefficients'])
        self.assertIsInstance(result['Coefficients']['x1'], float)
        self.assertIsInstance(result['Coefficients']['x2'], float)
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.regression.process(
                "invalid_data",
                target_col='y',
                feature_cols=['x1', 'x2']
            )
    
    def test_missing_target_column(self):
        """Test avec une colonne cible manquante."""
        with self.assertRaises(ValueError):
            self.regression.process(
                self.data,
                target_col='invalid_target',
                feature_cols=['x1', 'x2']
            )
    
    def test_missing_feature_columns(self):
        """Test avec des colonnes de caractéristiques manquantes."""
        with self.assertRaises(ValueError):
            self.regression.process(
                self.data,
                target_col='y',
                feature_cols=['x1', 'invalid_feature']
            )
    
    def test_missing_parameters(self):
        """Test avec des paramètres manquants."""
        with self.assertRaises(ValueError):
            self.regression.process(
                self.data
            )
    
    def test_insufficient_data(self):
        """Test avec des données insuffisantes."""
        small_data = self.data.head(5)
        with self.assertRaises(ValueError):
            self.regression.process(
                small_data,
                target_col='y',
                feature_cols=['x1', 'x2']
            )
    
    def test_perfect_fit(self):
        """Test avec un ajustement parfait."""
        perfect_data = pd.DataFrame({
            'x1': np.arange(100),
            'x2': np.arange(100) * 2,
            'y': np.arange(100) + np.arange(100) * 2  # y = x1 + x2
        })
        
        result = self.regression.process(
            perfect_data,
            target_col='y',
            feature_cols=['x1', 'x2']
        )
        
        # Avec un ajustement parfait, R² devrait être proche de 1
        self.assertGreater(result['R²'], 0.99)
        self.assertLess(result['MSE'], 0.01)
    
    def test_single_feature(self):
        """Test avec une seule caractéristique."""
        single_feature_data = pd.DataFrame({
            'x1': np.arange(100),
            'y': 2 * np.arange(100) + np.random.normal(0, 0.1, 100)
        })
        
        result = self.regression.process(
            single_feature_data,
            target_col='y',
            feature_cols=['x1']
        )
        
        self.assertIn('x1', result['Coefficients'])
        self.assertIsInstance(result['Coefficients']['x1'], float)
        self.assertTrue(0 <= result['R²'] <= 1)
        self.assertTrue(result['MSE'] >= 0)

if __name__ == '__main__':
    unittest.main() 