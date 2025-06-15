import unittest
import numpy as np
import pandas as pd
from py_stats_toolkit.stats.frequence.FrequenceModule import FrequenceModule

class TestFrequence(unittest.TestCase):
    def setUp(self):
        self.frequence = FrequenceModule()
        
        # Données de test
        self.data = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'B', 'A'])
        self.numeric_data = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    
    def test_process(self):
        """Test du traitement des données."""
        result = self.frequence.process(self.data)
        
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('Fréquence', result.columns)
        self.assertIn('Fréquence cumulée', result.columns)
        self.assertEqual(result['Fréquence'].sum(), len(self.data))
    
    def test_absolute_frequencies(self):
        """Test des fréquences absolues."""
        result = self.frequence.process(self.data)
        abs_freq = self.frequence.get_absolute_frequencies()
        
        self.assertIsInstance(abs_freq, pd.Series)
        self.assertEqual(abs_freq['A'], 4)
        self.assertEqual(abs_freq['B'], 3)
        self.assertEqual(abs_freq['C'], 2)
        self.assertEqual(abs_freq['D'], 1)
    
    def test_cumulative_frequencies(self):
        """Test des fréquences cumulées."""
        result = self.frequence.process(self.data)
        cum_freq = self.frequence.get_cumulative_frequencies()
        
        self.assertIsInstance(cum_freq, pd.Series)
        self.assertEqual(cum_freq['A'], 4)
        self.assertEqual(cum_freq['B'], 7)
        self.assertEqual(cum_freq['C'], 9)
        self.assertEqual(cum_freq['D'], 10)
    
    def test_relative_frequencies(self):
        """Test des fréquences relatives."""
        result = self.frequence.process(self.data)
        rel_freq = self.frequence.get_relative_frequencies()
        
        self.assertIsInstance(rel_freq, pd.Series)
        self.assertAlmostEqual(rel_freq['A'], 0.4)
        self.assertAlmostEqual(rel_freq['B'], 0.3)
        self.assertAlmostEqual(rel_freq['C'], 0.2)
        self.assertAlmostEqual(rel_freq['D'], 0.1)
    
    def test_numeric_data(self):
        """Test avec des données numériques."""
        result = self.frequence.process(self.numeric_data)
        
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result['Fréquence'].sum(), len(self.numeric_data))
        self.assertEqual(result['Fréquence'][1], 1)
        self.assertEqual(result['Fréquence'][2], 2)
        self.assertEqual(result['Fréquence'][3], 3)
        self.assertEqual(result['Fréquence'][4], 4)
    
    def test_empty_data(self):
        """Test avec des données vides."""
        empty_data = pd.Series([])
        result = self.frequence.process(empty_data)
        
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 0)
    
    def test_invalid_data_type(self):
        """Test avec un type de données invalide."""
        with self.assertRaises(TypeError):
            self.frequence.process("invalid_data")
    
    def test_get_frequency_table(self):
        """Test de la table de fréquence complète."""
        result = self.frequence.process(self.data)
        freq_table = self.frequence.get_frequency_table()
        
        self.assertIsInstance(freq_table, pd.DataFrame)
        self.assertIn('Fréquence', freq_table.columns)
        self.assertIn('Fréquence cumulée', freq_table.columns)
        self.assertIn('Fréquence relative', freq_table.columns)
        self.assertIn('Fréquence relative cumulée', freq_table.columns)
    
    def test_get_mode(self):
        """Test de la recherche du mode."""
        result = self.frequence.process(self.data)
        mode = self.frequence.get_mode()
        
        self.assertEqual(mode, 'A')
    
    def test_get_median(self):
        """Test de la recherche de la médiane."""
        result = self.frequence.process(self.numeric_data)
        median = self.frequence.get_median()
        
        self.assertEqual(median, 3)

if __name__ == '__main__':
    unittest.main() 