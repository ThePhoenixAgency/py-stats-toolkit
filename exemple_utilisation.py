"""
Exemple d'utilisation des modules de genetic_lottery_optimizer dans un nouveau projet
"""

from genetic_lottery_optimizer import (
    FrequenceAbsolueModule,
    EntropieShannonModule,
    DistributionEmpiriqueModule,
    trainer
)

def analyser_donnees(data):
    """Exemple d'utilisation des modules statistiques"""
    # Initialisation des modules
    freq_module = FrequenceAbsolueModule()
    entropie_module = EntropieShannonModule()
    distrib_module = DistributionEmpiriqueModule()
    
    # Calcul des scores
    scores_freq = freq_module.get_entity_scores(data, {})
    scores_entropie = entropie_module.get_entity_scores(data, {})
    scores_distrib = distrib_module.get_entity_scores(data, {})
    
    return {
        'frequence': scores_freq,
        'entropie': scores_entropie,
        'distribution': scores_distrib
    }

def entrainer_modele(data, config):
    """Exemple d'utilisation du trainer"""
    # Configuration de l'entraînement
    resultats = trainer.train_model(
        data=data,
        config=config,
        save_path='resultats_entrainement.json'
    )
    return resultats

if __name__ == '__main__':
    # Exemple de données
    donnees_test = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        # ... autres données
    ]
    
    # Configuration
    config = {
        'population_size': 100,
        'generations': 50,
        'mutation_rate': 0.1
    }
    
    # Utilisation des fonctions
    resultats_analyse = analyser_donnees(donnees_test)
    resultats_entrainement = entrainer_modele(donnees_test, config)
    
    print("Résultats de l'analyse:", resultats_analyse)
    print("Résultats de l'entraînement:", resultats_entrainement) 