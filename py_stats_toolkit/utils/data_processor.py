"""Data processing utilities."""

from typing import Union

import numpy as np
import pandas as pd


class DataProcessor:
    """Utility class for data processing and transformation."""

    @staticmethod
    def to_numpy(data: Union[pd.DataFrame, pd.Series, np.ndarray, list]) -> np.ndarray:
        """Convert data to numpy array."""
        if isinstance(data, np.ndarray):
            return data
        elif isinstance(data, pd.Series):
            return data.values
        elif isinstance(data, pd.DataFrame):
            return data.values
        elif isinstance(data, list):
            return np.array(data)
        else:
            raise TypeError(f"Cannot convert {type(data).__name__} to numpy array")

    @staticmethod
    def to_series(data: Union[pd.DataFrame, pd.Series, np.ndarray, list],
                  name: str = None, index=None) -> pd.Series:
        """Convert data to pandas Series."""
        if isinstance(data, pd.Series):
            return data
        elif isinstance(data, pd.DataFrame):
            if len(data.columns) == 1:
                return data.iloc[:, 0]
            else:
                raise ValueError("DataFrame has multiple columns, cannot convert to Series")
        elif isinstance(data, (np.ndarray, list)):
            return pd.Series(data, name=name, index=index)
        else:
            raise TypeError(f"Cannot convert {type(data).__name__} to pandas Series")

    @staticmethod
    def to_dataframe(data: Union[pd.DataFrame, pd.Series, np.ndarray, list],
                     columns=None) -> pd.DataFrame:
        """Convert data to pandas DataFrame."""
        if isinstance(data, pd.DataFrame):
            return data
        elif isinstance(data, pd.Series):
            return data.to_frame()
        elif isinstance(data, (np.ndarray, list)):
            return pd.DataFrame(data, columns=columns)
        else:
            raise TypeError(f"Cannot convert {type(data).__name__} to pandas DataFrame")
