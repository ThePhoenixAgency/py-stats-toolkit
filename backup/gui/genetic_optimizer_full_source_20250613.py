# ========== full_engine_singlefile.py (updated) ==========
import pandas as pd
import numpy as np
import random
import json
from datetime import datetime
from collections import Counter
from all_stat_modules import (
    FrequenceAbsolueModule,
    EntropieShannonModule,
    FixedCycleDetectorModule,
    RollingWeightModule,
    MarkovChainModule,
    FibonacciWeightModule,
    HotColdPatternModule
)

class GameRules:
    rules = {
        'euromillions': {
            'days': [1, 4],
            'main_numbers': 5, 'main_range': (1, 50),
            'stars': 2, 'stars_range': (1, 12), 'star_name': 'etoile'
        }
    }
    @classmethod
    def get(cls, game): return cls.rules.get(game, {})
    @classmethod
    def get_days(cls, game): return cls.rules.get(game, {}).get('days', [])

class DataProcessor:
    def __init__(self, game_name, file_path):
        self.game_name = game_name
        self.file_path = file_path
        self.rules = GameRules.get(game_name)

    def load_and_process_data(self):
        df = pd.read_csv(self.file_path, sep=';', parse_dates=['date_de_tirage'])
        num_cols = [f'num{i}' for i in range(1, self.rules['main_numbers'] + 1)]
        star_cols = [f"{self.rules['star_name']}{i}" for i in range(1, self.rules['stars'] + 1)]
        df['numeros'] = df[num_cols].values.tolist()
        df['etoiles'] = df[star_cols].values.tolist()
        return df[['date_de_tirage', 'numeros', 'etoiles']]

class ModuleManager:
    def __init__(self):
        self.modules = [
            FrequenceAbsolueModule(),
            EntropieShannonModule(),
            FixedCycleDetectorModule(28),
            RollingWeightModule(20),
            MarkovChainModule(),
            FibonacciWeightModule(),
            HotColdPatternModule(5)
        ]

    def get_profiles(self, data, rules):
        return [mod.get_entity_scores(data, rules) for mod in self.modules]

class GeneticOptimizer:
    def __init__(self, game_name, data, module_manager):
        self.rules = GameRules.get(game_name)
        self.data = data
        self.modules = module_manager
        self.gen_profiles = self.modules.get_profiles(data, self.rules)

    def _create_chromosome(self):
        return {
            'weights': [random.random() for _ in self.gen_profiles]
        }

    def _generate_grid(self, chrom):
        num_scores, star_scores = Counter(), Counter()
        for i, (n, s) in enumerate(self.gen_profiles):
            w = chrom['weights'][i]
            for k, v in n.items(): num_scores[k] += v * w
            for k, v in s.items(): star_scores[k] += v * w
        nums = random.choices(list(num_scores), weights=num_scores.values(), k=self.rules['main_numbers'])
        stars = random.choices(list(star_scores), weights=star_scores.values(), k=self.rules['stars'])
        return sorted(set(nums)), sorted(set(stars))

    def _calculate_fitness(self, chrom):
        total = 0
        for _ in range(min(50, len(self.data))):
            nums, stars = self._generate_grid(chrom)
            total += len(nums) + len(stars)
        return total / 50

    def run_evolution(self, generations=40, population_size=20):
        best = self._create_chromosome()
        best_score = self._calculate_fitness(best)
        for _ in range(generations):
            chrom = self._create_chromosome()
            score = self._calculate_fitness(chrom)
            if score > best_score:
                best, best_score = chrom, score
        return best, self._generate_grid(best)

def train_model(game, file_path):
    data = DataProcessor(game, file_path).load_and_process_data()
    if data is None:
        return None, "Erreur de chargement des données"
    modules = ModuleManager()
    optimizer = GeneticOptimizer(game, data, modules)
    best, (nums, stars) = optimizer.run_evolution()
    filename = f"strategie_{game}_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, 'w') as f:
        json.dump(best, f, indent=2)
    results = {
        "grille": {"numéros": nums, "étoiles": stars},
        "poids": {modules.modules[i].name: best['weights'][i] for i in range(len(modules.modules))},
        "fichier_stratégie": filename
    }
    return results, None