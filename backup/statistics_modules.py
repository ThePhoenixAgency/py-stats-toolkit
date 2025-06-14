# ========== statistics_modules.py ==========

from collections import Counter
import math

class StatModule:
    def __init__(self, name):
        self.name = name

    def get_entity_scores(self, data, rules):
        raise NotImplementedError


class FrequenceAbsolueModule(StatModule):
    def __init__(self):
        super().__init__("Fréquence Absolue")

    def get_entity_scores(self, data, rules):
        nums = [n for row in data['numeros'] for n in row]
        stars = [s for row in data['etoiles'] for s in row]
        return Counter(nums), Counter(stars)


class EntropieShannonModule(StatModule):
    def __init__(self):
        super().__init__("Entropie de Shannon")

    def get_entity_scores(self, data, rules):
        nums = [n for row in data['numeros'] for n in row]
        stars = [s for row in data['etoiles'] for s in row]
        c_n = Counter(nums)
        c_s = Counter(stars)

        def entropy(counter):
            total = sum(counter.values())
            return -sum((v / total) * math.log2(v / total) for v in counter.values() if v > 0)

        score_n = {k: 1.0 - entropy(Counter({k: v})) for k, v in c_n.items()}
        score_s = {k: 1.0 - entropy(Counter({k: v})) for k, v in c_s.items()}
        return score_n, score_s