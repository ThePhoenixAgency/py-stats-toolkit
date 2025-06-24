"""
import unittest
Test des imports de base pour vérifier la structure du package
"""
import pytest
import numpy as np
import pandas as pd

def test_package_import():
    """Test que le package principal peut être importé"""
    try:
        import py_stats_toolkit
        assert py_stats_toolkit.__version__ == "1.0.0"
    except ImportError as e:
        pytest.fail(f"Impossible d'importer py_stats_toolkit: {e}")

def test_capsules_import():
    """Test que les capsules peuvent être importées"""
    try:
        from py_stats_toolkit.capsules.BaseCapsule import BaseCapsule
        assert BaseCapsule is not None
    except ImportError as e:
        pytest.fail(f"Impossible d'importer BaseCapsule: {e}")

def test_basic_functionality():
    """Test de base avec numpy et pandas"""
    data = np.random.normal(0, 1, 100)
    df = pd.DataFrame({'values': data})
    
    assert len(df) == 100
    assert 'values' in df.columns
    assert abs(df['values'].mean()) < 1  # La moyenne devrait être proche de 0 