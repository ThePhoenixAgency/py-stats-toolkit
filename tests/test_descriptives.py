"""
Test autonome pour les statistiques descriptives (sans dépendance au package py_stats_toolkit).
"""
import unittest
import numpy as np
import pandas as pd

class DescriptiveStatistics:
    def analyze(self, data):
        if isinstance(data, list):
            data = np.array(data)
        elif isinstance(data, pd.Series):
            data = data.values
        elif isinstance(data, pd.DataFrame):
            if len(data.columns) == 1:
                data = data.iloc[:, 0].values
            else:
                return {col: self.analyze(data[col]) for col in data.columns}
        return {
            'count': len(data),
            'mean': np.mean(data),
            'std': np.std(data),
            'min': np.min(data),
            'max': np.max(data),
            'median': np.median(data),
            'q25': np.percentile(data, 25),
            'q75': np.percentile(data, 75)
        }

class TestDescriptiveStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = DescriptiveStatistics()
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.df = pd.DataFrame({'a': self.data, 'b': [2*x for x in self.data]})

    def test_analyze_list(self):
        result = self.stats.analyze(self.data)
        self.assertEqual(result['count'], 10)
        self.assertAlmostEqual(result['mean'], 5.5)
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['max'], 10)

    def test_analyze_dataframe(self):
        result = self.stats.analyze(self.df)
        self.assertIn('a', result)
        self.assertIn('b', result)
        self.assertEqual(result['a']['count'], 10)
        self.assertEqual(result['b']['max'], 20)

if __name__ == '__main__':
    unittest.main() 