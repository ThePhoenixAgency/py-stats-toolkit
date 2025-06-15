@echo off
echo Installation des dependances du Py_Stats_Toolkit...
echo.

:: Vérifie si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo Python n'est pas installe. Veuillez installer Python 3.8 ou superieur.
    pause
    exit /b 1
)

:: Vérifie si pip est à jour
echo Mise a jour de pip...
python -m pip install --upgrade pip

:: Installe les dépendances
echo Installation des dependances...
python install_dependencies.py

echo.
echo Installation terminee !
pause 