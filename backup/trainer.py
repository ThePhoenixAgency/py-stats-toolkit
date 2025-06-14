
import importlib
import os
import sys
from pathlib import Path
import json
from datetime import datetime
from core.rules import GameRules
from core.data_loader import DataProcessor
from core.optimizer import GeneticEngine

def train_model(game, file_path, output_path=None):
    data = DataProcessor(game, file_path).load_and_process_data()
    if data is None:
        return None, "Erreur de chargement des données."

    engine = GeneticEngine(game, data)
    best_chrom, (nums, stars) = engine.evolve()

    filename = output_path or f"strategie_{game}_{datetime.now().strftime('%Y%m%d')}.json"
    result = {
        "date": datetime.now().isoformat(),
        "game": game,
        "grid": {"numeros": nums, "etoiles": stars},
        "generative_weights": best_chrom['gen_w'],
        "evaluative_weights": best_chrom['eval_w'],
    }

    with open(Path(__file__).parent / filename, 'w') as f:
        json.dump(result, f, indent=2)

    return result, None

# Lancement en CLI
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python trainer.py euromillions path/to/file.csv")
    else:
        game = sys.argv[1]
        path = sys.argv[2]
        result, error = train_model(game, path, output_path="strategie_euromillions_force.json")
        if error:
            print("Erreur:", error)
        else:
            print("Grille prédite:", result["grid"])
