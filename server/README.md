# Serveur API Py-Stats-Toolkit

Ce dossier contient le serveur API REST pour Py-Stats-Toolkit, construit avec FastAPI.

## 🚀 Installation

1. Assurez-vous d'avoir Python 3.8+ installé
2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## 🛠️ Configuration

1. Créez un fichier `.env` à la racine du dossier `server` :
```env
APP_NAME="Py-Stats-Toolkit API"
VERSION="0.1.0"
HOST="0.0.0.0"
PORT=8000
DEBUG=true
SECRET_KEY="votre_clé_secrète_ici"
```

## 🏃‍♂️ Démarrage

Pour démarrer le serveur en mode développement :
```bash
python main.py
```

Le serveur sera accessible à l'adresse : http://localhost:8000

## 📚 Documentation API

Une fois le serveur démarré, la documentation interactive est disponible aux adresses :
- Swagger UI : http://localhost:8000/docs
- ReDoc : http://localhost:8000/redoc

## 🔍 Endpoints Disponibles

- `GET /` : Page d'accueil
- `GET /health` : Vérification de l'état du serveur
- `POST /analyze` : Endpoint principal pour l'analyse statistique

## 🔒 Sécurité

- Le serveur utilise CORS pour la sécurité
- Les tokens JWT sont utilisés pour l'authentification
- Les données sensibles sont stockées dans des variables d'environnement

## 🧪 Tests

Pour exécuter les tests :
```bash
pytest tests/
```

## 📝 Logs

Les logs sont configurés pour être affichés dans la console et peuvent être redirigés vers un fichier.

## 🔄 Déploiement

Pour le déploiement en production :
1. Désactivez le mode DEBUG
2. Changez la SECRET_KEY
3. Configurez les CORS_ORIGINS
4. Utilisez un serveur WSGI comme Gunicorn

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request 