"""
Py_Stats_Toolkit - Kit d'outils statistiques avancés
====================================================

Un toolkit complet pour l'analyse statistique avancée avec polymorphisme,
incluant des modules pour les statistiques descriptives, la régression,
la visualisation et l'analyse de données.

Modules disponibles:
- stats: Modules statistiques de base (descriptives, régression, corrélation)
- visualization: Modules de visualisation
- utils: Utilitaires et helpers
"""

# Version du toolkit
__version__ = "1.0.1"

# Imports des modules principaux
try:
    from .stats.descriptives import DescriptiveStatistics
    from .stats.regression import LinearRegression
    from .stats.correlation import CorrelationAnalysis
except ImportError:
    DescriptiveStatistics = None
    LinearRegression = None
    CorrelationAnalysis = None

try:
    from .visualization.plots import DataVisualizer
except ImportError:
    DataVisualizer = None

try:
    from .utils.data_processor import DataProcessor
    from .utils.validators import DataValidator
except ImportError:
    DataProcessor = None
    DataValidator = None


# Fonction utilitaire pour créer une instance polymorphique
def create_analysis_module(module_type: str, **kwargs):
    """
    Crée une instance de module d'analyse avec polymorphisme

    Args:
        module_type: Type de module ("descriptives", "regression", "correlation", "visualization")
        **kwargs: Arguments de configuration

    Returns:
        Instance du module correspondant
    """
    modules = {
        "descriptives": DescriptiveStatistics,
        "regression": LinearRegression,
        "correlation": CorrelationAnalysis,
        "visualization": DataVisualizer
    }

    if module_type not in modules:
        raise ValueError(f"Type de module non supporté: {module_type}. Types disponibles: {list(modules.keys())}")

    module_class = modules[module_type]
    if module_class is None:
        raise ImportError(f"Le module '{module_type}' n'est pas disponible")

    return module_class(**kwargs)


# Fonction pour analyser des données avec polymorphisme
def analyze_data(data, module_type: str = "descriptives", **kwargs):
    """
    Analyse des données avec polymorphisme automatique

    Args:
        data: Données à analyser (DataFrame, Series, List ou array)
        module_type: Type de module à utiliser
        **kwargs: Arguments additionnels

    Returns:
        Résultats de l'analyse
    """
    module = create_analysis_module(module_type, **kwargs)
    return module.analyze(data, **kwargs)


# Exports principaux
__all__ = [
    # Classes de modules
    'DescriptiveStatistics',
    'LinearRegression',
    'CorrelationAnalysis',
    'DataVisualizer',
    'DataProcessor',
    'DataValidator',

    # Fonctions utilitaires
    'create_analysis_module',
    'analyze_data',

    # Version
    '__version__'
]
