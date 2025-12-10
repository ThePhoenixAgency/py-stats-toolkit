'''
=====================================================================
File : MoyenneGlissanteModule.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module MoyenneGlissanteModule.py

tags : module, stats
=====================================================================
Ce module Description du module MoyenneGlissanteModule.py

tags : module, stats
=====================================================================
'''

import numpy as np
import pandas as pd
from ..core.AbstractClassBase import StatisticalModule
from ...utils.parallel import ParallelProcessor

class MoyenneGlissanteModule(StatisticalModule):
    """Module pour le calcul de la moyenne glissante."""
    
    def __init__(self, n_jobs: int = -1, batch_size: int = 1000):
        super().__init__()
        self.window_size = None
        self.batch_size = batch_size
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)
    
    def _process_chunk(self, chunk):
        """Traite un chunk de données."""
        return pd.Series(chunk).rolling(window=self.window_size).mean()
    
    def process(self, data, window_size=5, **kwargs):
        """
        Calcule la moyenne glissante sur les données en parallèle.
        
        Args:
            data: Données d'entrée (numpy array ou pandas Series)
            window_size: Taille de la fenêtre glissante
            **kwargs: Arguments additionnels
            
        Returns:
            Moyenne glissante calculée
        """
        self.validate_data(data)
        self.window_size = window_size
        
        if isinstance(data, pd.Series):
            data_array = data.values
        else:
            data_array = data
        
        # Simple rolling mean calculation for all data
        if isinstance(data, pd.Series):
            result = data.rolling(window=window_size).mean()
        else:
            result = pd.Series(data_array).rolling(window=window_size).mean()
        
        if isinstance(data, pd.Series):
            self.result = pd.Series(result, index=data.index)
        else:
            self.result = pd.Series(result)
        
        return self.result
    
    def get_window_size(self):
        """Retourne la taille de la fenêtre utilisée."""
        return self.window_size 