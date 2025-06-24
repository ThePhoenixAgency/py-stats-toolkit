"""
Tests pour le module TemporalValidationEngine
============================================

Tests unitaires pour la validation temporelle avec polymorphisme.
"""

import unittest
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import sys
import os

# Ajouter le répertoire parent au path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from py_stats_toolkit import TemporalValidationEngine

class TestTemporalValidationEngine(unittest.TestCase):
    """Tests pour TemporalValidationEngine"""
    
    def setUp(self):
        """Initialisation avant chaque test"""
        self.engine = TemporalValidationEngine()
        
        # Données de test temporelles
        self.time_series_data = [100, 105, 110, 108, 115, 120, 118, 125, 130, 128]
        self.time_series_series = pd.Series([100, 105, 110, 108, 115, 120, 118, 125, 130, 128])
        self.time_series_array = np.array([100, 105, 110, 108, 115, 120, 118, 125, 130, 128])
        
        # Dates de test
        self.dates = [
            "2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05",
            "2025-01-06", "2025-01-07", "2025-01-08", "2025-01-09", "2025-01-10"
        ]
        
        # Données historiques
        self.historical_data = [
            [95, 100, 105, 102, 110],
            [98, 103, 108, 105, 112],
            [101, 106, 111, 108, 115]
        ]
        
        # Données avec tendance
        self.trend_data = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
        
        # Données avec saisonnalité
        self.seasonal_data = [10, 15, 20, 15, 10, 15, 20, 15, 10, 15]
    
    def test_polymorphism_list(self):
        """Test du polymorphisme avec liste Python"""
        results = self.engine.comprehensive_temporal_validation(
            self.time_series_data,
            dates=self.dates
        )
        
        self.assertIsInstance(results, dict)
        self.assertIn('temporal_consistency', results)
        self.assertIn('cycle_analysis', results)
        self.assertIn('trend_analysis', results)
        self.assertIn('seasonality_analysis', results)
        self.assertIn('anomaly_detection', results)
        self.assertIn('forecast_validation', results)
        self.assertIn('global_temporal_score', results)
        self.assertIn('recommendations', results)
    
    def test_polymorphism_series(self):
        """Test du polymorphisme avec Series pandas"""
        results = self.engine.comprehensive_temporal_validation(
            self.time_series_series,
            dates=self.dates
        )
        
        self.assertIsInstance(results, dict)
        self.assertIn('global_temporal_score', results)
    
    def test_polymorphism_array(self):
        """Test du polymorphisme avec array numpy"""
        results = self.engine.comprehensive_temporal_validation(
            self.time_series_array,
            dates=self.dates
        )
        
        self.assertIsInstance(results, dict)
        self.assertIn('global_temporal_score', results)
    
    def test_consistency_across_types(self):
        """Test de la cohérence des résultats entre types de données"""
        results_list = self.engine.comprehensive_temporal_validation(
            self.time_series_data,
            dates=self.dates
        )
        
        results_series = self.engine.comprehensive_temporal_validation(
            self.time_series_series,
            dates=self.dates
        )
        
        # Les scores temporels doivent être cohérents
        self.assertAlmostEqual(
            results_list['global_temporal_score'], 
            results_series['global_temporal_score'], 
            delta=0.1
        )
    
    def test_temporal_consistency(self):
        """Test de la cohérence temporelle"""
        results = self.engine.comprehensive_temporal_validation(
            self.time_series_data,
            dates=self.dates
        )
        
        consistency = results['temporal_consistency']
        
        self.assertIsInstance(consistency, dict)
        self.assertIn('is_consistent', consistency)
        self.assertIn('consistency_score', consistency)
        self.assertIn('inconsistencies', consistency)
        self.assertIn('details', consistency)
        
        self.assertIsInstance(consistency['is_consistent'], bool)
        self.assertGreaterEqual(consistency['consistency_score'], 0.0)
        self.assertLessEqual(consistency['consistency_score'], 1.0 + 1e-10)
    
    def test_cycle_analysis(self):
        """Test de l'analyse des cycles"""
        results = self.engine.comprehensive_temporal_validation(
            self.time_series_data,
            dates=self.dates
        )
        
        cycle_analysis = results['cycle_analysis']
        
        self.assertIsInstance(cycle_analysis, dict)
        self.assertIn('has_cycles', cycle_analysis)
        self.assertIn('cycle_periods', cycle_analysis)
        self.assertIn('cycle_strength', cycle_analysis)
        self.assertIn('details', cycle_analysis)
        
        self.assertIsInstance(cycle_analysis['has_cycles'], bool)
        self.assertIsInstance(cycle_analysis['cycle_periods'], list)
        self.assertGreaterEqual(cycle_analysis['cycle_strength'], 0.0)
        self.assertLessEqual(cycle_analysis['cycle_strength'], 1.0 + 1e-10)
    
    def test_trend_analysis(self):
        """Test de l'analyse des tendances"""
        results = self.engine.comprehensive_temporal_validation(
            self.trend_data,
            dates=self.dates
        )
        
        trend_analysis = results['trend_analysis']
        
        self.assertIsInstance(trend_analysis, dict)
        self.assertIn('has_trend', trend_analysis)
        self.assertIn('trend_direction', trend_analysis)
        self.assertIn('trend_strength', trend_analysis)
        self.assertIn('trend_slope', trend_analysis)
        self.assertIn('details', trend_analysis)
        
        self.assertIsInstance(trend_analysis['has_trend'], bool)
        self.assertIn(trend_analysis['trend_direction'], ['increasing', 'decreasing', 'stable'])
        self.assertGreaterEqual(trend_analysis['trend_strength'], 0.0)
        self.assertLessEqual(trend_analysis['trend_strength'], 1.0 + 1e-10)
    
    def test_seasonality_analysis(self):
        """Test de l'analyse de saisonnalité"""
        results = self.engine.comprehensive_temporal_validation(
            self.seasonal_data,
            dates=self.dates
        )
        
        seasonality_analysis = results['seasonality_analysis']
        
        self.assertIsInstance(seasonality_analysis, dict)
        self.assertIn('has_seasonality', seasonality_analysis)
        self.assertIn('seasonal_period', seasonality_analysis)
        self.assertIn('seasonal_strength', seasonality_analysis)
        self.assertIn('details', seasonality_analysis)
        
        self.assertIsInstance(seasonality_analysis['has_seasonality'], bool)
        self.assertGreaterEqual(seasonality_analysis['seasonal_strength'], 0.0)
        self.assertLessEqual(seasonality_analysis['seasonal_strength'], 1.0 + 1e-10)
    
    def test_anomaly_detection(self):
        """Test de la détection d'anomalies temporelles"""
        # Créer des données avec une anomalie
        anomalous_data = self.time_series_data.copy()
        anomalous_data[5] = 999  # Anomalie évidente
        
        results = self.engine.comprehensive_temporal_validation(
            anomalous_data,
            dates=self.dates
        )
        
        anomaly_detection = results['anomaly_detection']
        
        self.assertIsInstance(anomaly_detection, dict)
        self.assertIn('has_anomalies', anomaly_detection)
        self.assertIn('anomaly_positions', anomaly_detection)
        self.assertIn('anomaly_scores', anomaly_detection)
        self.assertIn('details', anomaly_detection)
        
        self.assertIsInstance(anomaly_detection['has_anomalies'], bool)
        self.assertIsInstance(anomaly_detection['anomaly_positions'], list)
        self.assertIsInstance(anomaly_detection['anomaly_scores'], list)
    
    def test_forecast_validation(self):
        """Test de la validation des prévisions"""
        results = self.engine.comprehensive_temporal_validation(
            self.time_series_data,
            dates=self.dates,
            historical_data=self.historical_data
        )
        
        forecast_validation = results['forecast_validation']
        
        self.assertIsInstance(forecast_validation, dict)
        self.assertIn('forecast_accuracy', forecast_validation)
        self.assertIn('prediction_intervals', forecast_validation)
        self.assertIn('forecast_errors', forecast_validation)
        self.assertIn('details', forecast_validation)
        
        self.assertGreaterEqual(forecast_validation['forecast_accuracy'], 0.0)
        self.assertLessEqual(forecast_validation['forecast_accuracy'], 1.0 + 1e-10)
    
    def test_global_temporal_score(self):
        """Test du score temporel global"""
        results = self.engine.comprehensive_temporal_validation(
            self.time_series_data,
            dates=self.dates
        )
        
        global_score = results['global_temporal_score']
        
        self.assertIsInstance(global_score, float)
        self.assertGreaterEqual(global_score, 0.0)
        self.assertLessEqual(global_score, 1.0 + 1e-10)
    
    def test_recommendations(self):
        """Test des recommandations temporelles"""
        results = self.engine.comprehensive_temporal_validation(
            self.time_series_data,
            dates=self.dates
        )
        
        recommendations = results['recommendations']
        
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)
        
        for rec in recommendations:
            self.assertIsInstance(rec, str)
            self.assertGreater(len(rec), 0)
    
    def test_process_method(self):
        """Test de la méthode process avec polymorphisme"""
        # Test avec liste
        results_list = self.engine.process(self.time_series_data)
        self.assertIsInstance(results_list, dict)
        
        # Test avec Series
        results_series = self.engine.process(self.time_series_series)
        self.assertIsInstance(results_series, dict)
        
        # Test avec array
        results_array = self.engine.process(self.time_series_array)
        self.assertIsInstance(results_array, dict)
    
    def test_configure_method(self):
        """Test de la méthode configure"""
        original_params = self.engine.get_parameters().copy()
        
        # Configurer de nouveaux paramètres
        self.engine.configure(test_param="test_value", another_param=42)
        
        new_params = self.engine.get_parameters()
        
        # Vérifier que les nouveaux paramètres sont ajoutés
        self.assertIn('test_param', new_params)
        self.assertIn('another_param', new_params)
        self.assertEqual(new_params['test_param'], "test_value")
        self.assertEqual(new_params['another_param'], 42)
        
        # Vérifier que les paramètres originaux sont préservés
        for key, value in original_params.items():
            self.assertIn(key, new_params)
            self.assertEqual(new_params[key], value)
    
    def test_temporal_patterns(self):
        """Test de la détection de patterns temporels"""
        patterns = self.engine.detect_temporal_patterns(
            self.time_series_data,
            dates=self.dates
        )
        
        self.assertIsInstance(patterns, dict)
        self.assertIn('patterns', patterns)
        self.assertIn('pattern_scores', patterns)
        self.assertIn('details', patterns)
        
        self.assertIsInstance(patterns['patterns'], list)
        self.assertIsInstance(patterns['pattern_scores'], dict)
    
    def test_edge_cases(self):
        """Test des cas limites"""
        # Liste vide
        empty_results = self.engine.comprehensive_temporal_validation([], dates=[])
        self.assertIsInstance(empty_results, dict)
        
        # Liste avec un seul élément
        single_results = self.engine.comprehensive_temporal_validation([42], dates=["2025-01-01"])
        self.assertIsInstance(single_results, dict)
        
        # Données avec valeurs identiques
        identical_data = [100, 100, 100, 100, 100]
        identical_dates = ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"]
        identical_results = self.engine.comprehensive_temporal_validation(identical_data, dates=identical_dates)
        self.assertIsInstance(identical_results, dict)
    
    def test_date_validation(self):
        """Test de la validation des dates"""
        # Dates invalides
        invalid_dates = ["invalid", "date", "format", "here", "now"]
        
        results = self.engine.comprehensive_temporal_validation(
            self.time_series_data,
            dates=invalid_dates
        )
        
        # Le moteur doit gérer les dates invalides gracieusement
        self.assertIsInstance(results, dict)
        self.assertIn('global_temporal_score', results)

if __name__ == '__main__':
    unittest.main() 