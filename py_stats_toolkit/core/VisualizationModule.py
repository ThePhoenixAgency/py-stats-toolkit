'''
=====================================================================
VisualizationModule.py
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

This module defines the data visualization functionality for the
py_stats_toolkit library. It provides methods for creating various
types of statistical visualizations, including plots, charts, and
interactive visualizations.

tags : visualization, plots, charts, graphics, interactive, statistical plots
=====================================================================
Ce module définit les fonctionnalités de visualisation de données pour
la bibliothèque py_stats_toolkit. Il fournit des méthodes pour créer
différents types de visualisations statistiques, incluant des graphiques,
des diagrammes et des visualisations interactives.

tags : visualisation, graphiques, diagrammes, graphiques, interactif, graphiques statistiques
=====================================================================
'''

from abc import abstractmethod
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Any, Dict, List, Optional, Tuple, Union
from .StatisticalModule import StatisticalModule

class VisualizationModule(StatisticalModule):
    """
    Module de visualisation de données.
    
    Cette classe fournit des méthodes pour créer différents types
    de visualisations statistiques, incluant des graphiques, des
    diagrammes et des visualisations interactives.
    
    Attributes:
        data (Union[pd.DataFrame, pd.Series]): Données à visualiser
        figure (plt.Figure): Figure matplotlib courante
        axes (plt.Axes): Axes matplotlib courants
        style (Dict[str, Any]): Style de visualisation
        tags (List[str]): Tags associés au module
        version (str): Version du module
    """
    
    def __init__(self):
        """
        Initialise le module de visualisation.
        
        Cette méthode configure les attributs spécifiques à la
        visualisation et initialise les structures de données nécessaires.
        """
        super().__init__()
        self.data = None
        self.figure = None
        self.axes = None
        self.style = {
            'figure_size': (10, 6),
            'style': 'seaborn',
            'color_palette': 'Set2'
        }
        self.tags.extend(["visualisation", "graphiques"])
    
    @abstractmethod
    def process(self, data: Union[pd.DataFrame, pd.Series], **kwargs) -> Dict[str, Any]:
        """
        Crée la visualisation.
        
        Cette méthode doit être implémentée par les classes filles pour
        créer leur type spécifique de visualisation.
        
        Args:
            data (Union[pd.DataFrame, pd.Series]): Données à visualiser
            **kwargs: Arguments additionnels spécifiques à la visualisation
                - plot_type (str): Type de graphique à créer
                - style (Dict[str, Any]): Style de visualisation
                - params (Dict[str, Any]): Paramètres spécifiques au type de graphique
            
        Returns:
            Dict[str, Any]: Résultats de la visualisation
                - figure (plt.Figure): Figure matplotlib
                - axes (plt.Axes): Axes matplotlib
                - style (Dict[str, Any]): Style utilisé
                - params (Dict[str, Any]): Paramètres utilisés
            
        Raises:
            ValueError: Si les données sont invalides
            TypeError: Si les données ne sont pas dans le bon format
        """
        pass
    
    def set_style(self, style: Dict[str, Any]) -> None:
        """
        Configure le style de visualisation.
        
        Args:
            style (Dict[str, Any]): Paramètres de style
                - figure_size (Tuple[int, int]): Taille de la figure
                - style (str): Style matplotlib
                - color_palette (str): Palette de couleurs
            
        Raises:
            ValueError: Si les paramètres de style sont invalides
        """
        if not isinstance(style, dict):
            raise ValueError("Le style doit être un dictionnaire")
        
        self.style.update(style)
        plt.style.use(self.style['style'])
    
    def get_style(self) -> Dict[str, Any]:
        """
        Retourne le style de visualisation actuel.
        
        Returns:
            Dict[str, Any]: Paramètres de style
        """
        return self.style
    
    def save_figure(self, filename: str, **kwargs) -> None:
        """
        Sauvegarde la figure courante.
        
        Args:
            filename (str): Nom du fichier
            **kwargs: Arguments additionnels pour plt.savefig
                - dpi (int): Résolution
                - format (str): Format du fichier
                - bbox_inches (str): Gestion des marges
            
        Raises:
            ValueError: Si aucune figure n'est active
        """
        if self.figure is None:
            raise ValueError("Aucune figure n'est active")
        
        self.figure.savefig(filename, **kwargs)
    
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
        return f"Module Visualisation {self.__class__.__name__} v{self.version}"
    
    def __repr__(self) -> str:
        """
        Retourne une représentation technique du module.
        
        Returns:
            str: Représentation technique du module
        """
        return f"{self.__class__.__name__}(version={self.version})" 