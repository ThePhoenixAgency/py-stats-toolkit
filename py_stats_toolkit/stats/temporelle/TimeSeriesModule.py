"""
=====================================================================
File : TimeSeriesModule.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module TimeSeriesModule.py

tags : module, stats
=====================================================================
Ce module Description du module TimeSeriesModule.py

tags : module, stats
=====================================================================
"""

import numpy as np
import pandas as pd

from ...utils.parallel import ParallelProcessor
from ..core.AbstractClassBase import StatisticalModule


class TimeSeriesAnalyzer(StatisticalModule):
    """Module pour l'analyse de séries temporelles."""

    def __init__(self, n_jobs: int = -1, batch_size: int = 1000):
        super().__init__()
        self.batch_size = batch_size
        self.parallel_processor = ParallelProcessor(n_jobs=n_jobs)

    def process(self, data, timestamps=None, **kwargs):
        """
        Analyse une série temporelle.

        Args:
            data: Données d'entrée (numpy array ou pandas Series)
            timestamps: Timestamps pour les données
            **kwargs: Arguments additionnels

        Returns:
            DataFrame avec les analyses
        """
        self.validate_data(data)

        if timestamps is not None:
            self.set_timestamps(timestamps)

        if isinstance(data, pd.Series):
            series = data
        else:
            series = pd.Series(data, index=self.timestamps)

        # Calcul des statistiques de base
        stats = {
            "Moyenne": series.mean(),
            "Écart-type": series.std(),
            "Minimum": series.min(),
            "Maximum": series.max(),
            "Médiane": series.median(),
        }

        # Détection des tendances
        if len(series) > 1:
            x = np.arange(len(series))
            slope, intercept = np.polyfit(x, series.to_numpy(), 1)
            stats["Pente"] = slope
            stats["Intercept"] = intercept

        # Détection des cycles
        if len(series) > 2:
            # Compute FFT only on the positive frequencies to save computation
            fft = np.fft.rfft(
                series.to_numpy()
            )  # rfft is more efficient for real-valued data
            freqs = np.fft.rfftfreq(len(series))
            # Skip DC component (index 0)
            main_freq_idx = np.argmax(np.abs(fft[1:])) + 1
            stats["Fréquence Principale"] = freqs[main_freq_idx]
            stats["Période Principale"] = (
                1 / freqs[main_freq_idx] if freqs[main_freq_idx] != 0 else np.inf
            )

        self.result = pd.Series(stats)
        return self.result

    def get_trend(self, data=None):
        """
        Calcule la tendance linéaire.

        Args:
            data: Données optionnelles (utilise self.data si None)

        Returns:
            Tuple (pente, intercept)
        """
        if data is None:
            data = self.data

        if isinstance(data, pd.Series):
            series = data
        else:
            series = pd.Series(data)

        x = np.arange(len(series))
        return np.polyfit(x, series.to_numpy(), 1)

    def get_seasonality(self, data=None, period=None):
        """
        Détecte la saisonnalité.

        Args:
            data: Données optionnelles
            period: Période attendue (optionnelle)

        Returns:
            Période détectée
        """
        if data is None:
            data = self.data

        if isinstance(data, pd.Series):
            series = data
        else:
            series = pd.Series(data)

        # Calcul de l'autocorrélation
        acf = pd.Series(series).autocorr()

        if period is not None:
            return period

        # Détection automatique de la période - use rfft for efficiency
        fft = np.fft.rfft(
            series.to_numpy()
        )  # rfft is more efficient for real-valued data
        freqs = np.fft.rfftfreq(len(series))
        main_freq_idx = np.argmax(np.abs(fft[1:])) + 1
        return 1 / freqs[main_freq_idx] if freqs[main_freq_idx] != 0 else np.inf
