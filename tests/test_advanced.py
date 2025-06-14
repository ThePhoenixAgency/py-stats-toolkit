"""
Tests unitaires pour les fonctionnalités avancées.
"""

import pytest
import numpy as np
import pandas as pd
from py_stats_toolkit import StatsToolkit

@pytest.fixture
def toolkit():
    return StatsToolkit()

@pytest.fixture
def sample_dataframe():
    """Crée un DataFrame de test avec des données corrélées."""
    np.random.seed(42)
    n_samples = 100
    x = np.random.normal(0, 1, n_samples)
    y = 2 * x + np.random.normal(0, 0.1, n_samples)
    z = -x + np.random.normal(0, 0.1, n_samples)
    
    return pd.DataFrame({
        'x': x,
        'y': y,
        'z': z
    })

def test_polynomial_regression(toolkit):
    """Test de la régression polynomiale."""
    x = np.array([1, 2, 3, 4, 5])
    y = 2 * x**2 + 3 * x + 1 + np.random.normal(0, 0.1, 5)
    
    model = toolkit.polynomial_regression(x, y, degree=2)
    
    assert hasattr(model, 'coefficients')
    assert len(model.coefficients) == 3
    assert hasattr(model, 'r_squared')
    assert 0 <= model.r_squared <= 1

def test_multiple_regression(toolkit, sample_dataframe):
    """Test de la régression multiple."""
    X = sample_dataframe[['x', 'y']]
    y = sample_dataframe['z']
    
    model = toolkit.multiple_regression(X, y)
    
    assert hasattr(model, 'coefficients')
    assert len(model.coefficients) == 2
    assert hasattr(model, 'r_squared')
    assert 0 <= model.r_squared <= 1

def test_correlation_matrix(toolkit, sample_dataframe):
    """Test de la matrice de corrélation."""
    corr_matrix = toolkit.correlation_matrix(sample_dataframe)
    
    assert isinstance(corr_matrix, pd.DataFrame)
    assert corr_matrix.shape == (3, 3)
    assert np.all(np.diag(corr_matrix) == 1.0)
    assert np.all(corr_matrix >= -1) and np.all(corr_matrix <= 1)

def test_descriptive_stats(toolkit, sample_dataframe):
    """Test des statistiques descriptives."""
    stats = toolkit.descriptive_stats(sample_dataframe)
    
    assert isinstance(stats, dict)
    assert all(col in stats for col in sample_dataframe.columns)
    for col_stats in stats.values():
        assert 'mean' in col_stats
        assert 'std' in col_stats
        assert 'min' in col_stats
        assert 'max' in col_stats

def test_plot_functions(toolkit, sample_dataframe):
    """Test des fonctions de visualisation."""
    # Test plot_histogram
    fig = toolkit.plot_histogram(sample_dataframe['x'])
    assert fig is not None
    
    # Test plot_scatter
    fig = toolkit.plot_scatter(sample_dataframe['x'], sample_dataframe['y'])
    assert fig is not None
    
    # Test plot_boxplot
    fig = toolkit.plot_boxplot(sample_dataframe)
    assert fig is not None

def test_data_quality_check(toolkit, sample_dataframe):
    """Test de la vérification de la qualité des données."""
    # Test avec des données propres
    quality_report = toolkit.check_data_quality(sample_dataframe)
    assert isinstance(quality_report, dict)
    assert 'missing_values' in quality_report
    assert 'outliers' in quality_report
    
    # Test avec des données problématiques
    df_with_issues = sample_dataframe.copy()
    df_with_issues.loc[0, 'x'] = np.nan
    df_with_issues.loc[1, 'y'] = 1000  # Valeur aberrante
    
    quality_report = toolkit.check_data_quality(df_with_issues)
    assert quality_report['missing_values']['x'] > 0
    assert len(quality_report['outliers']['y']) > 0

def test_analysis_metadata(toolkit):
    """Test de la gestion des métadonnées d'analyse."""
    metadata = {
        'title': 'Test Analysis',
        'description': 'Test analysis description',
        'author': 'Test Author',
        'date': '2024-01-01'
    }
    
    toolkit.set_analysis_metadata(**metadata)
    retrieved_metadata = toolkit.get_analysis_metadata()
    
    assert retrieved_metadata == metadata

def test_error_handling(toolkit):
    """Test de la gestion des erreurs."""
    # Test avec des données invalides
    with pytest.raises(ValueError):
        toolkit.mean([1, 2, 'invalid', 4])
    
    # Test avec des dimensions incompatibles
    with pytest.raises(ValueError):
        toolkit.linear_regression([1, 2, 3], [1, 2])
    
    # Test avec des données manquantes
    with pytest.raises(ValueError):
        toolkit.validate_input(np.array([1, np.nan, 3]))

def test_performance(toolkit):
    """Test de performance avec de grandes quantités de données."""
    n_samples = 10000
    data = np.random.normal(0, 1, n_samples)
    
    import time
    start_time = time.time()
    
    # Test des performances des calculs statistiques
    toolkit.mean(data)
    toolkit.std(data)
    toolkit.variance(data)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Vérifier que les calculs sont effectués en moins d'une seconde
    assert execution_time < 1.0 