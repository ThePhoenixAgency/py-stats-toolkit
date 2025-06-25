#!/usr/bin/env python3
"""
Script pour vérifier le statut de py-stats-toolkit sur PyPI
"""

import requests
import json
from datetime import datetime

def check_pypi_status():
    try:
        # Récupérer les informations du package
        url = "https://pypi.org/pypi/py-stats-toolkit/json"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            info = data['info']
            
            print("📦 STATUT PYPI - py-stats-toolkit")
            print("=" * 50)
            print(f"Version actuelle: {info.get('version', 'N/A')}")
            print(f"Résumé: {info.get('summary', 'N/A')}")
            print(f"URL: {info.get('package_url', 'N/A')}")
            
            # Afficher les versions disponibles avec dates
            releases = data['releases']
            print(f"\n📋 Versions disponibles ({len(releases)}):")
            for version in sorted(releases.keys(), reverse=True)[:5]:  # 5 dernières versions
                release_info = releases[version]
                if release_info:
                    # Prendre la date du premier fichier de la release
                    upload_time = release_info[0].get('upload_time', 'N/A') if release_info else 'N/A'
                    print(f"  - {version} (upload: {upload_time})")
                else:
                    print(f"  - {version}")
            
            print("\n✅ Package disponible sur PyPI")
                
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ Erreur JSON: {e}")
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")

if __name__ == "__main__":
    check_pypi_status() 