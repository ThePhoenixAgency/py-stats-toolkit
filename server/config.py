"""
Configuration du serveur Py-Stats-Toolkit
=======================================

Ce module contient les configurations du serveur API.

Tags:
    - configuration
    - server
    - settings
"""

from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Configuration du serveur."""
    
    # Configuration de base
    APP_NAME: str = "Py-Stats-Toolkit API"
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"
    
    # Configuration du serveur
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    RELOAD: bool = True
    
    # Configuration CORS
    CORS_ORIGINS: List[str] = ["*"]
    CORS_CREDENTIALS: bool = True
    CORS_METHODS: List[str] = ["*"]
    CORS_HEADERS: List[str] = ["*"]
    
    # Configuration de la sécurité
    SECRET_KEY: str = "votre_clé_secrète_ici"  # À changer en production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Configuration des logs
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    class Config:
        """Configuration de Pydantic."""
        env_file = ".env"
        case_sensitive = True

# Instance des paramètres
settings = Settings() 