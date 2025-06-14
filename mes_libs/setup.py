from setuptools import setup, find_packages

setup(
    name="mes_libs",
    version="0.1.0",
    description="Bibliothèques Python personnelles",
    author="VotreNom",
    author_email="votre.email@example.com",
    url="https://github.com/votre-username/mes_libs",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
        "matplotlib>=3.4.0",
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
        ]
    },
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
) 