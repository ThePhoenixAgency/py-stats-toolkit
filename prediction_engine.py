# prediction_engine.py

import importlib
import random
from collections import Counter
from AbstractModule import BaseModule

class PredictionEngine:
    def __init__(self, game_rules, modules):
        self.rules = game_rules
        self.modules = modules  # liste d'instances de modules BaseModule
        self.weights = {mod.name: 1.0 for mod in modules}

    def set_weights(self, custom_weights):
        for mod in self.modules:
            if mod.name in custom_weights:
                self.weights[mod.name] = custom_weights[mod.name]

    def compute_scores(self, data):
        score_nums, score_stars = Counter(), Counter()
        for mod in self.modules:
            if hasattr(mod, 'supports') and not mod.supports(self.rules.get("game", "")):
                continue
            sn, ss = mod.get_entity_scores(data, self.rules)
            w = self.weights.get(mod.name, 1.0)
            for n, v in sn.items(): score_nums[n] += v * w
            for s, v in ss.items(): score_stars[s] += v * w
        return score_nums, score_stars

    def generate_grid(self, data):
        nums, stars = self.compute_scores(data)
        selected_nums = sorted(random.choices(list(nums), weights=nums.values(), k=self.rules['main_numbers']))
        selected_stars = sorted(random.choices(list(stars), weights=stars.values(), k=self.rules['stars']))
        return selected_nums, selected_stars
