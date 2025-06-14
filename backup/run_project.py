import os
import subprocess

print("📦 Lancement de l'optimiseur génétique de loterie...")

# Chemins potentiels à lancer
gui_path = os.path.join("interface", "genetic_optimizer_gui.py")
trainer_path = os.path.join("moteur", "trainer.py")
test_path = os.path.join("interface", "test_optimizer.py")

options = {
    "1": ("🖥️ Interface graphique", gui_path),
    "2": ("🧪 Entraînement manuel", trainer_path),
    "3": ("📊 Script de test", test_path)
}

# Affichage
print("Que souhaitez-vous exécuter ?")
for key, (desc, _) in options.items():
    print(f"{key}. {desc}")

choice = input("\nEntrez votre choix (1-3) : ").strip()

if choice in options:
    desc, path = options[choice]
    if os.path.exists(path):
        print(f"🚀 Lancement de {desc}...")
        subprocess.run(["python", path])
    else:
        print(f"❌ Fichier introuvable : {path}")
else:
    print("❌ Choix invalide.")