
import pandas as pd

class DataProcessor:
    def __init__(self, game, file_path):
        from core.rules import GameRules
        self.rules = GameRules.get(game)
        self.file_path = file_path

    def load_and_process_data(self):
        df = pd.read_csv(self.file_path, sep=';', parse_dates=['date_de_tirage'])
        num_cols = self.rules['csv_columns']['numeros']
        star_cols = self.rules['csv_columns']['etoiles']
        df['numeros'] = df[num_cols].values.tolist()
        df['etoiles'] = df[star_cols].values.tolist()
        df['payouts'] = [{} for _ in range(len(df))]
        return df[['date_de_tirage', 'numeros', 'etoiles', 'payouts']]
