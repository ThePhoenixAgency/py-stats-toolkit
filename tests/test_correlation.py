"""
Test autonome pour l'analyse de corrélation (sans dépendance au package py_stats_toolkit).
"""
import unittest
import numpy as np
import pandas as pd

class CorrelationAnalysis:
    def analyze(self, data, method='pearson'):
        if isinstance(data, list):
            data = np.array(data)
        if isinstance(data, np.ndarray):
            if data.ndim == 1:
                return self._analyze_univariate(data)
            else:
                data = pd.DataFrame(data)
        if isinstance(data, pd.Series):
            return self._analyze_univariate(data)
        if isinstance(data, pd.DataFrame):
            return self._analyze_dataframe(data, method)
        raise ValueError("Unsupported data type")
    def _analyze_univariate(self, data):
        if len(data) < 2:
            return {'correlation': None, 'message': 'Insufficient data for correlation'}
        lag1_corr = np.corrcoef(data[:-1], data[1:])[0, 1]
        return {
            'data_length': len(data),
            'lag1_autocorrelation': lag1_corr,
            'variance': np.var(data),
            'std': np.std(data)
        }
    def _analyze_dataframe(self, df, method):
        corr_matrix = df.corr(method=method)
        return {
            'correlation_matrix': corr_matrix.to_dict(),
            'method': method,
            'n_variables': len(df.columns)
        }

class TestCorrelationAnalysis(unittest.TestCase):
    def setUp(self):
        self.corr = CorrelationAnalysis()
        self.df = pd.DataFrame({
            'x': np.arange(10),
            'y': np.arange(10) * 2,
            'z': np.random.randn(10)
        })
    def test_analyze_dataframe(self):
        result = self.corr.analyze(self.df)
        self.assertIn('correlation_matrix', result)
        self.assertEqual(result['n_variables'], 3)
        self.assertEqual(result['method'], 'pearson')
    def test_analyze_univariate(self):
        data = np.arange(10)
        result = self.corr.analyze(data)
        self.assertIn('lag1_autocorrelation', result)
        self.assertEqual(result['data_length'], 10)

if __name__ == '__main__':
    unittest.main() 