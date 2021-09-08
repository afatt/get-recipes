import sys
from setuptools import setup, find_packages

__version__ = '1.0.0'

REQUIRES = [
    'Pillow==8.3.2',
    'pypng==0.0.20',
    'pyzbar==0.1.8',
    'selenium==3.141.0',
    'urllib3==1.25.9'
]

setup(
    name='Get Recipes',
    author='Austin Fatt',
    author_email='afatt90@gmail.com',
    url='https://github.com/afatt/get-recipes',
    version=__version__,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='Trader',
    packages=find_packages(),
    install_requires=REQUIRES
)
