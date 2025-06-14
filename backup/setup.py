from setuptools import setup, find_packages

setup(
    name="genetic_lottery_optimizer",
    version="1.0.0",
    description="Optimiseur génétique pour grilles de loterie avec modules statistiques avancés",
    author="VotreNom",
    packages=find_packages(where='.'),
    include_package_data=True,
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "tqdm"
    ],
    entry_points={
        'console_scripts': [
            'loto-gui=interface.genetic_optimizer_gui:main',
            'loto-train=moteur.trainer:main',
            'loto-test=interface.test_optimizer:main',
        ]
    },
    python_requires='>=3.7'
)