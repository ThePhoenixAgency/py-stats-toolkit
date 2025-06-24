'''
import unittest
import pytest
=====================================================================
File : test_visualization.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module test_visualization.py

tags : module, stats
=====================================================================
Ce module Description du module test_visualization.py

tags : module, stats
=====================================================================
'''

# Imports spécifiques au module
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

# Imports de la base
from py_stats_toolkit.Abstracts.AbstractClassBase import StatisticalModule

class TestVisualization(unittest.TestCase):
    """
    Tests pour le module de visualisation.
    """
    
    def setUp(self):
        """
        Configuration initiale pour les tests.
        """
        self.data = pd.DataFrame({
            'x': np.random.normal(0, 1, 100),
            'y': np.random.normal(0, 1, 100)
        })
        self.visualizer = StatisticalModule()
        
        # Données de test pour les histogrammes et boîtes à moustaches
        self.single_series = pd.Series(np.random.normal(0, 1, 1000))
        self.multi_series = pd.DataFrame({
            'A': np.random.normal(0, 1, 1000),
            'B': np.random.normal(1, 1, 1000),
            'C': np.random.normal(2, 1, 1000)
        })
        
        # Données de test pour les nuages de points
        self.scatter_data = pd.DataFrame({
            'x': np.random.normal(0, 1, 100),
            'y': np.random.normal(0, 1, 100),
            'groupe': np.random.choice(['A', 'B'], size=100)
        })
        
        # Données de test pour les cartes de chaleur
        self.heatmap_data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
        
        # Données de test pour les séries temporelles
        self.time_series_data = pd.DataFrame({
            'temps': pd.date_range(start='2020-01-01', periods=100, freq='D'),
            'valeur': np.random.normal(0, 1, 100),
            'groupe': np.random.choice(['A', 'B'], size=100)
        })
        
        # Données de test pour les courbes de survie
        self.survival_data = {
            'A': {
                'Médiane de survie': 100,
                'Courbe de survie': pd.Series(
                    np.exp(-np.linspace(0, 200, 100)),
                    index=np.linspace(0, 200, 100)
                )
            },
            'B': {
                'Médiane de survie': 150,
                'Courbe de survie': pd.Series(
                    np.exp(-np.linspace(0, 200, 100)),
                    index=np.linspace(0, 200, 100)
                )
            }
        }
        
        # Données de test pour les visualisations
        self.data = pd.DataFrame({
            'x': np.random.normal(0, 1, 100),
            'y': np.random.normal(0, 1, 100),
            'categorie': ['A', 'B', 'C'] * 33 + ['A']
        })
    
    def test_histogram_single_series(self):
        """Test de l'histogramme avec une seule série."""
        fig = self.visualizer.process(self.single_series, plot_type="histogram")
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_histogram_multi_series(self):
        """Test de l'histogramme avec plusieurs séries."""
        fig = self.visualizer.process(self.multi_series, plot_type="histogram")
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_boxplot_single_series(self):
        """Test de la boîte à moustaches avec une seule série."""
        fig = self.visualizer.process(self.single_series, plot_type="boxplot")
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_boxplot_multi_series(self):
        """Test de la boîte à moustaches avec plusieurs séries."""
        fig = self.visualizer.process(self.multi_series, plot_type="boxplot")
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_scatter_plot(self):
        """Test du nuage de points."""
        fig = self.visualizer.process(
            self.scatter_data,
            plot_type="scatter",
            x_col='x',
            y_col='y',
            hue='groupe'
        )
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_heatmap(self):
        """Test de la carte de chaleur."""
        fig = self.visualizer.process(self.heatmap_data, plot_type="heatmap")
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_time_series_plot(self):
        """Test du graphique de série temporelle."""
        fig = self.visualizer.plot_time_series(
            self.time_series_data,
            time_col='temps',
            value_col='valeur',
            group_col='groupe'
        )
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_correlation_matrix(self):
        """Test de la matrice de corrélation."""
        fig = self.visualizer.plot_correlation_matrix(self.multi_series)
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_survival_curves(self):
        """Test des courbes de survie."""
        fig = self.visualizer.plot_survival_curves(self.survival_data)
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_invalid_plot_type(self):
        """Test avec un type de graphique invalide."""
        with self.assertRaises(ValueError):
            self.visualizer.process(self.single_series, plot_type="invalid_plot")
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.visualizer.process("invalid_data", plot_type="histogram")
    
    def test_scatter_missing_columns(self):
        """Test du nuage de points avec des colonnes manquantes."""
        with self.assertRaises(KeyError):
            self.visualizer.process(
                self.scatter_data,
                plot_type="scatter",
                x_col='invalid_x',
                y_col='y'
            )
    
    def test_histogramme(self):
        """Test de l'histogramme."""
        result = self.visualizer.process(
            self.data,
            plot_type="histogramme",
            value_col='x'
        )
        
        self.assertIn('Type', result)
        self.assertIn('Figure', result)
        self.assertEqual(result['Type'], 'Histogramme')
    
    def test_boxplot(self):
        """Test du boxplot."""
        result = self.visualizer.process(
            self.data,
            plot_type="boxplot",
            value_col='x',
            group_col='categorie'
        )
        
        self.assertIn('Type', result)
        self.assertIn('Figure', result)
        self.assertEqual(result['Type'], 'Boxplot')
    
    def test_scatter(self):
        """Test du nuage de points."""
        result = self.visualizer.process(
            self.data,
            plot_type="scatter",
            x_col='x',
            y_col='y'
        )
        
        self.assertIn('Type', result)
        self.assertIn('Figure', result)
        self.assertEqual(result['Type'], 'Nuage de points')
    
    def test_invalid_plot_type_basic(self):
        """Test avec un type de graphique invalide."""
        with self.assertRaises(ValueError):
            self.visualizer.process(
                self.data,
                plot_type="invalid_plot",
                value_col='x'
            )
    
    def test_invalid_data_type_basic(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.visualizer.process(
                "invalid_data",
                plot_type="histogramme",
                value_col='x'
            )
    
    def test_missing_columns(self):
        """Test avec des colonnes manquantes."""
        with self.assertRaises(ValueError):
            self.visualizer.process(
                self.data,
                plot_type="histogramme",
                value_col='invalid_col'
            )

if __name__ == '__main__':
    unittest.main() 