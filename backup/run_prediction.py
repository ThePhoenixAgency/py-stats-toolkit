import sys
import os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from core.rules import GameRules
from core.data_loader import DataProcessor
from core.optimizer import GeneticEngine
from datetime import datetime
import json

def main():
    game = "euromillions"
    file_path = "euromillions2.csv"

    rules = GameRules.get(game)
    data = DataProcessor(game, file_path).load_and_process_data()
    engine = GeneticEngine(game, data)
    best_chrom, (nums, stars) = engine.evolve()

    result = {
        "date": datetime.now().isoformat(),
        "game": game,
        "grid": {"numeros": nums, "etoiles": stars},
        "generative_weights": best_chrom['gen_w'],
        "evaluative_weights": best_chrom['eval_w'],
    }

    with open("strategie_euromillions_force.json", "w") as f:
        json.dump(result, f, indent=2)

    print("🎯 Grille générée :")
    print("Numéros :", nums)
    print("Étoiles :", stars)

if __name__ == "__main__":
    main()
