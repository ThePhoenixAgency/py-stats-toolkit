
# Chargement dynamique des modules statistiques
import importlib
import os
import sys
from pathlib import Path

modules_path = Path(__file__).parent / 'modules'
sys.path.insert(0, str(modules_path))

for module_file in modules_path.rglob("*.py"):
    if module_file.name != "__init__.py":
        mod_path = module_file.relative_to(modules_path).with_suffix("")
        mod_name = ".".join(mod_path.parts)
        importlib.import_module(mod_name)


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

import json
from datetime import datetime
from core.engine import GameRules, DataProcessor, ModuleManager, GeneticOptimizer


def train_model(game, file_path):
    data = DataProcessor(game, file_path).load_and_process_data()
    if data is None:
        return None, "Erreur de chargement des données."

    modules = ModuleManager(
        generative_modules=[
            FrequenceAbsolueModule(), EntropieModule(), MoyenneGlissanteModule(),
            CycleFixeModule(), AutoCorrelationModule(), ScoreHotColdModule(),
            AlgorithmeGenetiqueModule(), BoostAdaptatifModule(), SelectionNaturelleModule(),
            Markov1erOrdreModule(), TransitionTableModule(), ProbaBayesienneModule(),
            FFTModule(), FractaleModule(), ClusteringNumeriqueModule(),
            FibonacciModule(), ScoreTopologiqueModule(), ScoreMultijeuxModule()
        ],
        evaluative_modules=[
            EntropieModule(), MoyenneGlissanteModule()
        ]
    )

    optimizer = GeneticOptimizer(game, data, modules)
    best, (nums, stars) = optimizer.run_evolution()

    filename = "strategie_euromillions_force.json"
    with open(filename, 'w') as f:
        json.dump(best, f, indent=2)

    results = {
        "grille": {"numéros": nums, "étoiles": stars},
        "poids": {
            "génératifs": {mod.name: best['generative_weights'][i] for i, mod in enumerate(modules.generative_modules)},
            "évaluatifs": {mod.name: best['evaluative_weights'][i] for i, mod in enumerate(modules.evaluative_modules)}
        },
        "fichier_stratégie": filename
    }
    return results, None