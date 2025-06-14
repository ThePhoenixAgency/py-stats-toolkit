
# modules/abstract/AbstractModule.py

class BaseModule:
    def __init__(self, name="Unnamed Module"):
        self.name = name

    def prepare(self, data, rules):
        pass

    def score(self, *args, **kwargs):
        raise NotImplementedError("Chaque module doit implémenter la méthode score()")


class BaseGenerativeModule(BaseModule):
    def generate_scores(self, data, rules):
        raise NotImplementedError("Méthode de génération manquante")


class BaseEvaluativeModule(BaseModule):
    def score_grid(self, main_numbers, stars, rules):
        raise NotImplementedError("Méthode de score de grille manquante")
    def get_entity_scores(self, data, rules):
        """
        Méthode à surcharger pour générer des scores basés sur les entités.
        Doit retourner deux dictionnaires : (scores_nombres, scores_etoiles)
        """
        raise NotImplementedError("La méthode get_entity_scores doit être implémentée dans le module.")

    def supports(self, game_name):
        """
        Optionnel : Permet de restreindre ce module à certains jeux (euromillions, loto, etc.)
        """
        return True

    def description(self):
        """
        Retourne une description textuelle du module.
        """
        return self.name
