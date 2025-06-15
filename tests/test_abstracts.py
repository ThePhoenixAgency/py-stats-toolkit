'''
=====================================================================
File : test_abstracts.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module contient les tests unitaires pour les classes abstraites
de la bibliothèque py_stats_toolkit.

tags : tests, unitaires, abstraits, validation
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd
from py_stats_toolkit.Abstracts.AbstractClassBase import (
    StatisticalModule,
    TimeSeriesModule,
    RandomProcessModule
)

class TestStatisticalModule:
    """Tests pour la classe StatisticalModule."""
    
    def test_initialization(self):
        """Teste l'initialisation de base."""
        module = StatisticalModule()
        assert module.tags == ["stats", "module"]
        assert module.version == "1.0.0"
        assert module.data is None
        assert module.result is None
    
    def test_validate_data_numpy(self):
        """Teste la validation des données numpy."""
        module = StatisticalModule()
        data = np.array([1, 2, 3])
        module.validate_data(data)
        assert isinstance(module.data, np.ndarray)
    
    def test_validate_data_pandas(self):
        """Teste la validation des données pandas."""
        module = StatisticalModule()
        data = pd.DataFrame({'A': [1, 2, 3]})
        module.validate_data(data)
        assert isinstance(module.data, pd.DataFrame)
    
    def test_validate_data_invalid(self):
        """Teste la validation des données invalides."""
        module = StatisticalModule()
        with pytest.raises(TypeError):
            module.validate_data([1, 2, 3])
    
    def test_str_representation(self):
        """Teste la représentation textuelle."""
        module = StatisticalModule()
        assert str(module) == "Module StatisticalModule v1.0.0"
    
    def test_repr_representation(self):
        """Teste la représentation technique."""
        module = StatisticalModule()
        assert repr(module) == "StatisticalModule(version=1.0.0)"

class TestTimeSeriesModule:
    """Tests pour la classe TimeSeriesModule."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        module = TimeSeriesModule()
        assert module.timestamps is None
    
    def test_set_timestamps(self):
        """Teste la définition des timestamps."""
        module = TimeSeriesModule()
        timestamps = pd.date_range(start='2025-01-01', periods=3)
        module.set_timestamps(timestamps)
        assert isinstance(module.timestamps, pd.DatetimeIndex)
        assert len(module.timestamps) == 3

class TestRandomProcessModule:
    """Tests pour la classe RandomProcessModule."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        module = RandomProcessModule()
        assert module.seed is None
    
    def test_set_seed(self):
        """Teste la définition de la graine."""
        module = RandomProcessModule()
        seed = 42
        module.set_seed(seed)
        assert module.seed == seed
        
        # Vérifie que la graine est bien appliquée
        first_random = np.random.rand()
        module.set_seed(seed)
        second_random = np.random.rand()
        assert first_random == second_random 