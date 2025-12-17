"""
=====================================================================
File : CorrelationModule.py
=====================================================================
version : 2.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Refactored module for correlation analysis.
Follows SOLID principles with separation of business logic and algorithms.

tags : module, stats, refactored
=====================================================================
"""

tags : module, stats
"""
from typing import List, Tuple, Union

import pandas as pd
from scipy import stats

from ...utils.parallel import ParallelProcessor
from ..core.AbstractClassBase import StatisticalModule


class CorrelationModule(StatisticalModule):
    """Module pour l'analyse de corrélation."""

    def __init__(self, n_jobs: int = -1):
        super().__init__()
        self.method = None
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)

    def process(self, data, method="pearson", **kwargs):
        """
        Calcule la corrélation entre les variables.

        Args:
            data: Données d'entrée (pandas DataFrame)
            method: Méthode de corrélation ('pearson', 'spearman', 'kendall')
            **kwargs: Arguments additionnels

from py_stats_toolkit.algorithms import correlation as correlation_algos
from py_stats_toolkit.core.base import StatisticalModule
from py_stats_toolkit.core.validators import DataValidator


class CorrelationModule(StatisticalModule):
    """
    Module for correlation analysis (Business Logic Layer).

    Responsibilities:
    - Orchestrate correlation analysis workflow
    - Manage results and state
    - Provide user-facing API

    Delegates to:
    - DataValidator for validation
    - correlation_algos for computations
    """

    def __init__(self):
        """Initialize correlation module."""
        super().__init__()
        self.method = None

    def process(self, data: Union[pd.DataFrame, pd.Series], method: str = "pearson",
                **kwargs) -> pd.DataFrame:
        """
        Compute correlation between variables.

        Args:
            data: Input DataFrame
            method: Correlation method ('pearson', 'spearman', 'kendall')
            **kwargs: Additional arguments

        Returns:
            Correlation matrix
        """
        self.validate_data(data)
        self.method = method

        if not isinstance(data, pd.DataFrame):
            raise TypeError("Les données doivent être un pandas DataFrame")

        # Compute correlation matrix directly
        # pandas/numpy already use optimized algorithms
        # Note: Chunking correlation computation produces incorrect results because
        # correlation requires all data points to compute proper covariance and variance statistics
        self.result = data.corr(method=method)
        return self.result

    def get_correlation_matrix(self):
        """Retourne la matrice de corrélation."""
        return self.result

    def get_correlation_pairs(self, threshold=0.5):
        """
        Retourne les paires de variables avec une corrélation supérieure au seuil.

        Args:
            threshold: Seuil de corrélation
        # Validation (delegated to validator)
        DataValidator.validate_data(data)

        if not isinstance(data, pd.DataFrame):
            raise TypeError(f"Data must be a pandas DataFrame. Got {type(data).__name__} instead.")
import numpy as np
import pandas as pd
from scipy import stats
from ..core.AbstractClassBase import StatisticalModule
from ...utils.parallel import ParallelProcessor, get_optimal_chunk_size

        DataValidator.validate_numeric(data)

        # Store state
        self.data = data
        self.method = method

        # Computation (delegated to algorithm layer)
        self.result = correlation_algos.compute_correlation_matrix(data, method)

        return self.result

    def get_correlation_matrix(self) -> pd.DataFrame:
        """
        Get the correlation matrix.

        Returns:
            Correlation matrix
        """
        return self.get_result()

    def get_correlation_pairs(self, threshold: float = 0.5) -> List[Tuple[str, str, float]]:
        """
        Get variable pairs with correlation above threshold.

        Args:
            threshold: Minimum absolute correlation value

        Returns:
            List of (var1, var2, correlation) tuples
        """
        if self.result is None:
            raise ValueError("Exécutez d'abord process()")

        # Utilisation de numpy pour le calcul parallèle des paires
        corr_matrix = self.result.to_numpy()
        n = len(self.result.columns)

        # Création des indices pour les paires
        i, j = np.triu_indices(n, k=1)
        corr_values = corr_matrix[i, j]

        # Filtrage des paires selon le seuil
        mask = np.abs(corr_values) >= threshold
        mask_indices = np.where(mask)[0]

        # Vectorized construction of pairs using list comprehension
        pairs = [
            (self.result.columns[i[idx]], self.result.columns[j[idx]], corr_values[idx])
            for idx in mask_indices
        ]

        if not self.has_result():
            raise ValueError("No analysis performed. Call process() first.")

        # Extract pairs from the already-computed correlation matrix
        corr_matrix = self.result
        pairs = []
        cols = corr_matrix.columns
        for i in range(len(cols)):
            for j in range(i + 1, len(cols)):
                corr_value = corr_matrix.iloc[i, j]
                if abs(corr_value) >= threshold:
                    pairs.append((cols[i], cols[j], corr_value))
        return sorted(pairs, key=lambda x: abs(x[2]), reverse=True)
