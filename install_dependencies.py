import subprocess
import sys
import pkg_resources

def install_package(package):
    """Installe un package avec pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    # Liste des dépendances principales
    dependencies = [
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "scikit-learn>=0.24.0",
        "seaborn>=0.11.0",
        "matplotlib>=3.4.0",
        "scipy>=1.7.0",
        "lifelines>=0.26.0",
        "joblib>=1.0.0",
        "statsmodels>=0.13.0",
        "ephem>=4.1.0"
    ]
    
    # Dépendances supplémentaires pour les fonctionnalités avancées
    additional_deps = [
        "scikit-optimize>=0.9.0",  # Pour l'optimisation
        "tensorflow>=2.8.0",       # Pour le deep learning
        "torch>=1.10.0",          # Pour le deep learning
        "prophet>=1.1.0",         # Pour la prévision de séries temporelles
        "pmdarima>=2.0.0",        # Pour l'analyse ARIMA
        "arch>=5.0.0",            # Pour l'analyse GARCH
        "ta>=0.10.0",             # Pour l'analyse technique
        "yfinance>=0.1.70",       # Pour les données financières
        "plotly>=5.5.0",          # Pour les visualisations interactives
        "dash>=2.0.0",            # Pour les dashboards
        "streamlit>=1.0.0",       # Pour les applications web
        "fastapi>=0.70.0",        # Pour les API
        "uvicorn>=0.15.0",        # Pour servir les API
        "pytest>=6.2.5",          # Pour les tests
        "black>=21.12b0",         # Pour le formatage du code
        "flake8>=4.0.1",          # Pour le linting
        "mypy>=0.931",            # Pour le typage statique
        "sphinx>=4.4.0",          # Pour la documentation
        "jupyter>=1.0.0",         # Pour les notebooks
        "ipykernel>=6.0.0"        # Pour l'intégration avec Jupyter
    ]
    
    print("Installation des dépendances principales...")
    for dep in dependencies:
        try:
            install_package(dep)
            print(f"✓ {dep} installé avec succès")
        except Exception as e:
            print(f"✗ Erreur lors de l'installation de {dep}: {str(e)}")
    
    print("\nInstallation des dépendances supplémentaires...")
    for dep in additional_deps:
        try:
            install_package(dep)
            print(f"✓ {dep} installé avec succès")
        except Exception as e:
            print(f"✗ Erreur lors de l'installation de {dep}: {str(e)}")
    
    print("\nVérification des installations...")
    for dep in dependencies + additional_deps:
        try:
            pkg_resources.require(dep)
            print(f"✓ {dep} est correctement installé")
        except Exception as e:
            print(f"✗ {dep} n'est pas correctement installé: {str(e)}")

if __name__ == "__main__":
    main() 