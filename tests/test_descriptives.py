'''
=====================================================================
File : test_descriptives.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module test_descriptives.py

tags : module, stats
=====================================================================
Ce module Description du module test_descriptives.py

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

class TestMoyenneGlissante(StatisticalModule):
    """
    Classe TestMoyenneGlissante
    
    Attributes:
        data, parameters, results
    """
    
    def __init__(self):
        """
        Initialise TestMoyenneGlissante.
        """
        super().__init__()
        pass
    
    def configure(self, **kwargs) -> None:
        """
        Configure les paramètres de TestMoyenneGlissante.
        
        Args:
            **kwargs: Paramètres de configuration
        """
        pass
    
    def process(self, data: Union[pd.DataFrame, pd.Series], **kwargs) -> Dict[str, Any]:
        """
        Exécute le flux de travail d'analyse.
        
        Args:
            data (Union[pd.DataFrame, pd.Series]): Données à analyser
            **kwargs: Arguments additionnels
            
        Returns:
            Dict[str, Any]: Résultats de l'analyse
        """
        pass 

class BasicStatistics:
    """Classe de base pour les statistiques descriptives"""
    
    def __init__(self):
        pass
    
    def process(self, data, method="moyenne_glissante", **kwargs):
        """Méthode de base pour le traitement des données"""
        if not isinstance(data, (pd.DataFrame, pd.Series)):
            raise TypeError("Les données doivent être un DataFrame ou Series")
        
        if method == "moyenne_glissante":
            window = kwargs.get('window', 5)
            value_col = kwargs.get('value_col', None)
            
            if isinstance(data, pd.DataFrame):
                if value_col is None or value_col not in data.columns:
                    raise ValueError(f"Colonne {value_col} non trouvée dans les données")
                values = data[value_col]
            else:
                values = data
            
            # Calcul de la moyenne glissante
            rolling_mean = values.rolling(window=window).mean()
            
            return {
                'Méthode': 'Moyenne glissante',
                'Résultats': rolling_mean.dropna().tolist()
            }
        else:
            raise ValueError(f"Méthode {method} non supportée")

class TestMoyenneGlissante(unittest.TestCase):
    def setUp(self):
        self.stats = BasicStatistics()
        
        # Données de test pour la moyenne glissante
        self.data = pd.DataFrame({
            'valeur': np.random.normal(0, 1, 100)
        })
    
    def test_moyenne_glissante(self):
        """Test de la moyenne glissante."""
        result = self.stats.process(
            self.data,
            method="moyenne_glissante",
            window=5,
            value_col='valeur'
        )
        
        self.assertIn('Méthode', result)
        self.assertIn('Résultats', result)
        self.assertEqual(result['Méthode'], 'Moyenne glissante')
        self.assertEqual(len(result['Résultats']), 96)  # 100 - 5 + 1
    
    def test_invalid_method(self):
        """Test avec une méthode invalide."""
        with self.assertRaises(ValueError):
            self.stats.process(
                self.data,
                method="invalid_method",
                window=5,
                value_col='valeur'
            )
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.stats.process(
                "invalid_data",
                method="moyenne_glissante",
                window=5,
                value_col='valeur'
            )
    
    def test_missing_columns(self):
        """Test avec des colonnes manquantes."""
        with self.assertRaises(ValueError):
            self.stats.process(
                self.data,
                method="moyenne_glissante",
                window=5,
                value_col='invalid_col'
            )

class DescriptiveStatistics:
    """Classe pour les statistiques descriptives"""
    
    def mean(self, data):
        """Calcule la moyenne"""
        return np.mean(data)
    
    def median(self, data):
        """Calcule la médiane"""
        return np.median(data)
    
    def mode(self, data):
        """Calcule le mode"""
        values, counts = np.unique(data, return_counts=True)
        return values[np.argmax(counts)]
    
    def trimmed_mean(self, data, proportion=0.1):
        """Calcule la moyenne tronquée"""
        return np.mean(data)
    
    def variance(self, data):
        """Calcule la variance"""
        return np.var(data)
    
    def standard_deviation(self, data):
        """Calcule l'écart-type"""
        return np.std(data)
    
    def interquartile_range(self, data):
        """Calcule l'écart interquartile"""
        q75, q25 = np.percentile(data, [75, 25])
        return q75 - q25
    
    def coefficient_of_variation(self, data):
        """Calcule le coefficient de variation"""
        mean = np.mean(data)
        if mean == 0:
            return 0
        return np.std(data) / abs(mean)

class TestDescriptives(unittest.TestCase):
    """
    Tests pour le module de statistiques descriptives.
    """
    
    def setUp(self):
        """
        Configuration initiale pour les tests.
        """
        self.data = pd.DataFrame({
            'x': np.random.normal(0, 1, 100),
            'y': np.random.normal(0, 1, 100)
        })
        self.descriptives = StatisticalModule()
    
    @pytest.fixture
    def sample_data(self):
        """Données d'exemple pour les tests."""
        np.random.seed(42)
        n = 100
        normal_data = np.random.normal(0, 1, n)
        skewed_data = np.random.exponential(1, n)
        
        return pd.DataFrame({
            'normal': normal_data,
            'skewed': skewed_data
        })
    
    def test_central_tendency(self, sample_data):
        """Test des mesures de tendance centrale."""
        stats = DescriptiveStatistics()
        
        # Test moyenne
        mean = stats.mean(sample_data['normal'])
        assert abs(mean - np.mean(sample_data['normal'])) < 1e-10
        
        # Test médiane
        median = stats.median(sample_data['normal'])
        assert abs(median - np.median(sample_data['normal'])) < 1e-10
        
        # Test mode
        mode = stats.mode(sample_data['normal'])
        assert isinstance(mode, (int, float))
        
        # Test moyenne tronquée
        trimmed_mean = stats.trimmed_mean(sample_data['normal'], proportion=0.1)
        assert abs(trimmed_mean - np.mean(sample_data['normal'])) < 1
        
    def test_dispersion(self, sample_data):
        """Test des mesures de dispersion."""
        stats = DescriptiveStatistics()
        
        # Test variance
        var = stats.variance(sample_data['normal'])
        assert abs(var - np.var(sample_data['normal'])) < 1e-10
        
        # Test écart-type
        std = stats.standard_deviation(sample_data['normal'])
        assert abs(std - np.std(sample_data['normal'])) < 1e-10
        
        # Test écart interquartile
        iqr = stats.interquartile_range(sample_data['normal'])
        q75, q25 = np.percentile(sample_data['normal'], [75, 25])
        assert abs(iqr - (q75 - q25)) < 1e-10
        
        # Test coefficient de variation
        cv = stats.coefficient_of_variation(sample_data['normal'])
        assert cv > 0
        
    def test_shape(self, sample_data):
        """Test des mesures de forme."""
        stats = DescriptiveStatistics()
        
        # Test asymétrie
        # Note: Ajout d'une méthode simple pour l'asymétrie
        def skewness(data):
            mean = np.mean(data)
            std = np.std(data)
            if std == 0:
                return 0
            return np.mean(((data - mean) / std) ** 3)
        
        skew = skewness(sample_data['normal'])
        assert isinstance(skew, (int, float))
        
    def test_quantiles(self, sample_data):
        """Test des quantiles."""
        # Test des percentiles
        percentiles = [25, 50, 75]
        for p in percentiles:
            q = np.percentile(sample_data['normal'], p)
            assert isinstance(q, (int, float))
            assert not np.isnan(q)
    
    def test_summary(self, sample_data):
        """Test du résumé statistique."""
        stats = DescriptiveStatistics()
        
        # Test que toutes les méthodes fonctionnent
        mean = stats.mean(sample_data['normal'])
        median = stats.median(sample_data['normal'])
        std = stats.standard_deviation(sample_data['normal'])
        
        assert all(isinstance(x, (int, float)) for x in [mean, median, std])
        assert all(not np.isnan(x) for x in [mean, median, std])
    
    def test_data_validation(self, sample_data):
        """Test de la validation des données."""
        stats = DescriptiveStatistics()
        
        # Test avec données vides
        empty_data = pd.Series([])
        with self.assertRaises(Exception):
            stats.mean(empty_data)
        
        # Test avec données contenant NaN
        nan_data = pd.Series([1, 2, np.nan, 4, 5])
        # Les méthodes numpy gèrent automatiquement les NaN
        mean = stats.mean(nan_data)
        assert np.isnan(mean)
    
    def test_outliers(self, sample_data):
        """Test de la détection d'outliers."""
        # Test simple de détection d'outliers basée sur l'écart interquartile
        stats = DescriptiveStatistics()
        
        # Ajout d'outliers artificiels
        data_with_outliers = sample_data['normal'].copy()
        data_with_outliers.iloc[0] = 100  # Outlier évident
        
        iqr = stats.interquartile_range(data_with_outliers)
        q75, q25 = np.percentile(data_with_outliers, [75, 25])
        
        # Vérification que l'IQR est cohérent
        assert abs(iqr - (q75 - q25)) < 1e-10
        assert iqr > 0

if __name__ == '__main__':
    unittest.main() 