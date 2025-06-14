from abstracts import BaseModule
from .base import GeneratorModule, EvaluatorModule
import numpy as np
from collections import Counter, defaultdict

class FrequenceAbsolueModule(GeneratorModule):
    def __init__(self):
        super().__init__("Frequence Absolue")

    def get_entity_scores(self, data, rules):
        compteur = Counter()
        for ligne in data:
            compteur.update(ligne['numeros'])
        return dict(compteur), {}

    def score_grid(self, nums, stars, rules):
        return 1.0

class MoyenneGlissanteModule(GeneratorModule):
    def __init__(self):
        super().__init__("Moyenne Glissante")

    def get_entity_scores(self, data, rules):
        scores = []
        window = 10
        for i in range(window, len(data)):
            moyenne = np.mean([n for ligne in data[i-window:i] for n in ligne['numeros']])
            scores.append(moyenne)
        return {i: score for i, score in enumerate(scores)}, {}

    def score_grid(self, nums, stars, rules):
        return 1.0