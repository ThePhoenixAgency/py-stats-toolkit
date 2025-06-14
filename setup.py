from setuptools import setup, find_packages

setup(
    name="genetic_lottery_optimizer",
    version="1.0.0",
    description="Optimiseur génétique pour grilles de loterie avec modules statistiques avancés",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="VotreNom",
    author_email="votre.email@example.com",
    url="https://github.com/votre-username/genetic_lottery_optimizer",
    packages=find_packages(where='.'),
    include_package_data=True,
    package_data={
        'genetic_lottery_optimizer': [
            'data/*.json',
            'gui/resources/*',
        ],
    },
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
        "matplotlib>=3.4.0",
        "tqdm>=4.62.0",
        "scipy>=1.7.0",
        "scikit-learn>=0.24.0",
        "PyQt5>=5.15.0"
    ],
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'pytest-cov>=2.12.0',
            'black>=21.5b2',
            'flake8>=3.9.0'
        ],
        'gui': [
            'PyQt5>=5.15.0',
            'matplotlib>=3.4.0'
        ],
        'ml': [
            'scikit-learn>=0.24.0',
            'scipy>=1.7.0'
        ]
    },
    entry_points={
        'console_scripts': [
            'loto-gui=genetic_lottery_optimizer.gui.genetic_optimizer_gui:main',
            'loto-train=genetic_lottery_optimizer.core.trainer:main',
            'loto-test=genetic_lottery_optimizer.gui.test_optimizer:main',
            'loto-predict=genetic_lottery_optimizer.core.prediction_engine:main',
            'loto-run=genetic_lottery_optimizer.run_project:main'
        ]
    },
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Statistics'
    ],
    keywords='lottery, genetic algorithm, optimization, statistics, prediction',
    project_urls={
        'Documentation': 'https://github.com/votre-username/genetic_lottery_optimizer/docs',
        'Source': 'https://github.com/votre-username/genetic_lottery_optimizer',
        'Tracker': 'https://github.com/votre-username/genetic_lottery_optimizer/issues',
    }
)