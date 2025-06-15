import unittest
import numpy as np
import pandas as pd
from py_stats_toolkit.stats.correlation.CorrelationModule import CorrelationModule

class TestCorrelation(unittest.TestCase):
    def setUp(self):
        self.module = CorrelationModule()
        self.data = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [2, 4, 6, 8, 10],
            'C': [1, 3, 2, 4, 5]
        })
    
    def test_pearson_correlation(self):
        result = self.module.process(self.data, method='pearson')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (3, 3))
        self.assertAlmostEqual(result.loc['A', 'B'], 1.0)
    
    def test_spearman_correlation(self):
        result = self.module.process(self.data, method='spearman')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (3, 3))
    
    def test_correlation_pairs(self):
        self.module.process(self.data)
        pairs = self.module.get_correlation_pairs(threshold=0.5)
        self.assertIsInstance(pairs, list)
        self.assertTrue(len(pairs) > 0)
    
    def test_invalid_data(self):
        with self.assertRaises(TypeError):
            self.module.process(np.array([1, 2, 3]))

if __name__ == '__main__':
    unittest.main() 