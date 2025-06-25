#!/usr/bin/env python3
"""
Script simplifié pour construire le package et préparer la publication
"""

import subprocess
import sys

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

def main():
    """Fonction principale"""
    print("🚀 Préparation de la publication v1.0.2...")
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
    
    print("\n" + "=" * 60)
    print("🎉 Package prêt pour la publication!")
    print("📦 Fichiers créés dans le dossier 'dist/':")
    print("   - py_stats_toolkit-1.0.2.tar.gz")
    print("   - py_stats_toolkit-1.0.2-py3-none-any.whl")
    
    print("\n🚀 Étapes pour publier:")
    print("1. Allez sur: https://github.com/PhoenixGuardianTools/py-stats-toolkit/releases")
    print("2. Cliquez sur 'Create a new release'")
    print("3. Sélectionnez le tag v1.0.2")
    print("4. Remplissez les informations de la release")
    print("5. Publiez la release")
    print("6. La publication PyPI se fera automatiquement via GitHub Actions")
    
    print("\n🔗 Liens utiles:")
    print("- Releases: https://github.com/PhoenixGuardianTools/py-stats-toolkit/releases")
    print("- Actions: https://github.com/PhoenixGuardianTools/py-stats-toolkit/actions")
    print("- PyPI: https://pypi.org/project/py-stats-toolkit/")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 