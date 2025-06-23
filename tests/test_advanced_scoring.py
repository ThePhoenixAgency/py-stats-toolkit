"""
Tests pour le module AdvancedScoringEngine
=========================================

Tests unitaires pour le scoring avancé avec polymorphisme.
"""

import unittest
import numpy as np
import pandas as pd
from datetime import datetime
import sys
import os

# Ajouter le répertoire parent au path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from py_stats_toolkit import AdvancedScoringEngine

class TestAdvancedScoringEngine(unittest.TestCase):
    """Tests pour AdvancedScoringEngine"""
    
    def setUp(self):
        """Initialisation avant chaque test"""
        self.engine = AdvancedScoringEngine()
        
        # Données de test
        self.sample_data = [15, 23, 8, 42, 19, 31, 7, 28, 45, 12]
        self.sample_data_series = pd.Series([15, 23, 8, 42, 19, 31, 7, 28, 45, 12])
        self.sample_data_array = np.array([15, 23, 8, 42, 19, 31, 7, 28, 45, 12])
        
        # Données historiques
        self.historical_data = [
            [10, 20, 30, 40, 50],
            [5, 15, 25, 35, 45],
            [12, 22, 32, 42, 52]
        ]
        
        # Données de référence
        self.reference_data = [20, 25, 15, 35, 22, 30, 10, 25, 40, 18]
    
    def test_polymorphism_list(self):
        """Test du polymorphisme avec liste Python"""
        scores = self.engine.get_comprehensive_scores(self.sample_data)
        
        self.assertIsInstance(scores, dict)
        self.assertIn('variance_score', scores)
        self.assertIn('coherence_score', scores)
        self.assertIn('fractal_score', scores)
        self.assertIn('entropy_score', scores)
        self.assertIn('lunar_cycle_score', scores)
        self.assertIn('correlation_score', scores)
        self.assertIn('anova_score', scores)
        self.assertIn('global_score', scores)
        
        # Vérifier que les scores sont entre 0 et 1 (avec tolérance pour erreurs d'arrondi)
        tolerance = 1e-10
        for score_name, score_value in scores.items():
            if score_name != 'global_score':  # global_score peut être calculé différemment
                self.assertGreaterEqual(score_value, 0.0)
                self.assertLessEqual(score_value, 1.0 + tolerance)
    
    def test_polymorphism_series(self):
        """Test du polymorphisme avec Series pandas"""
        scores = self.engine.get_comprehensive_scores(self.sample_data_series)
        
        self.assertIsInstance(scores, dict)
        self.assertIn('variance_score', scores)
        self.assertIn('coherence_score', scores)
        self.assertIn('fractal_score', scores)
        self.assertIn('entropy_score', scores)
        self.assertIn('lunar_cycle_score', scores)
        self.assertIn('correlation_score', scores)
        self.assertIn('anova_score', scores)
        self.assertIn('global_score', scores)
    
    def test_polymorphism_array(self):
        """Test du polymorphisme avec array numpy"""
        scores = self.engine.get_comprehensive_scores(self.sample_data_array)
        
        self.assertIsInstance(scores, dict)
        self.assertIn('variance_score', scores)
        self.assertIn('coherence_score', scores)
        self.assertIn('fractal_score', scores)
        self.assertIn('entropy_score', scores)
        self.assertIn('lunar_cycle_score', scores)
        self.assertIn('correlation_score', scores)
        self.assertIn('anova_score', scores)
        self.assertIn('global_score', scores)
    
    def test_consistency_across_types(self):
        """Test de la cohérence des résultats entre types de données"""
        scores_list = self.engine.get_comprehensive_scores(self.sample_data)
        scores_series = self.engine.get_comprehensive_scores(self.sample_data_series)
        scores_array = self.engine.get_comprehensive_scores(self.sample_data_array)
        
        # Les scores doivent être cohérents (à une tolérance près)
        tolerance = 1e-10
        
        for score_name in ['variance_score', 'coherence_score', 'fractal_score', 'entropy_score']:
            self.assertAlmostEqual(
                scores_list[score_name], 
                scores_series[score_name], 
                delta=tolerance
            )
            self.assertAlmostEqual(
                scores_series[score_name], 
                scores_array[score_name], 
                delta=tolerance
            )
    
    def test_variance_score(self):
        """Test du score de variance"""
        variance_score = self.engine.variance_score(self.sample_data)
        
        self.assertIsInstance(variance_score, float)
        self.assertGreaterEqual(variance_score, 0.0)
        self.assertLessEqual(variance_score, 1.0 + 1e-10)
    
    def test_coherence_score(self):
        """Test du score de cohérence"""
        coherence_score = self.engine.coherence_score(self.sample_data)
        
        self.assertIsInstance(coherence_score, float)
        self.assertGreaterEqual(coherence_score, 0.0)
        self.assertLessEqual(coherence_score, 1.0 + 1e-10)
    
    def test_fractal_score(self):
        """Test du score fractal"""
        fractal_score = self.engine.fractal_score(self.sample_data)
        
        self.assertIsInstance(fractal_score, float)
        self.assertGreaterEqual(fractal_score, 0.0)
        self.assertLessEqual(fractal_score, 1.0 + 1e-10)
    
    def test_entropy_score(self):
        """Test du score d'entropie"""
        entropy_score = self.engine.entropy_score(self.sample_data)
        
        self.assertIsInstance(entropy_score, float)
        self.assertGreaterEqual(entropy_score, 0.0)
        self.assertLessEqual(entropy_score, 1.0 + 1e-10)
    
    def test_lunar_cycle_score(self):
        """Test du score de cycle lunaire"""
        date = "2025-01-15"
        lunar_score = self.engine.lunar_cycle_score(date, self.sample_data)
        
        self.assertIsInstance(lunar_score, float)
        self.assertGreaterEqual(lunar_score, 0.0)
        self.assertLessEqual(lunar_score, 1.0 + 1e-10)
    
    def test_correlation_score(self):
        """Test du score de corrélation"""
        correlation_score = self.engine.correlation_score(
            self.sample_data, 
            self.historical_data
        )
        
        self.assertIsInstance(correlation_score, float)
        self.assertGreaterEqual(correlation_score, 0.0)
        self.assertLessEqual(correlation_score, 1.0 + 1e-10)
    
    def test_anova_score(self):
        """Test du score ANOVA"""
        anova_score = self.engine.anova_score(
            self.sample_data, 
            self.historical_data
        )
        
        self.assertIsInstance(anova_score, float)
        self.assertGreaterEqual(anova_score, 0.0)
        self.assertLessEqual(anova_score, 1.0 + 1e-10)
    
    def test_equiprobability_test(self):
        """Test du test d'équiprobabilité"""
        result = self.engine.equiprobability_test(self.sample_data)
        
        self.assertIsInstance(result, dict)
        self.assertIn('is_equiprobable', result)
        self.assertIn('confidence', result)
        self.assertIn('p_value', result)
        self.assertIn('chi2_statistic', result)
        self.assertIn('details', result)
        
        self.assertIsInstance(result['is_equiprobable'], bool)
        self.assertGreaterEqual(result['confidence'], 0.0)
        self.assertLessEqual(result['confidence'], 1.0 + 1e-10)
    
    def test_global_score(self):
        """Test du score global"""
        global_score = self.engine.global_score(
            self.sample_data,
            date="2025-01-15",
            historical_data=self.historical_data
        )
        
        self.assertIsInstance(global_score, float)
        self.assertGreaterEqual(global_score, 0.0)
        self.assertLessEqual(global_score, 1.0 + 1e-10)
    
    def test_relative_scoring(self):
        """Test du scoring relatif"""
        relative_scores = self.engine.get_relative_scores(
            self.sample_data,
            self.reference_data
        )
        
        self.assertIsInstance(relative_scores, dict)
        self.assertIn('relative_variance', relative_scores)
        self.assertIn('relative_coherence', relative_scores)
        self.assertIn('relative_fractal', relative_scores)
        self.assertIn('relative_entropy', relative_scores)
        self.assertIn('overall_relative_score', relative_scores)
        
        # Vérifier que les scores relatifs sont des nombres
        for score_name, score_value in relative_scores.items():
            self.assertIsInstance(score_value, (int, float))
    
    def test_weighted_scoring(self):
        """Test du scoring pondéré"""
        weights = {
            'variance': 0.3,
            'coherence': 0.2,
            'fractal': 0.2,
            'entropy': 0.15,
            'lunar': 0.15
        }
        
        weighted_score = self.engine.get_weighted_score(
            self.sample_data,
            weights=weights,
            date="2025-01-15"
        )
        
        self.assertIsInstance(weighted_score, float)
        self.assertGreaterEqual(weighted_score, 0.0)
        self.assertLessEqual(weighted_score, 1.0 + 1e-10)
    
    def test_process_method(self):
        """Test de la méthode process avec polymorphisme"""
        # Test avec liste
        results_list = self.engine.process(self.sample_data)
        self.assertIsInstance(results_list, dict)
        
        # Test avec Series
        results_series = self.engine.process(self.sample_data_series)
        self.assertIsInstance(results_series, dict)
        
        # Test avec array
        results_array = self.engine.process(self.sample_data_array)
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
    
    def test_inheritance(self):
        """Test de l'héritage de StatisticalModule"""
        from py_stats_toolkit import StatisticalModule
        
        self.assertIsInstance(self.engine, StatisticalModule)
        self.assertTrue(hasattr(self.engine, 'configure'))
        self.assertTrue(hasattr(self.engine, 'process'))
        self.assertTrue(hasattr(self.engine, 'get_parameters'))
        self.assertTrue(hasattr(self.engine, 'get_results'))
    
    def test_score_interpretation(self):
        """Test de l'interprétation des scores"""
        interpretation = self.engine.interpret_scores(self.sample_data)
        
        self.assertIsInstance(interpretation, dict)
        self.assertIn('overall_assessment', interpretation)
        self.assertIn('strengths', interpretation)
        self.assertIn('weaknesses', interpretation)
        self.assertIn('recommendations', interpretation)
        
        self.assertIsInstance(interpretation['overall_assessment'], str)
        self.assertIsInstance(interpretation['strengths'], list)
        self.assertIsInstance(interpretation['weaknesses'], list)
        self.assertIsInstance(interpretation['recommendations'], list)
    
    def test_edge_cases(self):
        """Test des cas limites"""
        # Liste vide
        empty_scores = self.engine.get_comprehensive_scores([])
        self.assertIsInstance(empty_scores, dict)
        
        # Liste avec un seul élément
        single_scores = self.engine.get_comprehensive_scores([42])
        self.assertIsInstance(single_scores, dict)
        
        # Liste avec des valeurs identiques
        identical_scores = self.engine.get_comprehensive_scores([1, 1, 1, 1, 1])
        self.assertIsInstance(identical_scores, dict)
    
    def test_score_comparison(self):
        """Test de la comparaison de scores"""
        scores1 = self.engine.get_comprehensive_scores(self.sample_data)
        scores2 = self.engine.get_comprehensive_scores(self.reference_data)
        
        comparison = self.engine.compare_scores(scores1, scores2)
        
        self.assertIsInstance(comparison, dict)
        self.assertIn('better_dataset', comparison)
        self.assertIn('score_differences', comparison)
        self.assertIn('analysis', comparison)
        
        self.assertIsInstance(comparison['better_dataset'], str)
        self.assertIsInstance(comparison['score_differences'], dict)
        self.assertIsInstance(comparison['analysis'], str)

if __name__ == '__main__':
    unittest.main() 