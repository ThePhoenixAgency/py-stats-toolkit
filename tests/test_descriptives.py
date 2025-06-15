import unittest
import numpy as np
import pandas as pd
from py_stats_toolkit.stats.descriptives.MoyenneGlissanteModule import MoyenneGlissanteModule

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

if __name__ == '__main__':
    unittest.main() 