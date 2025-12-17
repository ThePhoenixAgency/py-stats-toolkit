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

tags : module, stats
"""
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.preprocessing import StandardScaler

from ...utils.parallel import ParallelProcessor
from ..core.AbstractClassBase import StatisticalModule


class FactorielleModule(StatisticalModule):
    """Module pour l'analyse factorielle."""

    def __init__(self, n_jobs: int = -1):
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

    def process(self, data, method="pca", n_components=None, **kwargs):
        """
        Effectue une analyse factorielle.

        Args:
            data: DataFrame avec les données
            method: Méthode d'analyse ('pca', 'fa')
            n_components: Nombre de composantes à extraire
            **kwargs: Arguments additionnels
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
        self.validate_data(data)

        # Standardisation des données
        X = self.scaler.fit_transform(data)

        if method == "pca":
            return self._pca(X, data.columns, n_components, **kwargs)
        elif method == "fa":
            return self._factor_analysis(X, data.columns, n_components, **kwargs)
        else:
            raise ValueError(f"Méthode {method} non supportée")

    def _pca(self, X, feature_names, n_components, **kwargs):
        """Analyse en composantes principales."""
        if n_components is None:
            n_components = min(X.shape)

        pca = PCA(n_components=n_components, **kwargs)
        pca.fit(X)

        # Calcul des composantes
        components = pca.transform(X)

        # Création du DataFrame des composantes
        components_df = pd.DataFrame(
            components, columns=[f"PC{i+1}" for i in range(n_components)]
        )

        # Calcul des contributions des variables
        loadings = pd.DataFrame(
            pca.components_.T,
            columns=[f"PC{i+1}" for i in range(n_components)],
            index=feature_names,
        )

        self.result = {
            "Type": "ACP",
            "Composantes": components_df,
            "Loadings": loadings,
            "Variance expliquée": pca.explained_variance_ratio_,
            "Variance cumulée": np.cumsum(pca.explained_variance_ratio_),
            "Modèle": pca,
        }

        return self.result

    def _factor_analysis(self, X, feature_names, n_components, **kwargs):
        """Analyse factorielle."""
        if n_components is None:
            n_components = min(X.shape)

        fa = FactorAnalysis(n_components=n_components, **kwargs)
        fa.fit(X)

        # Calcul des facteurs
        factors = fa.transform(X)

        # Création du DataFrame des facteurs
        factors_df = pd.DataFrame(
            factors, columns=[f"F{i+1}" for i in range(n_components)]
        )

        # Calcul des contributions des variables
        loadings = pd.DataFrame(
            fa.components_.T,
            columns=[f"F{i+1}" for i in range(n_components)],
            index=feature_names,
        )

        self.result = {
            "Type": "Analyse factorielle",
            "Facteurs": factors_df,
            "Loadings": loadings,
            "Noise variance": fa.noise_variance_,
            "Modèle": fa,
        }

        return self.result

        DataValidator.validate_data(data)
        DataValidator.validate_numeric(data)

        if not isinstance(data, pd.DataFrame):
            raise TypeError("FactorielleModule requires a DataFrame")
from ..core.AbstractClassBase import StatisticalModule
from ...utils.parallel import ParallelProcessor

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
    
    def get_quality_metrics(self):
        """
        Calcule les métriques de qualité de l'analyse.

        Returns:
            Métriques de qualité
        """
        if not hasattr(self, "result"):
            raise ValueError("Aucune analyse n'a été effectuée")

        if self.result["Type"] == "ACP":
            return {
                "Variance expliquée par composante": {
                    f"PC{i+1}": val
                    for i, val in enumerate(self.result["Variance expliquée"])
                },
                "Variance cumulée": {
                    f"PC{i+1}": val
                    for i, val in enumerate(self.result["Variance cumulée"])
                },
                "Nombre de composantes pour 80% de variance": np.argmax(
                    self.result["Variance cumulée"] >= 0.8
                )
                + 1,
            }
        else:
            return {
                "Variance du bruit": self.result["Noise variance"].tolist(),
                "Qualité de l'ajustement": 1 - np.mean(self.result["Noise variance"]),
            }

    def transform(self, new_data):
        """
        Transforme de nouvelles données.

        Args:
            new_data: Nouvelles données à transformer

        Returns:
            Données transformées
        """
        if not hasattr(self, "result"):
            raise ValueError("Aucune analyse n'a été effectuée")

        # Standardisation des nouvelles données
        X_new = self.scaler.transform(new_data)

        # Transformation selon la méthode utilisée
        if self.result["Type"] == "ACP":
            return pd.DataFrame(
                self.result["Modèle"].transform(X_new),
                columns=[
                    f"PC{i+1}" for i in range(self.result["Modèle"].n_components_)
                ],
            )
        else:
            return pd.DataFrame(
                self.result["Modèle"].transform(X_new),
                columns=[f"F{i+1}" for i in range(self.result["Modèle"].n_components_)],
            )

    def get_contributions(self, threshold=0.5):
        """
        Obtient les contributions significatives des variables.

        Args:
            threshold: Seuil de contribution
        Transform new data using the fitted model.

        Args:
            new_data: New data to transform

        Returns:
            Transformed data
        """
        if not hasattr(self, "result"):
            raise ValueError("Aucune analyse n'a été effectuée")

        loadings = self.result["Loadings"]
        contributions = {}

        for col in loadings.columns:
            significant_vars = loadings[col][abs(loadings[col]) >= threshold]
            if not significant_vars.empty:
                contributions[col] = significant_vars.to_dict()

        return contributions
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
