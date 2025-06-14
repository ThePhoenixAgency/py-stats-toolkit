"""
Module de machine learning
"""

from .predictor import MLPredictor
from .classifier import Classifier
from .regressor import Regressor
from .clustering import ClusterAnalyzer

__all__ = [
    'MLPredictor',
    'Classifier',
    'Regressor',
    'ClusterAnalyzer'
] 