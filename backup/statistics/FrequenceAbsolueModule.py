from AbstractClassStatistics import AbstractStatisticsModule
from collections import Counter

class FrequenceAbsolueModule(AbstractStatisticsModule):
    def score(self, data):
        compteur = Counter()
        for ligne in data:
            compteur.update(ligne['numeros'])
        return sum(compteur.values()) / len(data)

    def score_detaille(self, data):
        compteur_n = Counter()
        compteur_e = Counter()
        for ligne in data:
            compteur_n.update(ligne['numeros'])
            compteur_e.update(ligne['etoiles'])
        return {
            'numeros': dict(compteur_n),
            'etoiles': dict(compteur_e)
        }