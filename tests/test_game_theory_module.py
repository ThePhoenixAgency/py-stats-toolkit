'''
=====================================================================
File : test_game_theory_module.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module contient les tests unitaires pour le module de théorie des jeux
de la bibliothèque py_stats_toolkit.

tags : tests, unitaires, théorie des jeux, validation
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd
from py_stats_toolkit.Abstracts.GameTheoryModule import GameTheoryModule

class TestGameTheoryModule:
    """Tests pour la classe GameTheoryModule."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        module = GameTheoryModule()
        assert module.tags == ["stats", "module", "game_theory"]
        assert module.version == "1.0.0"
        assert module.data is None
        assert module.result is None
        assert module.payoff_matrix is None
        assert module.players is None
    
    def test_set_payoff_matrix(self):
        """Teste la définition de la matrice de gains."""
        module = GameTheoryModule()
        matrix = np.array([
            [[3, 3], [0, 5]],
            [[5, 0], [1, 1]]
        ])
        module.set_payoff_matrix(matrix)
        assert isinstance(module.payoff_matrix, np.ndarray)
        assert module.payoff_matrix.shape == (2, 2, 2)
    
    def test_set_players(self):
        """Teste la définition des joueurs."""
        module = GameTheoryModule()
        players = ["Joueur 1", "Joueur 2"]
        module.set_players(players)
        assert module.players == players
    
    def test_validate_payoff_matrix(self):
        """Teste la validation de la matrice de gains."""
        module = GameTheoryModule()
        invalid_matrix = np.array([1, 2, 3])
        with pytest.raises(ValueError):
            module.set_payoff_matrix(invalid_matrix)
    
    def test_find_nash_equilibrium(self):
        """Teste la recherche d'équilibre de Nash."""
        module = GameTheoryModule()
        matrix = np.array([
            [[3, 3], [0, 5]],
            [[5, 0], [1, 1]]
        ])
        module.set_payoff_matrix(matrix)
        equilibrium = module.find_nash_equilibrium()
        assert isinstance(equilibrium, dict)
        assert 'strategies' in equilibrium
        assert 'payoffs' in equilibrium
    
    def test_find_dominant_strategy(self):
        """Teste la recherche de stratégie dominante."""
        module = GameTheoryModule()
        matrix = np.array([
            [[3, 3], [0, 5]],
            [[5, 0], [1, 1]]
        ])
        module.set_payoff_matrix(matrix)
        dominant = module.find_dominant_strategy()
        assert isinstance(dominant, dict)
        assert 'player' in dominant
        assert 'strategy' in dominant
    
    def test_calculate_pareto_optimal(self):
        """Teste le calcul des solutions Pareto-optimales."""
        module = GameTheoryModule()
        matrix = np.array([
            [[3, 3], [0, 5]],
            [[5, 0], [1, 1]]
        ])
        module.set_payoff_matrix(matrix)
        pareto = module.calculate_pareto_optimal()
        assert isinstance(pareto, list)
        assert all(isinstance(sol, dict) for sol in pareto)
    
    def test_solve_zero_sum_game(self):
        """Teste la résolution d'un jeu à somme nulle."""
        module = GameTheoryModule()
        matrix = np.array([
            [3, -2],
            [-1, 4]
        ])
        module.set_payoff_matrix(matrix)
        solution = module.solve_zero_sum_game()
        assert isinstance(solution, dict)
        assert 'value' in solution
        assert 'strategies' in solution
    
    def test_calculate_mixed_strategy(self):
        """Teste le calcul des stratégies mixtes."""
        module = GameTheoryModule()
        matrix = np.array([
            [[3, 3], [0, 5]],
            [[5, 0], [1, 1]]
        ])
        module.set_payoff_matrix(matrix)
        mixed = module.calculate_mixed_strategy()
        assert isinstance(mixed, dict)
        assert 'probabilities' in mixed
        assert 'expected_payoff' in mixed 