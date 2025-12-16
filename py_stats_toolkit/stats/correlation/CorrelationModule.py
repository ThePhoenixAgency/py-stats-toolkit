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

from typing import List, Tuple, Union

import pandas as pd

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
        # Validation (delegated to validator)
        DataValidator.validate_data(data)
        
        if not isinstance(data, pd.DataFrame):
            raise TypeError(f"Data must be a pandas DataFrame. Got {type(data).__name__} instead.")
        
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