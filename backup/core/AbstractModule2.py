
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
