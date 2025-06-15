# Fonctions à utiliser avec le multiprocessing :
def square(x):
    return {'squared': x ** 2}

def complex_operation(df):
    return {
        'sum': df.sum().to_dict(),
        'mean': df.mean().to_dict(),
        'std': df.std().to_dict()
    }

'''
=====================================================================
File : test_parallel.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Tests unitaires pour le module de traitement parallèle.
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd
from py_stats_toolkit.utils.parallel import ParallelProcessor

def test_parallel_processor_initialization():
    """Test l'initialisation du processeur parallèle."""
    processor = ParallelProcessor()
    assert processor.n_workers > 0
    assert processor.use_threading is False
    assert processor.chunk_size == 1000

def test_parallel_processor_custom_initialization():
    """Test l'initialisation avec des paramètres personnalisés."""
    processor = ParallelProcessor(n_workers=4, use_threading=True, chunk_size=500)
    assert processor.n_workers == 4
    assert processor.use_threading is True
    assert processor.chunk_size == 500

def test_process_data_empty():
    """Test le traitement avec des données vides."""
    processor = ParallelProcessor()
    data = pd.DataFrame()
    with pytest.raises(ValueError):
        processor.process_data(data, lambda x: x)

def test_process_data_simple():
    """Test le traitement simple de données."""
    processor = ParallelProcessor(n_workers=2)
    data = pd.Series([1, 2, 3, 4, 5])
    results = processor.process_data(data, square)
    assert 'squared' in results
    assert len(results['squared']) == len(data)

def test_process_data_complex():
    """Test le traitement de données complexes."""
    processor = ParallelProcessor(n_workers=2)
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    })
    results = processor.process_data(data, complex_operation)
    assert all(key in results for key in ['sum', 'mean', 'std'])
    assert all(key in results['sum'] for key in ['A', 'B'])

def test_combine_results():
    """Test la combinaison des résultats."""
    processor = ParallelProcessor()
    results = [
        {'sum': 10, 'data': np.array([1, 2])},
        {'sum': 20, 'data': np.array([3, 4])}
    ]
    
    combined = processor._combine_results(results)
    assert combined['sum'] == 30
    assert len(combined['data']) == 4

def test_string_representation():
    """Test la représentation textuelle."""
    processor = ParallelProcessor(n_workers=4, use_threading=True)
    assert str(processor) == "ParallelProcessor(n_workers=4, use_threading=True)"

def test_repr_representation():
    """Test la représentation technique."""
    processor = ParallelProcessor(n_workers=4, use_threading=True, chunk_size=500)
    assert repr(processor) == "ParallelProcessor(n_workers=4, use_threading=True, chunk_size=500)" 