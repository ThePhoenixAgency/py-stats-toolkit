"""
Genetic Lottery Optimizer - Un package d'optimisation pour les grilles de loterie
utilisant des algorithmes génétiques et des modules statistiques avancés.
"""

from .modules import (
    FrequenceAbsolueModule,
    EntropieShannonModule,
    DistributionEmpiriqueModule,
    DeviationStandardModule,
    ComptagePondereModule,
    MoyenneGlissanteModule,
    MarkovFirstOrderModule,
    ConditionalWeightModule,
    FFTModule,
    FractalModule,
    GeneticAlgorithmModule,
    EvolutionaryStrategyModule,
    HybridScoringModule,
    EnsembleLearningModule
)

from .core import (
    trainer,
    prediction_engine,
    core_engine
)

from .gui import (
    genetic_optimizer_gui,
    test_optimizer
)

__version__ = "1.0.0"
__author__ = "VotreNom"

__all__ = [
    # Modules statistiques
    'FrequenceAbsolueModule',
    'EntropieShannonModule',
    'DistributionEmpiriqueModule',
    'DeviationStandardModule',
    'ComptagePondereModule',
    'MoyenneGlissanteModule',
    'MarkovFirstOrderModule',
    'ConditionalWeightModule',
    'FFTModule',
    'FractalModule',
    'GeneticAlgorithmModule',
    'EvolutionaryStrategyModule',
    'HybridScoringModule',
    'EnsembleLearningModule',
    
    # Core modules
    'trainer',
    'prediction_engine',
    'core_engine',
    
    # GUI modules
    'genetic_optimizer_gui',
    'test_optimizer'
] 