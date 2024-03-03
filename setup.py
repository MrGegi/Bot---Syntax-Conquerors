from setuptools import setup

setup(
    name='Osobisty_asystent',
    version='1.0',
    packages=['address_book'],
    entry_points={
        'console_scripts': [
            'personal-assistant = address_book.main:main'
        ]
    }
)