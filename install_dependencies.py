#!/usr/bin/env python3
"""
Script d'installation des dépendances pour Stats Toolkit
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements(file_path):
    """Installe les dépendances depuis un fichier requirements"""
    if not file_path.exists():
        return False
    
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", str(file_path)
        ], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    """Fonction principale"""
    print("🔧 Installation des dépendances Stats Toolkit...")
    
    # Vérifier que pip est disponible
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("❌ pip n'est pas disponible")
        sys.exit(1)
    
    # Mettre à jour pip
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "--upgrade", "pip"
        ], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        pass  # Continue même si la mise à jour échoue
    
    # Installer les dépendances principales
    requirements_file = Path("requirements.txt")
    if install_requirements(requirements_file):
        print("✅ Dépendances principales installées")
    else:
        print("❌ Erreur lors de l'installation des dépendances principales")
        sys.exit(1)
    
    # Installer les dépendances de développement si demandé
    dev_requirements_file = Path("requirements-dev.txt")
    if dev_requirements_file.exists():
        install_dev = input("Installer les dépendances de développement ? (o/n): ").strip().lower()
        if install_dev == 'o':
            if install_requirements(dev_requirements_file):
                print("✅ Dépendances de développement installées")
            else:
                print("❌ Erreur lors de l'installation des dépendances de développement")
    
    print("🎉 Installation terminée avec succès !")

if __name__ == "__main__":
    main() 