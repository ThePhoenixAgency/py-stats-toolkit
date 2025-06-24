'''
import unittest
=====================================================================
File : test_regression_module.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module contient les tests unitaires pour le module de régression
de la bibliothèque py_stats_toolkit.

tags : tests, unitaires, régression, validation
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd
from py_stats_toolkit.Abstracts.RegressionModule import RegressionModule

class TestRegressionModule:
    """Tests pour la classe RegressionModule."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        module = RegressionModule()
        assert module.tags == ["stats", "module", "regression"]
        assert module.version == "1.0.0"
        assert module.data is None
        assert module.result is None
        assert module.model is None
        assert module.features is None
        assert module.target is None
    
    def test_set_features(self):
        """Teste la définition des features."""
        module = RegressionModule()
        features = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        module.set_features(features)
        assert isinstance(module.features, pd.DataFrame)
        assert module.features.shape == (3, 2)
    
    def test_set_target(self):
        """Teste la définition de la cible."""
        module = RegressionModule()
        target = pd.Series([1, 2, 3])
        module.set_target(target)
        assert isinstance(module.target, pd.Series)
        assert len(module.target) == 3
    
    def test_validate_data_dimensions(self):
        """Teste la validation des dimensions des données."""
        module = RegressionModule()
        features = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        target = pd.Series([1, 2])
        
        module.set_features(features)
        with pytest.raises(ValueError):
            module.set_target(target)
    
    def test_fit_model(self):
        """Teste l'entraînement du modèle."""
        module = RegressionModule()
        features = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        target = pd.Series([2, 4, 6])
        
        module.set_features(features)
        module.set_target(target)
        module.fit()
        
        assert module.model is not None
        assert hasattr(module.model, 'predict')
    
    def test_predict(self):
        """Teste la prédiction."""
        module = RegressionModule()
        features = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        target = pd.Series([2, 4, 6])
        
        module.set_features(features)
        module.set_target(target)
        module.fit()
        
        new_data = pd.DataFrame({
            'A': [4],
            'B': [7]
        })
        predictions = module.predict(new_data)
        assert isinstance(predictions, np.ndarray)
        assert len(predictions) == 1
    
    def test_evaluate(self):
        """Teste l'évaluation du modèle."""
        module = RegressionModule()
        features = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        target = pd.Series([2, 4, 6])
        
        module.set_features(features)
        module.set_target(target)
        module.fit()
        
        metrics = module.evaluate()
        assert isinstance(metrics, dict)
        assert 'mse' in metrics
        assert 'r2' in metrics 