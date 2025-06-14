# __init__.py
# Point d'entrée principal du package

from .modules import (
    # Modules fondamentaux
    FrequenceAbsolueModule,
    EntropieShannonModule,
    DistributionEmpiriqueModule,
    DeviationStandardModule,
    ComptagePondereModule,
    MoyenneGlissanteModule,
    
    # Liste combinée
    ALL_MODULES
)

from .abstracts import (
    BaseModule,
    AbstractStatisticsModule
)

__version__ = '1.0.0'
__author__ = 'Genetic Lottery Project Team'

__all__ = [
    'FrequenceAbsolueModule',
    'EntropieShannonModule',
    'DistributionEmpiriqueModule',
    'DeviationStandardModule',
    'ComptagePondereModule',
    'MoyenneGlissanteModule',
    'ALL_MODULES',
    'BaseModule',
    'AbstractStatisticsModule'
]
