from abstracts import BaseModule
from .base import GeneratorModule, EvaluatorModule
import numpy as np
from collections import defaultdict
import math

class EntropieShannonModule(GeneratorModule):
    def __init__(self):
        super().__init__("Entropie Shannon")

    def get_entity_scores(self, data, rules):
        compteur = defaultdict(int)
        total = 0
        for ligne in data:
            for n in ligne['numeros']:
                compteur[n] += 1
                total += 1
        
        entropie = {}
        for num, freq in compteur.items():
            p = freq / total
            entropie[num] = -p * math.log2(p)
        return entropie, {}

    def score_grid(self, nums, stars, rules):
        return 1.0

class DistributionEmpiriqueModule(GeneratorModule):
    def __init__(self):
        super().__init__("Distribution Empirique")

    def get_entity_scores(self, data, rules):
        compteur = defaultdict(int)
        for ligne in data:
            for n in ligne['numeros']:
                compteur[n] += 1
        
        # Normalisation des scores
        max_freq = max(compteur.values())
        return {num: freq/max_freq for num, freq in compteur.items()}, {}

    def score_grid(self, nums, stars, rules):
        return 1.0

class DeviationStandardModule(GeneratorModule):
    def __init__(self):
        super().__init__("Deviation Standard")

    def get_entity_scores(self, data, rules):
        compteur = defaultdict(list)
        for ligne in data:
            for n in ligne['numeros']:
                compteur[n].append(1)
        
        # Calcul de l'écart-type pour chaque numéro
        scores = {}
        for num, valeurs in compteur.items():
            scores[num] = np.std(valeurs)
        return scores, {}

    def score_grid(self, nums, stars, rules):
        return 1.0

class ComptagePondereModule(GeneratorModule):
    def __init__(self):
        super().__init__("Comptage Pondere")

    def get_entity_scores(self, data, rules):
        compteur = defaultdict(float)
        for i, ligne in enumerate(data):
            poids = 1.0 / (i + 1)  # Plus récent = plus de poids
            for n in ligne['numeros']:
                compteur[n] += poids
        return dict(compteur), {}

    def score_grid(self, nums, stars, rules):
        return 1.0

class FFTModule(GeneratorModule):
    def __init__(self):
        super().__init__("FFT Analysis")

    def get_entity_scores(self, data, rules):
        valeurs = [sum(ligne['numeros']) for ligne in data]
        freq = np.fft.fft(valeurs)
        mag = np.abs(freq)
        return {i: float(m) for i, m in enumerate(mag)}, {}

class FractalModule(GeneratorModule):
    def __init__(self):
        super().__init__("Fractal Analysis")

    def get_entity_scores(self, data, rules):
        unique = set()
        for ligne in data:
            unique.update(ligne['numeros'])
        return {num: 1.0 for num in unique}, {}

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