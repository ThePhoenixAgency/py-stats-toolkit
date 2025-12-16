"""Pure regression algorithms."""

from typing import Any, Dict

import numpy as np
from scipy import stats
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures


def compute_linear_regression(X: np.ndarray, y: np.ndarray) -> Dict[str, Any]:
    """Compute linear regression."""
    model = LinearRegression()
    model.fit(X, y)
    
    y_pred = model.predict(X)
    residuals = y - y_pred
    
    return {
        'coefficients': model.coef_,
        'intercept': model.intercept_,
        'r2_score': model.score(X, y),
        'predictions': y_pred,
        'residuals': residuals,
        'model': model
    }


def compute_ridge_regression(X: np.ndarray, y: np.ndarray, alpha: float = 1.0) -> Dict[str, Any]:
    """Compute Ridge regression."""
    model = Ridge(alpha=alpha)
    model.fit(X, y)
    
    y_pred = model.predict(X)
    residuals = y - y_pred
    
    return {
        'coefficients': model.coef_,
        'intercept': model.intercept_,
        'r2_score': model.score(X, y),
        'alpha': alpha,
        'predictions': y_pred,
        'residuals': residuals,
        'model': model
    }


def compute_lasso_regression(X: np.ndarray, y: np.ndarray, alpha: float = 1.0) -> Dict[str, Any]:
    """Compute Lasso regression."""
    model = Lasso(alpha=alpha)
    model.fit(X, y)
    
    y_pred = model.predict(X)
    residuals = y - y_pred
    
    return {
        'coefficients': model.coef_,
        'intercept': model.intercept_,
        'r2_score': model.score(X, y),
        'alpha': alpha,
        'predictions': y_pred,
        'residuals': residuals,
        'model': model
    }


def compute_polynomial_regression(X: np.ndarray, y: np.ndarray, degree: int = 2) -> Dict[str, Any]:
    """Compute polynomial regression."""
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    
    model = LinearRegression()
    model.fit(X_poly, y)
    
    y_pred = model.predict(X_poly)
    residuals = y - y_pred
    
    return {
        'coefficients': model.coef_,
        'intercept': model.intercept_,
        'r2_score': model.score(X_poly, y),
        'degree': degree,
        'predictions': y_pred,
        'residuals': residuals,
        'model': model,
        'transformer': poly
    }


def compute_residuals_analysis(residuals: np.ndarray) -> Dict[str, Any]:
    """Analyze regression residuals."""
    return {
        'mean': np.mean(residuals),
        'std': np.std(residuals),
        'skewness': stats.skew(residuals),
        'kurtosis': stats.kurtosis(residuals),
        'normality_test': stats.normaltest(residuals)
    }
