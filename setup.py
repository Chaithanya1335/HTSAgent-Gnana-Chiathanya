from setuptools import setup,find_packages
from typing import List


def get_requirements(path:str)->List[str]:
    """
    This Function Takes path of requirements and returns list of requirements

    Args: Path:str

    Returns: Requirements:List(str)
    """
    with open(path,'r') as f:
        requirements = f.readlines()

    requirements = [requirement.replace("\n",'')
                        for requirement in requirements if requirement !='-e .']

    return requirements



setup(
    name='HTS_AGENT',
    version='1.0',
    author='M Gnana Chithanya',
    author_email='gnanachaithanyamangammagari@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)
