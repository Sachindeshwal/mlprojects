# resposible for creating machine learning application as a package
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str)->List[str]:
    '''
    this function will return the liat of the requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name = "mlproject",
    version="0.0.1",
    author = "sachin",
    author_email = "deshwalsachin433@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)