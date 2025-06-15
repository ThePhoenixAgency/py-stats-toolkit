"""
=====================================================================
Module       : AbstractClassStatistics.py
Date         : 2025-06-08
Description  : Classes abstraites pour l'analyse statistique
tags         : abstract, module, statistics, analysis, stats
=====================================================================
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Union
import pandas as pd
import numpy as np
from dataclasses import dataclass
from enum import Enum
import logging

class ModuleType(Enum):
    """Types de modules statistiques."""
    FREQUENTIEL = "frequentiel"
    SEQUENTIEL = "sequentiel"
    FRACTAL = "fractal"
    THEORIQUE = "theorique"
    IA = "ia"

@dataclass
class ModuleResult:
    """Résultat d'un module statistique."""
    scores_line: np.ndarray
    score_global: float
    description: str
    confidence: float = 1.0
    metadata: Dict[str, Any] = None

    def __post_init__(self):
        """Initialisation post-création."""
        if self.metadata is None:
            self.metadata = {}

class AbstractStatisticsModule(ABC):
    """Classe abstraite pour les modules statistiques."""
    
    def __init__(self, 
                 name: str,
                 description: str,
                 module_type: ModuleType,
                 required_columns: List[str],
                 version: str = "1.0.0"):
        """Initialise le module statistique.
        
        Args:
            name: Nom du module
            description: Description du module
            module_type: Type de module
            required_columns: Colonnes requises dans le DataFrame
            version: Version du module
        """
        self.name = name
        self.description = description
        self.module_type = module_type
        self.required_columns = required_columns
        self.version = version
        self.logger = logging.getLogger(f"statistics.{module_type.value}.{name}")
        self.logger.setLevel(logging.ERROR)  # On ne log que les erreurs
        
    @abstractmethod
    def run(self, data: pd.DataFrame) -> ModuleResult:
        """Exécute le module sur les données.
        
        Args:
            data: DataFrame contenant les données à analyser
            
        Returns:
            ModuleResult contenant les résultats du module
        """
        pass
        
    def validate_data(self, data: pd.DataFrame) -> bool:
        """Valide les données d'entrée.
        
        Args:
            data: DataFrame à valider
            
        Returns:
            bool: True si les données sont valides
        """
        try:
            # Vérifie les colonnes requises
            missing_cols = [col for col in self.required_columns if col not in data.columns]
            if missing_cols:
                self.logger.error(f"Colonnes manquantes: {missing_cols}")
                return False
                
            # Vérifie les types de données
            for col in self.required_columns:
                if not self._validate_column_type(data[col]):
                    return False
                    
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la validation: {str(e)}")
            return False
            
    def _validate_column_type(self, series: pd.Series) -> bool:
        """Valide le type d'une colonne.
        
        Args:
            series: Série à valider
            
        Returns:
            bool: True si le type est valide
        """
        return True  # À surcharger selon les besoins
        
    def log_error(self, message: str, error: Optional[Exception] = None) -> None:
        """Log une erreur.
        
        Args:
            message: Message d'erreur
            error: Exception associée (optionnel)
        """
        if error:
            self.logger.error(f"{message}: {str(error)}")
        else:
            self.logger.error(message)
            
    def log_info(self, message: str) -> None:
        """Log une information.
        
        Args:
            message: Message d'information
        """
        self.logger.info(message)

class AbstractModuleCategory(ABC):
    """Classe abstraite pour les catégories de modules."""
    
    def __init__(self, name: str, module_type: ModuleType):
        """Initialise la catégorie.
        
        Args:
            name: Nom de la catégorie
            module_type: Type de modules de la catégorie
        """
        self.name = name
        self.module_type = module_type
        self.modules: List[AbstractStatisticsModule] = []
        self.logger = logging.getLogger(f"statistics.category.{name}")
        self.logger.setLevel(logging.ERROR)
        
    def add_module(self, module: AbstractStatisticsModule) -> None:
        """Ajoute un module à la catégorie.
        
        Args:
            module: Module à ajouter
        """
        if module.module_type != self.module_type:
            raise ValueError(f"Type de module incompatible: {module.module_type} != {self.module_type}")
        self.modules.append(module)
        self.logger.info(f"Module {module.name} ajouté à la catégorie {self.name}")
        
    def run_all(self, data: pd.DataFrame) -> Dict[str, ModuleResult]:
        """Exécute tous les modules de la catégorie.
        
        Args:
            data: DataFrame contenant les données à analyser
            
        Returns:
            Dict contenant les résultats de tous les modules
        """
        results = {}
        for module in self.modules:
            if module.validate_data(data):
                try:
                    results[module.name] = module.run(data)
                except Exception as e:
                    self.logger.error(f"Erreur dans le module {module.name}: {str(e)}")
        return results

class StatisticsManager:
    """Gestionnaire central des modules statistiques."""
    
    def __init__(self, logger=None):
        """Initialise le gestionnaire.
        
        Args:
            logger: Logger à utiliser
        """
        self.categories: Dict[ModuleType, AbstractModuleCategory] = {}
        self._logger = logger
        self.logger = logging.getLogger("statistics.manager")
        self.logger.setLevel(logging.ERROR)
        
    def register_category(self, category: AbstractModuleCategory) -> None:
        """Enregistre une catégorie.
        
        Args:
            category: Catégorie à enregistrer
        """
        category.logger = self._logger
        self.categories[category.module_type] = category
        self.logger.info(f"Catégorie {category.name} enregistrée")
        
    def run_analysis(self, data: pd.DataFrame, module_types: Optional[List[ModuleType]] = None) -> Dict[str, Dict[str, ModuleResult]]:
        """Exécute l'analyse sur les données.
        
        Args:
            data: DataFrame à analyser
            module_types: Types de modules à exécuter (tous si None)
            
        Returns:
            Dict contenant les résultats par catégorie
        """
        results = {}
        types_to_run = module_types or list(self.categories.keys())
        
        for module_type in types_to_run:
            if module_type in self.categories:
                category = self.categories[module_type]
                results[category.name] = category.run_all(data)
                
        return results
        
    def get_module_info(self) -> Dict[str, List[Dict[str, Any]]]:
        """Récupère les informations sur tous les modules.
        
        Returns:
            Dict contenant les informations des modules par catégorie
        """
        info = {}
        for category in self.categories.values():
            info[category.name] = [
                {
                    'name': module.name,
                    'description': module.description,
                    'version': module.version,
                    'required_columns': module.required_columns
                }
                for module in category.modules
            ]
        return info 