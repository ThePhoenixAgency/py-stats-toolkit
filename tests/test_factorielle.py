import unittest
import numpy as np
import pandas as pd
from py_stats_toolkit.stats.factorielle.FactorielleModule import FactorielleModule

class TestFactorielle(unittest.TestCase):
    def setUp(self):
        self.factorielle = FactorielleModule()
        
        # Données de test pour l'ACP
        np.random.seed(42)
        n_samples = 100
        self.pca_data = pd.DataFrame({
            'var1': np.random.normal(0, 1, n_samples),
            'var2': np.random.normal(0, 1, n_samples),
            'var3': np.random.normal(0, 1, n_samples),
            'var4': np.random.normal(0, 1, n_samples)
        })
        
        # Données de test pour l'analyse factorielle
        self.fa_data = pd.DataFrame({
            'var1': np.random.normal(0, 1, n_samples),
            'var2': np.random.normal(0, 1, n_samples),
            'var3': np.random.normal(0, 1, n_samples),
            'var4': np.random.normal(0, 1, n_samples)
        })
    
    def test_pca(self):
        """Test de l'analyse en composantes principales."""
        result = self.factorielle.process(
            self.pca_data,
            method="pca",
            n_components=2
        )
        
        self.assertEqual(result['Type'], 'ACP')
        self.assertIn('Composantes', result)
        self.assertIn('Chargements', result)
        self.assertIn('Variance expliquée', result)
        self.assertEqual(len(result['Composantes']), 2)
    
    def test_factor_analysis(self):
        """Test de l'analyse factorielle."""
        result = self.factorielle.process(
            self.fa_data,
            method="factor_analysis",
            n_factors=2
        )
        
        self.assertEqual(result['Type'], 'Analyse factorielle')
        self.assertIn('Facteurs', result)
        self.assertIn('Chargements', result)
        self.assertIn('Variance expliquée', result)
        self.assertEqual(len(result['Facteurs']), 2)
    
    def test_quality_metrics(self):
        """Test des métriques de qualité."""
        # Entraînement du modèle
        self.factorielle.process(
            self.pca_data,
            method="pca",
            n_components=2
        )
        
        metrics = self.factorielle.get_quality_metrics()
        self.assertIn('Variance totale expliquée', metrics)
        self.assertIn('Qualité de représentation', metrics)
        self.assertIn('Contributions', metrics)
    
    def test_transform(self):
        """Test de la transformation des données."""
        # Entraînement du modèle
        self.factorielle.process(
            self.pca_data,
            method="pca",
            n_components=2
        )
        
        # Nouvelles données pour la transformation
        new_data = pd.DataFrame({
            'var1': np.random.normal(0, 1, 10),
            'var2': np.random.normal(0, 1, 10),
            'var3': np.random.normal(0, 1, 10),
            'var4': np.random.normal(0, 1, 10)
        })
        
        transformed = self.factorielle.transform(new_data)
        self.assertEqual(transformed.shape[1], 2)
    
    def test_get_significant_contributions(self):
        """Test de l'extraction des contributions significatives."""
        # Entraînement du modèle
        self.factorielle.process(
            self.pca_data,
            method="pca",
            n_components=2
        )
        
        contributions = self.factorielle.get_significant_contributions(threshold=0.5)
        self.assertIsInstance(contributions, dict)
        self.assertIn('Variables', contributions)
        self.assertIn('Composantes', contributions)
    
    def test_invalid_method(self):
        """Test avec une méthode invalide."""
        with self.assertRaises(ValueError):
            self.factorielle.process(
                self.pca_data,
                method="invalid_method",
                n_components=2
            )
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.factorielle.process(
                "invalid_data",
                method="pca",
                n_components=2
            )
    
    def test_invalid_n_components(self):
        """Test avec un nombre de composantes invalide."""
        with self.assertRaises(ValueError):
            self.factorielle.process(
                self.pca_data,
                method="pca",
                n_components=10  # Plus que le nombre de variables
            )

if __name__ == '__main__':
    unittest.main() 