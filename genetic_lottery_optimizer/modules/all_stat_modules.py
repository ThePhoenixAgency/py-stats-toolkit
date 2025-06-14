# all_stat_modules.py
# Point d'entrée pour tous les modules statistiques

from .fondamentaux import (
    FrequenceAbsolueModule,
    MoyenneGlissanteModule
)

from .avances import (
    EntropieShannonModule,
    DistributionEmpiriqueModule,
    DeviationStandardModule,
    ComptagePondereModule,
    FFTModule,
    FractalModule
)

from .evolutifs import (
    BoostAdaptiveModule,
    MultiModelScoringModule
)

from .cycliques import (
    SeasonalPatternModule,
    CyclicWeightModule,
    PeriodicAnalysisModule
)

from .probabilistes import (
    MarkovFirstOrderModule,
    ConditionalWeightModule
)

from .personnalises import (
    CrossGameScoreModule,
    WinningPatternMemoryModule
)

from .topologiques import (
    TopologicalPatternModule,
    NetworkAnalysisModule
)

from .hybrides import (
    HybridScoringModule,
    EnsembleLearningModule
)

from .genetiques import (
    GeneticAlgorithmModule,
    EvolutionaryStrategyModule
)

# Liste de tous les modules disponibles
ALL_MODULES = [
    # Modules fondamentaux
    FrequenceAbsolueModule(),
    MoyenneGlissanteModule(),
    
    # Modules avancés
    EntropieShannonModule(),
    DistributionEmpiriqueModule(),
    DeviationStandardModule(),
    ComptagePondereModule(),
    FFTModule(),
    FractalModule(),
    
    # Modules évolutifs
    BoostAdaptiveModule(),
    MultiModelScoringModule(),
    
    # Modules cycliques
    SeasonalPatternModule(),
    CyclicWeightModule(),
    PeriodicAnalysisModule(),
    
    # Modules probabilistes
    MarkovFirstOrderModule(),
    ConditionalWeightModule(),
    
    # Modules personnalisés
    CrossGameScoreModule(),
    WinningPatternMemoryModule(),
    
    # Modules topologiques
    TopologicalPatternModule(),
    NetworkAnalysisModule(),
    
    # Modules hybrides
    HybridScoringModule(),
    EnsembleLearningModule(),
    
    # Modules génétiques
    GeneticAlgorithmModule(),
    EvolutionaryStrategyModule()
] 