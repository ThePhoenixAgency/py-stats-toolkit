#!/bin/bash

echo "Installation des dependances du Py_Stats_Toolkit..."
echo

# Vérifie si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "Python n'est pas installe. Veuillez installer Python 3.8 ou superieur."
    exit 1
fi

# Vérifie si pip est à jour
echo "Mise a jour de pip..."
python3 -m pip install --upgrade pip

# Installe les dépendances
echo "Installation des dependances..."
python3 install_dependencies.py

echo
echo "Installation terminee !" 