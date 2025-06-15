'''
=====================================================================
TimeSeriesModule.py
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

This module defines the time series analysis functionality for the
py_stats_toolkit library. It provides methods for analyzing and
forecasting time series data, including decomposition, trend analysis,
and seasonality detection.

tags : time series, temporal, analysis, forecasting, decomposition, trend, seasonality
=====================================================================
Ce module définit les fonctionnalités d'analyse de séries temporelles pour
la bibliothèque py_stats_toolkit. Il fournit des méthodes pour l'analyse
et la prévision de séries temporelles, incluant la décomposition, l'analyse
de tendance et la détection de saisonnalité.

tags : séries temporelles, temporel, analyse, prévision, décomposition, tendance, saisonnalité
=====================================================================
'''

from abc import abstractmethod
import numpy as np
import pandas as pd
from typing import Any, Dict, List, Optional, Tuple, Union
from .StatisticalModule import StatisticalModule

class TimeSeriesModule(StatisticalModule):
    """
    Module d'analyse de séries temporelles.
    
    Cette classe fournit des méthodes spécifiques pour l'analyse et la
    prévision de séries temporelles, incluant la décomposition, l'analyse
    de tendance et la détection de saisonnalité.
    
    Attributes:
        data (pd.Series): Données de la série temporelle
        frequency (int): Fréquence des données
        decomposition (Dict[str, pd.Series]): Résultats de la décomposition
        model (Any): Modèle de prévision
        tags (List[str]): Tags associés au module
        version (str): Version du module
    """
    
    def __init__(self):
        """
        Initialise le module d'analyse de séries temporelles.
        
        Cette méthode configure les attributs spécifiques aux séries
        temporelles et initialise les structures de données nécessaires.
        """
        super().__init__()
        self.data = None
        self.frequency = None
        self.decomposition = None
        self.model = None
        self.tags.extend(["séries temporelles", "prévision"])
    
    @abstractmethod
    def process(self, data: pd.Series, **kwargs) -> Dict[str, Any]:
        """
        Analyse la série temporelle.
        
        Cette méthode doit être implémentée par les classes filles pour
        effectuer leur analyse spécifique de séries temporelles.
        
        Args:
            data (pd.Series): Series pandas contenant la série temporelle
            **kwargs: Arguments additionnels spécifiques à l'analyse
                - frequency (int): Fréquence des données
                - method (str): Méthode d'analyse à utiliser
                - params (Dict[str, Any]): Paramètres de la méthode
            
        Returns:
            Dict[str, Any]: Résultats de l'analyse
                - decomposition (Dict[str, pd.Series]): Composantes de la série
                - statistics (Dict[str, float]): Statistiques de base
                - method (str): Méthode utilisée
                - params (Dict[str, Any]): Paramètres utilisés
            
        Raises:
            ValueError: Si les données ne sont pas une série temporelle valide
            TypeError: Si les données ne sont pas dans le bon format
        """
        pass
    
    @abstractmethod
    def forecast(self, steps: int, **kwargs) -> pd.Series:
        """
        Effectue des prévisions.
        
        Cette méthode doit être implémentée par les classes filles pour
        effectuer leurs prévisions spécifiques.
        
        Args:
            steps (int): Nombre de pas de temps à prévoir
            **kwargs: Arguments additionnels spécifiques au modèle
                - method (str): Méthode de prévision à utiliser
                - params (Dict[str, Any]): Paramètres de la méthode
            
        Returns:
            pd.Series: Prévisions de la série temporelle
            
        Raises:
            ValueError: Si le modèle n'a pas été entraîné
            RuntimeError: Si une erreur survient pendant la prévision
        """
        pass
    
    def decompose(self) -> Dict[str, pd.Series]:
        """
        Décompose la série temporelle en composantes.
        
        Cette méthode décompose la série en tendance, saisonnalité
        et résidus en utilisant la décomposition saisonnière.
        
        Returns:
            Dict[str, pd.Series]: Composantes de la série
                - Tendance: Composante de tendance
                - Saisonnalité: Composante saisonnière
                - Résidus: Composante résiduelle
            
        Raises:
            ValueError: Si les données n'ont pas été traitées
            RuntimeError: Si une erreur survient pendant la décomposition
        """
        if self.data is None:
            raise ValueError("Les données n'ont pas été traitées")
        
        from statsmodels.tsa.seasonal import seasonal_decompose
        decomposition = seasonal_decompose(self.data, period=self.frequency)
        
        self.decomposition = {
            "Tendance": decomposition.trend,
            "Saisonnalité": decomposition.seasonal,
            "Résidus": decomposition.resid
        }
        
        return self.decomposition
    
    def get_basic_stats(self) -> Dict[str, float]:
        """
        Calcule les statistiques de base de la série.
        
        Returns:
            Dict[str, float]: Statistiques de base
                - Moyenne: Moyenne de la série
                - Écart-type: Écart-type de la série
                - Minimum: Valeur minimale
                - Maximum: Valeur maximale
                - Médiane: Médiane de la série
            
        Raises:
            ValueError: Si les données n'ont pas été traitées
        """
        if self.data is None:
            raise ValueError("Les données n'ont pas été traitées")
        
        return {
            "Moyenne": self.data.mean(),
            "Écart-type": self.data.std(),
            "Minimum": self.data.min(),
            "Maximum": self.data.max(),
            "Médiane": self.data.median()
        }
    
    def get_trend_info(self) -> Dict[str, Any]:
        """
        Analyse la tendance de la série.
        
        Returns:
            Dict[str, Any]: Informations sur la tendance
                - Type: Type de tendance (Croissante/Décroissante)
                - Pente: Pente de la régression linéaire
                - R2: Coefficient de détermination
                - p-valeur: P-valeur du test de significativité
            
        Raises:
            ValueError: Si les données n'ont pas été traitées
        """
        if self.data is None:
            raise ValueError("Les données n'ont pas été traitées")
        
        from scipy import stats
        x = np.arange(len(self.data))
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, self.data)
        
        return {
            "Type": "Croissante" if slope > 0 else "Décroissante",
            "Pente": slope,
            "R2": r_value**2,
            "p-valeur": p_value
        }
    
    def get_seasonality_info(self) -> Dict[str, Any]:
        """
        Analyse la saisonnalité de la série.
        
        Returns:
            Dict[str, Any]: Informations sur la saisonnalité
                - Période: Période de la saisonnalité
                - Amplitude: Amplitude de la saisonnalité
                - Phase: Phase de la saisonnalité
            
        Raises:
            ValueError: Si les données n'ont pas été traitées
        """
        if self.data is None:
            raise ValueError("Les données n'ont pas été traitées")
        
        if self.decomposition is None:
            self.decompose()
        
        seasonal = self.decomposition["Saisonnalité"]
        return {
            "Période": self.frequency,
            "Amplitude": seasonal.max() - seasonal.min(),
            "Phase": seasonal.idxmax()
        }
    
    def test_stationarity(self) -> Dict[str, Any]:
        """
        Teste la stationnarité de la série.
        
        Returns:
            Dict[str, Any]: Résultats du test
                - Test de Dickey-Fuller: Statistique du test
                - p-valeur: P-valeur du test
                - Stationnaire: Résultat du test (True/False)
            
        Raises:
            ValueError: Si les données n'ont pas été traitées
        """
        if self.data is None:
            raise ValueError("Les données n'ont pas été traitées")
        
        from statsmodels.tsa.stattools import adfuller
        result = adfuller(self.data.dropna())
        
        return {
            "Test de Dickey-Fuller": result[0],
            "p-valeur": result[1],
            "Stationnaire": result[1] < 0.05
        }
    
    def get_autocorrelation(self, lags: int = 40) -> pd.Series:
        """
        Calcule l'autocorrélation de la série.
        
        Args:
            lags (int): Nombre de décalages à calculer
            
        Returns:
            pd.Series: Autocorrélations de la série
            
        Raises:
            ValueError: Si les données n'ont pas été traitées
        """
        if self.data is None:
            raise ValueError("Les données n'ont pas été traitées")
        
        from statsmodels.tsa.stattools import acf
        return pd.Series(acf(self.data, nlags=lags))
    
    def get_partial_autocorrelation(self, lags: int = 40) -> pd.Series:
        """
        Calcule l'autocorrélation partielle de la série.
        
        Args:
            lags (int): Nombre de décalages à calculer
            
        Returns:
            pd.Series: Autocorrélations partielles de la série
            
        Raises:
            ValueError: Si les données n'ont pas été traitées
        """
        if self.data is None:
            raise ValueError("Les données n'ont pas été traitées")
        
        from statsmodels.tsa.stattools import pacf
        return pd.Series(pacf(self.data, nlags=lags))
    
    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du module.
        
        Returns:
            str: Description du module
        """
        return f"Module Série Temporelle {self.__class__.__name__} v{self.version}"
    
    def __repr__(self) -> str:
        """
        Retourne une représentation technique du module.
        
        Returns:
            str: Représentation technique du module
        """
        return f"{self.__class__.__name__}(version={self.version})" 