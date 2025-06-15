import unittest
import numpy as np
import pandas as pd
from py_stats_toolkit.stats.temporelle.TimeSeriesModule import TimeSeriesAnalyzer

class TestTimeSeries(unittest.TestCase):
    def setUp(self):
        self.analyzer = TimeSeriesAnalyzer()
        
        # Données de test avec tendance
        dates = pd.date_range(start='2020-01-01', periods=100, freq='D')
        trend = np.linspace(0, 10, 100)
        noise = np.random.normal(0, 1, 100)
        self.trend_data = pd.Series(trend + noise, index=dates)
        
        # Données de test avec saisonnalité
        t = np.arange(100)
        seasonal = 5 * np.sin(2 * np.pi * t / 12)  # Saisonnalité annuelle
        self.seasonal_data = pd.Series(seasonal + noise, index=dates)
        
        # Données de test avec tendance et saisonnalité
        self.complex_data = pd.Series(trend + seasonal + noise, index=dates)
    
    def test_process(self):
        """Test du traitement des données."""
        result = self.analyzer.process(self.complex_data)
        
        self.assertIsInstance(result, pd.Series)
        self.assertIn('Moyenne', result)
        self.assertIn('Écart-type', result)
        self.assertIn('Tendance', result)
        self.assertIn('Saisonnalité', result)
    
    def test_basic_stats(self):
        """Test des statistiques de base."""
        result = self.analyzer.process(self.complex_data)
        stats = self.analyzer.get_basic_stats()
        
        self.assertIsInstance(stats, dict)
        self.assertIn('Moyenne', stats)
        self.assertIn('Écart-type', stats)
        self.assertIn('Minimum', stats)
        self.assertIn('Maximum', stats)
        self.assertIn('Médiane', stats)
    
    def test_trend_analysis(self):
        """Test de l'analyse de tendance."""
        result = self.analyzer.process(self.trend_data)
        trend_info = self.analyzer.get_trend_info()
        
        self.assertIsInstance(trend_info, dict)
        self.assertIn('Type', trend_info)
        self.assertIn('Pente', trend_info)
        self.assertIn('R2', trend_info)
    
    def test_seasonality_analysis(self):
        """Test de l'analyse de saisonnalité."""
        result = self.analyzer.process(self.seasonal_data)
        seasonality_info = self.analyzer.get_seasonality_info()
        
        self.assertIsInstance(seasonality_info, dict)
        self.assertIn('Période', seasonality_info)
        self.assertIn('Amplitude', seasonality_info)
        self.assertIn('Phase', seasonality_info)
    
    def test_forecast(self):
        """Test des prévisions."""
        result = self.analyzer.process(self.complex_data)
        forecast = self.analyzer.forecast(steps=10)
        
        self.assertIsInstance(forecast, pd.Series)
        self.assertEqual(len(forecast), 10)
    
    def test_decomposition(self):
        """Test de la décomposition."""
        result = self.analyzer.process(self.complex_data)
        decomposition = self.analyzer.decompose()
        
        self.assertIsInstance(decomposition, dict)
        self.assertIn('Tendance', decomposition)
        self.assertIn('Saisonnalité', decomposition)
        self.assertIn('Résidus', decomposition)
    
    def test_stationarity_test(self):
        """Test de la stationnarité."""
        result = self.analyzer.process(self.complex_data)
        stationarity = self.analyzer.test_stationarity()
        
        self.assertIsInstance(stationarity, dict)
        self.assertIn('Test de Dickey-Fuller', stationarity)
        self.assertIn('p-valeur', stationarity)
        self.assertIn('Stationnaire', stationarity)
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.analyzer.process("invalid_data")
    
    def test_non_time_index(self):
        """Test avec un index non temporel."""
        data = pd.Series(np.random.normal(0, 1, 100))
        with self.assertRaises(ValueError):
            self.analyzer.process(data)
    
    def test_empty_data(self):
        """Test avec des données vides."""
        empty_data = pd.Series([], index=pd.DatetimeIndex([]))
        with self.assertRaises(ValueError):
            self.analyzer.process(empty_data)
    
    def test_get_autocorrelation(self):
        """Test de l'autocorrélation."""
        result = self.analyzer.process(self.complex_data)
        acf = self.analyzer.get_autocorrelation()
        
        self.assertIsInstance(acf, pd.Series)
        self.assertTrue(all(abs(x) <= 1 for x in acf))
    
    def test_get_partial_autocorrelation(self):
        """Test de l'autocorrélation partielle."""
        result = self.analyzer.process(self.complex_data)
        pacf = self.analyzer.get_partial_autocorrelation()
        
        self.assertIsInstance(pacf, pd.Series)
        self.assertTrue(all(abs(x) <= 1 for x in pacf))

if __name__ == '__main__':
    unittest.main() 