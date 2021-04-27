from setuptools import setup

setup(
    name="eks",
    version='0.1',
    py_modules=['eks'],
    install_requires=[
        'Click',
        'pyyaml',
        'Jinja2',
        'configparser',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        eks=eks:cli
    ''',
)