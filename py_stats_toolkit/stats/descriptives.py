"""
Statistics descriptives module.

Provides the DescriptiveStatistics class for computing descriptive
statistics on various data types (lists, arrays, Series, DataFrames).
"""

from typing import Any, Dict, Union

import numpy as np
import pandas as pd


class DescriptiveStatistics:
    """
    Class for computing descriptive statistics.

    Handles various data types and provides comprehensive statistical measures
    including central tendency, dispersion, and percentiles.
    """

    def __init__(self):
        """Initialize DescriptiveStatistics."""
        pass

    def analyze(
        self, data: Union[list, np.ndarray, pd.Series, pd.DataFrame]
    ) -> Dict[str, Any]:
        """
        Analyze data and compute descriptive statistics.

        Args:
            data: Input data (list, array, Series, or DataFrame)

        Returns:
            Dictionary containing statistical measures
        """
        if isinstance(data, list):
            data = np.array(data)
        elif isinstance(data, pd.Series):
            data = data.values
        elif isinstance(data, pd.DataFrame):
            if len(data.columns) == 1:
                data = data.iloc[:, 0].values
            else:
                return {col: self.analyze(data[col]) for col in data.columns}

        return {
            "count": len(data),
            "mean": np.mean(data),
            "std": np.std(data),
            "min": np.min(data),
            "max": np.max(data),
            "median": np.median(data),
            "q25": np.percentile(data, 25),
            "q75": np.percentile(data, 75),
        }
