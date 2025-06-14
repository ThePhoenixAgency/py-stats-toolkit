# cycliques.py
# Modules de la catégorie cycliques

from AbstractModule import BaseModule


# ---- CyclesFixesModule ----


class CyclesFixesModule(BaseModule):
    def __init__(self):
        super().__init__("CyclesFixesModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- FenetreGlissanteConvolutionModule ----


class FenetreGlissanteConvolutionModule(BaseModule):
    def __init__(self):
        super().__init__("FenetreGlissanteConvolutionModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- AutocorrelationModule ----


class AutocorrelationModule(BaseModule):
    def __init__(self):
        super().__init__("AutocorrelationModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- ScoreTemporelDynamiqueModule ----


class ScoreTemporelDynamiqueModule(BaseModule):
    def __init__(self):
        super().__init__("ScoreTemporelDynamiqueModule")

    def get_entity_scores(self, data, rules):
        return {}, {}