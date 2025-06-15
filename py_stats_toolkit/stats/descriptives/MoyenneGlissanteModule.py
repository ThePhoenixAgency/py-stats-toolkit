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

# Imports spécifiques au module
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

# Imports de la base
from capsules.BaseCapsule import BaseCapsule

class MoyenneGlissanteModule(BaseCapsule):
    """
    Classe MoyenneGlissanteModule
    
    Attributes:
        data, parameters, results
    """
    
    def __init__(self):
        """
        Initialise MoyenneGlissanteModule.
        """
        super().__init__()
        pass
    
    def configure(self, **kwargs) -> None:
        """
        Configure les paramètres de MoyenneGlissanteModule.
        
        Args:
            **kwargs: Paramètres de configuration
        """
        pass
    
    def process(self, data: Union[pd.DataFrame, pd.Series], **kwargs) -> Dict[str, Any]:
        """
        Exécute le flux de travail d'analyse.
        
        Args:
            data (Union[pd.DataFrame, pd.Series]): Données à analyser
            **kwargs: Arguments additionnels
            
        Returns:
            Dict[str, Any]: Résultats de l'analyse
        """
        pass 

import numpy as np
import pandas as pd
from ..core.AbstractClassBase import StatisticalModule
from ...utils.parallel import ParallelProcessor, BatchProcessor

class MoyenneGlissanteModule(StatisticalModule):
    """Module pour le calcul de la moyenne glissante."""
    
    def __init__(self, n_jobs: int = -1, batch_size: int = 1000):
        super().__init__()
        self.window_size = None
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)
        self.batch_processor = BatchProcessor(batch_size=batch_size)
    
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
        
        # Utilisation du traitement par lots pour les grandes séries
        if len(data_array) > self.batch_processor.batch_size:
            result = self.batch_processor.process_batches(self._process_chunk, data_array)
        else:
            # Traitement parallèle pour les séries plus petites
            result = self.parallel_processor.parallel_apply(
                self._process_chunk,
                data_array.reshape(-1, 1),
                axis=0
            ).flatten()
        
        if isinstance(data, pd.Series):
            self.result = pd.Series(result, index=data.index)
        else:
            self.result = pd.Series(result)
        
        return self.result
    
    def get_window_size(self):
        """Retourne la taille de la fenêtre utilisée."""
        return self.window_size 