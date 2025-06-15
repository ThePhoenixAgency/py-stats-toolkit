@echo off
echo Deploiement de py_stats_toolkit sur PyPI...

REM Verification de Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Erreur: Python n'est pas installe!
    exit /b 1
)

REM Verification du token PyPI
if "%PYPI_API_TOKEN%"=="" (
    echo Erreur: Variable d'environnement PYPI_API_TOKEN non definie!
    echo Veuillez definir la variable d'environnement PYPI_API_TOKEN avec votre token PyPI.
    exit /b 1
)

REM Installation des dependances
echo Installation des dependances...
pip install --upgrade pip
pip install build twine

REM Construction et deploiement
echo Construction et deploiement...
python deploy.py

echo Deploiement termine!
pause 