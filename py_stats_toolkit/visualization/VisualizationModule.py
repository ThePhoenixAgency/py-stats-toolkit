import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ..core.AbstractClassBase import StatisticalModule
from ..utils.parallel import ParallelProcessor

class VisualizationModule(StatisticalModule):
    """Module pour la visualisation des données statistiques."""
    
    def __init__(self, n_jobs: int = -1):
        super().__init__()
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)
        self.style = 'seaborn'
        plt.style.use(self.style)
    
    def process(self, data, plot_type="histogram", **kwargs):
        """
        Génère des visualisations statistiques.
        
        Args:
            data: Données à visualiser
            plot_type: Type de graphique
            **kwargs: Arguments additionnels
            
        Returns:
            Figure matplotlib
        """
        self.validate_data(data)
        
        if plot_type == "histogram":
            return self._plot_histogram(data, **kwargs)
        elif plot_type == "boxplot":
            return self._plot_boxplot(data, **kwargs)
        elif plot_type == "scatter":
            return self._plot_scatter(data, **kwargs)
        elif plot_type == "heatmap":
            return self._plot_heatmap(data, **kwargs)
        else:
            raise ValueError(f"Type de graphique {plot_type} non supporté")
    
    def _plot_histogram(self, data, bins=30, density=True, **kwargs):
        """Histogramme avec courbe de densité."""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if isinstance(data, pd.Series):
            sns.histplot(data=data, bins=bins, stat='density' if density else 'count', **kwargs)
            if density:
                sns.kdeplot(data=data, ax=ax, color='red')
        else:
            for col in data.columns:
                sns.histplot(data=data[col], bins=bins, stat='density' if density else 'count', 
                           label=col, alpha=0.5, **kwargs)
                if density:
                    sns.kdeplot(data=data[col], ax=ax, color='red', label=f'{col} (densité)')
        
        ax.set_title('Distribution des données')
        ax.set_xlabel('Valeurs')
        ax.set_ylabel('Densité' if density else 'Fréquence')
        if isinstance(data, pd.DataFrame):
            ax.legend()
        
        return fig
    
    def _plot_boxplot(self, data, **kwargs):
        """Boîte à moustaches."""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if isinstance(data, pd.Series):
            sns.boxplot(data=data, ax=ax, **kwargs)
        else:
            sns.boxplot(data=data, ax=ax, **kwargs)
        
        ax.set_title('Boîte à moustaches')
        ax.set_ylabel('Valeurs')
        
        return fig
    
    def _plot_scatter(self, data, x_col, y_col, hue=None, **kwargs):
        """Nuage de points."""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        sns.scatterplot(data=data, x=x_col, y=y_col, hue=hue, ax=ax, **kwargs)
        
        ax.set_title('Nuage de points')
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        
        return fig
    
    def _plot_heatmap(self, data, **kwargs):
        """Carte de chaleur."""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        if isinstance(data, pd.DataFrame):
            sns.heatmap(data, annot=True, cmap='coolwarm', ax=ax, **kwargs)
        else:
            sns.heatmap(data, annot=True, cmap='coolwarm', ax=ax, **kwargs)
        
        ax.set_title('Carte de chaleur')
        
        return fig
    
    def plot_time_series(self, data, time_col, value_col, group_col=None, **kwargs):
        """
        Visualisation de séries temporelles.
        
        Args:
            data: DataFrame avec les données
            time_col: Colonne des temps
            value_col: Colonne des valeurs
            group_col: Colonne des groupes (optionnelle)
            **kwargs: Arguments additionnels
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        if group_col is None:
            sns.lineplot(data=data, x=time_col, y=value_col, ax=ax, **kwargs)
        else:
            sns.lineplot(data=data, x=time_col, y=value_col, hue=group_col, ax=ax, **kwargs)
        
        ax.set_title('Série temporelle')
        ax.set_xlabel('Temps')
        ax.set_ylabel('Valeur')
        
        return fig
    
    def plot_correlation_matrix(self, data, **kwargs):
        """Matrice de corrélation."""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        corr_matrix = data.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax, **kwargs)
        
        ax.set_title('Matrice de corrélation')
        
        return fig
    
    def plot_survival_curves(self, survival_data, **kwargs):
        """
        Courbes de survie.
        
        Args:
            survival_data: Résultats de l'analyse de survie
            **kwargs: Arguments additionnels
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        for group, data in survival_data.items():
            data['Courbe de survie'].plot(ax=ax, label=group)
        
        ax.set_title('Courbes de survie')
        ax.set_xlabel('Temps')
        ax.set_ylabel('Probabilité de survie')
        ax.legend()
        
        return fig 