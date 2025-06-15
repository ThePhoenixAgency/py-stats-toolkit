'''
=====================================================================
File : setup.py
=====================================================================
version : 1.0.0
release : 15/06/2025
author : Phoenix Project
contact : contact@phonxproject.onmicrosoft.fr
license : MIT
=====================================================================
Copyright (c) 2025, Phoenix Project
All rights reserved.

Description du module setup.py

tags : module, setup
=====================================================================
Ce module contient la configuration du package.

tags : module, setup
=====================================================================
'''

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="py-stats-toolkit",
    version="1.0.0",
    author="Phoenix Project",
    author_email="contact@phonxproject.onmicrosoft.fr",
    description="Kit d'outils statistiques en Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phoenixproject/py-stats-toolkit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Statistics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=1.0.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "flake8>=4.0.0",
            "mypy>=0.900",
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0"
        ]
    },
    project_urls={
        "Bug Tracker": "https://github.com/phoenixproject/py-stats-toolkit/issues",
        "Documentation": "https://py-stats-toolkit.readthedocs.io/",
        "Source Code": "https://github.com/phoenixproject/py-stats-toolkit"
    }
) 