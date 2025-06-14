from AbstractClassStatistics import AbstractStatisticsModule
from collections import defaultdict

class MarkovFirstOrderModule(AbstractStatisticsModule):
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

class ConditionalWeightModule(AbstractStatisticsModule):
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