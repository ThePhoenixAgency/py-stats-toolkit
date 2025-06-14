from AbstractClassStatistics import AbstractStatisticsModule
from collections import defaultdict
import random
import numpy as np

class GeneticSelectionModule(AbstractStatisticsModule):
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

class BoostAdaptiveModule(AbstractStatisticsModule):
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

class MultiModelScoringModule(AbstractStatisticsModule):
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