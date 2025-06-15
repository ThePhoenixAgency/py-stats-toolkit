import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from py_stats_toolkit.visualization.VisualizationModule import VisualizationModule

class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.viz = VisualizationModule()
        
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
    
    def test_histogram_single_series(self):
        """Test de l'histogramme avec une seule série."""
        fig = self.viz.process(self.single_series, plot_type="histogram")
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_histogram_multi_series(self):
        """Test de l'histogramme avec plusieurs séries."""
        fig = self.viz.process(self.multi_series, plot_type="histogram")
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_boxplot_single_series(self):
        """Test de la boîte à moustaches avec une seule série."""
        fig = self.viz.process(self.single_series, plot_type="boxplot")
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_boxplot_multi_series(self):
        """Test de la boîte à moustaches avec plusieurs séries."""
        fig = self.viz.process(self.multi_series, plot_type="boxplot")
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_scatter_plot(self):
        """Test du nuage de points."""
        fig = self.viz.process(
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
        fig = self.viz.process(self.heatmap_data, plot_type="heatmap")
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_time_series_plot(self):
        """Test du graphique de série temporelle."""
        fig = self.viz.plot_time_series(
            self.time_series_data,
            time_col='temps',
            value_col='valeur',
            group_col='groupe'
        )
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_correlation_matrix(self):
        """Test de la matrice de corrélation."""
        fig = self.viz.plot_correlation_matrix(self.multi_series)
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_survival_curves(self):
        """Test des courbes de survie."""
        fig = self.viz.plot_survival_curves(self.survival_data)
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_invalid_plot_type(self):
        """Test avec un type de graphique invalide."""
        with self.assertRaises(ValueError):
            self.viz.process(self.single_series, plot_type="invalid_plot")
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.viz.process("invalid_data", plot_type="histogram")
    
    def test_scatter_missing_columns(self):
        """Test du nuage de points avec des colonnes manquantes."""
        with self.assertRaises(KeyError):
            self.viz.process(
                self.scatter_data,
                plot_type="scatter",
                x_col='invalid_x',
                y_col='y'
            )

if __name__ == '__main__':
    unittest.main() 