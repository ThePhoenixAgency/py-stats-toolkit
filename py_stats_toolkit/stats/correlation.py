"""
Correlation analysis module.

Provides the CorrelationAnalysis class for computing correlations between variables.
"""

from typing import Any, Dict, Union

import numpy as np
import pandas as pd
from scipy import stats


class CorrelationAnalysis:
    """
    Correlation analysis class.

    Computes correlation coefficients between variables with support for
    different correlation methods (Pearson, Spearman, Kendall).
    """

    def __init__(self, method: str = "pearson"):
        """
        Initialize CorrelationAnalysis.

        Args:
            method: Correlation method ('pearson', 'spearman', or 'kendall')
        """
        valid_methods = {"pearson", "spearman", "kendall"}
        if method not in valid_methods:
            raise ValueError(f"Method must be one of {valid_methods}, got '{method}'")
        self.method = method

    def analyze(
        self,
        data: Union[pd.DataFrame, pd.Series, np.ndarray],
        y: Union[pd.Series, np.ndarray, None] = None,
    ) -> Dict[str, Any]:
        """
        Perform correlation analysis.

        Args:
            data: Input data (DataFrame, Series, or array)
            y: Optional second variable for bivariate correlation

        Returns:
            Dictionary containing correlation results
        """
        # Univariate case (single variable correlation with itself or autocorrelation)
        if y is None and isinstance(data, (pd.Series, np.ndarray)):
            if isinstance(data, pd.Series):
                data_array = data.values
            else:
                data_array = data

            return {"correlation": 1.0, "method": self.method, "n": len(data_array)}

        # DataFrame case - compute correlation matrix
        if isinstance(data, pd.DataFrame):
            if self.method == "pearson":
                corr_matrix = data.corr(method="pearson")
            elif self.method == "spearman":
                corr_matrix = data.corr(method="spearman")
            elif self.method == "kendall":
                corr_matrix = data.corr(method="kendall")
            else:
                raise ValueError(f"Unknown correlation method: {self.method}")

            return {"correlation_matrix": corr_matrix, "method": self.method}

        # Bivariate case
        if y is not None:
            if isinstance(data, pd.Series):
                data = data.values
            if isinstance(y, pd.Series):
                y = y.values

            data = np.array(data) if not isinstance(data, np.ndarray) else data
            y = np.array(y) if not isinstance(y, np.ndarray) else y

            if self.method == "pearson":
                corr, pval = stats.pearsonr(data, y)
            elif self.method == "spearman":
                corr, pval = stats.spearmanr(data, y)
            elif self.method == "kendall":
                corr, pval = stats.kendalltau(data, y)
            else:
                raise ValueError(f"Unknown correlation method: {self.method}")

            return {
                "correlation": corr,
                "p_value": pval,
                "method": self.method,
                "n": len(data),
            }

        raise ValueError(
            "Invalid input: provide either a DataFrame or two arrays/Series"
        )
