from utils.trainer import train_model

def test_optimizer():
    game = "euromillions"
    file_path = "euromillions2.csv"
    results, error = train_model(game, file_path)
    if error:
        print(f"Erreur : {error}")
        return
    print("Grille prédite :", results['grille'])
    print("Poids des modules :")
    for name, w in results['poids'].items():
        print(f"{name:<30} : {w:.2f}")
    print("Stratégie enregistrée :", results['fichier_stratégie'])

if __name__ == "__main__":
    test_optimizer()