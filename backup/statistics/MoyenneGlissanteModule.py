from AbstractClassStatistics import AbstractStatisticsModule
import numpy as np
from collections import defaultdict

class MoyenneGlissanteModule(AbstractStatisticsModule):
    def score(self, data):
        scores = []
        window = 10
        for i in range(window, len(data)):
            moyenne = np.mean([n for ligne in data[i-window:i] for n in ligne['numeros']])
            scores.append(moyenne)
        return float(np.mean(scores))

    def score_detaille(self, data):
        compteur_n = defaultdict(float)
        compteur_e = defaultdict(float)
        window = 20
        for i in range(window, len(data)):
            nums = [n for ligne in data[i-window:i] for n in ligne['numeros']]
            etoiles = [e for ligne in data[i-window:i] for e in ligne['etoiles']]
            for n in nums:
                compteur_n[n] += 1
            for e in etoiles:
                compteur_e[e] += 1
        return {
            'numeros': dict(compteur_n),
            'etoiles': dict(compteur_e)
        }