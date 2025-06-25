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
    run("python -m pip install --upgrade pip build sphinx sphinx-rtd-theme twine", check=True)

def build_package():
    run("python -m build", check=True)

def build_docs():
    run("sphinx-build -b html docs docs/_build/html", check=True)

def git_push_docs():
    run("git add -f docs/_build/html", check=True)
    run("git commit -m 'Mise à jour de la documentation HTML après build'", check=False)
    run("git push", check=True)

def publish_pypi():
    twine_password = os.environ.get('TWINE_PASSWORD')
    if twine_password:
        run("python -m twine upload -u __token__ -p $env:TWINE_PASSWORD dist/*", check=True)
    elif os.path.exists(os.path.expanduser('~/.pypirc')):
        run("python -m twine upload dist/*", check=True)
    else:
        print(f"{RED}Aucun token PyPI trouvé dans TWINE_PASSWORD ni de fichier .pypirc détecté.\nLa publication ne peut pas continuer sans authentification.{ENDC}")
        sys.exit(1)

def main():
    try:
        print(f"{GREEN}🚀 Début du processus de publication...{ENDC}")
        
        install_deps()
        print(f"{GREEN}✅ Dépendances installées{ENDC}")
        
        build_package()
        print(f"{GREEN}✅ Package construit{ENDC}")
        
        build_docs()
        print(f"{GREEN}✅ Documentation générée{ENDC}")
        
        git_push_docs()
        print(f"{GREEN}✅ Documentation poussée sur Git{ENDC}")
        
        print(f"{YELLOW}Vérifie que tout est OK dans dist/ et docs/_build/html avant de publier.{ENDC}")
        confirm = input(f"{YELLOW}Souhaites-tu publier sur PyPI ? (o/n) : {ENDC}").strip().lower()
        if confirm == 'o':
            publish_pypi()
            print(f"{GREEN}🎉 Publication terminée avec succès !{ENDC}")
        else:
            print(f"{RED}Publication annulée.{ENDC}")
    finally:
        cleanup_processes()

if __name__ == "__main__":
    main() 