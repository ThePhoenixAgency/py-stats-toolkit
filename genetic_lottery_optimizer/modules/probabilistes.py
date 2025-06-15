from abstracts import BaseModule
from .base import GeneratorModule, EvaluatorModule
import numpy as np
from collections import defaultdict

class MarkovFirstOrderModule(GeneratorModule):
    def __init__(self):
        super().__init__("Markov First Order")

    def get_entity_scores(self, data, rules):
        return {}, {}

    def score_grid(self, nums, stars, rules):
        return 1.0

    def score(self, data):
        transitions = defaultdict(int)
        for i in range(1, len(data)):
            prev = tuple(sorted(data[i-1]['numeros']))
            curr = tuple(sorted(data[i]['numeros']))
            if prev and curr:
                transitions[(prev, curr)] += 1
        return sum(transitions.values()) / (len(data) - 1)

    def score_detaille(self, data):
        compteur_n = defaultdict(float)
        for i in range(1, len(data)):
            nums = set(data[i]['numeros']) & set(data[i-1]['numeros'])
            for n in nums:
                compteur_n[n] += 1
        return {'numeros': dict(compteur_n), 'etoiles': {}}

class ConditionalWeightModule(GeneratorModule):
    def __init__(self):
        super().__init__("Conditional Weight")

    def get_entity_scores(self, data, rules):
        return {}, {}

    def score_grid(self, nums, stars, rules):
        return 1.0

    def score(self, data):
        poids = 0
        for i in range(1, len(data)):
            common = set(data[i]['numeros']) & set(data[i-1]['numeros'])
            poids += len(common)
        return poids / len(data)

    def score_detaille(self, data):
        compteur = defaultdict(int)
        for i in range(1, len(data)):
            common = set(data[i]['numeros']) & set(data[i-1]['numeros'])
            for n in common:
                compteur[n] += 1
        return {'numeros': dict(compteur), 'etoiles': {}}