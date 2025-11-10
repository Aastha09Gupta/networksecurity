'''
This setup.py file is an essential part of packaging
distributing Python projects. IT is used by setuptools
(or disutils in older python versions) to define the configuration
of your projects, such as metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

requirements_lst:List[str]=[]

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    try:
        with open('requirements.txt','r') as file:
            ##Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirements=line.strip()
                ## ignore empty lines and -e.
                if requirements and requirements!='-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("Reqiurements.txt file is not found.")

    return requirements_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Aastha Gupta",
    author_email="ag3162517@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
