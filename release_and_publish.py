#!/usr/bin/env python3
"""
Script complet pour la release, publication GitHub et publication PyPI
"""

import os
import sys
import subprocess
import requests
import json
from datetime import datetime

def run_command(command, description=""):
    """Exécute une commande et affiche le résultat"""
    if description:
        print(f"🔄 {description}...")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        if result.stdout:
            print(f"✅ {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur: {e}")
        if e.stderr:
            print(f"   Détails: {e.stderr.strip()}")
        return False

def check_git_status():
    """Vérifie le statut Git"""
    print("🔍 Vérification du statut Git...")
    
    # Vérifier s'il y a des changements non commités
    result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if result.stdout.strip():
        print("⚠️  Il y a des changements non commités:")
        print(result.stdout.strip())
        return False
    
    print("✅ Aucun changement non commité")
    return True

def create_github_release():
    """Crée une release GitHub via l'API"""
    
    # Configuration
    repo_owner = "ThePhoenixAgency"
    repo_name = "py-stats-toolkit"
    tag_name = "v1.0.4"
    
    # Le token GitHub doit être dans les variables d'environnement
    github_token = os.getenv('GITHUB_TOKEN')
    
    if not github_token:
        print("❌ Erreur: GITHUB_TOKEN non défini")
        print("💡 Définissez votre token GitHub: set GITHUB_TOKEN=your_token_here")
        print("   Ou utilisez un token personnel GitHub avec permissions 'repo'")
        return False
    
    # URL de l'API GitHub
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
    
    # Données de la release
    release_data = {
        "tag_name": tag_name,
        "name": f"Release {tag_name}",
        "body": f"""## 🚀 Release {tag_name} - Badges de qualité et conformité complète

### ✨ Nouvelles fonctionnalités
- Ajout de badges de compliance dans le README
- Section dédiée à la qualité du code avec standards de qualité
- Documentation complète des outils de qualité utilisés

### 🔧 Améliorations
- Badges pour Black (formatage), isort (imports), flake8 (linting)
- Badges pour MyPy (type checking), Bandit (sécurité), Pytest (tests)
- Badge de couverture de code avec Codecov
- Section explicative des standards de qualité

### 🏆 Qualité du Code
- **Black** : Formatage automatique selon PEP8
- **isort** : Organisation automatique des imports
- **Flake8** : Détection des erreurs de style et qualité
- **MyPy** : Vérification statique des types
- **Bandit** : Analyse de sécurité pour vulnérabilités
- **Pytest** : Framework de tests avec couverture

### 📦 Installation
```bash
pip install py-stats-toolkit==1.0.4
```

### 🔗 Liens
- [Documentation](https://py-stats-toolkit.readthedocs.io/)
- [PyPI](https://pypi.org/project/py-stats-toolkit/)
- [Issues](https://github.com/ThePhoenixAgency/py-stats-toolkit/issues)

---
*Release créée automatiquement le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*""",
        "draft": False,
        "prerelease": False
    }
    
    # Headers pour l'API GitHub
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        print(f"🚀 Création de la release {tag_name}...")
        
        # Création de la release
        response = requests.post(url, headers=headers, json=release_data)
        
        if response.status_code == 201:
            release_info = response.json()
            print(f"✅ Release créée avec succès!")
            print(f"📋 URL: {release_info['html_url']}")
            return True
        else:
            print(f"❌ Erreur lors de la création de la release:")
            print(f"   Status: {response.status_code}")
            print(f"   Réponse: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def publish_pypi():
    """Publie le package sur PyPI en utilisant twine et le token d'environnement ou .pypirc"""
    print("\n🔄 Publication sur PyPI...")
    twine_password = os.environ.get('TWINE_PASSWORD')
    if twine_password:
        # Pour Windows PowerShell, $env:TWINE_PASSWORD fonctionne, sinon %TWINE_PASSWORD% sous cmd
        cmd = "python -m twine upload -u __token__ -p $env:TWINE_PASSWORD dist/*"
        return run_command(cmd, "Publication PyPI avec TWINE_PASSWORD")
    elif os.path.exists(os.path.expanduser('~/.pypirc')):
        return run_command("python -m twine upload dist/*", "Publication PyPI avec .pypirc")
    else:
        print("❌ Aucun token PyPI trouvé dans TWINE_PASSWORD ni de fichier .pypirc détecté. La publication ne peut pas continuer sans authentification.")
        return False

def main():
    """Fonction principale"""
    print("🚀 Début du processus de release, publication GitHub et PyPI...")
    print("=" * 60)
    
    # 1. Vérifier le statut Git
    if not check_git_status():
        print("❌ Arrêt du processus - veuillez commiter vos changements")
        return False
    
    # 2. Construire le package
    if not run_command("python -m build", "Construction du package"):
        print("❌ Échec de la construction du package")
        return False
    
    # 3. Vérifier le package
    if not run_command("python -m twine check dist/*", "Vérification du package"):
        print("❌ Échec de la vérification du package")
        return False
    
    # 4. Créer la release GitHub
    if not create_github_release():
        print("❌ Échec de la création de la release GitHub")
        print("\n💡 Pour créer la release manuellement:")
        print("1. Allez sur https://github.com/ThePhoenixAgency/py-stats-toolkit/releases")
        print("2. Cliquez sur 'Create a new release'")
        print("3. Sélectionnez le tag v1.0.2")
        print("4. Remplissez les informations et publiez")
        return False
    
    # 5. Publier sur PyPI
    if not publish_pypi():
        print("❌ Échec de la publication PyPI")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 Processus terminé avec succès!")
    print("📤 La publication sur PyPI est terminée.")
    print("⏱️  Cela peut prendre quelques minutes pour apparaître sur PyPI...")
    print("\n🔗 Liens utiles:")
    print("- Release GitHub: https://github.com/ThePhoenixAgency/py-stats-toolkit/releases")
    print("- PyPI: https://pypi.org/project/py-stats-toolkit/")
    print("- Actions: https://github.com/ThePhoenixAgency/py-stats-toolkit/actions")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 