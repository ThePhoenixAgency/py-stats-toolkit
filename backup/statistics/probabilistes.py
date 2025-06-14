# probabilistes.py
# Modules de la catégorie probabilistes

from AbstractModule import BaseModule


# ---- MarkovOrdre1Module ----


class MarkovOrdre1Module(BaseModule):
    def __init__(self):
        super().__init__("MarkovOrdre1Module")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- MarkovOrdre2Module ----


class MarkovOrdre2Module(BaseModule):
    def __init__(self):
        super().__init__("MarkovOrdre2Module")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- TablesTransitionModule ----


class TablesTransitionModule(BaseModule):
    def __init__(self):
        super().__init__("TablesTransitionModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- PoidsConditionnelsModule ----


class PoidsConditionnelsModule(BaseModule):
    def __init__(self):
        super().__init__("PoidsConditionnelsModule")

    def get_entity_scores(self, data, rules):
        return {}, {}

# ---- ProbabiliteBayesiennePlagesModule ----


class ProbabiliteBayesiennePlagesModule(BaseModule):
    def __init__(self):
        super().__init__("ProbabiliteBayesiennePlagesModule")

    def get_entity_scores(self, data, rules):
        return {}, {}