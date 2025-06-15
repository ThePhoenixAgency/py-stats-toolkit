'''
=====================================================================
File : __init__.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module initialise le package principal py_stats_toolkit. Il définit
les imports publics et les configurations globales pour l'ensemble
de la bibliothèque d'analyse statistique.

tags : initialisation, package, configuration, bibliothèque, statistiques
=====================================================================
'''

from .Abstracts.AbstractClassBase import StatisticalModule
from .Abstracts.TimeSeriesModule import TimeSeriesModule
from .Abstracts.RegressionModule import RegressionModule
from .Abstracts.TestModule import TestModule
from .Abstracts.VisualizationModule import VisualizationModule
from .Abstracts.GameTheoryModule import GameTheoryModule
from .Abstracts.FractalModule import FractalModule
from .Abstracts.MarkovChainModule import MarkovChainModule
from .Abstracts.AdvancedTimeSeriesModule import AdvancedTimeSeriesModule
from .Abstracts.NetworkAnalysisModule import NetworkAnalysisModule
from .Abstracts.GeneticAlgorithmModule import GeneticAlgorithmModule
from .capsules.BaseCapsule import BaseCapsule

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
    'GeneticAlgorithmModule',
    'BaseCapsule'
] 