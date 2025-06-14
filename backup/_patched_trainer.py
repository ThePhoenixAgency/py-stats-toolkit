import json
from datetime import datetime
from core.engine import GameRules, DataProcessor, ModuleManager, GeneticOptimizer

from modules.fondamentaux import *
from modules.cycliques import *
from statistics_modules_full.modules.evolutifs import *
from modules.probabilistes import *
from statistics_modules_full.modules.avances import *
from statistics_modules_full.modules.personnalises import *

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

    filename = f"strategie_{game}_{datetime.now().strftime('%Y%m%d')}.json"
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