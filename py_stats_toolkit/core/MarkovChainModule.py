'''
=====================================================================
MarkovChainModule.py
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

This module defines the Markov chain analysis functionality for the
py_stats_toolkit library. It provides methods for analyzing
stochastic processes, transition probabilities, and steady states.

tags : markov chains, stochastic processes, transition matrix, steady state, probability
=====================================================================
Ce module définit les fonctionnalités d'analyse des chaînes de Markov
pour la bibliothèque py_stats_toolkit. Il fournit des méthodes pour
analyser les processus stochastiques, les probabilités de transition
et les états stationnaires.

tags : chaînes de Markov, processus stochastiques, matrice de transition, état stationnaire, probabilité
=====================================================================
'''

from abc import abstractmethod
import numpy as np
import pandas as pd
from typing import Any, Dict, List, Optional, Tuple, Union
from .StatisticalModule import StatisticalModule

class MarkovChainModule(StatisticalModule):
    """
    Module d'analyse des chaînes de Markov.
    
    Cette classe fournit des méthodes pour analyser les chaînes
    de Markov, calculer les probabilités de transition et déterminer
    les états stationnaires.
    
    Attributes:
        transition_matrix (np.ndarray): Matrice de transition
        states (List[str]): Liste des états
        initial_state (str): État initial
        steady_state (np.ndarray): État stationnaire
        tags (List[str]): Tags associés au module
        version (str): Version du module
    """
    
    def __init__(self):
        """
        Initialise le module d'analyse des chaînes de Markov.
        
        Cette méthode configure les attributs spécifiques à l'analyse
        des chaînes de Markov et initialise les structures de données nécessaires.
        """
        super().__init__()
        self.transition_matrix = None
        self.states = []
        self.initial_state = None
        self.steady_state = None
        self.tags.extend(["markov", "stochastique"])
    
    @abstractmethod
    def process(self, transition_matrix: np.ndarray, **kwargs) -> Dict[str, Any]:
        """
        Analyse la chaîne de Markov.
        
        Cette méthode doit être implémentée par les classes filles pour
        analyser leur type spécifique de chaîne de Markov.
        
        Args:
            transition_matrix (np.ndarray): Matrice de transition
            **kwargs: Arguments additionnels spécifiques à l'analyse
                - states (List[str]): Liste des états
                - initial_state (str): État initial
                - steps (int): Nombre d'étapes à simuler
        
        Returns:
            Dict[str, Any]: Résultats de l'analyse
                - steady_state (np.ndarray): État stationnaire
                - probabilities (Dict[str, float]): Probabilités par état
                - transitions (Dict[str, Dict[str, float]]): Probabilités de transition
        
        Raises:
            ValueError: Si la matrice de transition est invalide
            TypeError: Si les données ne sont pas dans le bon format
        """
        pass
    
    def calculate_steady_state(self) -> np.ndarray:
        """
        Calcule l'état stationnaire de la chaîne.
        
        Returns:
            np.ndarray: État stationnaire
            
        Raises:
            ValueError: Si la matrice de transition est invalide
        """
        if self.transition_matrix is None:
            raise ValueError("La matrice de transition n'a pas été fournie")
        
        # Calcul de l'état stationnaire
        # À implémenter selon le type de chaîne
        pass
    
    def simulate_chain(self, steps: int) -> List[str]:
        """
        Simule la chaîne de Markov.
        
        Args:
            steps (int): Nombre d'étapes à simuler
        
        Returns:
            List[str]: Séquence d'états
            
        Raises:
            ValueError: Si les paramètres sont invalides
        """
        if self.transition_matrix is None:
            raise ValueError("La matrice de transition n'a pas été fournie")
        
        if self.initial_state is None:
            raise ValueError("L'état initial n'a pas été spécifié")
        
        # Simulation de la chaîne
        # À implémenter selon le type de chaîne
        pass
    
    def get_transition_probability(self, from_state: str, to_state: str) -> float:
        """
        Obtient la probabilité de transition entre deux états.
        
        Args:
            from_state (str): État de départ
            to_state (str): État d'arrivée
        
        Returns:
            float: Probabilité de transition
            
        Raises:
            ValueError: Si les états sont invalides
        """
        if self.transition_matrix is None:
            raise ValueError("La matrice de transition n'a pas été fournie")
        
        if from_state not in self.states or to_state not in self.states:
            raise ValueError("États invalides")
        
        # Calcul de la probabilité de transition
        # À implémenter selon le type de chaîne
        pass
    
    def validate_data(self) -> bool:
        """
        Valide les données d'entrée.
        
        Returns:
            bool: True si les données sont valides
            
        Raises:
            ValueError: Si les données sont invalides
            TypeError: Si les données ne sont pas dans le bon format
        """
        if self.transition_matrix is None:
            raise ValueError("La matrice de transition n'a pas été fournie")
        
        if not isinstance(self.transition_matrix, np.ndarray):
            raise TypeError("La matrice de transition doit être un tableau numpy")
        
        if len(self.states) == 0:
            raise ValueError("Aucun état n'a été spécifié")
        
        return True
    
    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du module.
        
        Returns:
            str: Description du module
        """
        return f"Module Chaînes de Markov {self.__class__.__name__} v{self.version}"
    
    def __repr__(self) -> str:
        """
        Retourne une représentation technique du module.
        
        Returns:
            str: Représentation technique du module
        """
        return f"{self.__class__.__name__}(version={self.version})" 