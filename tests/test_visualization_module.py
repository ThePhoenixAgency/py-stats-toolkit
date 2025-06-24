'''
import unittest
=====================================================================
File : test_visualization_module.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module contient les tests unitaires pour le module de visualisation
de la bibliothèque py_stats_toolkit.

tags : tests, unitaires, visualisation, validation
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from py_stats_toolkit.Abstracts.VisualizationModule import VisualizationModule

class TestVisualizationModule:
    """Tests pour la classe VisualizationModule."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        module = VisualizationModule()
        assert module.tags == ["stats", "module", "visualization"]
        assert module.version == "1.0.0"
        assert module.data is None
        assert module.result is None
        assert module.fig is None
        assert module.ax is None
    
    def test_create_figure(self):
        """Teste la création d'une figure."""
        module = VisualizationModule()
        module.create_figure()
        assert isinstance(module.fig, plt.Figure)
        assert isinstance(module.ax, plt.Axes)
    
    def test_set_data(self):
        """Teste la définition des données."""
        module = VisualizationModule()
        data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        module.set_data(data)
        assert isinstance(module.data, pd.DataFrame)
        assert module.data.shape == (3, 2)
    
    def test_plot_histogram(self):
        """Teste la création d'un histogramme."""
        module = VisualizationModule()
        data = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 5])
        module.set_data(data)
        module.create_figure()
        module.plot_histogram()
        assert len(module.ax.patches) > 0
    
    def test_plot_scatter(self):
        """Teste la création d'un nuage de points."""
        module = VisualizationModule()
        data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        module.set_data(data)
        module.create_figure()
        module.plot_scatter('A', 'B')
        assert len(module.ax.collections) > 0
    
    def test_plot_line(self):
        """Teste la création d'un graphique en ligne."""
        module = VisualizationModule()
        data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        module.set_data(data)
        module.create_figure()
        module.plot_line('A', 'B')
        assert len(module.ax.lines) > 0
    
    def test_set_title(self):
        """Teste la définition du titre."""
        module = VisualizationModule()
        module.create_figure()
        title = "Test Title"
        module.set_title(title)
        assert module.ax.get_title() == title
    
    def test_set_labels(self):
        """Teste la définition des labels."""
        module = VisualizationModule()
        module.create_figure()
        xlabel = "X Axis"
        ylabel = "Y Axis"
        module.set_labels(xlabel, ylabel)
        assert module.ax.get_xlabel() == xlabel
        assert module.ax.get_ylabel() == ylabel
    
    def test_save_figure(self, tmp_path):
        """Teste la sauvegarde de la figure."""
        module = VisualizationModule()
        module.create_figure()
        filepath = tmp_path / "test_plot.png"
        module.save_figure(str(filepath))
        assert filepath.exists()
    
    def test_clear_figure(self):
        """Teste le nettoyage de la figure."""
        module = VisualizationModule()
        module.create_figure()
        module.plot_histogram()
        module.clear_figure()
        assert len(module.ax.patches) == 0 