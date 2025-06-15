'''
=====================================================================
File : test_biostats.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module test_biostats.py

tags : module, stats
=====================================================================
Ce module Description du module test_biostats.py

tags : module, stats
=====================================================================
'''

# Imports spécifiques au module
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
import unittest
from py_stats_toolkit.Modules.biostats.BioStatsModule import BioStatsModule

class TestBioStats(unittest.TestCase):
    def setUp(self):
        self.biostats = BioStatsModule()
        
        # Données de test pour le test t
        self.t_test_data = pd.DataFrame({
            'groupe': ['A'] * 50 + ['B'] * 50,
            'valeur': np.concatenate([
                np.random.normal(0, 1, 50),
                np.random.normal(1, 1, 50)
            ])
        })
        
        # Données de test pour l'ANOVA
        self.anova_data = pd.DataFrame({
            'groupe': ['A'] * 30 + ['B'] * 30 + ['C'] * 30,
            'valeur': np.concatenate([
                np.random.normal(0, 1, 30),
                np.random.normal(1, 1, 30),
                np.random.normal(2, 1, 30)
            ])
        })
        
        # Données de test pour le chi2
        self.chi2_data = pd.DataFrame({
            'A': [10, 20, 30],
            'B': [15, 25, 35],
            'C': [20, 30, 40]
        })
        
        # Données de test pour l'analyse de survie
        self.survival_data = pd.DataFrame({
            'temps': np.random.exponential(scale=100, size=100),
            'evenement': np.random.binomial(1, 0.7, size=100),
            'groupe': np.random.choice(['A', 'B'], size=100)
        })
    
    def test_t_test(self):
        """Test du test t de Student."""
        result = self.biostats.process(
            self.t_test_data,
            test_type="t-test",
            group_col='groupe',
            value_col='valeur'
        )
        
        self.assertIn('Test', result)
        self.assertIn('Statistique t', result)
        self.assertIn('p-valeur', result)
        self.assertIn('Groupes', result)
        self.assertEqual(result['Test'], 't-test')
        self.assertEqual(len(result['Groupes']), 2)
    
    def test_anova(self):
        """Test de l'ANOVA."""
        result = self.biostats.process(
            self.anova_data,
            test_type="anova",
            group_col='groupe',
            value_col='valeur'
        )
        
        self.assertIn('Test', result)
        self.assertIn('Statistique F', result)
        self.assertIn('p-valeur', result)
        self.assertIn('Groupes', result)
        self.assertEqual(result['Test'], 'ANOVA')
        self.assertEqual(len(result['Groupes']), 3)
    
    def test_chi2(self):
        """Test du chi2."""
        result = self.biostats.process(
            self.chi2_data,
            test_type="chi2"
        )
        
        self.assertIn('Test', result)
        self.assertIn('Statistique Chi2', result)
        self.assertIn('p-valeur', result)
        self.assertIn('Degrés de liberté', result)
        self.assertEqual(result['Test'], 'Chi2')
    
    def test_survival_analysis(self):
        """Test de l'analyse de survie."""
        result = self.biostats.survival_analysis(
            self.survival_data,
            time_col='temps',
            event_col='evenement',
            group_col='groupe'
        )
        
        self.assertIsInstance(result, dict)
        for group in ['A', 'B']:
            self.assertIn(group, result)
            self.assertIn('Médiane de survie', result[group])
            self.assertIn('Courbe de survie', result[group])
    
    def test_invalid_test_type(self):
        """Test avec un type de test invalide."""
        with self.assertRaises(ValueError):
            self.biostats.process(
                self.t_test_data,
                test_type="invalid_test"
            )
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.biostats.process(
                "invalid_data",
                test_type="t-test"
            )
    
    def test_t_test_invalid_groups(self):
        """Test t avec un nombre invalide de groupes."""
        invalid_data = pd.DataFrame({
            'groupe': ['A'] * 30 + ['B'] * 30 + ['C'] * 30,
            'valeur': np.random.normal(0, 1, 90)
        })
        
        with self.assertRaises(ValueError):
            self.biostats.process(
                invalid_data,
                test_type="t-test",
                group_col='groupe',
                value_col='valeur'
            )

if __name__ == '__main__':
    unittest.main() 