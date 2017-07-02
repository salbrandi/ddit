from setuptools import setup

setup(
    name='DDIT',
    version='0.0.1',
    py_modules=['diceroller', 'chcreator'],
    install_requires=['Click', 'pandas'],
    entry_points='''
        [console_scripts]
        roll=diceroller:roll
        fumble=diceroller:p_fumble
        ''',

)
