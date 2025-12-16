"""
=====================================================================
File : RegressionModule.py
=====================================================================
version : 2.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Refactored module for regression analysis.
Follows SOLID principles with separation of business logic and algorithms.

tags : module, stats, refactored
=====================================================================
"""

from typing import Any, Dict, List, Union

import numpy as np
import pandas as pd

from py_stats_toolkit.algorithms import regression as regression_algos
from py_stats_toolkit.core.base import StatisticalModule
from py_stats_toolkit.core.validators import DataValidator


class RegressionModule(StatisticalModule):
    """
    Module for regression analysis (Business Logic Layer).

    Responsibilities:
    - Orchestrate regression workflow
    - Manage results and state
    - Provide user-facing API

    Delegates to:
    - DataValidator for validation
    - regression_algos for computations
    """

    def __init__(self):
        """Initialize regression module."""
        super().__init__()

    def process(self, data: pd.DataFrame, x_cols: List[str], y_col: str,
                regression_type: str = "linear", **kwargs) -> Dict[str, Any]:
        """
        Perform regression analysis.

        Args:
            data: DataFrame with data
            x_cols: List of feature column names
            y_col: Target column name
            regression_type: Type of regression ('linear', 'ridge', 'lasso', 'polynomial')
            **kwargs: Additional arguments (alpha for ridge/lasso, degree for polynomial)

        Returns:
            Dictionary with regression results containing:
            - 'coefficients': Regression coefficients
            - 'intercept': Intercept value
            - 'r2_score': R-squared score
            - 'predictions': Predicted values
            - 'residuals': Residual values
            - 'model': Fitted model object
            - 'regression_type': Type of regression performed
            - Additional keys depending on regression type
        """
        # Validation (delegated to validator)
        DataValidator.validate_data(data)
        DataValidator.validate_columns(data, x_cols + [y_col])

        # Extract features and target
        X = data[x_cols].values
        y = data[y_col].values

        # Store state
        self.data = data

        # Computation (delegated to algorithm layer)
        if regression_type == "linear":
            result = regression_algos.compute_linear_regression(X, y)
        elif regression_type == "ridge":
            alpha = kwargs.get('alpha', 1.0)
            result = regression_algos.compute_ridge_regression(X, y, alpha)
        elif regression_type == "lasso":
            alpha = kwargs.get('alpha', 1.0)
            result = regression_algos.compute_lasso_regression(X, y, alpha)
        elif regression_type == "polynomial":
            degree = kwargs.get('degree', 2)
            result = regression_algos.compute_polynomial_regression(X, y, degree)
        else:
            raise ValueError(
                f"Unsupported regression type: {regression_type}. "
                f"Supported types are: 'linear', 'ridge', 'lasso', 'polynomial'."
            )

        # Format results with column names
        result['regression_type'] = regression_type
        if regression_type != 'polynomial':
            result['coefficients'] = dict(zip(x_cols, result['coefficients']))

        self.result = result
        return self.result

    def predict(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """
        Make predictions with the trained model.

        Args:
            X: Feature data

        Returns:
            Predictions
        """
        if not self.has_result():
            raise ValueError("No model has been trained. Call process() first.")

        # Convert to numpy if needed
        if isinstance(X, pd.DataFrame):
            X = X.values

        model = self.result['model']

        # Apply transformation for polynomial regression
        if self.result['regression_type'] == 'polynomial':
            X = self.result['transformer'].transform(X)

        return model.predict(X)

    def get_residuals_analysis(self) -> Dict[str, Any]:
        """
        Analyze residuals.

        Returns:
            Residual statistics
        """
        if not self.has_result():
            raise ValueError("No analysis performed. Call process() first.")

        residuals = self.result['residuals']

        # Delegate computation to algorithm layer
        return regression_algos.compute_residuals_analysis(residuals)
