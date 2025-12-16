"""Pure descriptive statistics algorithms."""

from typing import Any, Dict

import numpy as np
import pandas as pd


def compute_moving_average(data: np.ndarray, window_size: int) -> np.ndarray:
    """Compute moving average."""
    series = pd.Series(data)
    return series.rolling(window=window_size).mean().values


def compute_descriptive_statistics(data: np.ndarray) -> Dict[str, Any]:
    """Compute descriptive statistics."""
    return {
        'count': len(data),
        'mean': np.mean(data),
        'std': np.std(data),
        'min': np.min(data),
        'max': np.max(data),
        'median': np.median(data),
        'q25': np.percentile(data, 25),
        'q75': np.percentile(data, 75)
    }


def compute_frequency_distribution(data: np.ndarray, normalize: bool = False) -> pd.DataFrame:
    """Compute frequency distribution."""
    series = pd.Series(data)
    freq = series.value_counts(normalize=normalize)
    cum_freq = freq.cumsum()
    
    result = pd.DataFrame({
        'Frequency': freq,
        'Cumulative_Frequency': cum_freq
    })
    
    if normalize:
        result.columns = ['Relative_Frequency', 'Relative_Cumulative_Frequency']
    
    return result
