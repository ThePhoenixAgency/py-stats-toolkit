"""Parallel processing utilities."""

import multiprocessing
from typing import Any, Callable, List

import numpy as np


def get_optimal_chunk_size(n_items: int, n_jobs: int) -> int:
    """Calculate optimal chunk size for parallel processing."""
    if n_jobs <= 0:
        n_jobs = multiprocessing.cpu_count()
    return max(1, n_items // n_jobs)


class ParallelProcessor:
    """Utility for parallel processing operations."""

    def __init__(self, n_jobs: int = -1):
        """Initialize parallel processor."""
        if n_jobs == -1:
            self.n_jobs = multiprocessing.cpu_count()
        else:
            self.n_jobs = max(1, n_jobs)

    def parallel_map(self, func: Callable, items: List[Any]) -> List[Any]:
        """Apply function to items in parallel."""
        if len(items) < 100:
            return [func(item) for item in items]

        try:
            with multiprocessing.Pool(processes=self.n_jobs) as pool:
                return pool.map(func, items)
        except Exception:
            return [func(item) for item in items]

    def parallel_apply(self, func: Callable, data: np.ndarray, axis: int = 0) -> np.ndarray:
        """Apply function along axis in parallel."""
        if data.size < 1000:
            return np.apply_along_axis(func, axis, data)

        splits = np.array_split(data, self.n_jobs, axis=axis)
        results = self.parallel_map(lambda s: np.apply_along_axis(func, axis, s), splits)
        return np.concatenate(results, axis=axis)


class BatchProcessor:
    """Utility for batch processing of large datasets."""

    def __init__(self, batch_size: int = 1000):
        """Initialize batch processor."""
        self.batch_size = max(1, batch_size)

    def process_batches(self, func: Callable, data: np.ndarray) -> np.ndarray:
        """Process data in batches."""
        n_batches = (len(data) + self.batch_size - 1) // self.batch_size
        results = []

        for i in range(n_batches):
            start_idx = i * self.batch_size
            end_idx = min((i + 1) * self.batch_size, len(data))
            batch = data[start_idx:end_idx]
            results.append(func(batch))

        if isinstance(results[0], np.ndarray):
            return np.concatenate(results)
        elif hasattr(results[0], 'values'):
            import pandas as pd
            return pd.concat(results)
        else:
            return results
