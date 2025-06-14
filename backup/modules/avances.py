from AbstractClassStatistics import AbstractStatisticsModule
from collections import defaultdict
import numpy as np

class FFTModule(AbstractStatisticsModule):
    def score(self, data):
        valeurs = [sum(ligne['numeros']) for ligne in data]
        freq = np.fft.fft(valeurs)
        mag = np.abs(freq)
        return float(np.mean(mag))

    def score_detaille(self, data):
        compteur = defaultdict(float)
        for ligne in data:
            for n in ligne['numeros']:
                compteur[n] += 1
        return {'numeros': dict(compteur), 'etoiles': {}}

class FractalModule(AbstractStatisticsModule):
    def score(self, data):
        unique = set()
        for ligne in data:
            unique.update(ligne['numeros'])
        return len(unique) / (len(data) * 5)

    def score_detaille(self, data):
        compteur = defaultdict(int)
        for ligne in data:
            for n in ligne['numeros']:
                compteur[n] += 1
        return {'numeros': dict(compteur), 'etoiles': {}}