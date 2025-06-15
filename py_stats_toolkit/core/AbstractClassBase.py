'''
=====================================================================
AbstractClassBase.py
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

This module defines the base abstract class for all statistical modules
in the py_stats_toolkit library. It provides the fundamental interface
and common functionality that all statistical modules must implement.

tags : abstract, base class, interface, stats, core, foundation
=====================================================================
Ce module définit la classe abstraite de base pour tous les modules
statistiques de la bibliothèque py_stats_toolkit. Il fournit l'interface
fondamentale et les fonctionnalités communes que tous les modules
statistiques doivent implémenter.

tags : abstrait, classe de base, interface, stats, cœur, fondation
=====================================================================
'''

from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from typing import Any, Dict, List, Optional

class StatisticalModule(ABC):
    """
    Classe abstraite de base pour tous les modules statistiques.
    
    Cette classe définit l'interface commune que tous les modules
    statistiques doivent implémenter. Elle fournit les méthodes
    de base et la structure commune pour l'analyse statistique.
    
    Attributes:
        tags (List[str]): Tags associés au module
        version (str): Version du module
    """
    
    def __init__(self):
        """
        Initialise le module statistique.
        
        Cette méthode configure les attributs de base du module,
        notamment les tags et la version.
        """
        self.tags = ["stats", "module"]
        self.version = "1.0.0"
        self.data = None
        self.result = None
    
    @abstractmethod
    def process(self, data: Any, **kwargs) -> Dict[str, Any]:
        """
        Traite les données statistiques.
        
        Cette méthode doit être implémentée par toutes les classes filles
        pour effectuer leur traitement statistique spécifique.
        
        Args:
            data (Any): Données à traiter
            **kwargs: Arguments additionnels spécifiques au traitement
            
        Returns:
            Dict[str, Any]: Résultats du traitement
            
        Raises:
            NotImplementedError: Si la méthode n'est pas implémentée
        """
        raise NotImplementedError("La méthode process doit être implémentée")
    
    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du module.
        
        Returns:
            str: Description du module
        """
        return f"Module {self.__class__.__name__} v{self.version}"
    
    def __repr__(self) -> str:
        """
        Retourne une représentation technique du module.
        
        Returns:
            str: Représentation technique du module
        """
        return f"{self.__class__.__name__}(version={self.version})"
    
    def validate_data(self, data):
        """Valide les données d'entrée."""
        if isinstance(data, (np.ndarray, pd.DataFrame, pd.Series)):
            self.data = data
        else:
            raise TypeError("Les données doivent être un numpy array ou un pandas DataFrame/Series")
    
    def get_result(self):
        """Retourne le résultat du traitement."""
        return self.result

class TimeSeriesModule(StatisticalModule):
    """Classe de base pour l'analyse temporelle."""
    
    def __init__(self):
        super().__init__()
        self.timestamps = None
    
    def set_timestamps(self, timestamps):
        """Définit les timestamps pour l'analyse temporelle."""
        self.timestamps = timestamps

class RandomProcessModule(StatisticalModule):
    """Classe de base pour les processus aléatoires."""
    
    def __init__(self):
        super().__init__()
        self.seed = None
    
    def set_seed(self, seed):
        """Définit la graine pour la reproductibilité."""
        self.seed = seed
        np.random.seed(seed) 