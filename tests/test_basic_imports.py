"""
Tests des imports de base pour vérifier les dépendances essentielles.
"""
import unittest
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

class TestBasicImports(unittest.TestCase):
    def test_numpy(self):
        data = np.random.normal(0, 1, 100)
        self.assertEqual(len(data), 100)
        self.assertIsInstance(data, np.ndarray)

    def test_pandas(self):
        df = pd.DataFrame({'values': [1, 2, 3, 4, 5]})
        self.assertEqual(len(df), 5)
        self.assertIn('values', df.columns)

    def test_sklearn(self):
        X = np.random.randn(100, 2)
        y = np.dot(X, [1.0, 2.0]) + np.random.normal(0, 0.1, 100)
        model = LinearRegression()
        model.fit(X, y)
        predictions = model.predict(X)
        mse = mean_squared_error(y, predictions)
        self.assertGreaterEqual(mse, 0)
        self.assertEqual(len(predictions), len(y))

    def test_matplotlib(self):
        fig, ax = plt.subplots()
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_title("Test Plot")
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        plt.close(fig)

if __name__ == '__main__':
    unittest.main() 