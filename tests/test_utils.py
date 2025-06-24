'''
import unittest
=====================================================================
File : test_utils.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module contient les tests unitaires pour les utilitaires
de la bibliothèque py_stats_toolkit.

tags : tests, unitaires, utilitaires, validation
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd
from py_stats_toolkit.utils.data_transformation import DataTransformer
from py_stats_toolkit.utils.data_validation import DataValidator
from py_stats_toolkit.utils.metrics import MetricsCalculator

class TestDataTransformer:
    """Tests pour la classe DataTransformer."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        transformer = DataTransformer()
        assert transformer.data is None
        assert transformer.transformed_data is None
    
    def test_normalize_data(self):
        """Teste la normalisation des données."""
        transformer = DataTransformer()
        data = np.array([1, 2, 3, 4, 5])
        normalized = transformer.normalize(data)
        assert isinstance(normalized, np.ndarray)
        assert np.mean(normalized) == pytest.approx(0, abs=1e-10)
        assert np.std(normalized) == pytest.approx(1, abs=1e-10)
    
    def test_standardize_data(self):
        """Teste la standardisation des données."""
        transformer = DataTransformer()
        data = np.array([1, 2, 3, 4, 5])
        standardized = transformer.standardize(data)
        assert isinstance(standardized, np.ndarray)
        assert np.mean(standardized) == pytest.approx(0, abs=1e-10)
        assert np.std(standardized) == pytest.approx(1, abs=1e-10)
    
    def test_encode_categorical(self):
        """Teste l'encodage des variables catégorielles."""
        transformer = DataTransformer()
        data = pd.Series(['A', 'B', 'A', 'C'])
        encoded = transformer.encode_categorical(data)
        assert isinstance(encoded, np.ndarray)
        assert len(np.unique(encoded)) == 3

class TestDataValidator:
    """Tests pour la classe DataValidator."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        validator = DataValidator()
        assert validator.data is None
        assert validator.validation_results is None
    
    def test_check_missing_values(self):
        """Teste la vérification des valeurs manquantes."""
        validator = DataValidator()
        data = pd.DataFrame({
            'A': [1, np.nan, 3],
            'B': [4, 5, np.nan]
        })
        missing = validator.check_missing_values(data)
        assert isinstance(missing, dict)
        assert 'A' in missing
        assert 'B' in missing
    
    def test_check_outliers(self):
        """Teste la détection des outliers."""
        validator = DataValidator()
        data = np.array([1, 2, 3, 100, 4, 5])
        outliers = validator.check_outliers(data)
        assert isinstance(outliers, np.ndarray)
        assert len(outliers) > 0
    
    def test_validate_data_types(self):
        """Teste la validation des types de données."""
        validator = DataValidator()
        data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        })
        types = validator.validate_data_types(data)
        assert isinstance(types, dict)
        assert 'A' in types
        assert 'B' in types

class TestMetricsCalculator:
    """Tests pour la classe MetricsCalculator."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        calculator = MetricsCalculator()
        assert calculator.metrics is None
    
    def test_calculate_accuracy(self):
        """Teste le calcul de l'exactitude."""
        calculator = MetricsCalculator()
        y_true = np.array([1, 0, 1, 0])
        y_pred = np.array([1, 0, 0, 0])
        accuracy = calculator.calculate_accuracy(y_true, y_pred)
        assert isinstance(accuracy, float)
        assert 0 <= accuracy <= 1
    
    def test_calculate_precision(self):
        """Teste le calcul de la précision."""
        calculator = MetricsCalculator()
        y_true = np.array([1, 0, 1, 0])
        y_pred = np.array([1, 0, 0, 0])
        precision = calculator.calculate_precision(y_true, y_pred)
        assert isinstance(precision, float)
        assert 0 <= precision <= 1
    
    def test_calculate_recall(self):
        """Teste le calcul du rappel."""
        calculator = MetricsCalculator()
        y_true = np.array([1, 0, 1, 0])
        y_pred = np.array([1, 0, 0, 0])
        recall = calculator.calculate_recall(y_true, y_pred)
        assert isinstance(recall, float)
        assert 0 <= recall <= 1
    
    def test_calculate_f1_score(self):
        """Teste le calcul du score F1."""
        calculator = MetricsCalculator()
        y_true = np.array([1, 0, 1, 0])
        y_pred = np.array([1, 0, 0, 0])
        f1 = calculator.calculate_f1_score(y_true, y_pred)
        assert isinstance(f1, float)
        assert 0 <= f1 <= 1 