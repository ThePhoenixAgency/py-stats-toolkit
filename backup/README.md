
# 🎯 Optimiseur Génétique Euromillions

Ce projet vise à générer des grilles optimisées pour l'Euromillions en combinant :
- Statistiques avancées (fréquences, entropie, fractales, etc.)
- Modules catégorisés (fondamentaux, cycliques, génétiques, probabilistes, topologiques)
- Algorithme génétique auto-adaptatif
- Moteur de prédiction entièrement automatisé

---

## 📦 Installation

```bash
python install.py
```

Cela :
- Crée les dossiers nécessaires
- Organise les fichiers selon l'architecture du projet

---

## 🚀 Lancement du moteur

### Option 1 — Grille + Fichier

```bash
./launch_prediction.sh
```

> Sauvegarde dans `strategie_euromillions_force.json`

### Option 2 — Grille + Affichage immédiat

```bash
./launch_and_print.sh
```

> Affiche la grille dans le terminal

---

## 📁 Structure simplifiée du projet

```
📦 /core
  ├─ prediction_engine.py
  ├─ trainer.py
  ├─ rules.py
  ├─ ...
📦 /modules
  ├─ fondamentaux/
  ├─ cycliques/
  ├─ génétiques/
  ├─ probabilistes/
  ├─ topologiques/
📦 /data
  ├─ euromillions2.csv
📄 install.py
📄 launch_prediction.sh
📄 launch_and_print.sh
📄 README.md
```

---

## 🔒 .gitignore

Seuls les fichiers suivants sont **conservés** dans le dépôt :
- `README.md`
- `install.py`
- `launch_*.sh`
- Fichiers sources dans `/core/` et `/modules/`
