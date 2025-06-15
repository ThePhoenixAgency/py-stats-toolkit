'''
=====================================================================
TestModule.py
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

This module defines the statistical testing functionality for the
py_stats_toolkit library. It provides methods for performing various
types of statistical tests, including hypothesis testing, normality
tests, and correlation tests.

tags : tests, hypothesis, normality, correlation, statistical tests, analysis
=====================================================================
Ce module définit les fonctionnalités de tests statistiques pour
la bibliothèque py_stats_toolkit. Il fournit des méthodes pour effectuer
différents types de tests statistiques, incluant les tests d'hypothèse,
les tests de normalité et les tests de corrélation.

tags : tests, hypothèse, normalité, corrélation, tests statistiques, analyse
=====================================================================
'''

from abc import abstractmethod
import numpy as np
import pandas as pd
from typing import Any, Dict, List, Optional, Tuple, Union
from .StatisticalModule import StatisticalModule

class TestModule(StatisticalModule):
    """
    Module de tests statistiques.
    
    Cette classe fournit des méthodes pour effectuer différents types
    de tests statistiques, incluant les tests d'hypothèse, les tests
    de normalité et les tests de corrélation.
    
    Attributes:
        data (Union[pd.DataFrame, pd.Series]): Données à tester
        test_type (str): Type de test à effectuer
        test_params (Dict[str, Any]): Paramètres du test
        results (Dict[str, Any]): Résultats du test
        tags (List[str]): Tags associés au module
        version (str): Version du module
    """
    
    def __init__(self):
        """
        Initialise le module de tests statistiques.
        
        Cette méthode configure les attributs spécifiques aux tests
        et initialise les structures de données nécessaires.
        """
        super().__init__()
        self.data = None
        self.test_type = None
        self.test_params = {}
        self.results = {}
        self.tags.extend(["tests", "hypothèse"])
    
    @abstractmethod
    def process(self, data: Union[pd.DataFrame, pd.Series], **kwargs) -> Dict[str, Any]:
        """
        Effectue le test statistique.
        
        Cette méthode doit être implémentée par les classes filles pour
        effectuer leur type spécifique de test.
        
        Args:
            data (Union[pd.DataFrame, pd.Series]): Données à tester
            **kwargs: Arguments additionnels spécifiques au test
                - test_type (str): Type de test à effectuer
                - alpha (float): Niveau de significativité
                - params (Dict[str, Any]): Paramètres spécifiques au test
            
        Returns:
            Dict[str, Any]: Résultats du test
                - statistic (float): Statistique du test
                - p_value (float): P-valeur
                - conclusion (str): Conclusion du test
                - method (str): Méthode utilisée
                - params (Dict[str, Any]): Paramètres utilisés
            
        Raises:
            ValueError: Si les données sont invalides
            TypeError: Si les données ne sont pas dans le bon format
        """
        pass
    
    def get_test_type(self) -> str:
        """
        Retourne le type de test effectué.
        
        Returns:
            str: Type de test
            
        Raises:
            ValueError: Si aucun test n'a été effectué
        """
        if not self.test_type:
            raise ValueError("Aucun test n'a été effectué")
        return self.test_type
    
    def get_test_params(self) -> Dict[str, Any]:
        """
        Retourne les paramètres du test.
        
        Returns:
            Dict[str, Any]: Paramètres du test
            
        Raises:
            ValueError: Si aucun test n'a été effectué
        """
        if not self.test_params:
            raise ValueError("Aucun test n'a été effectué")
        return self.test_params
    
    def get_results(self) -> Dict[str, Any]:
        """
        Retourne les résultats du test.
        
        Returns:
            Dict[str, Any]: Résultats du test
                - statistic: Statistique du test
                - p_value: P-valeur
                - conclusion: Conclusion du test
            
        Raises:
            ValueError: Si aucun test n'a été effectué
        """
        if not self.results:
            raise ValueError("Aucun test n'a été effectué")
        return self.results
    
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
        
        if not isinstance(self.data, (pd.DataFrame, pd.Series)):
            raise TypeError("Les données doivent être un DataFrame ou une Series pandas")
        
        return True
    
    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du module.
        
        Returns:
            str: Description du module
        """
        return f"Module Tests {self.__class__.__name__} v{self.version}"
    
    def __repr__(self) -> str:
        """
        Retourne une représentation technique du module.
        
        Returns:
            str: Représentation technique du module
        """
        return f"{self.__class__.__name__}(version={self.version})" 