"""
Serveur FastAPI pour Py-Stats-Toolkit
====================================

Ce module implémente un serveur API REST pour Py-Stats-Toolkit.
Il expose les fonctionnalités de la bibliothèque via des endpoints HTTP.

Tags:
    - server
    - api
    - fastapi
    - rest
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from typing import Dict, List, Optional, Union
import numpy as np
import pandas as pd

# Import des modules de py_stats_toolkit
from py_stats_toolkit import (
    StatisticalModule,
    TimeSeriesModule,
    RegressionModule,
    TestModule,
    VisualizationModule,
    GameTheoryModule,
    FractalModule,
    MarkovChainModule,
    AdvancedTimeSeriesModule,
    NetworkAnalysisModule,
    GeneticAlgorithmModule
)

# Initialisation de l'application FastAPI
app = FastAPI(
    title="Py-Stats-Toolkit API",
    description="API REST pour Py-Stats-Toolkit - Une bibliothèque d'analyse statistique avancée",
    version="0.1.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèles Pydantic pour la validation des données
class DataInput(BaseModel):
    """Modèle pour les données d'entrée."""
    data: List[float]
    method: str
    params: Optional[Dict] = None

class AnalysisResult(BaseModel):
    """Modèle pour les résultats d'analyse."""
    result: Dict
    status: str
    message: Optional[str] = None

# Routes API
@app.get("/")
async def root():
    """Route racine de l'API."""
    return {
        "message": "Bienvenue sur l'API Py-Stats-Toolkit",
        "version": "0.1.0",
        "documentation": "/docs"
    }

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_data(data_input: DataInput):
    """
    Endpoint pour l'analyse statistique.
    
    Args:
        data_input (DataInput): Données d'entrée et paramètres d'analyse
        
    Returns:
        AnalysisResult: Résultats de l'analyse
    """
    try:
        # Conversion des données en numpy array
        data = np.array(data_input.data)
        
        # Sélection du module approprié
        if data_input.method == "statistical":
            module = StatisticalModule()
        elif data_input.method == "timeseries":
            module = TimeSeriesModule()
        elif data_input.method == "regression":
            module = RegressionModule()
        elif data_input.method == "test":
            module = TestModule()
        elif data_input.method == "visualization":
            module = VisualizationModule()
        elif data_input.method == "gametheory":
            module = GameTheoryModule()
        elif data_input.method == "fractal":
            module = FractalModule()
        elif data_input.method == "markovchain":
            module = MarkovChainModule()
        elif data_input.method == "advancedtimeseries":
            module = AdvancedTimeSeriesModule()
        elif data_input.method == "networkanalysis":
            module = NetworkAnalysisModule()
        elif data_input.method == "geneticalgorithm":
            module = GeneticAlgorithmModule()
        else:
            raise HTTPException(status_code=400, detail="Méthode d'analyse non supportée")
        
        # Exécution de l'analyse
        result = module.process(data, **data_input.params or {})
        
        return AnalysisResult(
            result=result,
            status="success",
            message="Analyse terminée avec succès"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Vérification de l'état du serveur."""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 