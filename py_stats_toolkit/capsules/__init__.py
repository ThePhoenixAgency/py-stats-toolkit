"""
=====================================================================
File : __init__.py
=====================================================================
version : 2.0.0 (Refactored - Backward Compatibility)
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Backward compatibility module for capsules.
This module is deprecated. Use py_stats_toolkit.core.base.StatisticalModule instead.

tags : capsule, deprecated, backward-compatibility
=====================================================================
"""

# Import new base class for backward compatibility
from py_stats_toolkit.core.base import StatisticalModule

# Alias for backward compatibility
BaseCapsule = StatisticalModule

__all__ = ['BaseCapsule', 'StatisticalModule']
