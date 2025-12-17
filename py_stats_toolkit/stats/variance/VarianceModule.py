"""
=====================================================================
File : VarianceModule.py
=====================================================================
version : 2.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Refactored module for variance analysis.
Follows SOLID principles with separation of business logic and algorithms.

tags : module, stats, refactored
=====================================================================
"""

tags : module, stats
"""
from typing import Any, Dict

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

from py_stats_toolkit.algorithms import variance as variance_algos
from py_stats_toolkit.core.base import StatisticalModule
from py_stats_toolkit.core.validators import DataValidator


class VarianceModule(StatisticalModule):
    """
    Module for variance analysis (Business Logic Layer).

    Responsibilities:
    - Orchestrate variance analysis workflow
    - Manage results and state
    - Provide user-facing API

    Delegates to:
    - DataValidator for validation
    - variance_algos for computations
    """

    def __init__(self):
        """Initialize variance module."""
        super().__init__()

    def process(self, data: pd.DataFrame, group_col: str, value_col: str,
                test_type: str = "anova", **kwargs) -> Dict[str, Any]:
        """
        Perform variance analysis.

        Args:
            data: DataFrame with data
            group_col: Column name for groups
            value_col: Column name for values
            test_type: Type of test ('anova', 'kruskal', 'friedman')
            **kwargs: Additional arguments

        Returns:
            Dictionary with analysis results containing:
            For ANOVA:
                - 'f_statistic': F-statistic value
                - 'p_value': p-value
                - 'groups': List of group names
                - 'posthoc_method': 'Tukey HSD'
                - 'posthoc_results': Post-hoc test results
            For Kruskal-Wallis:
                - 'h_statistic': H-statistic value
                - 'p_value': p-value
                - 'groups': List of group names
                - 'posthoc_method': 'Mann-Whitney U'
                - 'posthoc_results': Post-hoc test results
            For Friedman:
                - 'statistic': Test statistic
                - 'p_value': p-value
                - 'groups': List of group names
                - 'posthoc_method': 'Wilcoxon'
                - 'posthoc_results': Post-hoc test results
        """
        self.validate_data(data)

        # Validation (delegated to validator)
        DataValidator.validate_data(data)
        DataValidator.validate_columns(data, [group_col, value_col])

        # Store state
        self.data = data
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import MultiComparison
from ..core.AbstractClassBase import StatisticalModule
from ...utils.parallel import ParallelProcessor

        # Computation (delegated to algorithm layer)
        if test_type == "anova":
            self.result = variance_algos.compute_anova_with_posthoc(data, group_col, value_col)
        elif test_type == "kruskal":
            self.result = variance_algos.compute_kruskal_with_posthoc(data, group_col, value_col)
        elif test_type == "friedman":
            self.result = variance_algos.compute_friedman_test(data, group_col, value_col)
        else:
            raise ValueError(f"Type de test {test_type} non supporté")

    def _anova(self, data, group_col, value_col, **kwargs):
        """Analyse de variance à un facteur."""
        # Get unique groups to maintain consistent ordering
        groups = data[group_col].unique()
        # Use groupby with get_group for efficient extraction while preserving order
        group_data = [
            data.groupby(group_col).get_group(g)[value_col].to_numpy() for g in groups
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

        # Friedman test requires complete cases - drop rows with NaN
        pivot_data = pivot_data.dropna()

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
            raise ValueError(
                f"Unsupported test type: {test_type}. "
                f"Supported types are: 'anova', 'kruskal', 'friedman'."
            )

        return self.result
