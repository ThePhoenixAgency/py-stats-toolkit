"""
=====================================================================
File : FactorielleModule.py
=====================================================================
version : 2.0.0 (Refactored)
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Refactored module for factorial analysis (PCA/Factor Analysis).
Follows SOLID principles with separation of business logic and algorithms.

tags : module, stats, refactored
=====================================================================
"""

from typing import Any, Dict, Optional, Union

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.preprocessing import StandardScaler

from py_stats_toolkit.core.base import StatisticalModule
from py_stats_toolkit.core.validators import DataValidator


class FactorielleModule(StatisticalModule):
    """
    Module for factorial analysis (Business Logic Layer).
    
    Provides dimensionality reduction using:
    - PCA (Principal Component Analysis)
    - Factor Analysis
    """
    
    def __init__(self):
        """Initialize factorial module."""
        super().__init__()
        self.scaler = StandardScaler()
        self.model = None
    
    def process(self, data: pd.DataFrame, method: str = "pca", 
                n_components: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        """
        Perform factorial analysis.
        
        Args:
            data: DataFrame with numerical features
            method: Analysis method ('pca' or 'fa' for factor analysis)
            n_components: Number of components to extract (None for all)
            **kwargs: Additional arguments for the model
            
        Returns:
            Dictionary with analysis results containing:
            - 'components': Transformed data
            - 'explained_variance': Variance explained by each component (PCA only)
            - 'loadings': Component loadings
            - 'n_components': Number of components
            - 'method': Method used
        """
        DataValidator.validate_data(data)
        DataValidator.validate_numeric(data)
        
        if not isinstance(data, pd.DataFrame):
            raise TypeError("FactorielleModule requires a DataFrame")
        
        self.data = data
        
        # Standardize data
        X_scaled = self.scaler.fit_transform(data)
        
        # Determine n_components if not specified
        if n_components is None:
            n_components = min(data.shape)
        
        # Choose model based on method
        if method.lower() == "pca":
            self.model = PCA(n_components=n_components, **kwargs)
        elif method.lower() == "fa":
            self.model = FactorAnalysis(n_components=n_components, **kwargs)
        else:
            raise ValueError(
                f"Unsupported method: {method}. "
                f"Supported methods are: 'pca', 'fa'."
            )
        
        # Fit and transform
        components = self.model.fit_transform(X_scaled)
        
        # Create component DataFrame with meaningful column names
        component_names = [f'Component_{i+1}' for i in range(n_components)]
        components_df = pd.DataFrame(
            components,
            columns=component_names,
            index=data.index
        )
        
        # Get loadings (components_ for PCA, components_ for FA)
        loadings = pd.DataFrame(
            self.model.components_.T,
            columns=component_names,
            index=data.columns
        )
        
        # Build result dictionary
        self.result = {
            'components': components_df,
            'loadings': loadings,
            'n_components': n_components,
            'method': method
        }
        
        # Add explained variance for PCA
        if method.lower() == "pca":
            self.result['explained_variance'] = self.model.explained_variance_ratio_
            self.result['cumulative_variance'] = np.cumsum(self.model.explained_variance_ratio_)
        
        return self.result
    
    def transform(self, new_data: pd.DataFrame) -> pd.DataFrame:
        """
        Transform new data using the fitted model.
        
        Args:
            new_data: New data to transform
            
        Returns:
            Transformed data
        """
        if self.model is None:
            raise ValueError("No model fitted. Call process() first.")
        
        X_scaled = self.scaler.transform(new_data)
        components = self.model.transform(X_scaled)
        
        n_components = self.result['n_components']
        component_names = [f'Component_{i+1}' for i in range(n_components)]
        
        return pd.DataFrame(
            components,
            columns=component_names,
            index=new_data.index
        )
