"""
=====================================================================
File : VarianceModule.py
=====================================================================
version : 2.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Refactored module for variance analysis.
Follows SOLID principles with separation of business logic and algorithms.

tags : module, stats, refactored
=====================================================================
"""

from typing import Any, Dict

import pandas as pd

from py_stats_toolkit.algorithms import variance as variance_algos
from py_stats_toolkit.core.base import StatisticalModule
from py_stats_toolkit.core.validators import DataValidator


class VarianceModule(StatisticalModule):
    """
    Module for variance analysis (Business Logic Layer).
    
    Responsibilities:
    - Orchestrate variance analysis workflow
    - Manage results and state
    - Provide user-facing API
    
    Delegates to:
    - DataValidator for validation
    - variance_algos for computations
    """
    
    def __init__(self):
        """Initialize variance module."""
        super().__init__()
    
    def process(self, data: pd.DataFrame, group_col: str, value_col: str,
                test_type: str = "anova", **kwargs) -> Dict[str, Any]:
        """
        Perform variance analysis.
        
        Args:
            data: DataFrame with data
            group_col: Column name for groups
            value_col: Column name for values
            test_type: Type of test ('anova', 'kruskal', 'friedman')
            **kwargs: Additional arguments
            
        Returns:
            Dictionary with analysis results containing:
            For ANOVA:
                - 'f_statistic': F-statistic value
                - 'p_value': p-value
                - 'groups': List of group names
                - 'posthoc_method': 'Tukey HSD'
                - 'posthoc_results': Post-hoc test results
            For Kruskal-Wallis:
                - 'h_statistic': H-statistic value
                - 'p_value': p-value
                - 'groups': List of group names
                - 'posthoc_method': 'Mann-Whitney U'
                - 'posthoc_results': Post-hoc test results
            For Friedman:
                - 'statistic': Test statistic
                - 'p_value': p-value
                - 'groups': List of group names
                - 'posthoc_method': 'Wilcoxon'
                - 'posthoc_results': Post-hoc test results
        """
        # Validation (delegated to validator)
        DataValidator.validate_data(data)
        DataValidator.validate_columns(data, [group_col, value_col])
        
        # Store state
        self.data = data
        
        # Computation (delegated to algorithm layer)
        if test_type == "anova":
            self.result = variance_algos.compute_anova_with_posthoc(data, group_col, value_col)
        elif test_type == "kruskal":
            self.result = variance_algos.compute_kruskal_with_posthoc(data, group_col, value_col)
        elif test_type == "friedman":
            self.result = variance_algos.compute_friedman_test(data, group_col, value_col)
        else:
            raise ValueError(
                f"Unsupported test type: {test_type}. "
                f"Supported types are: 'anova', 'kruskal', 'friedman'."
            )
        
        return self.result
