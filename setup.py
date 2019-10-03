from setuptools import setup, find_packages

from .conpygure.__version__ import __version__

setup(
    name='conpygure',
    version=__version__,
    packages=find_packages(exclude=('src', 'src.*', '*.src', '*.src.*')),
    author='Luca Soato',
    author_email='info@lucasoato.it',
    description='A library to con*py*gure little projects :) ',
    install_requires=['toml'],
    url="https://github.com/LucaSoato/conpygure"
)
