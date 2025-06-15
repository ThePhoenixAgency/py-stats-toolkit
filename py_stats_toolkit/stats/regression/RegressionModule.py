'''
=====================================================================
File : RegressionModule.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module RegressionModule.py

tags : module, stats
=====================================================================
Ce module Description du module RegressionModule.py

tags : module, stats
=====================================================================
'''

# Imports spécifiques au module
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

# Imports de la base
from capsules.BaseCapsule import BaseCapsule

class RegressionModule(BaseCapsule):
    """
    Classe RegressionModule
    
    Attributes:
        data, parameters, results
    """
    
    def __init__(self):
        """
        Initialise RegressionModule.
        """
        super().__init__()
        pass
    
    def configure(self, **kwargs) -> None:
        """
        Configure les paramètres de RegressionModule.
        
        Args:
            **kwargs: Paramètres de configuration
        """
        pass
    
    def process(self, data: Union[pd.DataFrame, pd.Series], **kwargs) -> Dict[str, Any]:
        """
        Exécute le flux de travail d'analyse.
        
        Args:
            data (Union[pd.DataFrame, pd.Series]): Données à analyser
            **kwargs: Arguments additionnels
            
        Returns:
            Dict[str, Any]: Résultats de l'analyse
        """
        pass 

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from ..core.AbstractClassBase import StatisticalModule
from ...utils.parallel import ParallelProcessor

class RegressionModule(StatisticalModule):
    """Module pour l'analyse de régression."""
    
    def __init__(self, n_jobs: int = -1):
        super().__init__()
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)
    
    def process(self, data, x_cols, y_col, regression_type="linear", **kwargs):
        """
        Effectue une analyse de régression.
        
        Args:
            data: DataFrame avec les données
            x_cols: Liste des colonnes prédictives
            y_col: Colonne cible
            regression_type: Type de régression ('linear', 'ridge', 'lasso', 'polynomial')
            **kwargs: Arguments additionnels pour le modèle
            
        Returns:
            Résultats de la régression
        """
        self.validate_data(data)
        
        X = data[x_cols]
        y = data[y_col]
        
        if regression_type == "linear":
            return self._linear_regression(X, y, **kwargs)
        elif regression_type == "ridge":
            return self._ridge_regression(X, y, **kwargs)
        elif regression_type == "lasso":
            return self._lasso_regression(X, y, **kwargs)
        elif regression_type == "polynomial":
            return self._polynomial_regression(X, y, **kwargs)
        else:
            raise ValueError(f"Type de régression {regression_type} non supporté")
    
    def _linear_regression(self, X, y, **kwargs):
        """Régression linéaire simple."""
        model = LinearRegression(**kwargs)
        model.fit(X, y)
        
        y_pred = model.predict(X)
        residuals = y - y_pred
        
        self.result = {
            'Type': 'Régression linéaire',
            'Coefficients': dict(zip(X.columns, model.coef_)),
            'Intercept': model.intercept_,
            'R2': model.score(X, y),
            'Prédictions': y_pred,
            'Résidus': residuals,
            'Modèle': model
        }
        
        return self.result
    
    def _ridge_regression(self, X, y, alpha=1.0, **kwargs):
        """Régression Ridge."""
        model = Ridge(alpha=alpha, **kwargs)
        model.fit(X, y)
        
        y_pred = model.predict(X)
        residuals = y - y_pred
        
        self.result = {
            'Type': 'Régression Ridge',
            'Coefficients': dict(zip(X.columns, model.coef_)),
            'Intercept': model.intercept_,
            'R2': model.score(X, y),
            'Alpha': alpha,
            'Prédictions': y_pred,
            'Résidus': residuals,
            'Modèle': model
        }
        
        return self.result
    
    def _lasso_regression(self, X, y, alpha=1.0, **kwargs):
        """Régression Lasso."""
        model = Lasso(alpha=alpha, **kwargs)
        model.fit(X, y)
        
        y_pred = model.predict(X)
        residuals = y - y_pred
        
        self.result = {
            'Type': 'Régression Lasso',
            'Coefficients': dict(zip(X.columns, model.coef_)),
            'Intercept': model.intercept_,
            'R2': model.score(X, y),
            'Alpha': alpha,
            'Prédictions': y_pred,
            'Résidus': residuals,
            'Modèle': model
        }
        
        return self.result
    
    def _polynomial_regression(self, X, y, degree=2, **kwargs):
        """Régression polynomiale."""
        poly = PolynomialFeatures(degree=degree)
        X_poly = poly.fit_transform(X)
        
        model = LinearRegression(**kwargs)
        model.fit(X_poly, y)
        
        y_pred = model.predict(X_poly)
        residuals = y - y_pred
        
        self.result = {
            'Type': 'Régression polynomiale',
            'Coefficients': model.coef_,
            'Intercept': model.intercept_,
            'R2': model.score(X_poly, y),
            'Degré': degree,
            'Prédictions': y_pred,
            'Résidus': residuals,
            'Modèle': model,
            'Transformateur': poly
        }
        
        return self.result
    
    def predict(self, X):
        """
        Fait des prédictions avec le modèle entraîné.
        
        Args:
            X: Données pour la prédiction
            
        Returns:
            Prédictions
        """
        if not hasattr(self, 'result'):
            raise ValueError("Aucun modèle n'a été entraîné")
        
        model = self.result['Modèle']
        
        if self.result['Type'] == 'Régression polynomiale':
            X = self.result['Transformateur'].transform(X)
        
        return model.predict(X)
    
    def get_residuals_analysis(self):
        """
        Analyse des résidus.
        
        Returns:
            Statistiques sur les résidus
        """
        if not hasattr(self, 'result'):
            raise ValueError("Aucun modèle n'a été entraîné")
        
        residuals = self.result['Résidus']
        
        return {
            'Moyenne': np.mean(residuals),
            'Écart-type': np.std(residuals),
            'Skewness': stats.skew(residuals),
            'Kurtosis': stats.kurtosis(residuals),
            'Test de normalité': stats.normaltest(residuals)
        } 