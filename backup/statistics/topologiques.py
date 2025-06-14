# topologiques.py
# Modules de la catégorie topologiques

from AbstractModule import BaseModule


# ---- FourierFFTModule ----


class FourierFFTModule(BaseModule):
    def __init__(self):
        super().__init__("FourierFFTModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- FractaleAutosimilaireModule ----


class FractaleAutosimilaireModule(BaseModule):
    def __init__(self):
        super().__init__("FractaleAutosimilaireModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- TheorieDesJeuxModule ----


class TheorieDesJeuxModule(BaseModule):
    def __init__(self):
        super().__init__("TheorieDesJeuxModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- ClustersNumeriquesModule ----


class ClustersNumeriquesModule(BaseModule):
    def __init__(self):
        super().__init__("ClustersNumeriquesModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- FibonacciRecurrentModule ----


class FibonacciRecurrentModule(BaseModule):
    def __init__(self):
        super().__init__("FibonacciRecurrentModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- TopologieCombinatoireModule ----


class TopologieCombinatoireModule(BaseModule):
    def __init__(self):
        super().__init__("TopologieCombinatoireModule")

    def get_entity_scores(self, data, rules):
        return {}, {}