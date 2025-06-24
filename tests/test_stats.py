'''
import unittest
=====================================================================
File : test_stats.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module contient les tests unitaires pour les modules statistiques
de la bibliothèque py_stats_toolkit.

tags : tests, unitaires, statistiques, validation
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd
from py_stats_toolkit.stats.descriptives.basic_stats import BasicStatistics
from py_stats_toolkit.stats.correlation import CorrelationAnalysis
from py_stats_toolkit.stats.probabilistes import ProbabilityAnalysis
from py_stats_toolkit.stats.regression import RegressionAnalysis

class TestStats(unittest.TestCase):
    """
    Tests pour le module de statistiques descriptives.
    """
    
    def setUp(self):
        """
        Configuration initiale pour les tests.
        """
        np.random.seed(42)
        self.data = pd.DataFrame({
            'numeric': np.random.normal(0, 1, 100),
            'categorical': np.random.choice(['A', 'B', 'C'], 100),
            'binary': np.random.choice([0, 1], 100)
        })
        self.stats = BasicStatistics()
    
    def test_basic_statistics(self):
        """Test des statistiques de base."""
        result = self.stats.process(self.data['numeric'])
        
        self.assertIn('mean', result)
        self.assertIn('median', result)
        self.assertIn('std', result)
        self.assertIn('min', result)
        self.assertIn('max', result)
        self.assertIn('q1', result)
        self.assertIn('q3', result)
        self.assertIn('iqr', result)
        self.assertIn('skewness', result)
        self.assertIn('kurtosis', result)
        
        self.assertIsInstance(result['mean'], float)
        self.assertIsInstance(result['median'], float)
        self.assertIsInstance(result['std'], float)
        self.assertIsInstance(result['min'], float)
        self.assertIsInstance(result['max'], float)
        self.assertIsInstance(result['q1'], float)
        self.assertIsInstance(result['q3'], float)
        self.assertIsInstance(result['iqr'], float)
        self.assertIsInstance(result['skewness'], float)
        self.assertIsInstance(result['kurtosis'], float)
    
    def test_dataframe_statistics(self):
        """Test des statistiques sur un DataFrame."""
        result = self.stats.process(self.data)
        
        self.assertIn('numeric', result)
        self.assertIn('categorical', result)
        self.assertIn('binary', result)
        
        # Vérifier que chaque colonne a ses statistiques
        numeric_stats = result['numeric']
        self.assertIn('mean', numeric_stats)
        self.assertIn('median', numeric_stats)
        self.assertIn('std', numeric_stats)
    
    def test_series_statistics(self):
        """Test des statistiques sur une Series."""
        series = pd.Series(np.random.normal(0, 1, 100))
        result = self.stats.process(series)
        
        self.assertIn('mean', result)
        self.assertIn('median', result)
        self.assertIn('std', result)
        self.assertIn('min', result)
        self.assertIn('max', result)
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.stats.process("invalid_data")
    
    def test_empty_data(self):
        """Test avec des données vides."""
        empty_data = pd.Series([])
        with self.assertRaises(ValueError):
            self.stats.process(empty_data)
    
    def test_single_value(self):
        """Test avec une seule valeur."""
        single_value = pd.Series([5.0])
        result = self.stats.process(single_value)
        
        self.assertEqual(result['mean'], 5.0)
        self.assertEqual(result['median'], 5.0)
        self.assertEqual(result['std'], 0.0)
        self.assertEqual(result['min'], 5.0)
        self.assertEqual(result['max'], 5.0)
    
    def test_constant_data(self):
        """Test avec des données constantes."""
        constant_data = pd.Series([1.0] * 10)
        result = self.stats.process(constant_data)
        
        self.assertEqual(result['mean'], 1.0)
        self.assertEqual(result['median'], 1.0)
        self.assertEqual(result['std'], 0.0)
        self.assertEqual(result['skewness'], 0.0)
        self.assertEqual(result['kurtosis'], 0.0)
    
    def test_quartiles(self):
        """Test des quartiles."""
        data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = self.stats.process(data)
        
        self.assertEqual(result['q1'], 3.25)  # Premier quartile
        self.assertEqual(result['q3'], 7.75)  # Troisième quartile
        self.assertEqual(result['iqr'], 4.5)  # Intervalle interquartile
    
    def test_skewness_and_kurtosis(self):
        """Test de l'asymétrie et de l'aplatissement."""
        # Données asymétriques
        skewed_data = pd.Series(np.random.exponential(1, 100))
        result = self.stats.process(skewed_data)
        
        self.assertIsInstance(result['skewness'], float)
        self.assertIsInstance(result['kurtosis'], float)
        
        # L'asymétrie devrait être positive pour des données exponentielles
        self.assertGreater(result['skewness'], 0)
    
    def test_normal_distribution(self):
        """Test avec une distribution normale."""
        normal_data = pd.Series(np.random.normal(0, 1, 1000))
        result = self.stats.process(normal_data)
        
        # Pour une distribution normale, l'asymétrie devrait être proche de 0
        self.assertLess(abs(result['skewness']), 0.5)
        
        # L'aplatissement devrait être proche de 0 pour une normale
        self.assertLess(abs(result['kurtosis']), 1.0)
    
    def test_edge_cases(self):
        """Test des cas limites."""
        # Données avec des valeurs extrêmes
        extreme_data = pd.Series([1, 2, 3, 1000])
        result = self.stats.process(extreme_data)
        
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['max'], 1000)
        self.assertGreater(result['mean'], 250)  # Moyenne élevée à cause de 1000
    
    def test_numpy_array(self):
        """Test avec un array numpy."""
        array_data = np.random.normal(0, 1, 100)
        result = self.stats.process(array_data)
        
        self.assertIn('mean', result)
        self.assertIn('median', result)
        self.assertIn('std', result)
        self.assertIsInstance(result['mean'], float)

class TestCorrelationAnalysis:
    """Tests pour la classe CorrelationAnalysis."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        analysis = CorrelationAnalysis()
        assert analysis.data is None
        assert analysis.results is None
    
    def test_calculate_pearson(self):
        """Teste le calcul de la corrélation de Pearson."""
        analysis = CorrelationAnalysis()
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 6, 8, 10])
        corr = analysis.calculate_pearson(x, y)
        assert isinstance(corr, float)
        assert -1 <= corr <= 1
    
    def test_calculate_spearman(self):
        """Teste le calcul de la corrélation de Spearman."""
        analysis = CorrelationAnalysis()
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 6, 8, 10])
        corr = analysis.calculate_spearman(x, y)
        assert isinstance(corr, float)
        assert -1 <= corr <= 1
    
    def test_calculate_kendall(self):
        """Teste le calcul de la corrélation de Kendall."""
        analysis = CorrelationAnalysis()
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 6, 8, 10])
        corr = analysis.calculate_kendall(x, y)
        assert isinstance(corr, float)
        assert -1 <= corr <= 1

class TestProbabilityAnalysis:
    """Tests pour la classe ProbabilityAnalysis."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        analysis = ProbabilityAnalysis()
        assert analysis.data is None
        assert analysis.results is None
    
    def test_calculate_probability(self):
        """Teste le calcul de probabilité."""
        analysis = ProbabilityAnalysis()
        data = np.array([1, 2, 2, 3, 3, 3])
        prob = analysis.calculate_probability(data, 2)
        assert isinstance(prob, float)
        assert 0 <= prob <= 1
    
    def test_calculate_conditional_probability(self):
        """Teste le calcul de probabilité conditionnelle."""
        analysis = ProbabilityAnalysis()
        data = pd.DataFrame({
            'A': [1, 1, 0, 0],
            'B': [1, 0, 1, 0]
        })
        prob = analysis.calculate_conditional_probability(data, 'A', 'B')
        assert isinstance(prob, float)
        assert 0 <= prob <= 1

class TestRegressionAnalysis:
    """Tests pour la classe RegressionAnalysis."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        analysis = RegressionAnalysis()
        assert analysis.data is None
        assert analysis.results is None
    
    def test_linear_regression(self):
        """Teste la régression linéaire."""
        analysis = RegressionAnalysis()
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 6, 8, 10])
        model = analysis.linear_regression(x, y)
        assert isinstance(model, dict)
        assert 'slope' in model
        assert 'intercept' in model
    
    def test_polynomial_regression(self):
        """Teste la régression polynomiale."""
        analysis = RegressionAnalysis()
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([1, 4, 9, 16, 25])
        model = analysis.polynomial_regression(x, y, degree=2)
        assert isinstance(model, dict)
        assert 'coefficients' in model 