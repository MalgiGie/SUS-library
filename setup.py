from setuptools import setup, find_packages

setup(
    name='sus_lib',  
    version='0.1',   
    packages=find_packages(include=['sus_lib']),
    install_requires=[
        'matplotlib',
        'numpy' 
    ],
    author='MalgiGie',
    python_requires='>=3.6'  
)
