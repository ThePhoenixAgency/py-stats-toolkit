
class GameRules:
    rules = {
        'euromillions': {
            'days': [1, 4],
            'main_numbers': 5, 'main_range': (1, 50),
            'stars': 2, 'stars_range': (1, 12),
            'star_name': 'etoile',
            'csv_columns': {
                'numeros': ['boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5'],
                'etoiles': ['etoile_1', 'etoile_2']
            }
        }
    }

    @classmethod
    def get(cls, game): return cls.rules.get(game, {})
