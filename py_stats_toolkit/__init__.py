"""
py-stats-toolkit - A comprehensive statistical analysis toolkit for Python
"""

__version__ = "0.1.0"
__author__ = "PhoenixGuardianTools"
__email__ = "phoenixguardiantools@gmail.com"

from .core import StatsToolkit
from .exceptions import DataError, AnalysisError

__all__ = [
    'StatsToolkit',
    'DataError',
    'AnalysisError',
] 