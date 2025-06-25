#!/usr/bin/env python3
"""
Script pour créer automatiquement une release GitHub
"""

import os
import requests
import json
from datetime import datetime

def create_github_release():
    """Crée une release GitHub via l'API"""
    
    # Configuration
    repo_owner = "PhoenixGuardianTools"
    repo_name = "py-stats-toolkit"
    tag_name = "v1.0.2"
    
    # Le token GitHub doit être dans les variables d'environnement
    github_token = os.getenv('GITHUB_TOKEN')
    
    if not github_token:
        print("❌ Erreur: GITHUB_TOKEN non défini dans les variables d'environnement")
        print("💡 Pour définir le token: set GITHUB_TOKEN=your_token_here")
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
            print(f"🏷️  Tag: {release_info['tag_name']}")
            print(f"📦 Assets: {len(release_info.get('assets', []))}")
            return True
        else:
            print(f"❌ Erreur lors de la création de la release:")
            print(f"   Status: {response.status_code}")
            print(f"   Réponse: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

if __name__ == "__main__":
    success = create_github_release()
    if success:
        print("\n🎉 La release GitHub a été créée avec succès!")
        print("📤 La publication sur PyPI se fera automatiquement via GitHub Actions.")
    else:
        print("\n💡 Pour créer la release manuellement:")
        print("1. Allez sur https://github.com/PhoenixGuardianTools/py-stats-toolkit/releases")
        print("2. Cliquez sur 'Create a new release'")
        print("3. Sélectionnez le tag v1.0.2")
        print("4. Remplissez les informations et publiez") 