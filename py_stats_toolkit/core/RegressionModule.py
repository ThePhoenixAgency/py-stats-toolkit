'''
=====================================================================
RegressionModule.py
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

This module defines the regression analysis functionality for the
py_stats_toolkit library. It provides methods for performing various
types of regression analysis, including linear, polynomial, and
multiple regression.

tags : regression, analysis, linear, polynomial, multiple, modeling, prediction
=====================================================================
Ce module définit les fonctionnalités d'analyse de régression pour
la bibliothèque py_stats_toolkit. Il fournit des méthodes pour effectuer
différents types d'analyse de régression, incluant la régression linéaire,
polynomiale et multiple.

tags : régression, analyse, linéaire, polynomiale, multiple, modélisation, prévision
=====================================================================
'''

from abc import abstractmethod
import numpy as np
import pandas as pd
from typing import Any, Dict, List, Optional, Tuple, Union
from .StatisticalModule import StatisticalModule

class RegressionModule(StatisticalModule):
    """
    Module d'analyse de régression.
    
    Cette classe fournit des méthodes pour effectuer différents types
    d'analyse de régression, incluant la régression linéaire, polynomiale
    et multiple.
    
    Attributes:
        data (pd.DataFrame): Données d'entrée
        X (pd.DataFrame): Variables explicatives
        y (pd.Series): Variable à prédire
        model (Any): Modèle de régression
        coefficients (Dict[str, float]): Coefficients du modèle
        metrics (Dict[str, float]): Métriques d'évaluation
        tags (List[str]): Tags associés au module
        version (str): Version du module
    """
    
    def __init__(self):
        """
        Initialise le module d'analyse de régression.
        
        Cette méthode configure les attributs spécifiques à la régression
        et initialise les structures de données nécessaires.
        """
        super().__init__()
        self.data = None
        self.X = None
        self.y = None
        self.model = None
        self.coefficients = {}
        self.metrics = {}
        self.tags.extend(["régression", "modélisation"])
    
    @abstractmethod
    def process(self, data: pd.DataFrame, target: str, **kwargs) -> Dict[str, Any]:
        """
        Effectue l'analyse de régression.
        
        Cette méthode doit être implémentée par les classes filles pour
        effectuer leur type spécifique de régression.
        
        Args:
            data (pd.DataFrame): Données d'entrée
            target (str): Nom de la variable à prédire
            **kwargs: Arguments additionnels spécifiques à la régression
                - features (List[str]): Variables explicatives à utiliser
                - method (str): Méthode de régression à utiliser
                - params (Dict[str, Any]): Paramètres de la méthode
            
        Returns:
            Dict[str, Any]: Résultats de l'analyse
                - coefficients (Dict[str, float]): Coefficients du modèle
                - metrics (Dict[str, float]): Métriques d'évaluation
                - method (str): Méthode utilisée
                - params (Dict[str, Any]): Paramètres utilisés
            
        Raises:
            ValueError: Si les données sont invalides
            TypeError: Si les données ne sont pas dans le bon format
        """
        pass
    
    @abstractmethod
    def predict(self, X: pd.DataFrame) -> pd.Series:
        """
        Effectue des prédictions avec le modèle.
        
        Cette méthode doit être implémentée par les classes filles pour
        effectuer leurs prédictions spécifiques.
        
        Args:
            X (pd.DataFrame): Variables explicatives pour la prédiction
            
        Returns:
            pd.Series: Prédictions du modèle
            
        Raises:
            ValueError: Si le modèle n'a pas été entraîné
            RuntimeError: Si une erreur survient pendant la prédiction
        """
        pass
    
    def get_coefficients(self) -> Dict[str, float]:
        """
        Retourne les coefficients du modèle.
        
        Returns:
            Dict[str, float]: Coefficients du modèle
            
        Raises:
            ValueError: Si le modèle n'a pas été entraîné
        """
        if not self.coefficients:
            raise ValueError("Le modèle n'a pas été entraîné")
        return self.coefficients
    
    def get_metrics(self) -> Dict[str, float]:
        """
        Retourne les métriques d'évaluation du modèle.
        
        Returns:
            Dict[str, float]: Métriques d'évaluation
                - R2: Coefficient de détermination
                - RMSE: Racine de l'erreur quadratique moyenne
                - MAE: Erreur absolue moyenne
            
        Raises:
            ValueError: Si le modèle n'a pas été entraîné
        """
        if not self.metrics:
            raise ValueError("Le modèle n'a pas été entraîné")
        return self.metrics
    
    def validate_data(self) -> bool:
        """
        Valide les données d'entrée.
        
        Returns:
            bool: True si les données sont valides
            
        Raises:
            ValueError: Si les données sont invalides
            TypeError: Si les données ne sont pas dans le bon format
        """
        if self.data is None:
            raise ValueError("Les données n'ont pas été fournies")
        
        if not isinstance(self.data, pd.DataFrame):
            raise TypeError("Les données doivent être un DataFrame pandas")
        
        if self.X is None or self.y is None:
            raise ValueError("Les variables explicatives et la variable cible doivent être définies")
        
        return True
    
    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du module.
        
        Returns:
            str: Description du module
        """
        return f"Module Régression {self.__class__.__name__} v{self.version}"
    
    def __repr__(self) -> str:
        """
        Retourne une représentation technique du module.
        
        Returns:
            str: Représentation technique du module
        """
        return f"{self.__class__.__name__}(version={self.version})" 