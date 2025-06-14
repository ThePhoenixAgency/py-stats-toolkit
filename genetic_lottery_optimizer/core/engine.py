import pandas as pd
import numpy as np
from collections import Counter
import random

class GameRules:
    rules = {
        'euromillions': {
            'days': [1, 4],
            'main_numbers': 5, 'main_range': (1, 50),
            'stars': 2, 'stars_range': (1, 12),
            'star_name': 'etoile',
            'csv_columns': {
                'numeros': ['boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5'],
                'etoiles': ['etoile_1', 'etoile_2']
            }
        }
    }

    @classmethod
    def get(cls, game): return cls.rules.get(game, {})

class DataProcessor:
    def __init__(self, game, file_path):
        self.rules = GameRules.get(game)
        self.file_path = file_path

    def load_and_process_data(self):
        df = pd.read_csv(self.file_path, sep=';', parse_dates=['date_de_tirage'])
        num_cols = self.rules['csv_columns']['numeros']
        star_cols = self.rules['csv_columns']['etoiles']

        df['numeros'] = df[num_cols].values.tolist()
        df['etoiles'] = df[star_cols].values.tolist()
        df['payouts'] = [{} for _ in range(len(df))]
        return df[['date_de_tirage', 'numeros', 'etoiles', 'payouts']]

class BaseModule:
    def __init__(self, name): self.name = name

class FrequencyModule(BaseModule):
    def __init__(self): super().__init__("Freq")

    def get_entity_scores(self, data, rules):
        num_counter = Counter([n for row in data['numeros'] for n in row])
        star_counter = Counter([s for row in data['etoiles'] for s in row])
        return num_counter, star_counter

class EvaluatorModule(BaseModule):
    def __init__(self): super().__init__("EvenSum")

    def score_grid(self, nums, stars, rules):
        s = sum(nums)
        ideal = rules['main_numbers'] * (rules['main_range'][1] + 1) / 2
        return 1.0 - abs(s - ideal) / (ideal * 0.5)

class GeneticEngine:
    def __init__(self, game, data):
        self.rules = GameRules.get(game)
        self.data = data
        self.generative_modules = [FrequencyModule()]
        self.evaluative_modules = [EvaluatorModule()]
        self.gen_scores = [mod.get_entity_scores(data, self.rules) for mod in self.generative_modules]

    def _create_chromosome(self):
        return {
            'gen_w': [random.random() for _ in self.generative_modules],
            'eval_w': [random.random() for _ in self.evaluative_modules]
        }

    def _generate_grid(self, chrom):
        num_scores, star_scores = Counter(), Counter()
        for i, (mod_num, mod_star) in enumerate(self.gen_scores):
            for k, v in mod_num.items(): num_scores[k] += v * chrom['gen_w'][i]
            for k, v in mod_star.items(): star_scores[k] += v * chrom['gen_w'][i]
        nums = sorted(random.choices(list(num_scores), weights=num_scores.values(), k=self.rules['main_numbers']))
        stars = sorted(random.choices(list(star_scores), weights=star_scores.values(), k=self.rules['stars']))
        return nums, stars

    def _score_chrom(self, chrom):
        scores = []
        for _ in range(20):
            nums, stars = self._generate_grid(chrom)
            s = sum(m.score_grid(nums, stars, self.rules) * chrom['eval_w'][i]
                    for i, m in enumerate(self.evaluative_modules))
            scores.append(s)
        return np.mean(scores)

    def evolve(self, gens=20):
        best = self._create_chromosome()
        best_score = self._score_chrom(best)
        for _ in range(gens):
            chrom = self._create_chromosome()
            score = self._score_chrom(chrom)
            if score > best_score:
                best, best_score = chrom, score
        return best, self._generate_grid(best)

class ModuleManager:
    def __init__(self, generative_modules=None, evaluative_modules=None):
        self.generative_modules = generative_modules or []
        self.evaluative_modules = evaluative_modules or []

class GeneticOptimizer:
    def __init__(self, game, data, module_manager):
        self.rules = GameRules.get(game)
        self.data = data
        self.modules = module_manager
        self.gen_scores = [mod.get_entity_scores(data, self.rules) for mod in self.modules.generative_modules]

    def _create_chromosome(self):
        return {
            'generative_weights': [random.random() for _ in self.modules.generative_modules],
            'evaluative_weights': [random.random() for _ in self.modules.evaluative_modules]
        }

    def _generate_grid(self, chrom):
        num_scores, star_scores = Counter(), Counter()
        for i, (mod_num, mod_star) in enumerate(self.gen_scores):
            for k, v in mod_num.items(): num_scores[k] += v * chrom['generative_weights'][i]
            for k, v in mod_star.items(): star_scores[k] += v * chrom['generative_weights'][i]
        nums = sorted(random.choices(list(num_scores), weights=num_scores.values(), k=self.rules['main_numbers']))
        stars = sorted(random.choices(list(star_scores), weights=star_scores.values(), k=self.rules['stars']))
        return nums, stars

    def _score_chrom(self, chrom):
        scores = []
        for _ in range(20):
            nums, stars = self._generate_grid(chrom)
            s = sum(m.score_grid(nums, stars, self.rules) * chrom['evaluative_weights'][i]
                    for i, m in enumerate(self.modules.evaluative_modules))
            scores.append(s)
        return np.mean(scores)

    def run_evolution(self, gens=20):
        best = self._create_chromosome()
        best_score = self._score_chrom(best)
        for _ in range(gens):
            chrom = self._create_chromosome()
            score = self._score_chrom(chrom)
            if score > best_score:
                best, best_score = chrom, score
        return best, self._generate_grid(best)
