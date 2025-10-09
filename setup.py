# setup.py
from setuptools import setup, find_packages

setup(
    name='north_diagnostics',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',   # Add more dependencies if you need
    ],
    include_package_data=True,
    zip_safe=False
)
