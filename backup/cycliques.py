from AbstractClassStatistics import AbstractStatisticsModule
from collections import defaultdict
import numpy as np
import math

class CycleFixeModule(AbstractStatisticsModule):
    def __init__(self, periode=28):
        self.periode = periode

    def score(self, data):
        count = 0
        for i, ligne in enumerate(data):
            if i % self.periode == 0:
                count += sum(ligne['numeros'])
        return count / len(data)

    def score_detaille(self, data):
        compteur_n = defaultdict(int)
        compteur_e = defaultdict(int)
        for i, ligne in enumerate(data):
            if i % self.periode == 0:
                for n in ligne['numeros']:
                    compteur_n[n] += 1
                for e in ligne['etoiles']:
                    compteur_e[e] += 1
        return {
            'numeros': dict(compteur_n),
            'etoiles': dict(compteur_e)
        }

class AutoCorrelationModule(AbstractStatisticsModule):
    def score(self, data):
        if len(data) < 2:
            return 0
        corr = 0
        for i in range(1, len(data)):
            inter = len(set(data[i]['numeros']) & set(data[i-1]['numeros']))
            corr += inter
        return corr / (len(data) - 1)

    def score_detaille(self, data):
        compteur_n = defaultdict(float)
        compteur_e = defaultdict(float)
        for i in range(1, len(data)):
            nums = set(data[i]['numeros']) & set(data[i-1]['numeros'])
            etoiles = set(data[i]['etoiles']) & set(data[i-1]['etoiles'])
            for n in nums:
                compteur_n[n] += 1
            for e in etoiles:
                compteur_e[e] += 1
        return {
            'numeros': dict(compteur_n),
            'etoiles': dict(compteur_e)
        }

class ScoreHotColdModule(AbstractStatisticsModule):
    def score(self, data):
        freq = defaultdict(int)
        for ligne in data:
            for n in ligne['numeros']:
                freq[n] += 1
        moyenne = np.mean(list(freq.values()))
        ecart = np.std(list(freq.values()))
        return ecart / (moyenne + 1e-5)

    def score_detaille(self, data):
        compteur_n = defaultdict(int)
        compteur_e = defaultdict(int)
        for ligne in data:
            for n in ligne['numeros']:
                compteur_n[n] += 1
            for e in ligne['etoiles']:
                compteur_e[e] += 1
        return {
            'numeros': dict(compteur_n),
            'etoiles': dict(compteur_e)
        }