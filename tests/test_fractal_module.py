'''
import unittest
=====================================================================
File : test_fractal_module.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module contient les tests unitaires pour le module de fractales
de la bibliothèque py_stats_toolkit.

tags : tests, unitaires, fractales, validation
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd

class TestFractalModule:
    """Tests pour la classe FractalModule."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        module = FractalModule()
        assert module.tags == ["stats", "module", "fractal"]
        assert module.version == "1.0.0"
        assert module.data is None
        assert module.result is None
        assert module.dimension is None
        assert module.scales is None
    
    def test_set_data(self):
        """Teste la définition des données."""
        module = FractalModule()
        data = np.array([1, 2, 3, 4, 5])
        module.set_data(data)
        assert isinstance(module.data, np.ndarray)
        assert len(module.data) == 5
    
    def test_calculate_hurst_exponent(self):
        """Teste le calcul de l'exposant de Hurst."""
        module = FractalModule()
        data = np.random.randn(1000)  # Bruit blanc
        module.set_data(data)
        hurst = module.calculate_hurst_exponent()
        assert isinstance(hurst, float)
        assert 0 <= hurst <= 1
    
    def test_calculate_box_counting_dimension(self):
        """Teste le calcul de la dimension de comptage de boîtes."""
        module = FractalModule()
        data = np.array([
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ])
        module.set_data(data)
        dimension = module.calculate_box_counting_dimension()
        assert isinstance(dimension, float)
        assert dimension > 0
    
    def test_calculate_correlation_dimension(self):
        """Teste le calcul de la dimension de corrélation."""
        module = FractalModule()
        data = np.random.randn(100, 2)  # Points 2D
        module.set_data(data)
        dimension = module.calculate_correlation_dimension()
        assert isinstance(dimension, float)
        assert dimension > 0
    
    def test_calculate_lyapunov_exponent(self):
        """Teste le calcul de l'exposant de Lyapunov."""
        module = FractalModule()
        data = np.random.randn(1000)  # Série temporelle
        module.set_data(data)
        lyapunov = module.calculate_lyapunov_exponent()
        assert isinstance(lyapunov, float)
    
    def test_calculate_multifractal_spectrum(self):
        """Teste le calcul du spectre multifractal."""
        module = FractalModule()
        data = np.random.randn(1000)  # Série temporelle
        module.set_data(data)
        spectrum = module.calculate_multifractal_spectrum()
        assert isinstance(spectrum, dict)
        assert 'alpha' in spectrum
        assert 'f_alpha' in spectrum
    
    def test_calculate_detrended_fluctuation(self):
        """Teste le calcul de l'analyse de fluctuation détendue."""
        module = FractalModule()
        data = np.random.randn(1000)  # Série temporelle
        module.set_data(data)
        dfa = module.calculate_detrended_fluctuation()
        assert isinstance(dfa, dict)
        assert 'scales' in dfa
        assert 'fluctuations' in dfa
    
    def test_calculate_renyi_dimensions(self):
        """Teste le calcul des dimensions de Rényi."""
        module = FractalModule()
        data = np.random.randn(100, 2)  # Points 2D
        module.set_data(data)
        dimensions = module.calculate_renyi_dimensions()
        assert isinstance(dimensions, dict)
        assert 'q' in dimensions
        assert 'Dq' in dimensions
    
    def test_calculate_lacunarity(self):
        """Teste le calcul de la lacunarité."""
        module = FractalModule()
        data = np.array([
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ])
        module.set_data(data)
        lacunarity = module.calculate_lacunarity()
        assert isinstance(lacunarity, float)
        assert lacunarity >= 0 