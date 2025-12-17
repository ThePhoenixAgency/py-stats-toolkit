"""Data validation utilities."""

from typing import Union

import numpy as np
import pandas as pd


class DataValidator:
    """Validator for statistical data."""

    @staticmethod
    def validate_data(data: Union[pd.DataFrame, pd.Series, np.ndarray, list]) -> None:
        """Validate input data for statistical analysis."""
        if data is None:
            raise ValueError("Data cannot be None")

        if isinstance(data, list):
            if len(data) == 0:
                raise ValueError("Data cannot be empty")
            return

        if isinstance(data, np.ndarray):
            if data.size == 0:
                raise ValueError("Data cannot be empty")
            return

        if isinstance(data, pd.Series):
            if len(data) == 0:
                raise ValueError("Data cannot be empty")
            return

        if isinstance(data, pd.DataFrame):
            if len(data) == 0:
                raise ValueError("Data cannot be empty")
            if len(data.columns) == 0:
                raise ValueError("DataFrame must have at least one column")
            return

        raise TypeError(
            f"Unsupported data type: {type(data).__name__}. "
            f"Supported types: DataFrame, Series, ndarray, list"
        )

    @staticmethod
    def validate_columns(data: pd.DataFrame, columns: list) -> None:
        """Validate that specified columns exist in DataFrame."""
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame")

        missing_cols = [col for col in columns if col not in data.columns]
        if missing_cols:
            raise ValueError(f"Columns not found in DataFrame: {missing_cols}")

    @staticmethod
    def validate_numeric(data: Union[pd.DataFrame, pd.Series, np.ndarray]) -> None:
        """Validate that data is numeric."""
        if isinstance(data, pd.DataFrame):
            non_numeric = data.select_dtypes(exclude=[np.number]).columns.tolist()
            if non_numeric:
                raise TypeError(f"Non-numeric columns found: {non_numeric}")
        elif isinstance(data, pd.Series):
            if not pd.api.types.is_numeric_dtype(data):
                raise TypeError("Series must be numeric")
        elif isinstance(data, np.ndarray):
            if not np.issubdtype(data.dtype, np.number):
                raise TypeError("Array must be numeric")
