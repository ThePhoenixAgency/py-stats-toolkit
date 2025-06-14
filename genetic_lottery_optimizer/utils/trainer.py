import importlib
import os
import sys
from pathlib import Path
import json
from datetime import datetime
from core_engine import GameRules, DataProcessor, GeneticEngine
from modules import (
    FrequenceAbsolueModule, EntropieShannonModule, DistributionEmpiriqueModule,
    DeviationStandardModule, ComptagePondereModule, MoyenneGlissanteModule,
    ALL_MODULES
)

def load_modules():
    """Charge tous les modules statistiques disponibles."""
    return ALL_MODULES

def train_model(game, file_path, output_path=None, use_advanced_modules=True):
    """
    Entraîne le modèle avec les données fournies.
    
    Args:
        game (str): Nom du jeu (ex: "euromillions")
        file_path (str): Chemin vers le fichier de données
        output_path (str, optional): Chemin de sortie pour la stratégie
        use_advanced_modules (bool): Si True, utilise tous les modules avancés
    
    Returns:
        tuple: (résultats, erreur)
    """
    # Convertir le chemin en chemin absolu
    file_path = Path(file_path).resolve()
    if not file_path.exists():
        return None, f"Fichier introuvable : {file_path}"

    data = DataProcessor(game, str(file_path)).load_and_process_data()
    if data is None:
        return None, "Erreur de chargement des données."

    if use_advanced_modules:
        # Utiliser les modules avancés
        engine = GeneticEngine(game, data)
        engine.generative_modules = [
            FrequenceAbsolueModule(),
            EntropieShannonModule(),
            DistributionEmpiriqueModule(),
            DeviationStandardModule(),
            ComptagePondereModule(),
            MoyenneGlissanteModule()
        ]
        best_chrom, (nums, stars) = engine.evolve()
        
        results = {
            "grille": {"numéros": nums, "étoiles": stars},
            "poids": {
                "génératifs": {mod.name: best_chrom['gen_w'][i] for i, mod in enumerate(engine.generative_modules)},
                "évaluatifs": {mod.name: best_chrom['eval_w'][i] for i, mod in enumerate(engine.evaluative_modules)}
            }
        }
    else:
        # Version simple avec le moteur de base
        engine = GeneticEngine(game, data)
        best_chrom, (nums, stars) = engine.evolve()
        
        results = {
            "grille": {"numéros": nums, "étoiles": stars},
            "generative_weights": best_chrom['gen_w'],
            "evaluative_weights": best_chrom['eval_w']
        }

    # Sauvegarder la stratégie
    filename = output_path or f"strategie_{game}_{datetime.now().strftime('%Y%m%d')}.json"
    with open(Path(__file__).parent / filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    results["fichier_stratégie"] = filename
    return results, None

# Lancement en CLI
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python trainer.py euromillions path/to/file.csv [--simple]")
    else:
        game = sys.argv[1]
        path = sys.argv[2]
        use_advanced = "--simple" not in sys.argv
        result, error = train_model(game, path, use_advanced_modules=use_advanced)
        if error:
            print("Erreur:", error)
        else:
            print("Grille prédite:", result["grille"])
            if "poids" in result:
                print("\nPoids des modules :")
                for category, weights in result["poids"].items():
                    print(f"\n{category}:")
                    for name, weight in weights.items():
                        print(f"  {name:<30} : {weight:.2f}")
