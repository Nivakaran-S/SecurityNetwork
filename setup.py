
'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools
(or for distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages, setup 
# this scans through all the folders and gets the folders that has the __init__ file
# setup is reponsible of providing all the information about the project

from typing import List

def get_requirements()->List[str]:
    """
    This function will return a list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## Ignore empty lines and -e .
                
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)



    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1", # This can be changed later
    author="Nivakaran S.",
    author_email="nivakaran@hotmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

