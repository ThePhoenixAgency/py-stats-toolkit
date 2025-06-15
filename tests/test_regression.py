import pytest
import numpy as np
import pandas as pd
from py_stats_toolkit.stats.regression import LinearRegression, PolynomialRegression, LogisticRegression

class TestRegression:
    @pytest.fixture
    def sample_data(self):
        """Données d'exemple pour les tests."""
        np.random.seed(42)
        X = np.random.rand(100, 2)
        y_linear = 2 * X[:, 0] + 3 * X[:, 1] + np.random.normal(0, 0.1, 100)
        y_poly = X[:, 0]**2 + 2*X[:, 1] + np.random.normal(0, 0.1, 100)
        y_logistic = (X[:, 0] + X[:, 1] > 1).astype(int)
        
        return {
            'X': X,
            'y_linear': y_linear,
            'y_poly': y_poly,
            'y_logistic': y_logistic
        }
    
    def test_linear_regression(self, sample_data):
        """Test de la régression linéaire."""
        X = sample_data['X']
        y = sample_data['y_linear']
        
        model = LinearRegression()
        model.fit(X, y)
        
        # Test des coefficients
        assert len(model.coefficients_) == X.shape[1]
        assert model.intercept_ is not None
        
        # Test des prédictions
        y_pred = model.predict(X)
        assert len(y_pred) == len(y)
        assert np.all(np.isfinite(y_pred))
        
        # Test du score R²
        r2 = model.score(X, y)
        assert 0 <= r2 <= 1
        
        # Test des résidus
        residuals = model.residuals_
        assert len(residuals) == len(y)
        assert np.mean(residuals) < 0.1  # Moyenne proche de 0
        
    def test_polynomial_regression(self, sample_data):
        """Test de la régression polynomiale."""
        X = sample_data['X']
        y = sample_data['y_poly']
        
        model = PolynomialRegression(degree=2)
        model.fit(X, y)
        
        # Test des coefficients
        assert len(model.coefficients_) > X.shape[1]  # Plus de coefficients que de variables
        assert model.intercept_ is not None
        
        # Test des prédictions
        y_pred = model.predict(X)
        assert len(y_pred) == len(y)
        assert np.all(np.isfinite(y_pred))
        
        # Test du score R²
        r2 = model.score(X, y)
        assert 0 <= r2 <= 1
        
        # Test de la validation croisée
        cv_scores = model.cross_validate(X, y, cv=5)
        assert len(cv_scores) == 5
        assert all(0 <= score <= 1 for score in cv_scores)
        
    def test_logistic_regression(self, sample_data):
        """Test de la régression logistique."""
        X = sample_data['X']
        y = sample_data['y_logistic']
        
        model = LogisticRegression()
        model.fit(X, y)
        
        # Test des coefficients
        assert len(model.coefficients_) == X.shape[1]
        assert model.intercept_ is not None
        
        # Test des prédictions
        y_pred = model.predict(X)
        assert len(y_pred) == len(y)
        assert np.all(np.isin(y_pred, [0, 1]))
        
        # Test des probabilités
        y_proba = model.predict_proba(X)
        assert y_proba.shape == (len(y), 2)
        assert np.all((y_proba >= 0) & (y_proba <= 1))
        
        # Test de la précision
        accuracy = model.score(X, y)
        assert 0 <= accuracy <= 1
        
        # Test de la matrice de confusion
        conf_matrix = model.confusion_matrix(X, y)
        assert conf_matrix.shape == (2, 2)
        assert np.all(conf_matrix >= 0)
        
    def test_regression_validation(self, sample_data):
        """Test de la validation des données."""
        X = sample_data['X']
        y = sample_data['y_linear']
        
        model = LinearRegression()
        
        # Test avec données invalides
        with pytest.raises(ValueError):
            model.fit(X, y[:-1])  # X et y de tailles différentes
            
        with pytest.raises(ValueError):
            model.fit(X, np.array(['a', 'b']))  # y non numérique
            
        with pytest.raises(ValueError):
            model.fit(np.array([[1, 2, 3], [4, 5, 6]]), y)  # X et y incompatibles
            
    def test_regression_metrics(self, sample_data):
        """Test des métriques de régression."""
        X = sample_data['X']
        y = sample_data['y_linear']
        
        model = LinearRegression()
        model.fit(X, y)
        
        # Test MSE
        mse = model.mean_squared_error(X, y)
        assert mse >= 0
        
        # Test RMSE
        rmse = model.root_mean_squared_error(X, y)
        assert rmse >= 0
        assert rmse == np.sqrt(mse)
        
        # Test MAE
        mae = model.mean_absolute_error(X, y)
        assert mae >= 0
        
        # Test R² ajusté
        adj_r2 = model.adjusted_r2(X, y)
        assert adj_r2 <= model.score(X, y)  # R² ajusté <= R² 