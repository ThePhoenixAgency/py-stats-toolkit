#!/usr/bin/env python3
"""
Tests pour les fonctionnalités d'historique de Py_Stats_Toolkit
"""

import unittest
import tempfile
import os
import json
import numpy as np
import pandas as pd
from py_stats_toolkit.stats.descriptives.basic_stats import BasicStatistics
from py_stats_toolkit.stats.correlation.correlation import Correlation
from py_stats_toolkit.stats.regression.regression import Regression
from py_stats_toolkit.visualization.basic_plots import BasicPlots
from py_stats_toolkit.utils.data_processor import DataProcessor
from py_stats_toolkit.utils.data_validator import DataValidator

class TestHistoryFunctionality(unittest.TestCase):
    """Tests pour les fonctionnalités d'historique"""
    
    def setUp(self):
        """Configuration initiale pour les tests"""
        # Créer un dossier temporaire pour les fichiers d'historique
        self.temp_dir = tempfile.mkdtemp()
        
        # Données de test
        np.random.seed(42)
        self.test_data = pd.DataFrame({
            'x': np.random.normal(0, 1, 50),
            'y': np.random.normal(0, 1, 50),
            'z': np.random.normal(0, 1, 50)
        })
    
    def tearDown(self):
        """Nettoyage après les tests"""
        # Supprimer les fichiers temporaires de manière récursive
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_basic_statistics_history(self):
        """Test de l'historique des statistiques de base"""
        history_file = os.path.join(self.temp_dir, "test_stats_history.json")
        stats = BasicStatistics(history_file=history_file)
        
        # Effectuer plusieurs analyses
        for i in range(3):
            stats.process(self.test_data, analysis_type=f"test_{i}")
        
        # Vérifier que le fichier d'historique existe
        self.assertTrue(os.path.exists(history_file))
        
        # Vérifier le contenu de l'historique
        with open(history_file, 'r') as f:
            history = json.load(f)
        
        self.assertEqual(len(history), 3)
        self.assertEqual(history[0]['module_type'], 'basic_statistics')
        self.assertEqual(history[0]['data_points'], 50)
        
        # Vérifier les méthodes d'analyse
        history_stats = stats.get_statistics_history()
        self.assertEqual(history_stats['total_analyses'], 3)
        self.assertEqual(history_stats['average_data_points'], 50.0)
        self.assertIsNotNone(history_stats['last_analysis'])
    
    def test_correlation_history(self):
        """Test de l'historique des corrélations"""
        history_file = os.path.join(self.temp_dir, "test_corr_history.json")
        corr = Correlation(history_file=history_file)
        
        # Effectuer plusieurs corrélations
        methods = ['pearson', 'spearman', 'kendall']
        for method in methods:
            corr.process(self.test_data, x_col='x', y_col='y', method=method)
        
        # Vérifier le fichier d'historique
        self.assertTrue(os.path.exists(history_file))
        
        with open(history_file, 'r') as f:
            history = json.load(f)
        
        self.assertEqual(len(history), 3)
        self.assertEqual(history[0]['module_type'], 'correlation')
        
        # Vérifier les méthodes d'analyse
        history_stats = corr.get_correlation_history()
        self.assertEqual(history_stats['total_analyses'], 3)
        self.assertEqual(len(history_stats['most_common_methods']), 3)
    
    def test_regression_history(self):
        """Test de l'historique des régressions"""
        history_file = os.path.join(self.temp_dir, "test_reg_history.json")
        reg = Regression(history_file=history_file)
        
        # Effectuer plusieurs régressions
        reg.process(self.test_data, feature_cols=['x'], target_col='y')
        reg.process(self.test_data, feature_cols=['y'], target_col='z')
        reg.process(self.test_data, feature_cols=['x', 'y'], target_col='z')
        
        # Vérifier le fichier d'historique
        self.assertTrue(os.path.exists(history_file))
        
        with open(history_file, 'r') as f:
            history = json.load(f)
        
        self.assertEqual(len(history), 3)
        self.assertEqual(history[0]['module_type'], 'regression')
        
        # Vérifier les méthodes d'analyse
        history_stats = reg.get_regression_history()
        self.assertEqual(history_stats['total_analyses'], 3)
        self.assertIsInstance(history_stats['average_r2'], float)
    
    def test_visualization_history(self):
        """Test de l'historique des visualisations"""
        history_file = os.path.join(self.temp_dir, "test_viz_history.json")
        viz = BasicPlots(history_file=history_file)
        
        # Créer plusieurs visualisations
        viz.process(self.test_data, plot_type='histogram', x_col='x')
        viz.process(self.test_data, plot_type='scatter', x_col='x', y_col='y')
        viz.process(self.test_data, plot_type='boxplot', x_col='z')
        
        # Vérifier le fichier d'historique
        self.assertTrue(os.path.exists(history_file))
        
        with open(history_file, 'r') as f:
            history = json.load(f)
        
        self.assertEqual(len(history), 3)
        self.assertEqual(history[0]['module_type'], 'visualization')
        
        # Vérifier les méthodes d'analyse
        history_stats = viz.get_visualization_history()
        self.assertEqual(history_stats['total_plots'], 3)
        self.assertEqual(len(history_stats['most_common_plot_types']), 3)
    
    def test_data_processor_history(self):
        """Test de l'historique du traitement de données"""
        history_file = os.path.join(self.temp_dir, "test_proc_history.json")
        processor = DataProcessor(history_file=history_file)
        
        # Effectuer plusieurs traitements
        processor.process(self.test_data, operation='standardize')
        processor.process(self.test_data, operation='normalize')
        processor.process(self.test_data, operation='robust_scale')
        
        # Vérifier le fichier d'historique
        self.assertTrue(os.path.exists(history_file))
        
        with open(history_file, 'r') as f:
            history = json.load(f)
        
        self.assertEqual(len(history), 3)
        self.assertEqual(history[0]['module_type'], 'data_processing')
        
        # Vérifier les méthodes d'analyse
        history_stats = processor.get_processing_history()
        self.assertEqual(history_stats['total_operations'], 3)
        self.assertEqual(len(history_stats['most_common_operations']), 3)
    
    def test_data_validator_history(self):
        """Test de l'historique de la validation de données"""
        history_file = os.path.join(self.temp_dir, "test_val_history.json")
        validator = DataValidator(history_file=history_file)
        
        # Effectuer plusieurs validations
        validator.process(self.test_data, validation_type='comprehensive')
        validator.process(self.test_data, validation_type='numeric')
        validator.process(self.test_data, validation_type='missing')
        
        # Vérifier le fichier d'historique
        self.assertTrue(os.path.exists(history_file))
        
        with open(history_file, 'r') as f:
            history = json.load(f)
        
        self.assertEqual(len(history), 3)
        self.assertEqual(history[0]['module_type'], 'data_validation')
        
        # Vérifier les méthodes d'analyse
        history_stats = validator.get_validation_history()
        self.assertEqual(history_stats['total_validations'], 3)
        self.assertIsInstance(history_stats['success_rate'], float)
    
    def test_json_serialization(self):
        """Test de la sérialisation JSON avec booléens"""
        history_file = os.path.join(self.temp_dir, "test_serialization.json")
        stats = BasicStatistics(history_file=history_file)
        
        # Effectuer une analyse qui génère des booléens
        stats.process(self.test_data)
        
        # Vérifier que le fichier peut être lu sans erreur
        with open(history_file, 'r') as f:
            history = json.load(f)
        
        # Vérifier que les booléens ont été convertis en entiers
        self.assertIsInstance(history[0]['results'], dict)
    
    def test_history_file_creation(self):
        """Test de la création automatique des dossiers"""
        # Créer un chemin avec des sous-dossiers
        nested_dir = os.path.join(self.temp_dir, "nested", "subdir")
        history_file = os.path.join(nested_dir, "test_history.json")
        
        stats = BasicStatistics(history_file=history_file)
        stats.process(self.test_data)
        
        # Vérifier que le dossier a été créé automatiquement
        self.assertTrue(os.path.exists(nested_dir))
        self.assertTrue(os.path.exists(history_file))
    
    def test_empty_history_handling(self):
        """Test de la gestion des historiques vides"""
        history_file = os.path.join(self.temp_dir, "empty_history.json")
        stats = BasicStatistics(history_file=history_file)
        
        # Vérifier que les méthodes d'analyse fonctionnent avec un historique vide
        history_stats = stats.get_statistics_history()
        self.assertEqual(history_stats['total_analyses'], 0)
        self.assertEqual(history_stats['average_data_points'], 0)
        self.assertIsNone(history_stats['last_analysis'])

if __name__ == '__main__':
    unittest.main() 