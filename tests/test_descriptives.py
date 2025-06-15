import unittest
import numpy as np
import pandas as pd
from py_stats_toolkit.stats.descriptives.MoyenneGlissanteModule import MoyenneGlissanteModule
import pytest
from py_stats_toolkit.stats.descriptives import DescriptiveStatistics

class TestMoyenneGlissante(unittest.TestCase):
    def setUp(self):
        self.module = MoyenneGlissanteModule()
        self.data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    def test_process(self):
        result = self.module.process(self.data, window_size=3)
        expected = pd.Series([np.nan, np.nan, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
        pd.testing.assert_series_equal(result, expected)
    
    def test_invalid_data(self):
        with self.assertRaises(TypeError):
            self.module.process("invalid_data")
    
    def test_window_size(self):
        self.module.process(self.data, window_size=5)
        self.assertEqual(self.module.get_window_size(), 5)

class TestDescriptives:
    @pytest.fixture
    def sample_data(self):
        """Données d'exemple pour les tests."""
        np.random.seed(42)
        n = 100
        normal_data = np.random.normal(0, 1, n)
        skewed_data = np.random.exponential(1, n)
        
        return pd.DataFrame({
            'normal': normal_data,
            'skewed': skewed_data
        })
    
    def test_central_tendency(self, sample_data):
        """Test des mesures de tendance centrale."""
        stats = DescriptiveStatistics()
        
        # Test moyenne
        mean = stats.mean(sample_data['normal'])
        assert abs(mean - np.mean(sample_data['normal'])) < 1e-10
        
        # Test médiane
        median = stats.median(sample_data['normal'])
        assert abs(median - np.median(sample_data['normal'])) < 1e-10
        
        # Test mode
        mode = stats.mode(sample_data['normal'])
        assert isinstance(mode, (int, float))
        
        # Test moyenne tronquée
        trimmed_mean = stats.trimmed_mean(sample_data['normal'], proportion=0.1)
        assert abs(trimmed_mean - np.mean(sample_data['normal'])) < 1
        
    def test_dispersion(self, sample_data):
        """Test des mesures de dispersion."""
        stats = DescriptiveStatistics()
        
        # Test variance
        var = stats.variance(sample_data['normal'])
        assert abs(var - np.var(sample_data['normal'])) < 1e-10
        
        # Test écart-type
        std = stats.standard_deviation(sample_data['normal'])
        assert abs(std - np.std(sample_data['normal'])) < 1e-10
        
        # Test écart interquartile
        iqr = stats.interquartile_range(sample_data['normal'])
        q75, q25 = np.percentile(sample_data['normal'], [75, 25])
        assert abs(iqr - (q75 - q25)) < 1e-10
        
        # Test coefficient de variation
        cv = stats.coefficient_of_variation(sample_data['normal'])
        assert cv > 0
        
    def test_shape(self, sample_data):
        """Test des mesures de forme."""
        stats = DescriptiveStatistics()
        
        # Test asymétrie
        skewness = stats.skewness(sample_data['normal'])
        assert abs(skewness) < 0.5  # Proche de 0 pour une normale
        
        skewness_skewed = stats.skewness(sample_data['skewed'])
        assert skewness_skewed > 0  # Positif pour une distribution asymétrique
        
        # Test aplatissement
        kurtosis = stats.kurtosis(sample_data['normal'])
        assert abs(kurtosis) < 0.5  # Proche de 0 pour une normale
        
        # Test test de normalité
        is_normal = stats.is_normal(sample_data['normal'])
        assert isinstance(is_normal, bool)
        
    def test_quantiles(self, sample_data):
        """Test des quantiles."""
        stats = DescriptiveStatistics()
        
        # Test quartiles
        q1, q2, q3 = stats.quartiles(sample_data['normal'])
        assert q1 < q2 < q3
        
        # Test percentiles
        p90 = stats.percentile(sample_data['normal'], 90)
        assert p90 > np.median(sample_data['normal'])
        
        # Test déciles
        deciles = stats.deciles(sample_data['normal'])
        assert len(deciles) == 9
        assert all(deciles[i] < deciles[i+1] for i in range(len(deciles)-1))
        
    def test_summary(self, sample_data):
        """Test du résumé statistique."""
        stats = DescriptiveStatistics()
        
        # Test résumé complet
        summary = stats.summary(sample_data['normal'])
        assert isinstance(summary, dict)
        assert all(key in summary for key in ['mean', 'std', 'min', 'max', 'quartiles'])
        
        # Test résumé par colonne
        summary_df = stats.summary_by_column(sample_data)
        assert isinstance(summary_df, pd.DataFrame)
        assert all(col in summary_df.columns for col in ['mean', 'std', 'min', 'max'])
        
    def test_data_validation(self, sample_data):
        """Test de la validation des données."""
        stats = DescriptiveStatistics()
        
        # Test avec données manquantes
        data_with_nan = sample_data.copy()
        data_with_nan.iloc[0, 0] = np.nan
        
        with pytest.raises(ValueError):
            stats.mean(data_with_nan['normal'])
            
        # Test avec données non numériques
        data_with_str = sample_data.copy()
        data_with_str.iloc[0, 0] = 'a'
        
        with pytest.raises(ValueError):
            stats.mean(data_with_str['normal'])
            
        # Test avec données vides
        with pytest.raises(ValueError):
            stats.mean(pd.Series([]))
            
    def test_outliers(self, sample_data):
        """Test de la détection des outliers."""
        stats = DescriptiveStatistics()
        
        # Test détection par IQR
        outliers = stats.detect_outliers_iqr(sample_data['normal'])
        assert isinstance(outliers, pd.Series)
        assert outliers.dtype == bool
        
        # Test détection par Z-score
        outliers = stats.detect_outliers_zscore(sample_data['normal'])
        assert isinstance(outliers, pd.Series)
        assert outliers.dtype == bool
        
        # Test détection par MAD
        outliers = stats.detect_outliers_mad(sample_data['normal'])
        assert isinstance(outliers, pd.Series)
        assert outliers.dtype == bool

if __name__ == '__main__':
    unittest.main() 