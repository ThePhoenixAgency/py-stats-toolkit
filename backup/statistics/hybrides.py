# hybrides.py
# Modules de la catégorie hybrides

from AbstractModule import BaseModule


# ---- ScoreCompositeMultijeuxModule ----


class ScoreCompositeMultijeuxModule(BaseModule):
    def __init__(self):
        super().__init__("ScoreCompositeMultijeuxModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- RecoupementMultiLotteriesModule ----


class RecoupementMultiLotteriesModule(BaseModule):
    def __init__(self):
        super().__init__("RecoupementMultiLotteriesModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- HistoriqueGrillesGagnantesModule ----


class HistoriqueGrillesGagnantesModule(BaseModule):
    def __init__(self):
        super().__init__("HistoriqueGrillesGagnantesModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- CorrelationJeuxDatesModule ----


class CorrelationJeuxDatesModule(BaseModule):
    def __init__(self):
        super().__init__("CorrelationJeuxDatesModule")

    def get_entity_scores(self, data, rules):
        return {}, {}