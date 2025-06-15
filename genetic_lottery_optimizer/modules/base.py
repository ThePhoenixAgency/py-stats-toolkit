# base.py
# Classes de base pour les modules statistiques

from abc import ABC, abstractmethod
from collections import Counter
import numpy as np


class BaseStatisticsModule(ABC):
    """Classe de base pour tous les modules statistiques."""
    
    def __init__(self, name=None):
        self.name = name or self.__class__.__name__

    @abstractmethod
    def get_entity_scores(self, data, rules):
        """
        Calcule les scores pour les numéros et les étoiles.
        
        Args:
            data: DataFrame contenant les données historiques
            rules: Dictionnaire des règles du jeu
            
        Returns:
            tuple: (scores_numeros, scores_etoiles)
        """
        pass

    @abstractmethod
    def score_grid(self, nums, stars, rules):
        """
        Évalue une grille selon les critères du module.
        
        Args:
            nums: Liste des numéros
            stars: Liste des étoiles
            rules: Dictionnaire des règles du jeu
            
        Returns:
            float: Score entre 0 et 1
        """
        pass


class GeneratorModule(BaseStatisticsModule):
    """Module qui génère des scores pour la création de grilles."""
    
    def get_entity_scores(self, data, rules):
        num_counter = Counter([n for row in data['numeros'] for n in row])
        star_counter = Counter([s for row in data['etoiles'] for s in row])
        return num_counter, star_counter

    def score_grid(self, nums, stars, rules):
        # Par défaut, les modules générateurs ne notent pas les grilles
        return 1.0


class EvaluatorModule(BaseStatisticsModule):
    """Module qui évalue la qualité des grilles."""
    
    def get_entity_scores(self, data, rules):
        # Par défaut, les modules évaluateurs ne génèrent pas de scores
        return {}, {}

    def score_grid(self, nums, stars, rules):
        # À implémenter par les sous-classes
        raise NotImplementedError 