"""
Tests for refactored modules to verify SOLID principles and DRY compliance.
Tests verify that business logic separation works correctly.
"""

import unittest

import numpy as np
import pandas as pd

from py_stats_toolkit.stats.correlation.CorrelationModule import CorrelationModule
from py_stats_toolkit.stats.descriptives.MoyenneGlissanteModule import (
    MoyenneGlissanteModule,
)
from py_stats_toolkit.stats.frequence.FrequenceModule import FrequenceModule
from py_stats_toolkit.stats.probabilistes.ProbabilistesModule import ProbabilistesModule
from py_stats_toolkit.stats.regression.RegressionModule import RegressionModule
from py_stats_toolkit.stats.variance.VarianceModule import VarianceModule


class TestRefactoredCorrelationModule(unittest.TestCase):
    """Test refactored CorrelationModule."""

    def setUp(self):
        self.df = pd.DataFrame(
            {"x": np.arange(10), "y": np.arange(10) * 2, "z": np.random.randn(10)}
        )
        self.module = CorrelationModule()

    def test_process_returns_correlation_matrix(self):
        result = self.module.process(self.df, method="pearson")
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (3, 3))

    def test_get_correlation_pairs(self):
        self.module.process(self.df, method="pearson")
        pairs = self.module.get_correlation_pairs(threshold=0.5)
        self.assertIsInstance(pairs, list)


class TestRefactoredRegressionModule(unittest.TestCase):
    """Test refactored RegressionModule."""

    def setUp(self):
        np.random.seed(42)
        self.df = pd.DataFrame(
            {
                "x1": np.random.randn(50),
                "x2": np.random.randn(50),
                "y": np.random.randn(50),
            }
        )
        self.module = RegressionModule()

    def test_linear_regression(self):
        result = self.module.process(
            self.df, ["x1", "x2"], "y", regression_type="linear"
        )
        self.assertIn("coefficients", result)
        self.assertIn("intercept", result)
        self.assertIn("r2_score", result)

    def test_predict(self):
        self.module.process(self.df, ["x1", "x2"], "y", regression_type="linear")
        predictions = self.module.predict(self.df[["x1", "x2"]])
        self.assertEqual(len(predictions), len(self.df))


class TestRefactoredMoyenneGlissanteModule(unittest.TestCase):
    """Test refactored MoyenneGlissanteModule."""

    def setUp(self):
        self.data = np.arange(20)
        self.module = MoyenneGlissanteModule()

    def test_process_moving_average(self):
        result = self.module.process(self.data, window_size=5)
        self.assertIsInstance(result, pd.Series)
        self.assertEqual(len(result), len(self.data))

    def test_get_window_size(self):
        self.module.process(self.data, window_size=3)
        self.assertEqual(self.module.get_window_size(), 3)


class TestRefactoredFrequenceModule(unittest.TestCase):
    """Test refactored FrequenceModule."""

    def setUp(self):
        self.data = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        self.module = FrequenceModule()

    def test_process_frequency(self):
        result = self.module.process(self.data, normalize=False)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn("Frequency", result.columns)

    def test_process_relative_frequency(self):
        result = self.module.process(self.data, normalize=True)
        self.assertIn("Relative_Frequency", result.columns)


class TestRefactoredVarianceModule(unittest.TestCase):
    """Test refactored VarianceModule."""

    def setUp(self):
        np.random.seed(42)
        self.df = pd.DataFrame(
            {
                "group": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
                "value": np.random.randn(9),
            }
        )
        self.module = VarianceModule()

    def test_anova(self):
        result = self.module.process(self.df, "group", "value", test_type="anova")
        self.assertIn("f_statistic", result)
        self.assertIn("p_value", result)


class TestRefactoredProbabilistesModule(unittest.TestCase):
    """Test refactored ProbabilistesModule."""

    def setUp(self):
        np.random.seed(42)
        self.data = np.random.normal(0, 1, 100)
        self.module = ProbabilistesModule()

    def test_fit_normal_distribution(self):
        result = self.module.process(self.data, distribution="normal")
        self.assertIsNotNone(result)

    def test_get_pdf(self):
        self.module.process(self.data, distribution="normal")
        x = np.array([0, 1, 2])
        pdf = self.module.get_pdf(x)
        self.assertEqual(len(pdf), len(x))


if __name__ == "__main__":
    unittest.main()
