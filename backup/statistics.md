
# 📊 Modules statistiques et mathématiques — Optimiseur Génétique

Ce document liste et décrit les modules disponibles ou planifiés pour l’optimisation génétique de grilles de loterie. Ils sont regroupés par catégorie fonctionnelle.

---

## 🧠 Fondamentaux logiques et fréquentiels

- **Fréquence absolue et relative**  
  → Nombre d'apparitions brutes et en proportion du total de tirages

- **Entropie de Shannon**  
  → Mesure d'imprévisibilité dans la distribution des numéros

- **Distribution empirique des probabilités**  
  → Courbe probabiliste dérivée des fréquences observées

- **Déviation standard & variance**  
  → Mesures de dispersion des combinaisons générées

- **Comptage pondéré (wRAG)**  
  → Fréquences pondérées par distance ou priorité

- **Mode / Médiane / Moyenne glissante**  
  → Analyse des statistiques centrales dans des fenêtres de temps

---

## ⏳ Modules cycliques et temporels

- **Détection de cycles fixes (13, 28, 33 jours, etc.)**  
  → Identification de rythmes calendaires probables

- **Fenêtres glissantes & convolution**  
  → Pondération temporelle appliquée sur les données passées

- **Auto-corrélation**  
  → Similarité d’un tirage avec des tirages précédents à intervalle constant

- **Score temporel dynamique (hot/cold cycles)**  
  → Calcul du statut chaud/froid en fonction de la période en cours

---

## 🧬 Modules évolutifs et génétiques

- **Algorithmes génétiques (top-N, croisement, mutation intelligente)**  
  → Évolution guidée par fitness, croisement sélectif, mutations ciblées

- **Rollback adaptatif**  
  → Retour à des états antérieurs en cas de stagnation du score

- **Multi-modèle avec scoring moyen**  
  → Utilisation de plusieurs modules avec pondération collaborative

- **Sélection naturelle pondérée**  
  → Favorise les chromosomes statistiquement supérieurs

- **Boost adaptatif sur pics/cycles**  
  → Augmentation temporaire de poids sur modules cycliques dominants

---

## 🎲 Probabilités et chaînes

- **Chaînes de Markov (1er et 2ᵉ ordre)**  
  → Transitions probables entre grilles ou états

- **Tables de transition**  
  → Matrice décrivant les probabilités de passage d'un état à un autre

- **Poids conditionnels inter-tirages**  
  → Influence d’un tirage sur la probabilité des suivants

- **Probabilités Bayésiennes sur plages**  
  → Score bayésien appliqué à des groupes de numéros

---

## 📈 Modules avancés & topologiques

- **Transformée de Fourier (FFT)**  
  → Extraction de fréquences profondes dans la série temporelle des tirages

- **Analyse fractale (autosimilarité)**  
  → Détection de répétitions auto-similaires dans la distribution

- **Théorie des jeux (positionnement stratégique)**  
  → Simulation de décisions en compétition avec d’autres stratégies

- **Clusters numériques (KMeans / heuristiques locales)**  
  → Regroupement naturel de combinaisons similaires

- **Fibonacci & suites récurrentes**  
  → Détection de motifs basés sur des suites mathématiques

- **Score de topologie combinatoire**  
  → Analyse de positionnement dans la grille (zones chaudes/froides)

---

## 🧩 Modules personnalisés ou hybrides

- **Scoring composite multijeux**  
  → Comparaison croisée entre plusieurs types de loteries

- **Score prédictif pondéré par recoupement (multi-lotteries)**  
  → Fusion de prédictions issues de différentes sources

- **Historisation des grilles “gagnantes” avec patterns associés**  
  → Archivage et apprentissage sur les grilles gagnantes passées

- **Corrélations croisées entre jeux et dates**  
  → Recherche de correspondances entre calendrier et sorties

---
