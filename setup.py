# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="py_stats_toolkit",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "scikit-learn>=0.24.0",
        "seaborn>=0.11.0",
        "matplotlib>=3.4.0",
        "scipy>=1.7.0",
        "lifelines>=0.26.0",
        "joblib>=1.0.0",
        "statsmodels>=0.13.0",
        "ephem>=4.1.0"
    ],
    author="Phoenix Project",
    author_email="contact@phonxproject.onmicrosoft.com",
    description="Une boîte à outils complète pour l'analyse statistique en Python",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PhoenixGuardianTools/py-stats-toolkit",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
) 