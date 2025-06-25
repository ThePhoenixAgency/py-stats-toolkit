#!/usr/bin/env python3
"""
Script complet pour la release et publication automatique
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
    repo_owner = "PhoenixGuardianTools"
    repo_name = "py-stats-toolkit"
    tag_name = "v1.0.2"
    
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
        "body": f"""## 🚀 Release {tag_name} - Nettoyage complet et conformité PyPI

### ✨ Nouvelles fonctionnalités
- Script `clean_cache.py` pour nettoyage automatique des fichiers cache
- Messages de confirmation améliorés dans tous les scripts utilitaires

### 🔧 Améliorations
- Correction de la configuration de licence dans `pyproject.toml` (format SPDX)
- Mise à jour de l'email de contact vers `autopublisher.ai@gmail.com`
- Amélioration des workflows GitHub Actions
- Suppression de `setup.py` redondant

### 🐛 Corrections
- Conformité PyPI complète
- Suppression de tous les fichiers cache et temporaires
- Correction des warnings de dépréciation setuptools

### 📦 Installation
```bash
pip install py-stats-toolkit==1.0.2
```

### 🔗 Liens
- [Documentation](https://py-stats-toolkit.readthedocs.io/)
- [PyPI](https://pypi.org/project/py-stats-toolkit/)
- [Issues](https://github.com/PhoenixGuardianTools/py-stats-toolkit/issues)

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

def main():
    """Fonction principale"""
    print("🚀 Début du processus de release et publication...")
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
        print("1. Allez sur https://github.com/PhoenixGuardianTools/py-stats-toolkit/releases")
        print("2. Cliquez sur 'Create a new release'")
        print("3. Sélectionnez le tag v1.0.2")
        print("4. Remplissez les informations et publiez")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 Processus terminé avec succès!")
    print("📤 La publication sur PyPI se fera automatiquement via GitHub Actions")
    print("⏱️  Cela peut prendre quelques minutes...")
    print("\n🔗 Liens utiles:")
    print("- Release GitHub: https://github.com/PhoenixGuardianTools/py-stats-toolkit/releases")
    print("- PyPI: https://pypi.org/project/py-stats-toolkit/")
    print("- Actions: https://github.com/PhoenixGuardianTools/py-stats-toolkit/actions")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 