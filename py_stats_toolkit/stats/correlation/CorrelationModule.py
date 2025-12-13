"""
=====================================================================
File : CorrelationModule.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module CorrelationModule.py

tags : module, stats
=====================================================================
Ce module Description du module CorrelationModule.py

tags : module, stats
=====================================================================
"""

import numpy as np
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

        Returns:
            Matrice de corrélation
        """
        self.validate_data(data)
        self.method = method

        if not isinstance(data, pd.DataFrame):
            raise TypeError("Les données doivent être un pandas DataFrame")

        # Compute correlation matrix directly
        # pandas/numpy already use optimized algorithms
        # Chunking correlation computation produces incorrect results
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

        Returns:
            Liste de tuples (var1, var2, corr)
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

        return sorted(pairs, key=lambda x: abs(x[2]), reverse=True)
