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
from py_stats_toolkit.stats.descriptives import DescriptiveStats
from py_stats_toolkit.stats.correlation import CorrelationAnalysis
from py_stats_toolkit.stats.probabilistes import ProbabilityAnalysis
from py_stats_toolkit.stats.regression import RegressionAnalysis

class TestDescriptiveStats:
    """Tests pour la classe DescriptiveStats."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        stats = DescriptiveStats()
        assert stats.data is None
        assert stats.results is None
    
    def test_calculate_mean(self):
        """Teste le calcul de la moyenne."""
        stats = DescriptiveStats()
        data = np.array([1, 2, 3, 4, 5])
        mean = stats.calculate_mean(data)
        assert isinstance(mean, float)
        assert mean == 3.0
    
    def test_calculate_median(self):
        """Teste le calcul de la médiane."""
        stats = DescriptiveStats()
        data = np.array([1, 2, 3, 4, 5])
        median = stats.calculate_median(data)
        assert isinstance(median, float)
        assert median == 3.0
    
    def test_calculate_mode(self):
        """Teste le calcul du mode."""
        stats = DescriptiveStats()
        data = np.array([1, 2, 2, 3, 4])
        mode = stats.calculate_mode(data)
        assert isinstance(mode, (int, float))
        assert mode == 2
    
    def test_calculate_variance(self):
        """Teste le calcul de la variance."""
        stats = DescriptiveStats()
        data = np.array([1, 2, 3, 4, 5])
        variance = stats.calculate_variance(data)
        assert isinstance(variance, float)
        assert variance > 0
    
    def test_calculate_std(self):
        """Teste le calcul de l'écart-type."""
        stats = DescriptiveStats()
        data = np.array([1, 2, 3, 4, 5])
        std = stats.calculate_std(data)
        assert isinstance(std, float)
        assert std > 0

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