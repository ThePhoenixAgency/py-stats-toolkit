'''
=====================================================================
BaseCapsule.py
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

This module defines the base class for all statistical analysis capsules
in the py_stats_toolkit library. It provides a common interface and basic
functionality for specialized statistical analysis workflows. Each capsule
is designed to handle specific types of statistical analysis with predefined
workflows and configurations.

tags : capsule, analysis, workflow, specialized, stats, base class, interface
=====================================================================
Ce module définit la classe de base pour toutes les capsules d'analyse
statistique de la bibliothèque py_stats_toolkit. Il fournit une interface
commune et des fonctionnalités de base pour les flux de travail d'analyse
statistique spécialisés. Chaque capsule est conçue pour gérer des types
spécifiques d'analyse statistique avec des flux de travail et des
configurations prédéfinis.

tags : capsule, analyse, flux de travail, spécialisé, stats, classe de base, interface
=====================================================================
'''

from abc import abstractmethod
import numpy as np
import pandas as pd
from typing import Any, Dict, List, Optional, Tuple, Union
from core.AbstractClassBase import StatisticalModule

class BaseCapsule(StatisticalModule):
    """
    Classe abstraite de base pour toutes les capsules d'analyse statistique.
    
    Cette classe définit l'interface commune que toutes les capsules d'analyse
    statistique doivent implémenter. Elle fournit des méthodes de base pour
    la gestion des flux de travail d'analyse et la configuration des capsules.
    
    Attributes:
        data (Union[pd.DataFrame, pd.Series]): Données à analyser
        parameters (Dict[str, Any]): Paramètres de configuration de la capsule
        results (Dict[str, Any]): Résultats de l'analyse
        workflow (List[str]): Étapes du flux de travail
        tags (List[str]): Tags associés à la capsule
    """
    
    def __init__(self):
        """
        Initialise la capsule d'analyse statistique.
        
        Cette méthode doit être appelée par toutes les classes filles
        pour initialiser les attributs de base de la capsule. Elle
        configure les attributs par défaut et ajoute les tags de base.
        """
        super().__init__()
        self.data = None
        self.parameters = {}
        self.results = {}
        self.workflow = []
        self.tags.extend(["capsule", "flux de travail"])
    
    @abstractmethod
    def configure(self, **kwargs) -> None:
        """
        Configure les paramètres de la capsule.
        
        Cette méthode doit être implémentée par toutes les classes filles
        pour configurer les paramètres spécifiques à leur type d'analyse.
        
        Args:
            **kwargs: Paramètres de configuration spécifiques à la capsule
                - Les paramètres exacts dépendent du type de capsule
                - Doivent être documentés dans la classe fille
            
        Raises:
            ValueError: Si les paramètres sont invalides
            TypeError: Si les types des paramètres sont incorrects
        """
        pass
    
    @abstractmethod
    def process(self, data: Union[pd.DataFrame, pd.Series], **kwargs) -> Dict[str, Any]:
        """
        Exécute le flux de travail d'analyse.
        
        Cette méthode doit être implémentée par toutes les classes filles
        pour exécuter leur flux de travail d'analyse spécifique.
        
        Args:
            data (Union[pd.DataFrame, pd.Series]): Données à analyser
            **kwargs: Arguments additionnels spécifiques à l'analyse
                - Les arguments exacts dépendent du type de capsule
                - Doivent être documentés dans la classe fille
            
        Returns:
            Dict[str, Any]: Dictionnaire contenant les résultats de l'analyse
                - La structure exacte dépend du type de capsule
                - Doit être documentée dans la classe fille
            
        Raises:
            ValueError: Si les données sont invalides
            TypeError: Si les données ne sont pas dans le bon format
            RuntimeError: Si une erreur survient pendant l'analyse
        """
        pass
    
    def validate_data(self) -> bool:
        """
        Valide les données d'entrée.
        
        Cette méthode vérifie que les données sont valides pour l'analyse.
        Elle peut être surchargée par les classes filles pour ajouter des
        validations spécifiques à leur type d'analyse.
        
        Returns:
            bool: True si les données sont valides, False sinon
            
        Raises:
            ValueError: Si les données n'ont pas été chargées
            TypeError: Si les données ne sont pas dans le bon format
        """
        if self.data is None:
            raise ValueError("Les données n'ont pas été chargées")
        return True
    
    def get_workflow_steps(self) -> List[str]:
        """
        Retourne la liste des étapes du flux de travail.
        
        Cette méthode permet d'obtenir la liste des étapes qui seront
        exécutées lors de l'analyse. Chaque étape doit être clairement
        identifiée et documentée.
        
        Returns:
            List[str]: Liste des étapes du flux de travail
        """
        return self.workflow
    
    def get_results(self) -> Dict[str, Any]:
        """
        Retourne les résultats de l'analyse.
        
        Cette méthode permet d'accéder aux résultats de l'analyse
        après l'exécution du flux de travail. Les résultats sont
        organisés dans un dictionnaire dont la structure dépend
        du type de capsule.
        
        Returns:
            Dict[str, Any]: Dictionnaire contenant les résultats
            
        Raises:
            ValueError: Si l'analyse n'a pas été exécutée
        """
        if not self.results:
            raise ValueError("L'analyse n'a pas été exécutée")
        return self.results
    
    def __str__(self) -> str:
        """
        Retourne une représentation textuelle de la capsule.
        
        Cette méthode fournit une description lisible de la capsule,
        incluant son nom et le nombre d'étapes dans son flux de travail.
        
        Returns:
            str: Description de la capsule
        """
        return f"Capsule {self.__class__.__name__} avec {len(self.workflow)} étapes"
    
    def __repr__(self) -> str:
        """
        Retourne une représentation technique de la capsule.
        
        Cette méthode fournit une représentation technique de la capsule,
        utile pour le débogage et le développement.
        
        Returns:
            str: Représentation technique de la capsule
        """
        return f"{self.__class__.__name__}(workflow={self.workflow})" 