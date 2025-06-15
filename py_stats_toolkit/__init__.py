'''
=====================================================================
py_stats_toolkit
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

A comprehensive statistical analysis toolkit providing advanced
methods for data analysis, visualization, and modeling.

tags : statistics, data analysis, visualization, modeling, machine learning
=====================================================================
Une boîte à outils complète d'analyse statistique fournissant des
méthodes avancées pour l'analyse de données, la visualisation et
la modélisation.

tags : statistiques, analyse de données, visualisation, modélisation, apprentissage automatique
=====================================================================
'''

from .core.StatisticalModule import StatisticalModule
from .core.TimeSeriesModule import TimeSeriesModule
from .core.RegressionModule import RegressionModule
from .core.TestModule import TestModule
from .core.VisualizationModule import VisualizationModule
from .core.GameTheoryModule import GameTheoryModule
from .core.FractalModule import FractalModule
from .core.MarkovChainModule import MarkovChainModule
from .core.AdvancedTimeSeriesModule import AdvancedTimeSeriesModule
from .core.NetworkAnalysisModule import NetworkAnalysisModule
from .core.GeneticAlgorithmModule import GeneticAlgorithmModule

__version__ = '0.1.0'
__author__ = 'Phoenix Project'
__license__ = 'MIT'

__all__ = [
    'StatisticalModule',
    'TimeSeriesModule',
    'RegressionModule',
    'TestModule',
    'VisualizationModule',
    'GameTheoryModule',
    'FractalModule',
    'MarkovChainModule',
    'AdvancedTimeSeriesModule',
    'NetworkAnalysisModule',
    'GeneticAlgorithmModule'
] 