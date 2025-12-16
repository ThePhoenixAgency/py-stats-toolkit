"""
=====================================================================
File : MoyenneGlissanteModule.py
=====================================================================
version : 2.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Refactored module for moving average (descriptive statistics).
Follows SOLID principles with separation of business logic and algorithms.

tags : module, stats, refactored
=====================================================================
"""

from typing import Union
import numpy as np
import pandas as pd

# Import base class and utilities
from py_stats_toolkit.core.base import StatisticalModule
from py_stats_toolkit.core.validators import DataValidator
from py_stats_toolkit.algorithms import descriptive_stats as desc_algos
from py_stats_toolkit.utils.data_processor import DataProcessor


class MoyenneGlissanteModule(StatisticalModule):
    """
    Module for moving average calculation (Business Logic Layer).

    Responsibilities:
    - Orchestrate moving average workflow
    - Manage results and state
    - Provide user-facing API

    Delegates to:
    - DataValidator for validation
    - desc_algos for computations
    - DataProcessor for data transformations
    """

    def __init__(self):
        """Initialize moving average module."""
        super().__init__()
        self.window_size = None

    def process(self, data: Union[pd.Series, np.ndarray, list],
                window_size: int = 5, **kwargs) -> pd.Series:
        """
        Compute moving average.

        Args:
            data: Input data (Series, array, or list)
            window_size: Size of the moving window
            **kwargs: Additional arguments

        Returns:
            Moving average as Series
        """
        # Validation (delegated to validator)
        DataValidator.validate_data(data)

        # Store state
        self.data = data
        self.window_size = window_size

        # Convert to numpy for computation
        data_array = DataProcessor.to_numpy(data)

        # Computation (delegated to algorithm layer)
        result_array = desc_algos.compute_moving_average(data_array, window_size)

        # Convert back to Series
        if isinstance(data, pd.Series):
            self.result = pd.Series(result_array, index=data.index, name=data.name)
        else:
            self.result = pd.Series(result_array)

        return self.result

    def get_window_size(self) -> int:
        """
        Get the window size used.

        Returns:
            Window size
        """
        return self.window_size
