import numpy as np
import pandas as pd
from scipy import stats
from ..core.AbstractClassBase import StatisticalModule
from ...utils.parallel import ParallelProcessor, get_optimal_chunk_size

class CorrelationModule(StatisticalModule):
    """Module pour l'analyse de corrélation."""
    
    def __init__(self, n_jobs: int = -1):
        super().__init__()
        self.method = None
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)
    
    def _compute_correlation_chunk(self, chunk_data):
        """Calcule la corrélation pour un chunk de données."""
        return chunk_data.corr(method=self.method)
    
    def process(self, data, method="pearson", **kwargs):
        """
        Calcule la corrélation entre les variables en parallèle.
        
        Args:
            data: Données d'entrée (pandas DataFrame)
            method: Méthode de corrélation ('pearson', 'spearman', 'kendall')
            **kwargs: Arguments additionnels
            
        Returns:
            Matrice de corrélation
        """
        self.validate_data(data)
        self.method = method
        
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Les données doivent être un pandas DataFrame")
        
        # Pour les petits DataFrames, calcul direct
        if len(data.columns) < 100:
            self.result = data.corr(method=method)
            return self.result
        
        # Pour les grands DataFrames, traitement parallèle
        n_cols = len(data.columns)
        chunk_size = get_optimal_chunk_size(n_cols, self.parallel_processor.n_jobs)
        
        # Division des colonnes en chunks
        chunks = []
        for i in range(0, n_cols, chunk_size):
            chunk_cols = data.columns[i:min(i + chunk_size, n_cols)]
            chunks.append(data[chunk_cols])
        
        # Calcul parallèle des corrélations
        chunk_results = self.parallel_processor.parallel_map(
            self._compute_correlation_chunk,
            chunks
        )
        
        # Assemblage des résultats
        self.result = pd.concat(chunk_results, axis=1)
        return self.result
    
    def get_correlation_matrix(self):
        """Retourne la matrice de corrélation."""
        return self.result
    
    def get_correlation_pairs(self, threshold=0.5):
        """
        Retourne les paires de variables avec une corrélation supérieure au seuil.
        
        Args:
            threshold: Seuil de corrélation
            
        Returns:
            Liste de tuples (var1, var2, corr)
        """
        if self.result is None:
            raise ValueError("Exécutez d'abord process()")
        
        # Utilisation de numpy pour le calcul parallèle des paires
        corr_matrix = self.result.values
        n = len(self.result.columns)
        
        # Création des indices pour les paires
        i, j = np.triu_indices(n, k=1)
        corr_values = corr_matrix[i, j]
        
        # Filtrage des paires selon le seuil
        mask = np.abs(corr_values) >= threshold
        pairs = []
        
        for idx in np.where(mask)[0]:
            var1 = self.result.columns[i[idx]]
            var2 = self.result.columns[j[idx]]
            corr = corr_values[idx]
            pairs.append((var1, var2, corr))
        
        return sorted(pairs, key=lambda x: abs(x[2]), reverse=True) 