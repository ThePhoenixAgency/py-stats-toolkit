import unittest
import numpy as np
from py_stats_toolkit.stats.probabilistes.ProbabilistesModule import ProbabilistesModule

class TestProbabilistes(unittest.TestCase):
    def setUp(self):
        self.module = ProbabilistesModule()
        self.data = np.random.normal(0, 1, 1000)
    
    def test_normal_distribution(self):
        result = self.module.process(self.data, distribution='normal')
        self.assertIsNotNone(result)
        params = self.module.get_distribution_params()
        self.assertEqual(len(params), 2)  # mean and std
    
    def test_exponential_distribution(self):
        exp_data = np.random.exponential(1, 1000)
        result = self.module.process(exp_data, distribution='exponential')
        self.assertIsNotNone(result)
        params = self.module.get_distribution_params()
        self.assertEqual(len(params), 1)  # scale
    
    def test_probability_density(self):
        self.module.process(self.data)
        x = np.linspace(-3, 3, 100)
        pdf = self.module.get_probability_density(x)
        self.assertEqual(len(pdf), len(x))
        self.assertTrue(np.all(pdf >= 0))
    
    def test_cumulative_distribution(self):
        self.module.process(self.data)
        x = np.linspace(-3, 3, 100)
        cdf = self.module.get_cumulative_distribution(x)
        self.assertEqual(len(cdf), len(x))
        self.assertTrue(np.all((cdf >= 0) & (cdf <= 1)))
    
    def test_invalid_distribution(self):
        with self.assertRaises(ValueError):
            self.module.process(self.data, distribution='invalid')

if __name__ == '__main__':
    unittest.main() 