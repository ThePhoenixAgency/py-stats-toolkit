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

from typing import Any, Union

import numpy as np
from scipy.stats import rv_continuous

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
        """
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
        """
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
