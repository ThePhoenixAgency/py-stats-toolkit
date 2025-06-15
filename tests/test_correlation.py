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
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
import unittest

# Imports de la base
from py_stats_toolkit.Abstracts.AbstractClassBase import StatisticalModule
from py_stats_toolkit.stats.correlation.correlation import Correlation

class TestCorrelation(unittest.TestCase):
    """
    Tests pour le module de corrélation.
    """
    
    def setUp(self):
        """
        Configuration initiale pour les tests.
        """
        self.data = pd.DataFrame({
            'x': np.random.normal(0, 1, 100),
            'y': np.random.normal(0, 1, 100)
        })
        self.correlation = StatisticalModule()
        
        # Données de test pour la corrélation de Pearson
        self.pearson_data = pd.DataFrame({
            'x': np.random.normal(0, 1, 100),
            'y': np.random.normal(0, 1, 100)
        })
        
        # Données de test pour la corrélation de Spearman
        self.spearman_data = pd.DataFrame({
            'x': np.random.uniform(0, 1, 100),
            'y': np.random.uniform(0, 1, 100)
        })
        
        # Données de test pour la corrélation de Kendall
        self.kendall_data = pd.DataFrame({
            'x': np.random.uniform(0, 1, 100),
            'y': np.random.uniform(0, 1, 100)
        })
    
    def test_pearson_correlation(self):
        """Test de la corrélation de Pearson."""
        result = self.correlation.process(
            self.pearson_data,
            method="pearson",
            x_col='x',
            y_col='y'
        )
        
        self.assertIn('Méthode', result)
        self.assertIn('Coefficient', result)
        self.assertIn('p-valeur', result)
        self.assertEqual(result['Méthode'], 'Pearson')
    
    def test_spearman_correlation(self):
        """Test de la corrélation de Spearman."""
        result = self.correlation.process(
            self.spearman_data,
            method="spearman",
            x_col='x',
            y_col='y'
        )
        
        self.assertIn('Méthode', result)
        self.assertIn('Coefficient', result)
        self.assertIn('p-valeur', result)
        self.assertEqual(result['Méthode'], 'Spearman')
    
    def test_kendall_correlation(self):
        """Test de la corrélation de Kendall."""
        result = self.correlation.process(
            self.kendall_data,
            method="kendall",
            x_col='x',
            y_col='y'
        )
        
        self.assertIn('Méthode', result)
        self.assertIn('Coefficient', result)
        self.assertIn('p-valeur', result)
        self.assertEqual(result['Méthode'], 'Kendall')
    
    def test_invalid_method(self):
        """Test avec une méthode invalide."""
        with self.assertRaises(ValueError):
            self.correlation.process(
                self.pearson_data,
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
                self.pearson_data,
                method="pearson",
                x_col='invalid_x',
                y_col='y'
            )

import pytest
import numpy as np
import pandas as pd
from py_stats_toolkit.stats.correlation import (
    CorrelationAnalyzer,
    PartialCorrelation,
    CanonicalCorrelation
)

