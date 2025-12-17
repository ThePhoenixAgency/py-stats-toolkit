"""Pure correlation algorithms."""

from typing import List, Tuple

import numpy as np
import pandas as pd
from scipy import stats


def compute_correlation_matrix(data: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    """Compute correlation matrix."""
    return data.corr(method=method)


def compute_pairwise_correlations(data: pd.DataFrame, method: str = "pearson",
                                  threshold: float = 0.0) -> List[Tuple[str, str, float]]:
    """Compute pairwise correlations above threshold."""
    corr_matrix = compute_correlation_matrix(data, method)
    n = len(corr_matrix.columns)

    i, j = np.triu_indices(n, k=1)
    corr_values = corr_matrix.values[i, j]

    mask = np.abs(corr_values) >= threshold
    pairs = []

    for idx in np.where(mask)[0]:
        var1 = corr_matrix.columns[i[idx]]
        var2 = corr_matrix.columns[j[idx]]
        corr = corr_values[idx]
        pairs.append((var1, var2, corr))

    return sorted(pairs, key=lambda x: abs(x[2]), reverse=True)


def compute_correlation_test(x: np.ndarray, y: np.ndarray,
                             method: str = "pearson") -> Tuple[float, float]:
    """Compute correlation coefficient and p-value."""
    if method == "pearson":
        return stats.pearsonr(x, y)
    elif method == "spearman":
        return stats.spearmanr(x, y)
    elif method == "kendall":
        return stats.kendalltau(x, y)
    else:
        raise ValueError(f"Unknown method: {method}")
