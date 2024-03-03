from setuptools import setup, find_namespace_packages

setup(
    name='Osobisty_asystent',
    version='1.0',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': [
            'personal-assistant = address_book.main:main'
        ]
    }
)