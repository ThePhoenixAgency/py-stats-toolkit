import pytest
import numpy as np
from py_stats_toolkit.stats.probabilistes import (
    DiscreteDistribution,
    ContinuousDistribution,
    ProbabilityCalculator
)

class TestProbabilistes:
    @pytest.fixture
    def discrete_data(self):
        """Données discrètes pour les tests."""
        return {
            'values': [1, 2, 3, 4, 5],
            'probabilities': [0.1, 0.2, 0.3, 0.2, 0.2]
        }
    
    @pytest.fixture
    def continuous_data(self):
        """Données continues pour les tests."""
        return np.random.normal(0, 1, 1000)
    
    def test_discrete_distribution(self, discrete_data):
        """Test de la distribution discrète."""
        dist = DiscreteDistribution(
            discrete_data['values'],
            discrete_data['probabilities']
        )
        
        # Test de la normalisation
        assert abs(sum(dist.probabilities) - 1.0) < 1e-10
        
        # Test de la fonction de masse
        for val, prob in zip(dist.values, dist.probabilities):
            assert dist.pmf(val) == prob
            
        # Test de la fonction de répartition
        assert dist.cdf(1) == 0.1
        assert dist.cdf(2) == 0.3
        assert dist.cdf(5) == 1.0
        
        # Test de l'espérance
        expected_value = sum(v * p for v, p in zip(dist.values, dist.probabilities))
        assert abs(dist.expected_value() - expected_value) < 1e-10
        
        # Test de la variance
        variance = sum((v - expected_value)**2 * p for v, p in zip(dist.values, dist.probabilities))
        assert abs(dist.variance() - variance) < 1e-10
        
    def test_continuous_distribution(self, continuous_data):
        """Test de la distribution continue."""
        dist = ContinuousDistribution(continuous_data)
        
        # Test de la densité
        x = np.linspace(-3, 3, 100)
        pdf = dist.pdf(x)
        assert len(pdf) == len(x)
        assert np.all(pdf >= 0)
        assert abs(np.trapz(pdf, x) - 1.0) < 0.1  # Intégrale ≈ 1
        
        # Test de la fonction de répartition
        cdf = dist.cdf(x)
        assert len(cdf) == len(x)
        assert np.all((cdf >= 0) & (cdf <= 1))
        assert cdf[-1] > cdf[0]  # Fonction croissante
        
        # Test des moments
        assert abs(dist.mean() - np.mean(continuous_data)) < 1e-10
        assert abs(dist.variance() - np.var(continuous_data)) < 1e-10
        assert abs(dist.skewness() - 0) < 0.1  # Proche de 0 pour une normale
        assert abs(dist.kurtosis() - 0) < 0.1  # Proche de 0 pour une normale
        
    def test_probability_calculator(self):
        """Test du calculateur de probabilités."""
        calc = ProbabilityCalculator()
        
        # Test des probabilités conditionnelles
        p_a = 0.3
        p_b_given_a = 0.7
        p_b = 0.4
        
        p_a_given_b = calc.bayes_theorem(p_a, p_b_given_a, p_b)
        assert 0 <= p_a_given_b <= 1
        
        # Test de l'indépendance
        assert not calc.are_independent(p_a, p_b_given_a, p_b)
        
        # Test des probabilités combinées
        p_combined = calc.combined_probability([0.3, 0.4, 0.5])
        assert 0 <= p_combined <= 1
        
        # Test des probabilités mutuellement exclusives
        p_mutual = calc.mutually_exclusive_probability([0.3, 0.4, 0.5])
        assert 0 <= p_mutual <= 1
        
    def test_distribution_validation(self, discrete_data):
        """Test de la validation des distributions."""
        # Test avec probabilités négatives
        with pytest.raises(ValueError):
            DiscreteDistribution(
                discrete_data['values'],
                [-0.1, 0.2, 0.3, 0.2, 0.4]
            )
            
        # Test avec somme des probabilités ≠ 1
        with pytest.raises(ValueError):
            DiscreteDistribution(
                discrete_data['values'],
                [0.1, 0.2, 0.3, 0.2, 0.1]
            )
            
        # Test avec valeurs et probabilités de tailles différentes
        with pytest.raises(ValueError):
            DiscreteDistribution(
                discrete_data['values'][:3],
                discrete_data['probabilities']
            )
            
    def test_distribution_sampling(self, discrete_data, continuous_data):
        """Test de l'échantillonnage des distributions."""
        # Test échantillonnage discret
        dist_discrete = DiscreteDistribution(
            discrete_data['values'],
            discrete_data['probabilities']
        )
        samples = dist_discrete.sample(1000)
        assert len(samples) == 1000
        assert all(s in discrete_data['values'] for s in samples)
        
        # Test échantillonnage continu
        dist_continuous = ContinuousDistribution(continuous_data)
        samples = dist_continuous.sample(1000)
        assert len(samples) == 1000
        assert np.all(np.isfinite(samples)) 