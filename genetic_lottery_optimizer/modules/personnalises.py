from abstracts import BaseModule
from .base import GeneratorModule, EvaluatorModule
import numpy as np
from collections import defaultdict

class CrossGameScoreModule(GeneratorModule):
    def __init__(self):
        super().__init__("Cross Game Score")

    def get_entity_scores(self, data, rules):
        return {}, {}

    def score_grid(self, nums, stars, rules):
        return 1.0

class WinningPatternMemoryModule(GeneratorModule):
    def __init__(self):
        super().__init__("Winning Pattern Memory")

    def get_entity_scores(self, data, rules):
        return {}, {}

    def score_grid(self, nums, stars, rules):
        return 1.0