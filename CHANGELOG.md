# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère à [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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