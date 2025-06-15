import numpy as np
import pandas as pd
from scipy import stats
from ..core.AbstractClassBase import StatisticalModule
from ..utils.parallel import ParallelProcessor

class BioStatsModule(StatisticalModule):
    """Module pour les analyses biostatistiques."""
    
    def __init__(self, n_jobs: int = -1):
        super().__init__()
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)
    
    def process(self, data, test_type="t-test", **kwargs):
        """
        Effectue des tests statistiques.
        
        Args:
            data: Données d'entrée (DataFrame avec groupes)
            test_type: Type de test ('t-test', 'anova', 'chi2', etc.)
            **kwargs: Arguments additionnels
            
        Returns:
            Résultats des tests
        """
        self.validate_data(data)
        
        if test_type == "t-test":
            return self._t_test(data, **kwargs)
        elif test_type == "anova":
            return self._anova(data, **kwargs)
        elif test_type == "chi2":
            return self._chi2_test(data, **kwargs)
        else:
            raise ValueError(f"Type de test {test_type} non supporté")
    
    def _t_test(self, data, group_col, value_col, **kwargs):
        """Test t de Student."""
        groups = data[group_col].unique()
        if len(groups) != 2:
            raise ValueError("Le test t nécessite exactement 2 groupes")
        
        group1 = data[data[group_col] == groups[0]][value_col]
        group2 = data[data[group_col] == groups[1]][value_col]
        
        t_stat, p_value = stats.ttest_ind(group1, group2, **kwargs)
        
        self.result = {
            'Test': 't-test',
            'Statistique t': t_stat,
            'p-valeur': p_value,
            'Groupes': groups.tolist()
        }
        
        return self.result
    
    def _anova(self, data, group_col, value_col, **kwargs):
        """Analyse de variance (ANOVA)."""
        groups = data[group_col].unique()
        group_data = [data[data[group_col] == g][value_col] for g in groups]
        
        f_stat, p_value = stats.f_oneway(*group_data, **kwargs)
        
        self.result = {
            'Test': 'ANOVA',
            'Statistique F': f_stat,
            'p-valeur': p_value,
            'Groupes': groups.tolist()
        }
        
        return self.result
    
    def _chi2_test(self, data, **kwargs):
        """Test du chi2."""
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Les données doivent être un DataFrame")
        
        chi2_stat, p_value, dof, expected = stats.chi2_contingency(data, **kwargs)
        
        self.result = {
            'Test': 'Chi2',
            'Statistique Chi2': chi2_stat,
            'p-valeur': p_value,
            'Degrés de liberté': dof
        }
        
        return self.result
    
    def survival_analysis(self, data, time_col, event_col, group_col=None):
        """
        Analyse de survie.
        
        Args:
            data: DataFrame avec les données
            time_col: Colonne des temps
            event_col: Colonne des événements
            group_col: Colonne des groupes (optionnelle)
            
        Returns:
            Résultats de l'analyse de survie
        """
        from lifelines import KaplanMeierFitter
        
        kmf = KaplanMeierFitter()
        
        if group_col is None:
            kmf.fit(data[time_col], data[event_col])
            self.result = {
                'Médiane de survie': kmf.median_survival_time_,
                'Courbe de survie': kmf.survival_function_
            }
        else:
            groups = data[group_col].unique()
            results = {}
            
            for group in groups:
                group_data = data[data[group_col] == group]
                kmf.fit(group_data[time_col], group_data[event_col])
                results[group] = {
                    'Médiane de survie': kmf.median_survival_time_,
                    'Courbe de survie': kmf.survival_function_
                }
            
            self.result = results
        
        return self.result 