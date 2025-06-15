import os
import subprocess
import sys
from pathlib import Path

def get_pypi_token():
    """Récupère le token PyPI depuis les variables d'environnement ou les secrets GitHub."""
    # Essai de récupérer depuis les variables d'environnement
    token = os.getenv('PYPI_API_TOKEN')
    
    # Si non trouvé, essai de récupérer depuis les secrets GitHub
    if not token and os.getenv('GITHUB_ACTIONS'):
        token = os.getenv('PYPI_TOKEN_SECRET')
    
    if not token:
        print("Erreur: Token PyPI non trouvé!")
        print("Veuillez définir la variable d'environnement PYPI_API_TOKEN")
        sys.exit(1)
    
    return token

def run_command(command):
    """Exécute une commande et affiche sa sortie."""
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        universal_newlines=True
    )
    
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        print(f"Erreur lors de l'exécution de la commande: {command}")
        print(f"Sortie d'erreur: {stderr}")
        sys.exit(1)
    
    return stdout

def build_package():
    """Construit le package."""
    print("Construction du package...")
    
    # Nettoyage des anciens builds
    if os.name == 'nt':  # Windows
        run_command("if exist build rmdir /s /q build")
        run_command("if exist dist rmdir /s /q dist")
        run_command("if exist *.egg-info rmdir /s /q *.egg-info")
    else:  # Linux/Mac
        run_command("rm -rf build/ dist/ *.egg-info/")
    
    # Construction du package
    run_command("python setup.py sdist bdist_wheel")
    
    print("Package construit avec succès!")

def deploy_to_pypi():
    """Déploie le package sur PyPI."""
    print("Déploiement sur PyPI...")
    
    # Vérification de l'installation de twine
    try:
        import twine
    except ImportError:
        print("Installation de twine...")
        run_command("pip install twine")
    
    # Récupération du token
    token = get_pypi_token()
    
    # Déploiement avec le token
    run_command(f"python -m twine upload --username __token__ --password {token} dist/*")
    
    print("Déploiement terminé avec succès!")

def main():
    """Fonction principale."""
    # Vérification de la présence du fichier setup.py
    if not Path("setup.py").exists():
        print("Erreur: setup.py non trouvé!")
        sys.exit(1)
    
    # Vérification de la présence du README.md
    if not Path("README.md").exists():
        print("Erreur: README.md non trouvé!")
        sys.exit(1)
    
    # Construction et déploiement
    build_package()
    deploy_to_pypi()

if __name__ == "__main__":
    main() 