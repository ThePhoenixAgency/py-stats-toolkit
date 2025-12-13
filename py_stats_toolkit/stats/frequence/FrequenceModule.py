'''
=====================================================================
File : FrequenceModule.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module FrequenceModule.py

tags : module, stats
=====================================================================
Ce module Description du module FrequenceModule.py

tags : module, stats
=====================================================================
'''

import numpy as np
import pandas as pd
from ..core.AbstractClassBase import StatisticalModule
from ...utils.parallel import ParallelProcessor

class FrequenceModule(StatisticalModule):
    """Module pour l'analyse de fréquence."""
    
    def __init__(self, n_jobs: int = -1):
        super().__init__()
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)
    
    def process(self, data, normalize=False, **kwargs):
        """
        Calcule les fréquences des valeurs.
        
        Args:
            data: Données d'entrée (numpy array ou pandas Series)
            normalize: Si True, retourne les fréquences relatives
            **kwargs: Arguments additionnels
            
        Returns:
            DataFrame avec les fréquences
        """
        self.validate_data(data)
        
        if isinstance(data, pd.Series):
            series = data
        else:
            series = pd.Series(data)
        
        # Calcul des fréquences
        freq = series.value_counts(normalize=normalize)
        cum_freq = freq.cumsum()
        
        # Création du DataFrame de résultats
        self.result = pd.DataFrame({
            'Fréquence': freq,
            'Fréquence Cumulée': cum_freq
        })
        
        if normalize:
            self.result.columns = ['Fréquence Relative', 'Fréquence Relative Cumulée']
        
        return self.result
    
    def get_frequence_absolue(self):
        """Retourne les fréquences absolues."""
        if self.result is None:
            raise ValueError("Exécutez d'abord process()")
        return self.result['Fréquence']
    
    def get_frequence_cumulee(self):
        """Retourne les fréquences cumulées."""
        if self.result is None:
            raise ValueError("Exécutez d'abord process()")
        return self.result['Fréquence Cumulée']
    
    def get_frequence_relative(self):
        """Retourne les fréquences relatives."""
        if self.result is None:
            raise ValueError("Exécutez d'abord process()")
        # Check if already normalized
        if 'Fréquence Relative' in self.result.columns:
            return self.result['Fréquence Relative']
        # Normalize existing frequency counts instead of reprocessing
        freq_col = 'Fréquence' if 'Fréquence' in self.result.columns else self.result.columns[0]
        return self.result[freq_col] / self.result[freq_col].sum() 