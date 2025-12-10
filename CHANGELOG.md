# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère à [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.5] - 2025-12-10

### Changed
- **BREAKING:** Mise à jour de la version minimale de Python de 3.8 à 3.9
- Mise à jour majeure de toutes les dépendances vers leurs dernières versions sécurisées
  - numpy: >=2.0.0 (précédemment >=1.21.0)
  - pandas: >=2.0.0 (précédemment >=1.3.0)
  - scipy: >=1.10.0 (précédemment >=1.7.0)
  - matplotlib: >=3.8.0 (précédemment >=3.4.0)
  - scikit-learn: >=1.3.0 (précédemment >=0.24.0)
  - fastapi: >=0.115.0 (précédemment >=0.68.0)
  - pydantic: >=2.10.0 (précédemment >=1.8.0)
  - cryptography: >=44.0.0 (précédemment >=3.4.0)
  - pytest: >=8.3.0 (précédemment >=7.0.0)
  - black: >=24.10.0 (précédemment >=21.5b2)
  - mypy: >=1.13.0 (précédemment >=0.910)
- Ajout du support officiel pour Python 3.12
- Mise à jour des configurations d'outils (black, mypy) pour cibler Python 3.9+

### Added
- Ajout de pip-audit>=2.10.0 aux dépendances de développement pour l'analyse de sécurité

### Removed
- Suppression des entrées dupliquées dans requirements.txt
- Abandon du support pour Python 3.8 (fin de vie en octobre 2024)

### Security
- Correction de 22 vulnérabilités de sécurité identifiées par pip-audit
- Mise à jour de cryptography vers la version >=44.0.0 pour corriger plusieurs CVEs critiques
- Note: Une vulnérabilité subsiste dans ecdsa (CVE-2024-23342) - considérée hors périmètre par les mainteneurs

## [1.0.3] - 2025-01-27

### Added
- Script `publish_automated.py` pour publication PyPI 100% automatisée
- Workflow GitHub Actions simplifié utilisant `release_and_publish.py`
- Publication automatique sans interaction utilisateur
- Gestion d'erreurs robuste avec couleurs dans les scripts

### Changed
- Remplacement de `publish_all.py` par `publish_automated.py` (plus simple)
- Workflow GitHub Actions optimisé pour l'automatisation complète
- Amélioration des messages de confirmation dans tous les scripts

### Removed
- Script `publish_all.py` (remplacé par `publish_automated.py`)

### Fixed
- Automatisation complète de la publication PyPI
- Suppression des interactions utilisateur dans les scripts de publication

## [1.0.2] - 2025-01-27

### Added
- Script `clean_cache.py` pour nettoyage automatique des fichiers cache
- Messages de confirmation améliorés dans tous les scripts utilitaires

### Changed
- Correction de la configuration de licence dans `pyproject.toml` (format SPDX)
- Mise à jour de l'email de contact vers `autopublisher.ai@gmail.com`
- Amélioration des workflows GitHub Actions
- Suppression de `setup.py` redondant

### Fixed
- Conformité PyPI complète
- Suppression de tous les fichiers cache et temporaires
- Correction des warnings de dépréciation setuptools

## [1.0.1] - 2025-01-26

### Added
- Support pour Python 3.11
- Nouvelles dépendances : networkx, deap
- Documentation améliorée

### Changed
- Mise à jour des dépendances minimales
- Amélioration de la structure du package

## [1.0.0] - 2025-01-25

### Added
- Première version stable
- Modules de statistiques descriptives
- Modules de régression linéaire
- Modules d'analyse de corrélation
- Modules de visualisation
- Utilitaires de traitement de données
- Architecture modulaire avec polymorphisme

### Features
- Statistiques descriptives complètes
- Régression linéaire avec validation
- Analyse de corrélation multivariée
- Visualisations statistiques avancées
- Traitement et nettoyage de données
- Validation et vérification de données

## [0.1.3] - 2024-03-19

### Ajouté
- Configuration initiale du workflow GitHub Actions pour la publication automatique sur PyPI
- Documentation des changements dans le CHANGELOG

## [0.1.2] - 2024-03-19

### Ajouté
- Configuration initiale du projet
- Structure de base du toolkit statistique
- Tests unitaires de base 