"""
=====================================================================
File : BaseCapsule.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module BaseCapsule.py

Base class for all statistical analysis capsules/modules.
Provides common interface and functionality for data processing.

tags : module, base, capsule
=====================================================================
"""

from typing import Any, Dict, Union

import numpy as np
import pandas as pd


class BaseCapsule:
    """
    Base class for all statistical analysis modules.

    Provides common interface for data validation, configuration,
    and processing workflow.

    Attributes:
        data: Input data being processed
        parameters: Configuration parameters
        result: Analysis results
    """

    def __init__(self):
        """Initialize BaseCapsule with default attributes."""
        self.data = None
        self.parameters = {}
        self.result = None

    def configure(self, **kwargs) -> None:
        """
        Configure the module parameters.

        Args:
            **kwargs: Configuration parameters
        """
        self.parameters.update(kwargs)

    def validate_data(
        self, data: Union[pd.DataFrame, pd.Series, np.ndarray, list]
    ) -> None:
        """
        Validate input data.

        Args:
            data: Data to validate

        Raises:
            ValueError: If data is invalid
        """
        if data is None:
            raise ValueError("Data cannot be None")

        if isinstance(data, (pd.DataFrame, pd.Series)):
            if data.empty:
                raise ValueError("Data cannot be empty")
        elif isinstance(data, (np.ndarray, list)):
            if len(data) == 0:
                raise ValueError("Data cannot be empty")
        else:
            # Try to convert to array-like
            try:
                data_array = np.array(data)
                if data_array.size == 0:
                    raise ValueError("Data cannot be empty")
            except Exception as e:
                raise ValueError(f"Invalid data type: {type(data)}. Error: {e}")

    def process(
        self, data: Union[pd.DataFrame, pd.Series, np.ndarray], **kwargs
    ) -> Dict[str, Any]:
        """
        Process data and perform analysis.

        This method should be overridden by subclasses.

        Args:
            data: Input data to process
            **kwargs: Additional processing parameters

        Returns:
            Dict[str, Any]: Analysis results
        """
        raise NotImplementedError("Subclasses must implement the process method")

    def get_result(self) -> Any:
        """
        Get the analysis result.

        Returns:
            Analysis result
        """
        return self.result

    def reset(self) -> None:
        """Reset the module to initial state."""
        self.data = None
        self.parameters = {}
        self.result = None
