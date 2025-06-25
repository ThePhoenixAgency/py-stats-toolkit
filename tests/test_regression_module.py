"""
Tests unitaires pour la régression linéaire avec sklearn.
"""
import unittest
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class TestRegressionModule(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.X = np.random.randn(100, 3)
        self.y = np.dot(self.X, [1.5, -0.5, 2.0]) + np.random.normal(0, 0.1, 100)

    def test_linear_regression_fit(self):
        model = LinearRegression()
        model.fit(self.X, self.y)
        self.assertTrue(hasattr(model, 'coef_'))
        self.assertTrue(hasattr(model, 'intercept_'))
        self.assertEqual(len(model.coef_), 3)

    def test_linear_regression_predict(self):
        model = LinearRegression()
        model.fit(self.X, self.y)
        predictions = model.predict(self.X)
        self.assertEqual(len(predictions), len(self.y))
        self.assertIsInstance(predictions, np.ndarray)

    def test_regression_metrics(self):
        model = LinearRegression()
        model.fit(self.X, self.y)
        predictions = model.predict(self.X)
        mse = mean_squared_error(self.y, predictions)
        r2 = r2_score(self.y, predictions)
        self.assertIsInstance(mse, float)
        self.assertIsInstance(r2, float)
        self.assertGreaterEqual(mse, 0)
        self.assertLessEqual(r2, 1)

    def test_regression_coefficients(self):
        model = LinearRegression()
        model.fit(self.X, self.y)
        self.assertTrue(np.all(np.isfinite(model.coef_)))
        self.assertTrue(np.isfinite(model.intercept_))
        self.assertEqual(model.coef_.shape, (3,))

if __name__ == '__main__':
    unittest.main() 