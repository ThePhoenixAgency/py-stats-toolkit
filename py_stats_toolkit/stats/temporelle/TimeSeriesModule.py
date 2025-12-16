"""
=====================================================================
File : TimeSeriesModule.py
=====================================================================
version : 2.0.0 (Refactored)
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Refactored module for time series analysis.
Follows SOLID principles with separation of business logic and algorithms.

tags : module, stats, refactored
=====================================================================
"""

from typing import Any, Dict, Union

import numpy as np
import pandas as pd

from py_stats_toolkit.core.base import StatisticalModule
from py_stats_toolkit.core.validators import DataValidator


class TimeSeriesModule(StatisticalModule):
    """
    Module for time series analysis (Business Logic Layer).

    Provides basic time series analysis including:
    - Rolling statistics (mean, std, min, max)
    - Trend detection
    - Seasonality detection (basic)
    """

    def __init__(self):
        """Initialize time series module."""
        super().__init__()
        self.timestamps = None

    def process(self, data: Union[pd.DataFrame, pd.Series],
                window: int = 7, **kwargs) -> Dict[str, Any]:
        """
        Process time series data.

        Args:
            data: Time series data (Series or DataFrame with time index)
            window: Window size for rolling statistics
            **kwargs: Additional arguments

        Returns:
            Dictionary with analysis results containing:
            - 'rolling_mean': Rolling mean
            - 'rolling_std': Rolling standard deviation
            - 'trend': Linear trend coefficient
            - 'summary': Statistical summary
        """
        DataValidator.validate_data(data)
        self.data = data

        # Convert to Series if DataFrame with single column
        if isinstance(data, pd.DataFrame):
            if len(data.columns) == 1:
                series = data.iloc[:, 0]
            else:
                raise ValueError(
                    "TimeSeriesModule requires a single time series. "
                    f"Got DataFrame with {len(data.columns)} columns."
                )
        else:
            series = data

        # Calculate rolling statistics
        rolling_mean = series.rolling(window=window).mean()
        rolling_std = series.rolling(window=window).std()
        rolling_min = series.rolling(window=window).min()
        rolling_max = series.rolling(window=window).max()

        # Calculate trend (simple linear regression on index)
        x = np.arange(len(series))
        y = series.values

        # Remove NaN values for trend calculation
        mask = ~np.isnan(y)
        if np.sum(mask) > 1:
            trend_coef = np.polyfit(x[mask], y[mask], 1)[0]
        else:
            trend_coef = 0.0

        # Statistical summary
        summary = {
            'mean': float(series.mean()),
            'std': float(series.std()),
            'min': float(series.min()),
            'max': float(series.max()),
            'count': int(series.count())
        }

        self.result = {
            'rolling_mean': rolling_mean,
            'rolling_std': rolling_std,
            'rolling_min': rolling_min,
            'rolling_max': rolling_max,
            'trend_coefficient': trend_coef,
            'summary': summary
        }

        return self.result

    def get_rolling_stats(self) -> pd.DataFrame:
        """
        Get rolling statistics as a DataFrame.

        Returns:
            DataFrame with rolling statistics
        """
        if not self.has_result():
            raise ValueError("No analysis performed. Call process() first.")

        return pd.DataFrame({
            'rolling_mean': self.result['rolling_mean'],
            'rolling_std': self.result['rolling_std'],
            'rolling_min': self.result['rolling_min'],
            'rolling_max': self.result['rolling_max']
        })
