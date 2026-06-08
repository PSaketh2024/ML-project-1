from setuptools import find_packages,setup
from typing import List


def get_requriements(path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requriement = []
    HYPEN_E_DOT  =  "-e ."
    with open(path) as file_obj:
        requirement = file_obj.readlines()
        requirement =  [req.replace("\n","") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    return requirement

        
setup(
name = "ml-project-1",
version = "0.0.1",
author = "Saketh",
author_email = "sakethpatki1@gmail.com",
packages=find_packages(),
install_requires = get_requriements("requirements.txt")



)