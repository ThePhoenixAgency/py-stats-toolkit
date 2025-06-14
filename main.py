import sys
from utils.trainer import train_model
from gui.genetic_optimizer_gui import launch_gui

def main():
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "console":
            game = "euromillions"
            file_path = "data/euromillions.csv"
            print("Démarrage de l'entraînement...")
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
            print("\nAppuyez sur Entrée pour quitter...")
            input()
        else:
            launch_gui()
    except KeyboardInterrupt:
        print("\nProgramme interrompu par l'utilisateur.")
        sys.exit(0)
    except Exception as e:
        print(f"\nUne erreur inattendue s'est produite : {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
