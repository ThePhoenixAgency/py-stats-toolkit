import sys
from utils.trainer import train_model
from gui.genetic_optimizer_gui import launch_gui

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "console":
        game = "euromillions"
        file_path = "data/euromillions.csv"
        results, error = train_model(game, file_path)
        if error:
            print(f"Erreur : {error}")
        else:
            print(f"Grille prédite : {results['grille']['numéros']} Étoiles : {results['grille']['étoiles']}")
            print("Poids :")
            for name, w in results['poids']['génératifs'].items():
                print(f"  [G] {name} : {w:.2f}")
            for name, w in results['poids']['évaluatifs'].items():
                print(f"  [E] {name} : {w:.2f}")
            print(f"Stratégie sauvegardée dans : {results['fichier_stratégie']}")
    else:
        launch_gui()

if __name__ == "__main__":
    main()
