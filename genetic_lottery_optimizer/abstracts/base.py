"""
Module       : base.py
Date         : 2025-06-08
Description  : Classes de base pour les modules statistiques
Commit Git   : [v0.3.16 - 1411876]
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any
import pandas as pd
import numpy as np

class BaseModule(ABC):
    """Classe de base abstraite pour tous les modules statistiques."""
    
    def __init__(self, name: str, description: str):
        """Initialise le module.
        
        Args:
            name: Nom du module
            description: Description du module
        """
        self.name = name
        self.description = description
        
    @abstractmethod
    def run(self, data: pd.DataFrame) -> Dict[str, Any]:
        """Exécute le module sur les données.
        
        Args:
            data: DataFrame contenant les données à analyser
            
        Returns:
            Dict contenant les résultats du module
        """
        pass
        
    def validate_data(self, data: pd.DataFrame) -> bool:
        """Valide les données d'entrée.
        
        Args:
            data: DataFrame à valider
            
        Returns:
            bool: True si les données sont valides
        """
        return True
        
    def format_results(self, scores_line: np.ndarray, score_global: float) -> Dict[str, Any]:
        """Formate les résultats du module.
        
        Args:
            scores_line: Array des scores par ligne
            score_global: Score global
            
        Returns:
            Dict contenant les résultats formatés
        """
        return {
            'scores_line': scores_line,
            'score_global': score_global,
            'description': self.description
        }

class ModuleCategory(ABC):
    """Classe de base pour les catégories de modules."""
    
    def __init__(self, name: str):
        """Initialise la catégorie.
        
        Args:
            name: Nom de la catégorie
        """
        self.name = name
        self.modules: List[BaseModule] = []
        
    def add_module(self, module: BaseModule) -> None:
        """Ajoute un module à la catégorie.
        
        Args:
            module: Module à ajouter
        """
        self.modules.append(module)
        
    def run_all(self, data: pd.DataFrame) -> Dict[str, Dict[str, Any]]:
        """Exécute tous les modules de la catégorie.
        
        Args:
            data: DataFrame contenant les données à analyser
            
        Returns:
            Dict contenant les résultats de tous les modules
        """
        results = {}
        for module in self.modules:
            if module.validate_data(data):
                results[module.name] = module.run(data)
        return results 