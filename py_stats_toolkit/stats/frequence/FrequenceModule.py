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
"""

from typing import Union
import numpy as np
import pandas as pd

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
