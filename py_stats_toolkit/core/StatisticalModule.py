"""
Module de base pour les analyses statistiques.

Ce module définit l'interface commune pour tous les modules statistiques
de la bibliothèque py_stats_toolkit.
"""

from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from typing import Any, Dict, List, Optional, Union

class StatisticalModule(ABC):
    """
    Classe abstraite de base pour tous les modules statistiques.
    
    Cette classe définit l'interface commune que tous les modules statistiques
    doivent implémenter. Elle fournit des méthodes de base pour le traitement
    des données et la validation des entrées.
    
    Attributes:
        name (str): Nom du module statistique
        description (str): Description détaillée du module
        version (str): Version du module
        tags (list): Liste des tags associés au module
    """
    
    def __init__(self):
        """
        Initialise le module statistique.
        
        Cette méthode doit être appelée par toutes les classes filles
        pour initialiser les attributs de base.
        """
        self.name = self.__class__.__name__
        self.description = "Module statistique de base"
        self.version = "1.0.0"
        self.tags = ["statistiques", "base"]
    
    @abstractmethod
    def process(self, data: Union[pd.DataFrame, pd.Series, np.ndarray], **kwargs) -> Any:
        """
        Traite les données et effectue l'analyse statistique.
        
        Args:
            data: Données à analyser (DataFrame, Series ou array numpy)
            **kwargs: Arguments additionnels spécifiques au module
            
        Returns:
            Résultat de l'analyse statistique
            
        Raises:
            TypeError: Si le type de données n'est pas supporté
            ValueError: Si les données sont invalides
        """
        pass
    
    def validate_data(self, data: Union[pd.DataFrame, pd.Series, np.ndarray]) -> None:
        """
        Valide les données d'entrée.
        
        Args:
            data: Données à valider
            
        Raises:
            TypeError: Si le type de données n'est pas supporté
            ValueError: Si les données sont vides ou invalides
        """
        if not isinstance(data, (pd.DataFrame, pd.Series, np.ndarray)):
            raise TypeError("Les données doivent être un DataFrame, Series ou array numpy")
        
        if isinstance(data, (pd.DataFrame, pd.Series)) and data.empty:
            raise ValueError("Les données ne peuvent pas être vides")
        
        if isinstance(data, np.ndarray) and data.size == 0:
            raise ValueError("Les données ne peuvent pas être vides")
    
    def get_info(self) -> Dict[str, Any]:
        """
        Retourne les informations sur le module.
        
        Returns:
            Dictionnaire contenant les informations du module
        """
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "tags": self.tags
        }
    
    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du module.
        
        Returns:
            Chaîne de caractères décrivant le module
        """
        return f"{self.name} (v{self.version}) - {self.description}"
    
    def __repr__(self) -> str:
        """
        Retourne une représentation technique du module.
        
        Returns:
            Chaîne de caractères technique du module
        """
        return f"{self.__class__.__name__}(name='{self.name}', version='{self.version}')" 