class TestCorrelation:
    @pytest.fixture
    def sample_data(self):
        """Données d'exemple pour les tests."""
        np.random.seed(42)
        n = 100
        x1 = np.random.normal(0, 1, n)
        x2 = 0.5 * x1 + np.random.normal(0, 0.5, n)
        x3 = 0.3 * x1 + 0.7 * x2 + np.random.normal(0, 0.3, n)
        
        return pd.DataFrame({
            'x1': x1,
            'x2': x2,
            'x3': x3
        })
    
    def test_pearson_correlation(self, sample_data):
        """Test de la corrélation de Pearson."""
        analyzer = CorrelationAnalyzer()
        
        # Test corrélation simple
        corr = analyzer.pearson(sample_data['x1'], sample_data['x2'])
        assert -1 <= corr <= 1
        assert abs(corr - 0.5) < 0.2  # Proche de 0.5
        
        # Test matrice de corrélation
        corr_matrix = analyzer.pearson_matrix(sample_data)
        assert corr_matrix.shape == (3, 3)
        assert np.all(np.diag(corr_matrix) == 1)
        assert np.all(corr_matrix == corr_matrix.T)
        
        # Test significativité
        p_value = analyzer.pearson_significance(sample_data['x1'], sample_data['x2'])
        assert 0 <= p_value <= 1
        assert p_value < 0.05  # Corrélation significative
        
    def test_spearman_correlation(self, sample_data):
        """Test de la corrélation de Spearman."""
        analyzer = CorrelationAnalyzer()
        
        # Test corrélation simple
        corr = analyzer.spearman(sample_data['x1'], sample_data['x2'])
        assert -1 <= corr <= 1
        assert abs(corr - 0.5) < 0.2  # Proche de 0.5
        
        # Test matrice de corrélation
        corr_matrix = analyzer.spearman_matrix(sample_data)
        assert corr_matrix.shape == (3, 3)
        assert np.all(np.diag(corr_matrix) == 1)
        assert np.all(corr_matrix == corr_matrix.T)
        
        # Test significativité
        p_value = analyzer.spearman_significance(sample_data['x1'], sample_data['x2'])
        assert 0 <= p_value <= 1
        assert p_value < 0.05  # Corrélation significative
        
    def test_kendall_correlation(self, sample_data):
        """Test de la corrélation de Kendall."""
        analyzer = CorrelationAnalyzer()
        
        # Test corrélation simple
        corr = analyzer.kendall(sample_data['x1'], sample_data['x2'])
        assert -1 <= corr <= 1
        assert abs(corr - 0.5) < 0.2  # Proche de 0.5
        
        # Test matrice de corrélation
        corr_matrix = analyzer.kendall_matrix(sample_data)
        assert corr_matrix.shape == (3, 3)
        assert np.all(np.diag(corr_matrix) == 1)
        assert np.all(corr_matrix == corr_matrix.T)
        
        # Test significativité
        p_value = analyzer.kendall_significance(sample_data['x1'], sample_data['x2'])
        assert 0 <= p_value <= 1
        assert p_value < 0.05  # Corrélation significative
        
    def test_partial_correlation(self, sample_data):
        """Test de la corrélation partielle."""
        partial = PartialCorrelation()
        
        # Test corrélation partielle
        corr = partial.correlation(
            sample_data['x1'],
            sample_data['x2'],
            sample_data['x3']
        )
        assert -1 <= corr <= 1
        
        # Test matrice de corrélation partielle
        corr_matrix = partial.correlation_matrix(sample_data)
        assert corr_matrix.shape == (3, 3)
        assert np.all(np.diag(corr_matrix) == 1)
        assert np.all(corr_matrix == corr_matrix.T)
        
        # Test significativité
        p_value = partial.significance(
            sample_data['x1'],
            sample_data['x2'],
            sample_data['x3']
        )
        assert 0 <= p_value <= 1
        
    def test_canonical_correlation(self, sample_data):
        """Test de la corrélation canonique."""
        canonical = CanonicalCorrelation()
        
        # Préparation des données
        X = sample_data[['x1', 'x2']]
        Y = sample_data[['x3']]
        
        # Test corrélation canonique
        corr = canonical.correlation(X, Y)
        assert 0 <= corr <= 1
        
        # Test coefficients canoniques
        coef_X, coef_Y = canonical.canonical_coefficients(X, Y)
        assert len(coef_X) == X.shape[1]
        assert len(coef_Y) == Y.shape[1]
        
        # Test scores canoniques
        scores_X, scores_Y = canonical.canonical_scores(X, Y)
        assert len(scores_X) == len(X)
        assert len(scores_Y) == len(Y)
        
    def test_correlation_validation(self, sample_data):
        """Test de la validation des données."""
        analyzer = CorrelationAnalyzer()
        
        # Test avec données manquantes
        data_with_nan = sample_data.copy()
        data_with_nan.iloc[0, 0] = np.nan
        
        with pytest.raises(ValueError):
            analyzer.pearson(data_with_nan['x1'], data_with_nan['x2'])
            
        # Test avec données non numériques
        data_with_str = sample_data.copy()
        data_with_str.iloc[0, 0] = 'a'
        
        with pytest.raises(ValueError):
            analyzer.pearson(data_with_str['x1'], data_with_str['x2'])
            
        # Test avec tailles différentes
        with pytest.raises(ValueError):
            analyzer.pearson(sample_data['x1'], sample_data['x2'][:-1])
            
    def test_correlation_visualization(self, sample_data):
        """Test de la visualisation des corrélations."""
        analyzer = CorrelationAnalyzer()
        
        # Test heatmap
        fig = analyzer.plot_correlation_heatmap(sample_data)
        assert fig is not None
        
        # Test scatter matrix
        fig = analyzer.plot_scatter_matrix(sample_data)
        assert fig is not None
        
        # Test corrélation avec intervalle de confiance
        fig = analyzer.plot_correlation_with_ci(
            sample_data['x1'],
            sample_data['x2']
        )
        assert fig is not None 