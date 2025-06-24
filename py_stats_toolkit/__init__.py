"""
Py_Stats_Toolkit - Kit d'outils statistiques avancés
====================================================

Un toolkit complet pour l'analyse statistique avancée avec polymorphisme,
incluant des modules pour les statistiques descriptives, la détection d'anomalies,
la validation temporelle et le scoring avancé.

Modules disponibles:
- advanced: Modules statistiques avancés avec polymorphisme
- analysis: Modules d'analyse temporelle
- detection: Modules de détection d'anomalies
"""

# Version du toolkit
__version__ = "1.0.0"

# Imports des modules principaux avec polymorphisme (avec gestion d'erreurs)
try:
    from .advanced import AdvancedStatisticsEngine, AdvancedScoringEngine
except ImportError:
    AdvancedStatisticsEngine = None
    AdvancedScoringEngine = None

try:
    from .detection import AnomalyDetectionEngine
except ImportError:
    AnomalyDetectionEngine = None

try:
    from .analysis import TemporalValidationEngine
except ImportError:
    TemporalValidationEngine = None

# Imports des classes de base
try:
    from .Abstracts.AbstractClassBase import StatisticalModule, TimeSeriesModule, RandomProcessModule
except ImportError:
    StatisticalModule = None
    TimeSeriesModule = None
    RandomProcessModule = None

# Fonction utilitaire pour créer une instance polymorphique
def create_statistical_engine(engine_type: str, **kwargs):
    """
    Crée une instance d'engine statistique avec polymorphisme
    
    Args:
        engine_type: Type d'engine ("statistics", "anomaly", "validation", "scoring")
        **kwargs: Arguments de configuration
        
    Returns:
        Instance de l'engine correspondant
    """
    engines = {
        "statistics": AdvancedStatisticsEngine,
        "anomaly": AnomalyDetectionEngine,
        "validation": TemporalValidationEngine,
        "scoring": AdvancedScoringEngine
    }
    
    if engine_type not in engines:
        raise ValueError(f"Type d'engine non supporté: {engine_type}. Types disponibles: {list(engines.keys())}")
    
    engine_class = engines[engine_type]
    if engine_class is None:
        raise ImportError(f"Le module pour l'engine '{engine_type}' n'est pas disponible")
    
    return engine_class(**kwargs)

# Fonction pour analyser des données avec polymorphisme
def analyze_data(data, engine_type: str = "statistics", **kwargs):
    """
    Analyse des données avec polymorphisme automatique
    
    Args:
        data: Données à analyser (DataFrame, Series, List ou array)
        engine_type: Type d'engine à utiliser
        **kwargs: Arguments additionnels
        
    Returns:
        Résultats de l'analyse
    """
    engine = create_statistical_engine(engine_type, **kwargs)
    return engine.process(data, **kwargs)

# Exports principaux
__all__ = [
    # Classes d'engines avec polymorphisme
    'AdvancedStatisticsEngine',
    'AnomalyDetectionEngine', 
    'TemporalValidationEngine',
    'AdvancedScoringEngine',
    
    # Classes de base
    'StatisticalModule',
    'TimeSeriesModule',
    'RandomProcessModule',
    
    # Fonctions utilitaires
    'create_statistical_engine',
    'analyze_data',
    
    # Version
    '__version__'
] 