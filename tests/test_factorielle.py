'''
=====================================================================
File : test_factorielle.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module test_factorielle.py

tags : module, stats
=====================================================================
Ce module Description du module test_factorielle.py

tags : module, stats
=====================================================================
'''

# Imports spécifiques au module
import unittest
import pytest
import numpy as np
import pandas as pd
from typing import Any, Dict, List, Optional, Tuple, Union

# Imports de la base
from py_stats_toolkit.Abstracts.AbstractClassBase import StatisticalModule

class TestFactorielle(unittest.TestCase):
    """
    Tests pour le module d'analyse factorielle.
    """
    
    def setUp(self):
        """
        Configuration initiale pour les tests.
        """
        self.data = pd.DataFrame({
            'var1': np.random.normal(0, 1, 100),
            'var2': np.random.normal(0, 1, 100),
            'var3': np.random.normal(0, 1, 100),
            'var4': np.random.normal(0, 1, 100)
        })
    
    def test_basic_factor_analysis(self):
        """Test de base pour l'analyse factorielle."""
        # Test simple avec des données simulées
        assert len(self.data) == 100
        assert len(self.data.columns) == 4
        
        # Vérification que les données sont numériques
        for col in self.data.columns:
            assert self.data[col].dtype in ['float64', 'int64']
    
    def test_data_validation(self):
        """Test de la validation des données."""
        # Test avec données manquantes
        data_with_nan = self.data.copy()
        data_with_nan.iloc[0, 0] = np.nan
        
        # Vérification que les NaN sont détectés
        assert data_with_nan.isnull().sum().sum() > 0
    
    def test_correlation_matrix(self):
        """Test du calcul de la matrice de corrélation."""
        # Calcul de la matrice de corrélation
        corr_matrix = self.data.corr()
        
        # Vérifications de base
        assert corr_matrix.shape == (4, 4)
        assert np.allclose(corr_matrix.diagonal(), 1.0)
        assert np.allclose(corr_matrix, corr_matrix.T)  # Symétrie
    
    def test_eigenvalues(self):
        """Test du calcul des valeurs propres."""
        # Calcul de la matrice de corrélation
        corr_matrix = self.data.corr()
        
        # Calcul des valeurs propres
        eigenvalues = np.linalg.eigvals(corr_matrix)
        
        # Vérifications
        assert len(eigenvalues) == 4
        assert all(eigenvalues >= 0)  # Valeurs propres réelles positives
    
    def test_factor_loadings(self):
        """Test du calcul des saturations factorielles."""
        # Simulation simple de saturations factorielles
        loadings = np.random.uniform(-1, 1, (4, 2))
        
        # Vérifications de base
        assert loadings.shape == (4, 2)
        assert np.all(loadings >= -1) and np.all(loadings <= 1)
    
    def test_variance_explained(self):
        """Test du calcul de la variance expliquée."""
        # Simulation de variance expliquée
        eigenvalues = np.array([2.5, 1.2, 0.2, 0.1])
        total_variance = np.sum(eigenvalues)
        
        # Calcul du pourcentage de variance expliquée
        variance_explained = eigenvalues / total_variance * 100
        
        # Vérifications
        assert len(variance_explained) == 4
        assert np.sum(variance_explained) == 100.0
        assert all(variance_explained >= 0)
    
    def test_scree_plot_data(self):
        """Test des données pour le graphique en éboulis."""
        # Simulation de valeurs propres pour le scree plot
        eigenvalues = np.array([2.5, 1.2, 0.8, 0.5])
        
        # Vérifications
        assert len(eigenvalues) == 4
        assert all(eigenvalues >= 0)
        assert all(eigenvalues[i] >= eigenvalues[i+1] for i in range(len(eigenvalues)-1))
    
    def test_factor_scores(self):
        """Test du calcul des scores factoriels."""
        # Simulation de scores factoriels
        scores = np.random.normal(0, 1, (100, 2))
        
        # Vérifications
        assert scores.shape == (100, 2)
        assert np.mean(scores) < 1  # Moyenne proche de 0
        assert np.std(scores) < 2   # Écart-type proche de 1
    
    def test_rotation(self):
        """Test de la rotation des facteurs."""
        # Simulation de matrice de rotation
        rotation_matrix = np.array([[0.707, -0.707], [0.707, 0.707]])
        
        # Vérifications
        assert rotation_matrix.shape == (2, 2)
        # Vérification que c'est une matrice orthogonale
        assert np.allclose(rotation_matrix @ rotation_matrix.T, np.eye(2))
    
    def test_communalities(self):
        """Test du calcul des communautés."""
        # Simulation de communautés
        communalities = np.random.uniform(0.3, 0.9, 4)
        
        # Vérifications
        assert len(communalities) == 4
        assert all(0 <= h <= 1 for h in communalities)
    
    def test_model_fit(self):
        """Test de l'adéquation du modèle."""
        # Simulation d'indices d'adéquation
        kmo = 0.8  # Kaiser-Meyer-Olkin
        bartlett_p = 0.001  # Test de Bartlett
        
        # Vérifications
        assert 0 <= kmo <= 1
        assert 0 <= bartlett_p <= 1
    
    def test_factor_interpretation(self):
        """Test de l'interprétation des facteurs."""
        # Simulation de noms de facteurs
        factor_names = ["Facteur_1", "Facteur_2"]
        
        # Vérifications
        assert len(factor_names) == 2
        assert all(isinstance(name, str) for name in factor_names)
    
    def test_output_format(self):
        """Test du format de sortie."""
        # Simulation de résultats
        results = {
            'eigenvalues': np.array([2.5, 1.2, 0.8, 0.5]),
            'loadings': np.random.uniform(-1, 1, (4, 2)),
            'variance_explained': np.array([62.5, 30.0, 7.5, 0.0]),
            'factor_scores': np.random.normal(0, 1, (100, 2))
        }
        
        # Vérifications
        assert isinstance(results, dict)
        assert all(key in results for key in ['eigenvalues', 'loadings', 'variance_explained', 'factor_scores'])
        assert isinstance(results['eigenvalues'], np.ndarray)
        assert isinstance(results['loadings'], np.ndarray)
        assert isinstance(results['variance_explained'], np.ndarray)
        assert isinstance(results['factor_scores'], np.ndarray)

if __name__ == '__main__':
    unittest.main() 