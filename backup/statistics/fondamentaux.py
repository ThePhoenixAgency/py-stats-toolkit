# fondamentaux.py
# Modules de la catégorie fondamentaux

from AbstractModule import BaseModule


# ---- FrequenceAbsolueRelativeModule ----


class FrequenceAbsolueRelativeModule(BaseModule):
    def __init__(self):
        super().__init__("FrequenceAbsolueRelativeModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- EntropieShannonModule ----


class EntropieShannonModule(BaseModule):
    def __init__(self):
        super().__init__("EntropieShannonModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- DistributionEmpiriqueModule ----


class DistributionEmpiriqueModule(BaseModule):
    def __init__(self):
        super().__init__("DistributionEmpiriqueModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- VarianceDeviationModule ----


class VarianceDeviationModule(BaseModule):
    def __init__(self):
        super().__init__("VarianceDeviationModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- ComptagePondereWRAGModule ----


class ComptagePondereWRAGModule(BaseModule):
    def __init__(self):
        super().__init__("ComptagePondereWRAGModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- ModeMedianeMoyenneGlissanteModule ----


class ModeMedianeMoyenneGlissanteModule(BaseModule):
    def __init__(self):
        super().__init__("ModeMedianeMoyenneGlissanteModule")

    def get_entity_scores(self, data, rules):
        return {}, {}