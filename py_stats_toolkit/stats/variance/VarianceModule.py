"""
=====================================================================
File : VarianceModule.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module VarianceModule.py

tags : module, stats
=====================================================================
Ce module Description du module VarianceModule.py

tags : module, stats
=====================================================================
"""

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import MultiComparison

from ...utils.parallel import ParallelProcessor
from ..core.AbstractClassBase import StatisticalModule


class VarianceModule(StatisticalModule):
    """Module pour l'analyse de variance."""

    def __init__(self, n_jobs: int = -1):
        super().__init__()
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)

    def process(self, data, group_col, value_col, test_type="anova", **kwargs):
        """
        Effectue une analyse de variance.

        Args:
            data: DataFrame avec les données
            group_col: Colonne des groupes
            value_col: Colonne des valeurs
            test_type: Type de test ('anova', 'kruskal', 'friedman')
            **kwargs: Arguments additionnels

        Returns:
            Résultats de l'analyse
        """
        self.validate_data(data)

        if test_type == "anova":
            return self._anova(data, group_col, value_col, **kwargs)
        elif test_type == "kruskal":
            return self._kruskal_wallis(data, group_col, value_col, **kwargs)
        elif test_type == "friedman":
            return self._friedman(data, group_col, value_col, **kwargs)
        else:
            raise ValueError(f"Type de test {test_type} non supporté")

    def _anova(self, data, group_col, value_col, **kwargs):
        """Analyse de variance à un facteur."""
        # Use groupby for efficient group extraction
        groups = data[group_col].unique()
        group_data = [
            group[value_col].to_numpy() for _, group in data.groupby(group_col)
        ]

        f_stat, p_value = stats.f_oneway(*group_data, **kwargs)

        # Test post-hoc de Tukey
        mc = MultiComparison(data[value_col], data[group_col])
        tukey_result = mc.tukeyhsd()

        self.result = {
            "Type": "ANOVA",
            "Statistique F": f_stat,
            "p-valeur": p_value,
            "Groupes": groups.tolist(),
            "Test post-hoc": {"Méthode": "Tukey HSD", "Résultats": tukey_result},
        }

        return self.result

    def _kruskal_wallis(self, data, group_col, value_col, **kwargs):
        """Test de Kruskal-Wallis."""
        # Use groupby for efficient group extraction
        groups = data[group_col].unique()
        group_data_dict = {
            name: group[value_col].to_numpy() for name, group in data.groupby(group_col)
        }
        group_data = [group_data_dict[g] for g in groups]

        h_stat, p_value = stats.kruskal(*group_data, **kwargs)

        # Test post-hoc de Mann-Whitney - use pre-filtered data
        post_hoc_results = []
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                stat, p = stats.mannwhitneyu(
                    group_data_dict[groups[i]],
                    group_data_dict[groups[j]],
                    alternative="two-sided",
                )
                post_hoc_results.append(
                    {
                        "Groupe 1": groups[i],
                        "Groupe 2": groups[j],
                        "Statistique": stat,
                        "p-valeur": p,
                    }
                )

        self.result = {
            "Type": "Kruskal-Wallis",
            "Statistique H": h_stat,
            "p-valeur": p_value,
            "Groupes": groups.tolist(),
            "Test post-hoc": {"Méthode": "Mann-Whitney", "Résultats": post_hoc_results},
        }

        return self.result

    def _friedman(self, data, group_col, value_col, **kwargs):
        """Test de Friedman."""
        # Réorganisation des données pour le test de Friedman
        pivot_data = data.pivot(columns=group_col, values=value_col)

        # Get all column data as numpy array for efficient access
        columns = pivot_data.columns
        pivot_array = pivot_data.to_numpy()

        stat, p_value = stats.friedmanchisquare(
            *[pivot_array[:, i] for i in range(len(columns))], **kwargs
        )

        # Test post-hoc de Wilcoxon - use array indexing
        post_hoc_results = []
        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):
                stat, p = stats.wilcoxon(pivot_array[:, i], pivot_array[:, j])
                post_hoc_results.append(
                    {
                        "Groupe 1": columns[i],
                        "Groupe 2": columns[j],
                        "Statistique": stat,
                        "p-valeur": p,
                    }
                )

        self.result = {
            "Type": "Friedman",
            "Statistique": stat,
            "p-valeur": p_value,
            "Groupes": pivot_data.columns.tolist(),
            "Test post-hoc": {"Méthode": "Wilcoxon", "Résultats": post_hoc_results},
        }

        return self.result

    def get_effect_size(self):
        """
        Calcule la taille d'effet (eta-carré).

        Returns:
            Taille d'effet
        """
        if not hasattr(self, "result"):
            raise ValueError("Aucune analyse n'a été effectuée")

        if self.result["Type"] == "ANOVA":
            f_stat = self.result["Statistique F"]
            df_between = len(self.result["Groupes"]) - 1
            df_total = len(self.result["Groupes"]) * (len(self.result["Groupes"]) - 1)

            eta_squared = (f_stat * df_between) / (f_stat * df_between + df_total)

            return {
                "Taille d'effet": "Eta-carré",
                "Valeur": eta_squared,
                "Interprétation": self._interpret_eta_squared(eta_squared),
            }
        else:
            raise ValueError("La taille d'effet n'est disponible que pour l'ANOVA")

    def _interpret_eta_squared(self, eta_squared):
        """Interprète la taille d'effet eta-carré."""
        if eta_squared < 0.01:
            return "Effet négligeable"
        elif eta_squared < 0.06:
            return "Petit effet"
        elif eta_squared < 0.14:
            return "Effet moyen"
        else:
            return "Grand effet"
