# Documentation Site / GitHub Pages

Ce dossier contient la documentation et le site web statique pour py-stats-toolkit, hébergé gratuitement sur GitHub Pages.

## 🌐 Accès au site

Le site est accessible à l'adresse : **https://phoenixguardiantools.github.io/py-stats-toolkit/**

## 🎯 Objectif

Ce site répond à la question : "Comment avoir un nom de domaine gratuit comme github.io?"

GitHub Pages offre un hébergement gratuit avec un domaine automatique au format :
- `username.github.io` pour les sites utilisateur/organisation
- `username.github.io/repository-name` pour les sites de projet

## 📁 Structure

```
docs/
├── index.html          # Page d'accueil principale
├── 404.html           # Page d'erreur personnalisée
├── robots.txt         # Configuration pour les moteurs de recherche
├── sitemap.xml        # Plan du site pour SEO
├── _config.yml        # Configuration Jekyll
├── CNAME.example      # Exemple pour domaine personnalisé
└── README.md          # Cette documentation
```

## 🚀 Déploiement automatique

Le site est déployé automatiquement via GitHub Actions (`.github/workflows/deploy-pages.yml`) à chaque push sur la branche principale.

## 🎨 Fonctionnalités du site

- ✅ Design responsive et moderne
- ✅ Installation et exemples d'utilisation
- ✅ Liens vers PyPI et GitHub
- ✅ SEO optimisé
- ✅ Meta tags Open Graph et Twitter Card
- ✅ Favicon personnalisé
- ✅ Page 404 personnalisée

## 📈 SEO et référencement

- Sitemap XML pour l'indexation
- Robots.txt configuré
- Meta descriptions optimisées
- Structure HTML sémantique
- Schema.org markup

## 💡 Domaine personnalisé (optionnel)

Pour utiliser un domaine personnalisé :
1. Ajouter un fichier `CNAME` avec votre domaine
2. Configurer les DNS chez votre registrar
3. Activer HTTPS dans les paramètres GitHub Pages

## 🔧 Modifications

Pour modifier le site :
1. Éditez les fichiers dans le dossier `docs/`
2. Committez et pushez les changements
3. Le site se met à jour automatiquement