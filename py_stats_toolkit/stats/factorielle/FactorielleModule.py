'''
=====================================================================
File : FactorielleModule.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module FactorielleModule.py

tags : module, stats
=====================================================================
Ce module Description du module FactorielleModule.py

tags : module, stats
=====================================================================
'''

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.preprocessing import StandardScaler
from ..core.AbstractClassBase import StatisticalModule
from ...utils.parallel import ParallelProcessor

class FactorielleModule(StatisticalModule):
    """Module pour l'analyse factorielle."""
    
    def __init__(self, n_jobs: int = -1):
        super().__init__()
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)
        self.scaler = StandardScaler()
    
    def process(self, data, method="pca", n_components=None, **kwargs):
        """
        Effectue une analyse factorielle.
        
        Args:
            data: DataFrame avec les données
            method: Méthode d'analyse ('pca', 'fa')
            n_components: Nombre de composantes à extraire
            **kwargs: Arguments additionnels
            
        Returns:
            Résultats de l'analyse
        """
        self.validate_data(data)
        
        # Standardisation des données
        X = self.scaler.fit_transform(data)
        
        if method == "pca":
            return self._pca(X, data.columns, n_components, **kwargs)
        elif method == "fa":
            return self._factor_analysis(X, data.columns, n_components, **kwargs)
        else:
            raise ValueError(f"Méthode {method} non supportée")
    
    def _pca(self, X, feature_names, n_components, **kwargs):
        """Analyse en composantes principales."""
        if n_components is None:
            n_components = min(X.shape)
        
        pca = PCA(n_components=n_components, **kwargs)
        pca.fit(X)
        
        # Calcul des composantes
        components = pca.transform(X)
        
        # Création du DataFrame des composantes
        components_df = pd.DataFrame(
            components,
            columns=[f'PC{i+1}' for i in range(n_components)]
        )
        
        # Calcul des contributions des variables
        loadings = pd.DataFrame(
            pca.components_.T,
            columns=[f'PC{i+1}' for i in range(n_components)],
            index=feature_names
        )
        
        self.result = {
            'Type': 'ACP',
            'Composantes': components_df,
            'Loadings': loadings,
            'Variance expliquée': pca.explained_variance_ratio_,
            'Variance cumulée': np.cumsum(pca.explained_variance_ratio_),
            'Modèle': pca
        }
        
        return self.result
    
    def _factor_analysis(self, X, feature_names, n_components, **kwargs):
        """Analyse factorielle."""
        if n_components is None:
            n_components = min(X.shape)
        
        fa = FactorAnalysis(n_components=n_components, **kwargs)
        fa.fit(X)
        
        # Calcul des facteurs
        factors = fa.transform(X)
        
        # Création du DataFrame des facteurs
        factors_df = pd.DataFrame(
            factors,
            columns=[f'F{i+1}' for i in range(n_components)]
        )
        
        # Calcul des contributions des variables
        loadings = pd.DataFrame(
            fa.components_.T,
            columns=[f'F{i+1}' for i in range(n_components)],
            index=feature_names
        )
        
        self.result = {
            'Type': 'Analyse factorielle',
            'Facteurs': factors_df,
            'Loadings': loadings,
            'Noise variance': fa.noise_variance_,
            'Modèle': fa
        }
        
        return self.result
    
    def get_quality_metrics(self):
        """
        Calcule les métriques de qualité de l'analyse.
        
        Returns:
            Métriques de qualité
        """
        if not hasattr(self, 'result'):
            raise ValueError("Aucune analyse n'a été effectuée")
        
        if self.result['Type'] == 'ACP':
            return {
                'Variance expliquée par composante': {
                    f'PC{i+1}': val 
                    for i, val in enumerate(self.result['Variance expliquée'])
                },
                'Variance cumulée': {
                    f'PC{i+1}': val 
                    for i, val in enumerate(self.result['Variance cumulée'])
                },
                'Nombre de composantes pour 80% de variance': np.argmax(
                    self.result['Variance cumulée'] >= 0.8
                ) + 1
            }
        else:
            return {
                'Variance du bruit': self.result['Noise variance'].tolist(),
                'Qualité de l\'ajustement': 1 - np.mean(self.result['Noise variance'])
            }
    
    def transform(self, new_data):
        """
        Transforme de nouvelles données.
        
        Args:
            new_data: Nouvelles données à transformer
            
        Returns:
            Données transformées
        """
        if not hasattr(self, 'result'):
            raise ValueError("Aucune analyse n'a été effectuée")
        
        # Standardisation des nouvelles données
        X_new = self.scaler.transform(new_data)
        
        # Transformation selon la méthode utilisée
        if self.result['Type'] == 'ACP':
            return pd.DataFrame(
                self.result['Modèle'].transform(X_new),
                columns=[f'PC{i+1}' for i in range(self.result['Modèle'].n_components_)]
            )
        else:
            return pd.DataFrame(
                self.result['Modèle'].transform(X_new),
                columns=[f'F{i+1}' for i in range(self.result['Modèle'].n_components_)]
            )
    
    def get_contributions(self, threshold=0.5):
        """
        Obtient les contributions significatives des variables.
        
        Args:
            threshold: Seuil de contribution
            
        Returns:
            Variables contribuant significativement à chaque composante/facteur
        """
        if not hasattr(self, 'result'):
            raise ValueError("Aucune analyse n'a été effectuée")
        
        loadings = self.result['Loadings']
        contributions = {}
        
        for col in loadings.columns:
            significant_vars = loadings[col][abs(loadings[col]) >= threshold]
            if not significant_vars.empty:
                contributions[col] = significant_vars.to_dict()
        
        return contributions 