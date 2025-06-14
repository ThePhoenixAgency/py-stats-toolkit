# genetiques.py
# Modules de la catégorie genetiques

from AbstractModule import BaseModule


# ---- AlgoGenetiqueModule ----


class AlgoGenetiqueModule(BaseModule):
    def __init__(self):
        super().__init__("AlgoGenetiqueModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- RollbackAdaptatifModule ----


class RollbackAdaptatifModule(BaseModule):
    def __init__(self):
        super().__init__("RollbackAdaptatifModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- MultiModeleScoreMoyenModule ----


class MultiModeleScoreMoyenModule(BaseModule):
    def __init__(self):
        super().__init__("MultiModeleScoreMoyenModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- SelectionNaturelleModule ----


class SelectionNaturelleModule(BaseModule):
    def __init__(self):
        super().__init__("SelectionNaturelleModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- BoostAdaptatifModule ----


class BoostAdaptatifModule(BaseModule):
    def __init__(self):
        super().__init__("BoostAdaptatifModule")

    def get_entity_scores(self, data, rules):
        return {}, {}