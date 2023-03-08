from setuptools import find_packages,setup
from typing import List
Const="-e."
def get_requirements(file_path:str)->List[str]:
    """
    This function return required packages to be istalled
    in form of list of string
    """
    requirements=[]

    with open(file_path) as obj:
        requirements=obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if Const in requirements:
            requirements.remove(Const)

    return requirements

setup(
    name="Signature-Verification",
    version='0.0.1',
    author="Pranay",
    author_email="pranaysaha61@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
