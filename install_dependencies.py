'''
=====================================================================
File : install_dependencies.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module install_dependencies.py

tags : module, stats
=====================================================================
Ce module Description du module install_dependencies.py

tags : module, stats
=====================================================================
'''

import subprocess
import sys

def install_dependencies():
    """Installe les dépendances requises pour le projet."""
    dependencies = [
        "numpy",
        "pandas",
        "scipy",
        "matplotlib",
        "seaborn",
        "statsmodels",
        "scikit-learn"
    ]
    
    for package in dependencies:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Installation réussie de {package}")
        except subprocess.CalledProcessError:
            print(f"Erreur lors de l'installation de {package}")
            sys.exit(1)

if __name__ == "__main__":
    install_dependencies() 