"""
Linear regression module.

Provides the LinearRegression class for performing linear regression analysis.
"""

from typing import Any, Dict, Union

import numpy as np
from sklearn.linear_model import LinearRegression as SKLearnLinearRegression
from sklearn.metrics import mean_squared_error, r2_score


class LinearRegression:
    """
    Linear regression analysis class.

    Provides methods for fitting linear regression models and making predictions.
    """

    def __init__(self):
        """Initialize LinearRegression."""
        self.model = SKLearnLinearRegression()
        self.is_fitted = False

    def fit(
        self, X: Union[np.ndarray, list], y: Union[np.ndarray, list]
    ) -> "LinearRegression":
        """
        Fit the linear regression model.

        Args:
            X: Feature matrix
            y: Target vector

        Returns:
            Self for method chaining
        """
        X = np.array(X) if not isinstance(X, np.ndarray) else X
        y = np.array(y) if not isinstance(y, np.ndarray) else y

        self.model.fit(X, y)
        self.is_fitted = True
        return self

    def predict(self, X: Union[np.ndarray, list]) -> np.ndarray:
        """
        Make predictions using the fitted model.

        Args:
            X: Feature matrix

        Returns:
            Predicted values

        Raises:
            RuntimeError: If model hasn't been fitted
        """
        if not self.is_fitted:
            raise RuntimeError("Model must be fitted before making predictions")

        X = np.array(X) if not isinstance(X, np.ndarray) else X
        return self.model.predict(X)

    def analyze(
        self, X: Union[np.ndarray, list], y: Union[np.ndarray, list]
    ) -> Dict[str, Any]:
        """
        Perform complete regression analysis.

        Args:
            X: Feature matrix
            y: Target vector

        Returns:
            Dictionary containing regression results and metrics
        """
        self.fit(X, y)
        predictions = self.predict(X)

        return {
            "coefficients": self.model.coef_,
            "intercept": self.model.intercept_,
            "predictions": predictions,
            "mse": mean_squared_error(y, predictions),
            "r2": r2_score(y, predictions),
        }

    @property
    def coef_(self):
        """Get model coefficients."""
        return self.model.coef_ if self.is_fitted else None

    @property
    def intercept_(self):
        """Get model intercept."""
        return self.model.intercept_ if self.is_fitted else None
