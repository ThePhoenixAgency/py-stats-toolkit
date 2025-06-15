import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import numpy as np
from typing import Callable, List, Any, Union
import os

class ParallelProcessor:
    """Gestionnaire de traitement parallèle."""
    
    def __init__(self, n_jobs: int = -1, backend: str = 'process'):
        """
        Initialise le processeur parallèle.
        
        Args:
            n_jobs: Nombre de jobs (-1 pour utiliser tous les cœurs)
            backend: 'process' pour multiprocessing, 'thread' pour multithreading
        """
        self.n_jobs = mp.cpu_count() if n_jobs == -1 else n_jobs
        self.backend = backend
        self.executor = ProcessPoolExecutor if backend == 'process' else ThreadPoolExecutor
    
    def parallel_map(self, func: Callable, data: List[Any], chunksize: int = 1) -> List[Any]:
        """
        Applique une fonction en parallèle sur une liste de données.
        
        Args:
            func: Fonction à appliquer
            data: Liste de données à traiter
            chunksize: Taille des chunks pour le traitement
            
        Returns:
            Liste des résultats
        """
        with self.executor(max_workers=self.n_jobs) as executor:
            return list(executor.map(func, data, chunksize=chunksize))
    
    def parallel_apply(self, func: Callable, data: np.ndarray, axis: int = 0) -> np.ndarray:
        """
        Applique une fonction en parallèle sur un tableau numpy.
        
        Args:
            func: Fonction à appliquer
            data: Tableau numpy à traiter
            axis: Axe sur lequel appliquer la fonction
            
        Returns:
            Tableau numpy des résultats
        """
        if axis == 0:
            chunks = np.array_split(data, self.n_jobs)
        else:
            chunks = np.array_split(data.T, self.n_jobs)
            chunks = [chunk.T for chunk in chunks]
        
        results = self.parallel_map(func, chunks)
        return np.concatenate(results, axis=axis)

class BatchProcessor:
    """Gestionnaire de traitement par lots."""
    
    def __init__(self, batch_size: int = 1000):
        """
        Initialise le processeur par lots.
        
        Args:
            batch_size: Taille des lots
        """
        self.batch_size = batch_size
    
    def process_batches(self, func: Callable, data: np.ndarray) -> np.ndarray:
        """
        Traite les données par lots.
        
        Args:
            func: Fonction à appliquer
            data: Données à traiter
            
        Returns:
            Résultats du traitement
        """
        n_samples = len(data)
        results = []
        
        for i in range(0, n_samples, self.batch_size):
            batch = data[i:min(i + self.batch_size, n_samples)]
            results.append(func(batch))
        
        return np.concatenate(results)

def get_optimal_chunk_size(data_size: int, n_jobs: int = -1) -> int:
    """
    Calcule la taille optimale des chunks pour le traitement parallèle.
    
    Args:
        data_size: Taille des données
        n_jobs: Nombre de jobs
        
    Returns:
        Taille optimale des chunks
    """
    if n_jobs == -1:
        n_jobs = mp.cpu_count()
    
    # Règle empirique : environ 100 chunks par job
    return max(1, data_size // (n_jobs * 100)) 