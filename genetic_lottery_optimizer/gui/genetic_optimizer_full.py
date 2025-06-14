from modules.fondamentaux import *
from modules.cycliques import *
from modules.evolutifs import *
from modules.probabilistes import *
from modules.avances import *
from modules.personnalises import *

import json
import pandas as pd
from utils.trainer import train_model

if __name__ == "__main__":
    game = "euromillions"
    file_path = "data/euromillions2.csv"  # à adapter selon votre structure
    results, error = train_model(game, file_path)

    if error:
        print(f"Erreur d'entraînement : {error}")
    else:
        print(f"Grille prédite : {results['grille']['numéros']} Étoiles : {results['grille']['étoiles']}")
        print("\nPoids des modules :")
        for name, weight in results['poids']['génératifs'].items():
            print(f"  [G] {name:<25} : {weight:.2f}")
        for name, weight in results['poids']['évaluatifs'].items():
            print(f"  [E] {name:<25} : {weight:.2f}")
        print(f"\nStratégie sauvegardée dans : {results['fichier_stratégie']}")