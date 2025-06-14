import os
import json
from datetime import datetime, timedelta
from utils.trainer import train_model

def check_and_schedule_training(game, file_path, last_run_file='last_run.txt'):
    if os.path.exists(last_run_file):
        with open(last_run_file, 'r') as f:
            last_run_date = datetime.strptime(f.read().strip(), '%Y-%m-%d')
    else:
        last_run_date = datetime.min

    next_run_date = last_run_date + timedelta(days=7)
    today = datetime.now()

    if today >= next_run_date:
        results, error = train_model(game, file_path)
        if error:
            return f"Erreur : {error}"
        with open(last_run_file, 'w') as f:
            f.write(today.strftime('%Y-%m-%d'))
        return f"Entraînement lancé. Stratégie : {results['fichier_stratégie']}"
    return f"Prochain entraînement : {next_run_date.strftime('%Y-%m-%d')}"

def plot_module_weights_evolution(folder_path):
    import matplotlib.pyplot as plt
    from os import listdir
    files = sorted(f for f in listdir(folder_path) if f.endswith('.json'))
    import json

    history = {}
    dates = []

    for f in files:
        date = f.split('_')[-1].split('.')[0]
        dates.append(datetime.strptime(date, '%Y%m%d'))
        with open(os.path.join(folder_path, f)) as jf:
            data = json.load(jf)
        for key, val in data.items():
            if key not in history:
                history[key] = []
            history[key].append(val)

    for mod, vals in history.items():
        plt.plot(dates, vals, label=mod)
    plt.legend()
    plt.title("Évolution des poids")
    plt.xlabel("Date")
    plt.ylabel("Poids")
    plt.grid(True)
    plt.tight_layout()
    plt.show()