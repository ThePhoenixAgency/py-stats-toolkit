'''
=====================================================================
File : test_markov_chain_module.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module contient les tests unitaires pour le module de chaînes de Markov
de la bibliothèque py_stats_toolkit.

tags : tests, unitaires, chaînes de Markov, validation
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd
from py_stats_toolkit.Abstracts.MarkovChainModule import MarkovChainModule

class TestMarkovChainModule:
    """Tests pour la classe MarkovChainModule."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        module = MarkovChainModule()
        assert module.tags == ["stats", "module", "markov_chain"]
        assert module.version == "1.0.0"
        assert module.data is None
        assert module.result is None
        assert module.transition_matrix is None
        assert module.states is None
    
    def test_set_transition_matrix(self):
        """Teste la définition de la matrice de transition."""
        module = MarkovChainModule()
        matrix = np.array([
            [0.7, 0.3],
            [0.4, 0.6]
        ])
        module.set_transition_matrix(matrix)
        assert isinstance(module.transition_matrix, np.ndarray)
        assert module.transition_matrix.shape == (2, 2)
    
    def test_set_states(self):
        """Teste la définition des états."""
        module = MarkovChainModule()
        states = ["État A", "État B"]
        module.set_states(states)
        assert module.states == states
    
    def test_validate_transition_matrix(self):
        """Teste la validation de la matrice de transition."""
        module = MarkovChainModule()
        invalid_matrix = np.array([
            [0.7, 0.4],  # Somme > 1
            [0.4, 0.6]
        ])
        with pytest.raises(ValueError):
            module.set_transition_matrix(invalid_matrix)
    
    def test_calculate_stationary_distribution(self):
        """Teste le calcul de la distribution stationnaire."""
        module = MarkovChainModule()
        matrix = np.array([
            [0.7, 0.3],
            [0.4, 0.6]
        ])
        module.set_transition_matrix(matrix)
        stationary = module.calculate_stationary_distribution()
        assert isinstance(stationary, np.ndarray)
        assert np.isclose(np.sum(stationary), 1.0)
    
    def test_simulate_chain(self):
        """Teste la simulation de la chaîne."""
        module = MarkovChainModule()
        matrix = np.array([
            [0.7, 0.3],
            [0.4, 0.6]
        ])
        module.set_transition_matrix(matrix)
        states = ["A", "B"]
        module.set_states(states)
        simulation = module.simulate_chain(n_steps=100, initial_state="A")
        assert isinstance(simulation, list)
        assert len(simulation) == 100
        assert all(state in states for state in simulation)
    
    def test_calculate_absorption_probabilities(self):
        """Teste le calcul des probabilités d'absorption."""
        module = MarkovChainModule()
        matrix = np.array([
            [1.0, 0.0, 0.0],  # État absorbant
            [0.3, 0.4, 0.3],
            [0.0, 0.0, 1.0]   # État absorbant
        ])
        module.set_transition_matrix(matrix)
        probs = module.calculate_absorption_probabilities()
        assert isinstance(probs, np.ndarray)
        assert np.all(probs >= 0) and np.all(probs <= 1)
    
    def test_calculate_expected_time_to_absorption(self):
        """Teste le calcul du temps moyen jusqu'à l'absorption."""
        module = MarkovChainModule()
        matrix = np.array([
            [1.0, 0.0, 0.0],  # État absorbant
            [0.3, 0.4, 0.3],
            [0.0, 0.0, 1.0]   # État absorbant
        ])
        module.set_transition_matrix(matrix)
        times = module.calculate_expected_time_to_absorption()
        assert isinstance(times, np.ndarray)
        assert np.all(times >= 0)
    
    def test_calculate_n_step_transition(self):
        """Teste le calcul des probabilités de transition à n étapes."""
        module = MarkovChainModule()
        matrix = np.array([
            [0.7, 0.3],
            [0.4, 0.6]
        ])
        module.set_transition_matrix(matrix)
        n_step = module.calculate_n_step_transition(n=2)
        assert isinstance(n_step, np.ndarray)
        assert n_step.shape == matrix.shape
        assert np.all(n_step >= 0) and np.all(n_step <= 1)
    
    def test_check_irreducibility(self):
        """Teste la vérification d'irréductibilité."""
        module = MarkovChainModule()
        matrix = np.array([
            [0.7, 0.3],
            [0.4, 0.6]
        ])
        module.set_transition_matrix(matrix)
        is_irreducible = module.check_irreducibility()
        assert isinstance(is_irreducible, bool) 