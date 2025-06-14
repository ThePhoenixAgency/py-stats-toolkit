"""
Tests unitaires pour les fonctionnalités de base.
"""

import pytest
import numpy as np
from py_stats_toolkit import StatsToolkit

@pytest.fixture
def toolkit():
    return StatsToolkit()

@pytest.fixture
def sample_data():
    np.random.seed(42)
    return np.random.normal(0, 1, 1000)

def test_mean(toolkit, sample_data):
    """Test du calcul de la moyenne."""
    expected_mean = np.mean(sample_data)
    calculated_mean = toolkit.mean(sample_data)
    assert np.isclose(calculated_mean, expected_mean)

def test_median(toolkit, sample_data):
    """Test du calcul de la médiane."""
    expected_median = np.median(sample_data)
    calculated_median = toolkit.median(sample_data)
    assert np.isclose(calculated_median, expected_median)

def test_std(toolkit, sample_data):
    """Test du calcul de l'écart-type."""
    expected_std = np.std(sample_data)
    calculated_std = toolkit.std(sample_data)
    assert np.isclose(calculated_std, expected_std)

def test_variance(toolkit, sample_data):
    """Test du calcul de la variance."""
    expected_var = np.var(sample_data)
    calculated_var = toolkit.variance(sample_data)
    assert np.isclose(calculated_var, expected_var)

def test_linear_regression(toolkit):
    """Test de la régression linéaire."""
    x = np.array([1, 2, 3, 4, 5])
    y = 2 * x + 1 + np.random.normal(0, 0.1, 5)
    
    model = toolkit.linear_regression(x, y)
    
    assert hasattr(model, 'slope')
    assert hasattr(model, 'intercept')
    assert hasattr(model, 'r_squared')
    assert np.isclose(model.slope, 2, rtol=0.1)
    assert np.isclose(model.intercept, 1, rtol=0.1)

def test_t_test(toolkit):
    """Test du test t."""
    sample1 = np.random.normal(0, 1, 50)
    sample2 = np.random.normal(0.5, 1, 50)
    
    t_stat, p_value = toolkit.t_test(sample1, sample2)
    
    assert isinstance(t_stat, float)
    assert isinstance(p_value, float)
    assert 0 <= p_value <= 1

def test_anova(toolkit):
    """Test de l'ANOVA."""
    groups = [
        np.random.normal(0, 1, 50),
        np.random.normal(0.5, 1, 50),
        np.random.normal(1, 1, 50)
    ]
    
    f_stat, p_value = toolkit.anova(groups)
    
    assert isinstance(f_stat, float)
    assert isinstance(p_value, float)
    assert 0 <= p_value <= 1

def test_chi_square(toolkit):
    """Test du test de chi-carré."""
    observed = np.array([[10, 20], [30, 40]])
    expected = np.array([[15, 15], [25, 45]])
    
    chi2_stat, p_value = toolkit.chi_square(observed, expected)
    
    assert isinstance(chi2_stat, float)
    assert isinstance(p_value, float)
    assert 0 <= p_value <= 1

def test_data_validation(toolkit):
    """Test de la validation des données."""
    # Test avec des données valides
    valid_data = np.array([1, 2, 3, 4, 5])
    assert toolkit.validate_input(valid_data)
    
    # Test avec des données invalides
    invalid_data = np.array([1, 2, np.nan, 4, 5])
    with pytest.raises(ValueError):
        toolkit.validate_input(invalid_data)

def test_save_results(toolkit, tmp_path):
    """Test de la sauvegarde des résultats."""
    results = {
        'mean': 0.0,
        'std': 1.0,
        'test_results': {
            'p_value': 0.05
        }
    }
    
    output_file = tmp_path / "test_results.json"
    toolkit.save_results(results, str(output_file))
    
    assert output_file.exists()
    assert output_file.stat().st_size > 0 