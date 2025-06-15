import unittest
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from py_stats_toolkit.Modules.games.lottery import LotteryAnalysis

class TestLotteryAnalysis(unittest.TestCase):
    """Tests pour la classe LotteryAnalysis."""
    
    def setUp(self):
        """Prépare les données de test."""
        # Création d'un DataFrame de test
        dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
        numbers = [
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7],
            [4, 5, 6, 7, 8],
            [5, 6, 7, 8, 9]
        ] * 20  # Répéter 20 fois pour avoir 100 tirages
        
        self.test_data = pd.DataFrame({
            'date': dates,
            'numbers': numbers,
            'jackpot': np.random.uniform(1000000, 5000000, 100),
            'secondary_prizes': np.random.uniform(1000, 10000, 100)
        })
        
        self.lottery = LotteryAnalysis(self.test_data)
    
    def test_analyze_frequency(self):
        """Test de l'analyse de fréquence."""
        # Test avec un seul numéro
        freq = self.lottery.analyze_frequency(5)
        self.assertIsInstance(freq, dict)
        self.assertIn(5, freq)
        
        # Test avec plusieurs numéros
        freq = self.lottery.analyze_frequency([1, 2, 3])
        self.assertIsInstance(freq, dict)
        self.assertEqual(len(freq), 3)
        
        # Test avec group_by
        freq = self.lottery.analyze_frequency([1, 2, 3], group_by='date')
        self.assertIsInstance(freq, pd.DataFrame)
    
    def test_find_hot_numbers(self):
        """Test de la recherche des numéros chauds."""
        hot_nums = self.lottery.find_hot_numbers(n=3)
        self.assertIsInstance(hot_nums, list)
        self.assertEqual(len(hot_nums), 3)
        
        # Test avec filtres de fréquence
        hot_nums = self.lottery.find_hot_numbers(
            n=3,
            min_frequency=0.1,
            max_frequency=0.9
        )
        self.assertIsInstance(hot_nums, list)
    
    def test_analyze_patterns(self):
        """Test de l'analyse des patterns."""
        patterns = self.lottery.analyze_patterns(
            pattern_length=3,
            pattern_type='consecutive'
        )
        self.assertIsInstance(patterns, (dict, pd.DataFrame))
        
        # Test avec plusieurs longueurs de pattern
        patterns = self.lottery.analyze_patterns(
            pattern_length=[2, 3],
            pattern_type='arithmetic'
        )
        self.assertIsInstance(patterns, (dict, pd.DataFrame))
    
    def test_analyze_lunar_cycles(self):
        """Test de l'analyse des cycles lunaires."""
        lunar_stats = self.lottery.analyze_lunar_cycles()
        self.assertIsInstance(lunar_stats, dict)
        self.assertIn('new_moon', lunar_stats)
        self.assertIn('full_moon', lunar_stats)
        
        # Test avec dates spécifiques
        start_date = datetime.now() - timedelta(days=30)
        end_date = datetime.now()
        lunar_stats = self.lottery.analyze_lunar_cycles(
            start_date=start_date,
            end_date=end_date
        )
        self.assertIsInstance(lunar_stats, dict)
    
    def test_analyze_seasonality(self):
        """Test de l'analyse de saisonnalité."""
        seasonal_stats = self.lottery.analyze_seasonality()
        self.assertIsInstance(seasonal_stats, dict)
        self.assertIn('spring', seasonal_stats)
        self.assertIn('summer', seasonal_stats)
        self.assertIn('autumn', seasonal_stats)
        self.assertIn('winter', seasonal_stats)
    
    def test_find_repetition_cycles(self):
        """Test de la recherche des cycles de répétition."""
        cycles = self.lottery.find_repetition_cycles(
            max_cycle=5,
            min_cycle=1
        )
        self.assertIsInstance(cycles, dict)
    
    def test_calculate_expected_value(self):
        """Test du calcul de la valeur espérée."""
        expected_value = self.lottery.calculate_expected_value(
            ticket_price=2.0,
            include_secondary_prizes=True
        )
        self.assertIsInstance(expected_value, dict)
        self.assertIn('expected_value', expected_value)
        self.assertIn('roi', expected_value)
    
    def test_analyze_winning_probability(self):
        """Test de l'analyse des probabilités de gain."""
        prob = self.lottery.analyze_winning_probability(
            numbers=[1, 2, 3, 4, 5],
            prize_level=5
        )
        self.assertIsInstance(prob, dict)
        self.assertIn('probability', prob)
        self.assertIn('odds', prob)
    
    def test_find_optimal_strategy(self):
        """Test de la recherche de stratégie optimale."""
        strategy = self.lottery.find_optimal_strategy(
            budget=100.0,
            ticket_price=2.0,
            risk_tolerance=0.5
        )
        self.assertIsInstance(strategy, dict)
        self.assertIn('tickets_to_buy', strategy)
        self.assertIn('hot_numbers', strategy)
        self.assertIn('cold_numbers', strategy)
        self.assertIn('recommended_combinations', strategy)
    
    def test_input_data_processing(self):
        """Test du traitement des données d'entrée."""
        # Test avec DataFrame
        lottery_df = LotteryAnalysis(self.test_data)
        self.assertIsInstance(lottery_df.data, pd.DataFrame)
        
        # Test avec numpy array
        array_data = self.test_data.to_numpy()
        lottery_array = LotteryAnalysis(array_data)
        self.assertIsInstance(lottery_array.data, pd.DataFrame)
        
        # Test avec liste de dictionnaires
        dict_data = self.test_data.to_dict('records')
        lottery_dict = LotteryAnalysis(dict_data)
        self.assertIsInstance(lottery_dict.data, pd.DataFrame)
    
    def test_error_handling(self):
        """Test de la gestion des erreurs."""
        # Test avec données invalides
        with self.assertRaises(TypeError):
            LotteryAnalysis(123)  # Type non supporté
        
        # Test avec fichier inexistant
        with self.assertRaises(FileNotFoundError):
            LotteryAnalysis('fichier_inexistant.csv')
        
        # Test avec format de fichier non supporté
        with self.assertRaises(ValueError):
            LotteryAnalysis('test.txt')

if __name__ == '__main__':
    unittest.main() 