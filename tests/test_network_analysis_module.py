'''
import unittest
=====================================================================
File : test_network_analysis_module.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Ce module contient les tests unitaires pour le module d'analyse de réseau
de la bibliothèque py_stats_toolkit.

tags : tests, unitaires, analyse de réseau, validation
=====================================================================
'''

import pytest
import numpy as np
import pandas as pd
import networkx as nx

class TestNetworkAnalysisModule:
    """Tests pour la classe NetworkAnalysisModule."""
    
    def test_initialization(self):
        """Teste l'initialisation."""
        module = NetworkAnalysisModule()
        assert module.tags == ["stats", "module", "network_analysis"]
        assert module.version == "1.0.0"
        assert module.data is None
        assert module.result is None
        assert module.graph is None
        assert module.nodes is None
        assert module.edges is None
    
    def test_create_graph(self):
        """Teste la création d'un graphe."""
        module = NetworkAnalysisModule()
        edges = [(1, 2), (2, 3), (3, 1)]
        module.create_graph(edges)
        assert isinstance(module.graph, nx.Graph)
        assert module.graph.number_of_edges() == 3
        assert module.graph.number_of_nodes() == 3
    
    def test_set_graph(self):
        """Teste la définition d'un graphe."""
        module = NetworkAnalysisModule()
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 1)])
        module.set_graph(G)
        assert isinstance(module.graph, nx.Graph)
        assert module.graph.number_of_edges() == 3
    
    def test_calculate_degree_centrality(self):
        """Teste le calcul de la centralité de degré."""
        module = NetworkAnalysisModule()
        edges = [(1, 2), (2, 3), (3, 1)]
        module.create_graph(edges)
        centrality = module.calculate_degree_centrality()
        assert isinstance(centrality, dict)
        assert all(0 <= v <= 1 for v in centrality.values())
    
    def test_calculate_betweenness_centrality(self):
        """Teste le calcul de la centralité d'intermédiarité."""
        module = NetworkAnalysisModule()
        edges = [(1, 2), (2, 3), (3, 1)]
        module.create_graph(edges)
        centrality = module.calculate_betweenness_centrality()
        assert isinstance(centrality, dict)
        assert all(0 <= v <= 1 for v in centrality.values())
    
    def test_calculate_closeness_centrality(self):
        """Teste le calcul de la centralité de proximité."""
        module = NetworkAnalysisModule()
        edges = [(1, 2), (2, 3), (3, 1)]
        module.create_graph(edges)
        centrality = module.calculate_closeness_centrality()
        assert isinstance(centrality, dict)
        assert all(0 <= v <= 1 for v in centrality.values())
    
    def test_calculate_pagerank(self):
        """Teste le calcul du PageRank."""
        module = NetworkAnalysisModule()
        edges = [(1, 2), (2, 3), (3, 1)]
        module.create_graph(edges)
        pagerank = module.calculate_pagerank()
        assert isinstance(pagerank, dict)
        assert np.isclose(sum(pagerank.values()), 1.0)
    
    def test_find_communities(self):
        """Teste la détection de communautés."""
        module = NetworkAnalysisModule()
        edges = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]
        module.create_graph(edges)
        communities = module.find_communities()
        assert isinstance(communities, list)
        assert len(communities) > 0
    
    def test_calculate_clustering_coefficient(self):
        """Teste le calcul du coefficient de clustering."""
        module = NetworkAnalysisModule()
        edges = [(1, 2), (2, 3), (3, 1)]
        module.create_graph(edges)
        coefficient = module.calculate_clustering_coefficient()
        assert isinstance(coefficient, float)
        assert 0 <= coefficient <= 1
    
    def test_calculate_shortest_paths(self):
        """Teste le calcul des plus courts chemins."""
        module = NetworkAnalysisModule()
        edges = [(1, 2), (2, 3), (3, 1)]
        module.create_graph(edges)
        paths = module.calculate_shortest_paths()
        assert isinstance(paths, dict)
        assert all(isinstance(v, dict) for v in paths.values())
    
    def test_calculate_diameter(self):
        """Teste le calcul du diamètre."""
        module = NetworkAnalysisModule()
        edges = [(1, 2), (2, 3), (3, 1)]
        module.create_graph(edges)
        diameter = module.calculate_diameter()
        assert isinstance(diameter, int)
        assert diameter > 0
    
    def test_calculate_density(self):
        """Teste le calcul de la densité."""
        module = NetworkAnalysisModule()
        edges = [(1, 2), (2, 3), (3, 1)]
        module.create_graph(edges)
        density = module.calculate_density()
        assert isinstance(density, float)
        assert 0 <= density <= 1 