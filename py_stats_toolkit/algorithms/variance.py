"""Pure variance analysis algorithms."""

from typing import Any, Dict, List

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import MultiComparison


def compute_anova(groups: List[np.ndarray]) -> Dict[str, Any]:
    """Compute one-way ANOVA."""
    f_stat, p_value = stats.f_oneway(*groups)

    return {
        'f_statistic': f_stat,
        'p_value': p_value,
        'n_groups': len(groups)
    }


def compute_anova_with_posthoc(data: pd.DataFrame, group_col: str,
                               value_col: str) -> Dict[str, Any]:
    """Compute ANOVA with Tukey HSD post-hoc test."""
    groups = data[group_col].unique()
    group_data = [data[data[group_col] == g][value_col].values for g in groups]

    f_stat, p_value = stats.f_oneway(*group_data)

    mc = MultiComparison(data[value_col], data[group_col])
    tukey_result = mc.tukeyhsd()

    return {
        'f_statistic': f_stat,
        'p_value': p_value,
        'groups': groups.tolist(),
        'posthoc_method': 'Tukey HSD',
        'posthoc_results': tukey_result
    }


def compute_kruskal_wallis(groups: List[np.ndarray]) -> Dict[str, Any]:
    """Compute Kruskal-Wallis H-test."""
    h_stat, p_value = stats.kruskal(*groups)

    return {
        'h_statistic': h_stat,
        'p_value': p_value,
        'n_groups': len(groups)
    }


def compute_kruskal_with_posthoc(data: pd.DataFrame, group_col: str,
                                 value_col: str) -> Dict[str, Any]:
    """Compute Kruskal-Wallis with Mann-Whitney U post-hoc tests."""
    groups = data[group_col].unique()
    group_data = [data[data[group_col] == g][value_col].values for g in groups]

    h_stat, p_value = stats.kruskal(*group_data)

    post_hoc_results = []
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            stat, p = stats.mannwhitneyu(
                data[data[group_col] == groups[i]][value_col],
                data[data[group_col] == groups[j]][value_col],
                alternative='two-sided'
            )
            post_hoc_results.append({
                'group1': groups[i],
                'group2': groups[j],
                'statistic': stat,
                'p_value': p
            })

    return {
        'h_statistic': h_stat,
        'p_value': p_value,
        'groups': groups.tolist(),
        'posthoc_method': 'Mann-Whitney U',
        'posthoc_results': post_hoc_results
    }


def compute_friedman_test(data: pd.DataFrame, group_col: str,
                          value_col: str) -> Dict[str, Any]:
    """Compute Friedman test for repeated measures."""
    pivot_data = data.pivot(columns=group_col, values=value_col)

    stat, p_value = stats.friedmanchisquare(*[pivot_data[col] for col in pivot_data.columns])

    post_hoc_results = []
    for i in range(len(pivot_data.columns)):
        for j in range(i + 1, len(pivot_data.columns)):
            stat_w, p_w = stats.wilcoxon(
                pivot_data[pivot_data.columns[i]],
                pivot_data[pivot_data.columns[j]]
            )
            post_hoc_results.append({
                'group1': pivot_data.columns[i],
                'group2': pivot_data.columns[j],
                'statistic': stat_w,
                'p_value': p_w
            })

    return {
        'statistic': stat,
        'p_value': p_value,
        'groups': pivot_data.columns.tolist(),
        'posthoc_method': 'Wilcoxon',
        'posthoc_results': post_hoc_results
    }
