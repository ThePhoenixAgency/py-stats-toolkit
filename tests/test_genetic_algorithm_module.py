'''
import unittest
=====================================================================
File : test_genetic_algorithm_module.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module contient les tests unitaires pour le module d'algorithmes génétiques
de la bibliothèque py_stats_toolkit.

tags : tests, unitaires, algorithmes génétiques, validation
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd

class TestGeneticAlgorithmModule:
    """Tests pour la classe GeneticAlgorithmModule."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        module = GeneticAlgorithmModule()
        assert module.tags == ["stats", "module", "genetic_algorithm"]
        assert module.version == "1.0.0"
        assert module.data is None
        assert module.result is None
        assert module.population is None
        assert module.fitness_function is None
        assert module.best_solution is None
    
    def test_set_fitness_function(self):
        """Teste la définition de la fonction de fitness."""
        module = GeneticAlgorithmModule()
        def fitness(x): return np.sum(x**2)
        module.set_fitness_function(fitness)
        assert module.fitness_function == fitness
    
    def test_initialize_population(self):
        """Teste l'initialisation de la population."""
        module = GeneticAlgorithmModule()
        population_size = 100
        chromosome_length = 10
        module.initialize_population(population_size, chromosome_length)
        assert isinstance(module.population, np.ndarray)
        assert module.population.shape == (population_size, chromosome_length)
    
    def test_calculate_fitness(self):
        """Teste le calcul du fitness."""
        module = GeneticAlgorithmModule()
        def fitness(x): return np.sum(x**2)
        module.set_fitness_function(fitness)
        chromosome = np.array([1, 2, 3])
        fitness_value = module.calculate_fitness(chromosome)
        assert isinstance(fitness_value, float)
        assert fitness_value >= 0
    
    def test_selection(self):
        """Teste la sélection des individus."""
        module = GeneticAlgorithmModule()
        population_size = 100
        chromosome_length = 10
        module.initialize_population(population_size, chromosome_length)
        def fitness(x): return np.sum(x**2)
        module.set_fitness_function(fitness)
        selected = module.selection()
        assert isinstance(selected, np.ndarray)
        assert selected.shape[0] == population_size
    
    def test_crossover(self):
        """Teste le croisement des individus."""
        module = GeneticAlgorithmModule()
        parent1 = np.array([1, 1, 1, 1, 1])
        parent2 = np.array([0, 0, 0, 0, 0])
        child1, child2 = module.crossover(parent1, parent2)
        assert isinstance(child1, np.ndarray)
        assert isinstance(child2, np.ndarray)
        assert child1.shape == parent1.shape
        assert child2.shape == parent2.shape
    
    def test_mutation(self):
        """Teste la mutation des individus."""
        module = GeneticAlgorithmModule()
        chromosome = np.array([1, 1, 1, 1, 1])
        mutation_rate = 0.1
        mutated = module.mutation(chromosome, mutation_rate)
        assert isinstance(mutated, np.ndarray)
        assert mutated.shape == chromosome.shape
    
    def test_evolution_step(self):
        """Teste une étape d'évolution."""
        module = GeneticAlgorithmModule()
        population_size = 100
        chromosome_length = 10
        module.initialize_population(population_size, chromosome_length)
        def fitness(x): return np.sum(x**2)
        module.set_fitness_function(fitness)
        new_population = module.evolution_step()
        assert isinstance(new_population, np.ndarray)
        assert new_population.shape == (population_size, chromosome_length)
    
    def test_optimize(self):
        """Teste l'optimisation complète."""
        module = GeneticAlgorithmModule()
        population_size = 100
        chromosome_length = 10
        n_generations = 50
        def fitness(x): return np.sum(x**2)
        module.set_fitness_function(fitness)
        best_solution = module.optimize(
            population_size=population_size,
            chromosome_length=chromosome_length,
            n_generations=n_generations
        )
        assert isinstance(best_solution, dict)
        assert 'solution' in best_solution
        assert 'fitness' in best_solution
    
    def test_get_best_solution(self):
        """Teste la récupération de la meilleure solution."""
        module = GeneticAlgorithmModule()
        population_size = 100
        chromosome_length = 10
        module.initialize_population(population_size, chromosome_length)
        def fitness(x): return np.sum(x**2)
        module.set_fitness_function(fitness)
        module.optimize(
            population_size=population_size,
            chromosome_length=chromosome_length,
            n_generations=50
        )
        best = module.get_best_solution()
        assert isinstance(best, dict)
        assert 'solution' in best
        assert 'fitness' in best 