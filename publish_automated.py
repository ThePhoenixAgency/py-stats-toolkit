#!/usr/bin/env python3
"""
Script automatisé pour build et publication PyPI (sans release GitHub)
Basé sur publish_all.py mais 100% automatisé
"""

import subprocess
import sys
import os
import signal
import time

# Couleurs pour affichage
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
ENDC = '\033[0m'

# Liste des processus enfants pour nettoyage
child_processes = []

def cleanup_processes():
    """Nettoyer tous les processus enfants en cas d'interruption"""
    for proc in child_processes:
        try:
            if proc.poll() is None:  # Si le processus est encore actif
                proc.terminate()
                proc.wait(timeout=5)
        except:
            try:
                proc.kill()  # Force kill si nécessaire
            except:
                pass

def signal_handler(signum, frame):
    """Gestionnaire de signal pour nettoyer proprement"""
    print(f"\n{YELLOW}Interruption détectée, nettoyage des processus...{ENDC}")
    cleanup_processes()
    sys.exit(1)

# Enregistrer le gestionnaire de signal
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def run(cmd, check=True, timeout=300):
    """Exécuter une commande avec gestion d'erreur et timeout"""
    try:
        # Utiliser subprocess.Popen pour un meilleur contrôle
        proc = subprocess.Popen(
            cmd, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        child_processes.append(proc)
        
        # Attendre la fin avec timeout
        stdout, stderr = proc.communicate(timeout=timeout)
        
        if check and proc.returncode != 0:
            print(f"{RED}Erreur lors de l'exécution : {cmd}{ENDC}")
            if stderr:
                print(f"{RED}Détails: {stderr}{ENDC}")
            cleanup_processes()
            sys.exit(proc.returncode)
            
        return proc.returncode == 0
        
    except subprocess.TimeoutExpired:
        print(f"{RED}Timeout lors de l'exécution : {cmd}{ENDC}")
        proc.kill()
        cleanup_processes()
        sys.exit(1)
    except Exception as e:
        print(f"{RED}Erreur lors de l'exécution : {cmd} - {e}{ENDC}")
        cleanup_processes()
        sys.exit(1)

def install_deps():
    print(f"{GREEN}🔄 Installation des dépendances...{ENDC}")
    run("python -m pip install --upgrade pip build twine", check=True)

def build_package():
    print(f"{GREEN}🔄 Construction du package...{ENDC}")
    run("python -m build", check=True)

def check_package():
    print(f"{GREEN}🔄 Vérification du package...{ENDC}")
    run("python -m twine check dist/*", check=True)

def publish_pypi():
    print(f"{GREEN}🔄 Publication sur PyPI...{ENDC}")
    twine_password = os.environ.get('TWINE_PASSWORD')
    if twine_password:
        # Pour Windows PowerShell
        run("python -m twine upload -u __token__ -p $env:TWINE_PASSWORD dist/*", check=True)
    elif os.path.exists(os.path.expanduser('~/.pypirc')):
        run("python -m twine upload dist/*", check=True)
    else:
        print(f"{RED}Aucun token PyPI trouvé dans TWINE_PASSWORD ni de fichier .pypirc détecté.{ENDC}")
        print(f"{RED}La publication ne peut pas continuer sans authentification.{ENDC}")
        sys.exit(1)

def main():
    try:
        print(f"{GREEN}🚀 Début du processus de publication automatisé...{ENDC}")
        print("=" * 60)
        
        install_deps()
        print(f"{GREEN}✅ Dépendances installées{ENDC}")
        
        build_package()
        print(f"{GREEN}✅ Package construit{ENDC}")
        
        check_package()
        print(f"{GREEN}✅ Package vérifié{ENDC}")
        
        publish_pypi()
        print(f"{GREEN}✅ Package publié sur PyPI{ENDC}")
        
        print("\n" + "=" * 60)
        print(f"{GREEN}🎉 Publication terminée avec succès !{ENDC}")
        print(f"{YELLOW}Le package est maintenant disponible sur PyPI.{ENDC}")
        print(f"{YELLOW}Cela peut prendre quelques minutes pour apparaître.{ENDC}")
        
        print(f"\n🔗 Liens utiles:")
        print(f"- PyPI: https://pypi.org/project/py-stats-toolkit/")
        print(f"- GitHub: https://github.com/PhoenixGuardianTools/py-stats-toolkit")
        
    finally:
        cleanup_processes()

if __name__ == "__main__":
    main() 