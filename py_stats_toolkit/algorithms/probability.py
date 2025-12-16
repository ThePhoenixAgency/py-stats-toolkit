"""Pure probability algorithms."""

from typing import Any, Dict, Tuple

import numpy as np
from scipy import stats


def fit_normal_distribution(data: np.ndarray) -> Tuple[float, float]:
    """Fit normal distribution to data."""
    return stats.norm.fit(data)


def fit_exponential_distribution(data: np.ndarray) -> Tuple[float, float]:
    """Fit exponential distribution to data."""
    return stats.expon.fit(data)


def fit_gamma_distribution(data: np.ndarray) -> Tuple:
    """Fit gamma distribution to data."""
    return stats.gamma.fit(data)


def compute_pdf(distribution_type: str, params: Tuple, x: np.ndarray) -> np.ndarray:
    """Compute probability density function."""
    if distribution_type == 'normal':
        dist = stats.norm(*params)
    elif distribution_type == 'exponential':
        dist = stats.expon(*params)
    elif distribution_type == 'gamma':
        dist = stats.gamma(*params)
    else:
        raise ValueError(f"Unknown distribution: {distribution_type}")
    
    return dist.pdf(x)


def compute_cdf(distribution_type: str, params: Tuple, x: np.ndarray) -> np.ndarray:
    """Compute cumulative distribution function."""
    if distribution_type == 'normal':
        dist = stats.norm(*params)
    elif distribution_type == 'exponential':
        dist = stats.expon(*params)
    elif distribution_type == 'gamma':
        dist = stats.gamma(*params)
    else:
        raise ValueError(f"Unknown distribution: {distribution_type}")
    
    return dist.cdf(x)


def fit_distribution(data: np.ndarray, distribution_type: str) -> Dict[str, Any]:
    """Fit a distribution to data and return results."""
    if distribution_type == 'normal':
        params = fit_normal_distribution(data)
        dist = stats.norm(*params)
    elif distribution_type == 'exponential':
        params = fit_exponential_distribution(data)
        dist = stats.expon(*params)
    elif distribution_type == 'gamma':
        params = fit_gamma_distribution(data)
        dist = stats.gamma(*params)
    else:
        raise ValueError(f"Unknown distribution: {distribution_type}")
    
    return {
        'distribution': dist,
        'params': params,
        'type': distribution_type
    }
