from setuptools import setup, find_packages

#from my_pip_package import __version__


setup(
    name='TPC_Converters',
    version="1.0.0",#__version__,

    url='https://github.com/Themadhood/Converters',
    author='Themadhood Pequot',
    author_email='themadhoodpequot@gmail.com',

    packages=find_packages(),

    install_requires=[
        "pygame",#a platform for making games : mixer is only modual used
        ],

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
