
import random
import numpy as np
from collections import Counter
from core.rules import GameRules

class GeneticEngine:
    def __init__(self, game, data):
        self.rules = GameRules.get(game)
        self.data = data
        self.gen_modules = [self.freq_score]
        self.eval_modules = [self.even_sum]

    def _create_chromosome(self):
        return {'gen_w': [random.random()], 'eval_w': [random.random()]}

    def _generate_grid(self, chrom):
        counts = Counter([n for row in self.data['numeros'] for n in row])
        weights = {k: v * chrom['gen_w'][0] for k, v in counts.items()}
        nums = sorted(random.choices(list(weights), weights=weights.values(), k=self.rules['main_numbers']))
        stars = sorted(random.choices(range(1, 13), k=self.rules['stars']))
        return nums, stars

    def even_sum(self, nums, stars):
        ideal = 5 * (50 + 1) / 2
        return 1.0 - abs(sum(nums) - ideal) / (ideal * 0.5)

    def _score(self, chrom):
        return np.mean([self.even_sum(*self._generate_grid(chrom)) * chrom['eval_w'][0] for _ in range(10)])

    def evolve(self, gens=20):
        best = self._create_chromosome()
        best_score = self._score(best)
        for _ in range(gens):
            c = self._create_chromosome()
            s = self._score(c)
            if s > best_score:
                best, best_score = c, s
        return best, self._generate_grid(best)
