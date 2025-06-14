# all_stat_modules.py

# --- 🧠 Fondamentaux logiques et fréquentiels ---
class FrequenceAbsolueModule:
    def score(self, data): return len([n for row in data for n in row['numeros']]) / len(data)

class EntropieShannonModule:
    def score(self, data):
        from collections import Counter
        import math
        counts = Counter([n for row in data for n in row['numeros']])
        total = sum(counts.values())
        return -sum((c / total) * math.log2(c / total) for c in counts.values())

class DistributionEmpiriqueModule:
    def score(self, data): return len(set(n for row in data for n in row['numeros'])) / 50.0

class DeviationStandardModule:
    def score(self, data):
        import numpy as np
        vals = [n for row in data for n in row['numeros']]
        return np.std(vals)

class ComptagePondereModule:
    def score(self, data): return sum(sum(n for n in row['numeros']) for row in data) / (len(data) * 5)

class MoyenneGlissanteModule:
    def score(self, data):
        if len(data) < 2: return 0
        last = [sum(row['numeros']) for row in data[-3:]]
        return sum(last) / len(last)

# --- autres modules mis à jour à la suite ---
# ... pour l'exemple on garde cette section illustrée ...

# --- Liste combinée pour moteur ---
ALL_MODULES = [
    FrequenceAbsolueModule(), EntropieShannonModule(), DistributionEmpiriqueModule(),
    DeviationStandardModule(), ComptagePondereModule(), MoyenneGlissanteModule()
]