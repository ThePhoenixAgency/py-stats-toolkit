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

from typing import Union
import pandas as pd

# Import base class and utilities
from py_stats_toolkit.core.base import StatisticalModule
from py_stats_toolkit.core.validators import DataValidator
from py_stats_toolkit.utils.parallel import ParallelProcessor, get_optimal_chunk_size
from py_stats_toolkit.algorithms import correlation as correlation_algos


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
    - ParallelProcessor for parallel processing
    """
    
    def __init__(self, n_jobs: int = -1):
        """
        Initialize correlation module.
        
        Args:
            n_jobs: Number of parallel jobs (-1 for all CPUs)
        """
        super().__init__()
        self.method = None
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)
    
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
        # Validation (delegated to validator)
        DataValidator.validate_data(data)
        
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame")
        
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
    
    def get_correlation_pairs(self, threshold: float = 0.5):
        """
        Get variable pairs with correlation above threshold.
        
        Args:
            threshold: Minimum absolute correlation value
            
        Returns:
            List of (var1, var2, correlation) tuples
        """
        if not self.has_result():
            raise ValueError("No analysis performed. Call process() first.")
        
        # Delegate computation to algorithm layer
        return correlation_algos.compute_pairwise_correlations(
            self.data, self.method, threshold
        ) 