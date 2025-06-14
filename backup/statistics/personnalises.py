from AbstractClassStatistics import AbstractStatisticsModule
from collections import defaultdict

class CrossGameScoreModule(AbstractStatisticsModule):
    def score(self, data):
        total = 0
        for ligne in data:
            total += len(set(ligne['numeros']))
        return total / len(data)

    def score_detaille(self, data):
        compteur = defaultdict(int)
        for ligne in data:
            for n in ligne['numeros']:
                compteur[n] += 1
        return {'numeros': dict(compteur), 'etoiles': {}}

class WinningPatternMemoryModule(AbstractStatisticsModule):
    def score(self, data):
        patterns = defaultdict(int)
        for ligne in data:
            key = tuple(sorted(ligne['numeros']))
            patterns[key] += 1
        return len(patterns)

    def score_detaille(self, data):
        compteur = defaultdict(int)
        for ligne in data:
            for n in ligne['numeros']:
                compteur[n] += 1
        return {'numeros': dict(compteur), 'etoiles': {}}