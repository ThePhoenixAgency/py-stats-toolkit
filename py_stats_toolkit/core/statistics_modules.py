
import pandas as pd
import numpy as np
from collections import Counter, defaultdict


def apply_frequentiel(historique, nb_max=50):
    """Retourne les numéros les moins tirés (rareté)"""
    freq_counter = Counter()
    for nums in historique["boules"]:
        freq_counter.update(map(int, str(nums).split()))
    rarete = {i: nb_max - freq_counter.get(i, 0) for i in range(1, nb_max + 1)}
    return rarete


def apply_retard(historique, nb_max=50):
    """Retourne le nombre de tirages depuis la dernière apparition de chaque numéro"""
    retard = {i: 0 for i in range(1, nb_max + 1)}
    for _, row in historique[::-1].iterrows():
        nums = list(map(int, str(row["boules"]).split()))
        for i in retard:
            if retard[i] == 0 and i in nums:
                retard[i] = historique.shape[0] - _
    return retard


def detect_sequences(historique):
    """Détecte les séquences croissantes simples (ex. 12,13,14)"""
    sequences = []
    for _, row in historique.iterrows():
        nums = sorted(map(int, str(row["boules"]).split()))
        for i in range(len(nums) - 2):
            if nums[i + 1] == nums[i] + 1 and nums[i + 2] == nums[i] + 2:
                sequences.append(tuple(nums[i:i + 3]))
    return Counter(sequences)


def markov_prediction(historique, profondeur=2):
    """Réseau de Markov simplifié : prédit les numéros susceptibles de suivre un autre"""
    transitions = defaultdict(Counter)
    for _, row in historique.iterrows():
        nums = list(map(int, str(row["boules"]).split()))
        for i in range(len(nums) - profondeur):
            precedent = tuple(nums[i:i + profondeur])
            suivant = nums[i + profondeur]
            transitions[precedent][suivant] += 1
    return {k: v.most_common(1)[0][0] for k, v in transitions.items() if v}


def bayesian_adjustment(historique, nb_max=50):
    """Pondération des numéros selon une loi bayésienne très simple"""
    freq = apply_frequentiel(historique, nb_max)
    total = sum(freq.values())
    return {k: v / total for k, v in freq.items()}


def fractal_patterns(historique):
    """Analyse naïve de patterns fractals : répétitions de sous-séquences"""
    fractals = Counter()
    for _, row in historique.iterrows():
        nums = list(map(int, str(row["boules"]).split()))
        seen = set()
        for i in range(len(nums) - 1):
            pair = (nums[i], nums[i + 1])
            if pair in seen:
                fractals[pair] += 1
            else:
                seen.add(pair)
    return fractals


def periodic_trends(historique, periodicity=5):
    """Retourne les numéros qui apparaissent tous les X tirages"""
    periodic = Counter()
    for idx, row in historique.iterrows():
        if idx % periodicity == 0:
            nums = list(map(int, str(row["boules"]).split()))
            periodic.update(nums)
    return periodic


def calculate_ia_weight(grid, rarete, bayes):
    """Retourne une pondération IA simulée combinant rareté et probabilité bayésienne"""
    score = 0
    for n in grid:
        score += rarete.get(n, 0) * bayes.get(n, 0)
    return score / len(grid)
