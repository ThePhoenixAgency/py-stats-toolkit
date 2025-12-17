"""
=====================================================================
File : ProbabilistesModule.py
=====================================================================
version : 2.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Refactored module for probability analysis.
Follows SOLID principles with separation of business logic and algorithms.

tags : module, stats, refactored
=====================================================================
"""

tags : module, stats
"""
from typing import Any, Union

import numpy as np

from py_stats_toolkit.algorithms import probability as prob_algos
from py_stats_toolkit.core.base import StatisticalModule
from py_stats_toolkit.core.validators import DataValidator
from py_stats_toolkit.utils.data_processor import DataProcessor


class ProbabilistesModule(StatisticalModule):
    """
    Module for probability analysis (Business Logic Layer).

    Responsibilities:
    - Orchestrate probability analysis workflow
    - Manage results and state
    - Provide user-facing API

    Delegates to:
    - DataValidator for validation
    - prob_algos for computations
    """

    def __init__(self):
        """Initialize probability module."""
        super().__init__()
        self.distribution_type = None

    def process(self, data: Union[np.ndarray, list],
                distribution: str = "normal", **kwargs) -> Any:
        """
        Fit a distribution to data.

        Args:
            data: Input data (numpy array or list)
            distribution: Type of distribution ('normal', 'exponential', 'gamma')
            **kwargs: Additional parameters

        Returns:
            scipy.stats distribution object with fitted parameters.
            The returned object has methods like pdf(), cdf(), rvs(), etc.
        """
        # Validation (delegated to validator)
        DataValidator.validate_data(data)

        # Store state
        self.data = data
        self.distribution_type = distribution

        # Convert to numpy
        data_array = DataProcessor.to_numpy(data)

        # Computation (delegated to algorithm layer)
        self.result = prob_algos.fit_distribution(data_array, distribution)

        return self.result['distribution']

    def get_pdf(self, x: np.ndarray) -> np.ndarray:
from scipy import stats

from ...utils.parallel import ParallelProcessor
from ..core.AbstractClassBase import StatisticalModule


class ProbabilistesModule(StatisticalModule):
    """Module pour l'analyse probabiliste."""

    def __init__(self, n_jobs: int = -1, batch_size: int = 1000):
        super().__init__()
        self.distribution = None
        self.params = None
        self.batch_size = batch_size
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)

    def _fit_distribution_chunk(self, chunk):
        """Ajuste une distribution sur un chunk de données."""
        if self.distribution == "normal":
            return stats.norm.fit(chunk)
        elif self.distribution == "exponential":
            return stats.expon.fit(chunk)
        elif self.distribution == "gamma":
            return stats.gamma.fit(chunk)
        else:
            raise ValueError(f"Distribution {self.distribution} non supportée")

    def _average_params(self, param_list):
        """Moyenne les paramètres de distribution sur plusieurs chunks."""
        return np.mean(param_list, axis=0)

    def process(self, data, distribution="normal", **kwargs):
        """
        Ajuste une distribution aux données en parallèle.

        Args:
            data: Données d'entrée (numpy array)
            distribution: Type de distribution ('normal', 'exponential', 'gamma', etc.)
            **kwargs: Paramètres additionnels pour la distribution

        Returns:
            Objet de distribution ajusté
        """
        self.validate_data(data)
        self.distribution = distribution

        # Pour les petits ensembles de données, ajustement direct
        # Use 2x batch_size threshold to avoid parallel overhead for medium datasets
        if len(data) < self.batch_size * 2:
            if distribution == "normal":
                self.params = stats.norm.fit(data)
                self.result = stats.norm(*self.params)
            elif distribution == "exponential":
                self.params = stats.expon.fit(data)
                self.result = stats.expon(*self.params)
            elif distribution == "gamma":
                self.params = stats.gamma.fit(data)
                self.result = stats.gamma(*self.params)
            else:
                raise ValueError(f"Distribution {distribution} non supportée")
            return self.result

        # Pour les grands ensembles de données, traitement parallèle
        chunks = np.array_split(data, self.parallel_processor.n_jobs)
        chunk_params = self.parallel_processor.parallel_map(
            self._fit_distribution_chunk, chunks
        )
        self.params = self._average_params(chunk_params)

        # Création de l'objet de distribution avec les paramètres moyens
        if distribution == "normal":
            self.result = stats.norm(*self.params)
        elif distribution == "exponential":
            self.result = stats.expon(*self.params)
        elif distribution == "gamma":
            self.result = stats.gamma(*self.params)

        return self.result

    def get_distribution_params(self):
        """Retourne les paramètres de la distribution ajustée."""
        return self.params

    def get_probability_density(self, x):
        """
        Calcule la densité de probabilité pour les valeurs x en parallèle.

        Args:
            x: Valeurs pour lesquelles calculer la densité
        Compute probability density function.

        Args:
            x: Values at which to compute PDF

        Returns:
            PDF values
        """
        if not self.has_result():
            raise ValueError("No distribution fitted. Call process() first.")

        return prob_algos.compute_pdf(
            self.distribution_type,
            self.result['params'],
            x
        )

    def get_cdf(self, x: np.ndarray) -> np.ndarray:
        if self.result is None:
            raise ValueError("Exécutez d'abord process()")

        # Pour les petits ensembles, calcul direct
        # Use 2x batch_size threshold to avoid parallel overhead
        if len(x) < self.batch_size * 2:
            return self.result.pdf(x)

        # Pour les grands ensembles, traitement parallèle
        chunks = np.array_split(x, self.parallel_processor.n_jobs)
        pdf_chunks = self.parallel_processor.parallel_map(self.result.pdf, chunks)
        return np.concatenate(pdf_chunks)

    def get_cumulative_distribution(self, x):
        """
        Calcule la fonction de répartition pour les valeurs x en parallèle.

        Args:
            x: Valeurs pour lesquelles calculer la fonction de répartition
        Compute cumulative distribution function.

        Args:
            x: Values at which to compute CDF

        Returns:
            CDF values
        """
        if not self.has_result():
            raise ValueError("No distribution fitted. Call process() first.")

        return prob_algos.compute_cdf(
            self.distribution_type,
            self.result['params'],
            x
        )
        if self.result is None:
            raise ValueError("Exécutez d'abord process()")

        # Pour les petits ensembles, calcul direct
        # Use 2x batch_size threshold to avoid parallel overhead
        if len(x) < self.batch_size * 2:
            return self.result.cdf(x)

        # Pour les grands ensembles, traitement parallèle
        chunks = np.array_split(x, self.parallel_processor.n_jobs)
        cdf_chunks = self.parallel_processor.parallel_map(self.result.cdf, chunks)
        return np.concatenate(cdf_chunks)
        return np.concatenate(cdf_chunks) 
