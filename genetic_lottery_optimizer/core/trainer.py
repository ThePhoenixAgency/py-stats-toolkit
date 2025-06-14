# trainer.py

import json
from datetime import datetime
from prediction_engine import PredictionEngine
from genetic_optimizer_core import GameRules, DataProcessor
from fondamentaux import *  # ou importer toutes les autres catégories nécessaires
from cycliques import *
from genetiques import *
from probabilistes import *
from topologiques import *
from hybrides import *

def train_model(game, file_path):
    """
    Entraîne le moteur sur les données et retourne la meilleure grille selon tous les modules combinés.
    """
    rules = GameRules.get(game)
    rules['game'] = game  # pour filtre support()
    data = DataProcessor(game, file_path).load_and_process_data()
    if data is None:
        return None, "Erreur de chargement des données."

    # Initialiser tous les modules
    modules = []
    modules += [FrequenceAbsolueRelativeModule(), EntropieShannonModule(), DistributionEmpiriqueModule(),
                VarianceDeviationModule(), ComptagePondereWRAGModule(), ModeMedianeMoyenneGlissanteModule()]
    modules += [CyclesFixesModule(), FenetreGlissanteConvolutionModule(), AutocorrelationModule(), ScoreTemporelDynamiqueModule()]
    modules += [AlgoGenetiqueModule(), RollbackAdaptatifModule(), MultiModeleScoreMoyenModule(),
                SelectionNaturelleModule(), BoostAdaptatifModule()]
    modules += [MarkovOrdre1Module(), MarkovOrdre2Module(), TablesTransitionModule(),
                PoidsConditionnelsModule(), ProbabiliteBayesiennePlagesModule()]
    modules += [FourierFFTModule(), FractaleAutosimilaireModule(), TheorieDesJeuxModule(),
                ClustersNumeriquesModule(), FibonacciRecurrentModule(), TopologieCombinatoireModule()]
    modules += [ScoreCompositeMultijeuxModule(), RecoupementMultiLotteriesModule(),
                HistoriqueGrillesGagnantesModule(), CorrelationJeuxDatesModule()]

    # Lancer le moteur de prédiction
    engine = PredictionEngine(rules, modules)
    nums, stars = engine.generate_grid(data)

    # Sauvegarde
    filename = f"strategie_{game}_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"n": nums, "e": stars}, f, indent=2)

    return {
        "grille": {"numéros": nums, "étoiles": stars},
        "fichier_stratégie": filename
    }, None
