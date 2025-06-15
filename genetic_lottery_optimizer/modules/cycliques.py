from abstracts import BaseModule
from .base import GeneratorModule, EvaluatorModule
import numpy as np
from collections import defaultdict
from datetime import datetime, timedelta

class SeasonalPatternModule(GeneratorModule):
    def __init__(self):
        super().__init__("Seasonal Pattern")

    def get_entity_scores(self, data, rules):
        # Analyse des patterns saisonniers (par exemple, par jour de la semaine)
        scores = defaultdict(float)
        for ligne in data:
            date = datetime.strptime(ligne['date'], '%Y-%m-%d')
            day_of_week = date.weekday()
            for n in ligne['numeros']:
                scores[n] += 1.0 / (day_of_week + 1)  # Poids différent selon le jour
        return dict(scores), {}

    def score_grid(self, nums, stars, rules):
        return 1.0

class CyclicWeightModule(GeneratorModule):
    def __init__(self):
        super().__init__("Cyclic Weight")

    def get_entity_scores(self, data, rules):
        # Analyse des cycles temporels
        scores = defaultdict(float)
        cycle_length = 28  # Exemple de cycle de 28 jours
        
        for i, ligne in enumerate(data):
            cycle_position = i % cycle_length
            weight = 1.0 / (cycle_position + 1)
            for n in ligne['numeros']:
                scores[n] += weight
        return dict(scores), {}

    def score_grid(self, nums, stars, rules):
        return 1.0

class PeriodicAnalysisModule(GeneratorModule):
    def __init__(self):
        super().__init__("Periodic Analysis")

    def get_entity_scores(self, data, rules):
        # Analyse des périodes multiples
        scores = defaultdict(float)
        periods = [7, 14, 28]  # Différentes périodes à analyser
        
        for i, ligne in enumerate(data):
            for period in periods:
                if i % period == 0:
                    for n in ligne['numeros']:
                        scores[n] += 1.0 / period
        return dict(scores), {}

    def score_grid(self, nums, stars, rules):
        return 1.0