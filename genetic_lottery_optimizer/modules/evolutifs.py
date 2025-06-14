from abstracts import BaseModule
import numpy as np
from collections import defaultdict
from datetime import datetime, timedelta

class TimeBasedWeightModule(BaseModule):
    def __init__(self):
        super().__init__("Time Based Weight")

    def get_entity_scores(self, data, rules):
        return {}, {}

    def score_grid(self, nums, stars, rules):
        return 1.0

class TrendAnalysisModule(BaseModule):
    def __init__(self):
        super().__init__("Trend Analysis")

    def get_entity_scores(self, data, rules):
        return {}, {}

    def score_grid(self, nums, stars, rules):
        return 1.0

class GeneticSelectionModule(BaseModule):
    def __init__(self):
        super().__init__("Genetic Selection")

    def score(self, data):
        scores = []
        for ligne in data:
            unique = len(set(ligne['numeros']))
            scores.append(unique / len(ligne['numeros']))
        return float(np.mean(scores))

    def score_detaille(self, data):
        compteur_n = defaultdict(float)
        for ligne in data:
            for n in ligne['numeros']:
                compteur_n[n] += 1
        return {'numeros': dict(compteur_n), 'etoiles': {}}

class BoostAdaptiveModule(BaseModule):
    def __init__(self):
        super().__init__("Boost Adaptive")

    def score(self, data):
        boosts = []
        for i in range(1, len(data)):
            overlap = len(set(data[i]['numeros']) & set(data[i-1]['numeros']))
            boosts.append(overlap)
        return float(np.mean(boosts))

    def score_detaille(self, data):
        compteur_n = defaultdict(float)
        for i in range(1, len(data)):
            nums = set(data[i]['numeros']) & set(data[i-1]['numeros'])
            for n in nums:
                compteur_n[n] += 1
        return {'numeros': dict(compteur_n), 'etoiles': {}}

class MultiModelScoringModule(BaseModule):
    def __init__(self):
        super().__init__("Multi Model Scoring")

    def score(self, data):
        result = []
        for i in range(len(data)):
            val = sum(data[i]['numeros']) / len(data[i]['numeros'])
            result.append(val)
        return np.mean(result)

    def score_detaille(self, data):
        compteur_n = defaultdict(float)
        for ligne in data:
            for n in ligne['numeros']:
                compteur_n[n] += 1
        return {'numeros': dict(compteur_n), 'etoiles': {}}