from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
   
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="sensor",
    version="0.0.1",
    author="kanwal",
    author_email="kanwalarora@live.com",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)