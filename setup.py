from setuptools import setup, find_packages

setup(
    name='py-stats-toolkit',
    version='1.0.1',
    description='Kit d\'outils statistiques avancés',
    author='ThePhoenixAgency',
    author_email='contact@phonxproject.onmicrosoft.com',
    url='https://github.com/ThePhoenixAgency/py-stats-toolkit',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20.0',
        'pandas>=1.3.0',
        'scipy>=1.7.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
        'statsmodels>=0.13.0',
        'scikit-learn>=1.0.0',
        'networkx>=2.6.0',
        'deap>=1.3.0',
    ],
)