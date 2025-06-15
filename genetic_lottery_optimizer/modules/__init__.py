# modules/__init__.py
# Expose tous les modules statistiques

from .all_stat_modules import (
    # Modules fondamentaux
    FrequenceAbsolueModule,
    EntropieShannonModule,
    DistributionEmpiriqueModule,
    DeviationStandardModule,
    ComptagePondereModule,
    MoyenneGlissanteModule,
    
    # Modules évolutifs
    EvolutionGenetiqueModule,
    SelectionNaturelleModule,
    
    # Modules cycliques
    CyclesTemporelsModule,
    PatternsCycliquesModule,
    
    # Modules avancés
    AnalyseAvanceeModule,
    PredictionHybrideModule,
    
    # Modules probabilistes
    ProbabiliteConditionnelleModule,
    BayesModule,
    
    # Modules personnalisés
    ModulePersonnalise1,
    ModulePersonnalise2,
    
    # Modules topologiques
    FourierFFTModule,
    FractaleAutosimilaireModule,
    TheorieDesJeuxModule,
    ClustersNumeriquesModule,
    FibonacciRecurrentModule,
    TopologieCombinatoireModule,
    
    # Modules hybrides
    ScoreCompositeMultijeuxModule,
    RecoupementMultiLotteriesModule,
    HistoriqueGrillesGagnantesModule,
    CorrelationJeuxDatesModule,
    
    # Modules génétiques
    AlgoGenetiqueModule,
    RollbackAdaptatifModule,
    MultiModeleScoreMoyenModule,
    SelectionNaturelleModule,
    BoostAdaptatifModule,
    
    # Liste combinée
    ALL_MODULES
)

# Expose les classes de base
from .base import (
    BaseStatisticsModule,
    GeneratorModule,
    EvaluatorModule
)
