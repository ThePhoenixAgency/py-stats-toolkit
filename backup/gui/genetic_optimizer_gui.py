import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from utils.trainer import train_model
import os

def launch_gui():
    root = tk.Tk()
    app = GeneticOptimizerApp(root)
    root.mainloop()

class GeneticOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Optimiseur Génétique Loterie")
        self.file_path = None
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Jeu :").grid(row=0, column=0)
        self.game_var = tk.StringVar(value="euromillions")
        ttk.Combobox(self.root, textvariable=self.game_var, values=["euromillions"]).grid(row=0, column=1)

        ttk.Button(self.root, text="Charger CSV", command=self.load_file).grid(row=1, column=0, columnspan=2)
        ttk.Button(self.root, text="Lancer l'entraînement", command=self.train).grid(row=2, column=0, columnspan=2)

        self.output = tk.Text(self.root, height=20, width=80)
        self.output.grid(row=3, column=0, columnspan=2)

    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.output.insert(tk.END, f"Fichier sélectionné : {self.file_path}\n")

    def train(self):
        if not self.file_path:
            messagebox.showerror("Erreur", "Veuillez charger un fichier CSV.")
            return
        game = self.game_var.get()
        results, error = train_model(game, self.file_path)
        if error:
            self.output.insert(tk.END, f"Erreur : {error}\n")
            return
        self.output.insert(tk.END, f"Grille : {results['grille']['numéros']} Étoiles : {results['grille']['étoiles']}\n")
        for name, weight in results['poids'].items():
            self.output.insert(tk.END, f"{name:<30} : {weight:.2f}\n")
        self.output.insert(tk.END, f"Stratégie sauvegardée : {results['fichier_stratégie']}\n")

if __name__ == "__main__":
    launch_gui()