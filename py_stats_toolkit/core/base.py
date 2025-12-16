"""Base classes for statistical modules."""

from abc import ABC, abstractmethod
from typing import Any, Optional, Union

import numpy as np
import pandas as pd


class StatisticalModule(ABC):
    """Abstract base class for all statistical modules."""
    
    def __init__(self):
        """Initialize the statistical module."""
        self.result: Optional[Any] = None
        self.data: Optional[Any] = None
    
    @abstractmethod
    def process(self, data: Union[pd.DataFrame, pd.Series, np.ndarray], **kwargs) -> Any:
        """Process data and perform statistical analysis."""
        pass
    
    def get_result(self) -> Any:
        """Get the result of the last analysis."""
        if self.result is None:
            raise ValueError("No analysis has been performed yet. Call process() first.")
        return self.result
    
    def has_result(self) -> bool:
        """Check if a result is available."""
        return self.result is not None
