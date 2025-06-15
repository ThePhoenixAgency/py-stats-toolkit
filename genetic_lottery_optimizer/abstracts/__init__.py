# abstracts/__init__.py
# Expose les classes abstraites

from .AbstractModule import BaseModule
from .AbstractClassStatistics import AbstractStatisticsModule

__all__ = [
    'BaseModule',
    'AbstractStatisticsModule'
] 