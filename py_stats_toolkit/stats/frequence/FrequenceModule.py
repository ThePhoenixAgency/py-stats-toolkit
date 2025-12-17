"""
=====================================================================
File : FrequenceModule.py
=====================================================================
version : 2.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Refactored module for frequency analysis.
Follows SOLID principles with separation of business logic and algorithms.

tags : module, stats, refactored
=====================================================================
Ce module Description du module FrequenceModule.py

tags : module, stats
"""

from typing import Union
import numpy as np
import pandas as pd

from ...utils.parallel import ParallelProcessor
from ..core.AbstractClassBase import StatisticalModule


class FrequenceModule(StatisticalModule):
    """Module pour l'analyse de fréquence."""

    def __init__(self, n_jobs: int = -1):
        super().__init__()
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)

    def process(self, data, normalize=False, **kwargs):
        """
        Calcule les fréquences des valeurs.

        Args:
            data: Données d'entrée (numpy array ou pandas Series)
            normalize: Si True, retourne les fréquences relatives
            **kwargs: Arguments additionnels
# Import base class and utilities
from py_stats_toolkit.core.base import StatisticalModule
from py_stats_toolkit.core.validators import DataValidator
from py_stats_toolkit.algorithms import descriptive_stats as desc_algos
from py_stats_toolkit.utils.data_processor import DataProcessor


class FrequenceModule(StatisticalModule):
    """
    Module for frequency analysis (Business Logic Layer).

    Responsibilities:
    - Orchestrate frequency analysis workflow
    - Manage results and state
    - Provide user-facing API

    Delegates to:
    - DataValidator for validation
    - desc_algos for computations
    """

    def __init__(self):
        """Initialize frequency module."""
        super().__init__()

    def process(self, data: Union[pd.Series, np.ndarray, list],
                normalize: bool = False, **kwargs) -> pd.DataFrame:
        """
        Compute frequency distribution.

        Args:
            data: Input data
            normalize: If True, return relative frequencies
            **kwargs: Additional arguments

        Returns:
            DataFrame with frequencies
        """
        self.validate_data(data)

        if isinstance(data, pd.Series):
            series = data
        else:
            series = pd.Series(data)

        # Calcul des fréquences
        freq = series.value_counts(normalize=normalize)
        cum_freq = freq.cumsum()

        # Création du DataFrame de résultats
        self.result = pd.DataFrame({"Fréquence": freq, "Fréquence Cumulée": cum_freq})

        if normalize:
            self.result.columns = ["Fréquence Relative", "Fréquence Relative Cumulée"]

        return self.result

    def get_frequence_absolue(self):
        """Retourne les fréquences absolues."""
        if self.result is None:
            raise ValueError("Exécutez d'abord process()")
        return self.result["Fréquence"]

    def get_frequence_cumulee(self):
        """Retourne les fréquences cumulées."""
        if self.result is None:
            raise ValueError("Exécutez d'abord process()")
        return self.result["Fréquence Cumulée"]

    def get_frequence_relative(self):
        """Retourne les fréquences relatives."""
        if self.result is None:
            raise ValueError("Exécutez d'abord process()")
        # Check if already normalized
        if "Fréquence Relative" in self.result.columns:
            return self.result["Fréquence Relative"]
        # Normalize existing frequency counts instead of reprocessing
        # This should always exist if process() was called successfully
        if "Fréquence" not in self.result.columns:
            raise RuntimeError("Internal error: 'Fréquence' column missing")
        return self.result["Fréquence"] / self.result["Fréquence"].sum()
        # Validation (delegated to validator)
        DataValidator.validate_data(data)

        # Store state
        self.data = data

        # Convert to numpy for computation
        data_array = DataProcessor.to_numpy(data)

        # Computation (delegated to algorithm layer)
        self.result = desc_algos.compute_frequency_distribution(data_array, normalize)
tags : module, stats
'''

import numpy as np
import pandas as pd
from ..core.AbstractClassBase import StatisticalModule
from ...utils.parallel import ParallelProcessor

        return self.result
